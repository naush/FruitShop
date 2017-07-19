

if __name__ == "__main__":
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

  price = 0
  while True:
    res = raw_input("")

    fruits = res.replace(" ", "").split(",")

    for fruit in fruits:
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

    print price

