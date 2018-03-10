if __name__ == '__main__':
    n = int(raw_input())
    result = []
    for _ in xrange(n):
        s = raw_input().split(' ')
        command = s[0]
        if command == 'print':
            print result
            continue

        args = map(int, s[1:])
        getattr(result, command)(*args)
