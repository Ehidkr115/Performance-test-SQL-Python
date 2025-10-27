# Performance-test-SQL-Python
# 🏋️‍♂️ RIWI Sport Data Analysis

This project analyzes sales and customer behavior data from **RIWI Sport**, a Colombian company specializing in sports equipment.  
The goal is to extract insights and identify business opportunities through SQL queries, data cleaning, and visual analytics.

---

## 📦 Dependencies

To run this project, install the following dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

1. Restore the PostgreSQL database using the provided SQL dump file:

```bash
psql -U postgres -d riwisport -f riwisport.sql
```

2. Create a `.env` file in the project root to store database credentials:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=riwisport
```

---

## 📊 Running the Notebook

1. Open the Jupyter Notebook or VS Code notebook environment.  
2. Execute the notebook cells in order — they include:
   - Database connection and data extraction.
   - Data cleaning and preparation.
   - Statistical analysis (mean, median, mode, variance, etc.).
   - Visualization with Matplotlib and Seaborn.
   - Business insights and recommendations.

---

## 📈 Generating the PDF Report

After completing the analysis, you can generate the final PDF report by running:

```bash
python informe_Riwi_sport.py
```

The report will be saved as:

```
Informe_RiwiSport_Ehider_Villanueva.pdf
```

and will include:
- Data structure overview
- Key performance metrics (KPIs)
- Visual summaries
- Strategic recommendations

---

## 👤 Author

**Ehider Villanueva Pérez**  
Marketing & Data Analysis Enthusiast  

---

## 🧠 Notes

- Ensure your PostgreSQL service is running before executing the notebook.  
- Use environment variables for security (never hard-code passwords).  
- All code and documentation are written in English for clarity and compatibility.
