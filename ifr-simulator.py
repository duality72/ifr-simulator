#!/usr/bin/env python
from math import factorial
def nCombinations(n, r):
    return int(factorial(n)/factorial(n-r)/factorial(r))
import argparse
parser = argparse.ArgumentParser(description='Infection rate simulator')
parser.add_argument('num_party', type=int, help='number of people at the party')
args = parser.parse_args()


ASYMPTOMATIC_INFECTED_CHANCE = 0.0033
NON_INFECTED_CHANCE = 1 - ASYMPTOMATIC_INFECTED_CHANCE
INFECTION_RATE = 0.25
UNINFECTION_RATE = 1 - INFECTION_RATE

party_sim = ['U'] * args.num_party

def num_new_infected(group):
	num_infected = group.count('I')
	chance_of_remaining_uninfected = UNINFECTION_RATE / num_infected if num_infected > 0 else 1
	chance_of_getting_infected = 1 - chance_of_remaining_uninfected
	return group.count('U') * chance_of_getting_infected

def add_infected(group):
	to_change = group.index('U')
	group[to_change] = 'I'

def chance_of_this_permutation(group):
	result = 1
	for item in group:
		result *= ASYMPTOMATIC_INFECTED_CHANCE if item is 'I' else NON_INFECTED_CHANCE
	return result * nCombinations(len(group), group.count('I'))

expected_infections = 0
total_chance = 0
while True:
	new_infections = num_new_infected(party_sim)
	chance = chance_of_this_permutation(party_sim)
	print("{} {:5.2f} infections {:.2%}".format(party_sim, new_infections, chance))
	expected_infections += new_infections * chance
	total_chance += chance
	if 'U' not in party_sim:
		break
	add_infected(party_sim)

print("Total simulation chance: {}".format(total_chance))
print("Expected new infections: {}".format(expected_infections))
