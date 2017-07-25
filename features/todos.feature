#language: pt
#encoding: utf-8

@001
Funcionalidade: Implementar um TODO

Para cadastrar uma lista de TODOs em uma base de dados
Como usuário
Desejo um sistema web de TODOs


@10
Cenário: Desenvolver um método para listar todos os TODOs cadastrados
Dado nenhum valor
Quando o usuário buscar por todos os registros
Então a aplicação deve retornar uma lista, preenchida ou não

@11
Cenário: Desenvolver um método para localizar um TODO
Dado a palavra-chave "Python"
Quando o usuário fazer uma busca
Então a aplicação deve retornar um objeto contendo o valor "Python"

@12
Cenário: Desenvolver um método para deletar um TODO
Dado o ID "59713ab96e9552587fe95036"
Quando o usuário deletar um TODO do cadastro
Então a aplicação deve retornar o código "200"
