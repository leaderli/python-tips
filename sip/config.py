from li.li_cmd import LiCmd


class Config(LiCmd):

    def do_list(self, key):
        """ list the key"""
        print('list:', key)


config = Config()
