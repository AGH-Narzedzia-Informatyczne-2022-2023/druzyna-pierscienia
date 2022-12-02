#include <stdio.h>
#include <stdlib.h>
#define OCENIAJ  1

double average(int tablica[], int rozmiar)
{
    double suma = 0;
    for(int i = 0; i < rozmiar; i++)
    {
        suma += tablica[i];
    }
    double srednia = suma / rozmiar;
    return srednia;
}

int separate(int tablica[], int tabmin[], int tabmax[], int rozmiar, double v, int c)
{
    int j = 0;
    int k = 0;

    for(int i = 0; i < rozmiar; i++)
    {
        if(tablica[i] < v)
        {
            tabmin[j] = tablica[i];
            j = j+1;
        }
        else
        {
        tabmax[k] = tablica[i];
        k = k+1;
        }
    }
    if(c == 0)
    {
        return j;
    }
    if(c == 1)
    {
        return k;
    }
    
}

int print_int_table1D(int tablica[], int rozmiar)
{
    printf("\n");
    for(int i = 0; i < rozmiar; i++)
    {
    printf(" %d",tablica[i]);
    }
}



int main(void) {
    int seed, max, size;
    if(OCENIAJ == 0) printf("Wpisz seed, górną granicę domknietego przedziału losowanych liczb i dlugosc tablicy: ");
    scanf("%d %d %d",&seed,&max,&size);
    srand(seed);
    int tab[size];
    int tab0[size];
    int tab1[size];
    PRINTF("TU WYSTAPI KONFLIKT");
    for(int i = 0; i < size; i ++)
   {
        int a = rand() % (max + 1);
        int b = rand() % (max + 1);
        int c = a * b;
        tab[i] = c;
   }
   
    printf("\n %.2lf", average(tab,size));
    separate(tab, tab0, tab1, size, average(tab,size), 2 );
    print_int_table1D(tab0, separate(tab, tab0, tab1, size, average(tab,size), 0 ));
    printf("\n %.2lf", average(tab0,separate(tab, tab0, tab1, size, average(tab,size), 0 )));
    print_int_table1D(tab1, separate(tab, tab0, tab1, size, average(tab,size), 1 ));
    printf("\n %.2lf\n", average(tab1,separate(tab, tab0, tab1, size, average(tab,size), 1 )));
    
    return 0;

}
