import os


def checkCrontab():
    """
    新旧命令对比，有新命令则写入新命令
    """
    storage = '/' + path_list[-2]
    file = '/' + path_list[-1]
    crontab_list = f'{env}/config/crontab.list'
    key = '# xxxxxx（请勿删除此行）\n'
    new = f'{cron} python /jd{storage}{file} >> /jd/log{file.split(".")[0]}.log 2>&1\n'
    with open(crontab_list, 'r', encoding='utf-8') as f1:
        crontab = f1.readlines()
    if crontab[-1] == '\n':
        del(crontab[-1])
    if key in crontab:
        m = crontab.index(key)
        if crontab[m + 1] != new:
            del(crontab[m + 1])
            crontab.insert(m + 1,new)
    else:
        crontab.append(f'\n{key}{new}')
    with open(crontab_list, 'w', encoding='utf-8') as f2:
        print(''.join(crontab), file=f2)


# 开始执行主程序
if __name__ == '__main__':
    path_list = os.path.realpath(__file__).split('/')[1:]
    env = '/' + '/'.join(path_list[:-2])
    if os.path.isfile('/ql/config/cookie.sh') or os.path.isfile(f'{env}/config/cookie.sh'): # 青龙
        isv4 = False
        if not os.path.isfile(f'{env}/config/cookie.sh'): # 青龙容器内
            env = '/ql'
    else: # v4-bot
        isv4 = True
        if not os.path.isfile(f'{env}/config/config.sh'): # v4-bot 容器内
            env = '/jd'
    checkCrontab()
