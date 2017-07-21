from app import app
from flask import request, jsonify
from flask_api import status
from app.models.todo import Todo, TodoSchema


@app.route('/', methods=['GET'])
def get_all_todos():
    """
    Esta função retorna todos os TODOs cadastrados na base de dados
    em formato JSON.
    """
    return Todo.objects.to_json(), 200


@app.route('/<busca>', methods=['GET'])
def get_todo(busca):
    """
    Esta função retorna todos os TODOs cadastrados na base de dados
    em formato JSON que satisfaçam os critérios de busca

    Args:
        busca (str): Critério de busca que será comparado ao campo 'item'
            de cada TODO cadastrado
    """
    retorno = Todo.objects.filter(item__contains=busca)
    if retorno:
        return retorno.to_json(), status.HTTP_200_OK
    return "", status.HTTP_404_NOT_FOUND


@app.route('/', methods=['POST'])
def create_todo():
    """
    Esta função será responsável por receber os dados de um TODO informado
    pelo usuário e salvá-lo na base de dados
    """
    json_data = request.get_json()
    todos, errors = TodoSchema().load(data=json_data)

    if errors:
        return jsonify(errors), status.HTTP_400_BAD_REQUEST

    todos.save()
    return todos.to_json(), status.HTTP_201_CREATED


@app.route('/<id>', methods=['DELETE'])
def delete_todo(id):
    """
    Esta função será responsável por excluir da base de dados um TODO
    específico informado pelo usuário

    Args:
        id (str): ID do TODO a ser excluído da base de dados
    """
    Todo.objects(id=id).delete()
    return "", status.HTTP_204_NO_CONTENT
