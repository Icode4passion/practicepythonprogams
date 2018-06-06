# # word_list = ["red","yellow","green","red","blue","green","orange"]
# # unique_word = []
# # for word in word_list:
# # 	if word not in unique_word:
# # 		unique_word+=[word]

# # word_frequency = []

# # for word in unique_word:
# # 	word_frequency += [float(word_list.count(word))/len(word_list)]

# # for i in range(len(unique_word)):
# # 	print unique_word[i]
# # 	print word_frequency[i]


# # 	


# word_list = ['words', 'other', 'words']
# # Get a set of unique words from the list
# word_set = set(word_list)
# # create your frequency dictionary
# freq = {}
# # iterate through them, once per unique word.
# for word in word_set:
#     freq[word] = word_list.count(word) / float(len(word_list))

# print freq



test_string = raw_input("Enter a String")
l = []
l = test_string.split(' ')
word_feq = [l.count(p) for p in l]
print dict(zip(l,word_feq))