#Implementación Quicksort Vers.2

def quickSort(l):
    def quickSortRec(l, i, j):
        if i < j:
            k = particion(l, i, j)
            quickSortRec(l, i, k-1)
            quickSortRec(l, k+1, j)
    quickSortRec(l, 0, len(l)-1)


def particion(l, i, j):
    x = l[j]
    k = i-1
    for h in range(i,j):
        if l[h] <= x:
            k += 1
            aux  = l[h]
            l[h] = l[k]
            l[k] = aux
    aux = l[k+1]
    l[k+1] = l[j]
    l[j] = aux
    return k+1

##test
l=[8,5,4,10,-1]
print(l)
quickSort(l)
print(l)

##l = [int(item) for item in input("ingrese una lista de enteros separados por comas: ").split(",")]
##print(l)
#####print(type(l)) #hacer esListaEnteros
####while type(l)!= list:
####    print("ingreso erróneo")
####    l = input("ingrese una lista de enteros")
##quickSort(l)
##print(l)
