#!/usr/bin/env python
# coding: utf-8

# In[4]:


from gammapy.spectrum.models import Absorption
import astropy.units as u
import logging
logging.basicConfig(filename='EBLAbsorption.log',level=logging.WARNING,format='%(asctime)s %(message)s',                     datefmt='%m/%d/%Y %I:%M:%S %p')
class EBLAbsorption:
    def __init__(self,model="franceschini"):
        """ 
        to use this class you need:
                from gammapy.spectrum.models import Absorption
                import astropy.units as u
        parameters:
                "model" of spectral absorption ("franceschini" or "dominguez" or "finke")
                default model is "franceschini"
        
        downloading models to your compurter (Linux):
                after downloading and installing gammapy, open terminal window and execute:
                            gammapy download tutorials --release 0.12
                            cd gammapy-tutorials
                            export GAMMAPY_DATA=$PWD/datasets-0.12
                run anaconda-navigator and change channel to gammapy-0.12
        """
        self.model=model
        self.ebl=Absorption.read_builtin(str(self.model))
    
    def absorption(self,redshift,energy,unit):
        """ This function calculates absorption of EBL according to model stated in class definition
        parameters:
                redshift (int or float)
                energy (int or float or list or touple)
                unit of energy (str: "keV" or "MeV" or "GeV" or "TeV")
        
        output:
                numpy.ndarray if energy parameter = list or touple
                numpy.float64 if energy parameter = int or float
        
        """
        if (type(energy)==int or type(energy)==float)==True:
            if unit=="GeV":
                energy=energy
            elif unit=="keV":
                energy=energy*10**-6
            elif unit=="MeV":
                energy==energy*10**-3
            elif unit=="TeV":
                energy=energy*10**3
            if self.ebl.evaluate((energy*u.GeV),redshift)>energy:
                logging.warning("error: int or float input to EBLAbsorption.absorption() too high or too low. Consequence: output energy higher than input")
        elif (type(energy)==list or type(energy)==tuple)==True:
            for i in energy:
                if unit=="GeV":
                    i=i
                elif unit=="keV":
                    i=i*10**-6
                elif unit=="MeV":
                    i==i*10**-3
                elif unit=="TeV":
                    i=i*10**3
            if self.ebl.evaluate((min(energy)*u.GeV),redshift)>min(energy):
                logging.warning("error: minimum energy in list or tuple input to EBLAbsorption.absorption() is too low. Consequence: output energy higher than input")
            if self.ebl.evaluate((max(energy)*u.GeV),redshift)>max(energy):
                logging.warning("error: maximum energy in list or tuple input to EBLAbsorption.absorption() is too high. Consequence: output energy higher than input")
        return self.ebl.evaluate((energy*u.GeV),redshift)


# In[5]:


# a=EBLAbsorption()
# type(a.absorption(0.5,1,"GeV"))


# In[ ]:




