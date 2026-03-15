def apply_discount(price, discount):

    # check if price is a number
    if not isinstance(price, (int, float)):
        return "The price should be a number"

    # check if discount is a number
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"

    # check if price is valid
    if price <= 0:
        return "The price should be greater than 0"

    # check if discount is between 0 and 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"

    # calculate discount
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount

    return final_price