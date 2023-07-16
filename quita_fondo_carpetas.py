from rembg import remove
from PIL import Image
import os

def main():
    input_folder = r'C:\Respaldo\Fotos\png\con_fondo'  # Ruta de la carpeta de entrada
    output_folder = r'C:\Respaldo\Fotos\png\sin_fondo'  # Ruta de la carpeta de salida

    # Obtener la lista de archivos de imagen en la carpeta de entrada
    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    # Procesar cada imagen y guardar el resultado en la carpeta de salida
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        output_path = os.path.join(output_folder, image_file)

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

if __name__ == "__main__":
    main()
