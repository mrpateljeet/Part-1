def count_fully_contained_pairs(section_assignments):
    # Split the input into individual pairs
    pairs = section_assignments.split('\n')
    
    # Initialize a counter for fully contained pairs
    fully_contained_count = 0
    
    # Loop through each pair of section assignement
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):
            pair1 = set(range(int(pairs[i].split('-')[0]), int(pairs[i].split('-')[1])+1))
            pair2 = set(range(int(pairs[j].split('-')[0]), int(pairs[j].split('-')[1])+1))
            
            # Check if either pair is fully contained within the other
            if pair1.issubset(pair2):
                fully_contained_count += 1
            elif pair2.issubset(pair1):
                fully_contained_count += 1
    
    return fully_contained_count

input_string = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'
print(count_fully_contained_pairs(input_string))
