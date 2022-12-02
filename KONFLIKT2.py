print("goodbyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("tabelka mnozenia")
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
    print()
print("wypisanie liczb podzielnych przez 20 i mniejszych od 100")
for i in range(1,100):
    if i%20==0:
        print(i,end=' ')