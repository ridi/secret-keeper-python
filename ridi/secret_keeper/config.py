import os

from collections import namedtuple

ENVNAME_AWS_ACCESS_KEY = "SECRETKEEPER_AWS_ACCESS_KEY"
ENVNAME_AWS_SECRET_KEY = "SECRETKEEPER_AWS_SECRET_KEY"
ENVNAME_AWS_REGION = "SECRETKEEPER_AWS_REGION"
ENVNAME_AWS_SESSION_TOKEN = "SECRETKEEPER_AWS_SESSION_TOKEN"

ConnectArgsType = namedtuple('ConnectArgsType', [
    'aws_access_key', 'aws_secret_key', 'aws_region', 'aws_session_token'
])

AWS_CONNECT_ARGS = None


def configure(aws_access_key=None, aws_secret_key=None, aws_region=None, aws_session_token=None):
    global AWS_CONNECT_ARGS
    AWS_CONNECT_ARGS = ConnectArgsType(
        aws_access_key=aws_access_key,
        aws_secret_key=aws_secret_key,
        aws_region=aws_region,
        aws_session_token=aws_session_token,
    )


configure(
    aws_access_key=os.environ.get(ENVNAME_AWS_ACCESS_KEY),
    aws_secret_key=os.environ.get(ENVNAME_AWS_SECRET_KEY),
    aws_region=os.environ.get(ENVNAME_AWS_REGION),
    aws_session_token=os.environ.get(ENVNAME_AWS_SESSION_TOKEN),

)

__all__ = ["configure", "ENVNAME_AWS_ACCESS_KEY", "ENVNAME_AWS_SECRET_KEY", "ENVNAME_AWS_REGION",
           "ENVNAME_AWS_SESSION_TOKEN"]
