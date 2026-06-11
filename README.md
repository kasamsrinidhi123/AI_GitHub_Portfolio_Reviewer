# 🚀 AI GitHub Portfolio Reviewer

## 📌 Abstract

AI GitHub Portfolio Reviewer is an intelligent web application developed using Python and Streamlit that analyzes GitHub portfolios and provides recruiter-style feedback. The system integrates GitHub APIs, GitHub OAuth authentication, analytics modules, and Google Gemini AI to evaluate repository quality, programming languages, documentation coverage, and overall portfolio strength.

The application helps students, developers, and job seekers understand the quality of their GitHub profiles by generating portfolio scores, grades, analytics dashboards, and AI-powered recommendations. It also supports secure access to a user's private repositories through GitHub OAuth while ensuring that other users' private repositories remain inaccessible.

---

## 🎯 Problem Statement

Recruiters often evaluate candidates through their GitHub profiles. However, manually reviewing repositories, technologies used, documentation quality, and project diversity can be time-consuming.

This project automates the portfolio review process by:
- Fetching GitHub profile data
- Analyzing repositories
- Evaluating portfolio quality
- Generating scores and grades
- Providing AI-generated feedback

---

## ✨ Features

### 👤 GitHub Profile Analysis
- Fetch user profile information
- Display followers and repository statistics
- Analyze public repositories

### 🔒 Secure GitHub OAuth Login
- Authenticate users with GitHub
- Access authenticated user's private repositories
- Protect private repository access

### 📊 Portfolio Analytics
- Repository count analysis
- Language distribution analysis
- Documentation tracking
- Portfolio scoring system
- Grade generation

### 📈 Interactive Dashboard
- Repository statistics
- Language charts
- Portfolio metrics
- Analytics cards

### 🤖 AI-Powered Portfolio Review
- Powered by Google Gemini AI
- Answers user portfolio questions
- Generates recruiter-style feedback
- Suggests portfolio improvements

### 📁 Repository Analysis
- Analyze repository structure
- Identify technologies used
- Review documentation quality
- Evaluate project diversity

---

## 🏗️ System Architecture

```text
                ┌─────────────────┐
                │      User       │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Streamlit UI   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ GitHub API/OAuth│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Data Processing │
                │  & Analytics    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Portfolio Score │
                │   Calculation   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   Gemini AI     │
                │ Prompt + Review │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Dashboard & AI  │
                │    Feedback     │
                └─────────────────┘
```

---

## 🛠️ Technologies Used

### Frontend
- Streamlit
- HTML
- CSS

### Backend
- Python

### APIs
- GitHub REST API
- GitHub OAuth API
- Google Gemini API

### Libraries
- Requests
- Pandas
- Plotly
- Streamlit
- Google Generative AI

---

## 📂 Project Structure

```text
AI_GitHub_Portfolio_Reviewer/
│
├── app.py
├── github_api.py
├── analyzer.py
├── scorer.py
├── ai_review.py
├── requirements.txt
├── .gitignore
│
└── components/
    ├── sidebar.py
    ├── profile_card.py
    ├── dashboard.py
    ├── dashboard_cards.py
    ├── projects.py
    ├── repository_analyzer.py
    ├── language_chart.py
    ├── star_chart.py
    └── feedback.py
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/AI_GitHub_Portfolio_Reviewer.git

cd AI_GitHub_Portfolio_Reviewer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env File

```env
GITHUB_CLIENT_ID=YOUR_CLIENT_ID

GITHUB_CLIENT_SECRET=YOUR_CLIENT_SECRET

GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

### Step 1
User enters a GitHub username or logs in through GitHub OAuth.

### Step 2
The system fetches profile information and repositories using GitHub APIs.

### Step 3
Repository data is analyzed to determine:
- Repository count
- Languages used
- Documentation availability
- Portfolio quality

### Step 4
A scoring engine calculates:
- Portfolio Score
- Portfolio Grade
- Portfolio Level

### Step 5
The processed information is sent to Gemini AI.

### Step 6
Gemini generates:
- Portfolio insights
- Recommendations
- Recruiter-style feedback

### Step 7
Results are displayed through an interactive dashboard.

---

## 📊 Portfolio Metrics

The system evaluates:

### Repository Metrics
- Total repositories
- Public repositories
- Private repositories

### Documentation Metrics
- README availability
- Documentation coverage

### Technical Metrics
- Programming languages used
- Technology diversity

### Overall Metrics
- Portfolio Score
- Portfolio Grade
- Portfolio Level

---

## 🔒 Security Features

- OAuth-based authentication
- Environment variable protection
- Secure API access
- Private repository isolation
- No access to other users' private repositories

### Private Repository Protection

The system only accesses private repositories belonging to the authenticated user.

Example:

If Srinidhi logs in:
- Srinidhi's private repositories → Accessible
- Other users' private repositories → Not Accessible

This ensures complete privacy and security.

---

## 🚧 Limitations

- Depends on GitHub API availability
- Depends on Gemini API quota
- Documentation analysis is limited if README files are unavailable
- Repository quality assessment is based on available metadata

---

## 🔮 Future Enhancements

- README content analysis
- Commit activity tracking
- Contribution graph analytics
- Resume generation
- Project recommendations
- Deployment support
- Advanced repository quality analysis
- Team collaboration insights

---

## 📈 Sample Use Cases

### Students
Analyze GitHub portfolios before placements and internships.

### Developers
Improve project quality and documentation.

### Recruiters
Quickly assess candidate GitHub profiles.

### Open Source Contributors
Track portfolio growth and repository quality.

---

## 📋 Final Reflection

### Weakest Part
The AI feedback quality depends on the information available from GitHub APIs and repository metadata.

### Single Failure Mode
If GitHub APIs become unavailable, the application cannot fetch repository data and portfolio analysis stops.

### Value Without AI
Even without Gemini AI, the dashboard, analytics, repository scoring, and portfolio evaluation system remain highly useful for understanding GitHub portfolio quality.

---

## 👨‍💻 Author

### Kasam Srinidhi

