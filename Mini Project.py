# ==================================================
# RULE-BASED MOVIE RECOMMENDATION SYSTEM
# Using Python and Predefined IF-THEN Rules
# ==================================================

# Knowledge Base: Movie details
movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Thought-provoking"
    },
    {
        "title": "Inception",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Exciting"
    },
    {
        "title": "The Martian",
        "genre": "Sci-Fi",
        "language": "English",
        "mood": "Inspirational"
    },
    {
        "title": "3 Idiots",
        "genre": "Comedy",
        "language": "Hindi",
        "mood": "Inspirational"
    },
    {
        "title": "Hera Pheri",
        "genre": "Comedy",
        "language": "Hindi",
        "mood": "Happy"
    },
    {
        "title": "The Hangover",
        "genre": "Comedy",
        "language": "English",
        "mood": "Happy"
    },
    {
        "title": "The Conjuring",
        "genre": "Horror",
        "language": "English",
        "mood": "Scary"
    },
    {
        "title": "Bhool Bhulaiyaa",
        "genre": "Horror",
        "language": "Hindi",
        "mood": "Scary"
    },
    {
        "title": "Avengers: Endgame",
        "genre": "Action",
        "language": "English",
        "mood": "Exciting"
    },
    {
        "title": "Mad Max: Fury Road",
        "genre": "Action",
        "language": "English",
        "mood": "Exciting"
    },
    {
        "title": "Shershaah",
        "genre": "Action",
        "language": "Hindi",
        "mood": "Inspirational"
    },
    {
        "title": "Zindagi Na Milegi Dobara",
        "genre": "Drama",
        "language": "Hindi",
        "mood": "Relaxed"
    },
    {
        "title": "The Pursuit of Happyness",
        "genre": "Drama",
        "language": "English",
        "mood": "Inspirational"
    },
    {
        "title": "Jab We Met",
        "genre": "Romance",
        "language": "Hindi",
        "mood": "Happy"
    },
    {
        "title": "The Notebook",
        "genre": "Romance",
        "language": "English",
        "mood": "Relaxed"
    }
]


# Function to recommend movies using predefined rules
def recommend_movies(genre, language, mood):
    recommendations = []

    for movie in movies:
        # IF genre, language, and mood match
        # THEN recommend the movie
        if (
            movie["genre"].lower() == genre.lower()
            and movie["language"].lower() == language.lower()
            and movie["mood"].lower() == mood.lower()
        ):
            recommendations.append(movie)

    return recommendations


# Main program
def main():
    print("=" * 55)
    print("       RULE-BASED MOVIE RECOMMENDATION SYSTEM")
    print("=" * 55)

    # Display available options
    genres = sorted(set(movie["genre"] for movie in movies))
    languages = sorted(set(movie["language"] for movie in movies))
    moods = sorted(set(movie["mood"] for movie in movies))

    print("\nAvailable Genres:")
    print(", ".join(genres))

    print("\nAvailable Languages:")
    print(", ".join(languages))

    print("\nAvailable Moods:")
    print(", ".join(moods))

    # Accept user preferences
    genre = input("\nEnter your preferred genre: ").strip()
    language = input("Enter your preferred language: ").strip()
    mood = input("Enter your preferred mood: ").strip()

    # Generate recommendations
    recommendations = recommend_movies(genre, language, mood)

    # Display results
    print("\n" + "=" * 55)
    print("              MOVIE RECOMMENDATIONS")
    print("=" * 55)

    if recommendations:
        for i, movie in enumerate(recommendations, start=1):
            print(f"\n{i}. {movie['title']}")
            print(f"   Genre    : {movie['genre']}")
            print(f"   Language : {movie['language']}")
            print(f"   Mood     : {movie['mood']}")
    else:
        print("\nNo matching movies found.")
        print("Please try different preferences.")

    print("\n" + "=" * 55)
    print("Thank you for using the recommendation system!")
    print("=" * 55)


# Run the program
if __name__ == "__main__":
    main()