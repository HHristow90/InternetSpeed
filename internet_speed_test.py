from speedtest_cli import Speedtest
import tkinter as tk

st = Speedtest()


ws = tk.Tk()
ws.title('Internet Speed')
ws.geometry('477x390')
ws.config(bg='black')

img = tk.PhotoImage(file="hristow_speedtest_logo.png")
label = tk.Label(
    ws,
    image=img
)
label.place(x=0, y=0)

tk.Label(ws,
		text=f"Your Connection's Download speed is: {st.download():.2f}",
		fg="white",
		bg="dark grey",
		font="Helvetica 12 bold italic").place(x=50, y=150)

tk.Label(ws,
		text=f"Your Connection's Upload speed is: {st.upload():.2f}",
		fg="white",
		bg="dark grey",
		font="Helvetica 12 bold italic").place(x=50, y=180)


# tk.Button(
#     ws,
#     text='THANK YOU',
#     font=('Arial Bold', 18)
# ).place(x=190, y=250)

ws.mainloop()
