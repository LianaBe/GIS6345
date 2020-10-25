

#Exercise 11.1

fin = open("words.txt")

def dicttest():
    testdict = {}
    count = 0
    for line in fin:
        word = line.strip()
        testdict[word] = count
        count += 1
    return testdict

print(dicttest())
      

#Exercise 12.1

test = "banana"

def histogram(test):
    histdict = {}
    for letter in test:
        if letter not in histdict:
            histdict[letter] = 1
        else:
            histdict[letter] += 1
    return histdict

def most_frequent(test):
    histdict = histogram(test)
    histlist = []
    for letter, frequency in histdict.items():
        histlist.append((frequency, letter))
    histlist.sort(reverse = True)
    print(histlist)

print(most_frequent(test))


















