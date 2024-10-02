from PIL import Image
import numpy as np

base_to_bin_map = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}

def base_seq_to_bin_matrix(base_seq, img_r, img_c):
    # Get the original image dimensions

    img = []
    row = []
    curr_bin_string = ''

    for base in res:
        curr_bin_string += base_to_bin_map[base]
        
        if len(curr_bin_string) == 8:
            row.append(curr_bin_string)
            curr_bin_string = ''
        
        if len(row) == img_c:
            img.append(row)
            row = []

    # If there's any remaining incomplete row, add it to the image
    if row:
        img.append(row)

    # Ensure the image has the correct dimensions
    img = img[:img_r]
    img = [row[:img_c] for row in img]

    return img

def binary_matrix_to_image(binary_matrix, output_path):
    # Convert binary strings to integers
    to_int = lambda x: int(x, 2)
    int_matrix = np.array([[to_int(pixel) for pixel in row] for row in binary_matrix])
    
    # Ensure the values are within 0-255 range
    int_matrix = np.clip(int_matrix, 0, 255)
    
    # Convert to uint8 data type
    img_array = int_matrix.astype(np.uint8)
    
    # Create an image from the array
    img = Image.fromarray(img_array, mode='L')
    
    # Save the image
    img.save(output_path)
    
    return img

res = '' # Your base sequence here

bin_matrix = base_seq_to_bin_matrix(res, 87, 70)
binary_matrix_to_image(bin_matrix, 'generated_img.png')

# Look for generated_img.png in your current directory