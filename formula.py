import itertools
import os
import sys

Num = []
Res = []
Formulas = []

verbose = 0

path_registro = os.path.dirname(os.path.abspath(__file__))
nom_registros = ["formulas","numeros"]
nom_fichero = "formula.py"
argumentos = sys.argv

def encontrar_num(letra):
    for a in Num:
        if letra == a[1][0][0]:
            return a
def printf(texto):
    if verbose == 1:
        print(texto)

def ayuda():
    print("Uso: 'python formula.py [argumentos]'")
    print("")
    print("Argumentos:")
    print("-h Ayuda: Muestra este menú")
    print("-a [( numero palabra )] Añadir numero: Añade un numero al registro de valores de las formulas")
    print("-c [( palabra palabra... )] Comparar valores: Calcula incognitas de las formulas con estas palabras")
    print("-f [formula] Añadir formula: Añade una formula para poder calcular resultados")
    print("-v Versión: Muestra la version del programa")
    print("")
    print("*El programa esta hecho para calcular formulas con incognitas.")
    print("**No funcionan otras operaciones que no sean multiplicaciones y divisiones")
    
    print("")
    print("Programa escrito en Python")

def main():
    global path_registro, nom_registro
    if len(argumentos) > 0:
        prox = 0
        v = 0
        TMP = []
        for a in argumentos:
            if a == nom_fichero:
                if len(argumentos) == 1:
                    ayuda()
            else:   
                if prox == 0:    
                    if a == "-h":
                        ayuda()
                    elif a == "-a":
                        prox = 1
                        if len(Num) <= 0:                                                                              
                            archivo_registro = fichero(11)
                    elif a == "-c":
                        if len(Num) <= 0 and len(Formulas) <= 0: 
                            fichero(-1)
                        prox = 2
                    elif a == "-f":
                        prox = 3
                        if len(Formulas) <= 0:                                                                              
                            archivo_registro = fichero()
                    elif a == "-v":
                        print("Version 1.1")
                                          
                    elif a == "--borrar":
                        open(str(path_registro)+nom_registro,"w").close()
                    elif a == "--h":
                        print("")
                        print("**Menu de desarrollador**")
                        if os.path.exists(str(path_registro)+nom_registro):    
                            print("Directorio registro: " + str(path_registro))
                            print("Nombre del archivo de registro: " + str(nom_registro))
                        else:
                            print("Registro no encontrado")


                        print("")
                        print("--borrar Borra todos los registros PERMANENTEMENTE")
                        print("")

                    elif a == "--hh":
                        prox = -1
                    else:
                        print("No se ha reconocido el argumento.")
                        print("Por favor, verifique la entrada.")
                else:
                    if a == "(":
                        v = 1
                    elif a == ")":
                        V = 0
                        if prox == 1:
                            numer(TMP[0],TMP[1])
                            archivo_registro.close()
                        elif prox == 2:
                            comparar_valores(TMP)
                    elif prox == 1 or prox == 2:
                        TMP.append(a)
                    elif prox == -1:
                        if len(Num) <= 0 and len(Formulas) <= 0: 
                            fichero()
                        exec(a)
                    if v == 0:
                        prox = 0
    else:
        ayuda()


def fichero(ficher):
    global path_registro, nom_registros
    if fichero >= 0:
        nom_registro = nom_registros[ficher]
        printf("Funcion fichero()")
        if os.path.exists(str(path_registro)+nom_registro):
            printf("Archivo " + nom_registro + " encontrado en " + path_registro)
            archivo_registro = open(str(path_registro)+nom_registro,"rb+")
            leer_archivo(archivo_registro.read(),ficher)
            archivo_registro.close()
        else:
            
            printf("Archivo " + nom_registro + " no encontrado. Creando...")
            archivo_registro = open(str(path_registro+nom_registro),"w").close()
                                        
        return archivo_registro
    else:
        for a in nom_registro:
            fichero(a)

def leer_archivo(archiv,lista):
    inpt = ""
    psc = 2
    b = -1
    pare = 0
    for letter in str(archiv):   
        psc-=1
        if letter != "," and letter != "(" and letter != ")":
            if psc < 0:      
                inpt += letter
                printf("Añadida letra " + str(letter))
        else:   
            if letter == "(":
                pare = 1
            elif pare == 0 or (pare == 1 and letter == ")"):
                if lista == 0 and inpt != "":
                    add_form(inpt)
                    inpt = ""
                elif lista == 1 and inpt != "":
                    if b != -1:
                        numer(b, inpt)
                        b = -1
                    else:
                        b = int(inpt)
                        inpt = ""
                pare = 0


def add_num(num,unidades):
    ele = 1
    TMP = ""
    TMP2 = []
    for a in range(len(unidades)):
        print("a = " + str(a) + "/" + str(len(unidades)))
        if unidades[a] != "*" and unidades[a] != "/":
            if unidades[a] != " ":
                TMP += unidades[a]
        else:
            TMP2.append([TMP,ele])
            print("Anadido " + str(TMP) + "^" + str(ele))
            TMP = ""
            if unidades[a] == "/":
                ele = -1
    if TMP != "":
        TMP2.append([TMP,ele])
        print("Anadido " + str(TMP) + "^" + str(ele))
    print("Anadido valor " + str(num) + " " + str(TMP2))
    return([num,TMP2])

def add_form(formula):
    ele = 1
    TMP = ""
    TMP3 = []
    for a in range(len(formula)):
        print("a (" + str(formula[a]) + ") = " + str(a) + "/" + str(len(formula)))
        if formula[a] != "*" and formula[a] != "/" and formula[a] != "=":
            if formula[a] != " ":
                TMP += formula[a]
        else:
            if TMP != "":
                TMP3.append([TMP,ele])
                print("Anadido " + str(TMP) + "^" + str(ele))
            TMP = ""
            if formula[a] == "/":
                ele = -1
            elif formula[a] == "=":
                TMP3.append(["=",0])
                ele = 1
    if TMP != "":
        TMP3.append([TMP,ele])
        print("Anadido " + str(TMP) + "^" + str(ele))
    
    n = 0
    for a in Formulas:
       if a == TMP3:
            n += 1
    if n == 0:
        Formulas.append(TMP3)
        print("Anadida formula: " + str(TMP3))

def result(nume, unidad):
    Res.append(add_num(nume,unidad))

def numer(nume, unidad):
    Num.append(add_num(int(nume),unidad))

def comparar_valores(numeroo):
    TMP = []
    for a in numeroo:
        TMP.append(encontrar_num(a)) 
    comparar_valors(TMP)

def comparar_valors(numeroo):
    TMP = []
    Pos1 = 0
    comprovar()
    comprovar_f()
    #Arreglar soles 
    for num1 in numeroo:   
        for c in range(len(Formulas)):
            for e in range(len(Formulas[c])):
                for d in num1[1]:
                    if Formulas[c][e][0] == d[0]:
                        Pos1 += 1
            if Pos1 > 0:
                TMP.append([["1",c,Pos1], [Formulas[c],d]])
                print("Anadido a TMP " + str([["1",c,Pos1], [Formulas[c],d]]))
            Pos1 = 0


    print("TMP = " + str(TMP))
    TMP2 = []
    for a in range(len(TMP)-1):
        for b in range(len(TMP)-1):
            if TMP[a] != "" and TMP[b] != "":
                if TMP[a] != TMP[b]:
                    if TMP[a][0][1] == TMP[b][0][1] and TMP[a][1][1] != TMP[b][1][1]:
                        TMP2.append([["3",TMP[a][0][1],TMP[a][0][2]+TMP[b][0][2]],[TMP[a][1][0],[TMP[a][1][1],TMP[b][1][1]]]])
                        TMP[a]=""
                        TMP[b]=""

    print("")
    #c + Num
    for a in TMP2:
        a[0][2] = 0
        for b in a[1][0]:
            for c in Num:        
                for d in c[1]:
                    if b == d:
                        a[0][2]+=1
            
            if mostrar_formula(separar_formula(a[1][0])[0]) == mostrar_formula(c[1]):
                a[0][2] += len(c[1])
                a[1].append(b)
            if mostrar_formula(separar_formula(a[1][0])[1]) == mostrar_formula(c[1]):
                a[0][2] += len(c[1])
                a[1].append(b)

            
    #Aco es separara despues
    for a in TMP2:
        if a[0][2] == len(a[1][0]) - 2:
            print(a)
            calcular_formula(a[1][0])
    print("")

def separar_formula(formula):
    TMP = 1
    TMP1 = []
    TMP2 = []
    for a in formula:
        if TMP == 1 and a[0] != "=":
            TMP1.append(a)
        else:
            TMP = 2
            if a[0] != "=":
                TMP2.append(a)
    print("Formula: " + str(formula))
    print("TMP: " + str(TMP1) + " . " + str(TMP2))
    return [TMP1,TMP2]

def calcular_formula(formula):
    TMP0 = separar_formula(formula)
    TMP1 = TMP0[0]
    TMP2 = TMP0[1]

    TMP3 = []

    for a in TMP1:
        TMP3.append([a])
        for b in TMP2:
            TMP3.append([b])
            TMP3.append([[a[0],a[1]],[b[0],str(int(b[1])*-1)]])
   


    print("TMP3 = " + str(TMP3))

    TMP4 = []
    for a in TMP3:
        TMP4.append([a,valor_unidad(a)])
    print("TMP4" + str(TMP4))
    print("")

    TMP5 = []
    Pos = 0
    Posa = 0
    for a in TMP3:
        n = 0
        for b in TMP4:
            if a == b[0] and b[1] != None and n == 0:
                TMP5.append([b[0],b[1]])
                n = 1

    #TMP1,TMP2
    n1 = 0
    l1 = []
    n2 = 0
    l2 = []
    for a in TMP5:
        num1 = 0
        num2 = 0
        for b in TMP1:
            for g in a[0]:
                if g == b and n1 < len(TMP1) and num2 == 0:
                    n1 += 1
                    num1 = 1
                    l1.append(a[1])
        for c in TMP2:
            for d in a[0]:
                if d == c and n2 < len(TMP2) and num2 == 0:
                    n2 += 1
                    num2 = 1
                    l2.append(a[1])

    m1 = 1
    if n1 >= len(TMP1):
        form = []
        for d in l1:
            m1 *= d
    if len(l1) <= 0:
        n1 = 1
        
    m2 = 1
    if n2 >= len(TMP2):
        form = []
        for e in l2:
            m2 *= e
    if len(l2) <= 0:
        n2 = 1
        
       
    if len(l1) > 0:
        final = m1 / m2        
        Final = TMP2

    elif len(l2) > 0:
        final = m2 / m1
        Final = TMP1

#Crec que agafa el segon valor al reves, al menys quan agafa v/S

    print("m1 = " + str(m1))
    print("m2 = " + str(m2))
    print("Resultado: " + str(final))
    if n1 >= len(TMP1) or n2 >= len(TMP2):
        n = 0
        for y in Num:
            if [final,Final] == y:
                n += 1
        if n == 0:
            Num.append([final,Final])
            

    print("")

def invertir(form):
    for a in range(len(form)):
        form[a][1] *= -1
    return form

def comprovar():
    TMP2 = []
    for a in Num:
        TMP = []
        TMP1 = []
        TMP.append(1/a[0])
        for b in a[1]:
            TMP1.append([b[0],b[1]*-1])
        TMP.append(TMP1)
        TMP2.append(TMP)
    
    for c in Num:
        for d in c[1]:
            TMP = []
            TMP.extend(d)

        
    for d in TMP2:
        n = 0
        for e in Num:
            if d == e:
                n+=1
        if n == 0:
            Num.append(d)

def comprovar_f():
    #Calcular totes les posibles formules per poder calcular_formula()
    #A totes elles, i aixina traure tots els numeros sense tindre  
    #que fer-ho 2 vegades 
    TMP3 = []
    
    for a in Formulas:     
        TMP1 = []
        TMP2 = []
        TMP4 = []
        n = 0
        for b in separar_formula(a):           
            for c in b:
                n += 1
                t = []
                if n == 1:
                    if c[1]*-1 == -1:
                        TMP1.extend([c[0],c[1]*-1])
                    else:
                        t.extend(TMP1)
                        TMP1 = [c[0],c[1]*-1]
                        TMP4 = t
                else:
                    if c[1]*-1 == -1:
                        TMP2.extend([c[0],c[1]*-1])
                    else:
                        t.extend(TMP2)
                        TMP2 = [c[0],c[1]*-1]
                        TMP4 = t
                    n == 0
        if TMP4 != []:
            TMP3.append([TMP1,["=",0],TMP2,TMP4])
        else:
            TMP3.append([TMP1,["=",0],TMP2])
        
    for d in TMP3:
        n = 0
        for e in Formulas:
            if d == e:
                n+=1
        if n == 0:
            add_form(mostrar_formula(d))


def valor_unidad(uni):
    valor = ""
    TMP = None
    Pos = 0
    for a in Num:
        for b in a[1]:
            for c in uni:                        
                if c == b:
                    Pos += 1
        if Pos >= len(a[1]) and Pos >= len(uni):
            TMP = a[0]
        Pos = 0
    print("TMP =" + str(TMP))
    return TMP

def mostrar_formula(num1):
    form_num1 = ""
    for a in num1:
        if a[1] == 1:
            form_num1 += "*"
        elif a[1] == -1:
            form_num1 += "/"
        if a[1] != 0:
            form_num1 += a[0]
        else:
            form_num1 += "="

    
    #form_num1 = form_num1[1:]
    print("Formula num1 = " + str(form_num1))
    return form_num1

def comparar(r):
    brute = list(itertools.combinations(Num, r))
    for a in brute:
        print("a = " + str(a))
        comparar_valores(a)

def borrar_numer():
    Num = []

main()
print()