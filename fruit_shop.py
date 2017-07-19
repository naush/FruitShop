if __name__ == "__main__":
  fruitPrice = {"Apple": 100, "Cherry": 75, "Banana": 150}

  price = 0
  while True:
    res = raw_input("")
    price += fruitPrice.get(res, 0)
    print price

