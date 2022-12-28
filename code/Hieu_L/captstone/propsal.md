# Project Overview
I am wanting to build a game, using django as my framework. The application itself will be more than a game, but will allow the user to interact their "character" in the game. The user will be able to equip gear, manage inventory, and fight AI enemies with their in-game "character".

# Functionality
I will be using django framework to have multiple routes. one page to manage the character's inventory, one page to view equipped items, and one page for the character to do the 'battle'. I will use HTML to display the pages, bootstrap to style, and python to write the functionality of the page. 

One the "equipment" page plaers will be able to see the items they have equipped to their character along with an attach and defense number, signifying their strength in combat. 

on the inventory page, players will be able to compare stats of equipped items and other items that are inside of their 'backpack' 

fianlly a battle page, where the players will fight 'AI' enenmies. ultimately it will be very simple, the fighting will take place using the attach and defense numbers mentioned before. Using python i will write a funtion to calculate the higher damage number between the player's character and a randomly generated player. this page will use two functions, 1 for the actual battle and one to generater an enemy using the player class and item class.

# data model
i will have to have multiple data models for the project. 
- one data model for the character
    - what equipment can be equiped to the   character
    - total strength
    - total defense
- data model for the items
    - defense and attack number
    - where it equips to character (like chest armor on their chest, arm armor on their arm, etc.)

these classes will be able to be accessed by the function to generate random enemy players with random equipment. 

I will be using a library type database to store a completed list of 'equipment'. similar to the commerce store application, i will use the equipment data model to generate a library of equipmnent with specific states. 

could use javascript for api calls to have images for the  equipment similar to the drinks api lab, but want functionality via python functions first
# schedule

- create routes for the pages
- create data models 
- create sample library of 1 player and 1 item for each region (arms, legs, chest, sword, shield)
- create functionality of 'equiping' items, stats add up, registers proper status numbers
- create front end display of character and equipment, create front end functionality of equip function
- create random player generator using the models for equipments and player
- create fight functionality
- create front end display for fight function

2 tasks per week minumum