# Web Scraping Monster.com using Scrapy with JSON APIs

Today, we will be web scraping monster.com using scrapy with JSON APIs. We would be taking the Job Title as **“Product Manager”** and Location as **“USA”**.

![alt text](https://cdn-images-1.medium.com/max/1200/1*bGNqByOzzc7Clx0p_ObHLA.jpeg)

We will be using Python with **scrapy** and **BeautifulSoup** in this exercise. Go to your **terminal**, I’m using **Anaconda Prompt** on Windows. Go to your desired directory. Once you are there type this in the terminal :
```
scrapy startproject monster
```
![alt text](https://cdn-images-1.medium.com/max/800/1*mKC6BRHmSibC0B1YDeS1tQ.jpeg)
```
scrapy genspider monster-spider monster.com
```
Your spider is created!! Now go to the directory scrapy/monster/monster/spiders. Open monster-spider.py in your favorite editor, which will give you the basic template of the spider. I use Visual Studio Code as my editor.

![alt text](https://cdn-images-1.medium.com/max/800/1*m_SiAfqk_e0dQsiYU0fzzg.jpeg)

