import random
i = 0
r = random.randint(1, 100)
while True:
	guess = input("請輸入一個數字:")
	guess = int(guess)
	i = i + 1
	if guess == r:
		print ("猜對了!")
		print("這是你猜的第" , i, "次")
		break
	elif guess > r:
		print ("比答案大")
	else:
		print ("比答案小")
	print("這是你猜的第" , i, "次")