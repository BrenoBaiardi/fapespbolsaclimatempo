import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

class Plot():           
    def plotGraph(self,arr,label): #recebe uma lista a ser plotada e uma label de identificação
        res = {"time":[],"value":[]}
        for i in arr:
            res["time"].append(datetime.strptime(i[0], "%d/%m/%Y %H:%M:%S"))
            res["value"].append(i[1])
        # os comandos seguintes garantes que os
        # valores contidos no eixo x possam existir
        # e ser exibidos de maneira legível
        #dates = mdates.date2num(res["time"])
        plt.plot(res["time"], res["value"],label=label)
        return (plt.gcf().autofmt_xdate())
                
    def showGraph(self):
        plt.legend()
        plt.show()
            
