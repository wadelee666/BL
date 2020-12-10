import bluetooth

socket.setdefaulttimeout(5)
esp = 'C4:4F:33:3A:5B:83'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

 
while True:
	a = input()
	sock.connect((esp,port))
	if a == 'o':
		sock.send('g'.ljust(16))		# Windows和 Linux應該可以直接發送
		data = sock.recv(1)
		sock.close()
		print(data)
	if a == 'H':
		sock.send('H')
		sock.close()
	if a == 'L':
		sock.send('L')
		sock.close()
