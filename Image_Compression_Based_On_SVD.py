import numpy as np  # Import NumPy for numerical operations and SVD
import matplotlib.pyplot as plt  # Import Matplotlib for reading/saving images and plotting

# Load the original image from the current directory
# Assumes 'sample.jpg' is present; if color, convert to grayscale by averaging channels
img = plt.imread('sample.jpg')
if len(img.shape) == 3:  # Check if image is color (3 channels)
    img = np.mean(img, axis=2)  # Convert to grayscale by averaging RGB channels

# Get the dimensions of the image matrix
m, n = img.shape  # m: rows (height), n: columns (width)

# Perform Singular Value Decomposition on the image matrix
# full_matrices=False for economic SVD (U: m x r, S: r, Vt: r x n, where r = min(m,n))
U, S, Vt = np.linalg.svd(img, full_matrices=False)


# Define a function to compress the image using top k singular values
def compress_image(k):
    # Truncate matrices to keep only the top k singular values/vectors
    Uk = U[:, :k]  # First k columns of U (left singular vectors)
    Sk = S[:k]  # First k singular values
    Vtk = Vt[:k, :]  # First k rows of Vt (right singular vectors)

    # Reconstruct the approximated image matrix
    img_k = Uk @ np.diag(Sk) @ Vtk  # Matrix multiplication: U_k * diag(S_k) * V_k^T

    # Clip values to valid image range (assuming original is 0-255 uint8)
    # If original is float 0-1, adjust accordingly; here we assume uint8
    if img.max() > 1:  # Check if pixel values are in 0-255 range
        img_k = np.clip(img_k, 0, 255).astype('uint8')  # Clip and convert to uint8
    else:
        img_k = np.clip(img_k, 0, 1)  # Clip to 0-1 for float images

    # Save the compressed image with a filename indicating k
    plt.imsave(f'compressed_k{k}.jpg', img_k, cmap='gray')  # Save as JPEG with grayscale cmap

    # Calculate compression ratio using the formula from Section 3.7
    # Ratio = [k * (1 + m + n) / (m * n)] * 100%
    ratio = (k * (1 + m + n)) / (m * n) * 100

    # Print k and ratio for verification during run
    print(f'Compressed image for k={k}, compression ratio={ratio:.2f}%')

    return ratio  # Return ratio for potential further use


# Define 10 different k values (chosen to show progression from low to high quality)
# Assuming image size allows k up to min(m,n); e.g., for a 1024x1024 image, max k=1024
k_values = [1, 5, 10, 20, 50, 100, 200, 300, 400, 500]

# Loop through each k and compress/save the image
for k in k_values:
    compress_image(k)