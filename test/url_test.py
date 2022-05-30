import urllib.request


def download_url(url, save_path):
    with urllib.request.urlopen(url) as dl_file:
        with open(save_path, 'wb') as out_file:
            out_file.write(dl_file.read())


download_url('https://github.com/leaderli/litil/archive/refs/heads/master.zip', 'litil.zip')
