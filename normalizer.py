import pypandoc
import os

# Lista de formatos de salida que queremos obtener
formats = ['txt', 'docx', 'pdf', 'rtf', 'html', 'odt']

def convert_file(input_file, output_format):
    """
    Convierte input_file al formato output_format.
    El archivo resultante se guarda con el mismo nombre base y nueva extensión.
    """
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.{output_format}"
    
    # Determinar el formato de entrada en base a la extensión del archivo
    input_extension = os.path.splitext(input_file)[1][1:].lower()
    # Si es un archivo txt, lo tratamos como markdown (o plain, según corresponda)
    if input_extension == 'txt':
        input_format = 'markdown'
    else:
        input_format = input_extension

    try:
        pypandoc.convert_file(input_file, output_format, format=input_format, outputfile=output_file)
        print(f"Convertido {input_file} a {output_file}")
    except Exception as e:
        print(f"Error al convertir {input_file} a {output_format}: {e}")

# Ejemplo: Convertir 'ejemplo.txt' a los demás formatos de la lista
input_file = "ejemplo.txt"

# Convertir a cada formato que no sea el original
for fmt in formats:
    if fmt != os.path.splitext(input_file)[1][1:].lower():
        convert_file(input_file, fmt)
