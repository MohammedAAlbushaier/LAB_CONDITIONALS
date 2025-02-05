#Create a variable for the movie (choose any movie you like)
movie:str= "immortals"

#Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rating: int= 3

#Create a popularity score of type float , let it be 72.65
popularity:float= 72.65

#Using an if statement
# Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rating >=4 and popularity>80:
    print ("The Movie is highly recommended you watch the "+movie)

#else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it .
# It is good"
elif rating >=3 and popularity> 70:
    print("I recommended you watch the "+movie +" . It is good")

#else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
elif rating <= 2 and popularity> 60:
    print ("You should check out the "+movie+"!")
#else the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
else :
    print("Don't watch the "+movie+". It is a waste of time")

'''
this is the LAB_CONDITIONALS Bonus 
Feb5, 2025
By Mohammed Albushaier
'''
