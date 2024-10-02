from PIL import Image
import numpy as np

def binary_to_base_seq(binary_string: str) -> str:
    bin_to_base_map = {'00': 'A', '01': 'T', '10': 'G', '11': 'C'}

    res = ''

    ptr = 0

    while ptr < len(binary_string) - 1:
        res += bin_to_base_map[binary_string[ptr:ptr+2]]
        ptr += 2
    
    return res

def base_seq_to_amino_acid(base_seq: str) -> str:
    codon_to_amino = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    amino_acid_seq = ''
    for i in range(0, len(base_seq) - 2, 3):
        codon = base_seq[i:i+3]
        amino_acid_seq += codon_to_amino.get(codon, 'X')
    
    return amino_acid_seq

def image_to_binary_matrix(image_path: str):
    # Open the image and convert it to grayscale
    with Image.open(image_path) as img:
        img_gray = img.convert('L')
    
    # Convert the image to a numpy array
    img_array = np.array(img_gray)
    
    # Create a function to convert a number to 8-bit binary string
    to_binary = lambda x: format(x, '08b')
    
    # Apply the binary conversion to each pixel
    binary_matrix = np.vectorize(to_binary)(img_array)
    
    return binary_matrix


binary_matrix = image_to_binary_matrix('your_image_name.png')

res = '' # RESULT: base sequence from image binary

for row in binary_matrix:
    for pixel in row:
        res += binary_to_base_seq(pixel)

print('Base Sequence Result:')
print(res)