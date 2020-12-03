# Assignment 7, Task 2
# Name: Andrew Stuber
# Collaborators: friends 
# Time Spent: no idea

from typing import Tuple, Set, List

Hand = Set[Tuple[str, str]]

#Subtask 1
def is_straight_flush(h: Hand) -> bool:
    h = list(h)
    straight_lst = []
    flush_lst = []
    flush_lst_set = []
    lowest_rank = 15
    count_straight = 1
    is_straight = False
    is_flush = False
    for i in range(len(h)):
        straight_lst.append(list(h[i]))
    #remove suit
    for i in range(len(straight_lst)):
        straight_lst[i].pop(0)
    #Checking if A should be 1 or 14
    if ['A'] in straight_lst and ['2'] in straight_lst:
        for j in range(len(straight_lst)):
            if straight_lst[j] == ['A']:
                straight_lst[j] = ['1']
            if straight_lst[j] == ['J']:
                straight_lst[j] = ['11']
            if straight_lst[j] == ['Q']:
                straight_lst[j] = ['12']
            if straight_lst[j] == ['K']:
                straight_lst[j] = ['13']
    else:
        for j in range(len(straight_lst)):
            if straight_lst[j] == ['A']:
                straight_lst[j] = ['14']
            if straight_lst[j] == ['J']:
                straight_lst[j] = ['11']
            if straight_lst[j] == ['Q']:
                straight_lst[j] = ['12']
            if straight_lst[j] == ['K']:
                straight_lst[j] = ['13']
    #Checking straight
    for j in range(len(straight_lst)):
        if int(straight_lst[j][0]) < lowest_rank:
            lowest_rank = int(straight_lst[j][0])
    for k in range(len(straight_lst)):
        if count_straight == 5:
            is_straight = True
        if [str(lowest_rank + 1)] in straight_lst:
            count_straight += 1
            lowest_rank += 1   
    #Checking flush
    for o in range(len(h)):
        flush_lst.append(list(h[o]))
    for p in range(len(flush_lst)):
        flush_lst[p].pop(1)
    for k in range(len(flush_lst)):
        flush_lst_set.append(tuple(flush_lst[k]))
    flush_lst_set = set(flush_lst_set)
    flush_lst_set = list(flush_lst_set)
    if len(flush_lst_set) == 1:
        is_flush = True
    else:
        is_flush = False       
    return is_straight and is_flush
    
def is_four_of_a_kind(h: Hand) -> bool:
    h = list(h)
    count_4 = 0
    four_lst = []
    four_lst_set = []
    temp_lst = []
    for i in range(len(h)):
        four_lst.append(list(h[i]))
    for j in range(len(four_lst)):
        four_lst[j].pop(0)
    for k in range(len(four_lst)):
        four_lst_set.append(tuple(four_lst[k]))
    four_lst_set = set(four_lst_set)
    four_lst_set = list(four_lst_set)
    for a in four_lst_set:
        temp_lst.append(list(a))
    four_lst_set = temp_lst
    for o in range(len(four_lst_set)):
        for p in range(len(four_lst)):
            if four_lst_set[o] == four_lst[p]:
                count_4 += 1
        if count_4 == 4:
            return True
        count_4 = 0
    return False

def is_full_house(h: Hand) -> bool:
    h = list(h)
    house_lst = []
    house_lst_set = []
    for i in range(len(h)):
        house_lst.append(list(h[i]))
    for j in range(len(house_lst)):
        house_lst[j].pop(0)
    for k in range(len(house_lst)):
        house_lst_set.append(tuple(house_lst[k]))
    house_lst_set = set(house_lst_set)
    house_lst_set = list(house_lst_set)
    if not is_four_of_a_kind(set(h)) and len(house_lst_set) == 2:
        return True
    else:
        return False
    
def is_two_pair(h: Hand) -> bool:
    h = list(h)
    pair_lst = []
    pair_lst_set = []
    count_pair = 0
    lst_count_pair = []
    for i in range(len(h)):
        pair_lst.append(list(h[i]))
    for j in range(len(pair_lst)):
        pair_lst[j].pop(0)
    for k in range(len(pair_lst)):
        pair_lst_set.append(tuple(pair_lst[k]))
    pair_lst_set = set(pair_lst_set)
    pair_lst_set = list(pair_lst_set)
    for o in range(len(pair_lst_set)):
        for p in range(len(pair_lst)):
            rank = list(pair_lst_set[o])
            if rank == pair_lst[p]:
                count_pair += 1
        lst_count_pair.append(count_pair)
        count_pair = 0
    lst_count_pair = sorted(lst_count_pair)
    lst_count_pair = lst_count_pair[1:]
    if lst_count_pair[0] == 2 and lst_count_pair[1] == 2:
        return True
    else:
        return False

#Subtask 2
def all_hands() -> List[Hand]:
    rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suit = ['Spade','Club','Diamond','Heart']
    card = []
    for i in range(len(suit)):
        for j in range(len(rank)):
            card.append((suit[i], rank[j]))
    def combinations(deck, card_hand):
        if card_hand == 0:
            return [set()]
        else:
            hands = []
            for i in range(len(deck)):
                first_card = deck[i]
                other_card = deck[i+1:]
                rest_of_hand = combinations(other_card, card_hand - 1)
                for j in rest_of_hand:
                    set_of_hand = set([first_card])|j
                    hands.append(set_of_hand)
            return hands
    total_hands = combinations(card, 5)
    return total_hands

def all_straight_flush() -> List[Hand]:
    hands = all_hands()
    lst = []
    for i in hands:
        if is_straight_flush(i):
            lst.append(i)
    return lst
   
def all_four_of_a_kind() -> List[Hand]:
    hands = all_hands()
    lst = []
    for i in hands:
        if is_four_of_a_kind(i):
            lst.append(i)
    return lst

def all_full_house() -> List[Hand]:
    hands = all_hands()
    lst = []
    for i in hands:
        if is_full_house(i):
            lst.append(i)
    return lst

def all_two_pair() -> List[Hand]:
    hands = all_hands()
    lst = []
    for i in hands:
        if is_two_pair(i):
            lst.append(i)
    return lst











    

