import socket
import pickle
import time

def menu():
    """
    this function print the menu and take the user choose
    :return: the user choice, the data
    :rtype: int, str
    """
    user_choice = 0
    data = "data"
    flag = 0

    print("1 - album list\n"
          "2 - all the song in album\n"
          "3 - song len\n"
          "4 - song lyrics\n"
          "5 - search album by song\n"
          "6 - search song by name\n"
          "7 - search song by lyrics\n"
          "8 - quit")
    while flag == 0:
        flag = 1
        try:
            user_choice = int(input("Pleas enter your choose: "))
        except Exception as e:
            flag = 0
        if user_choice > 8 or user_choice < 1:
            print("Please enter number between 1 and 8")
            flag = 0


    if user_choice != 1 and user_choice != 8:
        if user_choice == 2:
            data = input("Please enter the album name: ")
        elif user_choice >= 3  and user_choice <= 5:
            data = input("Please enter the song name: ")
        else:
            data = input("Please enter the lyrice you want to search by: ")
    return user_choice, data



def main():
    """
    this function is the main
    :return: NONE
    """
    user_choice = 0
    data = ""

    tuple_of_selections = ("ALBM", "SIAL", "SLEN", "SLYR", "WALS", "SBNA", "SBLY", "QUIT")
    #SIAL is song in album, SLEN is song length, SLYR is song lyrics, WALS is which album song
    #SBNA is search by name, SBLY is search by lyrice

    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 1107
    server_msg = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        server_address = (SERVER_IP, SERVER_PORT)
        sock.connect(server_address)


        while True:
            user_choice, data = menu()
            sock.sendall(("%s/%s" % (tuple_of_selections[user_choice - 1], data)).encode())
            if user_choice == 8:
                break
            server_msg = sock.recv(4096)
            server_msg = pickle.loads(server_msg) #this line make the server msg to list

            for i in server_msg:
                print(i,end=', ')
            print("\n\n")
            time.sleep(1)
            server_msg.clear()

if __name__ == "__main__":
    main()
