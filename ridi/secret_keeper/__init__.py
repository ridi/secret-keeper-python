import os

import boto3

ENVNAME_AWS_ACCESS_KEY = "SECRETKEEPER_AWS_ACCESS_KEY"
ENVNAME_AWS_SECRET_KEY = "SECRETKEEPER_AWS_SECRET_KEY"
ENVNAME_AWS_REGION = "SECRETKEEPER_AWS_REGION"


def _get_client():
    access_key = os.environ[ENVNAME_AWS_ACCESS_KEY]
    secret_key = os.environ[ENVNAME_AWS_SECRET_KEY]
    region = os.environ[ENVNAME_AWS_REGION]

    client = boto3.client(
        'ssm',
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    return client


def tell(alias):
    response = _get_client().get_parameter(
        Name=alias, WithDecryption=True,
    )
    return response['Parameter']['Value']


def tell_safe(alias):
    try:
        return tell(alias)
    except Exception:
        return None


__all__ = ["tell", "tell_safe", "ENVNAME_AWS_ACCESS_KEY", "ENVNAME_AWS_SECRET_KEY", "ENVNAME_AWS_REGION"]
