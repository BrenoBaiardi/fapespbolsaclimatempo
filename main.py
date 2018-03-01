from Scraper import Scraper
from Plot import Plot

scraper = Scraper()
arr_guap,arr_colider = scraper.getData()
plot = Plot()
plot.plotGraph(arr_guap,"GUAPORÉ")
plot.plotGraph(arr_colider,"COLIDER")
plot.showGraph()

