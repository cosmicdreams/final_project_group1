# Pokedex Assistant 
## by Team Ashe’s Mustache
### A helpful Pokemon assistant for Pokemon Go

#### In Pokemon Lore, there is a Pokedex.  A digital assistant that helps you identify Pokemon and explain the detail about the game.  For our final project in Data Science boot camp we wanted to build a Pokedex that is capable of:

#### Identifying Pokemon from an image: What’s that Pokemon
- Uploading an image of an unknown Pokemon
- Our Machine Learning Model will make an ID to a Pokemon Character
- Output will include name and confirmation picture with statistics for that character
-	A classic Pokemon card for your viewing pleasure
## Link to Google Slides draft presentation: https://docs.google.com/presentation/d/1TUYjjJdEUT_wmSrtK9HSYktDf_2qKt652W3KmD4fK8A/edit?usp=sharing


To take these three different challenges we need to first gather data.

## Pokemon Identifier
#### In order to have our pokedex identify a pokemon from an uploaded picture we need a large image collection of pokemon.  This whole process sounds complicated. Luckily others have done this before.  

#### For our data pipeline we need a means of acquiring and classifying pokemon images.  A quick search found this set of 6,820 cropped and labeled pokemon. From there we just need to figure out the image classifier code and bundle up whatever comes from that.
---------------------------------------------------------------
### Machine Learning Model 

#### 1) For the data pre-processing in the machine learning model, we uploaded 6,820 images of 150 different Pokemon via Tensorflow ImageDataGenerator.
JN7.png
JN8.png
##### 2) Feature engineering aspects of our model included several rounds of the activation function ReLU (rectified linear unit) in hidden layer to avoid vanishing gradient problem and increased computation performance , and Softmax function use in last output layer to calculate the probabilities distribution. 
JN9.png
#### 3) We used 20 epochs
JN10.png
#### 4) The accuracy of the model was: 66%
JN11

## Might need to further articulate:
-	Description of how data was split into training and testing sets
-	Description of how the model was trained (or retrained, if the team is using an existing model)

## Pokemon Characteristics
#### In order to be able to retrieve a name with corresponding Pokemon characteristics, we needed to scrape, clean, and make a database.

---------------------------------------------------------------
### Database Integration
#### 1) Data was scraped from https://pokemondb.net/pokedex using pandas, splinter, and BeautifulSoup
JN1.png
#### 2) Data was cleaned after scraping (I.e. removal of odd characters)
JN1_5
#### 3) Output of data scraping:
JN2.png
#### 4) We utilized postgres in AWS to store our scraped data:
JN3.png
#### 5) Using Sqlalchemy, we queried the database to dynamically interface and retrieve specific character information
JN4.png

## (INSERT ERD WITH RELATIONSHIPS)

## Pokemon Visualization

### Dashboard 

#### We deployed a dashboard on herokuapp: 
https://pokedex-bootcamp.herokuapp.com/

JN5.png

#### With this, the user is able to upload an image of an unknown pokemon, select the button “Who’s that Pokemon”, and be able to search our image database for a matching pokemon. The app then retrieves specific information about the identified pokemon

JN6.png

---------------------------------------------------------

# Things we learned

## How to set up Webpack
1. Run npm i webpack-cli webpack
2. Run webpack-cli init and go through all the prompts. 
3. Configure the webpack.config.js to consume the javascript that needs to be compiled, and output the file into the app/static/js folder.
4. run webpack --mode production
5. modify your html file to use the new js at /static/js/main.js
