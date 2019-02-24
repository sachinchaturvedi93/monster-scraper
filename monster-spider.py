# -*- coding: utf-8 -*-
import scrapy
import json
from pprint import pprint

from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)


class MonsterSpiderSpider(scrapy.Spider):
    name = 'monster-spider'
    allowed_domains = ['monster.com']
    start_urls = ['https://www.monster.com/jobs/search/pagination/'
                    '?q=Product-Manager&where=USA&isDynamicPage=true&'
                    'isMKPagination=true&page={}'.format(i + 1) for i in range(2) ]

    def parse(self, response):
        results = json.loads(response.body)
        for result in results:
            try:
                job_id = result['MusangKingId']
                next_url = ('https://job-openings.monster.com/v2/job/pure-json-view?jobid={}').format(job_id)
                yield response.follow(next_url, callback = self.parse_detail)
            except:
                continue
            
    def parse_detail(self,response):
        result = json.loads(response.body)
        detail = {}
        detail["JobID"] = result['jobId']
        detail["Title"] = result['companyInfo']['companyHeader']
        detail["Location"] = result['companyInfo']['jobLocation']
        try:    
            detail["Company"] = result['companyInfo']['name']
        except:
            detail["Company"] = ''
        detail['Job Category'] = result["jobCategory"]
        detail["Description"] = text_from_html(result["jobDescription"])
        try:
            detail["Company Size"] = result['companyInfo']["companySizeName"]
        except:
            detail["Company Size"] = ''
        info = result['summary']['info']
        for i in info:
            detail[i['title']] = i['text']
        return detail
    
