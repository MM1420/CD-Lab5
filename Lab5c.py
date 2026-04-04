grammar = {
    'S': ['AB', 'b'],
    'A': ['a', '$'],
    'B': ['c']
}

'''

The grannar is as follows:

    S → AB | b
    A → a | ε
    B → c

The three rules are as follows:
    1. If symbol is terminal → return itself
    2. If production starts with ε → add $
    3. If production starts with nonterminal → compute FIRST of it

'''

first = {}

"""
Example after computation:

first = {
    'S': {'a','b','c'},
    'A': {'a','$'},
    'B': {'c'}
}

"""

def FIRST(symbol):

    # If terminal
    if symbol.islower():
        return {symbol}

    # If already computed
    if symbol in first:
        return first[symbol]

    result = set()

    for production in grammar[symbol]:

        first_symbol = production[0]

        # Case 1: epsilon

        # Case 2: terminal

        # Case 3: nonterminal
        

    first[symbol] = result
    return result


for nonterminal in grammar:
    print("FIRST({}) = {}".format(nonterminal, FIRST(nonterminal)))