'''
Created on Jul 20, 2017

@author: rjw0028
'''

'''

You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Do not use division in your solution.

'''



def get_products_of_all_ints_except_at_index():
    given_ints = [1, 0, 6, 5, 9]

    Products_List = []
    
    if len(given_ints) < 2:
        raise IndexError('We need at least 2 numbers in the list for this function...')
    
    
    
    for index, value in enumerate(given_ints):
        product = 1
        for item in range(len(given_ints)):
            if index == item:
                continue
            elif given_ints[item] == 0:
                product = 0
                break
            else:
                product *= given_ints[item] 
                           
        Products_List.append(product)
    
    print Products_List
    
    
    
get_products_of_all_ints_except_at_index()
 
    
    
    
    
    