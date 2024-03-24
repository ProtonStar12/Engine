#!/bin/bash

# Install Python if not already installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before running this script."
    exit 1
fi

# Install pip if not already installed
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed. Please install pip before running this script."
    exit 1
fi

# Install numpy and sumpy via pip
echo "Installing numpy and sumpy via pip..."
pip3 install numpy sumpy

# Check if numpy and sumpy were installed successfully
if ! python3 -c "import numpy, sumpy" &> /dev/null; then
    echo "Failed to install numpy or sumpy. Please check your internet connection and try again."
    exit 1
fi

# Set up alias for running menu.py
echo "Setting up alias 'Engine'..."
echo "alias Engine='python3 $(pwd)/Engine/menu.py'" >> ~/.bashrc

echo "Alias 'Engine' added. You can now use 'Engine' command to run menu.py."
