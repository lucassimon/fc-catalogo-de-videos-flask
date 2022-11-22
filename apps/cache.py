from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'RedisCache'})


def configure_cache(app):
    cache.init_app(app)
