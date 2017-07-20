from behave import given, when, then
from app.controllers.pessoaController import get_person
from app.controllers.pessoaController import get_all_people


##########################################################################
# Cenário: Desenvolver um método para listar todas as pessoas cadastradas
##########################################################################
@given(u'nenhum valor')
def step_impl(context):
    pass


@when(u'o usuário buscar por todos os registros')
def step_impl(context):
    context.retorno = str(get_all_people())


@then(u'a aplicação deve retornar uma lista, preenchida ou não')
def step_impl(context):
    assert context.retorno[-4:-1] == '200'


##########################################################################
# Cenário: Desenvolver um método para localizar uma pessoa pelo ID
##########################################################################
@given(u'o valor "{id}"')
def step_impl(context, id):
    context.id = id


@when(u'o usuário fazer uma busca por ID')
def step_impl(context):
    context.retorno = str(get_person(context.id))


@then(u'a aplicação deve retornar um objeto contendo o ID "{id}"')
def step_impl(context, id):
    assert context.retorno.find(id) >= 0
