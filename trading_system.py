import threading
import time
import abc
import yfinance as yf

class TradingSystem(abc.ABC):
    @abc.abstractclassmethod
    def abstractloop(self):
        pass
    
    def mainloop(self):
        while(True):
            self.abstractloop()
            time.sleep(self.timeframe)
            
    def __init__(self, ticker, timeframe):
        self.ticker = ticker
        self.timeframe = timeframe
        t = threading.Thread(target = self.mainloop)
        t.start()

class executer(TradingSystem):
    def abstractloop(self):
        print(self.googl.option_chain())
    
    def __init__(self, timeframe):
        self.ticker = 'GOOGL'
        self.googl = yf.Ticker(self.ticker)
        super().__init__('GOOGL', timeframe)
executer(10)