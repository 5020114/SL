def substution_cipher(text, s):
    result=""
    k=int(s)
    for i in range( len(text) ):
        char= text[i]
        if( char.isupper() ):
            result+= chr( (ord(char) + k -65)%26 + 65) 
        else:
            result+= chr( ( ord(char) + k -97)%26 +97 ) 
    return result

text=input("Enter text:")
s=input("Enter key:")
sub= substution_cipher(text,s)

def transposition_cipher(text):
    result=""
    i=0
    length= len(text)
    while i< length:
        if i%2==0:
            result+= text[i]
        i+=1
    i=1
    while i< length:
        if i%2==1:
            result+= text[i]
        i+=1
    return result
print("The result is:"+transposition_cipher( sub ))
        
            

        

 

