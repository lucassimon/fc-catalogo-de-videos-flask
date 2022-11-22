import logging
import structlog


def configure_logging():
    structlog.configure(
        processors=[
            # structlog.stdlib.add_logger_name,
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.CallsiteParameterAdder(
                {
                    structlog.processors.CallsiteParameter.FILENAME,
                    structlog.processors.CallsiteParameter.FUNC_NAME,
                    structlog.processors.CallsiteParameter.LINENO,
                    structlog.processors.CallsiteParameter.PATHNAME,
                }
            ),
            structlog.dev.set_exc_info,
            structlog.dev.ConsoleRenderer(
                exception_formatter=structlog.dev.rich_traceback
            ),
            # structlog.processors.dict_tracebacks
            # structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.NOTSET),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=False,
    )


def make_logger():
    log = structlog.get_logger()
    return log
