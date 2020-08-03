from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

# USUARIOS = {
#     'emerson': '123',
#     'bilieri': '321'
# }
#
#
# @auth.verify_password
# def verificacao(login, senha):
#     if not (login, senha):
#         return False
#     return USUARIOS.get(login) == senha

@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response

    @auth.login_required
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            dados = request.json
            print(dados)
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response

    @auth.login_required
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            mensagem = 'Pessoa {} excluida com sucesso'.format(pessoa.nome)
            pessoa.delete()
            response = {
                'status': 'sucesso',
                'mensagem': mensagem
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        print(pessoas)
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    @auth.login_required
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)
