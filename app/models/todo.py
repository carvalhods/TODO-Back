from mongoengine import StringField, IntField
from marshmallow_mongoengine import ModelSchema
import mongoengine_goodjson as mgj


class Todo(mgj.Document):
    item = StringField(required=True)


class TodoSchema(ModelSchema):
    class Meta:
        model = Todo
