import random

passw = "/*-+7894561230ºª!·$%&/()='¡?¿|@#~€¬qw€rtyuiop`^[]asdfghjklñ¨ç<>zxcvbnm,;.:-_QWERTYUIOPÑLAKSJDHFGZXCVBNM"
num = int(input("Inserta la cantidad de caracteres que quiere en su contraseña: "))
new_pass = ""

for i in range(num):
    new_pass += random.choice(passw) 

print("tu contraseña es:", new_pass)