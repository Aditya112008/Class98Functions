def countWordsFromFile() : 
        filename = input("enter the filename: ")
        file = open(filename , "r")
        numberOfWords = 0

        for line in file :
            words = line.split()
            print(words)
            numberOfWords = numberOfWords + len(words)
        print("number of words : ")
        print(numberOfWords)

countWordsFromFile()