import os
from PIL import Image

# Paths for input and output folders
input_folder = "All_Acne_Image"
output_folder = "Resize_Image"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # Check if the file is an image
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize((200, 200))

                # Save the resized image to the output folder
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)

                print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("Image resizing completed.")
