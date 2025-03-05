import pandas as pd

# Data
data = {
    "Food Item": [
        "Espresso"],
"Description": ["Strong and rich coffee shot"],
"Category": [ "Beverages"
    ],
"Price (INR)": [99],
"Calories": [10],
"Availability": ["Available"
    ],
"Path":["Espresso.jpg"]
}
df = pd.DataFrame(data)
df.to_csv("drinks.csv", index=False)