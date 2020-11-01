
#Exercise 14.1

helloFile = open("hello.txt")
helloContent = helloFile.read()
print(helloContent)



def sed(string1, string2, file1, file2):
    tobeReplaced = open(file1, "r")
    withThis = open(file2, "w")

    for line in tobeReplaced:
        line = line.replace(string1, string2)
        withThis.write(line)

    tobeReplaced.close()
    withThis.close()


string1 = "Hello world!"
string2 = "fingers crossed!"
file1 = "hello.txt"
file2 = "helloOutput.txt"

sed(string1, string2, file1, file2)

helloOutput = open("helloOutput.txt")
helloOutputContent = helloOutput.read()
print(helloOutputContent)












    
    
