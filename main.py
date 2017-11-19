import itertools

Num = []
Res = []
Formulas = []

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
        n = 0
        for a in Num:
            if a == [num,TMP]:
                n += 1
        if n == 0:
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
    Num.append(add_num(nume,unidad))

def comparar_valores(numeroo):
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
            print("A: " + str(a))
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
                if g == b and n1 < len(TMP1) and num1 == 0:
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

#TEST    
numer(6.67e-11,"G")
add_form("masaLuna=F*r*r/G*M1")
add_form("k=T*T/r*r")
add_form("Hz=/T")
numer(1.9e20,"F")
numer(6e24,"M1")
numer(3.9e8,"r")
def test():
    numer(49.0,"m")
    numer(5.0,"s")
    add_form("v=m/s")
    add_form("a=v/s")
    #comparar(6)
    comparar_valores([Num[0],Num[1],Num[2],Num[3]])
    comparar_valores([Num[len(Num)-1],Num[len(Num)-2]])
    comparar_valores([Num[len(Num)-1],Num[len(Num)-2]])
test()
#add_form("formula") para añadir una formula
#numer(valor, letra) para añadir un numero
#comparar_valores([[valor,[["letra",1]]],[valor2,[["letra2",1]]]...etc])
for a in Num:
    print(str(a))
print("FIN")