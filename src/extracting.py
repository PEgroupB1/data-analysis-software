import xml.etree.ElementTree as ET
import numpy as np

# Extracting the data from the xml file

class Extract:

    def __init__(self, path:str):
        """
        initilize the etraction of the data inside the xml file

        Args:
            path (str): path of the xml file 
        """
        self.path = path
        self.tree = ET.parse(self.path) 
        self.root = self.tree.getroot()

    def get_IV(self):
        """
        get the IV data and return an array with the data ready to plot the IV graph

        Returns:
            np.array: return an array with the X being the voltage and the Y the current.
        """
        
        for ivMesurement in self.root.iter('IVMeasurement'):
            self.voltage = ivMesurement.find('Voltage').text
            self.current = ivMesurement.find('Current').text

        self.currentList = self.current.split(',')
        self.voltageList = self.voltage.split(',')

        self.currentList = list(map(float, self.currentList))
        self.voltageList = list(map(float, self.voltageList))

        self.IV = np.array([self.voltageList, self.currentList])

        return self.IV

    def get_Spectrum(self):
        """
        get the Spectrum data and return 2 list

        Returns:
            list: return 2 list : 
                    - the first one is the list containing all the wavelength
                    - the second one is the list containing all the decibel
        """

        wavelenghtList = []
        dbList = []
        for portCombo in root.iter('PortCombo'):
            for wavelenght in portCombo.findall('WavelengthSweep'):
                wavelenghtList.append(wavelenght.find('L').text)
                dbList.append(wavelenght.find('IL').text)

        floatWaveLengthList = []
        for elem in wavelenghtList:
            wavelength_step = elem.split(',')
            floatWaveLengthList.append(list(map(float,wavelength_step)))

        floatdBList = []
        for elem in dbList:
            dB_step = elem.split(',')
            floatdBList.append(list(map(float,dB_step)))

        return floatWaveLengthList, floatdBList


