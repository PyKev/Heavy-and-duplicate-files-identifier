# Identificador-archivos-pesados-y-duplicados

Este script de Python "AnalizaArchivos.py" permite procesar archivos en una carpeta específica y generar un informe con detalles sobre los archivos encontrados. El objetivo principal es identificar archivos duplicados y archivos pesados dentro de la carpeta.

## Requisitos
- Python 3.x
- Biblioteca Pandas
  
## Instrucciones de Uso
- Clona el repositorio en tu máquina local.
- Ve a cmd y ejecuta el comando en las carpetas que deseas analizar `dir /s /a /q > tuarchivo.txt`
- Coloca el o los archivos generados que deseas procesar en la carpeta "archivos".
- Ejecuta el archivo "procesar_archivos.py" en un entorno de Python.

## Funciones del script:
- Unirá los archivos en uno solo llamado "Prueba.txt".
- Procesará los datos del archivo "Prueba.txt" para obtener información sobre los archivos y carpetas.
- Identificará y mostrará los archivos duplicados.
- Ordenará y filtrará el resultado obtenido.
- Creará un archivo de Excel llamado "PruebaExcel.xlsx" con dos hojas: "TOP archivos pesados" y "Archivos duplicados".
  
## Resultado
Puedes encontrar el informe generado en el archivo "PruebaExcel.xlsx". El informe contiene información detallada sobre los archivos, incluyendo el nombre, tamaño, propietario, peso, peso en GB, fecha, ruta y tipo de archivo.
Asegúrate de revisar el informe para identificar cualquier archivo duplicado y los archivos más pesados dentro de la carpeta.

## Notas adicionales
Si deseas cambiar la carpeta de origen, puedes modificar la variable "carpeta" en el script.
