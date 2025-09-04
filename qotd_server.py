#!/usr/bin/env python3
import socket
import subprocess
import threading

HOST = "0.0.0.0"
TCP_PORT = 17
UDP_PORT = 17
BUFFER_SIZE = 1024

def get_fortune():
    """fortune-modから1つ取得"""
    try:
        return subprocess.check_output(["fortune", "-s"], text=True)
    except Exception as e:
        return f"Error fetching fortune: {e}"

def handle_tcp_client(conn, addr):
    """TCP接続処理"""
    try:
        fortune = get_fortune()
        conn.sendall(fortune.encode("utf-8"))
    finally:
        conn.close()

def tcp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, TCP_PORT))
        s.listen()
        print(f"TCP server listening on port {TCP_PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_tcp_client, args=(conn, addr), daemon=True).start()

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, UDP_PORT))
        print(f"UDP server listening on port {UDP_PORT}")
        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)
            fortune = get_fortune()
            s.sendto(fortune.encode("utf-8"), addr)

if __name__ == "__main__":
    threading.Thread(target=udp_server, daemon=True).start()
    tcp_server()

