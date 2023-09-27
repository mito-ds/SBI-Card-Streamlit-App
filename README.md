# Data Verification Streamlit App
Centralize and automate your organizations's data reconciliation. Save your organization hundreds of hours of manual work each quarter. 

This Streamlit app is created using Mito. [Mito](https://www.trymito.io) is the spreadsheet desgined to help non-technical write Python code. Every edit you make to the Mito spreadsheet is automatically converted to production-ready Python code. Use spreadsheet formulas, pivot tables, and all of your faveorite Excel functionality.  

In this app, users will use Mito to:
1. [Import](https://docs.trymito.io/how-to/importing-data-to-mito) files 
2. Clean the file by [converting column dtypes](https://docs.trymito.io/how-to/type-changes), [filtering](https://docs.trymito.io/how-to/filter-data/filter-by-condition) columns, [using spreadsheet formulas](https://docs.trymito.io/how-to/interacting-with-your-data/mito-spreadsheet-formulas), etc. 
3. Download the file as a Pickle file

### Run Locally 
1. Create a virtual environment:
```
python3 -m venv venv
```

2. Start the virtual environment:
```
source venv/bin/activate
```

3. Install the required python packages:
```
pip install -r requirements.txt
```

4. Start the streamlit app
```
streamlit run app.py
```