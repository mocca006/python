from django.shortcuts import render
from django.http import HttpResponse
from newsapp import models
import math

page1 = 1  #目前頁面

def index(request, pageindex=None):
	global page1  #重複開啟本網頁時需保留 page1 的值
	pagesize = 8  #每頁顯示的資料筆數
	newsall = models.NewsUnit.objects.all().order_by('-id')  #讀取新聞資料表,依時間遞減排序
	datasize = len(newsall)  #新聞筆數
	totpage = math.ceil(datasize / pagesize)  #總頁數
	if pageindex==None:  #無參數
		page1 = 1
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
	elif pageindex=='1':  #上一頁
		start = (page1-2)*pagesize  #該頁第1筆資料
		if start >= 0:  #有前頁資料就顯示
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 -= 1
	elif pageindex=='2':  #下一頁
		start = page1*pagesize  #該頁第1筆資料
		if start < datasize:  #有下頁資料就顯示
			newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
			page1 += 1
	elif pageindex=='3':  #由詳細頁面返回首頁
		start = (page1-1)*pagesize  #取得原有頁面第1筆資料
		newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]

	currentpage = page1  #將目頁前頁面以區域變數傳回html
	return render(request, "index.html", locals())

def detail(request, detailid=None):
	unit = models.NewsUnit.objects.get(id=detailid)  #根據參數取出資料
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1  #點擊數加1
	unit.save()  #儲存資料
	
	return render(request, "detail.html", locals())

def insert(request):
    title = '新聞系統開始使用'
    message = '本新聞系統從 2016/12/25 開始使用。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = 'Excel2016高效實用範例必修16課'
    message = '結合多種超實用圖表、函數，以實用範例串聯功能應用，將數字變成容易閱讀、分析的有用資訊。隨身速查表 : 特別提供 Excel 快速鍵速查表＋Excel 函數速查表，方便隨時查找應用。'
    unit = models.NewsUnit.objects.create(nickname='小華', title=title, message=message, enabled=1, press=1, catego='公告') 
    unit.save()
    title = 'App Inventor 2資料庫專題特訓班重裝上陣！'
    message = '快速邁向Android的App之路！最全面的App Inventor資料庫開發體驗！結合熱門議題、突破設計思維，打造專業與商業兼具的高質感App！'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = 'Swift初學特訓班：iOS App開發快速養成與實戰'
    message = '掌握Swift活用奧義，從62個範例快速打好iOS App開發力！開啟Apple設計模式，掌握Swift關鍵精髓，直擊iOS App快速開發新思維！'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=1, catego='更新') 
    unit.save()
    title = '用S4A玩出科技創意大未來 - 動手玩教室'
    message = '熱門的低價硬體 x 超簡單的拼圖軟體從動畫、遊戲到互動控制，從智慧家庭、物聯網基礎運用，到行動裝置App互動的全面攻略！'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = 'App Inventor 2專題特訓班'
    message = '適用想直接開發較大型App專案者。涵蓋不同功能訴求的專題內容，提供有趣的App開發方向，突顯行動裝置的特性，並充份發揮App的魅力，如感測器、網路雲端、GPS、藍牙、資料庫、機器人、遊戲、Arduino互動控制、NFC等熱門話題的應用App。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=2, catego='公告') 
    unit.save()
    title = '挑戰PHP／MySQL程式設計與超強專題特訓班'
    message = '進入專業互動網站程式開發殿堂，撰寫資料庫程式可以更簡單！秉持由淺入深的學習規劃，搭配實用的範例進行教學，除了解說各種語法、函式用途及程式執行流程，最後更規劃5個方向與訴求不同的實戰範例(網路留言版、會員系統、網路相簿、購物車，以及行動購物網站)，供學習與實務運用。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = 'Office 2016高效實用範例必修16課'
    message = '實務應用 × 提昇效率 : 生活、辦公、學習的最佳幫手，帶你快速打造各式主題的文件、試算表、簡報、資料庫。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=2, catego='更新') 
    unit.save()
    title = '翻倍效率工作術 - 不會就太可惜的Google超極限應用(第二版)'
    message = '提升生活娛樂 X 加強工作效率，不論你是個人使用、工作需求、學校出題授課...都能利用Google免費且功能強大的雲端工具在電腦及行動載具上同步管理。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=3, catego='公告') 
    unit.save()
    title = '快快樂樂學威力導演14：影片/MV剪輯活用情報特蒐'
    message = '由淺入深、圖文並茂，帶你使用威力導演學習豐富的影音編輯功能以及製作技巧，讓學習有概念、創意更速成。內容涵蓋了用心自製的主題式影片作品，集結了實用與創意，並整理出拍攝心得、環境佈置與設備講解，除了讓影片剪輯這件事變得更有趣也能自己輕鬆拍出超有感的作品'
    unit = models.NewsUnit.objects.create(nickname='小華', title=title, message=message, enabled=1, press=0, catego='更新') 
    unit.save()
    title = '中老年人快樂學 Facebook + LINE'
    message = '手機除了用來通話，也一定會用到 Facebook、LINE 這二套最熱門的社群通訊軟體，本書特別針對熟齡者生活主軸，貼心切題的講述並搭配大圖詳細說明，讓大家都能快速學習時下最流行的社群交流方式，更輕鬆地與家人、朋友分享生活大小事。'
    unit = models.NewsUnit.objects.create(nickname='小華', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = '生活科技應用網路概論(第二版)'
    message = '本書完整的介紹了網際網路的觀念、電子商務網路行銷、行動雲端應用及網路應用不可缺少的相片、影片…等實用操作內容，讓您快速掌握資訊脈動。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = '中老年人快樂學拍照、攝影'
    message = '智慧型手機或平板電腦擁有多功能且方便隨身攜帶的優勢，拍出來的相片、影片還可以透過軟體直接編修美化與分享更是方便。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='更新') 
    unit.save()
    title = 'iOS 10+iPhone 7 / 7Plus / iPad 完全活用術'
    message = 'iPhone 7 的上市為智慧型手機揭開新領域，無法忽視的質感外型，討論不斷的新機功能，我們將帶你從全新的外觀、重新設計的主畫面按鈕、按鍵操控新配置、Lightning 連接新革命、機身防潑抗水、立體聲喇叭、廣角與長焦雙鏡頭 ... 等主要焦點進行實機巡禮。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=1, catego='公告') 
    unit.save()
    title = 'Excel2016高效實用範例必修16課-善用資料圖表x函數巨集'
    message = '結合多種超實用圖表、函數，以實用範例串聯功能應用，將數字變成容易閱讀、分析的有用資訊。隨身速查表 : 特別提供 Excel 快速鍵速查表＋Excel 函數速查表，方便隨時查找應用。'
    unit = models.NewsUnit.objects.create(nickname='小華', title=title, message=message, enabled=1, press=1, catego='更新') 
    unit.save()
    title = '中老年人愛用APP全收錄 ( 第二版 )'
    message = '以熟年用手機、平板的需求為出發點，整理了最實用的八大類App應用程式，當紅的iPhone、iPad與HTC、Samsung、Sony、LG、OPPO、小米…等，都可以使用。簡單易懂的?述與圖大字少的詳細步驟，重點是書中提及的App通通是免費的！讓您用的開心，一看就懂！'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=0, catego='公告') 
    unit.save()
    title = '中老年人快樂學電腦(Windows 10+Office 2016)'
    message = '初學者通常會遇到那些問題呢？這樣是正確的操作步驟嗎？以熱愛學習的熟齡者角度出發，量身打造出最適合的學習教材！'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=2, catego='公告') 
    unit.save()
    title = '快快樂樂學威力導演15 - 影片/MV剪輯活用情報特蒐'
    message = '由淺入深、圖文並茂，帶你使用威力導演學習豐富的影音編輯功能以及製作技巧，讓學習有概念、創意更速成。內容涵蓋了實用與創意，並整理出拍攝心得、環境佈置與設備講解，除了讓影片剪輯這件事變得更有趣也能自己輕鬆拍出具有特色的作品。'
    unit = models.NewsUnit.objects.create(nickname='大明', title=title, message=message, enabled=1, press=6, catego='公告') 
    unit.save()
    return HttpResponse('新增資料完成！')
