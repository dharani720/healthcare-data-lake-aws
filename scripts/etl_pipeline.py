import pandas as pd

# Simulated healthcare data
data = {
    "patient_id": [1, 2, 3],
    "age": [45, 60, 30],
    "billing_amount": [200, 500, 150]
}

df = pd.DataFrame(data)

# Transformation
df['billing_category'] = df['billing_amount'].apply(
    lambda x: 'High' if x > 300 else 'Low'
)

print("Transformed Data:")
print(df)

# Save to CSV (simulate S3 upload)
df.to_csv("processed_healthcare_data.csv", index=False)
