#!/usr/bin/env python3

import os
import shutil
import sys
from datetime import datetime
import piexif

def create_or_update_exif_date(image_path, new_date):
    try:
        # Attempt to load existing EXIF data; if none exists, create a new, empty EXIF dict
        try:
            exif_dict = piexif.load(image_path)
        except piexif.InvalidImageDataError:
            exif_dict = {"0th": {}, "Exif": {}, "1st": {}, "thumbnail": None, "GPS": {}}

        new_exif_date = datetime.strptime(new_date, "%d/%m/%Y").strftime("%Y:%m:%d %H:%M:%S")

        # Ensure the relevant tags exist in the '0th' and 'Exif' groups
        exif_dict['0th'][piexif.ImageIFD.DateTime] = new_exif_date.encode('utf-8')
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_exif_date.encode('utf-8')
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_exif_date.encode('utf-8')

        # Generate and insert new EXIF bytes
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, image_path)
        print(f"Updated or created EXIF date for '{image_path}' to '{new_exif_date}'.")
    except Exception as e:
        print(f"Error updating or creating EXIF data for '{image_path}': {e}")

def is_image_file(filepath):
    """Check if the file is a JPEG or TIFF image."""
    return filepath.lower().endswith(('.jpg', '.jpeg', '.tiff'))

def main(src_folder, dst_folder, date):
    if not os.path.isdir(src_folder):
        print("Source folder does not exist.")
        sys.exit(1)

    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder)

    log_file_path = os.path.join(dst_folder, "copy_log.txt")
    with open(log_file_path, "w") as log_file:
        for filename in os.listdir(src_folder):
            src_path = os.path.join(src_folder, filename)
            dst_path = os.path.join(dst_folder, filename)

            if os.path.isfile(src_path) and is_image_file(src_path):
                shutil.copy2(src_path, dst_path)
                create_or_update_exif_date(dst_path, date)
                log_file.write(f"Copied and updated or created EXIF date for '{filename}'\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <src_folder> <dst_folder> <DD/MM/YYYY>")
        sys.exit(1)

    src_folder = sys.argv[1]
    dst_folder = sys.argv[2]
    date = sys.argv[3]

    main(src_folder, dst_folder, date)

