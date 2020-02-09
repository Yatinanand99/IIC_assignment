# IIC_assignment

I was given 2 tasks that were as follows:
0. Sentiment Analysis from given text and then giving insights from the data collected
1. Analysis of any Youtube channel

# Task 0:
 
 The text was first cleaned by Python regex (re library) which was various tools to perform on texts.
 
 Sentiment Analysis was done by TextBlob python library which is very effective in giving the polarity of sentiments on text which is positive if the sentiment is positive and negative if the sentiment is negative and 0 if sentiment is neutral.
 
 So the Sentiment Analysis was performed on various comments and they are tagged as Positive, Negative and Neutral.
 
 Then various graphs are plot to study various results which are inside Output_Images folder.
 
 From Output it can be seen that:
 1. US airways is least liked by people with very high 30.9% negative comments
 2. Virgin America is most liked by people with 44.0% positive comments
 3. United airlines is highly preferred by people with very high comments percentage of all 26.1%
 4. JetBlue and SouthWest Air is very preferable airlines with decent ratio of comments and high positive comments or feedbacks
 5. American Airways is a decent airline with all positive comments and percentage share is equally likely.
 
# Note: 

All these are Sentiments from Machines and can be trusted at a certain level only.

# Task 1:

The Youtube Channel I chose was NadeKing which makes videos on CS:GO game and is highly famous among the gamers.

The output of the Mining can be seen in Output folder and also the script is model.py to make appropriate changes, but one has to use its own Youtube Data API which is restricted to be shared on public repository.

The output results shows that the channel is highly active and is gaining more likes over time and the trend of dislikes is also falling over time. The views of the videos is almost constant and which is a very good sign for consistency of the channel
