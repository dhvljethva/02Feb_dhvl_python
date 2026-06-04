import datetime

# In-memory data storage (temporary, resets on app restart)
users = {}  # Format: {'username': 'password'}
posts = []  # Format: [{'author': 'username', 'title': 'Title', 'description': 'Desc', 'date': 'YYYY-MM-DD'}]

def get_non_empty_input(prompt):
    """Continuously prompts the user until they enter a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please try again.")

def register():
    """Handles new user registration."""
    print("\n--- Register ---")
    while True:
        username = get_non_empty_input("Enter a new username: ")
        # Check for repeated usernames
        if username in users:
            print("Error: Username already exists. Please choose a different one.")
        else:
            break
    
    password = get_non_empty_input("Enter a password: ")
    users[username] = password
    print("Registration successful! You can now login.")

def login():
    """Handles user login with limited attempts."""
    print("\n--- Login ---")
    attempts = 3
    while attempts > 0:
        username = get_non_empty_input("Enter username: ")
        password = get_non_empty_input("Enter password: ")
        
        if username in users and users[username] == password:
            print(f"Login successful! Welcome, {username}.")
            return username
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Invalid username or password. {attempts} attempts remaining.")
            else:
                print("Too many failed login attempts. Returning to main menu.")
    return None

def create_post(username):
    """Allows a logged-in user to create a new post."""
    print("\n--- Create a New Post ---")
    title = get_non_empty_input("Enter post title: ")
    description = get_non_empty_input("Enter post description: ")
    
    # Date generation/manual entry
    while True:
        date_choice = input("Do you want to use the current date? (y/n): ").strip().lower()
        if date_choice == 'y':
            date_str = datetime.date.today().strftime("%Y-%m-%d")
            break
        elif date_choice == 'n':
            date_str = get_non_empty_input("Enter date (e.g., YYYY-MM-DD): ")
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")
        
    post = {
        'author': username,
        'title': title,
        'description': description,
        'date': date_str
    }
    posts.append(post)
    print("Post created successfully!")

def view_all_posts():
    """Displays all posts in a clean format."""
    print("\n--- All Posts ---")
    if not posts:
        print("No posts available.")
        return
    
    for i, post in enumerate(posts, 1):
        print(f"\nPost #{i}")
        print("-" * 30)
        print(f"Author     : {post['author']}")
        print(f"Title      : {post['title']}")
        print(f"Date       : {post['date']}")
        print(f"Description: {post['description']}")
        print("-" * 30)

def search_posts_by_username():
    """Searches and displays posts by a specific author."""
    print("\n--- Search Posts ---")
    search_user = get_non_empty_input("Enter the username to search for: ")
    
    # Case-insensitive search for username
    found_posts = [post for post in posts if post['author'].lower() == search_user.lower()]
    
    if not found_posts:
        print(f"No posts found for user '{search_user}'.")
    else:
        print(f"\nFound {len(found_posts)} post(s) by '{search_user}':")
        for i, post in enumerate(found_posts, 1):
            print(f"\nPost #{i}")
            print("-" * 30)
            print(f"Title      : {post['title']}")
            print(f"Date       : {post['date']}")
            print(f"Description: {post['description']}")
            print("-" * 30)

def postboard_menu(username):
    """The main application menu for logged-in users."""
    while True:
        print(f"\n=== PostBoard Menu ({username}) ===")
        print("1. Create Post")
        print("2. View All Posts")
        print("3. Search Posts by Username")
        print("4. Logout")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            create_post(username)
        elif choice == '2':
            view_all_posts()
        elif choice == '3':
            search_posts_by_username()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

def main_menu():
    """The entry point menu."""
    print("Welcome to PostBoard App!")
    while True:
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            register()
        elif choice == '2':
            logged_in_user = login()
            if logged_in_user:
                postboard_menu(logged_in_user)
        elif choice == '3':
            print("Thank you for using PostBoard App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()