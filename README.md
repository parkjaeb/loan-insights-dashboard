# Loan Application & Default Insights Dashboard 

In this project, I combined two real datasets - one for **loan approval** and another for **loan default** - and cleaned, merged, and analyzed them
to uncover meaningful insights for finanical institutions like Union One.

--- 

## Project Goal 

To analyze approval trends and risk patterns in loan applications using Python and visualization tools.
The key objectives: 
- Identify factors linked to higher loan approval.
- Discover which property areas have higher default rates.
- Visualize approval and default trends across income levels and property areas.

--- 

## Tools & Libraries 

- Python 3 
- Pandas
- Seaborn
- Matplotlib 

## Data Cleaning Steps 
- Standarized column names
- Parsed inconsistent date formats 
- Converted strings to numberic where needed 
- Filled missing categorical values using mode 
- Filled missing categorical values using mode
- Mapped 'Y'/'N' approval statuses to 1/0
- Removed outliers for cleaner visualizations


## Key Visual Insights 

### 1. Loan Approval by Education
What: Shows whether education level impacts approval rate.
Why: Helps determine if educaiton influences lending decisions.

### 2. Default Rate by Property Area
What: Reveals geographic risk areas with higher default patterns.
Why: Identify higher-risk geographic areas and adjust credit strategies or risk models accordingly.

### 3. Loan Amount Distribution
What: Examines borrowing behavior and helps identify potential outliers.
Why: Reveals applicant borrowing behavior and potential anomalies.

### 4. Correlation Heatmap
What: Explores the strength of relationships between features (income, loan amount, approval).
Why: Identifies which features might be useful in predictive modeling.

### 5. Approval Rate by Property Area
What: Highlights which geographic areas tend to have higher loan approval success.
Why: Highlights whether certain areas experience approval bias or priority.


## Next Steps 
- Build a predictive model for default risk
- Make the dashboard interactive
- Integrate additional data


Thank you!