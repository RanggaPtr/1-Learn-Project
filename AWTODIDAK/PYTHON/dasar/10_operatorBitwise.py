# operator bitwise,operasi biner,binary
a=9
b=5

# operasi bitwise:
print("Operasi bitwise: \n")
# | (bitwise OR)
c=a|b
print("================OR================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("nilai b :",b,", binary =",format(b,"08b"))
print("---------------------------------(|)")
print("nilai c :",c,", binary =",format(c,"08b"))
print('\n')

# & (bitwise AND)
c=a&b
print("=================AND================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("nilai b :",b,", binary =",format(b,"08b"))
print("---------------------------------(&)")
print("nilai c :",c,", binary =",format(c,"08b"))
print('\n')
# ^ (bitwise XOR)
c=a^b
print("=================XOR================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("nilai b :",b,", binary =",format(b,"08b"))
print("---------------------------------(^)")
print("nilai c :",c,", binary =",format(c,"08b"))
print('\n')


# ~ (bitwise NOT)
c=~a
print("=================NOT================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("---------------------------------(~)")
print("nilai c :",c,", binary =",format(c & 0xFF, '08b'))
print('\n')


# << (bitwise left shift)
c=a<<2
print("=================LEFT SHIFT================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("---------------------------------(<<)")
print("nilai c :",c,", binary =",format(c,"08b"))
print('\n')


# >> (bitwise right shift)
c=a>>2
print("=================RIGHT SHIFT================")
print("nilai a :",a,", binary =",format(a,"08b"))
print("---------------------------------(>>)")
print("nilai c :",c,", binary =",format(c,"08b"))
print('\n')

