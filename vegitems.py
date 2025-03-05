import pandas as pd

data = {
    "Food Item": ["Margherita Pizza", "Veggie Burger","Paneer Tikka",
        "Spring Rolls"],
    "Description":["Classic cheese pizza with tomato base",
        "A healthy burger with fresh veggies",
        "Grilled paneer with Indian spices",
        "Crispy rolls stuffed with veggies"],
"Category": [
        "Italian", "American","Indian","Chinese"],
"Price (INR)": [299, 199, 249,149],
"Calories": [270, 350, 300,200],
"Availability": [
        "Available", "Available", "Available",
        "Available"],
"Path":["Margherita Pizza.jpg","Veggie Burger.jpg","Paneer Tikka.jpg",
"Spring Rolls.jpg"]
}
df = pd.DataFrame(data)

df.to_csv("vegmenu.csv", index=False)