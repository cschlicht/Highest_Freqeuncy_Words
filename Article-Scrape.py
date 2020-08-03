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
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.transform import dodge
from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar
from nltk.corpus import wordnet as wn
import nltk

option = webdriver.ChromeOptions()
option.add_argument("- incognito")


browser = webdriver.Chrome(executable_path= r"C:\Users\servi\OneDrive\Documents\Side_Projects\Article_Scraper\chromedriver", chrome_options=option)


#Get the desired website
browser.get("https://www.nytimes.com/topic/destination/united-states")

#Wait 10 seconds for the page to load
time.sleep(10)

#try:
  #  WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '//img[@class="avatar width-full rounded-2"]')))
#except TimeoutException:
 #   print('Timed out waiting for page to load')
  #  browser.quit()

for y in range(0, 9):
    #Finding the show more button
    SM_Button = browser.find_elements_by_xpath('//button[text() = "Show More"]')
    #Click show more button
    SM_Button[0].click()
    #Allow time for website to load the content into the HTML
    time.sleep(5)





# find_elements_by_xpath returns an array of selenium objects.
titles_element = browser.find_elements_by_xpath('//h2[@class="css-1j9dxys e1xfvim30"]')
# use list comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
# print out all the titles.
#print('titles:')
#print(titles, '\n')


browser.get("https://www.cnn.com/specials/last-50-stories")

titles_cnn = browser.find_elements_by_xpath('//span[@class="cd__headline-text"]')

titles_2 = [x.text for x in titles_cnn]









database.deleteAll()



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

for x in range(0, len(titles)):
    words.append(titles[x].split(" "))
    
for x in range(0, len(titles_2)):
    words.append(titles[x].split(" "))

for y in words:
    for n in y:
        database.insert(n) 


count = 0
for n in database.viewOccurences():
    d = {}
    
    if isValid(n[0]) == False:
        continue
    d["Word:"] = n[0]
    d["Occurrences:"] = n[1]
    l.append(d)
    #count = count + 1
    #if count == 300:
      #  break


#word = []
#occurrences = []
#for n in database.viewOccurrences():
    
#    word.append(n[0])
 #   occurrences.append(n[1])


#print(len(word))
#print(occurrences)

l = sorted(l, key = lambda i: i['Occurrences:'], reverse=True)
print(l)
df = pandas.DataFrame(l)
df.to_csv("data.csv")

 
x = df["Word:"]
y = df["Occurrences:"]


#print(l)

p = figure(x_range=x, plot_height=500, plot_width = 35000, title="Word Occurences",
           toolbar_location=None, tools="")

p.vbar(x=x, top=y, bottom = 0, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

output_file("plot.html")

show(p)










