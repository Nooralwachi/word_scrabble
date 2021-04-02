

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
