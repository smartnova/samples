import re
import subprocess

CHROME_LIST_CMD = 'chrome-cli list links'
CHROME_LIST_RX = re.compile('(\[[0-9]+\]) *(http.*)')

def chrome2doi():
    '''
    Google Chrome のタブのうち、以下の URL にマッチするページの内容を入手し、
    そのページから DOI を読み取る。
    IEEE Explore:  https://ieeexplore.ieee.org/document/{ID}/
    Wiley Online:  https://onlinelibrary.wiley.com/doi/abs/{DOI}
    Springer LNDS: https://link.springer.com/chapter/{DOI}
    '''

    for line in subprocess.check_output(['chrome-cli', 'list', 'links']).decode('utf-8').split('\n'):
        print('-', line)

if __name__ == '__main__':
    chrome2doi()
