"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    Write a Python program, which returns a list with 2-tuples. 
    Each tuple consists of a the order number and the product of the price per items 
    and the quantity. 
    The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

"""

    
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]      

min_order = 100

order_summary = list(map(lambda x: (x[0], round(x[3] * x[4],2)), orders))

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), order_summary))
print(invoice_totals)
# or 

invoice_totals = list(map(lambda x: x if x[1] >= min_order else (x[0], x[1] + 10), 
                    map(lambda x: (x[0],x[2] * x[3]), orders)))

print(invoice_totals)



