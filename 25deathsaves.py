import random

def simulate_death_saves():
    failures = 0
    successes = 0
    
    while failures < 3 and successes < 3:
        roll = random.randint(1, 20)
        
        if roll == 1:
            failures += 2  
        elif roll == 20:
            return 'revived'  
        elif roll < 10:
            failures += 1
        else:
            successes += 1
        
        if failures >= 3:
            return 'died'
        if successes >= 3:
            return 'stabilized'

def estimate_probabilities(num_simulations = 100000):
    outcomes = {'died': 0, 'stabilized': 0, 'revived': 0}
    
    for _ in range(num_simulations):
        outcomes[simulate_death_saves()] += 1
    
    return {
        'died': outcomes['died'] / num_simulations,
        'stabilized': outcomes['stabilized'] / num_simulations,
        'revived': outcomes['revived'] / num_simulations,
    }

def main():
    probabilities = estimate_probabilities()
    print('Died:', round(probabilities['died'], 4))
    print('Stabilized:', round(probabilities['stabilized'], 4))
    print('Revived:', round(probabilities['revived'], 4))

main()
