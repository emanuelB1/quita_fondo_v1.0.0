from rembg import remove
from PIL import Image
import sys

def main():
    input_path = sys.argv[1]
    ouput_path = sys.argv[2]
    input = Image.open(input_path)
    ouput = remove(input)
    ouput.save(ouput_path)

if __name__ == "__main__":
    main()
