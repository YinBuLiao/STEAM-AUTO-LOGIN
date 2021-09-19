import signal
import subprocess
import time
import winreg
import re
import requests
import os

os.system("title Steam一键上号 By:YinBuLiao")

reg_path = r"SOFTWARE\Valve\Steam"  # 不要填入HKEY_CURRENT_USER，在openkey的时候填
key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, reg_path)
patch = winreg.QueryValueEx(key, 'SteamPath')  # 获取默认值 传递 None

account = input("请输入steam账号:")
try:
    # 获取账号关键词
    w1 = '----'

    # 获取SSFN文件
    w2 = '----'

    # 提取关键字
    pat = re.compile('(.*?)' + w1, re.S)
    splitaccount = account.split('ssfn')
    # 输出列表
    info = pat.findall(account)
    username = info[0]
    password = info[1]
    ssfn = splitaccount[1]

    pl = psutil.pids()
except :
    print('账号格式错误,格式：username----password----ssfnXXXX')
# 模拟chrome进行请求
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
}
def ssfndownload():
    url = r'https://ssfn.yinbuliao.cn/ssfn/ssfn'
    send_url = url + ssfn
    try:
        os.path.exists(patch[0] + '/' + 'ssfn' + ssfn)
        os.remove(patch[0] + '/' + 'ssfn' + ssfn)
        result = requests.get(send_url, headers=headers)
        filename = patch[0] + '/' + 'ssfn' + ssfn
        with open(filename, 'wb') as f:
            f.write(result.content)
    except:
        result = requests.get(send_url, headers=headers)
        filename = patch[0] + '/' + 'ssfn' + ssfn
        with open(filename, 'wb') as f:
            f.write(result.content)


def autoloign():
    steam = patch[0] + '/' + r"steam.exe"
    subprocess.run(steam + ' -login ' + str(username) + ' ' + str(password))

if __name__ == '__main__':
    try:
        subprocess.Popen('TASKKILL /F /IM steam.exe')
        print("正在启动或者关闭steam")
        time.sleep(1)
        ssfndownload()
        time.sleep(1)
        print("下载SSFN文件完成")
        print("自动登录成功，请手动退出程序")
        time.sleep(1)
        autoloign()
    except:
        os.system("pause");
