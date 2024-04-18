import os;
from PIL import Image;

def img_to_webp(input_folder, output_folder):
    """
  Converts images from input_folder to WebP format and saves them in output_folder.

  Args:
      input_folder: Path to the folder containing the images to convert.
      output_folder: Path to the folder where converted WebP images will be saved.
  """
    print("\n")
    
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' does not exist. Create the folder in same directory as file \n")
        return

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        # Check if it's a valid image file and skip if it is not
        if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            print(f"Skipping non-image file: '{filename}'\n")
            continue

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

        try:
            image = Image.open(input_path)
            print(f"Converting {filename} to WebP...")
            image.save(output_path, 'WebP', optimize=True, quality=80)
            print(f"{filename} converted and saved as {os.path.basename(output_path)}.\n")

        except (IOError, OSError) as e:
            print(f"Error converting {filename}: {e}\n")
        except Exception as e:
            print(f"Unexpected error converting {filename}: {e}\n")


img_to_webp('input', 'output')
