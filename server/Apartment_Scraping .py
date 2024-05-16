# central_pune = [Swargate, Deccan, Shivajinagar, Sadashivpeth]
# northern_pune = [Dhanori, Lohegaon, Wagholi, KoregaonPark, Vimannagar, Kharadi]
# western_pune = [Baner, Aundh, Bavdhan, Kothrud, Warje, KarveNagar]
# southern_pune = [Katraj, Bibwewadi, Khadewadi, Taljai, Kondhwa]
# eastern_pune = [Hadapsar, Magarpatta]

import pymongo

database_uri = "mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(database_uri)

db = client.majorDB

collection = db.users
record = collection.find().sort("_id", -1).limit(1)

for i in record:
    record = i
import socket
import re
import time
import random
import pandas as pd
import progressbar

def extract_info(element):
    title_text = re.search(r'<h2 class="heading-6">(.*?)</h2>', element).group(1).strip()
    location_text = re.search(r'<div class="text-gray-light">(.*?)</div>', element).group(1).strip()
    rent_price_text = re.search(r'<div class="font-semi-bold heading-6">(.*?)</div>', element).group(1).strip().replace('\n', '').replace('â¹', '₹')
    deposit_price_text = re.search(r'<div class="font-semi-bold heading-6" id="roomType">(.*?)</div>', element).group(1).strip().replace('\n', '').replace('â¹', '₹')
    builtup_area_text = re.search(r'<div class="heading-7">(.*?)</div>', element).group(1).strip().replace('\n', '')
    image_url = re.search(r'<img alt="{title_text}" src="(.*?)"', element).group(1)
    property_type_text = re.search(r'<div class="flex-1 border-r border-r-solid border-r-cardbordercolor">(.*?)</div>', element).group(1).strip()
    furnishing_text = re.search(r'<div class="flex">.?Furnishing.?<div>(.*?)</div>', element).group(1).strip()
    tenants_text = re.search(r'<div class="flex flex-1 border-r border-r-solid border-r-cardbordercolor">.?Preferred Tenants.?<div>(.*?)</div>', element).group(1).strip()
    availability_text = re.search(r'<div class="flex flex-1 pl-0.5p">.?Available From.?<div>(.*?)</div>', element).group(1).strip()
    return title_text, location_text, rent_price_text, deposit_price_text, builtup_area_text, image_url, property_type_text, furnishing_text, tenants_text, availability_text

# User input for the choice of area and preference
user_input_choice = record['area']
user_input_preference = record['preference']
urls = []

# Define URLs based on user input
if user_input_choice=='Central':
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41MDE4MzIyLCJsb24iOjczLjg2MzU5MTIsInBsYWNlSWQiOiJDaElKeFJnWkp4VEF3anNSUDAxSkREX21QUG8iLCJwbGFjZU5hbWUiOiJTd2FyZ2F0ZSJ9LHsibGF0IjoxOC41MzIyMTcsImxvbiI6NzMuODUxNjYyOSwicGxhY2VJZCI6IkNoSUpVeUVDczRmQXdqc1I1RGxWX0dQbEo2USIsInBsYWNlTmFtZSI6IlNoaXZhamluYWdhciBSYWlsd2F5IFN0YXRpb24ifSx7ImxhdCI6MTguNTE2NTQzNiwibG9uIjo3My44MzY2MDIxLCJwbGFjZUlkIjoiQ2hJSmZTOHFNSS1fd2pzUlpDNWMxckYyaGE0IiwicGxhY2VOYW1lIjoiRGVjY2FuIEd5bWtoYW5hIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Swargate,Shivajinagar%20Railway%20Station,Deccan%20Gymkhana")
    urls.append("https://www.nobroker.in/property/rent/pune/Sadashiv%20Peth?searchParam=W3sibGF0IjoxOC41MDgyNDg2LCJsb24iOjczLjg0NDA1NDgsInBsYWNlSWQiOiJDaElKdV9mWGtuUEF3anNSZ1ZDelNVQ2MtdHciLCJwbGFjZU5hbWUiOiJTYWRhc2hpdiBQZXRoIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Sadashiv%20Peth")
elif user_input_choice=='Northern':
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41OTY3NTg3LCJsb24iOjczLjg5Njg1MSwicGxhY2VJZCI6IkNoSUpvV0lfbmRiR3dqc1JoVUsxbW9kV2hLRSIsInBsYWNlTmFtZSI6IkRoYW5vcmkifSx7ImxhdCI6MTguNTk0NDcwNCwibG9uIjo3My45Mjc1ODg5LCJwbGFjZUlkIjoiQ2hJSm1jVS1acVBHd2pzUmxxN2JQM3AydzBNIiwicGxhY2VOYW1lIjoiTG9oZWdhb24ifSx7ImxhdCI6MTguNTgwNzcxOSwibG9uIjo3My45Nzg3MDYzLCJwbGFjZUlkIjoiQ2hJSmRfamVuNEhEd2pzUjRFczFYNWctR2RRIiwicGxhY2VOYW1lIjoiV2FnaG9saSJ9XQ==&radius=2.0&sharedAccomodation=0&city=pune&locality=Dhanori,Lohegaon,Wagholi")
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41MzYyMDg0LCJsb24iOjczLjg5Mzk3NDgsInBsYWNlSWQiOiJDaElKZFJJcU9FN0F3anNSOHM4dDRUdnV5QjQiLCJwbGFjZU5hbWUiOiJLb3JlZ2FvbiBQYXJrIn0seyJsYXQiOjE4LjU2NzkxNDYsImxvbiI6NzMuOTE0MzQzMTk5OTk5OTksInBsYWNlSWQiOiJDaElKdFlRVTVrYkJ3anNSc0xPMHFQY3NTTFkiLCJwbGFjZU5hbWUiOiJWaW1hbiBOYWdhciJ9LHsibGF0IjoxOC41NTM4MjQxLCJsb24iOjczLjk0NzY2ODksInBsYWNlSWQiOiJDaElKbGFTTEtNUER3anNSU2dCak9tRXo2RGciLCJwbGFjZU5hbWUiOiJLaGFyYWRpIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Koregaon%20Park,Viman%20Nagar,Kharadi")
elif user_input_choice=='Western':
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41NjQyNDUyLCJsb24iOjczLjc3Njg1MTEsInBsYWNlSWQiOiJDaElKeTlOZDhNLS13anNSZmF0Xy01Y1NrYUUiLCJwbGFjZU5hbWUiOiJCYW5lciJ9LHsibGF0IjoxOC41NjAxNjQ5LCJsb24iOjczLjgwMzEzMzUsInBsYWNlSWQiOiJDaElKelVGZ09raV93anNSTFRyZjJYN2dhTmsiLCJwbGFjZU5hbWUiOiJBdW5kaCJ9LHsibGF0IjoxOC41MTM0NjMsImxvbiI6NzMuNzY5ODU3ODk5OTk5OTksInBsYWNlSWQiOiJDaElKMDBYVHQxNi13anNSaDVjUmhEeWRFUEEiLCJwbGFjZU5hbWUiOiJCYXZkaGFuIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Baner,Aundh,Bavdhan&nbFr=New_HomePage")
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41MDczNTE0LCJsb24iOjczLjgwNzY1NDMsInBsYWNlSWQiOiJDaElKbllTdk1yZV93anNSOEVULXMwaUxCOVEiLCJwbGFjZU5hbWUiOiJLb3RocnVkIn0seyJsYXQiOjE4LjQ4NjQ3MjcsImxvbiI6NzMuNzk2ODMzOTk5OTk5OTksInBsYWNlSWQiOiJDaElKbFlzWVA4Ml93anNSTVNWZEN4dHc3amsiLCJwbGFjZU5hbWUiOiJXYXJqZSJ9LHsibGF0IjoxOC41MTA1MSwibG9uIjo3My44MzQ4MTgsInBsYWNlSWQiOiJDaElKVjdoR0hveV93anNSQkF1QzRfQzN5bmsiLCJwbGFjZU5hbWUiOiJLYXJ2ZSBSb2FkIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Kothrud,Warje,Karve%20Road&nbFr=New_HomePage")
elif user_input_choice=='Southern':
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC40NTI5MzIyLCJsb24iOjczLjg2NTIzNzk5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSmgxOWxBY0hxd2pzUnlKb00xaUFLVzh3IiwicGxhY2VOYW1lIjoiS2F0cmFqIn0seyJsYXQiOjE4LjQ2OTAyMTMsImxvbiI6NzMuODY0MDk0NCwicGxhY2VJZCI6IkNoSUpqWGFGUUpmcXdqc1JkdUtrYjMwX2ZSWSIsInBsYWNlTmFtZSI6IkJpYndld2FkaSJ9LHsibGF0IjoxOC40Njk1MDg4LCJsb24iOjczLjg4ODk3NzksInBsYWNlSWQiOiJDaElKVC0zeGRZcnF3anNSU3ZvbTlPSVZZTXciLCJwbGFjZU5hbWUiOiJLb25kaHdhIn1d&radius=2.0&sharedAccomodation=0&city=pune&locality=Katraj,Bibwewadi,Kondhwa&nbFr=New_HomePage")
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC40NzYyMjE1LCJsb24iOjczLjg0NDM3OTE5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSmI0NGRocXpxd2pzUkE5WjZSS2cwbEFvIiwicGxhY2VOYW1lIjoiVGFsamFpIE1hdGEgTWFuZGlyIn0seyJsYXQiOjE4LjQ0NzA5NDgsImxvbiI6NzMuODEwMTY0MywicGxhY2VJZCI6IkNoSUpsMkRmbGVHVXdqc1J0UDI1dnNjQUxCSSIsInBsYWNlTmFtZSI6IktoYWRld2FkaSJ9XQ==&radius=2.0&sharedAccomodation=0&city=pune&locality=Taljai%20Mata%20Mandir,Khadewadi&nbFr=New_HomePage")
else:
    urls.append("https://www.nobroker.in/property/rent/pune/multiple?searchParam=W3sibGF0IjoxOC41MDg5MzQsImxvbiI6NzMuOTI1OTEwMTk5OTk5OTksInBsYWNlSWQiOiJDaElKNmFyeGdmX3B3anNSVTR1c1ZUVTBZQ1UiLCJwbGFjZU5hbWUiOiJIYWRhcHNhciJ9LHsibGF0IjoxOC41MTU4MDU3LCJsb24iOjczLjkyNzE2NDQsInBsYWNlSWQiOiJDaElKVFVYVFA0M0J3anNSeE5DZ0NCQnJyamciLCJwbGFjZU5hbWUiOiJNYWdhcnBhdHRhLCBIYWRhcHNhciJ9XQ==&radius=2.0&sharedAccomodation=0&city=pune&locality=Hadapsar,Magarpatta,%20Hadapsar")

# Initialize DataFrame to store scraped data
df = pd.DataFrame()

# Iterate over the list of URLs
for url in urls:
    try:
        # Create a socket and establish a connection to the web server
        ip_address = socket.gethostbyname("www.nobroker.in")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_address, 80))

        # Send an HTTP GET request
        request = f"GET {url} HTTP/1.1\r\nHost: www.nobroker.in\r\n\r\n"
        client_socket.send(request.encode())

        # Receive and store the server's response
        response = ""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data.decode()

        client_socket.close()

        # Extract property information using regular expressions
        house_containers = re.findall(r'<article.*?</article>', response, re.DOTALL)
        if not house_containers:
            break

        for element in house_containers:
            title, location, rent_price, deposit_price, builtup_area, image_url, property_type, furnishing, tenants, availability = extract_info(element)

            # Append extracted data to DataFrame
            data = {
                "Property Title": title,
                "Location": location,
                "Rent Price": rent_price,
                "Deposit Price": deposit_price,
                "Built-up Area": builtup_area,
                "Image URL": image_url,
                "Property Type": property_type,
                "Furnishing": furnishing,
                "Preferred Tenants": tenants,
                "Availability": availability
            }
            df = pd.concat([df, pd.DataFrame([data])])

        # Introduce a delay between requests
        time.sleep(random.uniform(1, 2))

    except Exception as e:
        print(f"Error: {e}")

# Print the scraped data
print("Successfully scraped {} pages containing {} properties.".format(len(urls), len(df)))

# Store the data in a CSV file
df.to_csv('apartments.csv', index=False)


import pandas as pd
import numpy

df = pd.read_csv("apartments.csv")
df.drop(['Unnamed: 0'], axis=1, inplace=True)


def getCoordinates(url):
    # Send the API request and get the response
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = response.json()

        if len(data['results'])!=0:
            # Extract the first result from the data
            # print(data)
            result = data['results'][0]

            # Extract the latitude and longitude of the result
            if 'bbox' in result:
                latitude = result['bbox']['lat1']
                longitude = result['bbox']['lon1']
            else:
                latitude = result['lat']
                longitude = result['lon']

            return (latitude, longitude)
        else:
            return (None, None)

import requests

API_KEY = "dde5f64411d94c67a274008952e79cc1"

for ind in df.index:
    address = df['Location'][ind]

    # Build the API URL
    url = f"https://api.geoapify.com/v1/geocode/search?text={address}&lang=en&limit=1&type=amenity&filter=circle:73.85824143683541,18.510341823235862,16000&format=json&apiKey={API_KEY}"
    coords = getCoordinates(url)
    df.at[ind, 'Latitude'] = coords[0]
    df.at[ind, 'Longitude'] = coords[1]

df.to_csv('apartments.csv', index=True)

import pandas as pd
import matplotlib.pyplot as plt
import geopandas
import folium
from folium import plugins


df = pd.read_csv("apartments.csv")
df.dropna(subset=['Latitude','Longitude'], inplace=True)



# map1 = folium.Map(width = 900, height = 848, location = [18.5132,73.8579], zoom_start = 13)

# heat_data = [[lat, lon] for lat,lon in zip(df.Latitude,df.Longitude)]
# # heat_data

# plugins.HeatMap(heat_data).add_to(map1)
# map1


# # FourSquare API

import pandas as pd
import requests
import pandas as pd
import pprint

apartments_df = pd.read_csv('apartments.csv')

# Location information
RADIUS = 5000  # Radius in meters

# Categories of venues you're interested in (you can customize this)
CATEGORIES = [
    'food',  # Food venues
    'shops',  # Shops and stores
    'outdoors',  # Outdoor places
    'arts',  # Arts and entertainment
    'nightlife',  # Nightlife spots
]

# Initialize an empty DataFrame to store venue data
venues_df = pd.DataFrame(columns=['Apartment_Name','Apartment_Location', 'Apartment_Rent', 'Apartment_Deposit', 'Apartment_Negotiable', 'Apartment_Image_URL', 'Apartment_Latitude', 'Apartment_Longitude','Amenity_Name','Amenity_Category','Amenity_Latitude','Amenity_Longitude','Amenity_Address'])

# Loop through apartments and fetch amenity data
for index, apartment in apartments_df.iterrows():
    apartment_latitude = apartment['Latitude']
    apartment_longitude = apartment['Longitude']
    
    for category in CATEGORIES:
        url = f'https://api.foursquare.com/v3/places/search'
        params = {
            'll': f'{apartment_latitude},{apartment_longitude}',
            'radius': RADIUS,
            'categoryId': category,
            'limit': 50  # Number of venues per category
        }

        headers = {
            "Accept": "application/json",
            "Authorization": "fsq30OxgPdpMc4AoJP8av3qec1LhjDH3uSa2GD3p3ARgFDo="
        }

        response = requests.get(url, params=params, headers=headers).json()

        for venue_data in response.get('results', []):
            name = venue_data.get('name', 'N/A')
            categories = venue_data.get('categories', [])
            category = categories[0].get('name', 'N/A').capitalize() if categories else 'N/A'
            latitude = venue_data.get('geocodes', {}).get('main', {}).get('latitude', 'N/A')
            longitude = venue_data.get('geocodes', {}).get('main', {}).get('longitude', 'N/A')
            address = venue_data.get('location', {}).get('formatted_address', 'N/A')
#             price = category  # You can modify this based on your needs

            data = {
                'Apartment_Name': apartment['Property Title'],
                'Apartment_Location': apartment['Location'],
                'Apartment_Rent': apartment['Rent Price'],
                'Apartment_Deposit': apartment['Deposit Price'],
                'Apartment_Negotiable': apartment['Built-up Area'],
                'Apartment_Image_URL': apartment['Image URL'],
                'Apartment_Latitude': apartment['Latitude'],
                'Apartment_Longitude': apartment['Longitude'],
                'Amenity_Name': name,
                'Amenity_Category': category,
                'Amenity_Latitude': latitude,
                'Amenity_Longitude': longitude,
                'Amenity_Address': address
            }
    
#             venues_df = pd.concat([venues_df, pd.DataFrame(data)], ignore_index=True)
            venues_df.loc[len(venues_df.index)] = data

# Save the DataFrame to a CSV file
venues_df.to_csv('apartments_with_amenities.csv', index=False)

###########################

unique_apartments = pd.DataFrame(columns=['Apartment_Name', 'Apartment_Location', 'Apartment_Rent', 'Apartment_Deposit', 'Apartment_Negotiable', 'Apartment_Image_URL', 'Apartment_Latitude', 'Apartment_Longitude'])
amenity_counts = {} # store amenity counts for each apartment

for index, row in df.iterrows():
    apartment_name = row['Apartment_Name']
    amenity_category = row['Amenity_Category']
    
    if apartment_name not in amenity_counts:
        amenity_counts[apartment_name] = {}
    
    if amenity_category not in amenity_counts[apartment_name]:
        amenity_counts[apartment_name][amenity_category] = 0
    
    amenity_counts[apartment_name][amenity_category] += 1
    
    if apartment_name not in unique_apartments['Apartment_Name'].values:
        unique_apartments = unique_apartments.append(df[df['Apartment_Name'] == apartment_name].iloc[0], ignore_index=True)

amenity_count_list = []
for apartment_name, counts in amenity_counts.items():
    counts['Apartment_Name'] = apartment_name
    amenity_count_list.append(counts)

# Create a DataFrame from the list of dictionaries
amenity_count_df = pd.DataFrame(amenity_count_list).fillna(0)

apartments_with_amenity_type = pd.DataFrame()
for index, row in unique_apartments.iterrows():
    apartment_name = row['Apartment_Name']
    matching_counts = amenity_count_df[amenity_count_df['Apartment_Name'] == apartment_name]
    
    if not matching_counts.empty:
        merged_row = pd.concat([row, matching_counts.iloc[0]])
        apartments_with_amenity_type = apartments_with_amenity_type.append(merged_row, ignore_index=True)


###################################

# # Normalization


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

apartments_with_amenity_type = pd.read_csv("apartments_with_amenity_type.csv")

# Select only the columns containing amenity data
amenity_columns = apartments_with_amenity_type.iloc[:,9:].columns
amenity_data = apartments_with_amenity_type[amenity_columns]

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit and transform the amenity data
normalized_amenities = scaler.fit_transform(amenity_data)

# Create a new DataFrame with normalized amenity data
temp_df = pd.DataFrame(normalized_amenities, columns=amenity_columns)

# Add the 'Apartment Name' column back to the DataFrame
normalized_df = pd.concat([apartments_with_amenity_type[apartments.columns], temp_df[amenity_columns]], axis=1)

# # Preference Vector using NLP

import pandas as pd
import numpy as np
import string

apartments_with_amenity_type = pd.read_csv("apartments_with_amenity_type.csv")

# Select only the columns containing amenity data
preference_categories = amenity_columns

user_input_preference = record['preference']
# user_input_preference = 'I want french hotel , excuse me french gym'

user_input_preference_lower = ""

for char in user_input_preference:
    if(char>='A' and char<='Z'):
        user_input_preference_lower += chr(ord(char)+32)
    else:
        user_input_preference_lower += char

#Removing punctuations
cleaned_text=""
for char in user_input_preference_lower:
    if(char>='A' and char<='Z' or char>='a' and char<='z' or ord(char)==32):
        cleaned_text += char

#Tokenization
token_words=[]
n=len(cleaned_text)
word=""
i=0
while i<n:
    if(cleaned_text[i]==' '):
        if(len(word)>0):
            token_words.append(word)
            word=""
    else :
        word+=cleaned_text[i]
    i=i+1

if(len(word)>0):
    token_words.append(word)


# Removing stopwords
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

tokens=[]
for word in token_words:
    if word not in stop_words:
        tokens.append(word)



extracted_amenities=[]
for word in tokens:
    extracted_amenities = list(set(extracted_amenities) | set([s for s in preference_categories if word in s.lower()]))



# Create the preference vector
preference_vector = np.array([1 if category in extracted_amenities else 0 for category in preference_categories], dtype=np.float64)



# # Kmeans Clustering

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# List of all preference categories representing apartment features/preferences
apartment_features = normalized_df[amenity_columns]

# Number of clusters
num_clusters = 3

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
normalized_df['Cluster'] = kmeans.fit_predict(apartment_features)

distances = np.linalg.norm(apartment_features - preference_vector, axis=1)
scores = 1/(1+distances)
normalized_df['Score'] = scores
ranked_apartments = normalized_df.groupby('Cluster').apply(lambda group: group.sort_values(by='Score', ascending=False))
ranked_apartments.drop(amenity_columns, axis=1, inplace=True)
ranked_apartments.to_csv('Clustered_Apartments.csv', index=False)

# Get Coordinates for Amenities for Businesses
req_cluster = ranked_apartments.iloc[0]['Cluster']

lat, lon, count = 0, 0, 0
for index, row in ranked_apartments.iterrows():
    if (row['Cluster']==req_cluster):
        lat += row['Apartment_Latitude']
        lon += row['Apartment_Longitude']
        count += 1
    else:
        break

lat = lat/count
lon = lon/count

db = client.majorDB
collection = db.amenities_for_businesses

for category in extracted_amenities:
    query = {'Amenity': category}

    # New value to be added to the "Location" array
    new_location_value = {'latitude': lat, 'longitude': lon}

    # Use the $push operator to add the new value to the existing array
    update_query = {"$push": {"Locations": new_location_value}}

    # Update the document in the collection
    collection.update_one(query, update_query, upsert=True)

# # Visualisation of Clustered Apartments


# map2 = folium.Map(width = 900, height = 848, location = [18.5132,73.8579], tiles = "cartodbpositron", zoom_start = 12)

# for lat,lon,clus in zip(ranked_apartments.Apartment_Latitude, ranked_apartments.Apartment_Longitude, ranked_apartments.Cluster):
#     if clus==0:
#         folium.Marker(location=[lat,lon],popup='Best',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='green',icon='none')).add_to(map2)
#     elif clus==1:
#         folium.Marker(location=[lat,lon],popup='Better',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='blue',icon='none')).add_to(map2)
#     else:
#         folium.Marker(location=[lat,lon],popup='Good',tooltip='<strong>Click here to see Popup</strong>',icon=folium.Icon(color='red',icon='none')).add_to(map2)

# map2



test = pd.read_csv("Clustered_Apartments.csv")

collection = db.apartments
data_dict = test.to_dict("records")
# Insert collection
collection.drop()
collection.insert_many(data_dict)

print("Form Python file: Executed Succesfully")