base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
is_member = True
is_weekend = False
discount = 0

if age > 17:
    print('User is eligible to book a ticket')


if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')


if is_member == True:
    discount = 3
    print('User qualifies for membership discount')