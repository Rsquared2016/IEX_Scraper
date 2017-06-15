import glob, pickle

class PostMarket():
    def __init__(self,root,conn,cursor):
        self.root = root
        self.conn = conn
        self.cursor = cursor

    def post_run(self):
        files = glob.glob(self.root + "data/checkpoints/*.pkl")
        for file in files:
            with(open(file,"rb")) as f:
                dat = pickle.load(f)
            for i in range(len(dat["time"])):
                sql = "INSERT INTO l2 VALUES ('%s', %s, %s, %s, %s, %s, %s, %s);"\
                      % (dat["ticker"],dat["askSize"][i],dat["bidSize"][i],dat["askPrice"][i],dat["bidPrice"][i],\
                         dat["lastSalePrice"][i],dat["lastSaleSize"][i],dat["time"][i])

                self.cursor.execute(sql)
                self.conn.commit()