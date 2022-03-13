#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import socket


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定本地信息
    local_adr = ("", 8888)
    udp_socket.bind(local_adr)
    # 3.接受数据
    receive_data = udp_socket.recvfrom(1024)
    receive_msg = receive_data[0]
    receive_adr = receive_data[1]
    # 4.处理数据，接受 Windows 发送的信息可能编码要换成 gbk
    print("%s: %s" % (str(receive_adr), receive_msg.decode("utf-8")))
    # 5.关闭连接
    udp_socket.close()


if __name__ == '__main__':
    main()




