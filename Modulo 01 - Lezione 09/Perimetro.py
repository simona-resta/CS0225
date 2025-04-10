print("Scegli la figura geometrica di cui vuoi calcolare il perimetro ")
scelta = input("Premi: \n A per Quadrato \n B per Cerchio \n C per Rettangolo \n")

def quadrato():
    lato = int(input ("Inserisci il lato \n"))
    perimetro_quadrato = lato*4
    print(f'Il perimetro del quadrato è:', perimetro_quadrato)
    return perimetro_quadrato
    
def cerchio():
    raggio = int(input ("Inserisci il raggio \n"))
    perimetro_cerchio = raggio*6,28
    print(f'Il perimetro del cerchio è:', perimetro_cerchio)
    return perimetro_cerchio
    
def rettangolo():
    base = int(input ("Inserisci la base \n"))
    altezza = int(input ("Inserisci l'altezza \n"))
    perimetro_rettangolo = ((base*2) + (altezza*2))
    print(f'Il perimetro del rettangolo è:', perimetro_rettangolo)
    return perimetro_rettangolo
 
    
if scelta == "A" or scelta == "a":
    quadrato()
    
elif scelta == "B" or scelta == "b":
    cerchio()
    
elif scelta == "C" or scelta == "c":
    rettangolo()
    
else:
    scelta = input("Premi: \n A per Quadrato \n B per Cerchio \n C per Rettangolo \n")
