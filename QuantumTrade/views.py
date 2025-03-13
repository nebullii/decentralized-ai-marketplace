from django.shortcuts import render
import requests

def home_view(request):
    # Fetch Trending Crypto Assets
    crypto_url = "https://api.coingecko.com/api/v3/search/trending"
    crypto_response = requests.get(crypto_url)
    trending_assets = []

    if crypto_response.status_code == 200:
        data = crypto_response.json()
        for coin in data["coins"]:
            asset = {
                "name": coin["item"]["name"],
                "symbol": coin["item"]["symbol"].upper(),
                "floor_price": coin["item"].get("price_btc", 0),
                "volume": coin["item"].get("data", {}).get("total_volume", "N/A"),
                "icon": coin["item"]["large"]
            }
            trending_assets.append(asset)

    # Fetch Trending NFT Collections
    collections_url = "https://testnets-api.opensea.io/api/v2/collections"
    collections_response = requests.get(collections_url)
    
    trending_collections = []
    selected_collection = None  # Placeholder for collection details

    if collections_response.status_code == 200:
        collections = collections_response.json()
        
        for collection in collections.get("collections", []):  # Loop over collections
            image_url = collection.get("image_url", "")

            if image_url:  # Only add collections with an image
                collection_data = {
                    "name": collection.get("name", ""),
                    "image": image_url,
                    "floor_price": collection.get("floor_price", "N/A"),
                    "opensea_url": collection.get("opensea_url", ""),  # Store the OpenSea URL
                    "collection": collection.get("collection", ""),  # Use collection field as unique identifier
                }
                trending_collections.append(collection_data)

    # Fetch Collection Details if a collection is selected
    selected_collection_id = request.GET.get("collection")  # Fetch from URL
    if selected_collection_id:
        # Store the selected collection name in the session
        selected_collection_name = request.GET.get("collection")
        request.session['selected_collection_name'] = selected_collection_name  # Store in session
        print(selected_collection_name)
        # Fetch collection details using the `collection` field
        collection_details_url = f"https://testnets-api.opensea.io/api/v2/collections/{selected_collection_name}"
        print(collection_details_url)
        details_response = requests.get(collection_details_url)
        print(details_response)
        if details_response.status_code == 200:
            details_data = details_response.json()
            selected_collection = {
                "name": details_data.get("name", "Unnamed Collection"),
                "description": details_data.get("description", "No description available."),
                "image": details_data.get("image_url", ""),
                "banner": details_data.get("banner_image_url", ""),
                "owner": details_data.get("owner", ""),
            }

    return render(request, 'index.html', {
        'trending_assets': trending_assets,
        'trending_collections': trending_collections,
        'selected_collection': selected_collection
    })
