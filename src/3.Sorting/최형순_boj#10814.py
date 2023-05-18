if __name__ == "__main__":
    N = int(input())
    Person = []

    for i in range(N):
        age, name = map(str,input().split())
        Person.append([int(age),name])

    Person.sort(key=lambda age : age[0])

    for age,name in Person:
        print(age,name)