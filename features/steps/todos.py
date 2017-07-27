from behave import given, when, then
import requests as r
import json
from app import Todo


@given(u'o valor "{valor}"')
def step_impl(context, valor):
    context.valor = valor
    context.todo = Todo(item=valor)
    context.todo.save()


@then(u'a aplicação não deve retornar erros')
def step_impl(context):
    assert context.retorno.status_code != 500


##########################################################
# Cenário: Aplicação irá pesquisar um TODO
##########################################################
@when(u'a aplicação pesquisar um TODO')
def step_impl(context):
    context.retorno = r.get(context.server + "/" + context.valor)


# ########################################################
# # Cenário: Aplicação irá incluir um TODO
# ########################################################
@when(u'a aplicação incluir um TODO')
def step_impl(context):
    context.retorno = r.post(
        context.server + "/",
        json={"item": context.valor}
    )


##########################################################
# Cenário: Aplicação irá editar um TODO
##########################################################
@when(u'a aplicação editar um TODO')
def step_impl(context):
    context.retorno = r.post(
        context.server + "/",
        json={"id": str(context.todo.id), "item": context.todo.item}
    )


##########################################################
# Cenário: Aplicação irá deletar um TODO
##########################################################
@when(u'a aplicação deletar um TODO')
def step_impl(context):
    context.retorno = r.delete(context.server + "/" + str(context.todo.id))
