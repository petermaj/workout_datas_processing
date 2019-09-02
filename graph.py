from tkinter import *  
from tkinter import filedialog  
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

def window(distances, speeds, heartrates):
    window=Tk()  
    window.title("Workout Datas")      
    button_speed=Button(window, text="Show speed datas", command=lambda:show_speed(distances, speeds))
    button_heartrate=Button(window, text="Show heartrate datas", command=lambda:show_heartrate(distances, heartrates))
    button_speed.grid(row=0, column=0)
    button_heartrate.grid(row=1, column=0)
    canvas=Canvas(window, width=360, height=360, bg='white')
    canvas.grid(row=0, rowspan=4, column=1)
    window.mainloop()

def selectfile():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "../workoutdataprocessing/workoutdata",title = "Select file",filetypes = (("xlsx files","*.xlsx"),("all files","*.*")))
    root.destroy()
    return (root.filename)

def main():
    selectfile()
    datas=data.processing_workout_datas()
    distances=[]
    speeds=[]
    heartrates=[]
    for i in range(len(datas)):
        distances.append(datas[i].distance/1000)
        speeds.append(datas[i].speed*(3.6))
        heartrates.append(datas[i].heartrate)
    window(distances, speeds, heartrates)

main()

