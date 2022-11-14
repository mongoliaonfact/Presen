# @author: bbaasan
# date: 10/18/2022
# bbaasan@gmu.edu

import numpy
from pandas import DataFrame


def reprisk_firms():
    params = {
            'ticker': ['EQNR','TEVA', 'LKNCY', 'PCG','TSLA',
                   'NHYDY', 'AMZN','INDY.JK', '600521.SS','VWAGY','BOO.L' ],
            'company_name': ['Equinor ASA','Teva Pharma',
                         'Luckin Coffee Inc','PG&E Corporation',
                         'Tesla Inc','Norsk Hydro ASA',
                         'Amazon Inc','Indika Energy Tbk; PT',
                         'Hejiang Huahai Pharma Co LLC','Volkswagon AG',
                         'Boohoo Grup PLC'],
            'start_dt': numpy.repeat('2008-01-01', 11),
            'end_dt': numpy.repeat('2022-01-01', 11)
            }

    return DataFrame(params)

#print(reprisk_firms())
