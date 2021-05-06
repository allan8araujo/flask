from flask import Flask,request
from flask_restful import Api, Resource
from habilidades import Habilidades
import json
app=Flask(__name__)
api=Api(app)
desenvolvedores=[{'nome': 'Allan','habilidades':['Python','Flask']},
                 {'nome': 'allan tambem', 'habilidades':['python','Django']},
                 {'nome':'Test','habilidades':['testaprakrl','testa muito']},
                 ]
#devolve, edita e deleta um desenvolvedor pelo ID
class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response=desenvolvedores[id]
        except IndexError:
            mensage= 'Desenvolvedor de iD'+id+'Não existe'
        except Exception:
            mensagem= 'Erro desconhecido. Procure o adm da API'
            response= {'status':'erro', 'mensagem':mensagem}
        return (response)

    def put(self,id):
        dados=json.loads(request.data)
        desenvolvedores[id]= dados
        return (dados)
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','registro':'excluido'}
#lista de tds dev e inclui um new desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados=json.loads(request.data)
        posicao=len(desenvolvedores)
        dados['id']= posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')


if __name__ == '__main__':
    app.run(debug=True)
