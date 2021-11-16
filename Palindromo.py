string = input("Ingrese una palabra u oracion para invertir\n")
string = string.replace(" ","")

n = len(string)
string_invertido = ""

for i in range (1,n+1):

    string_invertido += string[n-i]

print(f"La oracion sin espacios es {string.lower()}")
print("\n")
print(f"La oracion invertida es {string_invertido.lower()}")
print("\n")

if string.lower() == string_invertido.lower():
    
    print("La oracion SI es un palindromo.")
    
else:

    print("La oracion NO es un palindromo.")