import requests

def client():

    # data = {
    #     "username": "admin2", 
    #     "email": "test@rest.com",
    #     "password1": "jamjam25",
    #     "password2": "jamjam25"
    #     }

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/",
    #                          data=data)

    token_h = "Token 2551275ce658c712e08d7905ded953e8c123708f"
    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            headers=headers)

    print("Status Code: ", response.status_code)
    
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()