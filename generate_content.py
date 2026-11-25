#!/usr/bin/env python3
"""Generate updated index.html with detailed content from reference site."""

# Each code has: code, title, unit, price_normal, price_remote, category, tags[], sections{}
# sections keys: regulation, must_do, must_not, mistakes, details, conflict

codes = []

# ===== BA01 =====
codes.append({
    'code': 'BA01', 'title': '基本身體清潔', 'unit': '1次',
    'price_normal': 260, 'price_remote': 310, 'category': '清潔沐浴',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助沐浴及洗頭以外之身體清潔，如：臉部、手、足局部清潔、口腔清潔及刮鬍子。',
        '給付價格 260 元（原住民族地區／離島 310 元）。',
        '原則每日以 1 組合為限，同一時段不可併同 BA07 及 BA23。',
    ],
    'must_do': [
        '確認水溫適宜，注意保暖與隱私。',
        '觀察皮膚狀況（紅腫、破皮、壓瘡前兆），發現異常立即記錄並回報督導。',
        '口腔清潔需含刷牙或口腔擦拭（視個案能力使用棉棒或紗布）。',
        '清潔順序：臉部→手部→足部→會陰部（依個案需求選做）。',
        '記錄項目：日期、起迄時間、實做部位、皮膚觀察。',
    ],
    'must_not': [
        '不可將沐浴（BA07）或洗頭（BA23）的內容拆進 BA01 申報。',
        '不可為同住家屬提供清潔服務。',
        '不可在皮膚有傷口或感染時自行處理（應通報護理師）。',
        '不可省略口腔清潔僅做擦臉就結案。',
    ],
    'mistakes': [
        {
            'q': '個案說「幫我順便洗個頭」，直接洗頭後以 BA01 申報。',
            'a': '洗頭屬 BA07 或 BA23 範圍，BA01 不含洗頭。應回報督導評估是否增加碼別。',
        },
        {
            'q': '擦臉加擦背，算不算沐浴可以報 BA07？',
            'a': '局部清潔仍屬 BA01，只有完整沐浴（含軀幹清潔）才能報 BA07。',
        },
        {
            'q': '早上擦臉、下午再來擦腳，可以報兩次 BA01？',
            'a': '原則每日 1 組合為限；如有特殊需求應由 A 個管評估核定。',
        },
    ],
    'details': [
        '含洗臉、口腔清潔、手足局部清潔、刮鬍子等。',
        '不含沐浴及洗頭，這些有獨立碼別（BA07、BA23）。',
        '得依第 21 條臨時先做後補。',
        '使用拋棄式清潔用品時，費用由長照計畫負擔或自備由個案決定。',
    ],
    'conflict': [
        '同時段互斥：<a href="#code-BA07">BA07</a>（協助沐浴及洗頭）、<a href="#code-BA23">BA23</a>（協助洗頭）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）、<a href="#code-AA03">AA03</a>（體重過重加計）。',
    ],
})

# ===== BA02 =====
codes.append({
    'code': 'BA02', 'title': '基本日常照顧', 'unit': '1次',
    'price_normal': 195, 'price_remote': 235, 'category': '日常照顧',
    'tags': [],
    'regulation': [
        '協助穿脫衣物、更換尿片（布）及乘坐輪椅或乘坐輔具之轉位。',
        '給付價格 195 元（原住民族地區／離島 235 元）。',
        '含協助更衣、更換尿片（布）、使用便盆或尿壺、轉位協助。',
        '不得與其他照顧組合併同使用，但可接續。',
    ],
    'must_do': [
        '轉位前先確認輪椅煞車已鎖、輔具已固定。',
        '使用正確搬運技巧（面對個案、腳步站穩、彎膝不彎腰）。',
        '更換尿片後觀察皮膚狀況，預防壓瘡。',
        '協助如廁須注意安全扶手是否穩固、地面是否濕滑。',
        '記錄：服務內容、皮膚觀察、排泄狀況（量、色、形態）。',
    ],
    'must_not': [
        '不得與其他組合併同使用（如在 BA07 沐浴途中另報 BA02 穿脫衣）。',
        '不得讓個案在未確保安全的情況下自行移位。',
        '不可省略尿片更換後的清潔步驟。',
        '不可將家務清潔混入 BA02 申報。',
    ],
    'mistakes': [
        {
            'q': '沐浴後幫個案穿衣、轉回輪椅，可以加報 BA02 嗎？',
            'a': '穿脫衣和轉位如在 BA07 服務過程中完成，屬該碼涵蓋範圍，不另報 BA02。',
        },
        {
            'q': '個案每天需換 3 次尿片，可以報 3 次 BA02？',
            'a': '需依照核定計畫執行，超出次數回報督導，由 A 個管評估核定。',
        },
    ],
    'details': [
        '包含穿脫衣物、更換尿片（布）、乘坐輪椅或輔具之轉位。',
        '轉位含床→輪椅、輪椅→馬桶等日常移位。',
        '協助使用便盆或尿壺。',
        '協助服藥提醒（但分藥是 BA17e、管灌是 BA04）。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '不得與其他照顧組合併同使用。',
        '分界：<a href="#code-BA10">BA10</a>（翻身拍背）、<a href="#code-BA15">BA15</a>（家務協助）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）、<a href="#code-AA05">AA05</a>（特殊加計）。',
    ],
})

# ===== BA03 =====
codes.append({
    'code': 'BA03', 'title': '測量生命徵象', 'unit': '1次',
    'price_normal': 155, 'price_remote': 185, 'category': '醫療相關',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助量血壓、量體溫、量脈搏、量呼吸。',
        '給付價格 155 元（原住民族地區／離島 185 元）。',
        '原則每日以 1 組合為限。',
    ],
    'must_do': [
        '依正確方式量測（坐姿休息 5 分鐘後量血壓、腋溫 5-10 分鐘）。',
        '量測結果必須完整記錄數值與時間，異常值須標記並通知督導。',
        '使用校正過的量測儀器（血壓計、體溫計）。',
    ],
    'must_not': [
        '不可只量血壓而不記錄其他項目（應視核定計畫執行全套或部分）。',
        '發現異常值不可隱匿或僅記「正常」。',
        '不可使用未校正的儀器。',
    ],
    'mistakes': [
        {
            'q': '個案說「今天量過了」就不量，直接抄數值。',
            'a': '必須親自量測並據實記錄，不得抄錄他人數據。',
        },
        {
            'q': '順便量了家屬的血壓，可以一起報嗎？',
            'a': '服務對象限核定個案，家屬不屬服務範圍。',
        },
    ],
    'details': [
        '含量血壓、量體溫、量脈搏、量呼吸。',
        '得依第 21 條臨時先做後補。',
        '量測結果異常應即時通知督導並啟動緊急聯絡機制。',
    ],
    'conflict': [
        '可搭配其他 BA 碼接續使用。',
        '相關：<a href="#code-BA17d1">BA17d1</a>（血糖機驗血糖）。',
    ],
})

# ===== BA04 =====
codes.append({
    'code': 'BA04', 'title': '協助進食或管灌餵食', 'unit': '1次',
    'price_normal': 195, 'price_remote': 235, 'category': '日常照顧',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助進食或管灌餵食。',
        '給付價格 195 元（原住民族地區／離島 235 元）。',
        '原則每日以 3 組合為限。',
    ],
    'must_do': [
        '確認食物種類與質地符合個案需求（如流質、半流質、碎食等）。',
        '管灌前確認管路位置正確（反抽胃液、聽診）。',
        '進食時協助坐姿（至少 45 度），飯後維持 30 分鐘。',
        '觀察吞嚥狀況，發現嗆咳立即處理。',
        '記錄進食量、管灌量、速度及個案反應。',
    ],
    'must_not': [
        '不可強迫進食。',
        '不可在個案躺平時灌食。',
        '管灌溫度過熱或速度過快。',
        '不可自行調整管灌配方或濃度（需依醫囑）。',
    ],
    'mistakes': [
        {
            'q': '個案管灌中途有殘餘，居服員自行減量。',
            'a': '管灌量與速度依醫囑或護理師指示，不可自行調整，需回報。',
        },
        {
            'q': '早餐午餐都來灌食但時間重疊了，報 2 次可以嗎？',
            'a': '每餐獨立計算一次組合，但不可時間重疊申報。需確實分開時段。',
        },
    ],
    'details': [
        '含口腔餵食（協助進食）和管灌餵食兩種。',
        '管灌前應確認管路：反抽、聽診、確認鼻胃管刻度。',
        '得依第 21 條臨時先做後補。',
    ],
    'conflict': [
        '相關：<a href="#code-BA17c">BA17c</a>（鼻胃管清潔固定）。',
        '可加計：<a href="#code-AA03">AA03</a>（體重過重加計）。',
    ],
})

# ===== BA05 =====
codes.append({
    'code': 'BA05', 'title': '餐食照顧', 'unit': '1次',
    'price_normal': 310, 'price_remote': 370, 'category': '日常照顧',
    'tags': [],
    'regulation': [
        '依據個案飲食需求準備餐食。',
        '給付價格 310 元（原住民族地區／離島 370 元）。',
        '含備餐、烹煮、善後清潔。',
    ],
    'must_do': [
        '依個案飲食計畫備餐（注意過敏原、疾病飲食限制）。',
        '確認食材新鮮度與保存期限。',
        '烹飪過程注意衛生（洗手、砧板分生熟）。',
        '完成後廚房善後清潔。',
        '記錄備餐內容與個案進食情形。',
    ],
    'must_not': [
        '不可未確認飲食限制就隨意煮食（如糖尿病需低糖飲食）。',
        '不可備餐後不清理廚房。',
        '不可為同住非個案家庭成員大量備餐（應以個案為主）。',
    ],
    'mistakes': [
        {
            'q': '順便幫家屬也煮了一份，可以嗎？',
            'a': '服務以個案為主。可在合理範圍內一起備餐（例如多煮一人份），但不得作為主要服務內容。',
        },
        {
            'q': 'BA05 備餐 + BA04 餵食可以同時報嗎？',
            'a': '可以接續申報，但需分別記錄服務時間，確保各碼有實際執行內容。',
        },
    ],
    'details': [
        '含備餐、烹煮、膳食善後清潔。',
        '應依個案營養需求調整食材和烹調方式。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '可接續：<a href="#code-BA04">BA04</a>（協助進食）。',
        '分界：<a href="#code-BA15">BA15</a>（家務協助）不含個案備餐。',
    ],
})

# ===== BA07 =====
codes.append({
    'code': 'BA07', 'title': '協助沐浴及洗頭', 'unit': '1次',
    'price_normal': 420, 'price_remote': 505, 'category': '清潔沐浴',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助移位、穿脫衣服、沐浴（含洗頭）、弄濕部位清潔。',
        '給付價格 420 元（原住民族地區／離島 505 元）。',
        '同一時段不可併同 BA01 及 BA23。',
    ],
    'must_do': [
        '確認浴室安全（防滑墊、扶手、水溫調節）。',
        '協助移位時使用正確搬運技巧。',
        '全身沐浴含軀幹、四肢、頭部清洗。',
        '沐浴後確認皮膚狀況，擦乾保暖。',
        '清洗後穿衣、吹乾頭髮、安置回適當位置。',
        '記錄：皮膚狀況觀察、異常回報。',
    ],
    'must_not': [
        '不可同一時段另報 BA01（基本清潔）或 BA23（洗頭）。',
        '不可在個案身體狀況不穩定時強行沐浴（如發燒、血壓異常）。',
        '不可讓個案在浴室內獨處。',
        '不可省略沐浴後的保暖步驟。',
    ],
    'mistakes': [
        {
            'q': '沐浴時個案喊冷不想洗了，只洗了上半身，還能報 BA07 嗎？',
            'a': '視個案狀況彈性調整，據實記錄實際執行內容，仍可報 BA07。個案安全與意願優先。',
        },
        {
            'q': '沐浴完幫個案穿衣轉位，可以加報 BA02 嗎？',
            'a': '穿脫衣和轉位在 BA07 過程中完成的，屬該碼涵蓋範圍，不另報 BA02。',
        },
    ],
    'details': [
        '含移位、穿脫衣、沐浴、洗頭、弄濕部位清潔。',
        '得依第 21 條臨時先做後補。',
        '浴室環境需事先檢查：防滑、水溫、通風。',
    ],
    'conflict': [
        '同時段互斥：<a href="#code-BA01">BA01</a>（基本清潔）、<a href="#code-BA23">BA23</a>（協助洗頭）。',
        '不得與 <a href="#code-BA24">BA24</a>（協助排泄）在沐浴過程中併計。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）、<a href="#code-AA03">AA03</a>（體重過重加計）。',
    ],
})

# ===== BA08 =====
codes.append({
    'code': 'BA08', 'title': '足部照護', 'unit': '1次',
    'price_normal': 230, 'price_remote': 275, 'category': '清潔沐浴',
    'tags': [],
    'regulation': [
        '足部指甲修剪與足部照護。',
        '給付價格 230 元（原住民族地區／離島 275 元）。',
        '限領有認可訓練證明之照顧服務員執行。',
        '自 115 年 1 月 1 日施行。',
    ],
    'must_do': [
        '先泡腳軟化指甲（約 10-15 分鐘）。',
        '使用適當工具修剪（指甲鉗，非剪刀）。',
        '觀察足部皮膚狀況（龜裂、黴菌感染、雞眼、胼胝）。',
        '糖尿病個案特別注意周邊循環與傷口。',
        '記錄足部觀察與處理內容。',
    ],
    'must_not': [
        '不可修剪過深或修到甲溝（預防甲溝炎）。',
        '糖尿病個案不可自行處理傷口或厚繭。',
        '未取得認可訓練證明不得執行本碼。',
    ],
    'mistakes': [
        {
            'q': '個案手指甲也很長，順便剪一剪可以報 BA08 嗎？',
            'a': 'BA08 限足部照護，手指甲修剪不屬本碼範圍。',
        },
        {
            'q': '個案是糖尿病患者，足部有傷口，可以自己處理嗎？',
            'a': '糖尿病足部傷口屬醫療處置，應通報護理師或轉介醫療。',
        },
    ],
    'details': [
        '限領有認可訓練證明之照服員執行。',
        '含泡腳、指甲修剪、足部觀察與基礎照護。',
        '自 115 年 1 月 1 日施行。',
    ],
    'conflict': [
        '相關：<a href="#code-BA17d1">BA17d1</a>（血糖機驗血糖，糖尿病個案）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難）。',
    ],
})

# ===== BA09 =====
codes.append({
    'code': 'BA09', 'title': '協助上（下）樓梯', 'unit': '1次',
    'price_normal': 310, 'price_remote': 370, 'category': '交通外出',
    'tags': [],
    'regulation': [
        '協助個案上下樓梯（限無電梯公寓或需經樓梯進出之場所）。',
        '給付價格 310 元（原住民族地區／離島 370 元）。',
        '自 115 年 1 月 1 日施行。',
    ],
    'must_do': [
        '評估樓梯環境（寬度、扶手、照明）。',
        '上樓時照服員在後方保護；下樓時在前方保護。',
        '使用輔具（如移位腰帶）確保安全。',
        '記錄樓層數與個案狀況。',
    ],
    'must_not': [
        '不可在個案體力不支時強行上下樓。',
        '不可在無人協助下搬運輪椅個案上下樓。',
        '環境不安全時（如燈光不足、樓梯濕滑）應暫停並回報。',
    ],
    'mistakes': [
        {
            'q': '個案住 5 樓公寓，每次就醫都要下樓上樓，可以報 2 次嗎？',
            'a': '下樓一次、回程上樓一次，共 2 次獨立服務，可分別報。',
        },
    ],
    'details': [
        '限無電梯公寓或需經樓梯進出之場所。',
        '自 115 年 1 月 1 日施行。',
        '視個案失能程度決定是否需要兩名照服員協助。',
    ],
    'conflict': [
        '常搭配：<a href="#code-BA13">BA13</a>（陪同外出）、<a href="#code-BA14">BA14</a>（陪同就醫）。',
    ],
})

# ===== BA09a =====
codes.append({
    'code': 'BA09a', 'title': '協助上（下）樓梯（輪椅使用者）', 'unit': '1次',
    'price_normal': 440, 'price_remote': 530, 'category': '交通外出',
    'tags': [],
    'regulation': [
        '協助輪椅使用者上下樓梯（需 2 名以上服務人員或使用爬梯機）。',
        '給付價格 440 元（原住民族地區／離島 530 元）。',
        '自 115 年 1 月 1 日施行。',
    ],
    'must_do': [
        '至少 2 名照服員共同執行，或使用爬梯機。',
        '確認爬梯機或搬運器具功能正常。',
        '上下樓過程中全程固定輪椅安全帶。',
        '事前與個案及家屬溝通流程與注意事項。',
    ],
    'must_not': [
        '不可單人搬運輪椅個案上下樓。',
        '不可使用未經檢驗的搬運器具。',
        '環境不安全時不可強行執行。',
    ],
    'mistakes': [
        {
            'q': '只有一名照服員到場，個案急著要出門，可以先扛下去嗎？',
            'a': '絕對不行。必須等第二名人員到場或使用爬梯機。安全第一。',
        },
    ],
    'details': [
        '需 2 名以上服務人員或使用爬梯機。',
        '自 115 年 1 月 1 日施行。',
        '費用含 2 名照服員人力成本。',
    ],
    'conflict': [
        '常搭配：<a href="#code-BA13">BA13</a>（陪同外出）、<a href="#code-BA14">BA14</a>（陪同就醫）。',
        '分界：<a href="#code-BA09">BA09</a>（非輪椅使用者上下樓梯）。',
    ],
})

# ===== BA10 =====
codes.append({
    'code': 'BA10', 'title': '翻身拍背', 'unit': '1次',
    'price_normal': 155, 'price_remote': 185, 'category': '日常照顧',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助臥床個案翻身、拍背、肢體關節活動。',
        '給付價格 155 元（原住民族地區／離島 185 元）。',
        '原則每日以 3 組合為限。',
    ],
    'must_do': [
        '至少每 2 小時翻身一次（依護理計畫調整）。',
        '翻身後確認受壓部位有無紅腫、壓瘡徵兆。',
        '拍背順序：由下往上、由外向內。',
        '被動關節活動需注意力道，不可過度伸展。',
        '使用枕頭或楔形墊維持翻身後姿勢。',
    ],
    'must_not': [
        '不可拖拉個案身體（應使用翻身單或中單）。',
        '不可在骨折或手術部位執行被動關節活動。',
        '不可忽略翻身後的體位擺放（預防攣縮）。',
    ],
    'mistakes': [
        {
            'q': '個案拒絕翻身，說會痛，直接跳過。',
            'a': '應了解疼痛原因，回報護理師評估。不可完全不翻身（壓瘡風險）。可調整翻身角度或使用輔具減輕不適。',
        },
    ],
    'details': [
        '含翻身、拍背、肢體關節活動。',
        '得依第 21 條臨時先做後補。',
        '重點在預防壓瘡和維持關節活動度。',
    ],
    'conflict': [
        '可搭配其他 BA 碼接續使用。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）、<a href="#code-AA03">AA03</a>（體重過重加計）。',
    ],
})

# ===== BA11 =====
codes.append({
    'code': 'BA11', 'title': '肢體關節活動', 'unit': '1次',
    'price_normal': 310, 'price_remote': 370, 'category': '日常照顧',
    'tags': [],
    'regulation': [
        '針對長期臥床或行動不便者，執行肢體關節活動（含被動與主動協助運動）。',
        '給付價格 310 元（原住民族地區／離島 370 元）。',
    ],
    'must_do': [
        '依護理師或治療師指示執行運動項目。',
        '運動前先暖身，注意力道與角度。',
        '觀察個案反應（疼痛、腫脹即停止）。',
        '記錄各關節活動角度與個案反應。',
    ],
    'must_not': [
        '不可在急性期（如骨折、關節發炎）自行執行。',
        '不可超過醫療團隊指定的運動範圍。',
        '不可忽略個案疼痛反應強行執行。',
    ],
    'mistakes': [
        {
            'q': 'BA10 翻身拍背有含關節活動，BA11 和 BA10 有什麼不同？',
            'a': 'BA10 含「翻身拍背及肢體關節活動」是翻身時順便做的簡易活動；BA11 是專門安排的肢體關節運動課程，更有系統、時間更長。兩碼不可在同一時段申報。',
        },
    ],
    'details': [
        '含被動關節活動、主動協助運動。',
        '應依專業人員指導方案執行。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA10">BA10</a>（翻身拍背含簡易關節活動）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）。',
    ],
})

# ===== BA12 =====
codes.append({
    'code': 'BA12', 'title': '協助使用日常生活輔助器具', 'unit': '1次',
    'price_normal': 195, 'price_remote': 235, 'category': '日常照顧',
    'tags': [],
    'regulation': [
        '協助個案使用日常生活輔助器具（含穿脫義肢支架、助聽器、眼鏡等）。',
        '給付價格 195 元（原住民族地區／離島 235 元）。',
    ],
    'must_do': [
        '確認輔具功能正常（如助聽器電池、義肢固定扣）。',
        '依正確方式協助穿脫（避免皮膚磨損或壓傷）。',
        '觀察穿戴後皮膚狀況。',
        '記錄輔具使用狀況與個案適應情形。',
    ],
    'must_not': [
        '不可在皮膚有傷口處直接穿戴義肢或支架。',
        '不可自行調整義肢或支架的角度與鬆緊（需由輔具師處理）。',
    ],
    'mistakes': [
        {
            'q': '個案的助聽器壞了，可以幫忙修理嗎？',
            'a': '簡單處理如更換電池可以。但故障維修應轉介輔具廠商。',
        },
    ],
    'details': [
        '含義肢、支架、助聽器、眼鏡等日常輔具穿脫。',
        '不含輔具的維修與調整。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '可併用：<a href="#code-BA13">BA13</a>（陪同外出時穿戴輔具）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）。',
    ],
})

# ===== BA13 =====
codes.append({
    'code': 'BA13', 'title': '陪同外出', 'unit': '每30分鐘',
    'price_normal': 195, 'price_remote': 235, 'category': '交通外出',
    'tags': [],
    'regulation': [
        '陪同至醫療院所以外的地點，如至郵局辦事、採買日常用品、散步運動、參與社區活動。',
        '給付價格 195 元／每 30 分鐘（原住民族地區／離島 235 元）。',
        '含陪同至目的地及提供協助。',
    ],
    'must_do': [
        '確認外出目的與路線。',
        '攜帶必要物品（身分證件、藥物、聯絡資料）。',
        '全程陪同，注意行走安全。',
        '記錄外出目的地、路線、起迄時間。',
    ],
    'must_not': [
        '不可將個案獨留在外。',
        '不可趁陪同時處理自己的私事。',
        '不可陪同至不適當場所（如菸酒場所）。',
        '陪同就醫應用 BA14，不可以 BA13 替代。',
    ],
    'mistakes': [
        {
            'q': '個案想去公園散步 2 小時，可以報 4 單位 BA13 嗎？',
            'a': '可以，以 30 分鐘為一單位。但須確認核定額度是否足夠。',
        },
        {
            'q': '陪個案去醫院回診，用 BA13 報可以嗎？',
            'a': '不行，陪同就醫應使用 BA14。BA13 限醫療院所以外的地點。',
        },
    ],
    'details': [
        '限醫療院所以外之地點。',
        '含散步、採買、辦事、社區活動等。',
        '起點或終點須為個案住所或長照相關服務場所。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA14">BA14</a>（陪同就醫）。',
        '可併用：<a href="#code-BA12">BA12</a>（協助使用輔具）。',
        '可加計：<a href="#code-AA05">AA05</a>（特殊加計）。',
    ],
})

# ===== BA14 =====
codes.append({
    'code': 'BA14', 'title': '陪同就醫', 'unit': '每30分鐘',
    'price_normal': 195, 'price_remote': 235, 'category': '交通外出',
    'tags': [],
    'regulation': [
        '陪同至醫療院所就醫、復健。',
        '給付價格 195 元／每 30 分鐘（原住民族地區／離島 235 元）。',
        '原則每月以 1 次為限，超過 1.5 小時轉 BA13。',
    ],
    'must_do': [
        '事前確認掛號資料、攜帶健保卡。',
        '陪同就診全程在旁，協助描述症狀。',
        '記錄醫囑內容、回診時間。',
        '協助領藥、確認藥物。',
        '超過 1.5 小時的部分以 BA13 計算。',
    ],
    'must_not': [
        '不可代替個案簽署醫療同意書。',
        '不可自行決定就醫科別或更改掛號。',
        '不可在等候時離開個案。',
        '不可超時不報（超過 1.5 小時應轉 BA13）。',
    ],
    'mistakes': [
        {
            'q': '等候看診花了 3 小時，全部報 BA14 可以嗎？',
            'a': '前 1.5 小時報 BA14（3 組合），超過的部分轉報 BA13。',
        },
        {
            'q': '陪同就醫後順路去藥局拿藥，可以一起報 BA14 嗎？',
            'a': '拿藥屬就醫流程一部分，可含在 BA14 時間內。但領藥後另去採買就應報 BA13。',
        },
    ],
    'details': [
        '含陪同就醫、復健。',
        '原則每月 1 次為限，特殊需求經 A 個管評估可增加。',
        '超過 1.5 小時轉 BA13 計算。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA13">BA13</a>（陪同外出，非就醫）。超過 1.5 小時轉 BA13。',
        '搭配喘息：<a href="#code-GA09">GA09</a> 加計 BA14 時，時數需涵蓋喘息組數加 1.5 小時。',
        '可加計：<a href="#code-AA05">AA05</a>（特殊加計）。',
    ],
})

# ===== BA15 =====
codes.append({
    'code': 'BA15', 'title': '家務協助', 'unit': '每30分鐘',
    'price_normal': 195, 'price_remote': 235, 'category': '家務',
    'tags': [],
    'regulation': [
        '協助個案之換洗衣物洗滌及居家環境清潔。',
        '給付價格 195 元／每 30 分鐘（原住民族地區／離島 235 元）。',
        '限個案生活空間之清潔。',
    ],
    'must_do': [
        '清潔範圍以個案日常生活空間為主（臥室、浴室、客廳主要動線）。',
        '洗衣含洗滌、晾曬、摺疊。',
        '注意使用清潔劑的安全（通風、不混用）。',
        '記錄服務內容與完成情形。',
    ],
    'must_not': [
        '不可清潔個案生活空間以外的區域（如整棟房屋大掃除）。',
        '不可移動大型家具或爬高清潔。',
        '不可從事非個案相關的家務（如替家屬洗車、煮飯給家屬吃等）。',
    ],
    'mistakes': [
        {
            'q': '家屬要求打掃整棟透天厝，可以嗎？',
            'a': '限個案生活空間。如個案住 2 樓，以 2 樓為主。家屬如需大範圍清潔應另行安排。',
        },
        {
            'q': 'BA05 備餐後廚房清潔，算 BA15 嗎？',
            'a': 'BA05 備餐已含善後清潔，不另報 BA15。BA15 是獨立安排的居家環境清潔服務。',
        },
    ],
    'details': [
        '含換洗衣物洗滌、居家環境清潔。',
        '限個案日常生活空間。',
        '不含大型清掃、搬運或高處作業。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA05">BA05</a>（備餐已含廚房善後清潔）。',
        '不可加計：<a href="#code-AA05">AA05</a>（BA16 除外，BA15 也不加計 AA05）。',
    ],
})

# ===== BA16 =====
codes.append({
    'code': 'BA16', 'title': '代購或代領或代送服務', 'unit': '1次',
    'price_normal': 155, 'price_remote': 185, 'category': '家務',
    'tags': [],
    'regulation': [
        '代購日常用品、代領藥物或物品、代送文件等。',
        '給付價格 155 元（原住民族地區／離島 185 元）。',
    ],
    'must_do': [
        '確認代購清單、金額上限。',
        '保留收據，當日完成核對找零。',
        '代領藥物須確認藥袋資訊（姓名、藥品、用法）。',
        '記錄代購/代領項目與金額。',
    ],
    'must_not': [
        '不可代為保管大額現金或貴重物品。',
        '不可代購菸酒或不當物品。',
        '不可在無收據情況下完成代購。',
    ],
    'mistakes': [
        {
            'q': '個案請居服員代買 3 天份的菜，可以嗎？',
            'a': '可以代購日常用品含食材。需確認清單與金額，保留收據。',
        },
    ],
    'details': [
        '含代購日常用品、代領藥物、代送文件。',
        '需保留收據並當日核對。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '不可加計：<a href="#code-AA05">AA05</a>（BA16 不加計 AA05）。',
    ],
})

# ===== BA17a =====
codes.append({
    'code': 'BA17a', 'title': '協助執行輔助性醫療', 'unit': '1次',
    'price_normal': 65, 'price_remote': 80, 'category': '醫療相關',
    'tags': ['可臨時先做後補', '需認可訓練'],
    'regulation': [
        '依護理師開立之照護計畫執行輔助性醫療（如傷口換藥、熱敷等）。',
        '給付價格 65 元（原住民族地區／離島 80 元）。',
        '須領有認可訓練證明。',
    ],
    'must_do': [
        '依護理師照護計畫執行。',
        '執行前確認醫材有效期限與無菌狀態。',
        '確實記錄傷口狀況（大小、顏色、滲液量、氣味）。',
        '發現傷口惡化立即通報。',
    ],
    'must_not': [
        '不可超出護理師照護計畫範圍自行決定換藥方式。',
        '不可使用過期醫材。',
        '未取得認可訓練不得執行。',
    ],
    'mistakes': [
        {
            'q': '個案傷口比上次大了，可以自行更換敷料種類嗎？',
            'a': '不可以。應通報護理師重新評估傷口照護計畫。照服員只能依指示執行。',
        },
    ],
    'details': [
        '含傷口換藥、熱敷等輔助性醫療。',
        '須領有認可訓練證明。',
        '得依第 21 條臨時先做後補。',
    ],
    'conflict': [
        '相關：<a href="#code-BA17b">BA17b</a>（依指示使用藥膏或乳液塗抹之照護）。',
    ],
})

# ===== BA17b =====
codes.append({
    'code': 'BA17b', 'title': '依指示使用乳液或藥膏塗抹', 'unit': '1次',
    'price_normal': 50, 'price_remote': 60, 'category': '醫療相關',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '依指示使用藥膏或乳液塗抹之照護。',
        '給付價格 50 元（原住民族地區／離島 60 元）。',
    ],
    'must_do': [
        '確認藥膏名稱、用途與使用部位是否與醫囑相符。',
        '確認保存期限。',
        '戴手套操作，避免交叉感染。',
        '記錄塗抹部位與皮膚反應。',
    ],
    'must_not': [
        '不可自行選用藥膏（需依醫囑或護理師指示）。',
        '不可在開放性傷口上直接塗抹（需經醫療評估）。',
    ],
    'mistakes': [
        {
            'q': '個案皮膚乾燥，可以自己買乳液幫他擦嗎？',
            'a': '需依照核定計畫或護理師指示使用指定乳液或藥膏。自行購買的不屬本碼範圍。',
        },
    ],
    'details': [
        '含依指示塗抹藥膏或乳液。',
        '不要求認可訓練。',
        '得依第 21 條臨時先做後補。',
    ],
    'conflict': [
        '相關：<a href="#code-BA17a">BA17a</a>（輔助性醫療含傷口換藥）。',
    ],
})

# ===== BA17c =====
codes.append({
    'code': 'BA17c', 'title': '尿管及鼻胃管之清潔與固定', 'unit': '1次',
    'price_normal': 50, 'price_remote': 60, 'category': '醫療相關',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '尿管及鼻胃管之清潔與固定。',
        '給付價格 50 元（原住民族地區／離島 60 元）。',
    ],
    'must_do': [
        '確認管路固定位置未滑脫。',
        '清潔管路周圍皮膚，觀察有無紅腫感染。',
        '固定膠帶定期更換，避免皮膚損傷。',
        '觀察引流液顏色、量、性狀並記錄。',
    ],
    'must_not': [
        '不可自行拔除或重新插入管路。',
        '發現管路滑脫不可自行回插（通報護理師或就醫）。',
        '不可忽略管路周圍皮膚照護。',
    ],
    'mistakes': [
        {
            'q': '鼻胃管的膠帶鬆了，可以自己重新貼嗎？',
            'a': '重新固定膠帶屬本碼範圍可以做。但如果管路已滑出，必須通報護理師處理。',
        },
    ],
    'details': [
        '含尿管及鼻胃管周圍清潔與固定。',
        '不要求認可訓練。',
        '得依第 21 條臨時先做後補。',
    ],
    'conflict': [
        '相關：<a href="#code-BA04">BA04</a>（管灌前確認管路）。',
    ],
})

# ===== BA17d1 =====
codes.append({
    'code': 'BA17d1', 'title': '血糖機驗血糖', 'unit': '1次',
    'price_normal': 50, 'price_remote': 60, 'category': '醫療相關',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '攜帶式血糖機驗血糖。',
        '給付價格 50 元（原住民族地區／離島 60 元）。',
        '原則每日以 1 組合為限。',
    ],
    'must_do': [
        '洗手、酒精消毒待乾、指腹側邊採血。',
        '確認試紙未過期、機器已校正。',
        '記錄數值、時間、餐前或餐後。',
        '異常值立即通知督導及護理師。',
        '針頭依規定丟棄（銳器盒）。',
    ],
    'must_not': [
        '不可重複使用採血針。',
        '不可只記錄「正常」而不記數值。',
        '異常值不可隱匿不報。',
    ],
    'mistakes': [
        {
            'q': '家屬要求早晚各量一次血糖，可以報 2 次嗎？',
            'a': '原則每日 1 組合為限。額外需求依 A 個管評估核定。',
        },
    ],
    'details': [
        '使用攜帶式血糖機。',
        '得依第 21 條臨時先做後補。',
        '需熟悉各品牌血糖機操作方式。',
    ],
    'conflict': [
        '相關：<a href="#code-BA17e">BA17e</a>（置入藥盒含血糖藥）、<a href="#code-BA08">BA08</a>（足部照護，糖尿病個案）。',
    ],
})

# ===== BA17d2 =====
codes.append({
    'code': 'BA17d2', 'title': '甘油球通便', 'unit': '1次',
    'price_normal': 50, 'price_remote': 60, 'category': '醫療相關',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '甘油球通便。',
        '給付價格 50 元（原住民族地區／離島 60 元）。',
        '原則每週以 3 組合為限；特殊情況得由 A 個管評估。',
    ],
    'must_do': [
        '左側臥屈膝、潤滑管口、緩慢插入。',
        '請個案保留 5～10 分鐘後排便。',
        '觀察排便量、性狀、顏色。',
        '事後清潔個案會陰及臀部。',
    ],
    'must_not': [
        '不可硬塞、多次強行灌入。',
        '有肛門出血仍執行。',
        '不可超過核定次數未報告。',
    ],
    'mistakes': [
        {
            'q': '個案便秘嚴重，家屬要求每天都用甘油球。',
            'a': '原則每週 3 組合為限。先回報 A 個管，依評估走專案核給。',
        },
    ],
    'details': [
        '使用甘油球通便。',
        '得依第 21 條臨時先做後補。',
        '注意個案有無肛門相關疾病或手術史。',
    ],
    'conflict': [
        '相關：<a href="#code-BA24">BA24</a>（協助排泄）。',
    ],
})

# ===== BA17e =====
codes.append({
    'code': 'BA17e', 'title': '依指示置入藥盒', 'unit': '1次',
    'price_normal': 50, 'price_remote': 60, 'category': '醫療相關',
    'tags': [],
    'regulation': [
        '依照藥袋指示置入藥盒。',
        '給付價格 50 元（原住民族地區／離島 60 元）。',
        '原則每週以 1 組合為限。',
    ],
    'must_do': [
        '核對藥袋姓名、藥名、劑量、時間。',
        '依藥袋指示分裝入藥盒（早、中、晚、睡前）。',
        '分裝完請個案或家屬複核確認。',
        '記錄分藥內容與日期。',
    ],
    'must_not': [
        '不可憑記憶分藥（每次必須核對藥袋）。',
        '不可自行拆開膠囊、磨粉。',
        '不可把「協助服藥」也報 BA17e（服藥屬 BA02）。',
    ],
    'mistakes': [
        {
            'q': '個案拿了新藥回來，藥袋上沒有詳細說明，可以自己判斷放哪一格嗎？',
            'a': '不可以。應請個案或家屬確認或致電藥局/醫院諮詢後再分藥。',
        },
    ],
    'details': [
        '依藥袋指示置入藥盒。',
        '本碼不在臨時服務名單內。',
        '分藥是 BA17e，協助服藥是 BA02，兩者不同。',
    ],
    'conflict': [
        '分界：<a href="#code-BA02">BA02</a>（協助用藥/服藥）。',
        '相關：<a href="#code-BA17d1">BA17d1</a>（血糖機驗血糖，血糖藥分藥時注意）。',
    ],
})

# ===== BA18 =====
codes.append({
    'code': 'BA18', 'title': '安全看視', 'unit': '每30分鐘',
    'price_normal': 200, 'price_remote': 240, 'category': '陪伴看視',
    'tags': ['不得與其他組合併用'],
    'regulation': [
        '至案家陪伴、支持、看視注意安全。',
        '給付價格 200 元／每 30 分鐘（原住民族地區／離島 240 元）。',
        '限心智障礙者使用。',
        '不得與其他組合併同使用，但可接續。',
    ],
    'must_do': [
        '全程在場、視線不離開。',
        '安排有意義的活動（如簡單遊戲、音樂、繪畫等）。',
        '記錄行為狀況（情緒、異常行為、與人互動）。',
        '注意居家安全（瓦斯、電器、尖銳物品）。',
    ],
    'must_not': [
        '看視期間不可同時做家務再另報其他碼。',
        '非心智障礙者不可使用本碼（一般陪伴用 BA20）。',
        '不可在看視期間離開個案視線範圍。',
    ],
    'mistakes': [
        {
            'q': '看視時個案想上廁所，可以協助後另報 BA02 嗎？',
            'a': '可協助如廁，但屬看視內容，不得另報 BA02。',
        },
        {
            'q': '心智障礙個案行為穩定，可以用 BA20 比較便宜嗎？',
            'a': '依 A 個管核定。BA18 專為心智障礙者設計，有安全看視的專業要求。',
        },
    ],
    'details': [
        '限心智障礙者使用。',
        '不得與其他組合併同使用。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA20">BA20</a>（一般陪伴服務）。',
        '可加計：<a href="#code-AA11">AA11</a>、<a href="#code-AA05">AA05</a>。',
    ],
})

# ===== BA20 =====
codes.append({
    'code': 'BA20', 'title': '陪伴服務', 'unit': '每30分鐘',
    'price_normal': 175, 'price_remote': 210, 'category': '陪伴看視',
    'tags': ['不得與其他組合併用'],
    'regulation': [
        '至案家陪伴看視、日常生活參與，或讀紙本或電子新聞或書信。',
        '給付價格 175 元／每 30 分鐘（原住民族地區／離島 210 元）。',
        '不得與其他組合併同使用。',
    ],
    'must_do': [
        '有內容的陪伴（聊天、讀報、共同活動），不可只是坐著滑手機。',
        '觀察情緒、認知變化，異常狀況回報。',
        '獨立記錄起迄時間與陪伴內容。',
    ],
    'must_not': [
        '陪伴時間內不可同時做 BA02、BA15 再各報。',
        '外出時不可用 BA20（應為 BA13）。',
        '不可以 BA20 執行熱敷理療、刮痧（非屬日常生活參與）。',
    ],
    'mistakes': [
        {
            'q': '家屬希望聊天陪伴 2 小時，可以嗎？',
            'a': '可以，核定 4 單位 BA20。但陪伴期間不得夾雜其他服務碼別申報。',
        },
        {
            'q': '陪伴時個案想出去走走，可以直接出門嗎？',
            'a': '外出應用 BA13。如需變更服務內容需先回報督導。',
        },
    ],
    'details': [
        '含陪伴看視、日常生活參與、讀報讀信。',
        '不得與其他組合併同使用。',
        '本碼不在臨時服務名單內。',
    ],
    'conflict': [
        '分界：<a href="#code-BA18">BA18</a>（限心智障礙者之安全看視）、<a href="#code-BA13">BA13</a>（外出陪同）。',
        '可加計：<a href="#code-AA11">AA11</a>。',
    ],
})

# ===== BA22 =====
codes.append({
    'code': 'BA22', 'title': '巡視服務', 'unit': '1次含至少3次探視',
    'price_normal': 130, 'price_remote': 160, 'category': '陪伴看視',
    'tags': [],
    'regulation': [
        '上午 6 點至晚上 8 點，至案家探視至少 3 次。',
        '給付價格 130 元（原住民族地區／離島 160 元）。',
        '不得搭配其他照顧組合。',
        '非規定時段得加計 AA08。',
    ],
    'must_do': [
        '每次探視須記錄（時間、觀察內容）。',
        '簡易協助含翻身、換尿片、確認用藥。',
        '發現突發需求可依第 21 條臨時提供服務後通報。',
        '3 次探視需有合理間隔。',
    ],
    'must_not': [
        '不可同日與其他碼別搭配申報。',
        '3 次未達不可申報。',
        '不可只打電話取代實際到案家探視。',
    ],
    'mistakes': [
        {
            'q': '巡視時個案跌倒了怎麼辦？',
            'a': '先確保安全，可依第 21 條臨時提供 BA01 等必要服務，之後通知 A 個管。',
        },
        {
            'q': '探視 3 次每次 5 分鐘就走了，可以嗎？',
            'a': '臺東縣建議每次 10 分鐘內、間隔 2 小時以上。應有實質觀察與協助。',
        },
    ],
    'details': [
        '限上午 6 點至晚上 8 點。',
        '至少 3 次探視，含簡易協助。',
        '臺東縣建議每次 10 分鐘內，間隔 2 小時以上。',
    ],
    'conflict': [
        '不得搭配：所有其他照顧組合。',
        '可加計：<a href="#code-AA08">AA08</a>（非規定時段）。',
    ],
})

# ===== BA23 =====
codes.append({
    'code': 'BA23', 'title': '協助洗頭', 'unit': '1次',
    'price_normal': 200, 'price_remote': 240, 'category': '清潔沐浴',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助移位、穿脫衣服、洗頭、弄濕部位清潔。',
        '給付價格 200 元（原住民族地區／離島 240 元）。',
        '同一時段不可併同 BA01 及 BA07。',
    ],
    'must_do': [
        '床上洗頭使用洗頭槽，確認排水順暢。',
        '水溫確認（不可過燙，建議 38-40 度）。',
        '洗後吹乾保暖，避免受涼。',
        '觀察頭皮狀況（疥瘡、皮屑、傷口）。',
    ],
    'must_not': [
        '同一時段不可併報 BA01 或 BA07。',
        '不可在浴間做了全身沐浴卻只報 BA23。',
        '不可使用過熱的水。',
    ],
    'mistakes': [
        {
            'q': '洗頭順便擦背可以加報 BA01 嗎？',
            'a': '不行。單獨洗頭是 BA23。擦背加沐浴才是 BA07。同時段互斥。',
        },
    ],
    'details': [
        '含移位、穿脫衣服、洗頭、弄濕部位清潔。',
        '得依第 21 條臨時先做後補。',
        '床上洗頭或坐姿洗頭均適用。',
    ],
    'conflict': [
        '同時段互斥：<a href="#code-BA01">BA01</a>（基本清潔）、<a href="#code-BA07">BA07</a>（協助沐浴及洗頭）。',
        '可加計：<a href="#code-AA11">AA11</a>（移位困難加計）、<a href="#code-AA03">AA03</a>（體重過重加計）。',
    ],
})

# ===== BA24 =====
codes.append({
    'code': 'BA24', 'title': '協助排泄', 'unit': '1次',
    'price_normal': 220, 'price_remote': 265, 'category': '清潔沐浴',
    'tags': ['可臨時先做後補'],
    'regulation': [
        '協助排泄及清潔照護。含嘔吐物處理、失禁清理、造口照護等。',
        '給付價格 220 元（原住民族地區／離島 265 元）。',
        '如於 BA01 或 BA07 過程中同時執行不得併計。',
        '衛部顧字第1121961389號：本碼不應例行核予，以臨時性需求為原則。',
    ],
    'must_do': [
        '用於非預期的嘔吐、失禁處理。',
        '觀察排泄物（量、色、形態、氣味）並記錄。',
        '造口照護（更換造口袋、清潔周圍皮膚）。',
        '失禁處理（清潔會陰、更換衣物床單）。',
        '給予排泄相關衛教指導。',
    ],
    'must_not': [
        '不可當固定排程每天申報（本碼以臨時性為原則）。',
        '不可在 BA01/BA07 過程中另報 BA24。',
        '單純協助如廁不可報 BA24（屬 BA02）。',
    ],
    'mistakes': [
        {
            'q': '個案每天需要倒尿袋，可以每天報 BA24 嗎？',
            'a': '倒尿袋是例行照護屬 BA02 範圍。BA24 是針對臨時性排泄異常（如大量失禁、嘔吐、造口袋破裂）。',
        },
        {
            'q': '早上 BA07 沐浴，下午個案造口袋需更換，可以報 BA24 嗎？',
            'a': '可以。下午的造口袋更換是獨立事件，不在 BA07 過程中，可報 BA24。',
        },
        {
            'q': '個案長期失禁，每次服務都需要清理，可以每次加報 BA24 嗎？',
            'a': '需回報 A 個管評估。長期失禁可能需要調整照顧計畫，不適合以臨時碼每次加報。',
        },
    ],
    'details': [
        '含嘔吐物處理、失禁清理、造口照護、排泄觀察記錄。',
        '得依第 21 條臨時先做後補。',
        '各縣市審核趨嚴，以臨時性需求為原則。',
    ],
    'conflict': [
        '不得併計：<a href="#code-BA01">BA01</a>（過程中）、<a href="#code-BA07">BA07</a>（過程中）。',
        '分界：<a href="#code-BA02">BA02</a>（日常協助如廁、倒尿袋）。',
        '相關：<a href="#code-BA17d2">BA17d2</a>（甘油球通便）。',
    ],
})

# ===== GA09 =====
ga09 = {
    'code': 'GA09', 'title': '居家喘息服務', 'unit': '每2小時',
    'price_normal': 770, 'price_remote': 925, 'category': '喘息',
    'tags': [],
    'badge_class': 'ga',
    'regulation': [
        '居家喘息服務。以 2 小時為 1 單位，單日上限 10 小時（5 單位）。',
        '給付價格 770 元／每 2 小時（原住民族地區／離島 925 元）。',
        '喘息額度獨立：第 2-6 級 32,340 元/年、第 7-8 級 48,510 元/年。',
        '照顧者需離開現場或在家休息，以紓解其照顧壓力為目的。',
        '衛部顧字第1111960819號：喘息服務期間之照顧內容，由照顧服務員視個案需求提供。',
    ],
    'must_do': [
        '與家屬（照顧者）議定照顧內容。',
        '加計 BA14 時，時數需涵蓋喘息組數加 1.5 小時。',
        '例假日提供服務可加計 AA09。',
        '確實記錄服務時間與照顧內容。',
        '全程陪伴個案，不可離開。',
    ],
    'must_not': [
        '喘息時段內不可另拆 BA 碼申報（喘息已含照顧服務費用）。',
        '單日不可超過 10 小時（5 組合）。',
        '喘息期間不可帶個案外出購物（非屬喘息目的）。',
        '不可在照顧者未離場或未休息的情況下申報喘息。',
    ],
    'mistakes': [
        {
            'q': '照顧者只需要出門 1 小時，可以報半單位嗎？',
            'a': '不行。喘息以 2 小時為最小單位。不足 2 小時仍以 1 組合計。',
        },
        {
            'q': '喘息額度快用完了，可以用照顧服務額度補嗎？',
            'a': '不行。喘息額度獨立，不可與照顧及專業服務額度互相流用。',
        },
        {
            'q': '喘息期間個案需要就醫怎麼辦？',
            'a': '通知照顧者。如為緊急就醫可依第 21 條處理。喘息時段內不另報 BA14。',
        },
        {
            'q': '個案聘僱外籍看護工，可以使用喘息服務嗎？',
            'a': '聘僱外國人從事家庭看護工作者，以百分之三十額度用於專業服務為限，另含喘息額度依規定使用。',
        },
    ],
    'details': [
        '以 2 小時為一單位，單日上限 10 小時。',
        '喘息額度獨立（不與照顧服務額度共用）。',
        '114 年 9 月 1 日施行修正放寬陪同運動地點限制。',
        '喘息期間之照顧內容由照服員視需求提供，不另外拆碼。',
    ],
    'conflict': [
        '加計：<a href="#code-BA14">BA14</a>（陪同就醫，時數需涵蓋喘息組數加 1.5 小時）。',
        '加計：<a href="#code-AA09">AA09</a>（例假日加計）、<a href="#code-AA05">AA05</a>（特殊加計）。',
        '不可拆報任何 BA 碼。',
    ],
}


def gen_mistakes_html(mistakes):
    """Generate mistake Q&A HTML."""
    html = ''
    for m in mistakes:
        html += f'            <div class="scenario-item">\n'
        html += f'              <div class="scenario-q">⚠️ {m["q"]}</div>\n'
        html += f'              <div class="scenario-a"><strong>正確做法：</strong>{m["a"]}</div>\n'
        html += f'            </div>\n'
    return html


def gen_card(c):
    """Generate one card's HTML."""
    badge_class = c.get('badge_class', '')
    badge_cls = f' {badge_class}' if badge_class else ''

    # Tags
    tags_html = ''
    for tag in c.get('tags', []):
        if '臨時' in tag:
            tags_html += f'          <span class="tag temp-tag">🔄 {tag}</span>\n'
        elif '認可' in tag:
            tags_html += f'          <span class="tag cert-tag">📜 {tag}</span>\n'
        elif '併用' in tag:
            tags_html += f'          <span class="tag exclusive-tag">⚠️ {tag}</span>\n'
        else:
            tags_html += f'          <span class="tag">{tag}</span>\n'

    category_html = f'          <span class="category-tag">{c["category"]}</span>\n' if c.get('category') else ''

    html = f'''      <!-- {c["code"]} -->
      <div class="card" id="code-{c["code"]}">
        <div class="card-header">
          <span class="arrow">▶</span>
          <span class="code-badge{badge_cls}">{c["code"]}</span>
          <span class="title">{c["title"]}</span>
          <span class="price">￥{c["price_normal"]}</span>
        </div>
        <div class="card-body">
{category_html}{tags_html}          <div class="sub-tabs">
            <button class="sub-tab regulation" data-target="regulation">附表規定</button>
            <button class="sub-tab must-do" data-target="must-do">一定要做</button>
            <button class="sub-tab must-not" data-target="must-not">絕對不要</button>
            <button class="sub-tab mistakes" data-target="mistakes">常見誤區</button>
            <button class="sub-tab details" data-target="details">執行細節</button>
            <button class="sub-tab conflict" data-target="conflict">互斥搭配</button>
          </div>
          <div class="sub-content regulation">
            <h4>📄 附表規定</h4>
            <div class="price-info">💰 單位：{c["unit"]}｜一般 {c["price_normal"]}元 ／ 原民離島 {c["price_remote"]}元</div>
            <ul>
'''
    for item in c['regulation']:
        html += f'              <li>{item}</li>\n'

    html += f'''            </ul>
          </div>
          <div class="sub-content must-do">
            <h4>✅ 一定要做</h4>
            <ul>
'''
    for item in c['must_do']:
        html += f'              <li>{item}</li>\n'

    html += f'''            </ul>
          </div>
          <div class="sub-content must-not">
            <h4>🚫 絕對不要</h4>
            <ul>
'''
    for item in c['must_not']:
        html += f'              <li>{item}</li>\n'

    html += f'''            </ul>
          </div>
          <div class="sub-content mistakes">
            <h4>⚠️ 常見誤區</h4>
{gen_mistakes_html(c["mistakes"])}          </div>
          <div class="sub-content details">
            <h4>🔍 執行細節</h4>
            <ul>
'''
    for item in c['details']:
        html += f'              <li>{item}</li>\n'

    html += f'''            </ul>
          </div>
          <div class="sub-content conflict">
            <h4>🔀 互斥與搭配</h4>
            <ul>
'''
    for item in c['conflict']:
        html += f'              <li>{item}</li>\n'

    html += '''            </ul>
          </div>
        </div>
      </div>

'''
    return html


# Generate all BA cards
ba_cards_html = ''
for c in codes:
    ba_cards_html += gen_card(c)

# Generate GA09 card
ga09_html = gen_card(ga09)

# Generate conflicts table
conflicts_table = '''  <section id="conflicts" class="section">
    <h2 class="section-title"><span class="icon">🔀</span> 互斥與臨時服務速查</h2>
    <div style="overflow-x:auto">
      <table class="ref-table">
        <thead>
          <tr>
            <th style="width:28%">情境</th>
            <th style="width:35%">規定</th>
            <th style="width:37%">怎麼做</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>BA01／BA07／BA23</strong><br>同時段互斥</td>
            <td>基本清潔、沐浴洗頭、單獨洗頭三碼同一時段只能擇一</td>
            <td>做了沐浴（BA07）就不另報基本清潔（BA01）或洗頭（BA23）</td>
          </tr>
          <tr>
            <td><strong>BA24</strong><br>與 BA01/BA07 過程中不得併計</td>
            <td>協助排泄在沐浴或清潔過程中執行不另報</td>
            <td>BA24 以臨時性需求為原則，不在 BA01/BA07 過程中另計；獨立事件可報</td>
          </tr>
          <tr>
            <td><strong>BA02／BA18／BA20／BA22</strong><br>不得與其他組合併用</td>
            <td>這四碼各自不得與其他照顧組合併同使用</td>
            <td>服務時段內只做該碼內容，可「接續」其他碼但不可「併同」</td>
          </tr>
          <tr>
            <td><strong>BA13 與 BA12</strong><br>可併用</td>
            <td>陪同外出時可同時協助使用輔具</td>
            <td>出門前穿戴輔具報 BA12，接著陪同外出報 BA13</td>
          </tr>
          <tr>
            <td><strong>BA14 超過 1.5 小時</strong><br>轉 BA13</td>
            <td>陪同就醫超過 1.5 小時，超出部分改以 BA13 計算</td>
            <td>前 1.5 小時報 BA14（3 組合），超過的以 BA13 每 30 分鐘計</td>
          </tr>
          <tr>
            <td><strong>AA08 與 AA09</strong><br>同日不得同時申請</td>
            <td>非規定時段加計與例假日加計不可同日併報</td>
            <td>選擇其中一種加計申報</td>
          </tr>
          <tr>
            <td><strong>AA05 加計</strong><br>BA16 除外</td>
            <td>BA16（代購代領）不可加計 AA05</td>
            <td>其他 BA 碼視條件可加計 AA05，但 BA16 不行</td>
          </tr>
          <tr>
            <td><strong>第 21 條臨時先做後補</strong></td>
            <td>BA01、BA03、BA04、BA07、BA10、BA17a~d2、BA23、BA24 可臨時先做後補</td>
            <td>先執行服務→24小時內通報督導→督導聯繫 A 個管補入計畫</td>
          </tr>
          <tr>
            <td><strong>不得臨時提供</strong></td>
            <td>BA02、BA05、BA08、BA09(a)、BA11、BA12、BA13、BA14、BA15、BA16、BA17e、BA18、BA20、BA22</td>
            <td>這些碼必須事先納入照顧計畫才能執行</td>
          </tr>
          <tr>
            <td><strong>聘僱外籍看護工個案</strong></td>
            <td>給付額度百分之三十，限用於專業服務照顧組合</td>
            <td>BA 碼受限，另有獨立喘息額度可用</td>
          </tr>
          <tr>
            <td><strong>BA13／BA14 起終點</strong></td>
            <td>起點或終點須為個案住所或長照相關服務場所</td>
            <td>不可從 A 點到 B 點都不經過個案住所</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>'''

# Now read the original file and replace sections
import re

with open('/home/claude/home-care-handbook/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# === 1. Replace BA cards section ===
# Find: everything between <div id="manual-section"> and its closing </div>\n  </section>
# which is lines 73 (0-indexed 72) through 1786 (0-indexed 1785)
ba_start_marker = '<div id="manual-section">'
ba_end_marker = '</div>\n  </section>\n\n  <!-- === GA Codes === -->'

ba_start = content.find(ba_start_marker)
ba_end = content.find(ba_end_marker)
if ba_start == -1 or ba_end == -1:
    raise ValueError("Could not find BA section markers")

new_ba_section = ba_start_marker + '\n\n' + ba_cards_html + '    </div>\n  </section>\n\n  <!-- === GA Codes === -->'
content = content[:ba_start] + new_ba_section + content[ba_end + len(ba_end_marker):]

# === 2. Replace GA09 card ===
ga_start_marker = '<div id="ga-section">'
ga_end_marker = '</div>\n  </section>\n\n\n  <!-- === Conflicts Table === -->'

ga_start = content.find(ga_start_marker)
ga_end = content.find(ga_end_marker)
if ga_start == -1 or ga_end == -1:
    raise ValueError("Could not find GA section markers")

new_ga_section = ga_start_marker + '\n\n' + ga09_html + '    </div>\n  </section>\n\n\n  <!-- === Conflicts Table === -->'
content = content[:ga_start] + new_ga_section + content[ga_end + len(ga_end_marker):]

# === 3. Replace conflicts table ===
conflicts_start_marker = '<!-- === Conflicts Table === -->\n  <section id="conflicts"'
conflicts_end_marker = '</table>\n    </div>\n  </section>\n\n  <!-- === Scenarios === -->'

conflicts_start = content.find(conflicts_start_marker)
conflicts_end = content.find(conflicts_end_marker)
if conflicts_start == -1 or conflicts_end == -1:
    raise ValueError("Could not find conflicts section markers")

new_conflicts = '<!-- === Conflicts Table === -->\n' + conflicts_table + '\n\n  <!-- === Scenarios === -->'
content = content[:conflicts_start] + new_conflicts + content[conflicts_end + len(conflicts_end_marker):]

# Write updated file
with open('/home/claude/home-care-handbook/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ index.html updated successfully!")
print(f"  Total length: {len(content)} characters")
lines = content.split('\n')
print(f"  Total lines: {len(lines)}")
