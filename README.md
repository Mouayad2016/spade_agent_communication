# spade_agent_communication


Getting started:
Student advertising agency want a program to show the top 10 university in the word by using an official dataset, the data set considers of year, rank, name, point, city, and country. 
You can find reference to the data blow. 
The requester wants a program working with a multi-agent system, using XMPP instant messaging. 
For that I used SPADE Agent, a multi-agent systems platform written in Python and based on instant messaging (XMPP).
How it works?  
it’s simple! we have tow agents a sender and a receiver, sender read the data from CSV file and send it to the receiver by in coding it to JSON since FCM instant messaging only accept strings so by that the receiver agent need to handle the data and do some calculations.
And the calculations are:
-	Get all years top university by rank.
-	Get 2022 top 10 university by rank.
-	Get 2022 worst 10 university by rank.
UML
 by @Mouayad Mouayad
References: 
-	https://www.kaggle.com/datasets/mylesoneill/world-university-rankings
