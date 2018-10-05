import unittest
try:
    from unittest import mock
except ImportError:
    import mock

from botocore.exceptions import ClientError

from ridi import secret_keeper


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
        self._patcher = mock.patch('ridi.secret_keeper._get_client', return_value=_client)
        self._patcher.start()

    def tearDown(self):
        self._patcher.stop()


class TestSecretKeeperGet(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(secret_keeper.tell("ones"), "11111")

    def test_non_existing_keys(self):
        with self.assertRaises(ClientError):
            secret_keeper.tell("twos")


class TestSecretKeeperGetSafe(TestSecretKeeperBase):
    def test_existing_keys(self):
        self.assertEqual(secret_keeper.tell_safe("ones"), "11111")

    def test_non_existing_keys(self):
        self.assertEqual(secret_keeper.tell_safe("twos"), None)
