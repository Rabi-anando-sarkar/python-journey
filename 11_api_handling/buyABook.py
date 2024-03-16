import requests

def buy_a_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and 'data' in data:
        book_data = data["data"]
        title = book_data["volumeInfo"]["title"]
        author = book_data["volumeInfo"]["authors"]
        pageCount = book_data["volumeInfo"]['pageCount']
        saleInfo = book_data["saleInfo"]["saleability"]
        return title,author,pageCount,saleInfo
    else:
        raise Exception("Failed to fetch userdata!")
    
    
def main():
    try:
        title,author,pageCount,saleInfo = buy_a_book()
        print(f'''
              Title : {title}
              Author : {', '.join(author)}
              No. of pages : {pageCount}
              Is it for sale? : {saleInfo}
              ''')
    except Exception as exception:
        print(str(exception))
        

if __name__ == '__main__':
    main()
        