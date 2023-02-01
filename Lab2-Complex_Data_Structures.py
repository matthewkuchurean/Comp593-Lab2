def main() :
    about_me = {
        "Student_Name": "Matt Kuchurean",
        "Student_ID": 10210143,
        "pizza_toppings": ["Cheese", "Green Pepper", "Pepperoni"],
        "Movies": [
            {
                "Title": "Harry Potter and the Chamber of Secret",
                "Genre": "Adventure"
            },
            {
                "Title": "The Might Ducks",
                "Genre": ["Drama", "Comedy"]
            }
        ]
    }
    return about_me

    # Created a Function to define details about me and adding a movie to the data structure......
def Movies(New_Movie, about_me):
    New_Movie = {"Title": "Lethal Weapon", "Genre": ["Action"]}
    about_me["Movies"].append(New_Movie)

   
    #Step 4 - Function that prints student name and IDdef printing_sentence(details) : 
    # TODO: Step 4 - Function that prints student name and ID
    details =0
    Function = f"My name is" + {details['Student_Name']} + "But you can call me Lord" + {details["Student_Name"].removesuffix('Gogia')} + '.'\
    "And My Student ID is" + {details["Student_ID", "end = '\n\n'"]}  
    print(Function , "end = '\n\n'", "end = '\n\n'")


# Step 5 - Function that adds pizza toppings to data structure
     #adding new topping 
    details["Topping"].extend(New_Topping)

    # Adding a new topping 
    New_Topping = ['pizza seasoning']
    about_me["pizza_toppings"].append(New_Topping)


    #lowercasing the letters
    for i,a in enumerate(details['topping']) :
        details['topping'][i] = a.lower()
    
    #sorting the toppings in alphabetical order
    details['topping'].sort()

    
#  Step 6 - Function that prints bullet list of pizza toppings
#printing the toppings with bullets
def bullet_new_toppings(student_details) :
    print("My favourite toppings are:")

    for p in student_details['topping']:
        print(f"- {p}")
    print()


#Step 7 - Function that prints comma-separated list of movie genres
#printing genres
def comma_goto_genre(student_details) :
    print(f"My goto genres are", end='')
    for i,g in enumerate(student_details['movies']) :
        print(g['genre'], end='')
        if i < len(student_details['movies'])-1:
            print(', ', end='')
    print('.', end='\n\n')

#Step 8 - Function that prints comma-separated list of movie titles
#printing movies
def comma_list_genr(student_details) :
    print(f"My favourite movies are", end='')
    for i,g in enumerate(student_details['movies']) :
        print(g['title'], end='')
        if i < len(student_details['movies'])-1:
            print(', ', end='')
    print('.', end='\n\n')

#calling the main function
main()
Movies(main)
bullet_new_toppings(main)
comma_goto_genre(main)
comma_list_genr(main)





