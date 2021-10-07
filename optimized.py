dataset_ref = input('Quel dataset souhaitez-vous analyser : 1 - 2 ?')

actions_list = []
with open(f"dataset{dataset_ref}_Python+P7.csv", newline='') as file:
    for row in file:
        splitted_row = row.split(sep=',')
        action_name = splitted_row[0]
        action_price = float(splitted_row[1])*100
        splitted_row[2].replace('\n', '')
        splitted_row[2].replace('\r', '')
        action_benefit = action_price*float(splitted_row[2])/100
        action = (action_name, int(action_price), action_benefit)
        if action_price>0:
            actions_list.append(action)


def algo_optimized(capacite, elements):
    #Initialisation matrice à 0 pour aucun élément ou capacité à 0
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i-1][1] <= w:
            # si le poids de l'élément courant est inférieur à la capacité étudiée
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
                # on entre au croisement matrice de la ligne de l'elt actuel et de la capacité étudiée
                # on attribue le plus grand nombre entre :
                    # l'addition de la valeur de l'elt actuel et la valeur optimisée dans la ligne précédent de la matrice pour la capacité restante après retrait du poids de l'elt actuel à la capacité étudiée
                    # et la valeur inscrite dans la matrice précédente pour la même capacité étudiée
            else:
             #si le poids elt courant est supérieur à capacité étudiée
                matrice[i][w] = matrice[i-1][w]
                # on reprend valeur optimisée de la ligne précédente pour la même capacité

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1

    total_cost = sum(action[1] for action in elements_selection)/100
    total_profit = round(sum(action[2] for action in elements_selection)/100, 2)
    print (f'Total cost = {total_cost}')
    print (f'Total profit = {total_profit}')
    return matrice[-1][-1], elements_selection

wallet = algo_optimized(500*100, actions_list)
for action in wallet[1]:
    print (f'{action[0]} | {action[1]/100} | {round(action[2]/100, 2)}')
