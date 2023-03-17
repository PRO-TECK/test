a = int(input("Entrez a "))
b = int(input("Entrez b "))
def pgcd(x,y):
    r = x % y
    if r == 0:
         print(f"le PGCD est {b} \n le PPCM et egal: {a}")   
    if r != 0:
        x = y
        y = r
        print(f"le PGCD est {y} \n le PPCM egal : {(a*b)/y}")
   
    
    
pgcd(a, b)
        