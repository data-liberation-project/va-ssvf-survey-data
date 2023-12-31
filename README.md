# VA SSVF Satisfaction Survey Data

This repository contains data and PDF reports received by the [Data Liberation Project](https://www.data-liberation-project.org/), via a [Freedom of Information Act request](https://www.data-liberation-project.org/requests/ssvf-satisfaction-surveys/) to the US Department of Veterans Affairs (VA).

## Background

Please [see here](https://docs.google.com/document/d/1unanFEUnBDVBMK9pmpb0EVvRlpB-jtRC6gwlXSN-If4/edit) for general documentation.

## FOIA Records

The records provided by the VA (and reorganized, but not edited, by the Data Liberation Project) are as follows:

```
data/
├── documentation
│   └── 1772 VA SSVF Data Dictionary.xlsx
└── raw
    ├── FINAL Data - FY 2016-2017_Excluding PII.xlsx
    ├── FINAL Data - FY 2018-2020_Excluding PII.xlsx
    └── SSVF Annual National Report Data Oct 21 - Sep 22_Excluding PII.xlsx

pdfs/
├── SSVF FY21-22 National Report_Excluding PII.pdf
├── SSVF_Annual_Report_FY19.pdf
├── Statistical Summary 1.1.2015 - 2.10.2016.pdf
├── VA SSVF Year End Report FY16.pdf
├── VA SSVF Year End Report FY17.pdf
├── VA SSVF Year End Report FY18.pdf
└── VA SSVF Year End Report FY20.pdf
```

## Code

This repository currently contains two pieces of Python code:

- [`scripts/extract-pdf-tables.py`](scripts/extract-pdf-tables.py), which extracts the provider satisfaction table that spans on pages 21–25 of [`pdfs/VA SSVF Year End Report FY20.pdf`](pdfs/VA%20SSVF%20Year%20End%20Report%20FY20.pdf), and saves that data to [`data/from-pdfs/provider-satisfaction-fy20.csv`](data/from-pdfs/provider-satisfaction-fy20.csv). In the future, this script might be expanded to extract additional tables, and from additional PDFs.
- [`notebooks/satisfaction-calculations.ipynb`](notebooks/satisfaction-calculations.ipynb), which checks that the raw survey data matches (in at least the tested aspects) with the results presented in the PDF table noted above, and generates [`data/output/provider-satisfaction-by-fiscal-year.csv`](data/output/provider-satisfaction-by-fiscal-year.csv).

## Output

The [notebook mentioned above](notebooks/satisfaction-calculations.ipynb) generates [`data/output/provider-satisfaction-by-fiscal-year.csv`](data/output/provider-satisfaction-by-fiscal-year.csv), which calculates the total number of responses to the SSVF survey's question on general satisfaction, overall and by response (Extremely Poor, Below Average, Average, Above Average, Excellent), by provider and fiscal year.

| Column Name | Description |
|-------------|-------------|
| fiscal_year | The fiscal year (Oct.-Sept.) in question. |
| grant_id | The provider's grant ID. |
| provider_name | The provider's name, in the raw data. (Note: The FY 2022 raw data did not include the provider names.) |
| provider_name_latest | The provider's name, in the most recent fiscal year of raw data available. |
| responses_total | The total number of survey responses. |
| q1_1 | The number of responses rating "the quality of the services you have received" (Q1) as "Extremely Poor". |
| q1_2 | … as "Below Average". |
| q1_3 | … as "Average". |
| q1_4 | … as "Above Average". |
| q1_5 | … as "Excellent". |
| top_2_count | The total number of "Excellent" and "Above Average" responses to Q1. |
| top_2_pct | The percentage of "Excellent" and "Above Average" responses to Q1. |


## Licensing

The files provided directly via FOIA (see listing above) are, as government documents, now in the public domain. All other data files have been generated by the Data Liberation Project and are available under Creative Commons’ [CC BY-SA 4.0 license terms](https://creativecommons.org/licenses/by-sa/4.0/). This repository’s code is available under the [MIT License terms](https://opensource.org/license/mit/). 
