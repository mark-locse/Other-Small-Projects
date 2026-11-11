import math
combos = "Your combos needed are: "
score = 0
min_score = int(input("What is the required score? "))
Aplus_Rank = min_score * 2
combo_count = int(input("How many floors does the level have? "))
while (score <= Aplus_Rank) and (combo_count!=0):
    n = int(input("What combo did you get on the floor? "))
    score += (n*n + n) * 250
    combo_count -= 1
    print("Current Score: ",score)
    combos += str(n)+", "
print(combos," and the score you'd get is",score,"with the A+ Rank being", Aplus_Rank)
    
