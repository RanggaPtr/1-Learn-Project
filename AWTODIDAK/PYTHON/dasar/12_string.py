# Pengenalan string
data = "ini adalah string"
print("data :", data, "\ntype :", type(data))

# Cara membuat string
# 1. Single quote '...'
data = 'ini adalah string'
print("data :", data, "\ntype :", type(data))

# 2. Double quote "..."
data = "ini adalah string"
print("data :", data, "\ntype :", type(data))

# 3. Triple quote '''...'''
data = '''
ini adalah string
yang panjang
'''
print("data :", data, "\ntype :", type(data))

# Menggunakan tanda \
print("\nPenggunaan tanda '\\'")
print("' :")
print("mari kita shalat jum'at")
print("g'day, isn't it?")
# Backslash
# print('C:\user\jarwo') # menggunakan tanda \ salah
print('C:\\user\\jarwo')

# Tab
print("\nPenggunaan tab \\t")
print("saya\tmakan")

# Backspace
print("\nPenggunaan backspace \\b")
print("halo \brangga")

# Newline
print("\nPenggunaan newline")
print("halo \n rangga") # RL Line Feed -> Mac OS
print("halo \r rangga") # CR Carriage Return
print("halo \r\n rangga") # CRLF Carriage Return Line Feed -> Windows

# Formatting
print("\nFormatting")
print("halo \t rangga")
print("halo \b rangga")

# String literal/raw
print("\nString literal/raw")
print("C:\\nuser\\jarwo")

# Menggunakan raw string
print(r'C:\nuser\jarwo')

# Multiline string
print("\nMultiline string")
print("""
nama : jarwo
umur : 18
hobi : nonton
""")

# Multiline literal raw
print("\nMultiline literal raw")
print(r"""  
nama : jarwo
umur : 18
hobi : nonton\mancing
laman url : www.google.com/newID
""")
