"""
Задан путь к директории с музыкальными файлами (в названии 
которых нет номеров, а только названия песен) и текстовый файл, 
хранящий полный список песен с номерами и названиями в виде строк 
формата «01. Freefall [6:12]». Напишите скрипт, который корректирует 
имена файлов в директории на основе текста списка песен.
"""

import os, re

curd_dir  = os.getcwd() 
music_dir = 'music'
abs_path = True
#abs_path = False

if abs_path: music_dir = os.path.join(curd_dir, music_dir)
else:        music_dir = '.\\' + music_dir
print('music_dir:', music_dir)

music_files = {}
for dirpath, dirnames, filenames in os.walk(music_dir):
    for filename in filenames: 
        real_name, expansion = filename.rsplit('.', 1)
        music_files[real_name] = [dirpath, expansion]
print('\nmusic_files:')
for song_name, (dirpath, expansion) in music_files.items(): 
    print('%20s.%s in dir "%s"' % (song_name, expansion, dirpath))

songs_info = {}
with open('songs.txt', 'r', encoding = 'utf-8') as songs_file:
    for line in songs_file.readlines():
        line = line.replace('\n', '')
        match = re.match(r'[\d]+. ([\w ]+) \[[\d]+:[\d]+\]', line)
        if match:     
            song_name = match.groups()[0]
            if song_name in music_files:
                dirpath, expansion = music_files[song_name]   
                os.rename(os.path.join(dirpath, song_name + '.' + expansion), os.path.join(dirpath, line.replace(':','-') + '.' + expansion))

# проверка
print('\nmusic_files (after rename):')
for dirpath, dirnames, filenames in os.walk(music_dir):
    for filename in filenames: 
        print (os.path.join(dirpath, filename))



