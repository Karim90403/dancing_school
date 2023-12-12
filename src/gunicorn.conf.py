# file gunicorn.conf.py
# coding=utf-8

import multiprocessing

from pydantic.v1 import BaseSettings, Field


class GunicornConfig(BaseSettings):
    host: str = Field(default="127.0.0.1", env="API_HOST")
    port: int = Field(default=8080, env="API_PORT")
    log_level: str = Field(default="info", env="API_LOG_LEVEL")

    @property
    def gunicorn_bind_url(self):
        return f"{self.host}:{self.port}"


conf = GunicornConfig()

loglevel = conf.log_level
errorlog = "-"
accesslog = "-"

bind = conf.gunicorn_bind_url

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

worker_class = "gevent"
