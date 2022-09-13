inputWord = input("Input word: ")
word = inputWord

for i in range(len(inputWord)):
    if inputWord[i-1] == inputWord[-i]:
        word = inputWord[i:-i]
        print(word)

if len(word) <= 1:
    print(inputWord + " is a palindrom.")
else:
    print(inputWord + " is NOT a palindrom.")

#Samme kjøretid som oppgave 1a, av samme årsaker. Med en inputstørrelse på n,
#må inputordet kjøres gjennom n ganger for å fjerne alle like bokstaver.
#Kjøretid = O(n)