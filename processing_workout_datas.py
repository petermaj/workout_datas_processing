import getWorkoutData

class workoutData:
    def __init__(self, distance, heartrate, speed):
        self.distance=distance
        self.heartrate=heartrate
        self.speed=speed

        
def processing_workout_datas():
    workbook=getWorkoutData.openWorkbook("workoutdata/Move_2019_07_29_17_38_24_Cycling.xlsx")
    worksheetnames=getWorkoutData.getworksheetnames(workbook)
    row=getWorkoutData.getDatas(workbook,2)
    avgspeed=row[8]
    avgheartrate=row[5]
    datas=[]
    data=workoutData(row[53], row[54], row[55])
    datas.append(data)
    index=3
    while(index!=getWorkoutData.getRowNumber(workbook, worksheetnames[0])):
        row=getWorkoutData.getDatas(workbook,index)
        if(row[53]!=''):
            data=workoutData(row[53], row[54], row[55])    
            datas.append(data)
        index+=1
    del workbook
    return datas

