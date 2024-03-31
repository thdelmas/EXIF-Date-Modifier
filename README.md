# EXIF Date Modifier

The EXIF Date Modifier script (`EXIF-Date-Modifier.py`) is a Python utility designed to copy image files from a source directory to a destination directory, updating or adding EXIF date information to each image based on a specified date. This tool is particularly useful for photographers, digital archivists, and anyone needing to standardize the date metadata of a collection of image files.

## Features

- Copies all JPEG and TIFF images from a specified source directory to a destination directory.
- Updates existing EXIF date information or adds it if missing, setting it to a user-defined date.
- Logs all operations, providing a detailed account of changes made to each file.

## Requirements

Before running the script, ensure you have Python installed on your system (Python 3.6 or newer is recommended). You will also need to install the `piexif` library, which can be done via pip:

```sh
pip install piexif
```

## Usage

To use the script, you need to provide three command-line arguments:
1. The path to the source directory (`src_folder`) containing the images whose EXIF dates you wish to modify.
2. The path to the destination directory (`dst_folder`) where the modified images will be copied. This directory will be created if it does not already exist.
3. The new date in the format `DD/MM/YYYY`, which will be used to update the EXIF date metadata in the images.

### Syntax

```sh
python EXIF-Date-Modifier.py <src_folder> <dst_folder> <DD/MM/YYYY>
```

### Example

```sh
python EXIF-Date-Modifier.py ./old_photos ./updated_photos 01/01/2021
```

This command will copy all JPEG and TIFF images from `./old_photos` to `./updated_photos`, setting their EXIF dates to January 1, 2021. A log file named `copy_log.txt` will be created in the destination directory, listing the operations performed on each file.

## Troubleshooting

- Ensure all paths provided are correct and accessible by the script.
- The script only processes files with `.jpg`, `.jpeg`, and `.tiff` extensions. Other file types are ignored.
- If you encounter permission errors, check that you have read/write access to the involved directories.

## Contributing

Contributions to the EXIF Date Modifier are welcome! Feel free to fork the repository, make your changes, and submit a pull request. Whether it's a bug fix, feature addition, or documentation improvement, your help is appreciated.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as you see fit.

## Contact

For questions, suggestions, or bug reports, please open an issue in the GitHub repository. Your feedback is important to improve this tool.
