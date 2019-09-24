flask_papertrail
================

flask_papertrail -- Easily setup papertrail to your Flask application

.. image:: https://travis-ci.org/cuonglm/flask-papertrail.svg?branch=master
    :target: https://travis-ci.org/cuonglm/flask-papertrail

Installation
============

.. code:: sh

    pip install Flask-PaperTrail

Usage
=====

.. code:: python

    from flask import Flask
    from flask_papertrail import PaperTrail

    app = Flask(__name__)
    Papertrail(app)

Or using `init_app`:

.. code:: python

    from flask import Flask
    from flask_papertrail import PaperTrail

    app = Flask(__name__)
    p = PaperTrail()
    p.init_app(app)

Config
==============

Required:

.. code:: python

    app.config['PAPERTRAIL_HOST'] = 'your papertrail host setup'
    app.config['PAPERTRAIL_PORT'] = 'your papertrail port setup'

Optional:

.. code:: python

    app.config['PAPERTRAIL_APP'] = str(app)  # Your papertrail app name
    app.config['PAPERTRAIL_LOGFORMAT'] = '%(asctime)s %(hostname)s {0}: %(levelname)s %(message)s'.format(str(app))  # Log format

Author
======

Cuong Manh Le cuong.manhle.vn@gmail.com

License
=======

See `LICENSE <https://github.com/cuonglm/flask-papertrail/blob/master/LICENSE>`__
