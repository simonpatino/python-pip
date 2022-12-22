import requests
def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)
    print(r.text)
    categories = r.json()
    for x in categories:
        print(x["name"])
