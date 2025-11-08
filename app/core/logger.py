import logging
import sys
from app.core.config import settings
import sentry_sdk

# Desactiva los logs de fastapi-uvicorn 
logging.getLogger("uvicorn.access").disabled = True
logging.getLogger("uvicorn.error").disabled = True
logging.getLogger("uvicorn").disabled = True

if settings.SENTRY_KEY:
    sentry_sdk.init(
        dsn=settings.SENTRY_KEY,
        send_default_pii=True,
        enable_logs=True,
    )

logger = logging.getLogger("gym_app")

if logger.hasHandlers():
    logger.handlers.clear()

stream_handler = logging.StreamHandler(sys.stdout)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
