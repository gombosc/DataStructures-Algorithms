my_list = [3, 4, 6, 10, 11, 15]
alice_list = [1, 5, 8, 12, 14, 19]

def merge_lists(my_list, alice_list):
   merged_list_size = len(my_list) + len(alice_list)
   merged_list = [None] * merged_list_size
   print(f'Merged list: {merged_list}')

   current_index_mine = 0
   current_index_alice = 0
   current_index_merged = 0

   while current_index_merged < merged_list_size:

        is_my_list_exhausted = current_index_mine >= len(my_list)
        is_alice_list_exhausted = current_index_alice >= len(alice_list)

        if (not is_my_list_exhausted and 
            is_alice_list_exhausted or
            my_list[current_index_mine] < alice_list[current_index_alice] ):

            # Case: next comes from my list
            # My list must not be exhausted, and EITHER:
            # 1) Alice's list IS exhausted, or
            # 2) the current element in my list is less than the current element in Alice's list
            
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        
        else:
            # Case: next comes from Alice's list
            merged_list[current_index_merged] = alice_list[current_index_alice]
            current_index_alice += 1

   current_index_merged += 1
   return merged_list


# Edge cases to consider:
# 1. One or both of the input lists is 0 elements or 1 element
# 2. One of the lists is longer than the other
# 3. One of our lists runs out of elements before we're done merging

