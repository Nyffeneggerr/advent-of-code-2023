card_values = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}


def read_data():
    with open('data.txt') as file:
        return [line.rstrip() for line in file]


def get_value_from_hand(hand):
    card_with_value_counts = {}
    card_counts = []

    # char_count = 1
    # last_char = hand[0]
    # for x in range(1, 6):
    #     if x < 5:
    #         current_char = hand[x]
    #         if last_char == current_char:
    #             char_count += 1
    #         else:
    #             if char_count > 1:
    #                 card_counts.append(int(char_count))
    #                 char_count = 1
    #
    #         last_char = current_char
    #     else:
    #         if char_count > 1:
    #             card_counts.append(int(char_count))
    #
    # print(f'Hand {hand} results in {card_counts}')


    for card in card_values.keys():
        count = hand.count(card)
        if count > 1:
            card_with_value_counts[card] = count

    base_value = 0.0
    for x in range(5):
        hand_card_value = card_values[hand[x]] * (15**(6-x))
        # print(hand_card_value)
        base_value += hand_card_value

    base_value = base_value / 1_000_000_000

    card_counts = [x for x in card_with_value_counts.values()]
    # print(card_counts)

    if len(card_counts) == 2:
        if card_counts[0] == 2 and card_counts[1] == 2:
            #Two pairs
            base_value += 10
        elif card_counts[0] == 3 and card_counts[1] == 2:
            #Full House
            base_value += 1000
        elif card_counts[0] == 2 and card_counts[1] == 3:
            #Full House
            base_value += 1000
    elif len(card_counts) == 1:
        card_count = card_counts[0]
        if card_count == 5:
            #Five of a kind
            base_value += 100_000
        elif card_count == 4:
            #Four of a kind
            base_value += 10_000
        elif card_count == 3:
            #Three of a kind
            base_value += 100
        else:
            #one pair
            base_value += 1


    # One pair =                    1
    # Two pairs =                  10
    # Three =                     100
    # Full House =               1000
    # Four =                   10_000
    # Five =                 100_0000


    # print(hand + ' ' + str(card_count))
    return base_value


def take_third(elem):
    return float(elem[2])


if __name__ == '__main__':
    data = read_data()

    value_ranks = []

    for data_line in data:
        hand_and_bet = data_line.split()
        value = get_value_from_hand(hand_and_bet[0])
        hand_and_bet.append(str(value))
        value_ranks.append(hand_and_bet)

    print(value_ranks)
    value_ranks.sort(key=take_third)
    print(value_ranks)

    result = 0
    for x in range(len(value_ranks)):
        value = int(value_ranks[x][1]) * (x+1)
        print(f'{x}: Hand {value_ranks[x][0]} results in value {value} -> {value_ranks[x][2]}')
        # print(value)
        result += value

    print(result)


