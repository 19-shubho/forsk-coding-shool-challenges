import pandas as pd

#read the csv file
dataFrame = pd.read_csv('ign.csv')

#rate > 7 in xbox one filter out
XBO7=(dataFrame["score"]>7)&(dataFrame["platform"]=="Xbox One")

reviews=dataFrame[XBO7]

XBOfinal=reviews['title']

print(XBOfinal)


#XBOX ONE reviews...........
xBOX=dataFrame['platform']=="Xbox One"

xBOXdF=dataFrame[xBOX]

xBOXreview=xBOXdF['score_phrase']

xBOXreview.hist(bins=20,grid=False,xrot=90)

#PLAYSTATION FOUR reviews............
PS4=dataFrame['platform']=="PlayStation 4"

PS4df= dataFrame[PS4]

PS4review = PS4df['score_phrase']

PS4review.hist(bins=20, grid=False, xrot=90)

