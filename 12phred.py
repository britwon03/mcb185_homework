import math 
def char_to_prob(char): 
    if len(char) != 1 or not 33 <= ord(char) <= 126: 
        return None 
    return 10 ** (-(ord(char) - 33)/ 10)

def prob_to_char(prob): 
    if (0 < prob <= 1): 
        q_score = -10 * math.log10(prob)
        char = chr(round(q_score) + 33)
        if 33 <= ord(char) <= 126: 
            return char 
        return None 
   

print(char_to_prob('A'))
print(prob_to_char(0.001))
print(prob_to_char(0.456))

