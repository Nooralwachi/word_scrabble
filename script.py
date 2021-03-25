# Find the longest words in a given list of words that can be constructed from a given list of letters.
#   Your solution should take as its first argument the name of a plain text file that contains one word per line.
#   The remaining arguments define the list of legal letters. A letter may not appear in any single word more times than it appears in the list of letters.
# Example input: :~$ script.py filename  a c t 
# File contains:

# at
# act
# art
# cat
# Tat
# Tac

# Script returns [act, cat]

# prompt> scrabble.py WORD.LST w g d a s x z c y t e i o b
# WORD.LST:
# azotised
# bawdiest
# dystocia
# geotaxis
# iceboats
# oxidates
# oxyacids
# sweatbox
# tideways

# Output:
# ['azotised', 'bawdiest', 'dystocia', 'geotaxis', 'iceboats', 'oxidates', 'oxyacids', 'sweatbox', 'tideways']

def word_scrabble(filename,letters):
	with open(filename, 'r') as file:
		maximum =0
		result=[]
		words  = [line.strip() for line in file]
		for word in words:
			check = list(letters)
			flag = True
			length = len(word)
			for char in word:
				if char in check:
					check.remove(char)
				else:
					flag = False
			if flag:
				if maximum <length:
					result=[]
					result.append(word)
					maximum = length
				else:
					result.append(word)
					flag= True
		print(result)
letters_a = ['a','c','t','x']
word_scrabble('words_allowed2.txt', letters_a)
letters_b = ['w','g','d','a','s','x','z','c','y','t','e','i','o','b']
word_scrabble('words_allowed1.txt', letters_b)
letters = ['a', 'b','o','o','g','k', 'x','l', 't']
word_scrabble('words_allowed3.txt', letters)
