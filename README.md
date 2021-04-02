# word_scrabble
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
