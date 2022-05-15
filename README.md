# Team-Ashe's Mustache  - Technology.md Document
### Chris Weber, Elder Arias, Terra Lasho, Pierre Boucard, and Thaofeeqat Dauda
## Introduction: 
- This document provides a checkpoint, a first ‘planned sketch’ including a brief description of our technological intentions as we navigate this project.  So far, our group has narrowed down project ideas to 2, and as we continue this week to our final choice, we will delineate the needs/pathway for each below:
### Project:  Pokedex Assistant: A helpful Pokemon assistant for Pokemon Go

### Summary:
- In Pokemon Lore, there is a Pokedex.  A digital assistant that helps you identify Pokemon and explain the detail about the game.  For our final project in Data Science boot camp we wanted to build a Pokedex that is capable of:

#### Identifying Pokemon from an image: What’s that Pokemon
#### Suggest Pokemon to look out for near you.
#### Take a look at your roster, and suggest a Pokemon that would improve your team.

- To take these three different challenges we need to first gather data.

## Technologies Used:
-	Software: Jupyter Notebook, and Python 3.7.9
-	Python libraries:
- Numpy
- Pandas
- Seaborn (violin, factorplot, heatmap)
- Matplotlib
- Graphvis (for graphic visualization)
- Scikit-Learn

## Data Analysis and Pipeline Design:
### Pokemon Identifier
In order to have our pokedex identify a pokemon from an uploaded picture we need a large image collection of pokemon.  This whole process sounds complicated. Luckily others have done this before [!]https://github.com/victoria-lo/image-classifying-pokedex.  

For our data pipeline we need a means of acquiring and classifying pokemon images.  A quick search found this set of 7000 cropped and labeled pokemon.[!]https://www.kaggle.com/datasets/lantian773030/pokemonclassification From there we just need to figure out the image classifier code and bundle up whatever comes from that.

### Pokemon near you
- Our goal for the local pokemon suggester is to provide a list of 5 pokemon that can be found near a person’s geographical coordinates.  We could get those coordinates from a browser using HTML 5’s geolocation API.  In order to get pokemon related to geographical data we’re going to need to find Pokemon Go data.

- We’ve been able to find what Pokemon can be found in PokemonGo using public datasets.  And we could scrape all the data for ourselves by using the available pokemon go pokedex.  Given how location acts like a filter, we think the features that will drive the recommendation will be CP and availability.  The CP (Combat Points) describes how effective the pokemon is at battle. Availability is how likely it is to find one. 

- We want to recommend to include both Pokemon that are likely to be found and are of high value to the user.
### Team Balancer
- Similar to the recommendation that the pokedex can give you based on your location.  We’d like the assistant to recommend pokemon that will balance your team.  If you have Pokemon that are all of the same type, have it recommend a different type so you can have the advantage in different kinds of battles.

- For this we can reuse much of the same datasets we’ve already gathered.  We just need a means of inputting a user’s current team.
### Implementation
Our final deliverable will need:

- A web page
- The ability to upload images.
- The ability to provide your location
- The ability to define the pokemon that are in your team

