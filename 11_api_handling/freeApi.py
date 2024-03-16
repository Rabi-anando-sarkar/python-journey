import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch userdata!")
    
def main():
    try:
        username,country = fetch_random_user()
        print(f'User {username} Belongs From {country}')
    except Exception as exception:
        print(str(exception))

if __name__ == "__main__":
    main()