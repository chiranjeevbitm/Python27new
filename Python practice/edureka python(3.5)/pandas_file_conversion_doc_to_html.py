# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 19:07:39 2017

@author: Chiranjeev
"""

import pandas as pd 


country = pd.read_csv(r"C:\Users\Chiranjeev\Downloads\UN-data.csv")
country.to_html('succssefully_converted_csv_to_html.html')
