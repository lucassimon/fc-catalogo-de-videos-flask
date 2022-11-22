# -*- coding: utf-8 -*-
import os
from flask import current_app, Flask, request, request_started

# ,request_finished

# Third
from typing import Any
from flask_cors import CORS
import structlog


# Local
from .api import configure_api
from .cache import configure_cache
from .database import configure_database, configure_migrate
from .logging import configure_logging
from .config import config


def bind_request_details(_: Flask, **extra: dict[str, Any]) -> None:
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request=request, name=current_app.name)


# def log_response(sender: Flask, response, **extras: dict[str, Any]) -> None:
#     sender.logger.debug(
#         "Request context is about to close down. " "Response: %s", response
#     )


def create_app():
    app = Flask("admin-catalogo-de-videos")
    environment = os.getenv("ENVIRONMENT", "production")
    app.config.from_object(config[environment])

    request_started.connect(bind_request_details, app)
    # request_finished.connect(log_response, app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    if app.config.get("CACHE_ENABLED"):
        configure_cache(app)

    # configure database sqlalchemy
    configure_database(app)
    configure_migrate(app)
    configure_logging()

    # executa a chamada da função de configuração
    configure_api(app)

    return app
