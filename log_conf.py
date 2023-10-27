"""
2023-10-19 08:09:48,340 - uvicorn.access - INFO - 172.17.0.1:58842 - "GET /docs HTTP/1.1" 200
2023-10-19 08:09:48,406 - uvicorn.access - INFO - 172.17.0.1:58842 - "GET /openapi.json HTTP/1.1" 200
2023-10-19 08:10:04,385 - app.main - INFO - upload/e89c139e-6e56-11ee-afc5-0242ac110002.jpg
2023-10-19 08:10:04,590 - uvicorn.access - INFO - 172.17.0.1:48546 - "POST /predict HTTP/1.1" 200
"""
log_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
        "access": {
            "format": '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "uvicorn.error": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        },
        "uvicorn.access": {
            "handlers": ["access"],
            "level": "INFO",
            "propagate": False
        },
    },
    "root": {
        "handlers": ["default"],
        "level": "INFO",
        "propagate": False
    },
}
