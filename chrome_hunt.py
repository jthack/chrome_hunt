# Chrome Hunt - @th3_protoCOL
import re
import cmd
import requests
from pyfiglet import Figlet

class Chrome_Hunt(cmd.Cmd):
    """Hunt for chrome extentions! Made by @th3_protoCOL"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '[>] '
        fig = Figlet(font='slant')
        print(fig.renderText('ChromeHunt'))
        #print(fig.renderText(''))
        print("\t\t\t@th3_protoCOL")

    def do_download(self, arg):
        """Download [URL]
        Download a chrome extention"""
        extention_id = arg.rsplit('/',1)[1]
        url = 'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&acceptformat=crx3&x=id%3D'+extention_id+'%26installsource%3Dondemand%26uc'
        r = requests.get(url, allow_redirects=True)
        print("[*] Downloading extention w/ id: "+extention_id)
        open('Extention.crx', 'wb').write(r.content)
        print("[!] Wrote to Extention.crx")

    def do_extract(self):
        """Extract [Extention.crx]
        Extract a chrome extention"""

    def do_hunt():
        """Hunt for extentions"""
        print()

    def do_exit(self, line):
        "Exit the program"
        exit(1)

if __name__ == '__main__':
    Chrome_Hunt = Chrome_Hunt()
    Chrome_Hunt.cmdloop()
