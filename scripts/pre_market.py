import os,glob

class PreMarket():
    def __init__(self,root):
        self.root = root

    def pre_run(self):
        files = glob.glob("%sdata/checkpoints/*.pkl" % self.root)
        for f in files:
            os.remove(f)