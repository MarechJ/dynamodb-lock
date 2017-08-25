# dynamodb-lock

dynamodb-lock is based on https://github.com/joeabrams026/dynamo-lock, a node.js and dynamodb based locking client. It supports autoexpiring locks, spinning for a lock and manually releasing a lock. It's designed primarily for use in AWS Lambda code, but can be used elsewhere without modification.

It needs better docs, exception handling and testing, but the guts are currently there. Patches welcome!

Forked from: https://github.com/Elethiomel/dynamodb-lock

# Install from pypi

```
pip3 install dynamo_lock
```

# Usage
```python
from dynamo_lock import LockerClient

lock = Lockerclient('mylocktable')
```
Or with credentials:
```python
    lock = LockerClient(
        config.DYN_TABLE_NAME,
        config.DYN_ACCESS_KEY,
        config.DYN_SECRET_KEY
    )
```

If necessary, create the lock table.

```python
lock.create_lock_table()
```

Attempt to aquire a lock. Returns True or False if succeeded.

```python
lock_expiry_ms = 1000  # Milliseconds after which the lock expires
lock.acquire('mylock', lock_expiry_ms)
```

Alternatively, spin for a lock if locks are bound to be short lived and you can spare the cpu.

```python
lock.spinlock('mylock', 10)
```

Finally, release your lock

```python
lock.release('mylock', 10)
```
