import pandas as pd

# Data
data = {
    "Food Item": ["Chocolate Cake"],
    "Description": ["Decadent chocolate cake with ganache topping"],
    "Category": ["Desserts"],
    "Price (INR)": [349],
    "Calories": [450],
"Availability": [
        "Available"],
"Path":["Chocolate Cake.jpg"]
}


df = pd.DataFrame(data)
df.to_csv("desserts.csv", index=False)