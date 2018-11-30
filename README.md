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
- let your deployment systems use secrets, simply by adding an IAM policy to the IAM user or role that you use in deployment.  You don't have to manage per-project config files.


## Install
```bash
pip install secret-keeper
```

## Preparation
- [Create a dedicated encryption key in AWS KMS](https://github.com/ridi/secret-keeper-python/wiki/Create-a-dedicated-encryption-key-in-AWS-KMS)
- [Create a dedicated IAM Policy for accessing secrets](https://github.com/ridi/secret-keeper-python/wiki/Create-a-dedicated-IAM-Policy-for-accessing-secrets)
- Add the policy to you IAM User or IAM Role.
- [Create a sample secret in AWS SSM Parameter Store](https://github.com/ridi/secret-keeper-python/wiki/Create-a-sample-secret-in-AWS-SSM-Parameter-Store)

## Usage
### Prepare credentials
If you are running as an IAM user with its security credentials, make sure that your credentials are properly set in either `~/.aws/credentials` file, or `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
See [`boto3`'s credentials scheme](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#credentials) for details of setting credentials.

#### Before 0.2.0
If you are using `secret-keeper` of version `0.1.x`, you cannot use `boto3`'s
credentials scheme. You should store credentials as special environment variables, namely `SECRETKEEPER_AWS_ACCESS_KEY`, `SECRETKEEPER_AWS_SECRET_KEY` and `SECRETKEEPER_AWS_REGION`.

```bash
$ export SECRETKEEPER_AWS_ACCESS_KEY="YOUR_ACCESS_KEY_ID"
$ export SECRETKEEPER_AWS_SECRET_KEY="YOUR_SECRET_ACCESS_KEY"
$ export SECRETKEEPER_AWS_REGION="us-east-1"
```

### Commandline Interface
`secret-keeper` commandline interface is supported as of `0.3.0`.
- Write to stdout.
```
$ secret-keeper sample.secret
pa$$w@rd!
```
- Write to file.
```
$ secret-keeper sample.secret --o outfile && cat outfile
pa$$w@rd!
```
- Print help.

```
$ secret-keeper -h
usage: secret-keeper [-h] [-o OUTFILE] [-v] alias

Retrieve and print secrets from `secret-keeper`. You need to configure AWS
credentials by environment variables or files. See https://boto3.amazonaws.com
/v1/documentation/api/latest/guide/configuration.html#credentials for more
detail.

positional arguments:
 alias                 Alias of the secret

optional arguments:
 -h, --help            show this help message and exit
 -o OUTFILE, --outfile OUTFILE
                       Output file name. If not provided, secret is printed
                       to stdout.
 -v, --verbose         Gives detailed error message
```

### Sample application.
- Write a sample application.
```Python
# sample.py
if __name__ == "__main__":
    from ridi import secret_keeper

    secret = secret_keeper.tell("sample.secret")
    print("Secret: %s" % secret)
```

- Run the sample application.

```
$ python sample.py
pa$$w@rd!
```

- Rather than using `boto3`'s credentials cheme, you can pass your credentials and region to `configure` function. (as of `0.2.0`)

```python
# sample2.py
from ridi import secret_keeper

secret_keeper.configure(
    aws_access_key="YOUR_ACCESS_KEY_ID",
    aws_secret_key="YOUR_SECRET_ACCESS_KEY",
    aws_region="us-east-1",
)
```
