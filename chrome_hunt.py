# Chrome Hunt - @th3_protoCOL
import re
import cmd
import zipfile
import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet

class Chrome_Hunt(cmd.Cmd):
    """Hunt for chrome extension! Made by @th3_protoCOL"""
    found_extensions = []

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '[>] '
        fig = Figlet(font='slant')
        print(fig.renderText('ChromeHunt'))
        print("\t\t\t@th3_protoCOL")

    def do_download(self, arg):
        """download [URL]
        Download a chrome extension"""
        self.download(arg)

    def do_unzip(self, arg):
        """Extract [Extension.crx]
        Extract a chrome extension"""
        self.unzip(arg)

    def do_hunt(self, arg):
        """hunt [URL]
        Hunt for extensions! Downloads and Extracts."""
        output = input("Output name [Extension]: ")
        if output == '':
            output = "Extension.crx"
        if ".crx" not in output:
            output = output+".crx"
        self.download(arg, output)
        self.unzip(output)

    def do_spider(self, arg):
        print("[*] Requesting chrome store content")
        # Set headers
        headers = requests.utils.default_headers() # Move this to global maybe?
        headers.update({ 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
        response = requests.get("https://chrome.google.com/webstore/category/extensions", headers)
        extensions = self.parse_urls(response)
        self.parse_detail(extensions)

    def do_exit(self, line):
        "Exit the program"
        exit(1)

    def download(self, url, name="extension.crx"):
        extension_id = url.rsplit('/',1)[1]     # Parse the extension id from url
        download_url = 'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3D'+extension_id+'%26installsource%3Dondemand%26uc'    # Download .crx
        print("[*] Downloading extension with id: "+extension_id)
        r = requests.get(download_url, allow_redirects=True)
        if r.status_code == 200:
            open(name, 'wb').write(r.content)
            print("[*] Wrote to "+str(name))
        else:
            print("[-] Request Error: "+r.status_code)

    def unzip(self, zip):
        with zipfile.ZipFile(zip, 'r') as zip_ref:
            zip_ref.extractall(zip[:-4])
            print("[*] Unziped extension to "+str(zip[:-4])+"/")
        print("[!] Done!")

    def parse_detail(self, extensions):
        new_extensions = []
        for e in extensions:
            response = requests.get(e)
            soup = BeautifulSoup(response.text, "html.parser")
            name = e.rsplit('/',2)[1]
            link = e
            # Parse the <meta> tag for the exact number, remove junk characters and round it.
            download_tag = soup.find(itemprop="interactionCount").get("content")
            download_count = round(float(download_tag.rsplit(':',1)[1].replace(',','').replace('+','').replace('.','')))
            print("[*] Extension: "+name)
            if download_count >= 50000:
                print("\x1b[32m[+]\033[1;0m Downloads: "+str(download_count)+"")
            else:
                print("\033[91m[-]\033[1;0m Downloads: "+str(download_count)+"")
            print("[*] Link: "+link+"\n[ ]")
            # Search for releated extension urls on repsonse page. we will likely have to worry about dups later on.
            if name not in self.found_extensions:
                self.found_extensions.append(name)
                new_extensions.append(self.parse_urls(response))
        # Parse the new extensions!
        self.parse_detail(new_extensions)

    def parse_urls(self, response):
        # Regex for URLs on homepage
        urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
        extensions = []
        for link in urls:
            if "https://chrome.google.com/webstore/detail" in link:
                extensions.append(link)
        return extensions

if __name__ == '__main__':
    Chrome_Hunt = Chrome_Hunt()
    Chrome_Hunt.cmdloop()
