# Grammar representation
# Each nonterminal maps to a list of productions
grammar = {
    'S': ['AB', 'b'],  # S → AB | b
    'A': ['a'],        # A → a
    'B': ['c']         # B → c
}

def FIRST(symbol):
    """
    Recursive function to compute the FIRST set of a symbol.
    Returns a set of terminals.
    """

    # Step 1: If the symbol is a terminal (lowercase), its FIRST set is itself
    if symbol.islower():
        return {symbol}

    # Step 2: Initialize an empty set for the FIRST set
    result = set()

    # Step 3: Loop through all productions of the nonterminal
    for production in grammar[symbol]:
        # Take the first symbol of the production
        first_symbol = production[0]
        
        # Step 4: Recursively compute FIRST of the first symbol
        # Hint: Use result.update(...) to add all elements from the recursive call
        # result.update(FIRST(first_symbol))
        pass  # <-- Students should replace this line

    # Step 5: Return the computed FIRST set
    return result

# Compute and print FIRST sets for all nonterminals
for nonterminal in grammar:
    print("FIRST({}) = {}".format(nonterminal, FIRST(nonterminal)))
