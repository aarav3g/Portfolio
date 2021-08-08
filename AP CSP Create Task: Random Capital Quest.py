import random 

#These are the lists which hold the countries and capitals 

country_list = [“U.S.A.”, “Canada”, “Mexico”, “Spain”, “U.K.”, “Portugal”, “France”, “Germany”, “China”, “Russia”, “India”, “Turkey”, “Australia”, “Italy”, “Colombia”, “Iraq”, “Israel”, “Uruguay”, “Panama”, “Brazil”, “Nigeria”, “Saudi Arabia”] 

capital_list = [“Washington, D.C.”, “Ottawa”, “Mexico City”, “Madrid”, “London”, “Lisbon”, “Paris”, “Bonn”, “Beijing”, “Moscow”, “New Delhi”, “Istanbul”, “Canberra”, “Rome”, “Bogota”, “Baghdad”, “Jerusalem”, “Montevideo”, “Panama City”, “Brasilia”, “Abuja”, “Riyadh”] 

#This blank list will hold the players’ names when they enter them in the game 

player_names = [] 

 

#This function manages all of the game’s actions 

def user_guess_capitals (num_questions, num_players, num_attempts): 

#This displays the game’s instructions 

  print “Welcome to Random Capital Quest, where your fate is based on your luck. \nWe will begin with 	practice question, \nduring which you will be asked to state the capital of the randomly selected country. \nChoose an order amongst yourselves, and when the first person has finished their questions, \nthe next one will enter and their name, answer the questions and so forth. \nAfter the practice rounds, a message will state that the actual round has begun and will explain how it works. \nGood luck!” 

  #Loops the entire game based on the number of players 

  for i in range(num_players): 

    #Gets the players’ names 

    player_name = input(“Enter you name: “) 

    print “Welcome, ” + player_name 

    #Adds the players’ names to the “player_names” list 

    player_names.append(player_name) 

      #Loops the questions based on the specified number of questions 

      for i in range(num_questions): 

        #Randomly selects a country 

        country = random.choice(country_list) 

        #Loops through “country_list” to find the index of the selected country 

        for index in range(len(country_list)): 

          if country == country_list[index]: 

            #Initializes “cap_index” as the index of the selected country 

            cap_index = index 

        #States the name of the country 

        print “The country is ” + str(country) + “.” 

        #Initializes “user_guess” as the players’ guess of the capital of the country 

        user_guess = input(“What is the capital of this country? “) 

        #Checks the accuracy of the players’ guess by checking if it’s in the list of capitals 

        #And uses the selected countries’ index to check if the capital at that index is equal to the players’ guess 
  
        #Because both the country and its capital are at the same index in their respective lists 

        if user_guess in capital_list and capital_list[cap_index] == user_guess: 

          #If it is, the players are told they are correct 

          print “That is correct.” 

        elif user_guess not in capital_list and capital_list[cap_index] != user_guess: 

          #If not, the players are told they are incorrect 

          print “That is incorrect.” 

          #This loops through the specified amount of attempts 

          for i in range(num_attempts): 

            #Gives the players the ability to try again 

            user_guess = input(“Try again: “) 

            #Verifies their answers 

            if user_guess == capital_list[cap_index]: 

              #Players are told if their answer is correct 

              print “That is correct.” 

	#This displays an overview of the actual round 

	print “Now it is time for the actual round. \nHere, one player will be randomly selected, \nand will have to recall the country the randomly selected capital is the capital of. \nIf they have the correct answer, they win. If not, everyone else wins. \nGood luck!” 

	#This randomly selects one player from “player_list”, which is comprised of all the players’ names 

	rand_player = random.choice(player_names) 

	#Tells the players who the selected player is 

	print “The selected player is ” + rand_player + “.” 

	#Initializes “rand_capital” to be a randomly selected capital from “capital_list” 

	rand_capital = random.choice(capital_list) 

	#Initializes the player’s guess as “act_user_guess” 

	act_user_guess = input(“What country is ” + rand_capital + “ the capital of? “) 

	#Loops through “capital_list” to find the index of the selected capital 

	for i in range(len(capital_list)): 

		if rand_capital == capital_list[i]: 

			#Initializes “rand_index” as the value of that index 

			rand_index = i 

	#Verifies if the player’s guess is correct by checking if it’s in “country_list” and if the value at the index of the selected capital is equal to the player’s guess 

	if act_user_guess in country_list and country_list[rand_index] == act_user_guess: 

		#If it is, this tells them they have won 

		print  “Congratulations, ” + rand_player + “ you won the game.” 

	else:  

		#If is isn’t, this tells the other players they have won 

		print “Congratulations, other players, you have won the game.” 

	#Ends the game if there is no postive integer value for the number of questions per person 

	if num_question <= 0: 

		break 

	#Ends the game if there are less than 2 players 

	if num_players < 2: 

		print “This game would be more enjoyable with at least 2 people.” 

		break  

 
