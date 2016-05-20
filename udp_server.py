from socket import *
import time
udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(("", 5002))
# tcp_server.listen(5)
# client, client_info = tcp_server.accept()
while True:
	recv_data, addr = udp_server.recvfrom(1024)
	time.sleep(1)
	print(time.strftime('%Y-%m-%d %H:%M:%S'))
	print("You: %s"%recv_data.decode('utf-8'))
	if recv_data == "你好".encode('utf-8'):
		time.sleep(1)
		print(time.strftime('%Y-%m-%d %H:%M:%S'))
		print("你好, 傻妞")
	elif recv_data == "quit".encode('utf-8'):
		# client.close()
		tcp_server.close()
	else:
		time.sleep(1)
		print(time.strftime('%Y-%m-%d %H:%M:%S'))
		print("Me: %s"%recv_data.decode('utf-8'))

