#! /usr/bin/bash

printf "Starting the virtual environment.\n\n"

# Activate virtualenv
source env/bin/activate

printf "Installing dependencies first.\n\n"
# Install dependencies first
pip install -r requirements.txt

printf "Installation complete.\n\nRunning script.\n\n"

# Run the solution
python solution.py

printf "\nMeasuring time taken to complete job.\n\n"

time python solution.py


# Deactivate
deactivate
