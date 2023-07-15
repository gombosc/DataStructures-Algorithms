take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]

def first_come_first_served( take_out_orders, dine_in_orders, served_orders, take_out_index=0, dine_in_index=0, served_orders_index=0):
    if served_orders_index == len(served_orders):
        print("Done")
        return True
    
    if take_out_index < len(take_out_orders) and served_orders[served_orders_index] == take_out_orders[take_out_index]:
        take_out_index+=1
    elif ( dine_in_index < len(dine_in_orders) and served_orders[served_orders_index] == dine_in_orders[dine_in_index] ):
        dine_in_index+=1
    else:
        return False
    
    served_orders_index+=1
    return first_come_first_served(take_out_orders, dine_in_orders, served_orders, take_out_index, dine_in_index, served_orders_index)

first_come_first_served(take_out_orders, dine_in_orders, served_orders)

# This takes O(n) space in the call stack because of the recursion, we could write it as an iterative algo