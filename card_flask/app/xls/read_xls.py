from os.path import dirname, abspath
import pandas as pd
top_dir = dirname(dirname(dirname(dirname(abspath(__file__)))))#つまりトップ階層

xls = pd.read_excel(f"{top_dir}/abcd.xls",header=None,sheet_name="BB")

class Card100:
    def __init__(self,card_num,xls):
        idx = card_num + 1
        row = xls.values[idx,:]
        self.card_num = card_num
        self.key = row[7]
        self.key_hurigana = row[8]
        self.content_head = " ".join(row[2].split())
        self.content_tail = " ".join(row[3].split())
        self.writer_name = row[0]
def get_card(card_num):
    return Card100(card_num,xls)