# Intelligent Candidate Discovery & Ranking

## Overview

This project is an AI-powered candidate ranking system developed for the Redrob Intelligent Candidate Discovery & Ranking Challenge.

The system processes candidate profiles, extracts structured features, calculates a weighted ranking score, generates recruiter-friendly reasoning, and exports the Top 100 candidates into a submission CSV.

---

## Features

- Load 100,000 candidate profiles
- Feature extraction
- Experience scoring
- Skill matching
- Career history analysis
- Behavioral signal analysis
- Recruiter signal analysis
- Candidate ranking
- Explainable AI reasoning
- CSV submission generation

---

## Project Structure

```
Intelligent_Candidate_Discovery_Ranking/

│
├── data/
├── output/
├── src/
│   ├── parser.py
│   ├── feature_engineering.py
│   ├── scoring.py
│   ├── ranker.py
│   ├── reasoning.py
│   ├── exporter.py
│   └── utils.py
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```
---

## Output

The system generates

```
output/submission.csv
```

Columns

- rank
- candidate_id
- score
- reasoning

---

## Ranking Factors

- Years of experience
- Required skills
- Bonus skills
- Skill proficiency
- Skill duration
- Endorsements
- Career history
- Product company experience
- Recruiter response rate
- Interview completion rate
- Profile completeness
- Notice period
- Open-to-work status
- GitHub activity
- Search appearance
- Verification status


## Technologies

Python
Pandas
NumPy
tqdm

## Author

Keerthi Rishitha