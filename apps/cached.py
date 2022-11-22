import hashlib

from flask import request, current_app
from functools import wraps
from http import HTTPStatus

from .cache import cache


def cached(fn=None, timeout=3600):
    """Caches a Flask route/view in memcached.

    The request url, args, and current user are used to build the cache key.
    Only GET requests are cached.
    By default, cached requests expire after 3600 seconds == 1 hour
    """

    if not isinstance(timeout, int):
        raise Exception("Minutes must be an integer number.")

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if request.method != "GET":
                return func(*args, **kwargs)

            if not current_app.config["ENABLE_CACHE"]:
                return func(*args, **kwargs)

            prefix = f"{current_app.name}"
            path = request.full_path
            key = "{method}-{path}".format(method=request.method, path=path)
            hashed = hashlib.md5(key.encode("utf8")).hexdigest()
            hashed = "{prefix}-{hashed}".format(prefix=prefix, hashed=hashed)

            try:
                resp = cache.get(hashed)
                if resp:
                    return resp

            except Exception:
                resp = None

            resp = func(*args, **kwargs)

            if resp.status_code in [
                HTTPStatus.UNAUTHORIZED,
                HTTPStatus.BAD_REQUEST,
                HTTPStatus.NOT_FOUND,
                HTTPStatus.INTERNAL_SERVER_ERROR,
                HTTPStatus.CONFLICT,
            ]:
                return resp

            try:
                cache.set(hashed, resp, timeout=timeout)

            except Exception:
                # TODO add sentry or print the log or send to mail_admins
                pass

            return resp

        return inner

    return wrapper(fn) if fn else wrapper
