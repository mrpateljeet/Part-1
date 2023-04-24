# Define the priorities of each item type
def get_priority(c):
    if c.islower():
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27

# Reading in the list of rucksacks
rucksacks = []
with open('input.txt') as f:
    for line in f:
        rucksacks.append(line.strip())

# Iterate over each rucksack and find the item type that appears in both compartments
common_items = set()
for r in rucksacks:
    first_compartment = set(r[:len(r)//2])
    second_compartment = set(r[len(r)//2:])
    common = first_compartment.intersection(second_compartment)
    common_items.update(common)

# common item types
total = sum(get_priority(c) for c in common_items)

print(total)
