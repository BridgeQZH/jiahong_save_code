import re
import matplotlib.pyplot as plt

# Path to the text file containing the metrics
file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_ImageNET_500.txt'

# Initialize lists to store the metric values
canny_edge_density_values = []
gabor_energy_values = []

# Open the text file and read the lines
with open(file_path, 'r') as f:
    lines = f.readlines()

# Iterate over the lines and extract the metric values
for line in lines:
    # Use regular expressions to extract the relevant values
    canny_match = re.match(r"Canny_edge_density: (.+)", line)
    gabor_match = re.match(r"gabor_energy: (.+)", line)
    
    if canny_match:
        canny_edge_density = float(canny_match.group(1))
        canny_edge_density_values.append(canny_edge_density)
    elif gabor_match:
        gabor_energy = float(gabor_match.group(1))
        gabor_energy_values.append(gabor_energy)

# Plot the values in an XY graph
plt.scatter(canny_edge_density_values, gabor_energy_values)
plt.xlabel('Canny Edge Density')
plt.ylabel('Gabor Energy')
plt.title('ImageNET 500 Image Metrics')
plt.show()
