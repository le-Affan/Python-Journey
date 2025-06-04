# Create two sets: one with your favorite fruits, one with seasonal fruits.
# Find the union, intersection, and difference of these sets.
# Check if a particular fruit is present in your favorite fruits set.

fav_fruits={"Mango","Strawberry","Apple"}
seasonal_fruits={"Mango","Watermelon","Strawberry"}

print(fav_fruits.union(seasonal_fruits))
print(fav_fruits.intersection(seasonal_fruits))
print(fav_fruits.difference(seasonal_fruits))

if "Watermelon" in fav_fruits:
    print("Yes watermelon is one of my fav fruits")


