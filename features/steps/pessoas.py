from behave import given, when, then
from app.controllers.pessoaController import get_person


@given(u'o valor "{id}"')
def step_impl(context, id):
    context.id = id


@when(u'o usuário fazer uma busca por ID')
def step_impl(context):
    context.retorno = str(get_person(context.id))


@then(u'a aplicação deve retornar um objeto contendo o ID "{id}"')
def step_impl(context, id):
    assert context.retorno.find(id) >= 0
