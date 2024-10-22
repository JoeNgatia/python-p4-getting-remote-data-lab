import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.content  # Return the raw response body as bytes
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            try:
                return json.loads(response_body.decode('utf-8'))  # Decode bytes to string and parse as JSON
            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}")
                return None
        return None

if __name__ == "__main__":
    get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
    data = get_requester.load_json()
    print(data)
