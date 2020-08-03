from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Joao Lucas', idade=5)
    pessoa.save()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Emerson').first()
    pessoa.idade = 25
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Joao Lucas').first()
    pessoa.delete()


def consulta():
    pessoa = Pessoas.query.filter_by(nome='Joao Lucas').first()
    print('{} idade: {}'.format(pessoa, pessoa.idade))


def consulta_all():
    pessoa = Pessoas.query.all()
    print(pessoa)


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    # consulta_all()
    # consulta()
    #insere_usuario('emerson', '1234')
    #insere_usuario('bilieri', '4321')
    consulta_todos_usuarios()
