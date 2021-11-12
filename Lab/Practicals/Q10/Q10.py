def CalFrequency(str):
    d = {} # empty dictionary
    
    for i in str :
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    return d

def main():
    sentence = input("Enter a Sentence :-\n")
    LetterCount = CalFrequency(sentence)

    print(sentence)
    print("Frequency count of each letter :- ")
    print(LetterCount)

if __name__=='__main__':
    main()

    
