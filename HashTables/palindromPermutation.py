word = 'civic'

def palindromPermutation(word):
    word = word.lower()
    word = word.replace(" ", "")
    
    unpaired_chars = set()

    for char in word:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)
    
    if(len(unpaired_chars) > 1):
        print("Not a palindrome permutation")
        return False
    else:
        print("Word is a Palindrome permutation")
        return True
    
palindromPermutation(word)