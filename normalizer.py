import pypandoc
import os


formats = ['txt', 'docx', 'pdf', 'rtf', 'html', 'odt']

def convert_file(input_file, output_format):
    """
    Convierte input_file al formato output_format.
    El archivo resultante se guarda con el mismo nombre base y nueva extensión.
    """
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.{output_format}"
    
   
    input_extension = os.path.splitext(input_file)[1][1:].lower()
  
    if input_extension == 'txt':
        input_format = 'markdown'
    else:
        input_format = input_extension

    try:
        pypandoc.convert_file(input_file, output_format, format=input_format, outputfile=output_file)
        print(f"Convertido {input_file} a {output_file}")
    except Exception as e:
        print(f"Error al convertir {input_file} a {output_format}: {e}")


input_file = "ejemplo.txt"


for fmt in formats:
    if fmt != os.path.splitext(input_file)[1][1:].lower():
        convert_file(input_file, fmt)
