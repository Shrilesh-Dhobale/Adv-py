#Iterating through char
text="Python"
for char in text:
    ascii_code=ord(char)
    print(f"The Ascii code of '{text}' is {ascii_code}")

#Convering string to Ascii
text="Numpy"
ascii_list=[ord(char)for char in text]
print(f"Ascii code of character {text}:{ascii_list}")