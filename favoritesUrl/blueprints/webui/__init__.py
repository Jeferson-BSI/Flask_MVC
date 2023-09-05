from flask import Blueprint

from .views import index, urls

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index, endpoint="index")
bp.add_url_rule("/urls", view_func=urls, endpoint="urls", methods=["GET", "POST"] )


def init_app(app):
    app.register_blueprint(bp)
