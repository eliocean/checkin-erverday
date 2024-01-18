import argparse
import requests
requests.packages.urllib3.disable_warnings() # 关闭警告，ssl证书不验证会输出警告

def checkin(tokens):
   url = "https://apicn.aihao123.cn/luomacode-api/activity/signin"
   payload={}
   for token in tokens.split(','):
      headers = {
            'Origin': 'https://h5.aihao123.cn/',
            'Referer': 'https://h5.aihao123.cn/',
            'Token': token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
         }
      response = requests.request("POST", url, headers=headers, data=payload,verify=False)
      print(response.text)



def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('-t', '--token', type=str, default='', help='请输入token')
   args = parser.parse_args()

   if args.token:
      checkin(args.token)
   else:
      parser.print_help()


if __name__ == '__main__':
   main()