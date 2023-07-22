def checkPalindrome():
    string = "malayalam"
    answer = isPalindrom(string)
    if(answer):
        print("It is a palindrom")
    else:
        print("It is not a palindrom")

# Method 1 using inbuilt method
'''
def isPalindroem(string):
    if(string == string[::-1]):
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
'''

# Method 2 using while loop
'''
def isPalindrom(string):
    status = 1 # 1 means true and 0 means false
    length = len(string)
    start = 0
    end = length - 1
    while(start < end): 
        if(string[start] == string[end]): 
            start += 1
            end -= 1   
            status = 1
        else:
            status = 0
            break
    return status
'''

# Method 3 using for loop
'''
def isPalindrom(string):
    lenght = len(string)
    middleLen = len(string) // 2 
    for i in range(middleLen):
        if(string[i] != string[lenght - i - 1]):
            return False
    return True
'''

# Method 4 using recursion

def isPalindrom(string):
    length = len(string)
    if(length < 2):
        return True
    elif(string[0] != string[length - 1]):
        return False
    else:
        return isPalindrom(string[1: length - 1])

checkPalindrome()
    