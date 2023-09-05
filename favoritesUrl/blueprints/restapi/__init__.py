from flask import Blueprint
from flask_restful import Api

from .resources import CampeonatosResource, CampeonatoItemResource, CampeonatosItemResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(CampeonatosResource, "/campeonatos/")
    api.add_resource(CampeonatoItemResource, "/campeonato/<ano>")
    api.add_resource(CampeonatosItemResource, "/campeonatos/<time>")
    app.register_blueprint(bp)
