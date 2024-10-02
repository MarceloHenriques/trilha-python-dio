carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros): # Indica o indice de cada objeto na lista
    print(f"{indice}: {carro}") # quando for percorrer a lista importante colocar valores de indice
