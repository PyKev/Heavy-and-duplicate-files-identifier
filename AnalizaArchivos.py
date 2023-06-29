import pandas as pd
import os

carpeta = 'archivos\\'

archivos = [os.path.join(carpeta, path) for path in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, path))]

#Borra linea
for archivo1 in archivos:
    with open(archivo1, "rb+") as ar:
        lines = ar.readlines()
        if str(lines[0].strip())[1:].replace("'","") != "Marca":
            lines[0]=b'Marca\n'
            ar.writelines(lines)
            ar.seek(0)
            ar.truncate()
            ar.writelines(lines[:-4])

#Une archivos
with open('Prueba.txt', 'wb') as fp:
    for archivo in archivos:
        with open(archivo, "rb") as a:
            fp.write(a.read())

dictionary = {'Nombre': [], 'Tipo de archivo': [], 'Propietario': [], 'Peso': [], 'Ruta': [], 'Fecha': []}
peso_carpeta2 = 0.0

#Procesamiento datos
with open("Prueba.txt", "rb") as todo:
    # Dataframe
    texto = todo.readlines()
    for j in range(3,len(texto)):
        #Definiciones
        pos_directorio = str(texto[j][:11].strip())[1:].replace("'", "")
        pos_peso = str(texto[j][27:42].strip())[1:].replace("'", "").replace(',', "")
        pos_linea_final = str(texto[j][17:26].strip())[1:].replace("'","").replace(',',"")

        def asigna_elementos(indice,tipo,indice_propietario=None):
            indice = indice+2 if tipo == "Dir" else indice
            propietario = str(texto[indice_propietario][42:65].strip())[1:].replace("'", "").replace('.', "") if tipo == "Dir" else str(texto[j][42:65].strip())[1:].replace("'", "")
            return str(texto[indice][:11].strip())[1:].replace("'", ""), propietario

        def agregar_diccionario(nombre,tipo,propietario,peso,ruta,fecha):
            dictionary['Nombre'].extend([nombre])
            dictionary['Tipo de archivo'].extend([tipo])
            dictionary['Propietario'].extend([propietario])
            dictionary['Peso'].extend([peso])
            dictionary['Ruta'].extend([ruta])
            dictionary['Fecha'].extend([fecha])

        if pos_directorio == "Directorio":
            pos_ruta = str(texto[j][15:].strip())[1:].replace("'", "")
            nombre_carpeta2 = os.path.basename(pos_ruta)
            ruta_carpeta2 = os.path.abspath(pos_ruta)
            prop_carpeta_index = j+3 if j == 3 else j+2
            fecha_carpeta2,pos_propietario = asigna_elementos(j,"Dir",prop_carpeta_index)
            propietario_carpeta2 = pos_propietario[pos_propietario.find("\\") + 2:]

        if pos_peso.isnumeric():
            nombre_archivo2 = str(texto[j][65:].strip())[1:].replace("'", "")
            fecha_archivo2, pos_propietario_archivo = asigna_elementos(j,"archivo")
            propietario_archivo2 = pos_propietario_archivo[pos_propietario_archivo.find("\\") + 2:]
            peso_archivo2 = float(pos_peso)
            ruta_archivo2 = ruta_carpeta2 + "\\" + nombre_archivo2
            peso_carpeta2 += peso_archivo2
            agregar_diccionario(nombre_archivo2,"Archivo",propietario_archivo2,peso_archivo2,ruta_archivo2,fecha_archivo2)

        if pos_linea_final == "archivos":
            agregar_diccionario(nombre_carpeta2,"Carpeta",propietario_carpeta2,peso_carpeta2,ruta_carpeta2,fecha_carpeta2)
            peso_carpeta2 = 0.0

    df = pd.DataFrame(dictionary)
    df["Peso en GB"] = df["Peso"]/1000000000
    df_duplicado = df[df.duplicated(['Nombre','Peso'], keep=False)]
    df_duplicado = df_duplicado[['Nombre', 'Peso en GB', 'Ruta', "Tipo de archivo"]].sort_values(['Peso en GB','Nombre'], ascending=False)
    df = df.sort_values(['Peso'], ascending=False).groupby('Tipo de archivo').head(1000)
    #Excel
    rutaexcel = 'PruebaExcel.xlsx'
    writer = pd.ExcelWriter(rutaexcel)
    df.to_excel(writer, 'TOP archivos pesados',index=False)
    df_duplicado.to_excel(writer, 'Archivos duplicados',index=False)
    writer.close()