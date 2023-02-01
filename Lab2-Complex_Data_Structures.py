# Create a Complex Data Structure 
def main():
    about_me = {
        "Student_Name": "Matthew Kuchurean",
        "Student_ID": 10210143,
        "pizza_toppings": ["cheese", "green pepper", "Pepperoni"],
        "Movies": [
            {
                "Title": "Harry Potter and the Chamber of Secret",
                "Genre": ["Sci-Fi", "Adventure"]
            },
            {
                "Title": "Mighty Ducks",
                "Genre": ["Drama", "Action"]
            }
        ]
    }
    return about_me
# Add of New Movie
def Movies_new(details, New_Movie, about_me):
    New_Movie = {"Title": "Lethal Weapon", "Genre": ["Action"]}
    about_me["Movies"].append(New_Movie)

# Add of Function of Student Name and ID 
def aboutme_sentence(details):
    name = details["Student_Name"]
    id = details["Student_ID"]
    print(f"My name is {name}. You can call me Lord {name.rsplit(' ', 1)[0]}."
          f" My student ID is {id}")
# Add Function of New Pizza Topping 
def add__newpizza_topping(details, new_topping):
    details["pizza_toppings"].append(new_topping)
    for i, topping in enumerate(details["pizza_toppings"]):
        details["pizza_toppings"][i] = topping.lower()
    details["pizza_toppings"].sort()
# Favourite Pizza Topping
def print_Fav_pizza_toppings(details):
    print("My favorite pizza toppings are:")
    for topping in details["pizza_toppings"]:
        print(f"- {topping}")
    print()
# Function of Go to Movies and Genre 
def print_watch_genres(details):
    print("I like to watch ", end="")
    genres = []
    for movie in details["Movies"]:
        genres.extend(movie["Genre"])
    print(", ".join(genres), end=".")
    print()
# Fav Movie Titles 
def print_Fav_movie_titles(details):
    print("Some of my favorite movie titles are: ", end="")
    titles = [movie["Title"] for movie in details["Movies"]]
    print(", ".join(titles), end=".")
    print()
# Main Output
details = main()
Movies_new(details, "Pepper", details)
aboutme_sentence(details)
add__newpizza_topping(details, "Pizza sauce")
print_Fav_pizza_toppings(details)
print_watch_genres(details)
print_Fav_movie_titles(details)
