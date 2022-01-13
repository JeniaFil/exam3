card = "1234123412341234"
def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]
print(card_hide(card))




