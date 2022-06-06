from  li.li_bash import  ssh_call
# import subprocess
#
# r = subprocess.Popen(['echo', 'hello'], stdout=subprocess.PIPE, universal_newlines=True)
#
# print('-' * 100)
# print(r.stdout.read())
# print('-' * 100)
#
# r = subprocess.Popen(['echo', 'hello'], stdout=subprocess.PIPE)
# print(r.stdout.read())
# print('-' * 100)

ssh_call('li@192.168.142.128','~','ll')
