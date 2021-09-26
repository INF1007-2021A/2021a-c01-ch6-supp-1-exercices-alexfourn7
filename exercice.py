#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	liste_finale = []
	for liste in numbers:
		liste_finale.append(max(liste))

	return liste_finale

def join_integers(numbers):
	new_integer = ""
	for element in numbers:
		new_integer += str(element)

	return int(new_integer)

def generate_prime_numbers(limit):
	premiers = []
	nombres = []
	for i in range(2, limit+1):
		nombres.append(i)

	while len(nombres) > 0:
		premiers.append(nombres[0])
		for i in nombres:
			if i % nombres[0] == 0:
				nombres.remove(i)

	print(4 % 2)
	return premiers



def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	combinaison = []
	for s in strings:
		for i in range(1, num_combinations+1):
			if excluded_multiples == None:
				combinaison.append(s + str(i))

			elif i % excluded_multiples != 0:
				combinaison.append(s+str(i))

			else:
				continue



	return combinaison

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
