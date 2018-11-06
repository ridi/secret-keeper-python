import os

from collections import namedtuple

ENVNAME_AWS_ACCESS_KEY = "SECRETKEEPER_AWS_ACCESS_KEY"
ENVNAME_AWS_SECRET_KEY = "SECRETKEEPER_AWS_SECRET_KEY"
ENVNAME_AWS_REGION = "SECRETKEEPER_AWS_REGION"

ConnectArgsType = namedtuple('ConnectArgsType', [
    'aws_access_key', 'aws_secret_key', 'aws_region'
])

AWS_CONNECT_ARGS = None


def configure(aws_access_key=None, aws_secret_key=None, aws_region=None):
    global AWS_CONNECT_ARGS
    AWS_CONNECT_ARGS = ConnectArgsType(
        aws_access_key=aws_access_key,
        aws_secret_key=aws_secret_key,
        aws_region=aws_region,
    )


configure(
    aws_access_key=os.environ.get(ENVNAME_AWS_ACCESS_KEY),
    aws_secret_key=os.environ.get(ENVNAME_AWS_SECRET_KEY),
    aws_region=os.environ.get(ENVNAME_AWS_REGION),
)

__all__ = ["configure", "ENVNAME_AWS_ACCESS_KEY", "ENVNAME_AWS_SECRET_KEY", "ENVNAME_AWS_REGION"]
