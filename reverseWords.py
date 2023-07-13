
""" --------------- --------------------- First attempt
 def reverse_words(message):
     word = ''
     new_message = []
     for index, x in enumerate(message):
         if(x == ' ' or index==len(message)):
             new_message.append(word)
             word = ''
             continue
         else: 
             word += x
     print(new_message)

 reverse_words(message)"""

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
# Reverse the order of the words in the message, in place
def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, len(message)-1) # This is a helper function

    """This gives us the right word order
       but with each word backward.
       Now we'll make the words forward again by reversing each word's characters"""

    current_word_start_index = 0

    for i in range(len(message) + 1):
        if(i == len(message) or message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            current_word_start_index = i + 1
    print(message)
            

def reverse_characters(message, left_index, right_index):
    while left_index < right_index:
        message[left_index], message[right_index] = message[right_index], message[left_index]
        left_index+=1
        right_index-=1

reverse_words(message)