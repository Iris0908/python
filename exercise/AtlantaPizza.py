# AtlantaPizza.py - a simper pizza cost calculator

# Ask the person how many pizzas they want, get the number with eval()
number_of_pizzas = eval(input("请问你要多少个比萨？ "))

# Ask for the menu cost of each pizza
cost_per_pizza = eval(input("请问一个比萨多少元？ "))

subtotel = number_of_pizzas * cost_per_pizza

tax_rate = 0.08

tax = subtotel * tax_rate

tax_price = tax + subtotel

print("你的总价是",tax_price,"元，","你需要交的税是",tax,"元，","你的比萨的原价是",subtotel,"元。")
