import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

class Plot():           
    def plotGraph(self,arr,label):
        res = {"time":[],"value":[]}
        for i in arr:
            res["time"].append(datetime.strptime(i[0], "%d/%m/%Y %H:%M:%S"))
            res["value"].append(i[1])
        dates = mdates.date2num(res["time"])
        plt.plot(res["time"], res["value"],label=label)
        plt.legend
        return (plt.gcf().autofmt_xdate())
                
    def showGraph(self):
        plt.legend()
        plt.show()
            
