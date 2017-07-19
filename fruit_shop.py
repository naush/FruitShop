fruitPrice = {
        "Apple": 100,
        "Manzana": 100,
        "Pomme": 100,
        "Cherry": 75,
        "Banana": 150
        }
discount = {
        "Apple": [3, lambda x: x, 0],
        "Manzana": [2, lambda x: x, 0],
        "Cherry": [2, lambda x: x + 75 - 20, 0],
        "Banana": [3, lambda x: x, 0]
        }

def add_fruit(price, fruit):
    if fruit in discount:
        dc = discount[fruit]
        dc[2] += 1

        if dc[0] == dc[2]:
            price = dc[1](price)
            dc[2] = 0
        else:
            price += fruitPrice.get(fruit, 0)
    else:
        price += fruitPrice.get(fruit, 0)

    return price

totalFruitCount = 0
def five_fruits_for_one(price, fruit):
    global totalFruitCount
    totalFruitCount += 1
    if totalFruitCount == 5:
        price = price - 200
        totalFruitCount = 0
    return price

appleCount = 0
def four_apples_discount(price, fruit):
    global appleCount
    if fruit in ["Apple", "Manzana", "Pomme"]:
        appleCount += 1
        if appleCount == 4:
            price = price - 100
            appleCount = 0
    return price


if __name__ == "__main__":
  price = 0
  while True:
    res = raw_input("")

    fruits = res.replace(" ", "").split(",")

    for fruit in fruits:
        price = add_fruit(price, fruit)
        price = five_fruits_for_one(price, fruit)
        price = four_apples_discount(price, fruit)

    print price

