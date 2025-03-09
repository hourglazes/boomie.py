# Nursery Rhymes Selector

def get_nursery_rhymes(theme):
    nursery_rhymes = {
        "animals": [
            "Old MacDonald Had a Farm",
            "Baa Baa Black Sheep",
            "Five Little Ducks",
            "The Itsy Bitsy Spider",
            "Hickory Dickory Dock"
        ],
        "nature": [
            "Twinkle Twinkle Little Star",
            "Row Row Row Your Boat",
            "The Green Grass Grows All Around",
            "The Wheels on the Bus",
            "Incy Wincy Spider"
        ],
        "funny": [
            "Humpty Dumpty",
            "Hey Diddle Diddle",
            "This Old Man",
            "There Was an Old Woman Who Lived in a Shoe",
            "Little Miss Muffet"
        ],
        "classic": [
            "Ring a Ring o' Roses",
            "London Bridge is Falling Down",
            "Mary Had a Little Lamb",
            "Jack and Jill",
            "The Muffin Man"
        ]
    }

    return nursery_rhymes.get(theme, ["No nursery rhymes available for this theme."])

def main():
    print("Welcome to Aunty Kennys Nursery Rhymes Selector!")
    print("🌈🎶 Welcome little singing stars! 🎶🌈")
    print("Choose a theme for nursery rhymes:")
    print("1. Animals")
    print("2. Nature")
    print("3. Funny")
    print("4. Classic")

    choice = input("Enter the number corresponding to your choice (1-4): ")

    themes = {
        "1": "animals",
        "2": "nature",
        "3": "funny",
        "4": "classic"
    }

    selected_theme = themes.get(choice)

    if selected_theme:
        rhymes = get_nursery_rhymes(selected_theme)
        print(f"\nNursery Rhymes for the theme '{selected_theme}':")
        for rhyme in rhymes:
            print(f"- {rhyme}")
    else:
        print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()