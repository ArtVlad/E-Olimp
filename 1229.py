max = 200001;
tag   = [0]*max;
def Ejler():
	global tag, max
	ejler = [0]*max
	for i in range(1, max):
		ejler[i] = i
		
	for i in range(2, max):
		if ejler[i] == i:
			for j in range(i, max, i):
				ejler[j] -= ejler[j] / i
	
		for j in range(1, max):
			if i * j >= max:
				break
			tag[j * i] += j * ejler[i]
	
	for i in range(1, max):
		tag[i] += tag[i - 1]

Ejler()
while True:
	n = int(input())
	if n == 0:
		break
	print(int(tag[n]))
