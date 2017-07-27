from flask import Flask
from flask import jsonify
from flask import request
from flask_api import FlaskAPI
from flask_api import status
from flask_cors import CORS, cross_origin
from mongoengine import connect, StringField, IntField
from marshmallow_mongoengine import ModelSchema
import mongoengine_goodjson as mgj
from build import create_app

app = create_app()


class Todo(mgj.Document):
    item = StringField(required=True)


class TodoSchema(ModelSchema):
    class Meta:
        model = Todo


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
    retorno = Todo.objects.filter(item__icontains=busca)
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
    return "", status.HTTP_200_OK


if __name__ == '__main__':
    app.run(threaded=True, host="0.0.0.0", port=5000, debug=True)
