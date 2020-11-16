#!/usr/bin/python3
# coding: utf-8


# Il y a plusieurs façons de calculer la factorielle sans faire d’appel récursif pour un même résultat.


def factorielle(n):
    i = n
    calcul_correspondant = str(n)+”!=”
    while (i > 1):
       n = n *  (i - 1)
       calcul_correspondant = calcul_correspondant + str(i) +”*”
       i = i - 1
     print (calcul_correspondant + “1”)
     return n
     
try:
  n = int(input("Entrez un nombre dont on veut la factorielle : "))
  print (“Sa factorielle est”, factorielle(n))
except:
  print (“Veuillez saisir un nombre.”)
----------------------------------------------------------------------- Résultat ---------------------------------------------------------------------------
  

~                                                                        
~                                                                                  
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
~                                                                                   
"factorielle" 9 lines, 210 characters