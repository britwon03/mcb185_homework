import random 
trials = 1000
shared = 0 

for t in range(trials): 
    # does this classroom have shared birthday?  
    peeps = [] # empty list of students 
    for i in range(23): # adding 23 students to list 
        bday = random.randint(0,354)
        if bday in peeps: 
            shared += 1 
            break 
        else: 
            peeps.append(bday)


print(shared/trials)



