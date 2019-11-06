import socket

# 设置服务器默认端口号
PORT = 8000
# 创建一个套接字socket对象，用于进行通讯
# socket.AF_INET 指明使用INET地址集，进行网间通讯
# socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("10.196.247.110", PORT)
# 为服务器绑定一个固定的地址，ip和端口
server_socket.bind(address)
# 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
# recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
# recvfrom返回值说明
# receive_data表示接受到的传来的数据,是bytes类型, receive_data.decode()解码，将bytes类型转换为字符串类型
# client_address 表示传来数据的客户端的身份信息，客户端的ip和端口，元组
receive_data, client = server_socket.recvfrom(1024)

print("来自客户端%s,发送的%s" % (client, receive_data.decode()))
# 不再接收数据的时候，将套接字socket关闭
server_socket.close()