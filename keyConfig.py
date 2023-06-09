import configparser
from colorama import Fore, Back, Style
import os

def get_key():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')
    # 读取INI文件
    config = configparser.ConfigParser()
    config.read(config_path)
    # config.read('config.ini')

    # 获取key变量
    key = config.get('Section1', 'key', fallback='')

    # 如果key为空，则要求用户输入并保存到INI文件
    if not key:
        key = input('Please enter your api-key：')
        config.set('Section1', 'key', key)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        print('api-key set successfully')

    return key

def change_key(newKey):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set('Section1', 'key', newKey)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print( Fore.YELLOW +'api-key changed successfully' + Style.RESET_ALL)