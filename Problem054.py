from timeit import default_timer as timer
from collections import Counter

def poker(filename):
	with open(filename) as f:
		content = f.readlines()
		for i in range(len(content)):
			content[i] = content[i][:-1]
	one_wins = 0
	card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	for i in content:
		player_one = i[:14].split(' ')
		player_two = i[15:].split(' ')
		if check_winner(player_one, player_two, card_ranks):
			one_wins += 1
			print(p1, p2, "One Wins!")
	return one_wins

def check_winner(p1, p2, card_ranks):
	p1_ranks = [i[0] for i in p1]
	p1_suits = [i[1] for i in p1]
	p2_ranks = [i[0] for i in p2]
	p2_suits = [i[1] for i in p2]
	p1_rank_count = dict(Counter(p1_ranks))
	p1_suit_count = dict(Counter(p1_suits))
	p2_rank_count = dict(Counter(p2_ranks))
	p2_suit_count = dict(Counter(p2_suits))
	if 5 in p1_suit_count.values() or 5 in p2_suit_count.values():
		if set(p1_ranks) == {'A', 'K', 'Q', 'J', '10'}:
			return 'p1'
		if set(p2_ranks) == {'A', 'K', 'Q', 'J', '10'}:
			return
		for i in range(6, -1, -1):
			if set(card_ranks[i:i+5]) == set(p1_ranks):
				return 'p1'
			if set(card_ranks[i:i+5]) == set(p2_ranks):
				return
	if 4 in p1_rank_count.values() or 4 in p2_rank_count.values():
		if not 4 in p2_rank_count.values():
			return 'p1'
		if not 4 in p1_rank_count.values():
			return
		if find_key(4, p1_rank_count) > find_key(4, p2_rank_count):
			return 'p1'
		return
	if {3, 2} == p1_rank_count or {3, 2} == p2_rank_count:
		if {3, 2} != p2_rank_count:
			return 'p1'
		if {3, 2} != p1_rank_count:
			return
		if find_key(3, p1_rank_count) > find_key(3, p2_rank_count):
			return 'p1'
		return
	if 5 in p1_suit_count.values() or 5 in p2_suit_count.values():
		if 5 not in p2_suit_count.values():
			return 'p1'
		if 5 not in p1_suit_count.values():
			return
		for i in card_ranks[::-1]:
			if i in set(p1_ranks):
				return 'p1'
			if i in set(p2_ranks):
				return
	for i in range(7, -1, -1):
		if set(card_ranks[i:i+5]) == set(p1_ranks):
			return 'p1'
		if set(card_ranks[i:i+5]) == set(p2_ranks):
			return
	if 3 in p1_rank_count.values() or 3 in p2_rank_count.values():
		if not 3 in p2_rank_count.values():
			return 'p1'
		if not 3 in p1_rank_count.values():
			return
		if find_key(3, p1_rank_count) > find_key(3, p2_rank_count):
			return 'p1'
		return
	try Counter(p1_rank_count.values())[2] == 2:
		if Counter(p1_rank_count.values())[2] == 2 or Counter(p2_rank_count.values())[2] == 2:
			if Counter(p2_rank_count.values())[2] != 2:
				return 'p1'
			if Counter(p1_rank_count.values())[2] != 2:
				return
			for i in card_ranks[::-1]:
				if p1_rank_count[i] == 2 or p2_rank_count[i] == 2:
					if p2_rank_count[i] != 2:
						return 'p1'
					if p1_rank_count[i] != 2:
						return
			for i in card_ranks[::-1]:
				if i in p1_ranks:
					return 'p1'
				if i in p2_ranks:
					return
	except KeyError:
		pass
	if 2 in p1_rank_count.values() or 2 in p2_rank_count.values():
		if 2 not in p2_rank_count.values():
			return 'p1'
		if 2 not in p2_rank_count.values():
			return
		if find_key(2, p1_rank_count) > find_key(2, p2_rank_count):
			return 'p1'
		if find_key(2, p1_rank_count) < find_key(2, p2_rank_count):
			return
		for i in card_ranks[::-1]:
			if i in set(p1_ranks):
				return 'p1'
			if i in set(p2_ranks):
				return
	for i in card_ranks[::-1]:
		if i in p1_ranks:
			return 'p1'
		if i in p2_ranks:
			return

		

def find_key(value, d):
	for i in d:
		if d[i] == value:
			return i
	return 0

start = timer()
print(poker("p054_poker.txt"))
end = timer()
print("Time: ", end - start)