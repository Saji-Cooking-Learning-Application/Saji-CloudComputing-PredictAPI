import requests

resp = requests.post("http://localhost:5000/predict/bahan", files={'file': open('putih.jpeg', 'rb')})

print("Response Content:", resp.text)  # Print raw content

try:
    json_response = resp.json()  # Try to parse as JSON
    print("JSON Response:", json_response)
except ValueError as e:
    print(f"Error parsing JSON: {e}")
