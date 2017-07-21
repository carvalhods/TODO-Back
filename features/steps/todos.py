from behave import given, when, then
from app.controllers.todoController import get_all_todos
from app.controllers.todoController import get_todo
from app.controllers.todoController import delete_todo


##########################################################################
# Cenário: Desenvolver um método para listar todos os TODOs cadastrados
##########################################################################
@given(u'nenhum valor')
def step_impl(context):
    pass


@when(u'o usuário buscar por todos os registros')
def step_impl(context):
    context.retorno = str(get_all_todos())


@then(u'a aplicação deve retornar uma lista, preenchida ou não')
def step_impl(context):
    assert context.retorno[-4:-1] == '200'


##########################################################################
# Cenário: Desenvolver um método para localizar um TODO
##########################################################################
@given(u'a palavra-chave "{keyword}"')
def step_impl(context, keyword):
    context.keyword = keyword


@when(u'o usuário fazer uma busca')
def step_impl(context):
    context.retorno = str(get_todo(context.keyword))


@then(u'a aplicação deve retornar um objeto contendo o valor "{valor}"')
def step_impl(context, valor):
    assert context.retorno.find(valor) >= 0


##########################################################################
# Cenário: Desenvolver um método para deletar um TODO
##########################################################################
@given(u'o ID "{id}"')
def step_impl(context, id):
    context.id = id


@when(u'o usuário deletar um TODO do cadastro')
def step_impl(context):
    context.retorno = str(delete_todo(context.id))


@then(u'a aplicação deve retornar o código "{codigo}"')
def step_impl(context, codigo):
    assert context.retorno[-4:-1] == codigo
