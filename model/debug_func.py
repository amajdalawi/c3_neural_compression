import jax
import inspect
import functools
import os

def debug_func(func):

    @functools.wraps
    def wrapper(*args, **kwargs):
        frame = inspect.currentframe().f_back
        filename = os.path.basename(frame.f_code.co_filename)
        #print(f"{{Called {func.__name__} from {filename}}}")
        jax.debug.print(f"Called {func.__name__} from {filename}")
        return func(*args, **kwargs)
    return wrapper

