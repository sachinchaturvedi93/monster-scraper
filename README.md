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

Let’s try out the basic spider now. Go to your terminal and type :
```
scrapy crawl monster-spider
```
![alt text](https://cdn-images-1.medium.com/max/800/1*gbAS2WeFQFYizyvCAD23ng.jpeg)

The output would be something like in the image above. We see that our spider is getting redirected to monster.com.

Now let’s go to the monster website and search for Product Manager in USA. We see that the URL https://www.monster.com/jobs/search/?q=Product-Manager&where=USA&stpage=1&page=6&jobid=a0d751b0-a2d4-4ce4-9d1a-85ee2a2cba9b and https://www.monster.com/jobs/search/?q=Product-Manager&where=USA takes us to the same page. We use this URL - https://www.monster.com/jobs/search/?q=Product-Manager&where=USA while inspecting(Ctrl +Shift+I, in Google Chrome(Windows))the website. Go down and click on “Load more jobs” and check the Network tab. Check illustrations below for reference.

> What we are trying to do here is find a pattern in the URL so that we can apply that to do iterations for multiple pages. You’ll see below we will find the URL ending with page =2 which represents that the page number is 2.

![alt text](https://cdn-images-1.medium.com/max/1200/1*pNPqGL1B-m2-pdvz32kECQ.jpeg)

![alt text](https://cdn-images-1.medium.com/max/1200/1*LjXsVeKtUVFYyr9AIb8OMg.jpeg)

Now what we will do is take out the Request URL from the Headers tab and put it as a start URL in our spider to see what we get.

![alt text](https://cdn-images-1.medium.com/max/600/1*Oftt-rPWpGGMq9H0iu2w0g.jpeg)
![alt text](https://cdn-images-1.medium.com/max/600/1*hP5BxqIeO9R3d-lA3HeiWw.jpeg)





