import json
import requests

'''
We couldn't figure out how to get the data to display directly onto our html
page so we made an html page describing the project and a link to our code
so users can download and use it.
'''

def Info(symbol):
    '''
    This function retrieves the full company name of the stock symbol that the user entered.
    '''
    data = requests.get('https://financialmodelingprep.com/api/v3/profile/'+str(symbol)+'?apikey=0ddab2ba837ae41d88546a25b5a8d7f2')
    jata = data.json()
    fullname = jata[0]['companyName']
    print('The full name of this company is '+str(fullname))

def Price(symbol):
    '''
    This function retrieves the current price of the stock symbol that the user entered.
    '''
    data = requests.get('https://financialmodelingprep.com/api/v3/quote-short/'+str(symbol)+'?apikey=0ddab2ba837ae41d88546a25b5a8d7f2')
    jata = data.json()
    price = jata[0]['price']
    print('This stock currently costs '+str(price)+' dollars!')

def Rating(symbol):
    '''
    This function retrieves the six different stock ratings of the stock symbol that the user entered 
    and finds the average and if the rating is above 4 we advice the user to buy.
    '''
    data = requests.get('https://financialmodelingprep.com/api/v3/rating/'+str(symbol)+'?apikey=0ddab2ba837ae41d88546a25b5a8d7f2')
    jata = data.json()
    firstscore = jata[0]['ratingDetailsDCFScore']
    secondscore = jata[0]['ratingDetailsROEScore']
    thirdscore = jata[0]['ratingDetailsROAScore']
    fourthscore = jata[0]['ratingDetailsDEScore']
    fifthscore = jata[0]['ratingDetailsPEScore']
    sixthscore = jata[0]['ratingDetailsPBScore']
    rating = (firstscore+secondscore+thirdscore+fourthscore+fifthscore+sixthscore)/6
    print('The average rating of this stock is '+str(rating))
    if rating > 4:
        print('This is a high rating, meaning this stock is currently a good buy.')
    else:
        print('This is not such a high rating, meaning maybe you should wait to buy this stock.')

def Test():
    '''
    This function indexes into some arbitrary data just to see if it can.
    '''
    data = requests.get('https://financialmodelingprep.com/api/v3/quote-short/'+str(symbol)+'?apikey=0ddab2ba837ae41d88546a25b5a8d7f2')
    tata = data.json()[0]['symbol']

'''
The structure of this loop ensures that if the user enters the stock symbol incorrectly the code won't
break and they can keep trying until they get it right.
'''
valid = False
while not valid:
    symbol = input('Enter the symbol of a stock you are curious about (in all caps). ')
    try:
        Test()
        valid = True
    except:
        print('You did not enter a valid stock symbol, try again.')
        valid = False
    else:
        Info(symbol)
        Price(symbol)
        Rating(symbol)
