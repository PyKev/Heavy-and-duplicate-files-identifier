# Heavy and Duplicate Files Identifier

This Python script, "AnalizaArchivos.py," allows you to process files in a specific folder and generate a report with details about the files found. The main objective is to identify duplicate files and heavy files within the folder.

## Requirements
- Python 3.x
- Pandas library

## Usage Instructions
- Clone the repository to your local machine.
- Open the command prompt and navigate to the folder you want to analyze.
- Run the command `dir /s /a /q > yourfile.txt` to generate a file listing of the folder and its subdirectories.
- Place the generated file(s) that you want to process in the "archivos" (file) folder.
- Execute the "AnalizaArchivos.py" file in a Python environment.

## Script Functions:
- It will merge the files into one file called "Prueba.txt".
- It will process the data from the "Prueba.txt" file to obtain information about the files and folders.
- It will identify and display duplicate files.
- It will sort and filter the obtained result.
- It will create an Excel file named "PruebaExcel.xlsx" with two sheets: "TOP Heavy Files" and "Duplicate Files".

## Result
You can find the generated report in the "PruebaExcel.xlsx" file. The report contains detailed information about the files, including the name, size, owner, weight, weight in GB, date, path, and file type.
Make sure to review the report to identify any duplicate files and the heaviest files within the folder.

## Additional Notes
If you want to change the source folder, you can modify the "folder" (archivo) variable in the script.
