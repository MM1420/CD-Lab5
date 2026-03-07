# Grammar representation
# Each nonterminal maps to a list of productions
grammar = {
    'S': ['AB', 'b'],
    'A': ['a'],
    'B': ['c']
}

# Initialize FIRST sets
first = {}

for nonterminal in grammar:
    first[nonterminal] = set()

changed = True

while changed:
    changed = False
    
    for nonterminal in grammar:
        for production in grammar[nonterminal]:
            
            first_symbol = production[0]
            
            # Case 1: terminal
            if first_symbol.islower():
                if first_symbol not in first[nonterminal]:
                    first[nonterminal].add(first_symbol)
                    changed = True
            
            # Case 2: nonterminal
            else:
                for symbol in first[first_symbol]:
                    if symbol not in first[nonterminal]:
                        first[nonterminal].add(symbol)
                        changed = True

# Print FIRST sets
for nonterminal in first:
    print("FIRST({}) = {}".format(nonterminal, first[nonterminal]))
