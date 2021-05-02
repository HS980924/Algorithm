if __name__ == "__main__":
    N = int(input())
    Word = []

    for i in range(N):
        Word.append(input())
    
    Word = set(Word)
    Word = list(Word)

    Word.sort()
    Word.sort(key=len)

    for i in range(len(Word)): 
        print(Word[i])