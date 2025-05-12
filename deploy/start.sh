# start.sh
#!/bin/bash

# Ensure Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 not found. Please install it first."
    exit
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

source venv/bin/activate

# Install dependencies
pip install flask

# Start the Flask app
python3 app.py