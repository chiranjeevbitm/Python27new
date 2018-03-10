def split_and_join(line):
    result = line.split(" ")
    result = "-".join(result)
    # write your code here
    return result


if __name__ == '__main__':

    line = raw_input()

    result = split_and_join(line)

    print result
