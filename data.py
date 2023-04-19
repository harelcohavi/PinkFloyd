def sort_file():
    """
    this fuction make the txt file more comfortable to use
    :return: a dict that every key is album  and every value is list of dict of the song
    :type: dict
    """
    FILE_PATH = "Pink_Floyd_DB.txt"
    opened_file = open(FILE_PATH, 'r')
    file = opened_file.read()

    list_by_album = file.split('#')
    list_of_dict = []
    back_dict = {}
    value_list = []
    number_of_run = 0

    for i in list_by_album:
        if number_of_run == 0:
            number_of_run = 1
            continue
        value = i.split('*')[1:]

        for j in value:
            value_list.append(j.split('::'))
        list_of_dict.append({i.split('*')[0]:([{"name" : value_list[k][0], "songer" : value_list[k][1], "time" : value_list[k][2], "the_song" : value_list[k][3]} for k in range(len(value_list))]) })
        value = []
        value_list = []
    for i in list_of_dict:
        for key, value in i.items():
            #print(key)
            back_dict[tuple(key.split("::"))] = value
    opened_file.close()
    return back_dict

def albm(dict_album):
    """
    this function take all the album name
    :param list: the list of the album
    :type list: list
    :return: list with all the album name
    :rtype: list
    """
    back_list = []
    for i in dict_album.keys():
        back_list.append(i[0])
    return back_list

def sial(dict_of_album, album_name):
    """
    this function find all the song in the selected album
    :param dict_of_album: the dict with the album
    :type dict_of_album: dict
    :param album_name: the selected album name
    :type album_name: str
    :return: a list with all the song name
    :rtype: list
    """
    back_list = []
    for key, value in dict_of_album.items():
        if album_name in key[0]:
            for i in value:
                back_list.append(i['name'])
    return back_list

def slen(dict_of_album, song_name):
    """
    this function find the song len
    :param dict_of_album: dict with all the album
    :type dict_of_album: dict
    :param song_name: the song name
    :type song_name: str
    :return: the song len
    :rtype: str
    """
    back_msg = ""
    for i in list(dict_of_album.values()):
        for j in i:
            for k in j:
                if song_name in j['name']:
                    back_msg = j['time']
    return back_msg

def slyr(dict_of_album, song_name):
    """
    this function find the song lyrics
    :param dict_of_album: dict with all the album
    :type dict_of_album: dict
    :param song_name: the song name
    :type song_name: str
    :return: the song lytics
    :rtype: str
    """
    song = ""
    for i in list(dict_of_album.values()):
        for j in i:
            for k in j:
                if song_name == j['name']:
                    song = j['the_song']
    return song

def wals(dict_of_album, song_name):
    """
    this function find name of album by name of song in the album
    :param dict_of_album: the dict with the album name and song
    :type dict_of_album: dict
    :param song_name: the song name
    :type song_name: str
    :return: the album name
    :rtype: str
    """
    album_name = ""
    for key, value in dict_of_album.items():
        for j in value:
            if song_name == j['name']:
                album_name = key[0]
    return album_name

def sbna(dict_of_album, word):
    """
    this function search song by part of his name
    :param dict_of_album: the album and song dict
    :type dict_of_album: dict
    :param word: the word that is part of the song name
    :type word: str
    :return: list with the songs name
    :rtype: list
    """
    song_name = []
    temp_list = []
    word = word.lower()
    for i in list(dict_of_album.values()):
        for j in i:
            for k in j:
                if word in (j['name']).lower():
                    temp_list.append(j['name'])
    for i in temp_list:
        if i not in song_name:
            song_name.append(i)
    return song_name

def sbly(dict_of_album, lyrice):
    """
    this function search song by his lyrice
    :param dict_of_album: the album and song dict
    :type dict_of_album: dict
    :param lyrice: the word that is part of the song lyrice
    :type lyrice: str
    :return: list with the songs name
    :rtype: list
    """
    song_name = []
    temp_list = []
    lyrice = lyrice.lower()
    for i in list(dict_of_album.values()):
        for j in i:
            for k in j:
                if lyrice in (j['the_song']).lower():
                    temp_list.append(j['name'])
    for i in temp_list:
        if i not in song_name:
            song_name.append(i)
    return song_name


if __name__ == "__main__":
    dict_of_album = sort_file()
    print(dict_of_album)
