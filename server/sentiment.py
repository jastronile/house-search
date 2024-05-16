import string
from collections import Counter
import pymongo

database_uri = "mongodb+srv://tanishmodase18:projectcluster@cluster0.wbjdiu1.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(database_uri)

db = client.majorDB

collection = db.feedbacks
record = collection.find().sort("_id", -1).limit(1)

for i in record:
    record = i

text=record['feedback']

#converting to lower text
n=len(text)
lower_text=""
i=0
while i<n:
    if(text[i]>='A' and text[i]<='Z'):
        lower_text+=chr(ord(text[i])+32)
    else :
        lower_text+=text[i]
    i=i+1


#Removing punctuations
cleaned_text=""
for char in lower_text:
    if(char>='A' and char<='Z' or char>='a' and char<='z' or ord(char)==32):
        cleaned_text+=char

#Tokenization
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


#stop words
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
    if( word not in stop_words):
        tokens.append(word)

print(tokens)

emotions_list=[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(",",'').replace("'","").strip()
        word,emotion=clear_line.split(":")
        if word in tokens:
            emotions_list.append(emotion)

emo_count=Counter(emotions_list)
emo=''
maxi=0
for s,n in emo_count.items():
    if n>maxi:
        emo=s
        maxi=n

print("Emotion from the feedback is "+emo)