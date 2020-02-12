from itertools import combinations
import math
import random

A = set(['a', 'b', 'c', 'd'])
nonempty_subsets = set (combinations(A,1)).union(set(combinations(A,2))).union(set(combinations(A,3))).union(set(combinations(A,4)))
maxMoves = int(math.pow(2, len(A)))

nonempty_subset_array = []
fullSubset = None

# Mapped subset into array
for x in nonempty_subsets:
    if (len(x) < 4):
        nonempty_subset_array.append(x)
    else:
        fullSubset = x

nonempty_subsets.remove(fullSubset) # No player can pick this one.

playerOne_log = "Player One's Turn: Player one picked {}"
playerTwo_log = "Player Two;s Turn: Player two picked {}"

seenElements = []
loser = None

def winSelect(set):  
    elementsNeededToWin = ['a', 'b', 'c', 'd']
    elementsNeededToWin = list(map(lambda x: x if x not in seenElements else None, elementsNeededToWin))
    elementsNeededToWin = list(filter(None, elementsNeededToWin))
    for x in set:
        if (x in seenElements):
            return False
        else:
            elementsNeededToWin.remove(x)
    
    if (len(elementsNeededToWin) == 0):
        return True
    else:
        return False
    

for t in range(maxMoves, 0, -1):
    # Iterate through each turn
    if (t == maxMoves):
        # First player's move, can pick any combination.
        randomIndex = random.randint(0, len(nonempty_subset_array)) - 1
        print(playerOne_log.format(nonempty_subset_array[randomIndex]))
        for e in nonempty_subset_array[randomIndex]:
            seenElements.append(e)
        nonempty_subsets.remove(nonempty_subset_array[randomIndex]) # Remove from subset
        nonempty_subset_array.pop(randomIndex) # Remove from array
        print(seenElements)
        
    else:
        # Iterate through the available set for any set that is pickable.
        playerSelect = None
        for set in nonempty_subset_array:
            if (winSelect(set) == True):
                playerSelect = set
                for e in set:
                    seenElements.append(e)

        # No possible moves.
        if (playerSelect == None):
            if (t % 2 == 0):
                loser = "Player One Loses!"
            else:
                loser = "Player Two Loses!"
            break
            
    
        if (t % 2 == 0):
            print(playerOne_log.format(playerSelect))
        else:
            print(playerTwo_log.format(playerSelect))

print(loser)
    
