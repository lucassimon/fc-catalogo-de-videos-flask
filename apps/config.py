# -*- coding: utf-8 -*-
# Python
from datetime import timedelta
from decouple import config


class Config:
    SECRET_KEY = config("SECRET_KEY", default="hard to guess string")
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    SENTRY_DSN = config("SENTRY_DSN", default="")
    SSL_REDIRECT = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes=config("JWT_ACCESS_TOKEN_EXPIRES", default=20, cast=int)
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=config("JWT_REFRESH_TOKEN_EXPIRES", default=30, cast=int)
    )
    ENABLE_CACHE = config("ENABLE_CACHE", default=False, cast=bool)
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = config("CACHE_REDIS_URL", default="redis://localhost:6379/0")
    SQLALCHEMY_DATABASE_URI = config(
        "SQLALCHEMY_DATABASE_URI", default="sqlite:///db.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = config(
        "SQLALCHEMY_TRACK_MODIFICATIONS", default=False, cast=bool
    )
    ENABLE_JSON_LOGGING = config("ENABLE_JSON_LOGGING", default=False, cast=bool)


class DevelopmentConfig(Config):
    DEBUG = True
    ENABLE_CACHE = False
    CACHE_TYPE = "redis"
    CACHE_REDIS_URL = "redis://localhost:6379/0"


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False
    FLASK_DEBUG = False


class QaConfig(ProductionConfig):
    DEBUG = False
    FLASK_DEBUG = False


class HmlConfig(ProductionConfig):
    DEBUG = False
    FLASK_DEBUG = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "qa": QaConfig,
    "production": ProductionConfig,
    "hml": HmlConfig,
    "default": DevelopmentConfig,
}
