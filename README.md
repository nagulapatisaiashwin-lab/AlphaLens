# AlphaLens

## Professional Quantitative Portfolio Analytics Platform



AlphaLens is a quantitative portfolio analytics platform that converts portfolio data into an institutional-style research dashboard.

It is designed to analyze investment strategies, compare against benchmarks, evaluate risk, visualize performance, and generate professional portfolio tearsheets.

Built with a research-first approach combining quantitative finance, data engineering, and modern web technologies.

---

# Overview

Traditional portfolio analysis often requires manually building spreadsheets, calculating metrics, and creating charts.

AlphaLens automates this workflow:

```
Portfolio Data
      |
      ↓
Data Validation
      |
      ↓
Schema Detection
      |
      ↓
Normalization Pipeline
      |
      ↓
Analytics Engine
      |
      ↓
Interactive Research Dashboard
```

---

# Key Features

## Universal Portfolio Data Ingestion

AlphaLens accepts:

- CSV files
- Excel files (.xlsx, .xls)

Automatically detects:

- Date column
- Portfolio value/NAV column
- Benchmark column
- Dataset structure
- Sampling frequency

Example input:

```
Date | Portfolio Value | Benchmark Value
----------------------------------------
2020-01-01 | 1.00 | 1.00
2020-01-02 | 1.01 | 1.005
```

No manual code modification required.

---

# Performance Analytics

AlphaLens calculates:

- Total Return
- Annualized Return
- CAGR
- Equity Curve
- Benchmark Comparison
- Rolling Performance Metrics



---

# Risk Analytics

Includes professional risk measurements:

- Volatility
- Sharpe Ratio
- Sortino Ratio
- Maximum Drawdown
- Return Distribution
- Rolling Risk Metrics





---

# Benchmark Analysis

Compare portfolio performance against:

- Market indices
- Custom benchmarks
- Reference portfolios

Features:

- Relative performance comparison
- Excess return analysis
- Benchmark visualization

---

# Factor Analytics

Supports factor-based portfolio analysis.

Currently includes:

- CAPM Analysis
- Alpha
- Market Beta
- R²
- Statistical significance

Example:



---

# Interactive Visualization

Built with Plotly for interactive research workflows.

Includes:

## Equity Curve

Portfolio growth visualization.

## Drawdown Chart

Historical loss periods and recovery analysis.

## Monthly Return Heatmap

Calendar-style performance visualization.

## Rolling Metrics

Time-varying:

- Sharpe Ratio
- Volatility
- Returns

## Return Distribution

Statistical view of portfolio behaviour.

---

# Dashboard Preview


The dashboard provides:

- KPI cards
- Interactive charts
- Metric tables
- Mathematical definitions
- Research-style presentation

---

# Architecture

```
AlphaLens

├── Backend
│
│   ├── FastAPI API
│   │
│   ├── Data Ingestion
│   │   ├── Loader
│   │   ├── Validator
│   │   ├── Schema Detector
│   │   ├── Normalizer
│   │   └── Frequency Detection
│   │
│   ├── Analytics Engine
│   │   ├── Performance Metrics
│   │   ├── Risk Metrics
│   │   ├── Benchmark Analysis
│   │   └── Factor Analysis
│   │
│   ├── Visualization Engine
│   │
│   └── Report Generation
│
└── Frontend

    ├── Next.js
    ├── React
    ├── TypeScript
    ├── Tailwind CSS
    ├── Plotly Charts
    └── React Query
```

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pandas
- NumPy
- Plotly

## Frontend

- Next.js
- TypeScript
- React
- Tailwind CSS
- Zustand
- React Query

---

# Project Structure

```
AlphaLens/

├── backend/

│   ├── app/

│   │   ├── analytics/
│   │   ├── api/
│   │   ├── io/
│   │   ├── preprocessing/
│   │   ├── reporting/
│   │   └── visualization/

│   └── examples/


└── frontend/

    ├── app/

    ├── components/

    ├── hooks/

    ├── services/

    └── stores/
```

---

# Running AlphaLens

## Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:3000
```

---

# Example Workflow

1. Upload portfolio CSV/XLSX

2. Upload optional factor dataset

3. Generate analysis

4. Explore:

- Performance metrics
- Risk statistics
- Benchmark comparison
- Factor exposure
- Interactive charts

---

# Future Roadmap

## Advanced Analytics

- Fama-French 3 Factor Model
- Carhart Momentum Factor
- Risk attribution
- Portfolio optimization

## Research Features

- Strategy comparison
- Multi-portfolio analysis
- Automated research reports

## Deployment

- Cloud deployment
- User accounts
- Persistent reports

---

# Creator

## Sai Ashwin Nagulapati

B.Tech Electronics and Communication Engineering

IIT Jodhpur

---

# License

MIT License