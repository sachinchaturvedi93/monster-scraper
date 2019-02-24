# -*- coding: utf-8 -*-
import scrapy
import json
from pprint import pprint


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
        return detail
