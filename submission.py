def sum_of_intervals(intervals):
    # Sort intervals by their start points
    intervals.sort(key=lambda x: x[0])
    
    merged_intervals = []
    for start, end in intervals:
        # If the list of merged intervals is empty or no overlap
        if not merged_intervals or merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            # There is an overlap, merge intervals
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
    
    # Calculate the total length of merged intervals
    total_length = sum(end - start for start, end in merged_intervals)
    return total_length

            
        
