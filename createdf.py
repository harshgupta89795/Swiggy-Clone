import pandas as pd

# Data
data = {
    "Food Item": [
        "Margherita Pizza", "Veggie Burger", "Caesar Salad", "Butter Chicken",
        "Paneer Tikka", "Sushi Roll", "Chocolate Cake", "Tacos",
        "Spring Rolls", "Espresso"
    ],
    "Description": [
        "Classic cheese pizza with tomato base",
        "A healthy burger with fresh veggies",
        "Crisp romaine lettuce with Caesar dressing",
        "Rich and creamy butter chicken curry",
        "Grilled paneer with Indian spices",
        "Fresh sushi roll with salmon and avocado",
        "Decadent chocolate cake with ganache topping",
        "Soft tacos filled with chicken and veggies",
        "Crispy rolls stuffed with veggies",
        "Strong and rich coffee shot"
    ],
    "Category": [
        "Italian", "American", "Salads", "Indian", "Indian",
        "Japanese", "Desserts", "Mexican", "Chinese", "Beverages"
    ],
    "Price (INR)": [299, 199, 149, 399, 249, 499, 349, 199, 149, 99],
    "Calories": [270, 350, 180, 450, 300, 200, 450, 250, 200, 10],
    "Availability": [
        "Available", "Available", "Available", "Available",
        "Available", "Out of Stock", "Available", "Available",
        "Available", "Available"
    ],
    "Path":["Margherita Pizza.jpg","Veggie Burger.jpg","Caesar Salad.jpg",
            "Butter Chicken.jpg","Paneer Tikka.jpg","Sushi Roll.jpg",
            "Chocolate Cake.jpg","Tacos.jpg","Spring Rolls.jpg","Espresso.jpg"],
    "Key":["Veg","Veg","Non-Veg","Non-Veg","Veg","Non-Veg","Non-Veg","Non-Veg","Veg","Veg"]
}

df = pd.DataFrame(data)
df.to_csv("menu.csv", index=False)
