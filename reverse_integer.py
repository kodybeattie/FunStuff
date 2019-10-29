#Given a 32-bit signed integer, reverse digits of an integer.
def reverse_integer(n):
    return (int(str(n)[::-1]))

if __name__ == "__main__":
    print (reverse_integer(876))
