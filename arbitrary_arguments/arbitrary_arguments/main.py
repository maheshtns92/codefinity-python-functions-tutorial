def calculate_total(*prices):
    if prices == ():
        return "Your cart is empty."

    total = sum(prices)

    if total >= 200:
        total = total - 0.2 * total # 20% discount
    elif total >= 100:
        total = total - 0.1 * total  # 10% discount

    return f"Final total: ${total:.2f}"

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())