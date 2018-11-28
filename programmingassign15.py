#Calculate the wind chill from a specified temperature and wind speed (using a GUI)

#Joel Seidel

import tkinter

class WindChillConverterGUI:
	def __init__(self):
		#Main windows initialization
		self.main_window = tkinter.Tk()
		
		#Create widget groups
		self.title_row = tkinter.Frame()
		self.temp_input_row = tkinter.Frame()
		self.windspeed_input_row = tkinter.Frame()
		self.button_row = tkinter.Frame()
		self.output_display_row = tkinter.Frame()
		
		#Initialize title widget
		self.title_label = tkinter.Label(self.title_row, text='Windchill Calculator', fg='red', bg='yellow', font=("Verdana", 16))
		#Pack title label row
		self.title_label.pack(side='left')
		
		#Initialize temperature input widgets
		self.temp_input_label = tkinter.Label(self.temp_input_row, text='Enter the temperature in degrees Fahrenheit: ')
		self.temp_input_textbox = tkinter.Entry(self.temp_input_row, width=10)
		#Pack temperature input row
		self.temp_input_label.pack(side='left')
		self.temp_input_textbox.pack(side='left')
	
		#Initialize wind speed input widgets
		self.windspeed_input_label = tkinter.Label(self.windspeed_input_row, text='Enter the wind speed in mph: ')
		self.windspeed_input_textbox = tkinter.Entry(self.windspeed_input_row, width=10)
		#Pack wind speed input row
		self.windspeed_input_label.pack(side='left')
		self.windspeed_input_textbox.pack(side='left')
		
		#Initialize button row widget
		self.calc_button = tkinter.Button(self.button_row, text='Calculate Windchill', command=self.calculateWindChill)
		#Pack the button row
		self.calc_button.pack(side='left')
		
		#Initialize the calculation row widgets
		self.value = tkinter.StringVar()
		self.calculated_value_label = tkinter.Label(self.output_display_row, textvariable=self.value)
		#Pack the calculation row
		self.calculated_value_label.pack(side='left')
		
		#Pack the frames
		self.title_row.pack()
		self.temp_input_row.pack()
		self.windspeed_input_row.pack()
		self.button_row.pack()
		self.output_display_row.pack()
		
		#Tkinter main loop call
		tkinter.mainloop()
		
	#On click event handler for calculate button click
	def calculateWindChill(self):
		#Get temperature input string and convert to float
		temp = float(self.temp_input_textbox.get())
		#Get wind speed input string and convert to float
		windspeed = float(self.windspeed_input_textbox.get())
		#Calculate the wind chill from provided wind chill and temperature
		windchill = 35.74 + 0.6215 * temp - 35.75 * windspeed**0.16 + 0.4275 * temp * windspeed**0.16
		#Set the calculated wind chill
		self.value.set("The windchill temperature is: {0:.1f}".format(windchill))

#Initialize the gui and start the application
windchillCalc = WindChillConverterGUI()