#language: pt
#encoding: utf-8

@001
Funcionalidade: Implementar um cadastro de pessoas

Para cadastrar dados básicos de pessoas em uma base de dados
Como usuário
Desejo um sistema web de cadastro de pessoas

@10
Cenário: Desenvolver um método para localizar uma pessoa pelo ID
Dado o valor "596d1b786e95521f7596f7da"
Quando o usuário fazer uma busca por ID
Então a aplicação deve retornar um objeto contendo o ID "596d1b786e95521f7596f7da"