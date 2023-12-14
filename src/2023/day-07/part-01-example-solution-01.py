#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
Solution of the AoC 2023, day 7.
"""


def get_precedence_cards():
    return ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def get_hand_type(hand: str):
    unique_cards = set(hand)
    cards_repeated = []
    for unique_card in unique_cards:
        cards_repeated.append(hand.count(unique_card))
    cards_repeated.sort()

    card_type = 0
    if cards_repeated == [1, 1, 1, 1, 1]:
        card_type = 1
    elif cards_repeated == [1, 1, 1, 2]:
        card_type = 2
    elif cards_repeated == [1, 2, 2]:
        card_type = 3
    elif cards_repeated == [1, 1, 3]:
        card_type = 4
    elif cards_repeated == [2, 3]:
        card_type = 5
    elif cards_repeated == [1, 4]:
        card_type = 6
    elif cards_repeated == [5]:
        card_type = 7

    return card_type


def get_transformed_hand(hand):
    precedence_cards = get_precedence_cards()[::-1]
    hand_converted = ''
    for card in hand:
        new_character = chr(ord('A') + precedence_cards.index(card))
        hand_converted += new_character

    return hand_converted


def sort_cards_in_hand(hands_and_bids):
    hands_with_details = []

    for hand_and_bid in hands_and_bids:
        hand, bid = hand_and_bid
        hand_type = get_hand_type(hand)
        transformed_hand = get_transformed_hand(hand)
        unique_hand_dict = {
            'transformed_hand': transformed_hand,
            'hand_type': hand_type, 'hand': hand, 'bid': bid
        }
        hands_with_details.append(unique_hand_dict)

    hands_sorted = hands_with_details.copy()
    hands_sorted.sort(key=lambda k: (k['hand_type'], k['transformed_hand']))

    return hands_sorted


def get_total_winnings(ranked_hands):
    total = 0
    for ranked_hand_index, ranked_hand in enumerate(ranked_hands):
        multipy_rank = ranked_hand['bid'] * (ranked_hand_index + 1)
        total += multipy_rank
        print(f'{ranked_hand_index}: {ranked_hand}'
              f' | {ranked_hand["bid"]} * {ranked_hand_index + 1} = {multipy_rank}'
              f' | {total}')

    return total


if __name__ == '__main__':
    hands_and_bids = (
        ('32T3K', 765),
        ('T55J5', 684),
        ('KK677', 28),
        ('KTJJT', 220),
        ('QQQJA', 483),
    )

    sorted_hands = sort_cards_in_hand(hands_and_bids)
    # print(f'sorted_hands: {sorted_hands}')

    total_winnings = get_total_winnings(sorted_hands)
    print(f'total_winnings: {total_winnings}')
