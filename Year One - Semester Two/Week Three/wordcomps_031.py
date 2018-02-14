import sys

words = sys.stdin.readlines()

def contains(s, f):
	for c in s:
		if c in f:
			f = f.replace(c,'',1)
		else:
			return False
	return True


print ('Words containing 17 letters: {}'.format([word.strip() for word in words if len(word.strip()) == 17]))


print ('Words containing 18+ letters: {}'.format([word.strip() for word in words if len(word.strip()) >= 18]))


shortest = 'aa' * 9999999
for word in [word for word in words if contains('aeiou', word.strip().lower())]:
    if len(word) < len(shortest):
        shortest = word

print ("Shortest word containing all vowels: {}".format(shortest.strip()))


print ("Words with 4 a's: {}".format([word.strip() for word in words if contains('aaaa', word.strip().lower())]))


print ("Words with 2+ q's: {}".format([word.strip() for word in words if contains('qq', word.strip().lower())]))


print ("Words containing cie: {}".format([word.strip() for word in words if 'cie' in word.strip().lower()]))


print ("Anagrams of angle: {}".format([word.strip() for word in words if sorted('angle') == sorted(word.strip().lower()) and word.lower().strip() != 'angle']))


print ("Words ending in iary: {}".format(len([word.strip() for word in words if word.strip()[-4:] == 'iary'])))


print ("Words with q but no u: {}".format([word.strip() for word in words if contains('q', word.strip().lower()) and not contains('u', word.strip().lower())]))


most_e = [[]]
num_e = 0
for word in [word for word in words if contains('e', word.strip().lower())]:
    counter = 0
    for c in word:
        if c == 'e':
            counter = counter + 1

    if counter > num_e:
        num_e = counter
        most_e[0] = word.strip()

for word in [word for word in words if contains('e', word.strip().lower())]:
    counter = 0
    for c in word:
        if c == 'e':
            counter = counter + 1

    if counter == num_e and word.strip() != most_e[0].strip():
        most_e.append(word.strip())

print ("Words with most e's: {}".format(most_e))
