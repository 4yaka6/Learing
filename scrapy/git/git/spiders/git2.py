from os import times

import scrapy
from requests import session


class Git2Spider(scrapy.Spider):
    name = "git2"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        timestamp = response.xpath('//input[@name="timestamp"]/@value').extract_first()
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').extract_first()

        post_data = {
            "commit": "Sign in",
            "authenticity_token": token,
            "add_account": "login",
            "login": "ayakakinomiya@gmail.com",
            "password": "YYHys666.",
            "webauthn-conditional": "undefined",
            "javascript-support": "true",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "supported",
            "return_to": "https://github.com/login",
            "allow_signup": "",
            "client_id": "",
            "integration": "",
            "required_field_99a7": "",
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret
        }

        yield scrapy.FormRequest(
            url= 'https://github.com/session' ,
            callback=self.after_login ,
            formdata=post_data
        )

    def after_login(self,response) :
        yield scrapy.Request(
            url='https://github.com/4yaka6',
            callback=self.check_data
        )

    def check_data(self,response):
        print(response.xpath('/html/head/title/text()'))


