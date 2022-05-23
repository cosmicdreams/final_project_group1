# Generate a Pokemon Card that draws info from PokeAPI.co
## Fetch Data
### Build the Card using index.html and style.css:
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image1.png)

![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image2.png)
### - Link the Card to Pokeapi.co https://pokeapi.co/api/v2/pokemon/
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image3.png)
API Source:
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image4.png)
### - Define constant variables using document.getElementById for “card” and “btn” (the button) 
### -Initiates the callback that will be invoked with the btn (button) is “clicked”, and performs function: getPokeData.  We then defined the function for retrieving the pokemon from the API (using getPokeData). First, we decided to use a formula to draw a random Pokemon (by ID) from the Pokeapi.com database. We then created a variable (finalUrl) which held the PokeAPI url + the random caller (using the random Pokemon ID). We finally used .fetch to retrieve the callback ‘then.response’ and extract the data in .json (this includes ALL data -height, id, moves, etc). 
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image5.png)
## We will derive our live application Pokemon ID from our Image Classifier TBD…

-----------------------------------------------------------------------------------------------------------------------------------
## Generate and Style Card
### Const typeColor to match each Pokemon type to a Color to display on the card:
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image10.png)
### Defined themeColor to equal the typeColor and the Pokemon ID using stats retrieved in Console (see below for derivation of the const hp (which was composed of data.stats[0].base_stat
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image6.png)
![](https://github.com/Beetleee/Credit_Risk_Analysis/blob/main/Resources/image7.png)
