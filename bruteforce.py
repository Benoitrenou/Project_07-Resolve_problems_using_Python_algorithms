actions_src = [
    (1, 20, 5),
    (2, 30, 10), 
    (3, 50, 10), 
    (4, 70, 20), 
    (5, 60, 17), 
    (6, 80, 25), 
    (7, 22, 7), 
    (8, 26, 11), 
    (9, 48, 13),
    (10, 34, 27), 
    (11, 42, 17),
    (12, 110, 9),
    (13, 38, 23),
    (14, 14, 1),
    (15, 18, 3),
    (16, 8, 8),
    (17, 4, 12),
    (18, 10, 14),
    (19, 24, 21),
    (20, 114, 18)
    ]

actions_list = []
for action in actions_src:
    benefits = round(action[1]*(1+(action[2]/100))-action[1], 2)
    new_action = (action[0], action[1], benefits)
    actions_list.append(new_action)

def algo_force_brute(capacite, elements, elements_selection = []):
    if elements:
        val1, lstVal1 = algo_force_brute(capacite, elements[1:], elements_selection)
        #ignore élément courant -> [1:]
        val = elements[0]
        #isole élément courant
        if val[1] <= capacite:
        #vérification si contrainte élément courant <= capacité 
            val2, lstVal2 = algo_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            #si c'est le cas, rappel fonction en retirant capacité poids élément courant val[1] / renvoie liste éléments sans courant / ajout élément courant dans éléments sélectionnés
            if val1 < val2:
            #vérification si solution meilleure avec ajout élément ou non
                return val2, lstVal2
        return val1, lstVal1
        #si pas le cas, revnoie liste sans élément courant
    else:
        return sum([i[2] for i in elements_selection]), elements_selection
        #retour somme des valeurs et liste des éléments sélectionnés

wallet = algo_force_brute(500, actions_list)
total_profit = round(wallet[0],2)
total_cost = sum(action[1] for action in wallet[1])
print(f'Coût total portefeuille : {total_cost}€')
print(f'Bénéfice après 2 ans : {total_profit}€')
print('Actions comprises dans le portefeuille :')
for action in wallet[1]:
    print(f'N°{action[0]} | Prix : {action[1]}€ | Profit : {action[2]}€')
