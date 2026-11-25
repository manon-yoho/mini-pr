import numpy as np
import pandas as pd
df = pd.read_csv("raw_data.csv")

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# Summary stats (mean, median, min, max, std)
stats_summary = df[num_cols].agg(["mean", "median", "min", "max", "std"]).T
print(stats_summary)

# Compare groups (adjust column names to match your dataset)
grouped_summary = df.groupby("department", observed=False).agg(
    count=("employee_id", "count"),
    mean_salary=("salary", "mean"),
    median_salary=("salary", "median"),
    min_salary=("salary", "min"),
    max_salary=("salary", "max"),
)
print(grouped_summary)

corr_matrix = df[num_cols].corr(numeric_only=True)
print(corr_matrix)

# Unstack to find top 3 strongest absolute correlations
corr_pairs = corr_matrix.unstack().reset_index()
corr_pairs.columns = ["Feature_1", "Feature_2", "Correlation"]
corr_pairs = corr_pairs[corr_pairs["Feature_1"] != corr_pairs["Feature_2"]]
corr_pairs["Abs_Corr"] = corr_pairs["Correlation"].abs()

# Deduplicate mirrored pairs (A-B vs B-A)
corr_pairs["Pair_Key"] = corr_pairs.apply(
    lambda r: tuple(sorted([r["Feature_1"], r["Feature_2"]])), axis=1
)
top_3_corr = (
    corr_pairs.drop_duplicates("Pair_Key")
    .sort_values("Abs_Corr", ascending=False)
    .head(3)[["Feature_1", "Feature_2", "Correlation"]]
)
print("\nTop 3 relationships:\n", top_3_corr)

# Example secondary table (replace with your CSV/DataFrame)
dept_budget = pd.DataFrame({
    "department": ["Sales", "Engineering", "Hr", "Operations"],
    "annual_budget": [1200000, 2500000, 600000, 900000],
})

merged_df = pd.merge(df, dept_budget, on="department", how="left")

# Sample business questions with numeric outputs
q1 = merged_df.groupby("department", observed=False)["salary"].mean().idxmax()
q1_val = merged_df.groupby("department", observed=False)["salary"].mean().max()
print(f"Q1: Highest average salary is in {q1} ({q1_val:,.2f}).")

q2 = (
    merged_df.groupby("department", observed=False)
    .agg(total_salary=("salary", "sum"), annual_budget=("annual_budget", "first"))
    .assign(utilization_pct=lambda x: (x["total_salary"] / x["annual_budget"]) * 100)
)
print("\nQ2: Salary vs. Budget by department:\n", q2)

pivot = pd.pivot_table(
    df,
    values="salary",
    index="department",
    fill_value=0,
)
print(pivot)