# 🚀 Streamlit Cloud Deployment Guide

This guide will help you deploy the Myntra Review Scraper to Streamlit Community Cloud.

## 📋 Prerequisites

1. **GitHub Account**: Create a free account at https://github.com
2. **Streamlit Account**: Create a free account at https://streamlit.io/cloud
3. **Git installed**: Install Git on your local machine

## 🔄 Step-by-Step Deployment

### 1. Initialize Git Repository
```bash
cd "c:\Users\VAISHNAVI\Desktop\myntra 2"
git init
git add .
git commit -m "Initial commit - Myntra Review Scraper"
```

### 2. Create GitHub Repository
1. Go to https://github.com
2. Click "New repository"
3. Name: `myntra-review-scraper`
4. Description: "Myntra product review scraper with web interface"
5. Make it **Public** (required for Streamlit Cloud free tier)
6. Click "Create repository"

### 3. Push to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/myntra-review-scraper.git
git branch -M main
git push -u origin main
```

### 4. Deploy to Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Click "New app"
3. **Repository**: Select `myntra-review-scraper`
4. **Branch**: `main`
5. **Main file path**: `app.py`
6. Click "Deploy!"

## 🔧 Configure Database Connection

### Option A: Use Streamlit Secrets (Recommended)
1. In your Streamlit Cloud dashboard, go to your app
2. Click "⋮" → "Settings" → "Secrets"
3. Add these secrets:

```toml
[mysql]
host = "your-mysql-host"
user = "your-mysql-user"
password = "your-mysql-password"
database = "myntra_reviews"
```

### Option B: Use Cloud Database Services
- **PlanetScale**: Free MySQL hosting
- **Supabase**: Free PostgreSQL (can work with MySQL connector)
- **Railway**: Free MySQL hosting
- **AWS RDS**: Paid but reliable

### Update Code for Streamlit Secrets
Replace the environment variable loading in `app.py`:

```python
# Replace this:
from dotenv import load_dotenv
load_dotenv()

# With this:
import streamlit as st
```

And update the MySQL connection in `src/cloud_io/__init__.py`:

```python
# Add this at the top of the __init__ method:
try:
    import streamlit as st
    host = st.secrets["mysql"]["host"]
    user = st.secrets["mysql"]["user"]
    password = st.secrets["mysql"]["password"]
    database = st.secrets["mysql"]["database"]
except:
    host = os.getenv(MYSQL_HOST_KEY, "localhost")
    user = os.getenv(MYSQL_USER_KEY, "root")
    password = os.getenv(MYSQL_PASSWORD_KEY, "")
    database = os.getenv(MYSQL_DATABASE_KEY, MYSQL_DATABASE_NAME)
```

## 🌐 Free Database Options

### PlanetScale (Recommended)
1. Sign up at https://planetscale.com
2. Create new database
3. Get connection details
4. Add to Streamlit secrets

### Supabase
1. Sign up at https://supabase.com
2. Create new project
3. Get connection details
4. Add to Streamlit secrets

## 🚀 Deployment Benefits

- **Free hosting** for public repositories
- **Automatic SSL/HTTPS**
- **Custom subdomain** (your-app.streamlit.app)
- **Automatic deployments** on git push
- **Built-in monitoring**
- **Easy secrets management**

## 🔍 Troubleshooting

### Common Issues:
1. **Build fails**: Check requirements.txt for correct versions
2. **Database connection fails**: Verify secrets are correctly formatted
3. **Chrome/ChromeDriver issues**: Streamlit Cloud handles this automatically
4. **App not loading**: Check the deployment logs in Streamlit Cloud

### Debug Commands:
```bash
# Check git status
git status

# View deployment logs in Streamlit Cloud dashboard
# Go to your app → "Logs" tab
```

## 📱 Access Your App

Once deployed, your app will be available at:
`https://your-app-name.streamlit.app`

## 🔄 Automatic Updates

Every time you push changes to GitHub, Streamlit Cloud will automatically redeploy your app!

## 💡 Pro Tips

1. **Use environment-specific configurations** for local vs production
2. **Monitor app performance** in Streamlit Cloud dashboard
3. **Set up custom domain** for professional appearance
4. **Add error handling** for production robustness
5. **Use Streamlit's built-in metrics** at `/_stcore/metrics`

## 🆘 Support

- **Streamlit Docs**: https://docs.streamlit.io
- **Streamlit Community**: https://discuss.streamlit.io
- **GitHub Issues**: For code-specific problems
