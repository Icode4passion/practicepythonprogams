print("Know your Zodiac Sign")
def Zodiac(month):
	dic = {
		'january':'Aquarius','february':'Pisces','march':'Aries','april':'Taurus','may':'Gemini','june':'Cancer','july':'Leo','august':'Virgo','september':'Libra','october':'Scorpio',
		'november':'Sagittarius','december':'Capricorn'}
	if mnt in dic:
		print ("**{}** is your Zodiac Sign for {} month".format(dic[month],month))
	else :
		print ("Please Enter a valid month")

month = input("Please enter the Month of your Birth : \n")
mnt = str.lower(month)
Zodiac(mnt)
print ("Thanks for using our Zodic Table")