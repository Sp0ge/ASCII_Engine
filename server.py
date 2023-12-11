from player import Player
import time
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
        self.ip = "192.168.0.26"#str(socket.gethostbyname(socket.gethostname()))
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
                self.connected_users.append(threading.Thread(target=self.connected_client_thread, args=([conn, addr])).start())
            except Exception as e:
                traceback.print_exc()
            
    def connect_to_server(self, ip, port=25097):
        self.ip = str(ip)
        self.port = int(port)
        for i in range(11):
            try:
                self.sock.connect((ip, port))
                p = threading.Thread(target=self.server_connect_thread, args=([]), daemon=True)
                p.start()
                p.join()
                self.server_connect_thread
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
        conn.send(json.dumps('{"player_id":"' + str(player.id) + '"}').encode("utf-8"))
        conn.send(json.dumps(info).encode("utf-8"))
        print("Info sended")
        while self.server_up and self.running:
            data = conn.recv(1024*1024).decode('utf-8')
            try:
                if not data:
                    print(f"+ {addr} disconnected")
                    self.players.remove(player)
                    break
                else:
                    try:
                        data = json.loads(json.loads(data))
                    except Exception: 
                        data = json.loads(data)
                    if "player_id" in data:
                        if int(data['player_id']) == player.id:
                            print(f"Client id[{id}] ACCEPTED")
                        else:
                            self.import_server_info(data)
                    #print(info)
                    data = self.export_server_info()
                conn.sendall(str.encode(json.dumps(data)))
                
                    
            except Exception:                
                traceback.print_exc()
                self.players.remove(player)
                break
            
            
    def server_connect_thread(self):
        while self.running:
            try:
                data = self.sock.recv(1024*1024).decode("utf-8")
                print(data)
                if not data:
                    self.sock.close()
                    print("Connection Closed")
                    break
                else:
                    try:
                        data = json.loads(json.loads(data))
                    except: 
                        data = json.loads(data)
                    if "player_id" in data:
                        self.id = data['player_id']
                        print("send player accept")
                        self.sock.send(json.dumps('{"player_id":"' + str(self.id) + '"}').encode("utf-8"))
                    else:
                        self.import_server_info(data)
                        self.sock.send(str.encode(json.dumps(self.export_server_info())))
                        
            except Exception as e:
                print("error")
                traceback.print_exc()
                break
               
            
         
# if __name__ == "__main__":
#     Server().start_hosting()
#     Server().connect_to_server("169.254.83.194")