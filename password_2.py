#password retry 
#password='a123456'
#retry 3 times then break 
#correct => print('登入成功!') and back retry
#wrong => print('密碼錯誤!剩餘?次')

password = 'a123456'
i = 3
while i > 0:  #條件可以是True寫法,也可以添加真正的條件,
	          #當i>0時就可以重複以下動作
	  i = i - 1
	  pwd = input('請輸入密碼 : ')
	  if pwd == password:
	  	 print('登入成功')
		 break
	  else:
	     print('密碼錯誤! 還有',i ,'次機會')
	     # if i == 0: >>>因為i = 0才能重複執行,所以這一行就可以不用存在
	  	 break
		