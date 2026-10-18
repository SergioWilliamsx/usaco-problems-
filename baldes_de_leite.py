print("Bem vindo ao programa para analisar a quantidade maxima de leite a ser despejado")
baldes_tamanho = list(map(int, input("Escreva o tamanhos dos 3 baldes no seguinte formato: (tam1 tam2 tam3)").split()))

max_milk = 0
for a in range(round(max(baldes_tamanho) / min(baldes_tamanho)) ):
    for b in range(round((max(baldes_tamanho) / next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)])))):
        max_temp = a*min(baldes_tamanho) + b*next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)])
        if((a*min(baldes_tamanho) + b*next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)])) <= max(baldes_tamanho)):
            max_milk = max(max_milk, a*min(baldes_tamanho) + b*next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)]))

print(round(max(baldes_tamanho) / min(baldes_tamanho)) , round((max(baldes_tamanho) / next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)]))), min(baldes_tamanho)*round(max(baldes_tamanho) / min(baldes_tamanho)) + round(max(baldes_tamanho) / next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)]))*next(item for item in baldes_tamanho if item not in [min(baldes_tamanho),max(baldes_tamanho)]), max_milk)