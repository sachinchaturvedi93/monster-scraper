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

As you can see that the output is JSON encoded data. We will import pprint and json to make it more readable.

![alt text](https://cdn-images-1.medium.com/max/600/1*d4FpC_JvVMi69I04A6d7wA.jpeg)
![alt text](https://cdn-images-1.medium.com/max/600/1*l2dV2Ao4gihyQ7Ujs9v0uw.jpeg)

If you go through the output you will find many interesting things like Title, JobViewUrl, etc. I’m wondering what will happen if I try to open any JobViewUrl in the browser. Let’s check it out. And it certainly does open the job link on a separate page.

Let’s try something else. Let’s go the URL https://www.monster.com/jobs/search/?q=Product-Manager&where=USA and click on the jobs given on the left pane and see what pops up in the Network tab.

![alt text](https://cdn-images-1.medium.com/max/600/1*vLwa09_Sr_G-H_dDNM87fg.jpeg)
![alt text](https://cdn-images-1.medium.com/max/600/1*dStzYToYMm_XAAxMZCzp8Q.jpeg)

> We get this whenever we click on a specific job posting. As we will see below, every job posting has data encoded in JSON format.

If you search any text from the Job Description it would show up in the Response tab. Which shows we can get our desired output from the Request URL in the Headers tab in JSON format.

But when you take out the URL you find that it’s too complex. Have a look at it.

```
https://job-openings.monster.com/v2/job/pure-json-view?Js30Flow=%7B%22searchPath%22:%22%22,%22q%22:%22Product-Manager%22,%22where%22:%22USA%22,%22useLpfRootPrefix%22:true%7D&jobid=205603967&callback=jQuery33105010418825622995_1551036585977. 
```
The link above is complex with so many components. Let’s see if we can do something about this.
Let’s see what happens if we include just the jobid in the link and remove everything as follows :
```
https://job-openings.monster.com/v2/job/pure-json-view?jobid=205603967
```
![alt text](https://cdn-images-1.medium.com/max/1200/1*F9GLYCpOis6RWMdQvJVW5g.jpeg)

Perfect! If you search something from the Job Description(through which we got the link) you will find it in this JSON encoded data.

Now if we refer to the output that we got in the beginning importing json and pprint, we can see clearly that JobID is represented by key MusangKingID. Go through the output and try to see what it all represents. Like, Title refers to the Job Title, JobViewUrl refers to the URL of that specific job. Under Company you will find, Company URL and name of the Company.

![alt text](https://cdn-images-1.medium.com/max/800/1*Dm22yBEOKAMvPEevWgKrYQ.jpeg)
![alt text](https://cdn-images-1.medium.com/max/800/1*dY02NShcdvM2NEGhFmbzcQ.jpeg)

So, the above output give us the JobIDs for 2 pages since the start URL is set up to 2 pages for now. If we change it to 50 pages, we will get JobIDs for upto 50 pages. You can see we have used try and except statement here for Exception Handling.

## Let’s See What We Got Till Now

1. We have the start URL for the Job Title & Location. This link represent entries till page 2 as it is visible in the given URL.
```
https://www.monster.com/jobs/search/pagination/?q=Product-Manager&where=USA&isDynamicPage=true&isMKPagination=true&page=2
```
2. We have the start URL for every Job in JSON format. All we need is the Job IDs.
```
https://job-openings.monster.com/v2/job/pure-json-view?jobid=
```
3. We have the JobIDs, which we extracted from the start URL in No 1.

![alt text](https://cdn-images-1.medium.com/max/800/1*dY02NShcdvM2NEGhFmbzcQ.jpeg)

## Next Steps

Let us beautify the JSON data we have so that it is readable. I use JSON Formatter & Validator for this. Copy all your data and paste it in the empty box and click on Process. Voila!

















