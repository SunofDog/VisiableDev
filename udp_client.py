from socket import *
udp_client = socket(AF_INET, SOCK_DGRAM)

# tcp_client.connect(("zhouhua.me", 5001))
while True:
	msg = input(">")
	if msg == "quite":
		break
	else:
 		udp_client.sendto(bytes(msg, encoding = 'utf-8'), (("localhost", 5002)))

tcp_client.close()
