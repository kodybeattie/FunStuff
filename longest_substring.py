#Given a string, find the length of the longest substring without repeating characters
def longest_substring(longStr):
    good = []
    temp = ""
    for i in range(len(longStr)):
        if longStr[i] not in temp:
            temp = temp + longStr[i]
        else:
            good.append(temp)
            temp = longStr[i]
    good.append(temp)
    return max(good, key=len)

if __name__ == "__main__":
    print (longest_substring("abbcdeenklop"))
