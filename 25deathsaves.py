import random 
trials = 1000000
die = 0 
stable = 0 
revive = 0 


for i in range(trials): 
    failure = 0 
    success = 0 
    for i in range(trials): 
        r = random.randint(1,20)
        if r == 1 :  failure += 2 
        elif r <= 9: failure += 1 
        elif r <= 19: success += 1
        else:
            revive += 1 
            break 
        if success == 3: 
            stable += 1 
            break 
        if failure == 3: 
            die += 1 
            break 
print('die:', die/trials, 'stable:', stable/trials, 'revive:', revive/trials)