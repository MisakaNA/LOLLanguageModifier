import os
import subprocess
from os.path import exists
from time import sleep


def main():
    global server_int
    server = input('请选择更改的服务器：1. 正式服 2. 测试服\n')

    try:
        server_int = int(server)
        if server_int != 1 and server_int != 2: raise Exception()
    except:
        print('输你马呢\n')
        main()

    path = 'C:\\ProgramData\\Riot Games\\Metadata\\league_of_legends.live\\league_of_legends.live.product_settings.yaml' \
        if server_int == 1 else 'C:\\ProgramData\\Riot Games\\Metadata\\league_of_legends.pbe\\league_of_legends.pbe.product_settings.yaml'

    if not exists(path):
        print('文件或路径不存在')
        return

    data = ''
    try:
        with open(path, 'r') as f1:
            for line in f1:
                if 'en_US' in line:
                    line = line.replace('en_US', 'zh_CN')
                data += line
        with open(path, 'w') as f2:
            f2.write(data)
            print('语言属性写入完成！')
    except:
        print('文件写入错误\n将在十秒后终止程序\n')
        print('请前往 C:\\ProgramData\\Riot Games\\Metadata\\ 自行修改文件')
        sleep(10)
        return

    restart_game = input('是否重启当前客户端？ y/n\n')
    lol_path = ''
    if restart_game == 'y':
        cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Path'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line.find(b'League of Legends') != -1:
                lol_path = line.decode('utf-8').rstrip()
                break
    else:
        print('感谢您的使用')
        sleep(5)
        exit(0)

    if lol_path == '':
        print('没运行游戏你重启你马呢\n将在十秒后终止程序')
        sleep(10)
        exit(0)

    try:
        print('正在关闭英雄联盟')
        #os.system('taskkill /f /t /im LeagueClient.exe')
    except:
        pass
    sleep(1)


    header = lol_path[:lol_path.index('League of Legends')]
    riot_path = '"' + header + 'Riot Client\RiotClientServices.exe"' + ' --launch-product=league_of_legends --launch-patchline='
    riot_path += 'live' if lol_path.find('PBE') == -1 else 'pbe'

    print('启动命令已运行，若未出现游戏窗口请手动启动\n感谢您的使用')
    os.system(riot_path)
    exit(0)


if __name__ == '__main__':
    main()
