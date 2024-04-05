#As I misunderstood the question given, so I rewrite the functions for the question required.
#Which the first funtion is the read the input and create different combinations
#And the for loop is to find the minimum difference between these combinations 
def a2_q4(elements):
    def generate_combinations(elements, k):
        if k == 0:
            yield ()
        elif len(elements) == k:
            yield tuple(elements)
        else:
            for combo in generate_combinations(elements[1:], k - 1):
                yield (elements[0],) + combo
            for combo in generate_combinations(elements[1:], k):
                yield combo

    n = len(elements)
    k = n // 2
    min_diff = float('inf')
    min_combination = None

    for combo in generate_combinations(elements, k):
        group1 = set(combo)
        group2 = set(elements) - group1
        diff = abs(sum(group1) - sum(group2))
        if diff < min_diff:
            min_diff = diff
            min_combination = (group1, group2)

    result = {'group1': list(min_combination[0]),
              'group2': list(min_combination[1]),
              'diff': min_diff}
    
    return result