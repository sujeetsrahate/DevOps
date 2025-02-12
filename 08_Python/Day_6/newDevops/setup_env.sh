#!/bin/bash

# Step 1: Create a new virtual environment
echo "Creating virtual environment..."
python3 -m venv my_env

# Step 2: Activate the virtual environment
echo "Activating virtual environment..."
source my_env/bin/activate

# Step 3: Install required packages
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Run a Python file
echo "Running Python script..."
python3 my_script.py

# Step 5: Deactivate the virtual environment
echo "Deactivating virtual environment..."
deactivate
