from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas
import database
#from bokeh.core.properties import value
#from bokeh.io import show, output_file
#from bokeh.models import ColumnDataSource
#from bokeh.plotting import figure
#from bokeh.transform import dodge
#from bokeh.io import curdoc, show
#from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#set up options for our chrome browser
option = webdriver.ChromeOptions()
option.add_argument("- incognito")
option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')


browser = webdriver.Chrome(executable_path= r"C:\Users\servi\Documents\SideProjects\Highest_Freqeuncy_Words\chromedriver", chrome_options=option)


#Get the desired website
browser.get("https://www.nytimes.com/topic/destination/united-states")

#Wait 3 seconds for the page to load
time.sleep(3)

#finds and clicks the show more button the max amount of times the website will allow so we can get the most titles possible
for y in range(0, 9):
    #Finding the show more button
    SM_Button = browser.find_elements_by_xpath('//button[text() = "Show More"]')
    #Click show more button
    SM_Button[0].click()
    #Allow time for website to load the content into the HTML
    time.sleep(3)




# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath('//h2[@class="css-1j9dxys e1xfvim30"]')
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
#print('titles:')
#print(titles, '\n')


#extract titles from cnn
browser.get("https://www.cnn.com/specials/last-50-stories")

titles_cnn = browser.find_elements_by_xpath('//span[@class="cd__headline-text"]')

titles_2 = [x.text for x in titles_cnn]



#extract titles from usatoday
browser.get("https://www.usatoday.com/news/")

titles_usa = browser.find_elements_by_xpath('//div[@class="gnt_m gnt_m_flm"]')

titles_3 = [x.text for x in titles_usa]

#delete all data in the database for a fresh start
database.deleteAll()

#invalid words
def isValid(str):
    if(str.lower() == "the"):
        return False
    if(str.lower() == "of"):
        return False
    if(str.lower() == "to"):
        return False
    if(str.lower() == "is"):
        return False
    if(str.lower() == "a"):
        return False
    if(str.lower() == "in"):
        return False
    if(str.lower() == "the"):
        return False
    if(str.lower() == "how"):
        return False
    if(str.lower() == "and"):
        return False
    if(str.lower() == "will"):
        return False
    if(str.lower() == "as"):
        return False
    if(str.lower() == "it"):
        return False
    if(str.lower() == "on"):
        return False
    if(str.lower() == "why"):
        return False
    if(str.lower() == "a"):
        return False
    if(str.lower() == "was"):
        return False
    if(str.lower() == "are"):
        return False
    if(str.lower() == "more"):
        return False
    if(str.lower() == "for"):
        return False
    if(str.lower() == "after"):
        return False
    if(str.lower() == "than"):
        return False
    if(str.lower() == "its"):
        return False
    if(str.lower() == "you"):
        return False
    if(str.lower() == "my"):
        return False
    if(str.lower() == "this"):
        return False
    if(str.lower() == "that's"):
        return False
    if(str.lower() == "could"):
        return False
    if(str.lower() == "at"):
        return False
    if(str.lower() == "an"):
        return False
    if(str.lower() == "have"):
        return False
    if(str.lower() == "like"):
        return False
    if(str.lower() == "no"):
        return False
    if(str.lower() == "what"):
        return False
    if(str.lower() == "de"):
        return False
    if(str.lower() == "al"):
        return False
    if(str.lower() == "y"):
        return False
    if(str.lower() == "la"):
        return False
    if(str.lower() == "not"):
        return False
    if(str.lower() == "still"):
        return False
    if(str.lower() == "our"):
        return False
    if(str.lower() == "can"):
        return False
    if(str.lower() == "says"):
        return False
    if(str.lower() == "about"):
        return False
    if(str.lower() == "with"):
        return False
    if(str.lower() == "into"):
        return False
    if(str.lower() == "Here's"):
        return False
    if(str.lower() == "come"):
        return False
    if(str.lower() == "be"):
        return False
    if(str.lower() == "un"):
        return False
    if(str.lower() == "That's"):
        return False
    if(str.lower() == "en"):
        return False
    if(str.lower() == "met"):
        return False
    if(str.lower() == "may"):
        return False
    if(str.lower() == "who"):
        return False
    if(str.lower() == "some"):
        return False
    if(str.lower() == "that"):
        return False
    if(str.lower() == "..."):
        return False
    if(str.lower() == "se"):
        return False
    if(str.lower() == "debemos"):
        return False
    if(str.lower() == "in."):
        return False
    if(str.lower() == "don't"):
        return False
    if(str.lower() == "too"):
        return False
    if(str.lower() == "we're"):
        return False
    if(str.lower() == "'that's"):
        return False
    if(str.lower() == "here's"):
        return False
    return True


words = []
l = []

#clean up the text
for x in range(0, len(titles)):
    titles[x] = titles[x].replace("\n", " ")
    titles[x] = titles[x].replace("?", "")
    titles[x] = titles[x].replace("-", "")
    titles[x] = titles[x].replace("'", "")
    titles[x] = titles[x].replace(".", "")


for x in range(0, len(titles)):
    words.append(titles[x].split(" "))
    
#clean up the text
for x in range(0, len(titles_2)):
    titles_2[x] = titles_2[x].replace("\n", " ")
    titles_2[x] = titles_2[x].replace("?", "")
    titles_2[x] = titles_2[x].replace("-", "")
    titles_2[x] = titles_2[x].replace("'", "")
    titles_2[x] = titles_2[x].replace(".", "")

for x in range(0, len(titles_2)):
    words.append(titles_2[x].split(" "))


#usa has some formatting issues when you webscrap the titles so these lines fix it
for x in range(0, len(titles_3)):
    titles_3[x] = titles_3[x].replace("\n", " ")
    titles_3[x] = titles_3[x].replace("?", "")
    titles_3[x] = titles_3[x].replace("-", " ")
    titles_3[x] = titles_3[x].replace("'", "")
    titles_3[x] = titles_3[x].replace(".", "")

for x in range(0, len(titles_3)):
    words.append(titles_3[x].split(" "))
    
print(words)


for y in words:
    for n in y:
        if isValid(n[0]) == False: #if the word isn't a valid word, skip it. this prevents the bad words from entering the database in teh first place
                                   #(potential time saver) 
            continue
        database.insert(n) 



#count = 0 
for n in database.viewOccurences():
    d = {}
    
    
    d["Word:"] = n[0]
    d["Occurrences:"] = n[1]
    l.append(d)
    #count = count + 1
    #if count == 300:
      #  break




l = sorted(l, key = lambda i: i['Occurrences:'], reverse=True)
#print(l)
df = pandas.DataFrame(l)
df.to_csv("data.csv")

 
x = df["Word:"]
y = df["Occurrences:"]



database_words = database.viewOccurences()
text = " ".join([(k[0] + " ")*k[1] for k in database_words]) #this must be done for the word cloud to work, essentially turns (word, 3) into word word word




wordcloud = WordCloud(max_font_size=80, collocations = False, height= 700, width = 700 ).generate(text) 
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

#doesn't actually close the entire brower, just the tab that we are on
browser.close()
 #TODO: look up a way to close the entire browser for a more streamlined process
#TODO: find out why its so slow
#TODO: if you have time, create a system that you can select or type in the word and it returns all the articles with that word in the title


#bar graph for words (fuck this, too slow + looks bad)
r'''
p = figure(x_range=x, plot_height=500, plot_width = 35000, title="Word Occurences",
           toolbar_location=None, tools="")

p.vbar(x=x, top=y, bottom = 0, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

output_file("plot.html")

show(p)

'''








