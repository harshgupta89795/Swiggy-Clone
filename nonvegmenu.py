import pandas as pd

data = {
"Food Item": ["Caesar Salad", "Butter Chicken","Sushi Roll", "Tacos"],
"Description": ["Crisp romaine lettuce with Caesar dressing",
        "Rich and creamy butter chicken curry",
"Fresh sushi roll with salmon and avocado",
"Soft tacos filled with chicken and veggies"],
"Category": ["Salads", "Indian","Japanese", "Mexican"],
"Price (INR)": [149, 399, 499,199],
"Calories": [180, 450,200,250],
"Availability": [
        "Available", "Available", "Available", "Available"],
"Path":["Caesar Salad.jpg","Butter Chicken.jpg","Sushi Roll.jpg","Tacos.jpg"]
}


df = pd.DataFrame(data)

df.to_csv("nonvegmenu.csv", index=False)