# Big O: O(1) - Constant Time
def print_first_item(items):
    print(items[0])

# Big O: O(n) - Linear Time
def print_all_items(items):
    for item in items:
        print(item)

# Big O: O(n^2) - Quadratic Time
def print_all_possible_ordered_pairs(items):
    for first_item in items:
        for second_item in items:
            print(first_item, second_item)

bucket = [1,2,3,4,5,6,7,8,9,10]

print_all_possible_ordered_pairs(bucket)

# This is O(2n), which we just call O(n). 
def print_all_items_twice(items):
    for item in items:
        print(item)

    # Once more, with feeling
    for item in items:
        print(item)

# Worst Case
def contains(haystack, needle):
    # Does the haystack contain the needle?
    for item in haystack:
        if item == needle:
            return True

    return False
    
#  Here we might have 100 items in our haystack, but the first item might be the needle, in which case we would return in just 1 iteration of our loop.

# In general we'd say this is O(n) runtime and the "worst case" part would be implied. But to be more specific we could say this is worst case O(n) and best case O(1) runtime. For some algorithms we can also make rigorous statements about the "average case" runtime. 