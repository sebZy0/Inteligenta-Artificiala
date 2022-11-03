from ctypes import sizeof
import string
from tokenize import String
# ex. 1
lista = [3, 4, 5, 90, 4]
lista.sort()
print("1. ", lista)
# ex. 2
print("2.", "\nMinimul:", lista[0], "\nMaximul:", lista[-1])
# ex. 3
print("3.")
string_list = []
n = int(input("Introdu numarul de elemente: "))
for i in range(0, n):
    print("Introdu elementul la pozitia", i)
    string_list += [str(input())]
print("Lista este:", string_list, "\nEnuntul: ", *string_list)
# ex. 4
print("4.")
lista.remove(lista[1])
print("\n", lista)
# ex. 5
print("5.")
print("Introdu numarul pe care vrei sa il adaugi la sfarsitul listei de numere: ")
lista.append(int(input()))
print("\nNoua lista: ", lista)
