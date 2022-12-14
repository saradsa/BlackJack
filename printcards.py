def print_single(cards):

    s = ""
    s = s + "\t ________________"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    if cards.values == '10':
        s = s + "\t|  {}            |".format(cards.values)
    else:
        s = s + "\t|  {}             |".format(cards.values)
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|       {}        |".format(cards.suit_values)
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    s = s + "\t|                |"
    print(s)

    s = ""
    if cards.values == '10':
        s = s + "\t|            {}  |".format(cards.values)
    else:
        s = s + "\t|            {}   |".format(cards.values)
    print(s)

    s = ""
    s = s + "\t|________________|"
    print(s)

    print()


# Function to print both cards
def print_multi(cards):

    s = ""
    for card in cards:
        s = s + "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.values == '10':
            s = s + "\t|  {}            |".format(card.values)
        else:
            s = s + "\t|  {}             |".format(card.values)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit_values)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|                |"
    print(s)

    s = ""
    for card in cards:
        if card.values == '10':
            s = s + "\t|            {}  |".format(card.values)
        else:
            s = s + "\t|            {}   |".format(card.values)
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    print(s)

    print()


# function to print hidden card
def print_cards_hidden():

    s = ""
    s += "\t ________________"
    print(s)

    s = ""
    s += "\t|                |"
    print(s)

    s = ""
    s += "\t|                |"
    print(s)

    s = ""
    s += "\t|      * *       |"
    print(s)

    s = ""
    s += "\t|    *     *     |"
    print(s)

    s = ""
    s += "\t|   *       *    |"
    print(s)

    s = ""
    s += "\t|   *       *    |"
    print(s)

    s = ""
    s += "\t|          *     |"
    print(s)

    s = ""
    s += "\t|         *      |"
    print(s)

    s = ""
    s += "\t|        *       |"
    print(s)

    s = ""
    s += "\t|                |"
    print(s)

    s = ""
    s += "\t|                |"
    print(s)

    s = ""
    s += "\t|        *       |"
    print(s)

    s = ""
    s += "\t|________________|"
    print(s)

    print()
