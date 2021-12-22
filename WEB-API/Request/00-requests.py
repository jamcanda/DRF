import requests

def main():
    response = requests.get("http://www.google.com")
    #response = requests.get("http://www.google.com/random")
    print("Status Code: ", response.status_code)
    print("Headers: ", response.headers)


if __name__ == "__main__":
    main()