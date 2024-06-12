print("Calcola il perimetro delle figure")
print("premi 1 per il quafrato")
print("premi 2 per il triangolo")
print("premi 3 per il cerchio")

print("Inserisci la scelta:")
scelta = int(input())
if scelta == 1:
    print("inserisci la misura del lato del quadrato")
    lato = int(input())
    print("Il perimetro del quadrato è:", lato *4)

elif scelta == 2:

    print("Inserisci la base")
    base = float(input())
    print("Inserisci l'altezza")
    altezza = float(input())
    print("Il perimetro del triangolo è:", base*2 + 2*altezza)

elif scelta == 3:
    print("Hai scelto la circonferenza del Cerchio")
    r = float(input())
    print("Il perimetro del cerchio è:", 2* r* 3,14)

else:
    print("Inserire una scelta tra quelle elencate")

