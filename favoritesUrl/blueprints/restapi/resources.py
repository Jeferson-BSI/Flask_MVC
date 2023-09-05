from flask import abort, jsonify
from flask_restful import Resource

from favoritesUrl.models import Futbrdata


class CampeonatosResource(Resource):
    def get(self):
        campeonatos = Futbrdata.query.all() or abort(204)
        return jsonify(
            {"campeonatos": [campeonato.to_dict() for campeonato in campeonatos]}
        )


class CampeonatoItemResource(Resource):
    def get(self, ano):
        campeonato = Futbrdata.query.filter_by(ano=ano).first() or abort(404)
        print(campeonato)
        return jsonify(campeonato.to_dict())
    

class CampeonatosItemResource(Resource):
    def get(self, time):
        campeonatos = Futbrdata.query.filter_by(vencedor=str(time).title()).all() or abort(404)
        campeonatos_dict = {
            "campeonatos":[campeonato.to_dict() for campeonato in campeonatos],
            "total":len(campeonatos)
        }
        return jsonify(campeonatos_dict)
