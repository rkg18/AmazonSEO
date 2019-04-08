import os

from flask import Flask
from flask import render_template

# Create Application

def create_app(test_config=None):
    # Creates Instance & Tells App where files are relative
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/about')
    def about():
        return render_template('about.html')

    from . import keyword
    app.register_blueprint(keyword.bp)

    return app