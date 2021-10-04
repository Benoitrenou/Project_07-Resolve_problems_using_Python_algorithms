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


class Action: 
    def __init__(self, number, cost, rate):
        self.number = number
        self.cost = cost
        self.rate = rate
        self.benefits = round(self.cost*(1+(self.rate/100))-self.cost, 2)
    
    def __repr__(self):
        return (f"({self.number}, {self.cost}, {self.benefits})")

    def __str__(self):
        return (f"{self.number}, {self.cost}, {self.benefits}")



def algo_force_brute(capacite, elements, elements_selection = []):
    if elements:
        val1, lstVal1 = algo_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1] <= capacite:
            val2, lstVal2 = algo_force_brute(capacite - val[1], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2
        return val1, lstVal1
    else:
        return sum([i[2] for i in elements_selection]), elements_selection

actions_list = []
for action in actions_src:
    benefits = round(action[1]*(1+(action[2]/100))-action[1], 2)
    new_action = (action[0], action[1], benefits)
    actions_list.append(new_action)

print(algo_force_brute(500, actions_list))
