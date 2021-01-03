# text cleaning
# create a text file and open the text file
# convert the text file into a lowercase
# remove the panctuation like .,@! etc

import string
from collections import Counter
import matplotlib.pyplot as plt

myText = open("mytext.txt", encoding='utf 8').read()
# print(myText)
myText_lower=myText.lower()
#print(myText_lower)
# print(string.punctuation)
cleaned_myText=myText_lower.translate(str.maketrans('','',string.punctuation))
#print(cleaned_myText)


# tokenized and removed stop words like i,we,they etc
tokenized_words=cleaned_myText.split()
# print(tokenized_words)

stop_words= ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words=[]
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)

# NLP Algoriothm

# 1. check if the word in final_words list is also available in emotions.text or not
# 2. if word is present add the word in emotion list
# 3. finaly count each emotion in the emotion list

emotion_list=[]
with open("emotions.txt",'r') as file:
    for line in file:
        clear_line =line.replace("\n",'').replace(",",'').replace("'",'').strip()
        # print(clear_line)
        word,emotion=clear_line.split(':')
        # print("word :"+ word + " , " + "Emotions :" + emotion)
        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)

emotion_counter=Counter(emotion_list)
print(emotion_counter)

fig,ax1=plt.subplots()
ax1.bar(emotion_counter.keys(),emotion_counter.values())
fig.autofmt_xdate()
plt.savefig("myImage.png")
plt.show()