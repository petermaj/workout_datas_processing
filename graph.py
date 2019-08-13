from tkinter import *    
import processing_workout_datas as data
import matplotlib.pyplot as plt


def show_speed(_distances, _speeds):     
    plt.xlabel('Distance (km)')
    plt.ylabel('Speed (km/h)')
    plt.title("Speed Line Graph")
    plt.plot(_distances, _speeds)
    plt.show()

def show_heartrate(_distances, _heartrate):
    plt.xlabel('Distance (km)')
    plt.ylabel('Heartrate')
    plt.title("Heartrate Line Graph")
    plt.plot(_distances, _heartrate)
    plt.show()

window=Tk()  
window.title("Workout Datas")      
button_speed=Button(window, text="Show speed datas", command=lambda:show_speed(distances, speeds))
button_heartrate=Button(window, text="Show heartrate datas", command=lambda:show_heartrate(distances, heartrates))
button_speed.grid(row=0, column=0)
button_heartrate.grid(row=1, column=0)
canvas=Canvas(window, width=360, height=360, bg='white')
canvas.grid(row=0, rowspan=4, column=1)
window.mainloop()


