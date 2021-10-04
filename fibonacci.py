from time import process_time, sleep

""" class Action: 
    def __init__(self, number, cost, rate):
        self.number = number
        self.cost = cost
        self.rate = rate
        self.benefits = round(self.cost*(1+(self.rate/100))-self.cost, 2)

action1 = Action(1, 20, 5)
action2 = Action(2, 30, 10)
action3 = Action(3, 50, 15)
action4 = Action(4, 70, 20)
action5 = Action(5, 60, 17)
action6 = Action(6, 80, 25)
action7 = Action(7, 22, 7)
action8 = Action(8, 26, 11)
actions_list = [action1, action2, action3, action4, action5, action6, action7, action8]
for action in actions_list:
    print (f'Action n°{action.number} benefits after 2 years are {action.benefits}') """
""" liste = ['benoit', 'thomas', 'paula', 'clem', 'delphine', 'sandrine', 'vincent', 'mathurin']

def factorielle_iterative(n):
    x = 1
    for i in range(2, n+1):
        print (liste[i])
        x *= i
    return x
start = process_time()  
def fibonnacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)
print (fibonnacci(40))
end = process_time()
print(start)
print(end)
print (end-start) """

# Fibonacci Series using Dynamic Programming
""" start = process_time()  
def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
print(fibonacci(100))
end = process_time()
print(start)
print(end)
print (end-start) """

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
 
# Driver Program
 
print(fibonacci(10))
