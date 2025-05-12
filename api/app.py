# app.py
#!/bin/bash

echo "🔧 Starting Mystery Island Navigation Flask App..."

# Navigate to the API folder
cd "$(dirname "$0")/../api"

# Set up venv (optional but ideal)
cd ..
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Export Flask environment variables
export FLASK_APP=api/app.py
export FLASK_ENV=development  # Optional: Enables debugger

# Run Flask app in background with logging
echo "🚀 Launching on http://0.0.0.0:5000"
nohup flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 &
