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




## Pokemon Identifier
### In order to have our Pokedex identify a Pokemon from an uploaded picture we need a large image collection of Pokemon.  This whole process sounds complicated. Luckily others have done this before.  

### For our data pipeline we need a means of acquiring and classifying Pokemon images.  A quick search found this set of 6,820 cropped and labeled Pokemon. From there we just need to figure out the image classifier code and bundle up whatever comes from that.
---------------------------------------------------------------
### Machine Learning Model 

#### 1) For the data pre-processing in the machine learning model, we uploaded 6,820 images of 150 different Pokemon via Tensorflow ImageDataGenerator.
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN7.png)
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN8.png)

#### 2) The data was split into training/testing sets. 

![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN9_5.png)
#### 3) Feature engineering aspects of our model included several rounds of the activation function ReLU (rectified linear unit) in hidden layer to avoid vanishing gradient problem and increased computation performance , and Softmax function use in last output layer to calculate the probabilities distribution. 
![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN10_5.png)




## Pokemon Characteristics
### In order to be able to retrieve a name with corresponding Pokemon characteristics, we needed to scrape, clean, and make a database.

---------------------------------------------------------------
### Database Integration
#### 1) Data was scraped from https://pokemondb.net/pokedex using pandas, splinter, and BeautifulSoup
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN1.png)

#### 2) Data was cleaned after scraping (I.e. removal of odd characters)
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN1_5.png)

#### 3) Output of data scraping:
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN2.png)

#### 4) We utilized postgres in AWS to store our scraped data:
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN3.png)

#### 5) Using Sqlalchemy, we queried the database to dynamically interface and retrieve specific character information
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN4.png)

#### 6) The data ERD relationships:

![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN12.png)

## Poke-card js / custom elements
-------------------------------------------------------

#### 1) We constructed custom pokemon card using javascript and linked the card to specific Pokemon ID, name, and characteristics using Pokeapi.co (https://pokeapi.co/api/vs/pokemon). 
#### 2) With this script, and to allow us to trigger the card to receive a live and changing image result from the image classifier, we re-constructed the javascript as a custom element. This helped us with streamlined functionality instead of have to make long, nested batches of elements.
![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN13.png)
![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN14.png)
![](https://github.com/cosmicdreams/final_project_group1/blob/develop/app/Resources/JN15.png)

## Pokemon Visualization
--------------------------------------------------------
### Dashboard 
### 1) We deployed a dashboard on herokuapp: 
https://pokedex-bootcamp.herokuapp.com/
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN5.png)
#### 2) With this, the user is able to upload an image of an unknown Pokemon, select the button “Who’s that Pokemon”, and be able to search our image database for a matching Pokemon. The app then retrieves specific information about the identified Pokemon
![](https://github.com/cosmicdreams/final_project_group1/blob/main/app/Resources/JN6.png)

---------------------------------------------------------

# Things we learned

## How to set up Webpack
- Run npm i webpack-cli webpack
- Run webpack-cli init and go through all the prompts. 
- Configure the webpack.config.js to consume the javascript that needs to be compiled, and output the file into the app/static/js folder.
- Run webpack --mode production
- Modify your html file to use the new js at /static/js/main.js

----------------------------------------------------------
# Future Considerations / Ideas
- Save some of the images (if they meet a certain accuracy threshold) and create another app that manually curates them into either allowing them to be in a new training set or to remove them.
- Add a widget to the main app that asks the user to categorize 2 images each time they use the app.
- Separate the app into more granular bits, will increase memory we can use.
- Protect the app from huge incoming files.
- Add more guidance for app usage.
