from app import app
from flask import request, jsonify
from flask_api import status
from app.models.pessoa import Pessoa, PessoaSchema


@app.route('/', methods=['GET'])
def get_all_people():
    return Pessoa.objects.to_json(), 200


@app.route('/<id>', methods=['GET'])
def get_person(id):
    busca = Pessoa.objects.get(id=id)
    if busca:
        return busca.to_json(), status.HTTP_200_OK
    return "", status.HTTP_404_NOT_FOUND


@app.route('/', methods=['POST'])
def create_person():
    json_data = request.get_json()
    pessoas, errors = PessoaSchema().load(data=json_data)

    if errors:
        return jsonify(errors), status.HTTP_400_BAD_REQUEST

    pessoas.save()
    return pessoas.to_json(), status.HTTP_201_CREATED


@app.route('/<id>', methods=['DELETE'])
def delete_person(id):
    Pessoa.objects(id=id).delete()
    return "", status.HTTP_204_NO_CONTENT
