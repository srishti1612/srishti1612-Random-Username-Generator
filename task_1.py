
# random username generator 
import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Cool", "Happy", "Brave", "Clever", "Killer", "Swift", "Mighty", "Jolly"]
nouns = ["Gojo", "Dragon", "Knight", "Kakashi", "Panther", "Witch", "Pekka", "Samurai"]

# Function to generate a random username
def generate_username(include_numbers=True, include_special_chars=True, length=8):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun
    
    if include_numbers:
        username += str(random.randint(10, 99))
    
    if include_special_chars:
        username += random.choice(string.punctuation)
    
    return username[:length]  # Ensure username does not exceed the desired length

# Function to save usernames to a file
def save_to_file(username, filename="usernames.txt"):
    with open(filename, "a") as file:
        file.write(username + "\n")

# Function to get user input in a non-interactive environment
def get_user_preferences():
    return {
        "num_usernames": 5,
        "include_numbers": True,
        "include_special_chars": True,
        "length": 10
    }

# Main function
def main():
    print("Welcome to the Random Username Generator!")
    user_prefs = get_user_preferences()
    
    print("\nGenerated Usernames:")
    for _ in range(user_prefs["num_usernames"]):
        username = generate_username(user_prefs["include_numbers"], user_prefs["include_special_chars"], user_prefs["length"])
        print(username)
        save_to_file(username)
    
    print("\nUsernames saved to usernames.txt")

if __name__ == "__main__":
    main()
