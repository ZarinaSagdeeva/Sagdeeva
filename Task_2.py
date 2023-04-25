class Good:
    def __init__(self, name, price, weight, cost = 0):
        self.name = name
        self.price = price
        self.cost = cost
        self.weight = weight

    def calc(self):
        self.cost = self.price * self.weight

apple = Good('apple', 100, 1.5)
print(f'Имя товара: {apple.name}')
apple.calc()
print(f'Стоимость: {apple.cost} рублей')

print()

pear = Good('pear', 120, 0.8)
print(f'Имя товара: {pear.name}')
pear.calc()
print(f'Стоимость: {pear.cost} рублей')