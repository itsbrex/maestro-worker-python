from typing import Optional
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    log_level: str = "INFO"
    enable_json_logging: bool = False
    model_path: str = "./worker.py"
    sentry_dsn: Optional[str] = None
    sentry_traces_sample_rate: float = 1.0
    sentry_errors_sample_rate: float = 1.0
    environment: str = 'production'

settings = Settings()
