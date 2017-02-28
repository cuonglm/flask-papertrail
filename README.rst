flask_papertrail
====

flask_papertrail -- Easily setup papertrail to your Flask application

.. image:: https://travis-ci.org/Gnouc/flask_papertrail.svg?branch=master
    :target: https://travis-ci.org/Gnouc/flask_papertrail

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

Author
======

Cuong Manh Le cuong.manhle.vn@gmail.com

License
=======

See `LICENSE <https://github.com/Gnouc/flask_papertrail/blob/master/LICENSE>`__
