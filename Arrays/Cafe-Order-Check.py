take_out_orders = [17, 8, 24]
dine_in_orders = [12, 19, 2]
served_orders = [17, 8, 12, 19, 24, 2]

def first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_index = 0
    take_out_index_max = len(take_out_orders) -1 
    dine_in_index= 0
    dine_in_index_max =len(dine_in_orders) - 1
    response = ''

    for order in served_orders:
        if ( take_out_index <= take_out_index_max and order == take_out_orders[take_out_index] ):
            take_out_index+=1
        
        elif ( dine_in_index <= dine_in_index_max and order == dine_in_orders[dine_in_index]):
            dine_in_index+=1

        else:
            response = 'Not first come first served'
            print(response)
            return response
    
    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_index != len(dine_in_orders) or take_out_index != len(take_out_orders):
        print("False")
        return False
    
    # If all orders in served_orders have been "accounted for" so we're serving first-come, first-served!
    response = 'First Come First Served'
    print(response)
    return response

first_come_first_served(take_out_orders, dine_in_orders, served_orders)