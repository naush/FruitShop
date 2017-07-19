

if __name__ == "__main__":
  fruitPrice = {"Apple": 100, "Cherry": 75, "Banana": 150}
  # fruitDiscounts = {"Cherry": [2, 20, 0]}
  cherries = []

  price = 0
  while True:
    res = raw_input("")

    if res == "Cherry":
        cherries.append(res)

    price += fruitPrice.get(res, 0)

    # fruitDiscount = fruitDiscounts.get(res, [])

    if len(cherries) == 2:
        price = price - 20
        cherries = []

    print price

