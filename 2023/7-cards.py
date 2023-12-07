import re

cards = list(open("2023/7-cards.txt"))
rank = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def alter(result, count):
    for k, v in result.items():
        if v == max(result.values()):
            result[k] += count
            return result

def hand_type(hand):
    if 'J' in hand:
        count = hand.count('J')
        if count != 5:
            hand = hand.replace('J', '')
        result = dict((i, hand.count(i)) for i in hand)
        result = alter(result, count)
    else:    
        result = dict((i, hand.count(i)) for i in hand)
        
    if len(result.keys()) == 1:
        i = 7
    if len(result.keys()) == 2 and 4 in result.values():
        i = 6
    if len(result.keys()) == 2 and 3 in result.values() and 2 in result.values():
        i = 5
    if len(result.keys()) == 3 and 3 in result.values():
        i = 4
    if len(result.keys()) == 3 and 2 in result.values():
        i = 3
    if len(result.keys()) == 4 and 2 in result.values():
        i = 2
    if len(result.keys()) == 5:
        i = 1

    return i

def ranking(cards1, cards2):
    hand1 = cards1.split(' ')
    hand2 = cards2.split(' ')
    for i in range(5):
        if rank.index(hand1[0][i]) > rank.index(hand2[0][i]):
            return cards1, cards2
        elif rank.index(hand1[0][i]) < rank.index(hand2[0][i]):
            return cards2, cards1
        else:
            continue

print(ranking('KTJJT 220\n', 'KK677 28\n'))

def compare(cards):
    for i in range(len(cards)):
        for j in range(len(cards)-i-1):
            hand1 = cards[j].split(' ')
            hand2 = cards[j+1].split(' ')
            if hand_type(hand1[0]) > hand_type(hand2[0]):
                cards[j], cards[j+1] = cards[j+1], cards[j]
            if hand_type(hand1[0]) == hand_type(hand2[0]):
                cards[j], cards[j+1] = ranking(cards[j], cards[j+1])
            # print(cards)
    return cards

result = compare(cards)
def score(rank):
    num = 0
    for i, j in enumerate(rank):
        n = re.findall(r"\d+", j.split(' ')[1])
        num += int(n[0]) * (i+1)

    return num

num = score(result)
print(num)