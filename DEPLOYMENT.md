# 🚀 DEPLOYMENT GUIDE

## Streamlit Cloud Deployment (Recommended)

### Prerequisites

- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)
- Repository pushed to GitHub

### Step-by-Step Deployment

#### 1. Prepare Your Repository

Ensure these files exist:

```
✅ app.py
✅ requirements.txt
✅ .streamlit/config.toml (optional)
✅ packages.txt (optional, for system dependencies)
```

#### 2. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

#### 3. Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io
2. Click "New app"
3. Select your repository
4. Choose branch: `main`
5. Main file path: `app.py`
6. Click "Deploy"

#### 4. Wait for Deployment

The app will be deployed at:

```
https://YOUR_USERNAME-YOUR_REPO-BRANCH-HASH.streamlit.app
```

---

## 🔧 Troubleshooting

### Error: "installer returned a non-zero exit code"

**Causes:**

1. Incompatible package versions
2. Missing system dependencies
3. Python version mismatch

**Solutions:**

#### Solution 1: Use Simple Requirements

Replace `requirements.txt` content with:

```txt
streamlit
pandas
numpy
matplotlib
seaborn
```

#### Solution 2: Fix Python Version

Update `runtime.txt` to:

```txt
python-3.11
```

Or remove `runtime.txt` to use default Python version.

#### Solution 3: Add System Dependencies

Create `packages.txt`:

```txt
libgomp1
```

#### Solution 4: Check Dependencies Locally

```bash
pip install -r requirements.txt
```

If it fails locally, fix the requirements first.

---

### Error: "Module not found"

**Solution:**
Ensure all imports are in `requirements.txt`:

```bash
# Test imports
python -c "import streamlit; import pandas; import numpy; import matplotlib; import seaborn"
```

---

### Error: "Port already in use"

**Solution (Local):**

```bash
streamlit run app.py --server.port 8502
```

Or kill existing process:

```bash
# Find process
lsof -ti:8501

# Kill process
kill -9 $(lsof -ti:8501)
```

---

### Error: CORS Warning

**Solution:**
Remove `enableCORS = false` from `.streamlit/config.toml`:

```toml
[server]
headless = true
port = 8501
```

---

### Error: File not found (data/bank_transactions.csv)

**Solution:**
Ensure `data/` folder and CSV are committed:

```bash
git add data/bank_transactions.csv
git commit -m "Add data file"
git push
```

Or regenerate data:

```bash
python generate_data.py
```

---

## 🐳 Docker Deployment

### Build and Run

```bash
# Build image
docker build -t bank-dashboard .

# Run container
docker run -p 8501:8501 bank-dashboard
```

### Docker Compose

```bash
docker-compose up
```

Access at: http://localhost:8501

---

## 🌐 Heroku Deployment

### Prerequisites

- Heroku account
- Heroku CLI installed

### Deploy Steps

```bash
# Login
heroku login

# Create app
heroku create your-app-name

# Push code
git push heroku main

# Open app
heroku open
```

### Required Files

- `Procfile`: Already created
- `requirements.txt`: Already created
- `runtime.txt`: Optional (Python version)

---

## 📱 Local Testing Before Deploy

### Test Checklist

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test imports
python -c "import app"

# 3. Run app
streamlit run app.py

# 4. Check all pages
# - Home page loads
# - Dashboard works
# - Analytics works
# - Transactions works

# 5. Test filters
# - Date range
# - Categories
# - Transaction types
# - Amount range
# - Search

# 6. Test export
# - Download CSV works
```

---

## 🔍 Common Issues & Solutions

### Issue 1: Slow Loading

**Cause:** Large data file or inefficient code

**Solution:**

- Reduce data size
- Add caching with `@st.cache_data`
- Optimize pandas operations

### Issue 2: Memory Error

**Cause:** Too much data in memory

**Solution:**

- Filter data before processing
- Use data chunking
- Reduce chart size

### Issue 3: Charts Not Displaying

**Cause:** Matplotlib backend issues

**Solution:**
Add to app.py:

```python
import matplotlib
matplotlib.use('Agg')
```

### Issue 4: Sidebar Not Working

**Cause:** Navigation file naming

**Solution:**
Ensure pages are named: `1_📊_Name.py`

---

## ✅ Pre-Deployment Checklist

Before deploying, verify:

- [ ] All files committed to Git
- [ ] `requirements.txt` has correct packages
- [ ] `data/` folder included (if needed)
- [ ] `.streamlit/config.toml` valid
- [ ] No hardcoded paths
- [ ] App runs locally without errors
- [ ] All imports work
- [ ] No sensitive data in code
- [ ] README.md updated
- [ ] Git repository is public (for Streamlit Cloud free tier)

---

## 🎯 Streamlit Cloud Specific

### File Structure Required

```
your-repo/
├── app.py              ← Main file (REQUIRED)
├── requirements.txt    ← Dependencies (REQUIRED)
├── packages.txt        ← System deps (optional)
├── .streamlit/         ← Config (optional)
│   └── config.toml
├── data/               ← Data files
├── components/         ← Your modules
└── pages/              ← Multi-page (optional)
```

### Supported Python Versions

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11 (recommended)

### Free Tier Limits

- 1 GB RAM
- 1 CPU core
- Sleeps after 7 days of inactivity
- Unlimited public apps

---

## 🔄 Update Deployed App

After making changes:

```bash
# Commit changes
git add .
git commit -m "Update app"

# Push to GitHub
git push origin main
```

Streamlit Cloud will auto-redeploy (takes 1-2 minutes).

---

## 📊 Monitor Your App

### Streamlit Cloud Dashboard

- View logs
- Check resource usage
- Monitor errors
- See app analytics

### Access Logs

Click "Manage app" → "Logs" in Streamlit Cloud

---

## 🆘 Getting Help

### Streamlit Community

- Forum: https://discuss.streamlit.io
- Documentation: https://docs.streamlit.io
- GitHub: https://github.com/streamlit/streamlit

### This App

- Check README.md
- Read QUICKSTART.md
- Review DEVELOPER.md

---

## 🎉 Success Checklist

After deployment, verify:

- [ ] App loads without errors
- [ ] All pages accessible
- [ ] Filters work correctly
- [ ] Charts display properly
- [ ] Data loads successfully
- [ ] Export CSV works
- [ ] Mobile responsive
- [ ] Performance acceptable

---

## 📝 Example Deployment Configs

### Minimal requirements.txt

```txt
streamlit
pandas
numpy
matplotlib
seaborn
```

### With Versions (More Control)

```txt
streamlit>=1.28.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
```

### Exact Versions (Most Stable)

```txt
streamlit==1.31.0
pandas==2.1.4
numpy==1.26.2
matplotlib==3.8.2
seaborn==0.13.0
```

---

## 🚀 Quick Deploy Commands

```bash
# Fresh deployment
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main

# Then deploy on Streamlit Cloud web interface
```

---

**Need more help? Check the official Streamlit deployment docs:**
https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app

**Good luck with your deployment! 🎉**
