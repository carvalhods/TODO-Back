#language: pt
#encoding: utf-8

@001
Funcionalidade: Implementar um cadastro de pessoas

Para cadastrar dados básicos de pessoas em uma base de dados
Como usuário
Desejo um sistema web de cadastro de pessoas

  Contexto:
    Dado os seguintes valores:
      | id |
      | 596d1b786e95521f7596f7da |
      | 596d1c036e955221485d20cf |

@10
Cenário: Desenvolver um método para listar todas as pessoas cadastradas
Dado nenhum valor
Quando o usuário buscar por todos os registros
Então a aplicação deve retornar uma lista, preenchida ou não

@11
Cenário: Desenvolver um método para localizar uma pessoa pelo ID
# Dado o valor "596d1b786e95521f7596f7da"
Quando o usuário fazer uma busca por ID
Então a aplicação deve retornar um objeto contendo o ID "596d1b786e95521f7596f7da"

@12
Cenário: Desenvolver um método para deletar uma pessoa pelo ID
# Dado o valor "596d1c036e955221485d20cf"
Quando o usuário deletar uma pessoa do cadastro
Então a aplicação deve retornar o código "204"
