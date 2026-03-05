import numpy as np
import cv2
from tkinter import Tk, filedialog
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
from PIL import Image

# Suppress tkinter root window
Tk().withdraw()

# GUI to pick image
file_path = filedialog.askopenfilename(title="Select an image",
                                       filetypes=[("Image files", "*.jpg *.png *.bmp *.jpeg")])

if not file_path:
    print("No file selected.")
    exit()

# Load image in grayscale
img = Image.open(file_path).convert('L')
img_np = np.array(img, dtype=np.float32)

# Apply 2D DCT
dct_img = dct(dct(img_np.T, norm='ortho').T, norm='ortho')

# Apply inverse DCT
idct_img = idct(idct(dct_img.T, norm='ortho').T, norm='ortho')

# Clip and convert to uint8
idct_img_uint8 = np.uint8(np.clip(idct_img, 0, 255))

# Plot original, DCT spectrum, and reconstructed image
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(img_np, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("DCT Spectrum (log scale)")
plt.imshow(np.log1p(np.abs(dct_img)), cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Reconstructed (IDCT)")
plt.imshow(idct_img_uint8, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
