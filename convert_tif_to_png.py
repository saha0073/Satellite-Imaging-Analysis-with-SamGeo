import os
from glob import glob
import rasterio
from PIL import Image
import numpy as np

# Get all .tif files in the current directory
for tif_path in glob("*.tif"):
    with rasterio.open(tif_path) as src:
        arr = src.read()
        # If the image has more than 3 bands, use the first 3 for RGB
        if arr.shape[0] >= 3:
            img = np.stack([arr[0], arr[1], arr[2]], axis=-1)
        else:
            # For single-band (mask/annotation), just use the first band
            img = arr[0]
        # Normalize if needed
        if img.dtype != np.uint8:
            img = (255 * (img.astype(np.float32) / img.max())).astype(np.uint8)
        # Convert to PIL Image
        pil_img = Image.fromarray(img)
        # Save as PNG
        png_path = tif_path.replace('.tif', '.png')
        pil_img.save(png_path)
        # Save as JPG
        jpg_path = tif_path.replace('.tif', '.jpg')
        pil_img.convert('RGB').save(jpg_path)
        print(f"Converted {tif_path} to {png_path} and {jpg_path}") 