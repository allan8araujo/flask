from flask import Flask,request
import json
app=Flask(__name__)

desenvolvedores=[{'nome': 'Allan','habilidades':['Python','Flask']},
                 {'nome': 'allan tambem', 'habilidades':['python','Django']},
                 {'nome':'Test','habilidades':['testaprakrl','testa muito']},
                 ]

#devolve, edita e deleta um desenvolvedor pelo ID
@app.route('/dev/<int:id>',methods=['GET','PUT','DELETE'])
def Desenvolvedor(id):
    if request.method=='GET':
        desenvolvedor=desenvolvedores[id]
        return (desenvolvedor)

    elif 'DELETE' == request.method:
        desenvolvedores.pop(id)
        return ({'status':'sucesso','mensagem':'registro deletado'})

    elif request.method=='PUT':
        dados=json.loads(request.data)
        desenvolvedores[id]=dados
        return (dados)

#lista de tds dev e inclui um new desenvolvedor

@app.route('/dev/',methods=['POST','GET'])
def lista_desenvolvedores():
    if request.method =='POST':
        dados=json.loads(request.data)
        desenvolvedores.append(dados)
        return ({'status':'sucesso','dados':'Registro inserido'})
    elif request.method=='GET':
        return ''

if __name__ == '__main__':
    app.run(debug=True)
