# Chrome Hunt - @th3_protoCOL
import re
import cmd
import requests
import zipfile
from pyfiglet import Figlet

class Chrome_Hunt(cmd.Cmd):
    """Hunt for chrome extension! Made by @th3_protoCOL"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '[>] '
        fig = Figlet(font='slant')
        print(fig.renderText('ChromeHunt'))
        #print(fig.renderText(''))
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

    def do_exit(self, line):
        "Exit the program"
        exit(1)

    def download(self, url, name="extension.crx"):
        extention_id = url.rsplit('/',1)[1]     # Parse the extention id from url
        download_url = 'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3D'+extention_id+'%26installsource%3Dondemand%26uc'    # Download .crx
        print("[*] Downloading extension with id: "+extention_id)
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

if __name__ == '__main__':
    Chrome_Hunt = Chrome_Hunt()
    Chrome_Hunt.cmdloop()
