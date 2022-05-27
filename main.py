array_temp = []
f_acumuladas = []
marcas = []
sum = 0
n_clases = int(input("Numero de clases: "))
filas = [[j*0 for j in range(5)] for i in range(n_clases)]
lim_inf_exacto = input("Limite inferior: ").split(" ")
lim_sup_exacto = input("Limite superior: ").split(" ")
# marcas = input("Marca de clase: ").split(" ")
f_absolutas = input("Frecuencia absoluta: ").split(" ")
# lim_inferiores = input("Contenido desde: ").split(" ")
# lim_superiores = input("Contenido hasta: ").split(" ")

for dato in f_absolutas:
    if(len(dato)>0):
        dato = float(dato)
        sum+=dato
        f_acumuladas.append(str(sum))
i=0
for dato in lim_inf_exacto:
    if(len(dato)>0):
        dato = float(dato)
        dato2 = float(lim_sup_exacto[i])
        marcas.append(str((dato+dato2)/2))
    i+=1
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
    unidad_variacion = array[1][0] - array[0][1]
    if unidad_variacion>0:
        lim_inf_exacto_cm = array[clase][0] - unidad_variacion/2
        amplitud = array[clase][1] - array[clase][0] + unidad_variacion
    else:
        lim_inf_exacto_cm = array[clase][0]
        amplitud = array[clase][1] - array[clase][0]
    frecuencia_clase = array[clase][3]
    frecuencia_acumulada_anterior = array[clase-1][4]
    mediana = lim_inf_exacto_cm + ((((array[n_clases-1][4]/2) - frecuencia_acumulada_anterior)/frecuencia_clase) * amplitud)
    print("Mediana: {:<5,.3f}".format(mediana))
def calcular_moda(array,n_clases):
    max = None
    for i in range(n_clases):
        if(max is None or array[i][3]>max):
            clase = i
            max = array[i][3]
    if(clase == 0):
        delta1 = array[clase][3]
    else:
        delta1 = array[clase][3] - array[clase-1][3]
    if(clase == n_clases-1):
        delta2 = array[clase][3]
    else:
        delta2 = array[clase][3] - array[clase+1][3]
    unidad_variacion = array[1][0] - array[0][1]
    if unidad_variacion>0:
        lim_inf_clase_moda = array[clase][0] - unidad_variacion/2
        amplitud = array[clase][1] - array[clase][0] + unidad_variacion
    else:
        lim_inf_clase_moda = array[clase][0]
        amplitud = array[clase][1] - array[clase][0]
    moda = lim_inf_clase_moda + ((delta1/(delta1+delta2))*amplitud)
    print("Moda: {:<5,.3f}".format(moda))
def buscar_valor(filas, n_clases,valor):
    for i in range(n_clases):
        if(filas[i][1]>valor):
            clase = i
            break
    return clase
def calcular_nx(filas,clase,uv,valor):
    nx = (((filas[clase][1] - valor) + uv)/((filas[clase][1] -filas[clase][0]) + uv))*filas[clase][3]
    return nx
def calcular_ny(filas,clase,uv,valor):
    ny = (((valor - filas[clase][0]) + uv)/((filas[clase][1] -filas[clase][0]) + uv))*filas[clase][3]
    return ny
def calcular_intervalo(nx,ny,clase1,clase2,filas,n):
    sum = round(nx)+round(ny)
    for i in range(n):
        if(i>clase1 and i<clase2):
            sum+=filas[i][3]
    print("Desde la clase: ",clase1+1)
    print("Hasta la clase: ",clase2+1)
    print("Nx: ",nx)
    print("Ny: ",ny)
    print("{:<1,.0f} datos cumplen con la condicion dada".format(sum))
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
    opt = int(input("[1] Media,Mediana,Moda\t[2] Nx\t[3] Ny\t[4] Intervalo\t[5] Salir\n"))
    if(opt == 1):
        calcular_media(filas,n_clases)
        calcular_mediana(filas,n_clases)
        calcular_moda(filas,n_clases)
    elif(opt == 2 or opt == 3):
        valor = float(input("Valor: "))
        clase = buscar_valor(filas,n_clases,valor)
        unidad_variacion = filas[1][0] - filas[0][1]
        if(opt == 2):
            nx = calcular_nx(filas,clase,unidad_variacion,valor)
            sum = round(nx)
            for i in range(n_clases):
                if(i>clase):
                    sum+=filas[i][3]
            print("Clase: ",clase+1)
            print("Nx: ",nx)
            print("Al menos/cuando menos {:<1,.0f} datos cumplen con la condicion dada".format(sum))
        else:
            ny = calcular_ny(filas,clase,unidad_variacion,valor)
            sum = round(ny)
            for i in range(n_clases):
                if(i<clase):
                    sum+=filas[i][3]
            print("Clase: ",clase+1)
            print("Ny: ",ny)
            print("A lo mucho/cuando mucho {:<1,.0f} datos cumplen con la condicion dada".format(sum))
    elif(opt == 4):
        valor1 = float(input("Entre: "))
        valor2 = float(input("Y: "))
        clase1 = buscar_valor(filas,n_clases,valor1)
        clase2 = buscar_valor(filas,n_clases,valor2)
        unidad_variacion = filas[1][0] - filas[0][1]
        nx = calcular_nx(filas,clase1,unidad_variacion,valor1)
        ny = calcular_ny(filas,clase2,unidad_variacion,valor2)
        calcular_intervalo(nx,ny,clase1,clase2,filas,n_clases)
    elif(opt == 5):
        break
    else:
        print("Opcion inválida")