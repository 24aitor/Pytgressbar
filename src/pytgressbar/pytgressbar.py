# -*- coding: utf-8 -*-

import sys

class ProgressBar(object):
	"""docstring for ProgressBar"""
	def __init__(self, text = "Progress: ", fill = "█", space = " ", total = 100, length = 60, percentage = True, percentageDecimals = 0, parts = True, indicator="|", partsText = ""):
		self.fill = fill
		self.space = space
		self.text = text
		self.total = total
		self.length = length
		self.__last = 0
		self.parts = parts
		self.partsText = partsText
		self.indicator = indicator
		self.percentage = percentage
		self.percentageDecimals = percentageDecimals

	def update (self, value):
		completed = False
		update = True

		if (value >= self.total):
			bar = self.fill*self.length
			completed = True
		elif (value > self.__last):
			bar = self.fill * int(round((value*self.length)/self.total)) + self.space * int(self.length-round((value*self.length)/self.total))
			self.__last = value
		else:
			update = False

		if (self.percentage):
			if (self.percentageDecimals > 0):
				percentage = ' ' + str(format(round(float(value*100)/self.total, self.percentageDecimals), '.'+str(self.percentageDecimals)+'f')) + '%'
			else:
				percentage = ' ' + str(int(round((value*100)/self.total))) + '%'

		else:
			percentage = ""

		parts = (" ({}/{}){}").format(value, self.total, " " + self.partsText if len(self.partsText)>0 else "") if self.parts else ""
		lastChar = "\n" if completed == True else ""
		if update:
			sys.stdout.write("\r{}{}{}{}{}{}{}".format(self.text, self.indicator, bar, self.indicator, percentage, parts, lastChar))

		sys.stdout.flush()
