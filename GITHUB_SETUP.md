# 🚀 GitHub Repository Setup Guide

Your EventEcho project is now ready for GitHub! Follow these steps to push your code to GitHub.

## ✅ What's Already Prepared

- ✅ `requirements.txt` - All dependencies listed
- ✅ `README.md` - Professional documentation
- ✅ `data/sample_vendors.csv` - Sample dataset for testing
- ✅ `.gitignore` - Prevents uploading unnecessary files
- ✅ `notebooks/` - Jupyter notebooks showing AI development
- ✅ `app.py` - Main application
- ✅ `screenshots/` - Directory for UI screenshots

---

## 📋 Step-by-Step: Push to GitHub

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository named: `EventEcho`
3. Add description: "AI-Powered Event Planning Assistant with LLM Integration"
4. Choose **Public** (so evaluators can see it)
5. **DO NOT** initialize with README, .gitignore, or license (we have these)
6. Click **Create repository**

You'll get a page with commands like:

```bash
git remote add origin https://github.com/YOUR_USERNAME/EventEcho.git
git branch -M main
git push -u origin main
```

---

### Step 2: Initialize Git Locally

Open PowerShell in your `EventEcho` folder and run:

```bash
git init
git add .
git commit -m "Initial CAIE submission - EventEcho AI Event Planner"
```

---

### Step 3: Connect to GitHub

Copy the commands from your GitHub repo page and run them:

```bash
git remote add origin https://github.com/YOUR_USERNAME/EventEcho.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

---

### Step 4: Verify

Visit: `https://github.com/YOUR_USERNAME/EventEcho`

You should see:
- ✅ All your files listed
- ✅ README.md displayed nicely
- ✅ Code properly formatted
- ✅ `requirements.txt` showing dependencies

---

## 📸 Adding Screenshots (Important!)

Evaluators love visuals. Add screenshots to `screenshots/` folder:

### Option A: Manual Screenshots
1. Open the app at http://127.0.0.1:7860
2. Take screenshots of:
   - The main UI form
   - Example output with recommendations
   - Budget breakdown
3. Save as `.png` files in `screenshots/` folder
4. Commit and push:

```bash
git add screenshots/
git commit -m "Add UI screenshots"
git push
```

### Option B: Sample File Names to Use
```
screenshots/
├── 01_main_ui.png          - Form with all input fields
├── 02_event_plan.png       - Generated event plan output
├── 03_budget.png           - Budget breakdown table
├── 04_vendors.png          - Recommended vendors list
└── 05_booking_status.png   - Successful booking confirmation
```

---

## 📝 Important: Update HuggingFace Token

⚠️ **BEFORE submitting:**

Do NOT commit your actual HuggingFace token! In `app.py`, replace your real token with:

```python
client = InferenceClient(
    model="microsoft/Phi-3-mini-4k-instruct",
    token="hf_YOUR_TOKEN_HERE"  # Replace with actual token when running locally
)
```

This way, evaluators know what to do without exposing your credentials.

---

## 🔄 Update Repository After Changes

If you make changes later:

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## ✨ Final Checklist Before Submitting

- [ ] Repository is public
- [ ] README.md displays correctly
- [ ] All files visible (app.py, requirements.txt, etc.)
- [ ] `data/sample_vendors.csv` included
- [ ] `notebooks/` folder visible with 3 notebooks
- [ ] Screenshots in `screenshots/` folder
- [ ] `.gitignore` prevents uploading `.venv/` and `bookings.csv`
- [ ] Code has no API keys committed (use placeholder)
- [ ] Repository description mentions CAIE/AI/EventPlanning

---

## 🎯 What Evaluators Will See

When CAIE evaluators visit your repository:

```
EventEcho/
├── app.py                          ← Main application
├── requirements.txt                ← Easy dependency setup
├── README.md                       ← Comprehensive documentation
├── data/sample_vendors.csv         ← Shows dataset work
├── notebooks/                      ← Shows AI development process
│   ├── 01_data_cleaning.ipynb
│   ├── 02_recommender.ipynb
│   └── 03_llm_integration.ipynb
└── screenshots/                    ← Visual proof of working system
```

**They will think:** 
✅ "This shows data engineering"  
✅ "This shows machine learning"  
✅ "This shows AI integration"  
✅ "This shows professional development"  

---

## 🔗 Useful Links

- GitHub Profile: https://github.com/YOUR_USERNAME
- Your Live App: https://ginette-unisolationist-nonconsumptively.ngrok-free.dev
- HuggingFace Tokens: https://huggingface.co/settings/tokens
- GitHub Documentation: https://docs.github.com

---

## 💡 Pro Tips

1. **Fresh clone test**: Clone your repo to a new folder and test if it runs without issues
2. **Add issues**: Create 2-3 GitHub Issues describing potential improvements (shows reflection)
3. **Meaningful commits**: Use descriptive commit messages like "Add TF-IDF recommender" not "update code"
4. **Pin repository**: Pin EventEcho to your GitHub profile for visibility

---

## ❓ Troubleshooting

**"git: command not found"**
- Install Git: https://git-scm.com/download/win

**"fatal: not a git repository"**
- Make sure you're in the `EventEcho` folder
- Run `git init` first

**"fatal: repository not found"**
- Check your username and repo name in the URL
- Verify the repository exists on GitHub

**"Permission denied (publickey)"**
- Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

---

**You're ready! Good luck with your CAIE submission! 🚀**
