from socket import *
tcp_client = socket(AF_INET, SOCK_STREAM)

tcp_client.connect(("zhouhua.me", 5001))
while True:
	msg = input(">")
	if msg == "quite":
		break
	else:
 		tcp_client.send(bytes(msg, encoding = 'utf-8'))

tcp_client.close()
