from behave import given, when, then
from app.controllers.pessoaController import get_person
from app.controllers.pessoaController import get_all_people
from app.controllers.pessoaController import delete_person


@given(u'os seguintes valores')
def step_impl(context):
    for row in context.table:
        context.id = row['id']


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
@when(u'o usuário fazer uma busca por ID')
def step_impl(context):
    context.retorno = str(get_person(context.id))


@then(u'a aplicação deve retornar um objeto contendo o ID "{id}"')
def step_impl(context, id):
    assert context.retorno.find(id) >= 0


##########################################################################
# Cenário: Desenvolver um método para deletar uma pessoa pelo ID
##########################################################################
@when(u'o usuário deletar uma pessoa do cadastro')
def step_impl(context):
    context.retorno = str(delete_person(context.id))


@then(u'a aplicação deve retornar o código "{codigo}"')
def step_impl(context, codigo):
    assert context.retorno[-4:-1] == codigo
