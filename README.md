# AlphaLens

## Professional Quantitative Portfolio Analytics Platform

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Next.js](https://img.shields.io/badge/Next.js-14%2B-black.svg)](https://nextjs.org/)

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

- **CSV files** (.csv)
- **Excel files** (.xlsx, .xls)

### Accepted File Formats and Column Headings

The system automatically detects the following column headings (case-insensitive):

#### Date Column (Required)
- `date`
- `trade date`
- `datetime`
- `timestamp`
- `time`

#### Portfolio Column (Required)
- `portfolio`
- `portfolio value`
- `portfolio nav`
- `nav`
- `equity`
- `equity curve`
- `strategy value`
- `strategy equity`
- `account value`
- `total value`

#### Benchmark Column (Optional)
- `benchmark`
- `benchmark value`
- `index`
- `market`
- `spy`
- `nifty50`
- `nifty 50`

### Example Input Formats

**CSV Example:**
```csv
Date,Portfolio Value,Benchmark Value
2020-01-01,1.00,1.00
2020-01-02,1.01,1.005
2020-01-03,1.02,1.01
```

**Excel Example:**
| Date | Portfolio Value | Benchmark Value |
|------|-----------------|-----------------|
| 2020-01-01 | 1.00 | 1.00 |
| 2020-01-02 | 1.01 | 1.005 |
| 2020-01-03 | 1.02 | 1.01 |

### Data Detection Features

The system automatically detects:
- Date column format and encoding
- Portfolio value/NAV column
- Benchmark column (if present)
- Dataset structure
- Sampling frequency (daily, weekly, monthly, etc.)

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

## Prerequisites

- Python 3.8 or higher
- Node.js 18 or higher
- npm or yarn package manager

## Backend Setup

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs on:

```
http://localhost:8000
```

API Documentation available at: `http://localhost:8000/docs`

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

1. Upload portfolio CSV/XLSX file
2. Upload optional factor dataset
3. Generate analysis
4. Explore:
   - Performance metrics
   - Risk statistics
   - Benchmark comparison
   - Factor exposure
   - Interactive charts

## Quick Start

1. **Prepare your data**: Ensure your portfolio file contains at minimum a Date column and a Portfolio Value column
2. **Start the backend**: `cd backend && uvicorn main:app --reload`
3. **Start the frontend**: `cd frontend && npm run dev`
4. **Open your browser**: Navigate to `http://localhost:3000`
5. **Upload and analyze**: Use the upload buttons to load your portfolio data and generate insights

## Data Format Requirements

- **File size**: Recommended maximum 10MB for optimal performance
- **Date format**: YYYY-MM-DD (ISO 8601) preferred, but flexible parsing supported
- **Frequency**: Daily, weekly, or monthly data
- **Missing values**: System handles missing benchmark data gracefully
- **Encoding**: UTF-8, UTF-8-sig, CP1252, and Latin1 encodings supported

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

# Troubleshooting

## Common Issues

**Backend won't start:**
- Ensure Python 3.8+ is installed
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify port 8000 is not in use

**Frontend won't start:**
- Ensure Node.js 18+ is installed
- Check that all dependencies are installed: `npm install`
- Verify port 3000 is not in use

**File upload fails:**
- Check file format (CSV or Excel only)
- Verify required columns (Date, Portfolio Value)
- Ensure file is not corrupted
- Check file size (recommended < 10MB)

**Analysis doesn't complete:**
- Verify backend is running
- Check browser console for errors
- Ensure sufficient data points (minimum 30 records recommended)

---

# Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Development Guidelines

- Follow existing code style and conventions
- Add comments for complex logic
- Test changes thoroughly before submitting
- Update documentation as needed

---

# Creator

## Sai Ashwin Nagulapati

B.Tech Electronics and Communication Engineering

IIT Jodhpur

---

# License

MIT License