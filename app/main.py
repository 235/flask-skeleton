# -*- coding:utf-8 -*-

#FallBackToFlask:
from flask import Flask, render_template
#from diesel.web import DieselFlask, render_template

from blueprints.main import simple_page
default_blueprints = [
        (simple_page, ''),
        #(blueprint_instance, url_preffix)
    ]


def app_factory(config, app_name=None, blueprints=None):
    app_name = app_name or __name__
    #FallBackToFlask:
    app = Flask(app_name)
    #app = DieselFlask(app_name)

    configure_app(app, config)
    configure_blueprints(app, blueprints)
    configure_error_handlers(app)
    configure_database(app)
    configure_context_processors(app)
    configure_template_filters(app)
    configure_extensions(app)
    configure_before_request(app)
    configure_views(app)

    if app.config['DEBUG']: serve_static(app)

    return app


def configure_app(app, config):
    app.config.from_object(config)
    app.config.from_envvar("APP_CONFIG", silent=True)  # avaiable in the server


def configure_blueprints(app, blueprints):
    for blueprint, url_prefix in (blueprints or default_blueprints):
        app.register_blueprint(blueprint, url_prefix=url_prefix)


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        """
        The server understood the request, but is refusing to fulfill it.
        Authorization will not help and the request SHOULD NOT be repeated.
        If the request method was not HEAD and the server wishes to make public
        why the request has not been fulfilled, it SHOULD describe the reason for
        the refusal in the entity. If the server does not wish to make this
        information available to the client, the status code 404 (Not Found)
        can be used instead.
        """
        return render_template("errors/403_access_forbidden.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        """
        The server has not found anything matching the Request-URI. No indication
        is given of whether the condition is temporary or permanent. The 410 (Gone)
        status code SHOULD be used if the server knows, through some internally
        configurable mechanism, that an old resource is permanently unavailable
        and has no forwarding address. This status code is commonly used when the
        server does not wish to reveal exactly why the request has been refused,
        or when no other response is applicable.
        """
        return render_template("errors/404_page_not_found.html"), 404

    @app.errorhandler(405)
    def method_not_allowed_page(error):
        """
        The method specified in the Request-Line is not allowed for the resource
        identified by the Request-URI. The response MUST include an Allow header
        containing a list of valid methods for the requested resource.
        """
        return render_template("errors/405_method_not_allowed.html"), 405

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("errors/server_error.html"), 500


def configure_database(app):
    "Database configuration should be set here"
    # uncomment for sqlalchemy support
    # from database import db
    # db.app = app
    # db.init_app(app)


def configure_context_processors(app):
    "Modify templates context here"
    pass


def configure_template_filters(app):
    "Configure filters and tags for jinja"
    pass


def configure_extensions(app):
    "Configure extensions like mail and login here"
    pass


def configure_before_request(app):
    pass


def configure_views(app):
    "Add some simple views here like index_view"
    pass


def serve_static(app):
    from werkzeug import SharedDataMiddleware
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/':                        app.config['ROOT_PATH'],
        app.config['STATIC_URL']:   app.config['STATIC_PATH'],
        app.config['MEDIA_URL']:    app.config['MEDIA_PATH']
    })

