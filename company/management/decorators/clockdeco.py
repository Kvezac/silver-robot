from time import time
from functools import wraps

HEADER = '\033[95m'  # purple
OKGREEN = '\033[92m'  # green
OKBLUE = '\033[96m'  # blue
WARNING = '\033[93m'  # orange
ENDC = '\033[0m'  # default
FAIL = '\033[91m'  # red


def clock(func):
    @wraps(func)
    def clocked(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        elapsed = time() - time_start
        name = func.__name__
        args_lst = []
        if args:
            args_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={w}' if type(k) != "object" else k.__class__ for k, w in sorted(kwargs.items()) if w]
            args_lst.append(", ".join(pairs))
        arg_str = ", ".join(args_lst) if args_lst else f'{OKGREEN}finish{OKGREEN}'
        print(f'{HEADER}{name}{ENDC} -> time {OKBLUE}{elapsed:.2f}{ENDC}sec --> {arg_str}')
        return result

    return clocked
