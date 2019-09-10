def rabbit_traverse(garden):
    # Find starting cell
    # Dead center if possible
    row_width =  len(garden)
    col_width = len(garden[0])
    center = [row_width // 2, col_width // 2]
    candidates = [center]
    # If not, find all possible candidates then pick the larges
    if not row_width % 2:
        candidates.append([center[0] - 1, center[1]])
    if not col_width % 2:
        candidates.append([center[0], center[1] - 1])
    if not row_width % 2 and not col_width % 2:
        candidates.append([center[0] - 1, center[1] - 1])
    for candidate in candidates:
        if garden[candidate[0]][candidate[1]] > garden[center[0]][center[1]]:
            center = candidate
    ate_sum = 0
    seen = set()
    center = tuple(center)
    # Walk through adjacent candidates and pick largest
    while center:
        seen.add(center)
        ate_sum += garden[center[0]][center[1]]
        options = [tuple([center[0] + 1, center[1]]), tuple([center[0] - 1, center[1]]), tuple([center[0], center[1] + 1]), tuple([center[0], center[1] - 1])]
        center = None
        curr_max = float("-inf")
        for option in options:
            # Check if the option's x or y is out of bounds and if it's been previously used and if the cell is none zero
            if not option in seen and 0 <= option[0] <= row_width - 1 and 0 <= option[1] <= col_width - 1 and garden[option[0]][option[1]] >= curr_max and garden[option[0]][option[1]] != 0:
                center = option
                curr_max = garden[option[0]][option[1]]
    return ate_sum



    
    
    