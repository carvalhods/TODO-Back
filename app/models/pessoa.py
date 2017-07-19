from mongoengine import StringField, IntField
from marshmallow_mongoengine import ModelSchema
import mongoengine_goodjson as mgj


class Pessoa(mgj.Document):
    nome = StringField(required=True)
    idade = IntField(required=True)


class PessoaSchema(ModelSchema):
    class Meta:
        model = Pessoa
