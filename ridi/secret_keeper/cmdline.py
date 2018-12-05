from __future__ import print_function
import argparse
import sys
import traceback

from botocore.exceptions import ClientError

from ridi.secret_keeper.connect import tell


def run(arguments):
    description = """
    Retrieve and print secrets from `secret-keeper`.
    You need to configure AWS credentials by environment variables or files.
    See https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#credentials for more detail.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("alias", help="Alias of the secret")
    parser.add_argument("-o", "--outfile", help="Output file name. If not provided, secret is printed to stdout.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Gives detailed error message")
    args = parser.parse_args(arguments)

    alias = args.alias
    outfile = args.outfile
    verbose = args.verbose

    try:
        secret = tell(alias).strip()
        if outfile:
            with open(outfile, "w") as f:
                print(secret, file=f)
        else:
            print(secret)
        return 0
    except Exception as e:
        if verbose:
            traceback.print_exc(file=sys.stderr)
        if isinstance(e, ClientError):
            print("Secret of alias '%s' is not found." % alias, file=sys.stderr)
        return 1


def main():
    retval = run(sys.argv[1:])
    sys.exit(retval)


if __name__ == "__main__":
    main()
