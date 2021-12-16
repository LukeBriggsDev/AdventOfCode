"""
--- Part Two ---

On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""

import os

from part_1 import BingoCard, cards_from_file


def get_score(input_file):
    with open(input_file) as f:
        txt = f.readlines()

    called_nums = [int(x) for x in txt[0].strip().split(",")]

    bingo_cards = cards_from_file(txt)

    winning_cards = []

    call = 0

    # While not all the cards have won
    while len(winning_cards) < len(bingo_cards):
        for card_index in range(len(bingo_cards)):
            if bingo_cards[card_index].dab_number(called_nums[call]) and card_index not in winning_cards:
                winning_cards.append(card_index)
                
        call += 1

    # Calculate score
    total = 0
    for row in bingo_cards[winning_cards[-1]].card:
        for col in row:
            if col != "CHECKED":
                total += col


    return total * called_nums[call-1]

    
if __name__ == "__main__":
    print(get_score(os.path.dirname(__file__) + "/input.txt"))