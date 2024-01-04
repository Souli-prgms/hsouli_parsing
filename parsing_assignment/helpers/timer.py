"""Timer module."""
from typing import Callable, ParamSpec, TypeVar
import time

_Parameters = ParamSpec("_Parameters")
_ReturnT = TypeVar("_ReturnT")


def timer(func: Callable[_Parameters, _ReturnT]) -> Callable[_Parameters, _ReturnT]:
    """Times specific function.

    Args:
        func: Function to time.

    Returns:
        Decorated function.

    """

    def wrapped_function(
        *args: _Parameters.args, **kwargs: _Parameters.kwargs
    ) -> _ReturnT:
        start = time.time()
        return_value = func(*args, **kwargs)
        print(f"{time.time() - start} seconds elapsed")
        return return_value

    return wrapped_function
