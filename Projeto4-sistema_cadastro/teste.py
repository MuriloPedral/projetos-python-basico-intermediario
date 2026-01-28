carro = {"marca": "Chevrolet", "modelo": "Tracker", "ano": 2020}

pessoa = {
    "nome": "Paulo",
    "idade": 29,
    "filhos": [
        {"nome": "João", "idade": 6}, 
        {"nome": "Maria", "idade": 9}
    ]
}

carro = {"marca": "Chevrolet", "modelo": "Tracker", "ano": 2020}

carro = dict(marca="Chevrolet", modelo="Tracker", ano=2020)
print(carro)
# output:
# {'marca': 'Chevrolet', 'modelo': 'Tracker', 'ano': 2020}

capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
capital_brasil = capitais["Brasil"]
print(capital_brasil)
# output:
# Brasília

capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
pais = "Itália"
if pais in capitais:
    capital = capitais[pais]
    print(f"A capital de {pais} é {capital}.")
else:
    print(f"A capital de {pais} não foi encontrada no dicionário!")


capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
capitais["Itália"] = "Roma"
capital_italia = capitais["Itália"]
print(capital_italia)
# output:
# Roma

capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
capitais["Brasil"] = "???"
capital_brasil = capitais["Brasil"]
print(capital_brasil)
# output:
# ???

capitais = {"Brasil": "Brasília", "Alemanha": "Berlim", "Japão": "Tóquio"}
del capitais["Brasil"]
print(capitais)
# output:
# {'Alemanha': 'Berlim', 'Japão': 'Tóquio'}

print(carro)