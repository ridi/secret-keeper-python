import os
import random
import string
import unittest
try:
    from StringIO import StringIO   # for Python2 support
except ImportError:
    from io import StringIO

from ridi.secret_keeper import tell, tell_safe
from ridi.secret_keeper.cmdline import run

try:
    from unittest import mock
except ImportError:
    import mock

from botocore.exceptions import ClientError


class FakeClient(object):
    def __init__(self, dict):
        self._dict = dict

    def get_parameter(self, Name, WithDecryption):
        assert WithDecryption is True
        if Name in self._dict:
            return {
                'Parameter': {
                    'Name': Name,
                    'Type': "SecureString",
                    'Value': self._dict[Name],
                }
            }
        else:
            error_response = {
                'Error': {
                    'Code': "ParameterNotFound",
                },
            }
            raise ClientError(error_response, operation_name="GetParameter")


class TestSecretKeeperBase(unittest.TestCase):
    def setUp(self):
        _client = FakeClient({
            "ones": "11111",
        })
        self._patcher = mock.patch('boto3.client', return_value=_client)
        self._patcher.start()

    def tearDown(self):
        self._patcher.stop()


class TestSecretKeeperTell(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(tell("ones"), "11111")

    def test_non_existing_keys(self):
        with self.assertRaises(ClientError):
            tell("twos")


class TestSecretKeeperTellSafe(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(tell_safe("ones"), "11111")

    def test_non_existing_keys(self):
        self.assertEqual(tell_safe("twos"), None)


class TestSecretKeeperCLI(TestSecretKeeperBase):
    def test_success_stdout(self):
        with mock.patch('sys.stdout', new=StringIO()) as fake_stdout:
            retval = run(["ones"])
            output = fake_stdout.getvalue().strip()
            self.assertEqual(output, "11111")
            self.assertEqual(retval, 0)

    def test_success_file(self):
        outfile = "tmp." + "".join(random.choice(string.ascii_letters) for _ in range(10))
        if os.path.exists(outfile):
            os.remove(outfile)

        retval = run(["ones", "--outfile", outfile])

        with open(outfile, "r") as f:
            content = f.read().strip()

        if os.path.exists(outfile):
            os.remove(outfile)

        self.assertEqual(content, "11111")
        self.assertEqual(retval, 0)

    def test_fail_stderr(self):
        with mock.patch('sys.stderr', new=StringIO()) as fake_stderr:
            retval = run(["twos"])
            output = fake_stderr.getvalue().strip()
            self.assertIn("Secret of alias 'twos' is not found.", output)
            self.assertEqual(retval, 1)
