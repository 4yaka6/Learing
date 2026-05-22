from typing import Iterable, Any

import scrapy


class Git1Spider(scrapy.Spider):
    name = "git1"
    allowed_domains = ["github.com"]
    start_urls = ["https://github.com/4yaka6"]



    def start_requests(self) :
        url = self.start_urls[0]
        temp = '_device_id=7255f15f4e39f0d37994728258a676aa; saved_user_sessions=163295852%3Ai02K6NsyQaaVWANnIe8IXdVHaSSqz2OCVK2e32ROzYEGfckF; user_session=i02K6NsyQaaVWANnIe8IXdVHaSSqz2OCVK2e32ROzYEGfckF; __Host-user_session_same_site=i02K6NsyQaaVWANnIe8IXdVHaSSqz2OCVK2e32ROzYEGfckF; logged_in=yes; dotcom_user=4yaka6; _octo=GH1.1.721273753.1774860983; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=R38ztG52o7bRvVNofJGvIa4Vk1a8VmBWBA8vauiVr39sR9O32z730h15FzMo3GEtHWpWBueJvYuuK%2FT8j9WhI%2Fa6oQ8P6oP%2BjBQTBN0VNbnvPrnCmeyfSoyAOpBbWFfUIG5xvBi0Yoki20zW4Nm0hqnM8el5fBBdOOsVw4b3QNMKlxtVulIopA8f%2Ff817%2BZ2qkOQfU0EEvS%2BU5iUHv1hQ0J9T8SnhJvUewLa%2BNRHXRbMt8y9efNYeQ8GdftM2%2BAU3gMFgnKOxqLIvBxzp2dnbCahR%2FOtD3rSaf%2Bg3Af3YgNzevailIxIKT9pc1Vf4O%2BE5ZoRWeDpkfFn2TLsOnqQ%2FaKt1kLvIApU7R7g5v%2BoAULgApKXLOAPHTotq5nk61X0--9ZDXx%2BLEUrXq4VZj--TwyHm9I%2BfEqd88EYhBA6PA%3D%3D'
        cookie = {data.split('=')[0]: data.split('=')[-1] for data in temp.split(';')}

        yield scrapy.Request(
            url = url,
            cookies= cookie
        )

    def parse(self, response):
        print(response.xpath('/html/head/title/text()'))
