import shutil
from operator import itemgetter
from PIL import Image, ImageDraw, ImageFont
# read point colour and coordinates from file
points = []
break_pt=[]
def read_points_from_file(file_path):
    with open(file_path, 'r') as file:
        black = 1
        yellow=0
        nodot=0
        count=0
        for line in file:
            # Strip any leading/trailing whitespace characters (including newline)
#            print(line)
            line = line.strip()
            count=black+yellow+nodot
#            print(count)
            if line:  # Proceed if the line is not empty
                # Split the line by comma and strip any extra spaces
                parts = [part.strip() for part in line.split(' ')]
                if len(parts) == 3:
                    colour = parts[0]
#                    print(colour)
                    if colour == 'black': black = black +1
                    if colour == 'yellow': yellow = yellow +1
                    if colour == 'No_Dot': 
                        nodot = nodot +1
                        break_pt.append(count)
                    x = int(parts[1].strip('(').strip(','))
                    y = int(parts[2].strip(')').strip(','))
# Append as a tuple (point_name, (x, y))
                    points.append((colour, (x, y)))
        return points

# Change file name and path:
file_path = 'coord.txt'  # Path to your text file
points_array = read_points_from_file(file_path)

# Output the result
# Create a new image with white background from the first file
image_dir = 'D:/assets'
image_file = 'pilimg.png'

width, height = 512, 512
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# List of points (example points)
coords = list(map(itemgetter(1), points_array)) 
colors = list(map(itemgetter(0), points_array))

# Draw lines connecting the points
for i in range(len(coords) - 1):
    color = colors[i] 
    if colors[i] == 'No_Dot': 
        for point in break_pt:
            if i == (point-1): 
                i=i+1
    else:
        draw.line((coords[i], coords[i + 1]), fill=color, width=3)           
# Save the image
image.save('lines_image.png')

# Show the image (optional)
image.show()
