# Manufacturing Quality Data Analyzer 🏭

## About This Project
A Python tool to analyze manufacturing batch quality data,
identify defective batches, and visualize process trends.
Built as part of my learning journey in Python for 
Process Optimization in Manufacturing.

## Tools & Libraries Used
- Python 3.12
- pandas (data loading and analysis)
- matplotlib (data visualization)

## Features
- Loads real manufacturing CSV data automatically
- Calculates key process statistics:
  - Total batches analyzed
  - Average temperature and defect rate
  - Pass/Fail rate
- Detects and flags high-defect batches (Exception Reporting)
- Generates 2 visual charts:
  - Bar chart: Defects per batch (Green=Pass, Red=Fail)
  - Scatter plot: Temperature vs Defects correlation

## Key Finding
Batches with Temperature above 865°C showed significantly 
higher defect rates — demonstrating a clear 
process parameter correlation.

## How to Run
1. Install requirements:
pip install pandas matplotlib openpyxl

2. Run the analyzer:
python quality_analyzer.py

## My Background
- Studying Operational Excellence at Hochschule Hof
- Mechanical Engineering background
- Applying Python for data-driven process optimization

## Relevance to Bosch
This project demonstrates practical Python skills directly 
applicable to Wafer and Sensor manufacturing:
- Process data analysis
- Quality monitoring and exception reporting
- Data visualization for engineering decisions