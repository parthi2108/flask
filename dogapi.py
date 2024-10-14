import requests

# API URL
url = "https://dog.ceo/api/breeds/image/random"

# Open the file in write mode
with open("fact.txt", "w") as file:
    for _ in range(100):
        # Make the API call
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            dog_image_url = data.get("message", "No image found")

            # Write the dog image URL to the file
            file.write(f"Random Dog Image URL: {dog_image_url}\n")
        else:
            print("Failed to retrieve data from the API")

print("100 Dog image URLs have been saved to fact.txt")
