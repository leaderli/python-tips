import subprocess

r = subprocess.Popen(['echo', 'hello'], stdout=subprocess.PIPE, universal_newlines=True)

print('-' * 100)
print(r.stdout.read())
print('-' * 100)

r = subprocess.Popen(['echo', 'hello'], stdout=subprocess.PIPE)
print(r.stdout.read())
print('-' * 100)
