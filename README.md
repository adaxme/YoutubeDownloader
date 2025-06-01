# YoutubeDownloader

# Deploying FastAPI + yt-dlp Backend to Render

This guide will help you deploy your FastAPI backend to Render.com so it can be accessed by your React and Kotlin frontends.

## 1. Prerequisites
- A GitHub repository with your backend code (already set up)
- A free Render.com account (https://render.com)

## 2. Add a `render.yaml` Blueprint (optional but recommended)
Create a file named `render.yaml` in your project root with the following content:

```
services:
  - type: web
    name: youtube-downloader-backend
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 10000"
    plan: free
    envVars:
      - key: PORT
        value: 10000
```

## 3. Push All Changes to GitHub
Make sure your latest code and `render.yaml` are pushed:

```
git add .
git commit -m "Add Render deployment config"
git push
```

## 4. Create a New Web Service on Render
1. Go to https://dashboard.render.com/
2. Click "New +" > "Web Service"
3. Connect your GitHub repo and select your backend repository
4. For the build and start commands, use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Set the environment to Python 3.11 (or latest)
6. Set the port to 10000 (or leave as default if using the render.yaml)
7. Click "Create Web Service"

## 5. Test Your API
Once deployed, Render will give you a public URL (e.g., `https://youtube-downloader-backend.onrender.com`).
Test your `/download` endpoint with a POST request from your frontend or with curl/Postman.

---

**Note:**
- yt-dlp must be installed via requirements.txt (already done).
- If you need to persist downloads, consider using a cloud storage solution, as Render's disk is ephemeral.

---

For more details, see Render's official docs: https://render.com/docs/deploy-fastapi