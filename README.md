# Secret Keeper - Python

[![Build Status](https://travis-ci.com/ridi/secret-keeper-python.svg?branch=master)](https://travis-ci.com/ridi/secret-keeper-python)
[![PyPI version](https://badge.fury.io/py/secret-keeper.svg)](https://badge.fury.io/py/secret-keeper)
[![Coverage Status](https://coveralls.io/repos/github/ridi/secret-keeper-python/badge.svg?branch=master)](https://coveralls.io/github/ridi/secret-keeper-python?branch=master)

## Introduction
Without secret-keeper, you would have:
- hard-coded your secrets in your version-controlled source code (Worst!), or
- created a not-version-controlled config file and manually provide it when you deploy your code, or
- let your deployment system - Jenkins CI, etc - mananage your not-version-controlled config file, but you have as many of them as your projects.

With secret-keeper, you can:
- store your secrets in AWS and let your applications use it safely and conveniently.
- let AWS manage contents of your secrets, keeping them encoded and safe.
- version-control usage of secrets inside your applications, since secrets are referred only with their aliases.
- simply provide access key and secret key of your dedicated IAM user to your deployment system. You don't have to manage per-project config files.


## Install
```bash
pip install secret-keeper
```

## Preparation
- [Create a dedicated AWS IAM user](https://github.com/ridi/secret-keeper-python/wiki/Create-a-dedicated-AWS-IAM-user)
- [Create a dedicated encryption key in AWS KMS](https://github.com/ridi/secret-keeper-python/wiki/Create-a-dedicated-encryption-key-in-AWS-KMS)
- [Create a sample secret in AWS SSM Parameter Store](https://github.com/ridi/secret-keeper-python/wiki/Create-a-sample-secret-in-AWS-SSM-Parameter-Store)

## Usage
- Write a sample application.
```Python
# sample.py
if __name__ == "__main__":
    from ridi import secret_keeper

    secret = secret_keeper.tell("sample.secret")
    print("Secret: %s" % secret)
```

- Run the sample application. You must either provide the dedicated user's access key, secret key and the region as environment variables, or pass them to `configure` function.

### Provide as environment variables
```bash
$ export SECRETKEEPER_AWS_ACCESS_KEY="YOUR_ACCESS_KEY_ID"
$ export SECRETKEEPER_AWS_SECRET_KEY="YOUR_SECRET_ACCESS_KEY"
$ export SECRETKEEPER_AWS_REGION="us-east-1"
$ python sample.py
Secret: pa$$w@rd!
```

### Pass to `configure` function
```python
from ridi import secret_keeper

secret_keeper.configure(
    aws_access_key="YOUR_ACCESS_KEY_ID",
    aws_secret_key="YOUR_SECRET_ACCESS_KEY",
    aws_region="us-east-1",
)
```
