# %%
import cv2
import matplotlib.pyplot as plt
from skimage import exposure
import numpy as np

img = cv2.imread('drawing-2.png')
# show image using matplotlib

plt.imshow(img)
# %%
# split into independent channels red, green, blue

r, g, b = cv2.split(img)
# %% show red channel in grayscale
plt.imshow(r, cmap='gray')
r.shape
# %% scale up contrast of red channel based on histogram
r_eq = exposure.equalize_hist(r) * 255.0
plt.imshow(r_eq, cmap='gray')
# %%
# new image with average pixels of r and r_eq
r_avg = (r + r_eq) // 2
plt.imshow(r_avg, cmap='gray')
# %%
plt.imshow(r, cmap='gray')
# %%
np.abs(r_eq - r)
# %%
r
# %%
r_eq
# %%
# combine above into a function so we can apply to all channels
# one channel at a time
def equalize_channel(channel):
    channel_eq = exposure.equalize_hist(channel) * 255.0
    channel_avg = (channel + channel_eq) // 2
    return channel_avg
lin_eq_r = equalize_channel(r)
lin_eq_g = equalize_channel(g)

plt.imshow(lin_eq_r, cmap='gray')
# %%
plt.imshow(lin_eq_g, cmap='gray')
# %%

import hatched as H
from IPython.display import display, SVG, HTML


def _repr_svg_(geom):
    """SVG representation for iPython notebook"""
    svg_top = (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'xmlns:xlink="http://www.w3.org/1999/xlink" '
    )
    if geom.is_empty:
        return svg_top + "/>"
    else:
        # Establish SVG canvas that will fit all the data + small space
        xmin, ymin, xmax, ymax = geom.bounds
        if xmin == xmax and ymin == ymax:
            # This is a point; buffer using an arbitrary size
            xmin, ymin, xmax, ymax = geom.buffer(1).bounds
        else:
            # Expand bounds by a fraction of the data ranges
            expand = 0.04  # or 4%, same as R plots
            widest_part = max([xmax - xmin, ymax - ymin])
            expand_amount = widest_part * expand
            xmin -= expand_amount
            ymin -= expand_amount
            xmax += expand_amount
            ymax += expand_amount
        dx = xmax - xmin
        dy = ymax - ymin
        width = min([max([100.0, dx]), 300])
        height = min([max([100.0, dy]), 300])
        try:
            scale_factor = max([dx, dy]) / max([width, height])
        except ZeroDivisionError:
            scale_factor = 1.0
        view_box = f"{xmin} {ymin} {dx} {dy}"
        transform = f"matrix(1,0,0,-1,0,{ymax + ymin})"
        return svg_top + (
            'width="{1}" height="{2}" viewBox="{0}" '
            'preserveAspectRatio="xMinYMin meet">'
            '<g transform="{3}">{4}</g></svg>'
        ).format(view_box, width, height, transform, geom.svg(scale_factor))
# %%
(htch,*rest) = H._build_hatch(lin_eq_g)
# %%
svg  =SVG(_repr_svg_(htch))# %%
svg
# %%

# %%
np.array(rest).shape
# %%
htch
# %%
type(htch)
# %%
display(htch)

# %%
import cairosvg

# %%
cairosvg.svg2
# %%

# use the hatch function directly but save to in memory buffer 
# %%

import cairosvg
import io
from PIL import Image

def svgRead(svg):
   """Load an SVG file and return image in Numpy array"""
   # Make memory buffer
   mem = io.BytesIO()
   # Convert SVG to PNG in memory
   cairosvg.svg2png(bytestring=svg, write_to=mem, dpi=900)
   # Convert PNG to Numpy array
   return np.array(Image.open(mem))

# %%
plt.imshow(svgRead(svg.data))
# %%

plt.imshow(np.transpose(svgRead(svg.data)[:,:,1]))
# %%
plt.imshow(svgRead(svg.data)[:,:,1], cmap='gray')
plt.gca().invert_yaxis()
# %%
# %%
