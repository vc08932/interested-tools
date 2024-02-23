import random
def encode(string):
    string = str(string)
    code = []

    for i in range(len(string)):
        
        pointer = random.randint(1,9)
        hex_unicode = list(hex(ord(string[i]) + pointer)[2:])  # (Str + Pointer) --> Hex
        
        for k in range(0, len(hex_unicode)):
            if hex_unicode[k].isdigit() == True:
                hex_unicode[k] = chr(int(hex_unicode[k]) + 105)
        
        ciphertext = "".join(hex_unicode)
                
        code.append(chr(pointer + 65) + ciphertext + "Z") # ASCII --> Character
    return "".join(code)

def decode(string):
    string = str(string)
    text = []

    string = string.split("Z")

    
    for j in range(len(string)):
        hex_code , int_code = "", ""
        
        if string[j] == "":
            string.pop(j)
            continue
            
        pointer = ord(string[j][0])  - 65
        
        for i in range(1,len(string[j])):
            hex_code += str("{}").format((ord(string[j][i]) - 105) 
                                            if ord(string[j][i]) >= 105 
                                            else string[j][i])
            # If the character is hex (ASCII > 105), remains unchanged. Otherwise, minus 105

        text.append(chr(int(hex_code,16) - pointer)) 
    return "".join(text)

# while True:
#     string = str(input("Text:"))

#     string = encode(string)
#     print("密文：",string,"\n-")
#     print("原文：",decode(string))