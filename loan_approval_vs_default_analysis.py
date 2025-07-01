import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the datasets
df_approval = pd.read_csv('data/loan_approval.csv')
df_default = pd.read_csv('data/loan_default.csv')

# Standardize column names
df_approval.columns = df_approval.columns.str.strip().str.lower().str.replace(' ', '_')
df_default.columns = df_default.columns.str.strip().str.lower().str.replace(' ', '_')

# Merge two datasets
df_merged = pd.concat([df_approval, df_default], axis=0, ignore_index=True)

# Convert numerical columns
for col in ['loanamount', 'applicantincome', 'income']:
    if col in df_merged.columns:
        df_merged[col] = pd.to_numeric(df_merged[col], errors='coerce')

# Clean date columns
for col in df_merged.columns:
    if 'date' in col:
        df_merged[col] = pd.to_datetime(df_merged[col], errors='coerce')

# New column 'approved' by mapping 'Y' to 1 and 'N' to 0
if 'loan_status' in df_merged.columns:
    df_merged['loan_status'] = df_merged['loan_status'].astype(str).str.strip().str.upper()
    df_merged['approved'] = df_merged['loan_status'].map({'Y': 1, 'N': 0})
    df_merged['approved'] = df_merged['approved'].fillna(0)

# Fill missing values in categorical columns with mode
cat_cols = df_merged.select_dtypes(include='object').columns
for col in cat_cols:
    df_merged[col] = df_merged[col].fillna(df_merged[col].mode()[0])

df_merged.to_csv('cleaned_loan_data.csv', index=False)

# Load your cleaned CSV file
df = pd.read_csv('data/cleaned_loan_data.csv')

# 1. Approval Rate by Education Level
approval_by_education = df.groupby('education', as_index=False)['approved'].mean()

plt.figure(figsize=(8, 5))
sns.barplot(data=approval_by_education, x='education', y='approved')
plt.title('Loan Approval Rate by Education Level')
plt.ylabel('Approval Rate')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig('visuals/approval_by_education.png')
plt.close()
# Reveal if more educated applicants are more likely to get approved.

# 2. Default Rate by Property Area
if 'default' in df.columns:
    default_by_area = df.groupby('property_area', as_index=False)['default'].mean()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=default_by_area, x='property_area', y='default')
    plt.title('Default Rate by Property Area')
    plt.ylabel('Default Rate')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('visuals/default_by_area.png')
    plt.close()

# Understand which property area has higher risk.

# 3. Loan Amount Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['loanamount'], bins=20, kde=True)
plt.title('Loan Amount Distribution')
plt.xlabel('Loan Amount')
plt.tight_layout()
plt.savefig('visuals/loan_amount_distribution.png')
plt.close()
# Understand the loan ranges and spot outliers or skewed demand.

# 4. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Numeric Features')
plt.tight_layout()
plt.savefig('visuals/correlation_heatmap.png')
plt.close()
# Understand what drives approval or default statistically

# 5. Approval Rate by Property Area
if 'approved' in df.columns and 'property_area' in df.columns:
    approval_by_area = df.groupby('property_area', as_index=False)['approved'].mean()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=approval_by_area, x='property_area', y='approved', color='skyblue')
    plt.title('Loan Approval Rate by Property Area')
    plt.xlabel('Property Area')
    plt.ylabel('Approval Rate')
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig('visuals/approval_by_property_area.png')
    plt.close()
