from PIL import Image

# Set the border and color
borderSize = 40
color = (255, 255, 255)
imgPath = "image.png"

# Open original image and extract the alpha channel
im = Image.open(imgPath)
alpha = im.getchannel('A')

# Create white image the same size and copy alpha channel across
background = Image.new('RGBA', im.size, color=color)
background.putalpha(alpha) 

# Make the background bigger
background=background.resize((background.size[0]+borderSize, background.size[1]+borderSize))

# Merge the targeted image (foreground) with the background
foreground = Image.open(imgPath)
background.paste(foreground, (int(borderSize/2), int(borderSize/2)), foreground.convert("RGBA"))
imageWithBorder = background
imageWithBorder.show()
