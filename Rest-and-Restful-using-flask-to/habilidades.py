from flask_restful import Resource
habilidades=['python','javascript','java','c#','c++','Flask']

class Habilidades(Resource):
    def get(self):
        return habilidades
    def post(self):
        pass
    def delete(self):
        pass