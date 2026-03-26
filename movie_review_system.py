import os
import matplotlib.pyplot as plt

FILE = "movies.txt"

# Add Review
def add_review():
    movie = input("Enter movie name: ")
    reviewer = input("Enter your name: ")
    rating = input("Enter rating (1-5): ")
    review = input("Enter review: ").replace(",", " ")

    # Check for duplicate
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue
                m, r, ra, rev = parts

                if m == movie and r == reviewer:
                    print("⚠️ Review already exists!\n")
                    return

    with open(FILE, "a") as f:
        f.write(f"{movie},{reviewer},{rating},{review}\n")

    print("✅ Review added successfully!\n")
# View Reviews
def view_reviews():
    if not os.path.exists(FILE):
        print("No reviews found.\n")
        return

    with open(FILE, "r") as f:
        print("\n📄 Movie Reviews:\n")
        for line in f:
            parts = line.strip().split(",")

            # Skip invalid or empty lines
            if len(parts) != 4:
                continue

            movie, reviewer, rating, review = parts

            print(f"Movie: {movie}")
            print(f"Reviewer: {reviewer}")
            print(f"Rating: {rating}")
            print(f"Review: {review}")
            print("-" * 30)

# Update Review
def update_review():
    movie_name = input("Enter movie name to update: ")
    updated = False
    data = []

    if not os.path.exists(FILE):
        print("No data found.\n")
        return

    with open(FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) != 4:
               continue
            movie, reviewer, rating, review = parts
            if movie == movie_name:
                print("Enter new details:")
                reviewer = input("New reviewer name: ")
                rating = input("New rating: ")
                review = input("New review: ")
                updated = True
            data.append(f"{movie},{reviewer},{rating},{review}\n")

    with open(FILE, "w") as f:
        f.writelines(data)

    if updated:
        print("✅ Review updated successfully!\n")
    else:
        print("❌ Movie not found.\n")


# Delete Review
def delete_review():
    movie_name = input("Enter movie name to delete: ")
    deleted = False
    data = []

    if not os.path.exists(FILE):
        print("No data found.\n")
        return

    with open(FILE, "r") as f:
        for line in f:
            movie, reviewer, rating, review = line.strip().split(",")
            if movie != movie_name:
                data.append(line)
            else:
                deleted = True

    with open(FILE, "w") as f:
        f.writelines(data)

    if deleted:
        print("🗑️ Review deleted successfully!\n")
    else:
        print("❌ Movie not found.\n")


# 📊 Show Graph
def show_graph():
    if not os.path.exists(FILE):
        print("No data found.\n")
        return

    movies = []
    ratings = []

    with open(FILE, "r") as f:
        for line in f:
            movie, reviewer, rating, review = line.strip().split(",")
            movies.append(movie)
            ratings.append(float(rating))

    if len(movies) == 0:
        print("No data to display.\n")
        return

    plt.figure()
    plt.bar(movies, ratings)
    plt.xlabel("Movies")
    plt.ylabel("Ratings")
    plt.title("Movie Ratings Chart")
    plt.xticks(rotation=30)
    plt.show()


# Main Menu
while True:
    print("\n🎬 Movie Review System")
    print("1. Add Review")
    print("2. View Reviews")
    print("3. Update Review")
    print("4. Delete Review")
    print("5. Show Graph")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_review()
    elif choice == "2":
        view_reviews()
    elif choice == "3":
        update_review()
    elif choice == "4":
        delete_review()
    elif choice == "5":
        show_graph()
    elif choice == "6":
        print("👋 Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")
