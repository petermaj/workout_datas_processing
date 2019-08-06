from tkinter import *    

window=Tk()  
window.title("Workout Datas")      
button_speed=Button(window, text="Show speed datas") #, command=show_speed)
button_heartrate=Button(window, text="Show heartrate datas") #, command=show_heartrate)
button_speed.grid(row=0, column=0)
button_heartrate.grid(row=1, column=0)
canvas=Canvas(window, width=360, height=360, bg='white')
canvas.grid(row=0, rowspan=4, column=1)
window.mainloop()