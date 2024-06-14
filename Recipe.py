import requests
from passkey import uber_secret_id
def search_recipes(api_key, query):
    """
    Searches for recipes based on a given query using the Edamam API.

    Args:
        api_key (str): The API key for accessing the Edamam API.
        query (str): The query to search for recipes.
    """
    # Set the base URL for the API
    base_url = "https://api.edamam.com/search"

    # Set the parameters for the API request
    params = {
        "q": query,
        "app_id": uber_secret_id,
        "app_key": api_key,
    }

    # Send a GET request to the API
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Get the list of hits from the response
        hits = data.get("hits", [])

        # Check if there are any hits
        if not hits:
            print("No recipes found.")
        else:
            # Iterate over each hit and print the recipe details
            for hit in hits:
                recipe = hit.get("recipe", {})
                print("\nTitle:", recipe.get("label"))
                print("URL:", recipe.get("url"))
                print("Ingredients:", ", ".join(recipe.get("ingredientLines", [])))
                print("-" * 50)
    else:
        # Print the error message if the request was not successful
        print("Error:", response.status_code)


if __name__ == "__main__":
    api_key = "2d8e542a11e73df2d74066ce268fab34"

    user_query = input("Enter a recipe search query: ")

    search_recipes(api_key, user_query)