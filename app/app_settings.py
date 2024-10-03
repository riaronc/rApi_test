"""Settings that will be used throughout the application."""
import logging
import os
import sys
from typing import Any, Dict, List

from loguru import logger

from app.core.logging import format_record, InterceptHandler


class AppSettings:
    """Bundle all app settings."""
    app_env: str = os.getenv("APP_ENV")

    # FastAPI App settings
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    allowed_hosts: List[str] = ["*"]

    title: str = os.getenv("APP_TITLE")
    version: str = os.getenv("APP_VERSION")
    description: str = os.getenv("APP_DESCRIPTION")

    app_domain: str = os.getenv("APP_DOMAIN")
    api_domain: str = os.getenv("APP_DOMAIN")
    api_prefix: str = "/api/v1"
    api_search_prefix: str = f"{api_prefix}/search"

    qdrant_host: str = os.getenv("QDRANT_HOST")
    qdrant_port: int = os.getenv("QDRANT_PORT")
    qdrant_default_collection_name: str = os.getenv("QDRANT_DEFAULT_COLLECTION_NAME")

    @property
    def qdrant_db_kwargs(self) -> Dict[str, Any]:
        return {
            "host": self.qdrant_host,
            "port": self.qdrant_port,
        }

    def configure_logging(self) -> None:
        """Configure and format logging used in app."""
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
        # intercept everything at the root logger
        logging.root.handlers = [InterceptHandler()]
        logging.root.setLevel("DEBUG")

        # remove every other logger's handlers
        # and propagate to root logger
        for name in logging.root.manager.loggerDict.keys():
            logging.getLogger(name).handlers = []
            logging.getLogger(name).propagate = True

        # configure loguru
        logger.configure(
            handlers=[{"sink": sys.stdout, "serialize": False, "format": format_record, "colorize": True, }])


app_settings = AppSettings()
app_settings.configure_logging()
