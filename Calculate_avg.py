import re

# Path to the text file containing the metrics
file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_BigGAN_50.txt'

# Initialize variables
num_images = 0
total_canny_edge_density = 0
total_gabor_energy = 0
total_Variance_Blur_Measure = 0

# Open the text file and read the lines
with open(file_path, 'r') as f:
    lines = f.readlines()

# Iterate over the lines and extract the metrics
for line in lines:
    # Use regular expressions to extract the relevant values
    image_match = re.match(r"Image: (.+)", line)
    canny_match = re.match(r"Canny_edge_density: (.+)", line)
    gabor_match = re.match(r"gabor_energy: (.+)", line)
    Variance_Blur_Measure_match = re.match(r"Variance_Blur_Measure: (.+)", line)
    
    if image_match:
        num_images += 1
    elif canny_match:
        canny_edge_density = float(canny_match.group(1))
        total_canny_edge_density += canny_edge_density
    elif gabor_match:
        gabor_energy = float(gabor_match.group(1))
        total_gabor_energy += gabor_energy
    elif Variance_Blur_Measure_match:
        Variance_Blur_Measure = float(Variance_Blur_Measure_match.group(1))
        total_Variance_Blur_Measure += Variance_Blur_Measure

# Calculate the average values
average_canny_edge_density = total_canny_edge_density / num_images
average_gabor_energy = total_gabor_energy / num_images
average_Variance_Blur_Measure = total_Variance_Blur_Measure / num_images

# Print the average values
print(f"Average Canny Edge Density: {average_canny_edge_density}")
print(f"Average Gabor Energy: {average_gabor_energy}")
print(f"Average Variance Blur Measure: {average_Variance_Blur_Measure}")
