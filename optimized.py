from time import process_time

actions_list = []
with open("dataset1_Python+P7_v2.csv", newline='') as file:
    for row in file:
        splitted_row = row.split(sep=',')
        action = (splitted_row[0], abs(int(float(splitted_row[1])*100)), abs(int(float(splitted_row[2][0:-2])*100)))
        actions_list.append(action)


def algo_optimized(capacite, elements):
    #Initialisation matrice à 0 pour aucun élément ou capacité à 0
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):
            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

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
    total_profit = sum(action[2] for action in elements_selection)/100
    print (f'Total cost = {total_cost}')
    print (f'Total profit = {total_profit}')
    return matrice[-1][-1], elements_selection
start = process_time()
print(algo_optimized(500*100, actions_list))
end = process_time()
print (f'Time to proceed algorithm : {round(end-start, 2)} seconds')


