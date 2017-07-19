

if __name__ == "__main__":
  fruitPrice = {"Apple": 100, "Cherry": 75, "Banana": 150}
  cherries = []

  price = 0
  while True:
    res = raw_input("")

    fruits = res.replace(" ", "").split(",")

    for fruit in fruits:
        if fruit == "Cherry":
            cherries.append(fruit)

        price += fruitPrice.get(fruit, 0)

        if len(cherries) == 2:
            price = price - 20
            cherries = []

    print price

