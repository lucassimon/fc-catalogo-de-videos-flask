from functools import wraps
from timeit import default_timer
from apps.logging import make_logger


logger = make_logger()


def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        response = f(*args, **kwargs)
        total_elapsed_time = default_timer() - start_time
        logger.info("elapsed time", total_elapsed_time=total_elapsed_time)
        return response

    return wrapper
