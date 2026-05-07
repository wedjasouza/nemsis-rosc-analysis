# NEMSIS ROSC Analysis

An end-to-end healthcare data science project analyzing out-of-hospital cardiac arrest outcomes using the 2023 NEMSIS Cardiac Arrest Dataset.

This project explores factors associated with return of spontaneous circulation (ROSC) through exploratory data analysis, feature engineering, and multivariable logistic regression modeling using real-world EMS data.

---

## Project Goals

The primary goals of this project were to:

- preprocess and integrate large-scale relational EMS datasets,
- engineer clinically meaningful patient-level features,
- explore associations between cardiac arrest variables and ROSC,
- and identify independent predictors of ROSC using logistic regression.

---

## Dataset

Data was obtained from the public NEMSIS 2023 Cardiac Arrest research dataset.

The project utilized six relational tables containing:
- cardiac arrest incident data,
- medication administration records,
- EMS procedures,
- resuscitation interventions,
- symptom information,
- and ROSC outcome variables.

Raw source files were provided in SAS7BDAT format and imported using `pyreadstat`.

---

## Project Structure

```text
nemsis-rosc-analysis/
│
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_analysis.ipynb
│
├── src/
│   ├── processing.py
│   └── mappings.py
│
├── figures/
├── outputs/
├── references/
├── requirements.txt
└── README.md
```

## Workflow

1. Exploratory Data Processing

[01_exploration.ipynb](notebooks/01_exploration.ipynb)

- raw dataset inspection
- placeholder value handling
- categorical decoding
- feature engineering
- event-level aggregation by PCR key
- multi-table dataset integration
- analytical dataset construction

2. Statistical Analysis and Modeling

[02_analysis.ipynb](notebooks/02_analysis.ipynb)

- exploratory data analysis
- ROSC outcome visualization
- intervention analysis
- logistic regression modeling
- adjusted odds ratio analysis
- interpretation of key findings

## Key Features Engineered

Examples of engineered variables include:

- simplified cardiac rhythm categories
- CPR and defibrillation indicators
- medication counts
- unique medication counts
- intervention intensity
- grouped symptom categories
- patient-level procedure summaries

## Key Findings

Key findings from the analysis included:

- shockable cardiac rhythms were the strongest predictors of ROSC,
- defibrillation demonstrated a strong positive association with ROSC,
- CPR showed a moderate positive association,
- higher epinephrine counts were associated with prolonged or more severe resuscitation efforts,
- and early intervention prior to or immediately following EMS arrival appeared clinically important.

## Technologies Used

- Python
- pandas
- NumPy
- seaborn
- matplotlib
- scikit-learn
- pyreadstat
- Jupyter Notebook

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook and run:

[01_exploration.ipynb](notebooks/01_exploration.ipynb)
[02_analysis.ipynb](notebooks/02_analysis.ipynb)

## Data Access

The project uses the public 2023 NEMSIS Cardiac Arrest research dataset.

Dataset access:
https://nemsis.org/datasets/

Raw SAS7BDAT files are not included in this repository due to dataset size considerations. After downloading the dataset, place the required source folder inside a local `data/` directory before running the notebooks.

## Notes

Certain NEMSIS variables used coded placeholder values rather than standard null values and required preprocessing prior to analysis.

## Future Improvements

Potential future directions include:

- survival-to-discharge modeling
- neurologic outcome analysis
- more granular rhythm classification
- advanced predictive modeling approaches
- temporal EMS response analysis

## Author

Wedja Souza  
GitHub: https://github.com/wedjasouza
LinkedIn: https://linkedin.com/in/wedja-souza