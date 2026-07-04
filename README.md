# 🔍 Autonomous Research Agent

## Overview

The Autonomous Research Agent is an AI-powered application that autonomously researches a user-provided topic using Google Gemini and web search.

The agent:
- Understands the research topic
- Generates an optimized search query
- Searches multiple web sources
- Removes duplicate information
- Performs LLM-based reasoning
- Produces a structured research report
- Stores search history
- Exports the report as a PDF

---

## Features

- AI-generated optimized search queries
- Autonomous web search using DDGS
- Multi-source information collection
- Duplicate information removal using Gemini
- Structured research report generation
- Key Points
- Important Findings
- References
- Actionable Insights
- Search History (Memory)
- PDF Report Export
- Streamlit Web Interface

---

## Technologies Used

- Python 3.11+
- Streamlit
- Google Gemini API
- DDGS (DuckDuckGo Search)
- ReportLab
- python-dotenv

---

## Project Structure

```
AutonomousResearchAgent/
│
├── app.py
├── agent.py
├── llm.py
├── search.py
├── summarizer.py
├── export.py
├── memory.py
├── requirements.txt
├── README.md
├── .env.example
│
├── memory/
│   └── history.json
│
└── reports/
```

---

## Prerequisites

- Python 3.11 or later
- Google Gemini API Key

---

## Installation

### 1. Clone or Extract the Project

Download the ZIP or clone the repository.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` File

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. User enters a research topic.
2. Gemini generates an optimized search query.
3. DDGS searches the web.
4. Relevant information is collected.
5. Gemini analyzes and summarizes the results.
6. A structured research report is generated.
7. Search history is saved.
8. A PDF report can be downloaded.

---

## Sample Input

```
Large Language Models
```

---

## Sample Output

The generated report includes:

- Research Report
- Key Points
- Important Findings
- References
- Actionable Insights

---

## Future Improvements

- Multi-search engine support
- Vector database memory
- Markdown export
- Source quality ranking
- Advanced PDF formatting

---

## Author

Harshavardhan Neerati

---

## License

This project was developed as part of the Xiarch AI Automation Engineer Assessment.