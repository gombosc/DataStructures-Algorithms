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

