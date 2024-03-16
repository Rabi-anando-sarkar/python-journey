import requests

def fetch_qoutes():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    data = response.json()
    
    if data['success'] and 'data' in data:
        author_data = data['data']
        author_name = author_data['author']
        author_qoute = author_data['content']
        return author_name,author_qoute
    else:
        raise Exception("Failed to fetch authordata!")
    
def main():
    try:
        author_name,author_qoute = fetch_qoutes()
        print(f"{author_qoute} was qouted by {author_name}")
    except Exception as exception:
        print(str(exception))
        
if __name__ == "__main__":
    main()
        
