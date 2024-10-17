tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]]
root = 0
pruned = 0

def children(branch, depth, alpha, beta):
    global pruned
    i = 0
    for child in branch:
        if isinstance(child, list):
            nalpha, nbeta = children(child, depth + 1, alpha, beta)
            if depth % 2 == 1:  # Maximizing player
                beta = nalpha if nalpha < beta else beta
            else:  # Minimizing player
                alpha = nbeta if nbeta < alpha else beta
            branch[i] = beta if depth % 2 == 0 else alpha
            i += 1
        else:
            if depth % 2 == 0 and alpha < child:  # Maximizing player
                alpha = child
            if depth % 2 == 1 and beta > child:  # Minimizing player
                beta = child
            if alpha >= beta:
                pruned += 1
                break
    return alpha, beta

def alphabeta(tree, start, upper, lower):
    global pruned
    global root
    alpha, beta = children(tree, start, upper, lower)
    print("(alpha, beta):", alpha, beta)
    print("Result:", tree)
    print("Times pruned:", pruned)
    return alpha, beta, tree, pruned

if __name__ == "__main__":
    alphabeta(tree, root, -15, 15)
