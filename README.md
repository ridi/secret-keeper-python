# Secret Keeper - Python

## Setup
`pip install ridi-secret-keeper`

## Usage

1. Set environment variables
```bash
export SECRETKEEPER_AWS_ACCESS_KEY="YOUR_ACCESS_KEY"
export SECRETKEEPER_AWS_SECRET_KEY="YOUR_SECRET_KEY"
export SECRETKEEPER_AWS_REGION ="us-east-1"
```

2. Get secret in your code
```python
from ridi import secretkeeper
secret = secretkeeper.get(alias)
```
