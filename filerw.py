#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 09:57:15 2016

@author: yang
"""
#生成Blowing in the wind.txt文件
f = open(r'Blowing in the wind.txt','w')

f.writelines('How many roads must a man walk down\n')

f.writelines('Before they call him a man\n')

f.writelines('How many seas must a white dove sail\n')

f.writelines('Before she sleeps in the sand\n')

f.writelines('How many times must the cannon balls fly\n')

f.writelines('Before they\'re forever banned\n')

f.writelines('The answer my friend is blowing in the wind\n')

f.writelines('The answer is blowing in the wind\n')

f.close()

#读取该文件,添加专辑头,添加每首歌的作者,添加专辑尾
g = open(r'Blowing in the wind.txt','r')

songs = g.readlines()

h = open(r'Blowing in the wind1.txt','w')

h.writelines('Blowin\' in the wind\r\n')

#for line in songs:
#    h.write(line)
#    h.write(' Bob Dylan')

for i in range(0, len(songs)):
    #要用strip函数来清除换行符
    songs[i] = songs[i].strip() + ' - Bob Dylan\n'
    print(songs[i])

#    song = song + ' Bob Dylan'

h.writelines(songs)

h.writelines("1962 by Warner Bros. Inc.")

#print(h)
g.close()
h.close()

