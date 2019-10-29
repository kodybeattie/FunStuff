#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
#of rows like this: (you may want to display this pattern in a fixed font for
#better legibility)
#
#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: "PAHNAPLSIIGYIR"
#
#Write the code that will take a string and make this conversion given a
#number of rows:

def zigzag_convert(s, numRows):
    rows = []
    for row in range(numRows):
        rows.append([])
    index = 0
    add = True
    for char in s:
        rows[index].append(char)
        if add == False:
            index = index - 1
        else:
            index = index + 1
        if index == (numRows-1):
            add = False
        if index == 0:
            add = True
    zigzag = ""
    for row in rows:
        zigzag += ''.join(row)
    return zigzag

if __name__ == "__main__":
    print(zigzag_convert("PAPA",4))
