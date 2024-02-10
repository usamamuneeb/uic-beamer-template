"""
To install requirements:

    pip install pillow cairosvg

If you have DLL related issues with the `cairosvg` package,
try running this in Google Colab.

Replace `svg_path` with your departmental logo.
"""

from PIL import Image
import cairosvg
import io

svg_path = "COL.ENG.ECE.LOCKC.SM.INVT.RGB.SVG"
svg_data = open(svg_path, 'rb').read()

overlay_width = 2016
left_offset = 4032//2 - overlay_width//2
png_output = cairosvg.svg2png(svg_data, output_width=overlay_width)
svg_img = Image.open(io.BytesIO(png_output))
background_color = (0, 30, 98)  # This color is Navy Pier Blue
img = Image.new('RGB', (4032,3024), background_color)
img.paste(svg_img, (left_offset, 2016), svg_img)
img.save(f"{svg_path}.png")
