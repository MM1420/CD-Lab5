grammar = {
    'S': ['AB', 'b'],
    'A': ['a'],
    'B': ['c']
}


# Step 1: Initialize FIRST sets
first = {}

for nonterminal in grammar:
    # TODO: initialize each FIRST set as an empty set
    pass


# Step 2: Compute FIRST sets
changed = True

while changed:
    changed = False

    # TODO:
    # Loop over each nonterminal
    # Loop over each production
    # Apply the rules described in the lab sheet
    # Update FIRST sets accordingly
    pass


# Step 3: Print FIRST sets
for nonterminal in first:
    print("FIRST({}) = {}".format(nonterminal, first[nonterminal]))
