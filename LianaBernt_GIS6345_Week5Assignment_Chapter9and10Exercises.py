
#Exercise 9.1

fin = open("words.txt")

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

#Exercise 9.2

fin = open("words.txt")

def has_no_e(word):
    if "e" in word:
        return False
    else:
        return True

count = 0
total = 0

for line in fin:
    word = line.strip()
    total += 1
    if has_no_e(word):
        count += 1
#        print(word)

print(str(round((count/total * 100),2)) + "% of words have no e")


#Exercise 10.1


t = [[1, 2, 3], [4, 5, 6]]

def nested_sum(n):
    total = 0
    for item in n:
        total += sum(item)
    print(total)

nested_sum(t)


#Exercise 10.2

t = [1, 2, 3]

def cumsum(n):
    cum_n = 0
    new_n = []
    for i in n:
        cum_n += i
        new_n.append(cum_n)
    print(new_n)

cumsum(t)








