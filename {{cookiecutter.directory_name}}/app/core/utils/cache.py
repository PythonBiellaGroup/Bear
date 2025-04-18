import time
from functools import lru_cache, wraps


def time_cache(ttl_seconds: int, maxsize=1):
    """Cache the result of a function for at most ttl_seconds seconds."""

    def decorator(func):
        @lru_cache(maxsize=maxsize)
        def internal(_, *args, **kwds):
            return func(*args, **kwds)

        @wraps(func)
        def wrapper(*args, **kwds):
            timestamp = time.time() // ttl_seconds
            return internal(timestamp, *args, **kwds)

        return wrapper

    return decorator
