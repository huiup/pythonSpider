from urllib import request


class HtmlDownloader(object):
    def download_url(self, url):
        if url is None:
            return None
        response = request.urlopen(url)
        if response.getcode() != 200:
            print('  none none none none')
            return None
        return response.read()
