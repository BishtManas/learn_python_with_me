import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        user_info = {
            "Username": data.get("login"),
            "Name": data.get("name"),
            "Bio": data.get("bio"),
            "Public Repos": data.get("public_repos"),
            "Followers": data.get("followers"),
            "Following": data.get("following"),
            "Profile URL": data.get("html_url"),
        }
        return user_info
    elif response.status_code == 404:
        print("User not found.")
        return None
    else:
        print("Error fetching data:", response.status_code)
        return None

def display_user_info(user_info):
    print("\nGitHub User Info --->")
    for key, value in user_info.items():
        print(f"{key}: {value if value else 'N/A'}")

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    user_info = get_github_user_info(username)
    
    if user_info:
        display_user_info(user_info)
