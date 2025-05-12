# Mystery Island Navigation System

Welcome to the official navigation system project for **Mystery Island Theme Park** — a dynamic map-based experience designed to help guests explore attractions, view descriptions, and navigate the park like never before.

---

## 🗺️ Features
- Interactive island map with clickable attraction icons
- Pop-up cards with descriptions and images
- Responsive layout for desktop and mobile
- Flask-based backend for serving static files and data
- Terraform deployment script for AWS EC2

---

## 📁 Folder Structure
```
webapp/
├── index.html           # Main HTML layout
├── styles/main.css      # Styling for map and popups
├── scripts/
│   ├── main.js          # Handles popup logic
│   └── map.js           # Loads icon positions and data
├── assets/
│   ├── icons/           # Attraction icons
│   ├── images/          # Attraction photos
│   └── maps/            # Day/Night map backgrounds

data/
└── attractions.json     # List of attractions with mapX/mapY, descriptions, etc.

api/
└── app.py               # Flask backend

deploy/
└── start.sh             # Local/VM startup script

```

---

## 🚀 Run Locally
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Flask
pip install flask

# Start the app
python3 api/app.py
```

Then open your browser to: [http://localhost:5000](http://localhost:5000)

---

## ☁️ Deploy with Terraform
Edit your `main.tf` file and replace:
- `your-key-name` with your actual AWS key pair name

Then run:
```bash
cd infrastructure
terraform init
terraform apply
```

Once deployed, access the app via the public IP of the EC2 instance on port 5000.

---

## 🧠 Future Enhancements
- Dynamic directions and routing system
- Day/Night theme toggle
- Real-time event data integration

---

## 📸 Screenshots
*You can add images here later once the app is running.*

---

Built with ❤️ for the Mystery Island capstone project.
