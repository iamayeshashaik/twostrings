str1 = "EDYODA"
str2 = "YDEADO"

def string_Rotation(str1, str2):

    if len(str1) != len(str2):
        out = " "
        return False
  
    out = str1 + str1 
  
    if str1 in out: 
        print("\U0001F603 Strings are rotations of each other \U0001F603")
    else:
        print("\U0001F629 Strings are not rotations of each other \U0001F629")
  
string_Rotation(str1, str2)