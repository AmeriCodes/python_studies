"""
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
"""

def forty_discount(book_price ,copies=1):
    new_price = book_price - (book_price * 0.4)
    new_price *= copies
    total_price = new_price + 3 + ((copies - 1) * 0.75)
    return f'{total_price:.2f}'



book_price = 24.95
print(forty_discount(book_price, 60))