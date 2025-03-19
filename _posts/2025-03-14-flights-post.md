---
layout: post
title:  "Exploration of Least Delayed Airlines"
author: Kelson Jensen
description: Flight Delays Make No Ones Days
image: "/assets/images/airplane.jpg"
---


# _Introduction_ 
How many of us have had our flights delayed in an airport? Is there anything more frustrating than wanting to go on an amazing trip and when you're about to leave your flight is delayed 1, 2, or maybe even 24 hours? In this post we will explore what airlines lead to the largest average time of delayed flights, what percentage of flights are delayed based on the airline, and we will explore what days of the week cause the most delayed flights. All of this data will be based on the month of May at the SLC airport in 2024. To find this data we will use an API and with that take categories such as date, minutes delayed, airline, days of the week, and more. Lets find out some easier stress free ways to travel!

# _Data Collection_ 
Creating this dataset involved a few key steps, the API used was from [Aviation Edge](https://aviation-edge.com/)

- Get API Access – I used the Aviation Edge API to pull flight data. You’ll need to sign up for an account and get an API key which I had to get from emailing them and getting one. They also told me this was also public data and useable.

- Make API Requests – Using Python, I requested flight data for Salt Lake City (SLC) airport in May 2024. The API returned details like airline, scheduled time, actual time, and delay duration.

- Clean the Data – The raw data included extra information, so I filtered it to only keep relevant columns like airline, expected time, actual time, and flight date. I also removed missing values.

- Added Data - I took the times of expected and actual departure times and created a new variable that is called delay time that is the number of minutes of delay time from each flight. 

- Save the Data – To avoid making repeated API requests, I saved the cleaned dataset as a CSV file for analysis.

- Analyze Flight Delays – I explored which airlines had the longest average delays, what percentage of flights were delayed by more than 10 minutes, and how delays varied by day of the week.

By doing this I was able to make an easy dataset with which I could run some EDA on what I wanted to know from the introduction.

# _Airline Priority_ 
Some of us greatly value a dependable airline that is going to take off at the right time which in turn gets us to our destination at the right time. This is greatly important to those that have small layovers or schedules to keep. Not all airlines are the same when it comes to how often or how long they are delayed. If you are looking for an airline with the smallest percentage of delayed flights and shortest delays it would be wise to avoid Hawaiian airlines. If you want reliability then your best bet is definitely Alaskan or Delta. 
The chart below shows the average time of delay of a given airline. 
<img src="{{site.url}}/{{site.baseurl}}/assets/images/average_delay_time.jpg" alt="Average Delay Time" width="500">

The following chart shows what percentage of flights are delayed by each airline by 25 minutes or more. 
<img src="{{site.url}}/{{site.baseurl}}/assets/images/percent_delayed.jpg" alt="Percentage of Delayed Flights" width="500">

# _Day of the Week factor_
When we decide to go somewhere we have to think about when we want to leave. Sometimes the day of the week can have a greater effect than you might think. In a general sense the best day to travel is you are looking to avoid delays you should look to travel on Sundays. However, this varies a lot based on what airline you may choose to travel with. Some of the things that we will look at is which airline is the best on which days. 
This chart is a heatmap of the days of the week by airline and the average proportion of flights with delays over 25 minutes. 
<img src="{{site.url}}/{{site.baseurl}}/assets/images/dayofweek_flights.jpg" alt="Days of the Week" width="500">


# _Conclusion_
Looking at some of the things we learned from this. First, if you are looking for an airline that is going to give you the most assurance that your flight will be on time you should go with Alaskan airlines. Second, if you are thinking about the day of the week you want to travel, you should go with Sunday to encounter the least delays. The best case scenerio that you could find yourself in is going with Alaskan airlines on either a Monday or Wednesday. Lastly the worst case scenerio would be to book with Hawaiian airlines on a monday, which on average your flight will be delayed about 60% of the time. 


The code used for this post can be found on [My Github page](https://github.com/kelsjens/My-Blog/tree/main/_posts).
This data was collected from [Aviation Edge](https://aviation-edge.com/). 