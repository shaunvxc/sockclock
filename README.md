# sockclock
decorator to temporarily override socket's default timeout

## Why?

If you find yourself managing the `socket` module's default value to avoid the pesky `socket timeout` errors, this decorator can help you.  I've personally found it useful
when making http requests using `ChromeDriver` or `PhantomJS`.


## Usage
Decorate any function you'd like with the `set_timeout` decorator, and it override `socket`'s timeout value, but only during execution of that function.

```python

@sockclock.set_timeout(50)
def some_slow_fn():
    # the socket timeout will be updated to 50 during execution of this function.
    ...


some_slow_fn()

some_faster_fn() # socket's timeout is back to its normal default (ie, the default system timeout value).
```

## Installation
`$ pip install sockclock`
