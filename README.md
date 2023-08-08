# Aplicaciones para Eliminación de Fondo de Imágenes

Este repositorio contiene dos aplicaciones de línea de comandos desarrolladas en Python para eliminar el fondo de imágenes en formato PNG. Estas aplicaciones utilizan las bibliotecas `rembg` y `PIL` (Python Imaging Library) para llevar a cabo el proceso de eliminación de fondo.

## Aplicación 1: Removedor de Fondo en Lote

La primera aplicación, `batch_background_remover.py`, es una herramienta de procesamiento en lote que elimina el fondo de múltiples imágenes en una carpeta de entrada y guarda las imágenes resultantes en una carpeta de salida. Así es cómo se utiliza la aplicación:

```bash
python batch_background_remover.py <carpeta_entrada> <carpeta_salida>

## Aplicación 2: Removedor de Fondo para una Sola Imagen

La segunda aplicación, single_image_background_remover.py, es una utilidad para eliminar el fondo de una sola imagen proporcionada como argumento en la línea de comandos. Así es cómo se utiliza la aplicación:
