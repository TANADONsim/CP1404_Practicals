word_list = input("Text: ").split()
word_dict = {}
# another way is to sort the words in alphabetical order before the loop
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for word in sorted(word_dict, key=str.lower):
    print(str(word) + ": " + str(word_dict[word]))