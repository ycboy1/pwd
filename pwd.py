password = 'a123456'
i = 3
while i > 0 :
	i = i - 1
	pwd = input('請輸入你的密碼：')
	if pwd == password :
		print('你的密碼正確')
		break
	else :
		print('密碼輸入錯誤')
		if i > 0 :
			print('還有', i , '次機會')
		else :
			print('你沒有機會了，要鎖帳號')
	