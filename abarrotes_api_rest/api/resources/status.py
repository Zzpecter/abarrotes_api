from flask_restful import Resource


class Status(Resource):
    def get(self):
        return {"mensaje": "API conectada correctamente"}, 200
