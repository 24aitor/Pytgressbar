import pytgressbar
import time

if __name__ == '__main__':
        bar = pytgressbar.ProgressBar(total = 75, length = 50, fill="#", partsText = "Querys done!", percentageDecimals = 4)
        for i in range(75):
                bar.update(i)
                time.sleep(.1)
        bar.update(75)

        bar2 = pytgressbar.ProgressBar(total = 75, length = 50, partsText = "Querys done!", percentageDecimals = 2)
        for i in range(75):
                bar2.update(i)
                time.sleep(.1)
        bar2.update(75)
