#-*- coding: utf-8 -*-
import math
import random
import tkinter as tk

#背景、タブの表示
root = tk.Tk()
root.geometry('1920x1080')
root.title('Pythonでも席替えのドキドキ感を味わいたい！')
background=tk.PhotoImage(file="bb.png")
bg = tk.Label(root, image=background)
bg.pack(fill="x")
canvas = tk.Canvas(root, width =1920, height = 1080)
tbtxt={}

#リストとか
num_table=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
name=['A','B','C','D','E','F','G','H','I','J', 'K','L','M','N','O','P','Q','R', 'S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF','AG','AH','AI','AJ','AK','AL']

#机の描画
for i in range(len(num_table)):
  a=160*(i%5)
  b=80*math.floor(i/5)
  tb = tk.Canvas(root, width =120, height = 60)
  tbnum = tk.Label(root, text=str(i+1), background='#936E50',font=("",20))
  tb.create_rectangle(0,0,120,60, fill = '#936E50')
  tbtxt[i] = tk.Entry(width=10,font=("",))
  if i<=34:
   tbnum.place (x=372.5+a,y=145+b)
   tb.place(x=370+a, y=130+b)
   tbtxt[i] = tk.Entry(width=10,font=("",))
   tbtxt[i].place(x=405+a, y=140+b,width=80,height=40)
  else:
   tbnum.place (x=532.5+a,y=145+b)
   tb.place(x=530+a, y=130+b)
   tbtxt[i] = tk.Entry(width=10,font=("",))
   tbtxt[i].place(x=565+a, y=140+b,width=80,height=40)

#固定席追加に関するテキストボックス、ラベル
txt1 = tk.Entry(font=("",15))
txt1.place(x=160, y=100,width=90,height=30)
txt2 = tk.Entry(font=("",15))
txt2.place(x=160, y=150,width=90,height=30)
label = tk.Label(root, text="名前",font=("",15))
label.place (x=90,y=100,width=60,height=30)
label = tk.Label(root, text="席番号",font=("",15))
label.place (x=90,y=150,width=60,height=30)

#[追加]をクリックしたときの動作
def click():
  name_click=str(txt1.get())
  num_click=int(txt2.get())
  tbtxt[num_click-1].delete(0,tk.END)
  tbtxt[num_click-1].insert(tk.END,name_click)
  txt1.delete(0, tk.END)
  txt2.delete(0, tk.END)
  name.remove(name_click)
  num_table.remove(num_click)

#[抽選開始]をクリックしたときの動作
def rand():
 random.shuffle(name)
 for i in range(len(num_table)):
  tbtxt[num_table[i]-1].delete(0,tk.END)
  tbtxt[num_table[i]-1].insert(tk.END,name[i])

#ボタン
button = tk.Button(text="追加",font=("",15),command=click)
button.place(x=90, y=200,width=60,height=30)
button = tk.Button(text="抽選開始！",font=("",15),command=rand)
button.place(x=695, y=65,width=120,height=50)

root.mainloop()
