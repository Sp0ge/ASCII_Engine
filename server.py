from player import Player
import os
import random
import traceback
import threading
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
                print(e)
                
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
                print(e)
            
    def connect_to_server(self, ip, port=25097):
        self.ip = str(ip)
        self.port = int(port)
        for i in range(11):
            try:
                self.sock.connect((ip, port))
                print("pl")
                if self.players[0].id != 0:
                    id = self.sock.recv(1024*2).decode("utf-8")
                    Player.add_player(self.players ,str(self.host_player_name), int(id))
                self.server_connect_thread()
                #threading.Thread(target=self., args=([]), daemon=True)
                return True
            except Exception as e:
                print(e)
                print(f"Trying to connect... {11-i}")
            
        return False
    
    def connected_client_thread(self, conn, addr):
        player = Player(name="Connecting",pos=[20,20])
        self.players.append(player)
        id = len(self.players)
        player.id = id
        conn.send(str.encode(str(id)))
        while self.server_up and self.running:
            try:
                data = conn.recv(1024*2).decode('utf-8').split(",")

                if not data:
                    print(f"+ {addr} disconnected")
                    break
                else:
                    if data[0] == "conn_info":
                        socket.socket.sendto(conn,str.encode(str(id)),addr)
                        player.set_pos((int(data[0]),int(data[1])))
                        player.health = int(data[2])
                        player.bullets = int(data[3])
                        player.set_name(str(data[4]))
                    else:
                        self.import_server_info(str(data))
                        
                conn.sendall(str.encode(self.server_info()))
            except Exception as e:
                print(traceback.format_exc())
                break
            
    def server_connect_thread(self):
        self.sock.send(str.encode(self.players[0].get_player_info_full()))    
        while self.running:
            try:
                data = str(self.sock.recv(1024*2).decode("utf-8"))
                print(data)
                if not data:
                    self.sock.close()
                    self.connect_to_server(self.ip, self.port)
                    break
                else:
                    self.sock.send(str.encode(self.server_info()))
                    
            except Exception as e:
                print(traceback.format_exc())
                break
               
            
         
# if __name__ == "__main__":
#     Server().start_hosting()
#     Server().connect_to_server("169.254.83.194")