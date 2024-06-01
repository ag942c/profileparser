#!/bin/bash

# Update the package list and install pip if it's not already installed
echo "Updating package list and installing pip..."
sudo apt-get update
sudo apt-get install -y python3-pip

# Install virtualenv to create an isolated Python environment
echo "Installing virtualenv..."
pip3 install virtualenv

# Create a virtual environment for the project
echo "Creating a virtual environment..."
virtualenv venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Install the required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Run the Python API
echo "Running the Python API..."
python api.py

# Deactivate the virtual environment after the script finishes
echo "Deactivating the virtual environment..."
deactivate

echo "Setup and execution completed."