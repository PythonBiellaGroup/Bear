import asyncio
import time
from functools import lru_cache, wraps


def multiplexed(func):
    """Call wrapped function repeatedly for each set of zipped positional args."""

    @wraps(func)
    def wrapper(*args, **kwds):
        results = []
        for arg in zip(*args, strict=False):
            results.append(func(*arg, **kwds))

        return results

    return wrapper


def multiplexed_method(func):
    """Call wrapped function repeatedly for each set of zipped positional args except self."""

    @wraps(func)
    def wrapper(self, *args, **kwds):
        @multiplexed
        def inject_self(*a, **k):
            return func(self, *a, **k)

        return inject_self(*args, **kwds)

    return wrapper


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


def batched(batch_size: int = 64):
    """Call wrapped async function repeatedly for batch_sized chunks of ALL POSITIONAL ARGS."""

    def decorator(func):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError(f"Decorated function must be async: {func}")

        @wraps(func)
        async def wrapper(*args, **kwds):
            if len(args) == 0:
                raise TypeError("Wrapped function must have at least one positional arg")

            seq = list(zip(*args, strict=False))
            results = []
            for chunk in (seq[pos : pos + batch_size] for pos in range(0, len(seq), batch_size)):
                # Convert each arg into a list
                args = [list(arg) for arg in zip(*chunk, strict=False)]
                batch_result = await func(*args, **kwds)
                try:
                    results.extend(batch_result)
                except TypeError as e:
                    raise TypeError("Wrapped function must return an iterable") from e

            return results

        return wrapper

    return decorator


def batched_method(batch_size=64):
    """Call wrapped function repeatedly for batch_sized chunks of ALL POSITIONAL ARGS except self."""

    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwds):
            @batched(batch_size=batch_size)
            async def inject_self(*a, **k):
                return await func(self, *a, **k)

            return await inject_self(*args, **kwds)

        return wrapper

    return decorator
