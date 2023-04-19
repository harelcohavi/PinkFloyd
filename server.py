import socket
import pickle
import data

def main():
    """
    this function is the main
    :return: NONE
    """
    LISTEN_PORT = 1107
    client_msg = ""
    temp_list = []
    user_choice = 0
    the_data = ""
    back_list = []
    dict_of_album = data.sort_file()

    with socket.socket() as listening_sock:
        listening_sock.bind(('',LISTEN_PORT))
        listening_sock.listen(1)
        client_soc, client_address = listening_sock.accept()
        with client_soc:
            while "QUIT" not in client_msg:
                client_msg = client_soc.recv(1024)
                client_msg = client_msg.decode()
                temp_list = client_msg.split("/")
                user_choice = temp_list[0]
                the_data = temp_list[1]
                if user_choice == "ALBM":
                    back_list = data.albm(dict_of_album)
                elif user_choice == "SIAL":
                    back_list = data.sial(dict_of_album,the_data)
                elif user_choice == "SLEN":
                    back_list.append(data.slen(dict_of_album,the_data))
                elif user_choice == "SLYR":
                    back_list.append(data.slyr(dict_of_album,the_data))
                elif user_choice == "WALS":
                    back_list.append(data.wals(dict_of_album,the_data))
                elif user_choice == "SBNA":
                    back_list = data.sbna(dict_of_album, the_data)
                elif user_choice == "SBLY":
                    back_list = data.sbly(dict_of_album, the_data)
                elif user_choice == "QUIT":
                    break

                client_soc.send(pickle.dumps(back_list)) #this line send a list to the client
                back_list.clear()



if __name__ == "__main__":
    main()
