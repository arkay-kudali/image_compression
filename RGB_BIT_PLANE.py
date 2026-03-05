import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Button
from PIL import Image
from tkinter import Tk, filedialog

# GUI: Select image
Tk().withdraw()
file_path = filedialog.askopenfilename(title="Select an RGB image",
                                       filetypes=[("Image files", "*.png *.jpg *.bmp *.jpeg")])
if not file_path:
    print("No image selected.")
    exit()

# Load image and convert to RGB
img = Image.open(file_path).convert('RGB')
img_np = np.array(img, dtype=np.uint8)

# Split into channels
r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]

# Extract 8 bit planes for each channel
bit_planes_r = [(r >> i) & 1 for i in range(8)]
bit_planes_g = [(g >> i) & 1 for i in range(8)]
bit_planes_b = [(b >> i) & 1 for i in range(8)]

# Create display
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.35, bottom=0.2)
combined_rgb = np.zeros_like(img_np, dtype=np.uint8)
img_display = ax.imshow(combined_rgb)
ax.set_title("Combined Bit Planes (RGB)")
ax.axis('off')

# Checkbox labels
labels_r = [f'R{i}' for i in reversed(range(8))]
labels_g = [f'G{i}' for i in reversed(range(8))]
labels_b = [f'B{i}' for i in reversed(range(8))]

all_labels = labels_r + labels_g + labels_b
active_states = [False] * 24

# Checkboxes: Position for RGB bitplanes
rax = plt.axes([0.05, 0.35, 0.25, 0.55])
checkbox = CheckButtons(rax, all_labels, active_states)

# Save button
save_ax = plt.axes([0.05, 0.15, 0.25, 0.075])
save_button = Button(save_ax, 'Save Image')

# Store latest image
latest_combined = np.zeros_like(img_np, dtype=np.uint8)

def update(label):
    index = all_labels.index(label)
    active_states[index] = not active_states[index]

    global latest_combined

    combined_r = np.zeros_like(r, dtype=np.uint8)
    combined_g = np.zeros_like(g, dtype=np.uint8)
    combined_b = np.zeros_like(b, dtype=np.uint8)

    for i in range(8):
        if active_states[i]:        # R
            combined_r += (bit_planes_r[i] << i)
        if active_states[8 + i]:    # G
            combined_g += (bit_planes_g[i] << i)
        if active_states[16 + i]:   # B
            combined_b += (bit_planes_b[i] << i)

    latest_combined = np.stack([combined_r, combined_g, combined_b], axis=-1)
    img_display.set_data(latest_combined)
    fig.canvas.draw_idle()

def save_image(event):
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")],
                                             title="Save reconstructed RGB image")
    if save_path:
        Image.fromarray(latest_combined).save(save_path)
        print(f"Saved to: {save_path}")

checkbox.on_clicked(update)
save_button.on_clicked(save_image)

plt.show()
