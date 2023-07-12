# Write a function that takes a list of characters and reverses the letters in place. 
list_of_characters = ['a', 'b', 'c', 'd', 'e']

def reverse_characters(list_of_characters):
    left_index = 0
    print(f'Length of list_of_characters: {len(list_of_characters)}')
    right_index = len(list_of_characters) - 1

    while left_index < right_index:
        # Swap Characters
        # Line Continuation Character: \ is used to continue a statement to the next line
        # The following code is destructive, meaning it changes the original list_of_characters (in place)
        # Next line is unpacking the tuple 
        list_of_characters[left_index], list_of_characters[right_index] = \
            list_of_characters[right_index], list_of_characters[left_index]

        # Move towards middle
        left_index += 1
        right_index -= 1
    print(list_of_characters)
    return list_of_characters
 

reverse_characters(list_of_characters)