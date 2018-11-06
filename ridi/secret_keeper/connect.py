import boto3


def _get_client():
    from ridi.secret_keeper.config import AWS_CONNECT_ARGS

    client = boto3.client(
        'ssm',
        region_name=AWS_CONNECT_ARGS.aws_region,
        aws_access_key_id=AWS_CONNECT_ARGS.aws_access_key,
        aws_secret_access_key=AWS_CONNECT_ARGS.aws_secret_key,
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


__all__ = ["tell", "tell_safe"]
