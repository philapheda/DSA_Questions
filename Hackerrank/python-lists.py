if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        a = input()
        com = list(a.split(" "))
        if com[0] == 'insert':
            l.insert(int(com[1]), int(com[2]))
        elif com[0] == 'print':
            print(l)
        elif com[0] == 'remove':
            l.remove(int(com[1]))
        elif com[0] == 'append':
            l.append(int(com[1]))
        elif com[0] == 'sort':
            l.sort()
        elif com[0] == 'pop':
            l.pop()
        elif com[0] == 'reverse':
            l.reverse()
