'''
This python program will take a file of dehydrated tweets and return the first n tweet ids where n is the user's chosen subset length. To use this program, download it from Github and store it in your twarc utilities file. 

Usage: python utils/subset.py 


Takes user input of the following:

tweets - The name of the original tweet id file you'd like to take a subset of. This should be entered without quotes. Example user input: nh_ids.txt
subset - The name of a file you would like the subset ids to output to. The file doesn't have to exist prior as it will be created. Example user input: nh_sub_tweets.txt
length - The length you'd like your subset to be. Example user input: 20000

Each id must be on a separate line in the original tweet file for this to work. The program reads line by line. 
'''

# getting user input 
tweets = input("Enter the name of your tweet ids file: ")
subset = input("Enter the name of the output tweet ids file: ")
length = int(input("Enter the number of tweets you would like to subset: "))

# open both files
with open(tweets, 'r') as firstfile, open(subset, 'a') as secondfile:
        # set i as the number of tweet ids you would like to transfer
        for i, line in enumerate(firstfile):
                if i == length:
                        # if the number of lines is 20000, break
                        break
                else:
                        # if it isn't keep adding
                        secondfile.write(line)

# close both files
firstfile.close()
secondfile.close()

