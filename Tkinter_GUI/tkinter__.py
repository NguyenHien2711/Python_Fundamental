import tkinter as tk
root = tk.Tk()
root.geometry('400x500')
datas = []

def update_book():
    select.delete(0,'END')
    for n in datas:
        select.insert('END', n)
        
def add():
    global datas
    datas.append([name.get(), number.get(), txt_address.get(1.9, 'end-1c')])
    update_book()
    
def view():
    name.set(datas[int(select.curselection()[0])][0])
    number.set(datas[int(select.curselection()[0])][1])
    txt_address.delete(1.0, 'end')
    txt_address.insert(1.0, datas[int(select.curselection()[0])][2])

def delete():
    del datas[int(select.curselection()[0])]
    update_book()

def reset():
    name.set('')
    number.set('')
    txt_address.delete(1.0,"end")
name = tk.StringVar()
number = tk.StringVar()

frame = tk.Frame()
frame.pack(pady=10)

frame1 = tk.Frame()
frame1.pack(pady=10)

frame2 = tk.Frame()
frame2.pack(pady=10)

lbl_name = tk.Label(frame, text = 'Name', font='arial 12 bold').pack(side='LEFT')
ent_name = tk.Entry(frame, textvariable = name, width=50).pack()

lbl_phonenumber = tk.Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side='LEFT')
ent_phonenumber = tk.Entry(frame1, textvariable = number, width=50).pack()

lbl_address = tk.Label(frame2, text = 'Address', font='arial 12 bold').pack(side='LEFT')
txt_address = tk.Text(frame2, width=50, height =10).pack()

btn_add = tk.Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270)
btn_view = tk.Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310)
btn_del = tk.Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350)
btn_res = tk.Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390)

scroll_bar = tk.Scrollbar(root, orient = 'vertical')
select = tk.Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command = select.yview)
scroll_bar.pack(side='right', fill='y')
select.place(x=200,y=260)

root.mainloop()

