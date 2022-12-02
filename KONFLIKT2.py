print("hello")
print("tabelka mnozenia")
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=' ')
    print()
print("nie tabelka a wrecz tabela")
print("wypisanie liczb podzielnych przez 15 i mniejszych od 100")
for i in range(1,100):
    if i%15==0:
        print(i,end=' ')