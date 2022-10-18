import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = "https://wikitravel.org/en/Special:Random"

    article_page = requests.get(url)
    soup = BeautifulSoup(article_page.text, "html.parser")
    title = soup.find(class_="firstHeading")
    print("===================================================\n")
    print("Do you want to view your new travel destination(Y/N)")
    print("===================================================\n")
    ans = input("").lower()
    if ans == "y" or ans == "yes" or ans == "YES":
        webbrowser.open(url)
        break
    elif ans == "n" or ans == "no" or ans == "NO":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break