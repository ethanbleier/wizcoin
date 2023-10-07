from wizcoin import WizCoin

purse = WizCoin(2, 5, 99)
print(purse)
print("G:", purse.galleons, "S:", purse.sickles, "K:", purse.knuts)
print("Total value: ", purse.value())
print("Total weight: ", purse.weight_in_grams(), "grams")
print("\n")

coinJar = WizCoin(13, 0, 0)
print(coinJar)
print("G:", coinJar.galleons, "S:", coinJar.sickles, "K:", coinJar.knuts)
print("Total value: ", coinJar.value())
print("Total weight: ", coinJar.weight_in_grams(), "grams")
print("\n")
