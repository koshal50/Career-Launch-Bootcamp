MAX, MIN = 1000, -1000

def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # If leaf node reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):  # Left and Right child
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:  # Alpha-Beta Pruning
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:  # Alpha-Beta Pruning
                break
        return best


if __name__ == "__main__":
    print("Enter 8 leaf node values (space separated):")
    values = list(map(int, input().split()))

    if len(values) != 8:
        print("Error: You must enter exactly 8 values!")
    else:
        result = minimax(0, 0, True, values, MIN, MAX)
        print("The optimal value is:", result)





/*

#output 
hp@hp:~/B_17 NEW$ python3 ASSI3.py
Enter 8 leaf node values (space separated):
3 5 6 9 1 2 0 -1 
The optimal value is: 5


*/


