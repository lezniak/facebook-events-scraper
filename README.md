# facebook-events-scraper
### General info
The script allow to take out localization(city,road),date(YMD,hour) and the name from event url.
You can use it to your program to easy extract this data. As you know that facebook blocks typical Web Scraper.
My scraper download source from link and then looking for keywords. That way you can find this all things.
You can easily edit program and add yours things to search.

#### The example input and output:
Input: `http://www.facebook.com/events/2621820714730350`<br />
Output:`['Rybnik', 'Wiejska 1A', '2020-12-26', '21:00:00', 'I.GOT.U w Rybniku - Mega gwiazda w Face 2 Face']`
	
### Technologies
Project is created with:
* Python 3.6.9
	
### Setup
To run this project, you have to install:

```
$ pip install requests
$ git clone https://github.com/lezniak/facebook-events-scraper.git
```
### How to use

When you clone this project you have to fill the text file named 'links.txt' in with links one by one and then start with
```
python3 Apk.py
```
When the program exits, in folder should shows new txt file named 'result.txt' with expected result

ENJOY :)

P.S. I tested this program on english fb version.
