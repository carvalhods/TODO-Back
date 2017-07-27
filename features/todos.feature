#language: pt
#encoding: utf-8

@001
Funcionalidade: Implementar um TODO

  Para gerenciar TODOs
  Como aplicação
  Desejo uma API com funções CRUD

  Contexto:
    Dado o valor "Programar em JS"

  @10
  Cenário: Aplicação irá pesquisar um TODO
    Quando a aplicação pesquisar um TODO
    Então a aplicação não deve retornar erros

  @11
  Cenário: Aplicação irá incluir um TODO
    Quando a aplicação incluir um TODO
    Então a aplicação não deve retornar erros

  @12
  Cenário: Aplicação irá editar um TODO
    Quando a aplicação editar um TODO
    Então a aplicação não deve retornar erros

  @13
  Cenário: Aplicação irá deletar um TODO
    Quando a aplicação deletar um TODO
    Então a aplicação não deve retornar erros
