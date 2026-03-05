import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Button
from PIL import Image
from tkinter import Tk, filedialog

# GUI: Select image
Tk().withdraw()
file_path = filedialog.askopenfilename(title="Select an image",
                                       filetypes=[("Image files", "*.png *.jpg *.bmp *.jpeg")])
if not file_path:
    print("No image selected.")
    exit()

# Load and convert to grayscale
img = Image.open(file_path).convert('L')
img_np = np.array(img, dtype=np.uint8)

# Extract 8 bit planes
bit_planes = [(img_np >> i) & 1 for i in range(8)]

# Create display
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.3, bottom=0.2)
combined = np.zeros_like(img_np, dtype=np.uint8)
img_display = ax.imshow(combined, cmap='gray', vmin=0, vmax=255)
ax.set_title("Combined Bit Planes")
ax.axis('off')

# Checkboxes
labels = [f'Bit {i}' for i in reversed(range(8))]
active_states = [False] * 8
rax = plt.axes([0.05, 0.25, 0.2, 0.6])
checkbox = CheckButtons(rax, labels, active_states)

# Save button
save_ax = plt.axes([0.05, 0.1, 0.2, 0.075])
save_button = Button(save_ax, 'Save Image')

# Store latest image
latest_combined = np.zeros_like(img_np, dtype=np.uint8)

def update(label):
    idx = int(label.split()[1])
    active_states[idx] = not active_states[idx]

    global latest_combined
    latest_combined = np.zeros_like(img_np, dtype=np.uint8)
    for i in range(8):
        if active_states[i]:
            latest_combined += (bit_planes[i] << i)

    img_display.set_data(latest_combined)
    fig.canvas.draw_idle()

def save_image(event):
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
                                             title="Save reconstructed image")
    if save_path:
        Image.fromarray(latest_combined).save(save_path)
        print(f"Saved to: {save_path}")

checkbox.on_clicked(update)
save_button.on_clicked(save_image)

plt.show()
