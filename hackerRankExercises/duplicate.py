lst = [1,2,2,2,4,5,1,2,3,4,5,6]

def find_duplicate(lst):
    seen = set()
    duplicates = set()
    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)
print(find_duplicate(lst))
# Another approach using collections.Counter

import collections
def find_duplicate_counter(lst):
    count = collections.Counter(lst)
    return [num for num, freq in count.items() if freq > 1]
print(find_duplicate_counter(lst))