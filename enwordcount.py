import tkinter as tk
import tkinter.ttk as ttk
import threading
import pyclip

def _count(word):
    lines=word.split('\n')
    while '' in lines:
        lines.remove('')
    words=[]
    for line in lines:
        lineword=line.split(' ')
        for lw in lineword:
            words.append(lw)
    while '' in words:
        words.remove('')
    sentencecount=0
    charindex=0
    notriperiod=word.replace('...','') #Ignore ellipsis
    for char in notriperiod:
        if char=='.':
            sentencecount+=1
        charindex+=1
    #words.remove(' ')
    #words.remove('\n')
    return len(words),sentencecount,len(lines)

def count():
    wordcount,sentencecount,paracount=_count(txtinput.get(1.0,tk.END))
    countlabel['text']=str(wordcount)+' Words'+' | '+str(len(txtinput.get(1.0,tk.END))-1)+' Chars'+\
                       ' | '+str(sentencecount)+' Sentences (Periods)'+' | '+str(paracount)+' Paras (Lines)'

def updatecount():
    end=False
    while win.winfo_exists() and not end:
        try:
            count()
        except:
            print('EXIT')
            end=True
            break
    print('EXIT')
    exit()

def paste():
    txtinput.insert(tk.INSERT,pyclip.paste(encoding='utf-8'))

win=tk.Tk()
win.title('English Word Count')
win.minsize(640,360)
win.geometry('640x360')

txtinput=tk.Text(win,bd=0)

tk.Label(win,text='2023 By rgzz666').pack(side=tk.BOTTOM,fill=tk.X)

countrow=tk.Frame(win)

ttk.Button(countrow,text='REFRESH',command=count).pack(side=tk.RIGHT)
ttk.Button(countrow,text='↑ PASTE',command=paste).pack(side=tk.RIGHT)
ttk.Button(countrow,text='X CLEAR',command=lambda:txtinput.delete(1.0,tk.END)).pack(side=tk.RIGHT)

countlabel=tk.Label(countrow,text='Please press REFRESH first',anchor='w')
countlabel.pack(fill=tk.X)

countrow.pack(side=tk.BOTTOM,fill=tk.X)

txtinput.pack(fill=tk.BOTH,expand=True)

update_t=threading.Thread(target=updatecount)
update_t.start()

win.mainloop()
