# Image Compression

## Overview
This project provides a tool for compressing images using various algorithms.

## Installation Instructions

### Windows
1. Download the latest release from the [releases page](https://github.com/arkay-kudali/image_compression/releases).
2. Extract the ZIP file and navigate to the extracted folder.
3. Run the installer.

### Linux
1. Clone the repository:
   ```bash
   git clone https://github.com/arkay-kudali/image_compression.git
   cd image_compression
   ```
2. Install the required dependencies:
   ```bash
   sudo apt-get install build-essential
   sudo apt-get install <other-dependencies>
   ```
3. Run the setup script:
   ```bash
   ./setup.sh
   ```

### macOS
1. Clone the repository:
   ```bash
   git clone https://github.com/arkay-kudali/image_compression.git
   cd image_compression
   ```
2. Install Homebrew if you haven't already:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install the required dependencies:
   ```bash
   brew install <dependencies>
   ```

## Library Dependencies
- `dependency1`
- `dependency2`
- `dependency3`

## Setup Guide
1. After installation, ensure all dependencies are correctly set up using the following command:
   ```bash
   python check_setup.py
   ```
2. If any dependencies are missing, the script will provide instructions on how to install them.

## Usage Examples
- To compress a single image:
   ```bash
   python compress.py --input image.jpg --output compressed_image.jpg
   ```
- To compress multiple images at once:
   ```bash
   python compress.py --input *.jpg --output compressed/
   ```

## Troubleshooting
- **Issue:** Installation fails on Windows 10.
  - **Solution:** Ensure you have the latest version of Windows and update your Python installation.
- **Issue:** Dependency not found.
  - **Solution:** Recheck the installation steps and ensure all library dependencies are met.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or new features!