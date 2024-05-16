import pymongo

database_uri = "mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(database_uri)

db = client.majorDB

collection = db.businesses
record = collection.find().sort("_id", -1).limit(1)

for i in record:
    record = i

# Select only the columns containing amenity data
preference_categories = [
    'American restaurant', 'Arcade', 'Art gallery', 'Arts and entertainment',
    'Asian restaurant', 'Bakery', 'Bar', 'Bbq joint', 'Beer store',
    'Bicycle store', 'Bistro', 'Bowling alley', 'Brazilian restaurant',
    'Breakfast spot', 'Brewery', 'Burger joint',
    'Business and professional services', 'Cafe, coffee, and tea house', 'Café',
    'Candy store', 'Car dealership', 'Chinese restaurant', 'Coffee shop',
    'College and university', 'Community center', 'Concert hall',
    'Cultural center', 'Cupcake shop', 'Deli', 'Dentist', 'Department store',
    'Dessert shop', 'Diner', 'Dining and drinking', "Doctor's office",
    'Drugstore', 'Electronics store', 'Falafel restaurant', 'Farmers market',
    'Fast food restaurant', 'Flea market', 'Food court', 'Food truck',
    'Fried chicken joint', 'Garden', 'Gift store', 'Gourmet store',
    'Hardware store', 'Healthcare clinic', 'Hiking trail', 'Hindu temple',
    'History museum', 'Hookah bar', 'Hospital', 'Hotel', 'Housing development',
    'Ice cream parlor', 'Indian restaurant', 'Italian restaurant', 'Juice bar',
    'Korean restaurant', 'Laboratory', 'Lake', 'Lounge',
    'Maharashtrian restaurant', 'Medical center', 'Mobile phone store',
    'Motorcycle dealership', 'Mountain', 'Movie theater',
    'Multicuisine indian restaurant', 'Music venue', 'Night club',
    'North indian restaurant', 'Office building', 'Other great outdoors',
    'Pizzeria', 'Post office', 'Pub', 'Resort', 'Restaurant', 'Retail',
    'Sandwich spot', 'Seafood restaurant', 'Shopping mall', 'Snack place',
    'Soccer field', 'South indian restaurant', 'Southern food restaurant',
    'Spiritual center', 'Stationery store', 'Tea room', 'Temple',
    'Theme restaurant', 'Tobacco store', 'Video games store', 'Water park',
    'Winery'
]

business_keywords = record['Type'] + ' ' + record['keywords']

business_keywords_lower = ""
for char in business_keywords:
    if(char>='A' and char<='Z'):
        business_keywords_lower += chr(ord(char)+32)
    else:
        business_keywords_lower += char

#Removing punctuations
cleaned_text=""
for char in business_keywords_lower:
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

collection = db.amenities_for_businesses

db.required_amenities.delete_many({})
for amenity in extracted_amenities:
    result = collection.find({"Amenity": amenity})
    
    if result:
        for row in result:
            for coords in row['Locations']:
                db.required_amenities.insert_one({'Latitude': coords['latitude'], 'Longitude':coords['longitude']})