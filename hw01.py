
# input: Two natural numbers B and C — the results of Bob's and Charlie's die rolls.
def answer(B,C):
    # output: A string with the probability of Alice winning in the form of an 
    # irreducible fraction in format A/B, where A — the numerator, and B — the 
    # denominator.
    high = max(B,C)
    num = 7-high
    denom = 6
    if(num % 2 == 0):
        num = num/2
        denom = denom/2
    if(num % 3 == 0):
        num = num/3
        denom = denom/3
    return str(int(num))+"/"+str(int(denom))
print(answer(6,1))