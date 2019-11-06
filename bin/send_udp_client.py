import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = input("请输入要发送的内容：")  # 字符串类型， 通过msg.encode() 编码 转换为bytes类型
server_address = ("10.196.247.110", 8000)  # 接收方 服务器的ip地址和端口号
client_socket.sendto(msg.encode(), server_address)
client_socket.close()