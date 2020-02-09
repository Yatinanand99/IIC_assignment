
import pandas as pd
import re
import matplotlib.pyplot as plt
from textblob import TextBlob
import numpy as np
from collections import Counter

dataset = pd.read_csv("Tweets - Tweets.csv")

def __analysis__(text):
    score = TextBlob(__clean_text__(text))
    texts.append(__clean_text__(text))
    if score.sentiment.polarity > 0:
        analysis.append("positive")
    elif score.sentiment.polarity < 0:
        analysis.append("negative")
    else:
        analysis.append("neutral")
    
def __clean_text__(text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split()) 


def __plot_for_individual_airline__(final_list):
    for i in range(int((len(final_list))/3)):
        explode = (0.1,0,0.1)
        sizes = [new_list[1] for new_list in final_list[(i*3):(i*3)+3]]
        labels = [new_list[0] for new_list in final_list[(i*3):(i*3)+3]]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,explode = explode,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
        ax1.axis('equal')
        file_name = re.split('@',final_list[i*3][0], flags=re.IGNORECASE)[0].capitalize()
        plt.savefig("Output_Images/"+file_name)
        plt.show()

def __plot_for_airlines__(airlines):
    sizes = [new_list[1] for new_list in airlines]
    labels = [new_list[0] for new_list in airlines]
    explode = (0.05,)
    for i in range(len(airlines)-1):
        explode = explode + (0.05,)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    ax1.set_title("Comment % of individual Airlines")
    plt.savefig("Output_Images/All_Airlines_comments.png")
    plt.show()

def __main__(dataset): 
    X = dataset['text']
    airline_name = []
    for i in X:
        airline_name.append(re.search('(?>=@)\w+',i).group(0).lower())
        
    for i in X:
        __analysis__(i)
        
    Y = np.column_stack((airline_name,analysis))
    list_to_work = []
    for i in Y:
        list_to_work.append(i[0]+"@"+i[1])
    
    Z = Counter(list_to_work)
    C = Counter(airline_name)
    
    final_list = list(items for items in Z.items() if items[1]>10)
    airlines = list(items for items in C.items() if items[1]>10)
    
    final_list = sorted(final_list, key=lambda tup: tup[0])
    
    __plot_for_airlines__(airlines)
    __plot_for_individual_airline__(final_list)
 

#Run this piece of code to get various charts regarding the comments
texts = []
analysis = []  
__main__(dataset)





