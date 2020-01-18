# -*- coding: utf-8 -*
import requests # 請求
from bs4 import BeautifulSoup as soup # 解析html標籤
from fake_useragent import UserAgent # 偽裝請求
from sty import fg, bg, ef, rs,Style, RgbFg

def set_header_user_agent():
    user_agent = UserAgent()
    return user_agent.random

# Font, Colors
ef.end = '\033[0m'
# ef.italic for italic
ef.blod = '\033[1m'
ef.underline = '\033[4m'
# fg.rs for end
fg.orange = Style(RgbFg(255, 150, 50))
fg.gray = Style(RgbFg(165,165,165))
fg.gray_light = Style(RgbFg(125,125,125))

#################################################

def run_dcl(check="n"):
	check = check.lower()
	if check != "y" and check != "yes":
		pass

def main(url,url_board,sys_debug=False):
	while True:
		req_url=url+url_board
		req_useragent=set_header_user_agent()
		req_headers={"User-Agent": req_useragent}
		if sys_debug:
			print("\n"+str(req_headers))
		req=requests.get(req_url,headers=req_headers,timeout=15)
		req.encode="utf-8"
		# 查看回應
		if sys_debug:
			print("HOST => HTTP: "+req.url)
			print("HOST <= HTTP: "+str(req.status_code)+"\n")
		if req.status_code != requests.codes.ok:
			print("Um... Bad request :/\n")
			break
		# 解析
		req=soup(req.text,"html.parser")
		datas=req.select("a.ForumEntry_link_3tNC45.ForumEntry_unRead_1ptlOL")
		if len(datas)==0:
			print("Not Found!")
			x=input("Try again? (y/n)").replace(" ","").lower()
			print("")
			if x=="y" or x=="yes":
				continue
			else:
				break
		for data in datas:
			print("("+ef.blod+fg.gray+str(datas.index(data))+fg.rs+ef.end+") "+ef.italic+str(data.text)+ef.end+fg.gray_light+" ("+url+str(data.get("href"))+")"+fg.rs)
			if (datas.index(data))%20==0 and (datas.index(data))>0:
				x=input(fg.green+str(datas.index(data))+"/"+str(len(datas)-1)+fg.orange+"\n\"Enter\" for keep, Enter \"c\" for stop.\nEnter the above "+fg.gray+"<number>"+fg.rs+fg.orange+" to run crawler: "+fg.rs)
				if x=="c" or x=="C":
					break
		else:
			print(fg.orange+"No more.\n"+fg.rs)
		print("")
		break