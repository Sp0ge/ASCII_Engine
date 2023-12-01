from player import Player
import os
import random
import traceback
import threading
import json
import socket

class Server():
    def __init__(self):
        self.connected_users = list()
        #host
        self.server_up = True
        self.bind_status = False
        self.connect_status = False
        self.port = int(25097)
        self.ip = "127.0.0.1"#str(socket.gethostbyname(socket.gethostname()))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def start_hosting(self):
        retry = 0
        while not self.bind_status:
            try:
                self.sock.bind((self.ip, self.port))
                self.bind_status = True
            except socket.error as e:
                if retry < 10:
                    break
                retry += 1
                print(Exception,e)
                
        if self.bind_status:
            print(f"+ Bind on {self.ip}:{self.port} complete.")
            
            self.wait_for_connection()
        else:
            print(f"- Cannot bind on {self.ip}:{self.port} !!")
    
    def wait_for_connection(self):
        self.sock.listen()
        while self.server_up and self.running:
            try:
                conn, addr = self.sock.accept()
                print(f'+ {addr} is connected.')
                self.connected_client_thread(conn, addr)
                #self.connected_users.append(threading.Thread(target=self.connected_client_thread, args=([conn, addr])).start())
            except Exception as e:
                traceback.print_exc()
            
    def connect_to_server(self, ip, port=25097):
        self.ip = str(ip)
        self.port = int(port)
        for i in range(11):
            try:
                self.sock.connect((ip, port))
                self.server_connect_thread()
                #threading.Thread(target=self., args=([]), daemon=True)
                return True
            except Exception as e:
                traceback.print_exc()
                print(f"Trying to connect... {11-i}")
            
        return False
    
    def connected_client_thread(self, conn, addr):
        player = Player(name="Connecting",pos=[20,20])
        self.players.append(player)
        id = len(self.players)
        player.id = id
        info = self.export_server_info()
        conn.send(json.dumps(info).encode("utf-8"))
        print("Info sended")
        while self.server_up and self.running:
            try:
                data = conn.recv(1024*2).decode('utf-8')
                data = list(data.split(","))
                if not data[0]:
                    print(f"+ {addr} disconnected")
                    break
                else:
                    print("\n\n\n", str(data) ,"\n\n\n")
                        
                conn.sendall(str.encode(data[0]))
            except Exception as e:
                traceback.print_exc()
                break
            
    def server_connect_thread(self):
        self.sock.send(str.encode(self.server_))    
        while self.running:
            try:
                data = self.sock.recv(1024*2).decode("utf-8")
                
                if not data:
                    self.sock.close()
                    self.connect_to_server(self.ip, self.port)
                    break
                else:
                    data = self.sock.send(data)
                     
            except Exception as e:
                traceback.print_exc()
                break
               
            
         
# if __name__ == "__main__":
#     Server().start_hosting()
#     Server().connect_to_server("169.254.83.194")