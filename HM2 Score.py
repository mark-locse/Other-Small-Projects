import math
combos = "Your combos needed are: "
score = 0
min_score = int(input("What is the required score? "))
S_Rank = min_score * 2.5
combo_count = int(input("How many floors does the level have? "))
while (score <= S_Rank) and (combo_count!=0):
    n = int(input("What combo did you get on the floor? "))
    score += (n*n + n) * 250
    combo_count -= 1
    print("Current Score: ",score)
    combos += str(n)+", "
print(combos," and the score you'd get is",score," with the S Rank being", S_Rank)
    
