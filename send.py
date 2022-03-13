#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import socket


def main():
    # socket.AF_INET: 用于 Internet 进程间通信
    # socket.AF_UNIX: 用于同一台机器进程间通信
    # UDP: socket.SOCK_DGRAM
    # TCP: socket.SOCK_STREAM
    # 1.创建tcp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    local_adr = ("", 9999)
    udp_socket.bind(local_adr)

    while True:
        # 3.获取发送的数据
        try:
            send_data = input("请输入要发送的数据: ")
        except KeyboardInterrupt as e:
            print(e)
            break
        except Exception as e:
            print(e)
            break
        if send_data == "quit":
            break
        # 4.发送数据，不绑定端口，会随机绑定一个端口
        result = udp_socket.sendto(send_data.encode("utf-8"), ("127.0.0.1", 8888))
        print(result)

    # 5.关闭连接
    udp_socket.close()


if __name__ == '__main__':
    main()







