# chrome_hunt
Hunting for chrome extensions!


## Usage
1. `pip install -r requirements.txt`
2. `python chrome_hunt.py`

## Commands
`help` - Show help message

`hunt [URL]` - All in one function

`download [URL]` - Download a chrome extension

`unzip [Extension.crx]` - Unzip a chrome extension

## Example
```
python3 chrome_hunt.py

   ________                              __  __            __
  / ____/ /_  _________  ____ ___  ___  / / / /_  ______  / /_
 / /   / __ \/ ___/ __ \/ __ `__ \/ _ \/ /_/ / / / / __ \/ __/
/ /___/ / / / /  / /_/ / / / / / /  __/ __  / /_/ / / / / /_
\____/_/ /_/_/   \____/_/ /_/ /_/\___/_/ /_/\__,_/_/ /_/\__/

			                  @th3_protoCOL
[>] help

Documented commands (type help <topic>):
========================================
download  exit  help  hunt  unzip

[>] hunt https://chrome.google.com/webstore/detail/share-to-classroom/adokjfanaflbkibffcbhihgihpgijcei
Output name [Extension]:
[*] Downloading extension with id: adokjfanaflbkibffcbhihgihpgijcei
[*] Wrote to Extension.crx
[*] Unziped extension to Extension/
[!] Done!
[>] exit
```
