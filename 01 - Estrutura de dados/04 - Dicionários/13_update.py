contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)

# Deixa atualizar o dicionário, ele altera exatamente o que for pedido, se o dicionário tiver 3 chave:valor e pedir update para somente um valor ele apaga o restante
# Se os dados informados não existerem no dicionario, ele vai adicionar ao dicionario o novo contato
