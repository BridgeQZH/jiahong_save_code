import re
import random
import statistics
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

def find_winning_list_counts(lists):
    num_lists = len(lists)
    list_length = len(lists[0])
    counts = [0] * num_lists

    for i in range(list_length):
        max_value = float('-inf')
        max_indices = []

        for j in range(num_lists):
            if lists[j][i] > max_value:
                max_value = lists[j][i]
                max_indices = [j]
            elif lists[j][i] == max_value:
                max_indices.append(j)

        for idx in max_indices:
            counts[idx] += 1

    return counts

# Path to the text file containing the metrics
# file_path = '/home/eric/Downloads/A2/image_analysis_ImageNET_500.txt'
# file_path = '/home/eric/Downloads/A2/image_analysis_Dalle2_SDM_1000.txt'
# file_path = '/home/eric/Downloads/A2/image_analysis_Dalle2_later_50.txt'
# file_path = '/home/eric/Downloads/A2/image_analysis_Dalle2_later_50.txt'
file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_ImageNET_10000.txt'
# file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_SDM_1000.txt'
# file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_Dalle2_1000.txt'
# file_path = '/home/zihan/Downloads/Dataset_image/image_analysis_BigGAN_50_original.txt'


# file_path = '/home/eric/Downloads/A2/image_analysis_BigGAN_50.txt'

# Initialize variables
num_images = 0
total_canny_edge_density = 0
total_gabor_energy = 0
# total_Variance_Blur_Measure = 0
total_GLCM_contrast = 0
total_GLCM_energy = 0
total_GLCM_homogeneity = 0
total_Variance_Blur_Measure = 0
total_realism1 = 0
total_realism2 = 0
total_realism3 = 0
total_realism4 = 0
total_realism5 = 0
total_realism6 = 0
total_realism7 = 0
total_realism8 = 0
total_realism9 = 0
total_realism10 = 0
total_realism11 = 0
total_realism12 = 0
fake_num1 = 0
fake_num2 = 0
fake_num3 = 0
fake_num4 = 0
fake_num5 = 0
fake_num6 = 0
fake_num7 = 0
fake_num8 = 0
fake_num9 = 0
fake_num10 = 0
fake_num11 = 0
fake_num12 = 0
real_num = 0
def_fake_num = 0
mid_num = 0
thres = 1  # We fix this value for testing different realism formula
# thres2 = 2.97
total_spectrum = 0
realism_list1 = []
realism_list2 = []
realism_list3 = []
realism_list4 = []
realism_list5 = []
realism_list6 = []
realism_list7 = []
realism_list8 = []
realism_list9 = []
realism_list11 = []
realism_list10 = []
realism_list12 = []
spectrum_match_list = []
GLCM_contrast_list = []
GLCM_energy_list = []
canny_edge_density_list = []
Variance_Blur_Measure_list = []
max_realism_number = {}

# Open the text file and read the lines
with open(file_path, 'r') as f:
    lines = f.readlines()

# Iterate over the lines and extract the metrics
for line in lines:
    # Use regular expressions to extract the relevant values
    image_match = re.match(r"Image: (.+)", line)
    canny_match = re.match(r"metric 3 Canny_edge_density: (.+)", line)
    gabor_match = re.match(r"gabor_energy: (.+)", line)
    Variance_Blur_Measure_match = re.match(r"metric 4 Variance_Blur_Measure: (.+)", line)
    GLCM_contrast_match = re.match(r"metric 1 GLCM_contrast: (.+)", line)
    GLCM_energy_match = re.match(r"metric 2 GLCM_energy: (.+)", line)
    GLCM_homogeneity_match = re.match(r"GLCM_homogeneity: (.+)", line)
    realism_match1 = re.match(r"realism1: (.+)", line)
    realism_match2 = re.match(r"realism2: (.+)", line)
    realism_match3 = re.match(r"realism3: (.+)", line)
    realism_match4 = re.match(r"realism4: (.+)", line)
    realism_match5 = re.match(r"realism5: (.+)", line)
    realism_match6 = re.match(r"realism6: (.+)", line)
    realism_match7 = re.match(r"realism7: (.+)", line)
    realism_match8 = re.match(r"realism8: (.+)", line)
    realism_match9 = re.match(r"realism9: (.+)", line)
    realism_match10 = re.match(r"realism10: (.+)", line)
    realism_match11 = re.match(r"realism11: (.+)", line)
    realism_match12 = re.match(r"realism12: (.+)", line)
    spectrum_match = re.match(r"metric 5 Mean_spectrum: (.+)", line)

    
    if image_match:
        num_images += 1
    elif canny_match:
        canny_edge_density = float(canny_match.group(1))
        canny_edge_density_list.append(canny_edge_density)
        total_canny_edge_density += canny_edge_density
    elif gabor_match:
        gabor_energy = float(gabor_match.group(1))
        total_gabor_energy += gabor_energy
    elif Variance_Blur_Measure_match:
        Variance_Blur_Measure = float(Variance_Blur_Measure_match.group(1))
        Variance_Blur_Measure_list.append(Variance_Blur_Measure)
        total_Variance_Blur_Measure += Variance_Blur_Measure
    elif GLCM_contrast_match:
        GLCM_contrast = float(GLCM_contrast_match.group(1))
        GLCM_contrast_list.append(GLCM_contrast)
        total_GLCM_contrast += GLCM_contrast
    elif spectrum_match:
        spectrum = float(spectrum_match.group(1))
        spectrum_match_list.append(spectrum)
        total_spectrum += spectrum
    elif GLCM_energy_match:
        GLCM_energy = float(GLCM_energy_match.group(1))
        GLCM_energy_list.append(GLCM_energy)
        total_GLCM_energy += GLCM_energy
    elif GLCM_homogeneity_match:
        GLCM_homogeneity = float(GLCM_homogeneity_match.group(1))
        total_GLCM_homogeneity += GLCM_homogeneity
    elif realism_match1:
        realism1 = float(realism_match1.group(1))
        realism_list1.append(realism1)
        if realism1 <= thres:
            fake_num1 += 1
            # def_fake_num += 1
    elif realism_match2:
        realism2 = float(realism_match2.group(1))
        realism_list2.append(realism2)
        if realism2 <= thres:
            fake_num2 += 1
            # def_fake_num += 1
    elif realism_match3:
        realism3 = float(realism_match3.group(1))
        realism_list3.append(realism3)
        if realism3 <= thres:
            fake_num3 += 1
            # def_fake_num += 1
    elif realism_match4:
        realism4 = float(realism_match4.group(1))
        realism_list4.append(realism4)
        if realism4 <= thres:
            fake_num4 += 1
            # def_fake_num += 1
    elif realism_match5:
        realism5 = float(realism_match5.group(1))
        realism_list5.append(realism5)
        if realism5 <= thres:
            fake_num5 += 1
            # def_fake_num += 1
    elif realism_match6:
        realism6 = float(realism_match6.group(1))
        realism_list6.append(realism6)
        if realism6 <= thres:
            fake_num6 += 1
            # def_fake_num += 1
    elif realism_match7:
        realism7 = float(realism_match7.group(1))
        realism_list7.append(realism7)
        if realism7 <= thres:
            fake_num7 += 1
            # def_fake_num += 1
    elif realism_match8:
        realism8 = float(realism_match8.group(1))
        realism_list8.append(realism8)
        if realism8 <= thres:
            fake_num8 += 1
            # def_fake_num += 1
    elif realism_match9:
        realism9 = float(realism_match9.group(1))
        realism_list9.append(realism9)
        if realism9 <= thres:
            fake_num9 += 1
            # def_fake_num += 1
    elif realism_match10:
        realism10 = float(realism_match10.group(1))
        realism_list10.append(realism10)
        if realism10 <= thres:
            fake_num10 += 1
            # def_fake_num += 1
    elif realism_match11:
        realism11 = float(realism_match11.group(1))
        realism_list11.append(realism11)
        if realism11 <= thres:
            fake_num11 += 1
            # def_fake_num += 1
    elif realism_match12:
        realism12 = float(realism_match12.group(1))
        realism_list12.append(realism12)
        if realism12 <= thres:
            fake_num12 += 1
            # def_fake_num += 1
        # else:
        #     real_num += 1
        # if realism > thres and realism < thres2:
        #     mid_num += 1
        #     prob = (realism - thres) / (thres2-thres)
        #     random_number = random.random()  # Generates a random float between 0 and 1
        #     if random_number >= prob:
        #         fake_num += 1
        total_realism1 += realism1

# Calculate the average values
average_canny_edge_density = total_canny_edge_density / num_images
average_gabor_energy = total_gabor_energy / num_images
average_GLCM_contrast = total_GLCM_contrast / num_images
average_GLCM_energy = total_GLCM_energy / num_images
average_GLCM_homogeneity = total_GLCM_homogeneity / num_images
# average_realism = total_realism / num_images
average_spectrum = total_spectrum / num_images
average_Variance_Blur_Measure = total_Variance_Blur_Measure / num_images

# Print the average values
print(file_path)
# print(f"Average Spectrum: {average_spectrum}")
print(f"total number of images: {num_images}")
print(f"avg realism 1 area: {sum(realism1)/len(realism1)}")
# print(f"Average Canny Edge Density: {average_canny_edge_density}")
# print(f"Average Gabor Energy: {average_gabor_energy}")
# print(f"Average GLCM contrast: {average_GLCM_contrast}")
# print(f"Average GLCM energy: {average_GLCM_energy}")
max_fake_num = max(fake_num1, fake_num2, fake_num3, fake_num4, fake_num5, fake_num6, fake_num7, fake_num8, fake_num9, fake_num10, fake_num11, fake_num12)
min_fake_num = min(fake_num1, fake_num2, fake_num3, fake_num4, fake_num5, fake_num6, fake_num7, fake_num8, fake_num9, fake_num10, fake_num11, fake_num12)
# print(f"Fake_num1: {fake_num1}")
# print(f"Fake_num2: {fake_num2}")
# print(f"Fake_num3: {fake_num3}")
# print(f"Fake_num4: {fake_num4}")
# print(f"Fake_num5: {fake_num5}")
# print(f"Fake_num6: {fake_num6}")
# print(f"Fake_num7: {fake_num7}")
# print(f"Fake_num8: {fake_num8}")
# print(f"Fake_num9: {fake_num9}")
# print(f"Fake_num10: {fake_num10}")
# print(f"Fake_num11: {fake_num11}")
# print(f"Fake_num12: {fake_num12}")
print(f"Max Fake_num of 12 realisms: {max_fake_num}")
print(f"Min Fake_num of 12 realisms: {min_fake_num}")
print(len(spectrum_match_list))



# Example usage
lists = [realism_list1, realism_list2, realism_list3, realism_list4, realism_list5, realism_list6, realism_list7, realism_list8, realism_list9, realism_list10, realism_list11, realism_list12]  # Replace the ellipsis with the remaining lists

counts = find_winning_list_counts(lists)

for i, count in enumerate(counts):
    print(f"list{i+1}: {count} times")

print(f"The list that wins the most is list{max_index + 1} with {max_count} highest values.")

# Plotting the list
# plt.plot(spectrum_match_list)

# # Display the plot
# plt.show()
# Creating subplots
# fig, (ax1, ax2) = plt.subplots(2)

# # Plotting data in the first subplot
# ax1.plot(spectrum_match_list)
# ax1.set_title('Spectrum performance')

# # Plotting data in the second subplot
# ax2.plot(GLCM_contrast_list)
# ax2.set_title('GLCM Contrast performance')

# # Adjusting spacing between subplots
# plt.subplots_adjust(hspace=0.5)

# # Display the subplots
# plt.show()



# Calculate the Pearson correlation coefficient
correlation_coefficient, p_value = pearsonr(GLCM_contrast_list, GLCM_energy_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM Contrast and GLCM Energy:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_contrast_list, canny_edge_density_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM Contrast and canny_edge_density:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_contrast_list, Variance_Blur_Measure_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM Contrast and Variance_Blur_Measure:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_contrast_list, spectrum_match_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM Contrast and Spectrum match:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_energy_list, canny_edge_density_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM Energy and canny_edge_density:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_energy_list, Variance_Blur_Measure_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM_energy and Variance_Blur_Measure:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(GLCM_energy_list, spectrum_match_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between GLCM_energy and spectrum:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(canny_edge_density_list, Variance_Blur_Measure_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between canny_edge_density_list and Variance_Blur_Measure_list:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(canny_edge_density_list, spectrum_match_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between canny_edge_density and spectrum_match_list:", correlation_coefficient)

correlation_coefficient, p_value = pearsonr(Variance_Blur_Measure_list, spectrum_match_list)

# Print the correlation coefficient
print("Pearson correlation coefficient between Variance_Blur_Measure and spectrum:", correlation_coefficient)

# Plotting data in the first figure
# plt.figure()
# plt.plot(GLCM_contrast_list)
# plt.title('GLCM Contrast performance')
# plt.xlabel('Ordinal')
# plt.ylabel('Value')

# plt.figure()
# plt.plot(GLCM_energy_list)
# plt.title('GLCM Energy performance')
# plt.xlabel('Ordinal')
# plt.ylabel('Value')

# plt.figure()
# plt.plot(canny_edge_density_list)
# plt.title('Canny edge density performance')
# plt.xlabel('Ordinal')
# plt.ylabel('Value')

# plt.figure()
# plt.plot(Variance_Blur_Measure_list)
# plt.title('Variance Blur Measure performance')
# plt.xlabel('Ordinal')
# plt.ylabel('Value')

# plt.figure()
# plt.plot(spectrum_match_list)
# plt.title('Spectrum performance')
# plt.xlabel('Ordinal')
# plt.ylabel('Value')

# Plotting data in the second figure350 SEK + 150 SEK


# plt.show()



# print(f"Average GLCM homogeneity: {average_GLCM_homogeneity}")
# print(f"Average realism: {average_realism}")
# print(f"total number of fake images: {fake_num}")
# print(f"total number of def fake images: {def_fake_num}")
# print(f"total number of middle images: {mid_num}")
# print(f"total number of definite real images: {real_num}")
# print(realism_list)

# median = statistics.median(realism_list)
# max_value = max(realism_list)
# min_value = min(realism_list)
# Print the median
# print("Median:", median)
# print("Max:", max_value)
# print("Min:", min_value)
# print(f"Average Variance Blur Measure: {average_Variance_Blur_Measure}")
# Create a histogram
# plt.hist(realism_list, bins=10)  # Adjust the number of bins as needed

# # Add labels and a title
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram')

# # Show the plot
# plt.show()
