from PIL import Image

def get_image_size(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
    return width, height

def save_image_size(image_path, output_file):
    width, height = get_image_size(image_path)
    size_info = f"Width: {width}px, Height: {height}px"

    with open(output_file, 'w') as file:
        file.write(size_info)

# Provide the input image path and output text file path
input_image_path = "/home/zihan/Downloads/Dataset_image/ImageNET_500/500_images/ILSVRC2013_train_00030006.JPEG"
output_text_file = "/home/zihan/Downloads/Dataset_image/Realism_ImageNET.txt"

# Call the function to save the image size
save_image_size(input_image_path, output_text_file)
