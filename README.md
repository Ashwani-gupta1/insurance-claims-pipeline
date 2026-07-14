# 🚀 Insurance Claims Data Engineering + AI Analytics Platform

An end-to-end data engineering project that demonstrates how raw insurance claim data can be ingested, validated, transformed, loaded into a warehouse, analyzed, and queried using an AI-powered natural language assistant.

The project combines traditional data engineering practices with Generative AI capabilities to build an **AI-powered Insurance Claims Analytics Platform**.

---

# 📌 Project Overview

Insurance companies receive thousands of claim records from different sources. This project builds a complete pipeline to process claim data and provide business users with an easy way to analyze claims using natural language.

Example:

**User Question**

```
Show all closed claims
```

The AI Assistant:

1. Understands the user request
2. Generates SQL automatically
3. Executes the query on the warehouse
4. Returns results
5. Provides business-friendly insights

---

# 🏗️ Architecture

```
                 User
                  |
                  |
          Streamlit Chat UI
                  |
                  |
          AI Claims Assistant
                  |
        -----------------------
        |                     |
   SQL Generator          AI Model
        |                  (Llama 3.2)
        |
        |
 Analytics Query Layer
        |
        |
 SQLite Warehouse
        |
        |
 claims_fact Table


Data Pipeline:

CSV Source
    |
    |
Data Ingestion
    |
    |
Validation
    |
    |
Duplicate Detection
    |
    |
Transformation
    |
    |
Warehouse Load
    |
    |
Analytics
```

---

# ✨ Features

## Data Engineering Pipeline

✅ CSV data ingestion
✅ Automatic column standardization
✅ Data validation framework
✅ Duplicate claim detection
✅ Data transformation logic
✅ Audit timestamps
✅ Error/rejection handling
✅ Incremental warehouse loading

## Warehouse Layer

Implemented warehouse concepts:

* Fact table design
* MERGE / UPSERT logic
* Created timestamp tracking
* Updated timestamp tracking

Warehouse Table:

```
claims_fact
```

Schema:

| Column         | Description               |
| -------------- | ------------------------- |
| claim_id       | Unique claim identifier   |
| customer_name  | Customer name             |
| claim_amount   | Claim amount              |
| claim_date     | Date of claim             |
| status         | Claim status              |
| claim_category | Claim classification      |
| priority       | Claim priority            |
| processed_date | Processing date           |
| created_at     | Record creation timestamp |
| updated_at     | Record update timestamp   |

---

# 🤖 AI Assistant

The project includes a Generative AI assistant powered by:

* Ollama
* Llama 3.2
* Natural Language to SQL

Example:

Input:

```
Show all closed claims
```

Generated SQL:

```sql
SELECT *
FROM claims_fact
WHERE status='Closed';
```

Result:

```
claim_id   customer_name     status
1002       Alice Brown       Closed
1005       Michael Lee       Closed
```

---

# 🖥️ Application Interface

The project includes a Streamlit chat application.

Users can ask:

```
Show all high priority claims
```

```
What is the average claim amount?
```

```
Show claims by status
```

The assistant converts questions into SQL and provides results.

---

# 📂 Project Structure

```
insurance-claims-pipeline

│
├── app.py                  # Streamlit AI Chat Application
├── chat.py                 # CLI AI Assistant
├── requirements.txt
├── README.md
│
├── data
│   ├── sample
│   ├── processed
│   ├── rejected
│   ├── reports
│   └── warehouse
│
├── src
│
│   ├── ingestion
│   │   └── reader.py
│   │
│   ├── validation
│   │   ├── validator.py
│   │   ├── duplicate_checker.py
│   │   └── report.py
│   │
│   ├── transform
│   │   └── claim_transformer.py
│   │
│   ├── warehouse
│   │   ├── database.py
│   │   ├── schema.py
│   │   ├── loader.py
│   │   └── query.py
│   │
│   ├── analytics
│   │   └── queries.py
│   │
│   ├── ai
│   │   ├── client.py
│   │   ├── assistant.py
│   │   ├── prompts.py
│   │   └── sql_generator.py
│   │
│   └── utils
│
└── tests
    ├── test_ingestion.py
    └── test_transformation.py
```

---

# 🛠️ Tech Stack

## Programming

* Python
* SQL

## Data Engineering

* Pandas
* SQLite
* ETL Pipeline Design
* Data Validation
* Data Quality Checks

## AI

* Ollama
* Llama 3.2
* Natural Language to SQL
* Generative AI

## Application

* Streamlit

## Testing

* Pytest

## Version Control

* Git
* GitHub

---

# ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/Ashwani-gupta1/insurance-claims-pipeline.git
```

Navigate:

```bash
cd insurance-claims-pipeline
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Data Pipeline

Execute:

```bash
python -m src.main
```

Expected output:

```
Claims pipeline completed successfully

Records processed: 5
Rejected records: 0
Warehouse load completed
```

---

# ▶️ Run AI Chat Assistant

CLI:

```bash
python chat.py
```

Example:

```
Ask> Show all closed claims
```

---

# ▶️ Run Streamlit Application

Start:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

# 🧪 Testing

Run:

```bash
pytest
```

Result:

```
2 passed
```

---

# 🔮 Future Enhancements

Planned improvements:

* Cloud deployment using AWS
* AWS Glue based ETL pipeline
* Redshift warehouse integration
* Dashboard integration
* Automated data quality monitoring
* RAG based document assistant
* AI generated charts
* User authentication

---

# 👨‍💻 Author

**Ashwani Gupta**

Data Engineer | Python | SQL | AWS | AI Analytics

GitHub:

https://github.com/Ashwani-gupta1

---

Give it a star ⭐ on GitHub!
