import random

location=['A','B']
status=['Clean','Dirty']

table={('A','Clean'):'Right', 
       ('A','Dirty'):'Suck',
       ('B','Clean'):'Left', 
       ('B','Dirty'):'Right'}

percepts=[]

def tableDrivenVaccumFunction(percept):
    
    print("Agents Perceived: ",percept)
    percepts.append(percept)
    
    print("Complete History: ",percepts)
    action=table.get(percept)
    
    return action
    
for _ in range(10):
    
    l=random.choice(location)
    s=random.choice(status)
    
    percept=(l,s)
    action=tableDrivenVaccumFunction(percept)
    print(action)


