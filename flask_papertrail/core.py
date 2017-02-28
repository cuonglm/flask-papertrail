import logging
import socket

from logging.handlers import SysLogHandler


REQUIRE_CONFIG_KEYS = ['PAPERTRAIL_HOST', 'PAPERTRAIL_PORT']


class PaperTrail(object):

    def __init__(self, app=None):
        self.default_logformat = (
            '%(asctime)s %(hostname)s {0}: %(levelname)s %(message)s'
        )
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """This callback can be used to initialize an application for the
        use with papertrail setup
        """
        if any(k not in app.config for k in REQUIRE_CONFIG_KEYS):
            raise ConfigError

        app_name = app.config.setdefault('PAPERTRAIL_APP', str(app))
        f = _ContextFilter()
        app.logger.addFilter(f)

        syslog = SysLogHandler(
            address=(
                app.config['PAPERTRAIL_HOST'],
                app.config['PAPERTRAIL_PORT']
            )
        )
        formatter = logging.Formatter(
            app.config.setdefault(
                'PAPERTRAIL_LOGFORMAT',
                self.default_logformat.format(app_name)
            ),
            datefmt=app.config.setdefault('DATE_FORMAT', '%b %d %H:%M:%S')
        )
        syslog.setFormatter(formatter)

        app.logger.addHandler(syslog)


class ConfigError(BaseException):
    pass


class _ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = self.hostname
        return True
