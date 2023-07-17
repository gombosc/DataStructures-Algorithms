my_list = [3, 4, 6, 10, 11, 15]
alice_list = [1, 5, 8, 12, 14, 19]


def merge_lists(my_list, alice_list):
    cookie_list = my_list + alice_list
    print(cookie_list)
    i = 1
    while i < len(cookie_list)-1:
        while cookie_list[i] < cookie_list[i+1] and i!=0:
            temp = cookie_list[i]
            cookie_list[i] = cookie_list[i-1]
            cookie_list[i-1] = temp
            i-=1
        i+=1
    print (cookie_list)

merge_lists(my_list, alice_list)