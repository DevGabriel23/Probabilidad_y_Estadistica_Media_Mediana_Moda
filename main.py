array_temp = []
f_acumuladas = []
sum = 0
n_clases = int(input("Numero de clases: "))
filas = [[j*0 for j in range(5)] for i in range(n_clases)]
lim_inf_exacto = input("Limite inferior: ").split(" ")
lim_sup_exacto = input("Limite superior: ").split(" ")
marcas = input("Marca de clase: ").split(" ")
f_absolutas = input("Frecuencia absoluta: ").split(" ")
# lim_inferiores = input("Contenido desde: ").split(" ")
# lim_superiores = input("Contenido hasta: ").split(" ")

for dato in f_absolutas:
    if(len(dato)>0):
        dato = float(dato)
        sum+=dato
        f_acumuladas.append(str(sum))
array_temp.append(lim_inf_exacto)
array_temp.append(lim_sup_exacto)
array_temp.append(marcas)
array_temp.append(f_absolutas)
array_temp.append(f_acumuladas)
# array_temp.append(lim_inferiores)
# array_temp.append(lim_superiores)

def crear_tabla(array,n_clases,j):
    i=0
    for dato in array:
        if(dato.isdigit and len(dato)>0 and i<n_clases):
            filas[i][j] = (float(dato))
            i+=1
def calcular_media(array,n_clases):
    sum = 0
    for i in range(n_clases):
        sum+=(array[i][3]*array[i][2])
    media = sum/array[n_clases-1][4]
    print("Media: {:<5,.3f}".format(media))
def calcular_mediana(array,n_clases):
    pos_mediana = (array[n_clases-1][4]+1)/2
    for i in range(n_clases):
        if(array[i][4]>pos_mediana):
            clase = i
            break
    amplitud = array[clase][1] - array[clase][0]
    frecuencia_clase = array[clase][3]
    frecuencia_acumulada_anterior = array[clase-1][4]
    mediana = pos_mediana + ((((array[n_clases-1][4]/2) - frecuencia_acumulada_anterior)/frecuencia_clase) * amplitud)
    print("Mediana: {:<5,.3f}".format(mediana))
def calcular_moda(array,n_clases):
    max = None
    for i in range(n_clases):
        if(max is None or array[i][3]>max):
            clase = i
            max = array[i][3]
    lim_inf_clase_moda = array[clase][0]
    if(clase == 0):
        delta1 = array[clase][3]
    else:
        delta1 = array[clase][3] - array[clase-1][3]
    if(clase == n_clases-1):
        delta2 = array[clase][3]
    else:
        delta2 = array[clase][3] - array[clase+1][3]
    amplitud = array[clase][1] - array[clase][0]
    moda = lim_inf_clase_moda + ((delta1/(delta1+delta2))*amplitud)
    print("Moda: {:<5,.3f}".format(moda))

for i in range(5):
    crear_tabla(array_temp[i],n_clases,i)
print("\n{:^15} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Clase","Limite inferior","Limite superior","Marca de la clase","F. absoluta","F.acumulada"))
for i in range(n_clases):
    lim_inf_ex,lim_sup_ex,marca,f_absoluta, f_acumulada = filas[i]
    # clase = chr(65+i)
    clase = 1+i
    print("{:^15} {:^15,.2f} {:^25,.2f} {:^20,.2f} {:^10,.2f} {:^32,.2f}".format(clase,lim_inf_ex,lim_sup_ex,marca,f_absoluta, f_acumulada))
while True:
    print("\nCalcular:")
    opt = int(input("[1] Media,Mediana,Moda\t[2] Salir\n"))
    if(opt == 1):
        calcular_media(filas,n_clases)
        calcular_mediana(filas,n_clases)
        calcular_moda(filas,n_clases)
        break
    elif(opt == 2):
        break
    else:
        print("Opcion inválida")