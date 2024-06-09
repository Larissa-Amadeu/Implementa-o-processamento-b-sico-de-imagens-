from PIL import Image, ImageOps
import numpy as np

def separar_canais(image_path):
    image = Image.open(image_path)
    r, g, b = image.split()
    r.save("canal_r.png")
    g.save("canal_g.png")
    b.save("canal_b.png")

def rgb_para_cinza(image_path):
    image = Image.open(image_path)
    gray_image = ImageOps.grayscale(image)
    gray_image.save("tons_de_cinza.png")

def cinza_para_pb(image_path, limiar=128):
    image = Image.open(image_path)
    gray_image = ImageOps.grayscale(image)
    binary_image = gray_image.point(lambda x: 255 if x > limiar else 0, mode='1')
    binary_image.save("preto_e_branco.png")

def filtro_media(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    kernel = np.ones((3, 3)) / 9.0
    filtered_array = apply_filter(image_array, kernel)
    filtered_image = Image.fromarray(filtered_array.astype('uint8'))
    filtered_image.save("filtro_media.png")

def filtro_mediana(image_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    filtered_array = apply_median_filter(image_array)
    filtered_image = Image.fromarray(filtered_array.astype('uint8'))
    filtered_image.save("filtro_mediana.png")

def girar_90_graus(image_path):
    image = Image.open(image_path)
    rotated_image = image.rotate(-90, expand=True)
    rotated_image.save("girada_90_graus.png")

def inverter_horizontal(image_path):
    image = Image.open(image_path)
    flipped_image = ImageOps.mirror(image)
    flipped_image.save("inverter_horizontal.png")

def inverter_vertical(image_path):
    image = Image.open(image_path)
    flipped_image = ImageOps.flip(image)
    flipped_image.save("inverter_vertical.png")

def apply_filter(image_array, kernel):
    from scipy.ndimage import convolve
    if len(image_array.shape) == 3:
        filtered_array = np.zeros_like(image_array)
        for i in range(3):
            filtered_array[..., i] = convolve(image_array[..., i], kernel)
    else:
        filtered_array = convolve(image_array, kernel)
    return filtered_array

def apply_median_filter(image_array, size=3):
    from scipy.ndimage import median_filter
    if len(image_array.shape) == 3:
        filtered_array = np.zeros_like(image_array)
        for i in range(3):
            filtered_array[..., i] = median_filter(image_array[..., i], size=size)
    else:
        filtered_array = median_filter(image_array, size=size)
    return filtered_array

# Exemplos de uso:
# separar_canais('imagem.png')
# rgb_para_cinza('imagem.png')
# cinza_para_pb('tons_de_cinza.png', limiar=128)
# filtro_media('imagem.png')
# filtro_mediana('imagem.png')
# girar_90_graus('imagem.png')
# inverter_horizontal('imagem.png')
# inverter_vertical('imagem.png')
