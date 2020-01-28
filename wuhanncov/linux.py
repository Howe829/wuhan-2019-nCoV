import os


# [sudo] gem install terminal-notifier
def notify(summary, body, time:int):
    if os.name == 'posix':
        i = "-i {}".format("/".join(os.getcwd().split('/')[:-1])+'/arts/warning.png')
        t = "-t {}".format(str(time*1000))
        s = summary
        b = body
        cmd = u' '.join(['notify-send', i, s, b]).encode('utf-8').strip()
        os.system(cmd)




