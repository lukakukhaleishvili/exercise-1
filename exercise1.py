n = int(input("enter number: "))
given_words = []
count_words = {}
for i in range(n):
    words = input()
    given_words.append(words)
for words in given_words:
    count_words[words] = 0

for words in given_words:
    count_words[words] +=1


print(len(count_words))

x = count_words.values()

for i in x:
    print(i, end=" ")
    



