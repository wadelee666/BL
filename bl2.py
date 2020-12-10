import bluetooth

esp = 'C4:4F:33:3A:5B:83'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

 
while True:
	a = input()
	if a == 'o':
		sock.connect((esp,port))
		sock.send('g'.ljust(16))		# Windows和 Linux應該可以直接發送
		data = sock.recv(1)
		sock.close()
		print(data)
	if a == 'h':
		sock.connect((esp,port))
		sock.send('H')
		sock.close()
	if a == 'l':
		sock.connect((esp,port))
		sock.send('L')
		sock.close()
	if a == 'k':
		break
