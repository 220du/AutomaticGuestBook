import sqlite3
import time
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def check_pin_num(num):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM User WHERE Pin_Num =="{num}"')
    result = cursor.fetchone()
    return str(result)


def check_seq_user():
    db = sqlite3.connect(f"data.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT COUNT(*) FROM User')
    count = cursor.fetchone()[0]
    return int(count)


def check_seq_list():
    db = sqlite3.connect(f"data.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT COUNT(*) FROM List')
    count = cursor.fetchone()[0]
    return int(count)


def get_list(sort, desc):
    db = sqlite3.connect(f"data.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT COUNT(*) FROM List')
    count_lists = cursor.fetchone()[0]
    get_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM List Order By "{sort}"')
    else:
        cursor.execute(
            f'SELECT * FROM List Order By "{sort}" DESC')

    for i in range(count_lists):
        li = cursor.fetchone()[1:]
        get_list.append(li)
    return get_list


def input_Name(num):
    newWin = Tk()
    newWin.withdraw()
    name = askstring('회원가입', '이름을 입력해주세요', parent=newWin)
    if name == None:
        exit_message = tkinter.messagebox.showinfo(
            "취소", "회원가입이 취소되었습니다.")
        return 0
    content = askstring(
        '회원가입', f'{name}님이 소속되어 있는 단체명을 입력해주세요', parent=newWin)
    newWin.destroy()
    if content == None:
        exit_message = tkinter.messagebox.showinfo(
            "취소", "회원가입이 취소되었습니다.")
        return 0

    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT COUNT(*) FROM User')
    count = cursor.fetchone()[0]
    insert_query = \
        f"INSERT INTO User VALUES('{count+1}','{num}','{name}','{content}')"
    cursor.execute(insert_query)
    db.commit()
    message = tkinter.messagebox.showinfo(
        "회원가입 완료", "회원가입을 완료했습니다.")


def save(num):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT COUNT(*) FROM List')
    count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT Name, Content FROM User WHERE Pin_Num =="{num}"')
    data = cursor.fetchone()
    name = data[0]
    content = data[1]
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일" % (now.tm_year, now.tm_mon, now.tm_mday))
    Time = ("%02d시 %02d분 %02d초" % (now.tm_hour, now.tm_min, now.tm_sec))
    insert_query = \
        f"INSERT INTO List VALUES('{count+1}','{Date}','{Time}','{name}','{content}')"
    cursor.execute(insert_query)
    db.commit()
