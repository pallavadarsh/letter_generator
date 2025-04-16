🚀 Project Setup Instructions
🔹 Frontend
⚙️ Requirements

Node.js v18

🛠️ Steps to Run

bash
Copy
Edit
npm install         # Install dependencies
npm run build       # Build the project
npm run preview     # Preview the production build
🔹 Backend
⚙️ Requirements

Anaconda (or Miniconda)

Python 3.10

🛠️ Steps to Run

bash
Copy
Edit
# Create and activate a new conda environment
conda create -n your_env_name python=3.10
conda activate your_env_name

# Install required packages
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload --port 8080
