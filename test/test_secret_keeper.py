import os
import unittest

from ridi.secret_keeper import tell, tell_safe, ENVNAME_AWS_ACCESS_KEY, ENVNAME_AWS_SECRET_KEY, ENVNAME_AWS_REGION

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
        os.environ[ENVNAME_AWS_ACCESS_KEY] = "access_key"
        os.environ[ENVNAME_AWS_SECRET_KEY] = "secret_key"
        os.environ[ENVNAME_AWS_REGION] = "us-east-1"

        _client = FakeClient({
            "ones": "11111",
        })
        self._patcher = mock.patch('boto3.client', return_value=_client)
        self._patcher.start()

    def tearDown(self):
        self._patcher.stop()


class TestSecretKeeperGet(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(tell("ones"), "11111")

    def test_non_existing_keys(self):
        with self.assertRaises(ClientError):
            tell("twos")


class TestSecretKeeperGetSafe(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(tell_safe("ones"), "11111")

    def test_non_existing_keys(self):
        self.assertEqual(tell_safe("twos"), None)
