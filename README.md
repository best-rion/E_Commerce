# E_Commerce

A full featured E-commerce website with Frontend, Backend and Database using Python Flask.

A few days ago I followed a tutorial from a youtuber named Corey Schafer, and followed the Flask tutorial step by step and completed the series.

After completing the tutorial I decided to try out my skill and started this project on my own. I stucked many times, watched the videos again for particular problems that I faced in this project.
I learned many new things, jQuery being one of them. Let me tell you the context about jQuery. In flask, the website reloads everytime a post request is sent. For better User Experience I decided to post "Add to cart" action using jQuery. jQuery allows us to send post request without reloading the page each time. I am new to backend and I am still learning.


And there is more. This E-commerce website, I decided to make it a watch shop, just randomly. To make it look like a real E-commerce site, I scrapped thumbnails, names, prices and images from "timezonebd.com", saved informations in JSON file and saved images in "static/images/" folder.
I used Sqlite database for this project, simply because it is my first time with database and I watched it on the tutorial. 

There is again one more challenge I faced while trying to modify the model. The thing is, at first I made 'name' column with unique constrain. Later I had to change the constrain, but it is very difficult to change constrains in Sqlite DB. So in a forum, I found a solution, Sqlite DB Browser. It is basically a GUI for Sqlite database and very helpful. I changed the unique constrain easily with its help.
