from logging.handlers import SysLogHandler

from flask import Flask

from .context import flask_papertrail


def test_init_app():
    app = Flask(__name__)
    app.config['PAPERTRAIL_HOST'] = 'localhost'
    app.config['PAPERTRAIL_PORT'] = 1810

    flask_papertrail.PaperTrail(app)

    h = app.logger.handlers[-1]
    assert isinstance(h, SysLogHandler)

    f = app.logger.filters[-1]
    assert isinstance(f, flask_papertrail.core._ContextFilter)


def test_missing_configuration():
    app = Flask(__name__)

    try:
        flask_papertrail.PaperTrail(app)
    except flask_papertrail.core.ConfigError:
        assert True
    except Exception:
        assert False
