# Pokedex Assistant 
## by Team Ashe’s Mustache
### A helpful Pokemon assistant for Pokemon Go

#### In Pokemon Lore, there is a Pokedex.  A digital assistant that helps you identify Pokemon and explain the detail about the game.  For our final project in Data Science boot camp we wanted to build a Pokedex that is capable of:

Identifying Pokemon from an image: What’s that Pokemon
•	Uploading an image of an unknown Pokemon
•	Our Machine Learning Model will make an ID to a Pokemon Character
•	Output will include name and confirmation picture with statistics for that character
•	A classic Pokemon card for your viewing pleasure
## Link to Google Slides draft presentation: https://docs.google.com/presentation/d/1TUYjjJdEUT_wmSrtK9HSYktDf_2qKt652W3KmD4fK8A/edit?usp=sharing


To take these three different challenges we need to first gather data.

## Pokemon Identifier
In order to have our pokedex identify a pokemon from an uploaded picture we need a large image collection of pokemon.  This whole process sounds complicated. Luckily others have done this before.  

For our data pipeline we need a means of acquiring and classifying pokemon images.  A quick search found this set of 7000 cropped and labeled pokemon. From there we just need to figure out the image classifier code and bundle up whatever comes from that.

## Pokemon near you
Our goal for the local pokemon suggester is to provide a list of 5 pokemon that can be found near a person’s geographical coordinates.  We could get those coordinates from a browser using HTML 5’s geolocation API.  In order to get pokemon related to geographical data we’re going to need to find Pokemon Go data.

We’ve been able to find what Pokemon can be found in PokemonGo using public datasets.  And we could scrape all the data for ourselves by using the available pokemon go pokedex.  Given how location acts like a filter, we think the features that will drive the recommendation will be CP and availability.  The CP (Combat Points) describes how effective the pokemon is at battle. Availability is how likely it is to find one. 

We want to recommend to include both Pokemon that are likely to be found and are of high value to the user.

## Team Balancer
Similar to the recommendation that the pokedex can give you based on your location.  We’d like the assistant to recommend pokemon that will balance your team.  If you have Pokemon that are all of the same type, have it recommend a different type so you can have the advantage in different kinds of battles.

For this we can reuse much of the same datasets we’ve already gathered.  We just need a means of inputting a user’s current team.
Implementation

Our final deliverable will need:

* A web page
* The ability to upload images.
* The ability to provide your location
* The ability to define the pokemon that are in your team

# Things we learned

## How to set up Webpack
1. Run npm i webpack-cli webpack
2. Run webpack-cli init and go through all the prompts. 
3. Configure the webpack.config.js to consume the javascript that needs to be compiled, and output the file into the app/static/js folder.
4. run webpack --mode production
5. modify your html file to use the new js at /static/js/main.js
