L=[10,12,17,19,20]
Z=[]

def maplist(listequelle, startwert, endwert):
    scale=abs((endwert-startwert)/(listequelle[-1:][0]-listequelle[0]))
    return scale

print (L[-1:])     # liefert das letzte Element der Liste
                   # VORSICHT das ist eine Liste mit nur einem Element
print (L[-1:][0])  # liefert die tatsächliche Zahl!!!!


print(type(L[-1:]))
res=(L[-1:][0]-L[0])
print(res)
print (maplist(L,250,290))
