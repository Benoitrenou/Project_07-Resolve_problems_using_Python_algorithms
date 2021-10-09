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
        if action_price > 0 and action_benefit > 1:
            actions_list.append(action)


def algo_optimized(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]
        n -= 1
    return matrice[-1][-1], elements_selection

wallet = algo_optimized(500*100, actions_list)
for action in wallet[1]:
    print (f'{action[0]} | {action[1]/100:05.2f} | {round(action[2]/100, 2)}')

total_cost = sum(action[1] for action in wallet[1])/100
total_return = round(sum(action[2] for action in wallet[1])/100,2)
print('')
print(f'Total cost: {total_cost}')
print(f'Total return : {total_return}')
