Welcome to my **Backend Wizards Stage 0** project! 🎯  
This project demonstrates how to build a **simple FastAPI endpoint** that returns My profile information along with a **dynamic cat fact** fetched from a public API.


## 🧩 Project Overview

The goal of this project is to:

- Create a GET endpoint `/me`
- Return profile information in JSON format
- Dynamically fetch a random cat fact from [Cat Facts API](https://catfact.ninja/fact)
- Include the current UTC timestamp
- Follow best practices for backend development
- Deploy the app to **Railway** for public access

This project helped me learn:

- How to structure a FastAPI project
- How to integrate external APIs (`requests`)
- How to format JSON responses
- How to manage virtual environments (`venv`)
- How to initialize Git, commit changes, and push to GitHub
- How to deploy a FastAPI app on Railway
- Handling dynamic environment variables (PORT for deployment)
- Safe Git workflows for collaboration

---

## 🗂 Folder Structure

```text
backend-wizard/
├── main.py          # Main FastAPI app with /me endpoint
├── requirements.txt # List of Python dependencies
├── Procfile         # Instructions for Railway to run the app
├── .gitignore       # Files/folders Git should ignore
└── venv/            # Virtual environment (not tracked by Git)



⚡ Features

1. Dynamic /me Endpoint

Returns a JSON object with:

status: Always "success"

user: email, name, backend stack

timestamp: Current UTC time (ISO 8601)

fact: Random cat fact fetched dynamically




2. Error Handling

If Cat Facts API fails, a fallback message is returned

Network timeouts are handled safely



3. Deployment-Ready

Configured to run on Railway

Supports dynamic PORT environment variable

Includes Procfile and requirements.txt





🚀 Getting Started (Local Setup)

Prerequisites



1. Clone the Repository

2. Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt
pip install uvicorn

4. Run Locally

uvicorn main:app --reload

Open in browser:
http://127.0.0.1:8000/me



🌐 Deployment (Railway)

1. Sign up/log in to Railway


2. Click New Project → Deploy from GitHub


3. Select this repository


4. Railway will automatically:

Install dependencies from requirements.txt


5. Once deployed, access the /me endpoint via the Railway URL



Note: The app uses PORT from Railway to run the server dynamically:

port = int(os.environ.get("PORT", 8000))
uvicorn.run("main:app", host="0.0.0.0", port=port)



💡 Lessons Learned

Proper project structure matters (keeping code outside venv)

Git workflow is important:

git add, git commit, git push


FastAPI is excellent for building APIs quickly

Using requests for third-party APIs

Deploying to Railway is straightforward and beginner-friendly

Importance of .gitignore to prevent uploading unnecessary files

Handling dynamic environment variables for cloud deployment




🖇️ Links

Cat Facts API: https://catfact.ninja/fact

Railway Deployment: Your live URL after deployment

GitHub Repo: https://github.com/Elice99/Stage0-Backend-wizard


⚙️ Contact

Author: Elisha Bassey
Email: basseyelisha99@gmail.com
Stack: Python / FastAPI


This README is **beginner-friendly, comprehensive, and deployment-ready**.  
It explains:

- What the project does  
- How to set it up locally  
- How to deploy it to Railway  
- Lessons learned and future improvements  

