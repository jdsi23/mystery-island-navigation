#!/bin/bash

# Navigate into the project root
cd /home/ec2-user/mystery-island-navigation

# Reset permissions just in case
sudo chown -R ec2-user:ec2-user .

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Flask
pip install flask

# Run the Flask app in the background and log output
nohup python3 api/app.py > output.log 2>&1 &
