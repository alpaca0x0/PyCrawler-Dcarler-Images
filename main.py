# -*- coding: utf-8 -*
import sys
import signal # signal 安全退出
from modules.BoardList import main as ModBoardList # Modules Board List
from modules.BoardSearch import main as ModBoardSearch # Modules Board Search
from modules.dcl import main as DCL # Modules RUN DCL !
from sty import fg, bg, ef, rs,Style, RgbFg # Font color

class _info():
	def __init__(self):
		self.name="Dcarler"
		self.athr="Alpaca羊駝"
		self.ver="1.0"
		self.update="2019/01/18"
_info=_info()

# 運行參數
sys_debug=False
if ("--debug" in sys.argv) or ("-d" in sys.argv):
	print("Debug Mod On!\n")
	sys_debug=True;

def exit(signum, frame):
    print('\n Stoped '+_info.name+'！ \n')
    sys.exit()
signal.signal(signal.SIGINT, exit)
signal.signal(signal.SIGTERM, exit)

# Font, Colors
ef.end = '\033[0m'
# ef.italic for italic
ef.blod = '\033[1m'
ef.underline = '\033[4m'
# fg.rs for end
fg.red=Style(RgbFg(255, 50, 50))
fg.orange = Style(RgbFg(255, 150, 50))
fg.gray = Style(RgbFg(165,165,165))
fg.green = Style(RgbFg(110,255,120))

#################################################

url='https://www.dcard.tw'
url_board='/f'
url_search=url+"/f/search?query="

print(fg.green+"Use \"Ctrl+C\" to exit. \n\tHave fun! ヽ(●´∀`●)ﾉ"+fg.rs+"\n")

while True:
	# 查詢板塊
	dcl_mode=input(ef.blod+"(1) Board URL (Default)\n(2) Board list select\n(3) Board keyword search (Not recommend)"+ef.end+fg.orange+"\nChoice mode: "+fg.rs).replace(" ","")
	if dcl_mode=='' or dcl_mode=="1":
		# 鍵入給爬蟲板塊URL
		print("Selected mode 1")
		pass
	elif dcl_mode=="2":
		# 查看板塊清單
		print("")
		ModBoardList(sys_debug=sys_debug, url=url, url_board=url_board)
	elif dcl_mode=="3":
		# 搜尋板塊
		print("")
		ModBoardSearch(sys_debug=sys_debug, url_search=url_search)
		pass
	else:
		print(fg.red+ef.blod+"Only the above modes. Try again!\n"+ef.end+fg.rs)
		