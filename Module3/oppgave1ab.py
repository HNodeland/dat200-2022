
inputWord = input("Inpurt word: ")

def palindrom(word):
    if len(word) <= 1:
        print("done - " + inputWord + " is a palindrom.")
        
        return -1
    print(word)
    if word[0] == word[-1]:
        return palindrom(word[1:-1])
    else:
        print("Not a palindrom")

palindrom(inputWord)
#Kjøretid avhenger av størrlesen på input. Hvis vi har input med lengde n, 
#er kjøretiden O(n), ettersom vi fjerner 2 bokstaver for hver loop, og antallet
# bokstaver vi fjerner er konstant.
