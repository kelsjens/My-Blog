---
layout: post
title:  "SLC Flight Delays Exploration"
author: Kelson Jensen
description: All of us travel differently. Make sure you don't travel on the wrong days!
image: "/assets/images/SLC_airport.jpg"
---


# _Introduction_ 
In my previous post, we dug into the frustration of flight delays at Salt Lake City International Airport (SLC). Now, we’ll take a closer look at which airlines and which days of the week are the most—and least—reliable. After highlighting a few key findings, I’ll introduce an interactive dashboard so you can explore delay patterns on your own and plan your next trip with confidence.

## _Question_ 
Which airlines and days of the week have the worst delays, and how long are those delays on average?

# _Key Insights_ 
We’re going to quickly highlight a few simple but helpful findings from the data before you dive into the interactive dashboard.

One of the main questions we asked was: Which airline tends to have the worst delays—and which one performs best?
This graph below makes that pretty clear:

<img src="{{site.url}}/{{site.baseurl}}/assets/images/average_delay_time.jpg" alt="Average Delay Time" width="500">
As you can see, Hawaiian Airlines stands out with the longest average delay time by a wide margin.

Before I give away too many insights, I’ll stop here and let you explore the rest for yourself through the Streamlit app I built. Think of this as a teaser to get your brain warmed up and ready to find the travel patterns that matter most to you.

# _Steam lit app_ 
A great way to learn from data is to interact with it directly. That’s why I built a Streamlit app, a simple, interactive dashboard that lets you dive into the flight delay data on your own terms.

<img src="{{site.url}}/{{site.baseurl}}/assets/images/Streamlit_app.jpg" alt="Streamlit App" width="500">
On the left side, you'll find a dropdown menu with different views to explore. You can filter by airline, day of the week, or even combine multiple selections to compare trends side-by-side. This gives you the freedom to explore questions that matter most to you, whether you're curious about which airlines are most reliable on Fridays or how delays vary throughout the day.
This app can be found by clicking [here.](https://flights-app-kelsjens.streamlit.app/) 

# _Data and Execution_ 
This really is something anyone can do with the right steps and knowledge building a streamlit dashboard is quite simple and can help you explore data you are dealing with. I got this data from a website called Aviation Edge, where I got an API to begin my work. You can find that website and get your own API key [Here.](https://aviation-edge.com/) 
If you are looking to folow my code and see how I came up with what I did you can access that in [My Github page](https://github.com/kelsjens/My-Blog/tree/main/_posts). In there you can find the code for my streamlit app that could help you create your own. 

# _Conclusion_
Flight delays are frustrating, but by looking at the data, we can make more informed decisions. This project helped uncover which airlines tend to have the longest delays and how timing affects your chances of staying on schedule. With the Streamlit app, you can dig into these trends yourself and find the options that best suit your travel style.

Whether you just like data or are just planning your next trip, I hope this helps you take off a little more smoothly. And remember travel is amazing even if you have to wait 30 extra minutes for a flight so don't give up going for that. 