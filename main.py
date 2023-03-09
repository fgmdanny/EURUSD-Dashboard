import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

root = tk.Tk()
root.title("EUR/USD Dashboard")
root.geometry("800x600")

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Chart')
tab_control.add(tab2, text='Table')
tab_control.pack(expand=1, fill='both')

fig = plt.Figure(figsize=(6, 5), dpi=100)
ax = fig.add_subplot(111)
ax.set_title('EUR/USD')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.plot([1, 2, 3, 4, 5], [1.5, 2.0, 1.8, 1.6, 1.9])

canvas = FigureCanvasTkAgg(fig, master=tab1)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, tab1)
toolbar.update()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

table = ttk.Treeview(tab2)
table['columns'] = ('Date', 'Open', 'High', 'Low', 'Close', 'Volume')
table.column('#0', width=0, stretch=tk.NO)
table.column('Date', anchor=tk.CENTER, width=100)
table.column('Open', anchor=tk.CENTER, width=100)
table.column('High', anchor=tk.CENTER, width=100)
table.column('Low', anchor=tk.CENTER, width=100)
table.column('Close', anchor=tk.CENTER, width=100)
table.column('Volume', anchor=tk.CENTER, width=100)

table.heading('Date', text='Date')
table.heading('Open', text='Open')
table.heading('High', text='High')
table.heading('Low', text='Low')
table.heading('Close', text='Close')
table.heading('Volume', text='Volume')

for i in range(10):
    table.insert('', 'end', text=str(i),
                 values=('2022-03-0'+str(i+1), 1.2345, 1.2456, 1.2298, 1.2403, 1000+i))

table.pack(expand=1, fill='both')

root.mainloop()
