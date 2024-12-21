# Check-Point_poc
Check-Point安全网关任意文件读取漏洞(CVE-2024-24919)

python Check-Point_poc.py -h              

                ) (`-.            ) (`-.
         ( OO ).           ( OO ).
        (_/.  \_)-. ,-.-')(_/.  \_)-. ,-.-')
         \  `.'  /  |  |OO)\  `.'  /  |  |OO)
          \     /\  |  |  \ \     /\  |  |  \
           \   \ |  |  |(_/  \   \ |  |  |(_/
          .'    \_),|  |_.' .'    \_),|  |_.'
         /  .'.  \(_|  |   /  .'.  \(_|  |
        '--'   '--' `--'  '--'   '--' `--'


usage: Check-Point_poc.py [-h] [-u URL] [-f FILE]  

Check-Point安全网关任意文件读取漏洞(CVE-2024-24919)  

optional arguments:  
  -h, --help            show this help message and exit  
  -u URL, --url URL     添加url信息  
  -f FILE, --file FILE  添加txt文件  

example:  
    python3 Check-Point_poc.py -u http://xxxx.xxxx.xxxx.xxxx  
    python3 Check-Point_poc.py -f x_url.txt  
