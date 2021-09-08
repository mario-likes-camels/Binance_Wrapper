#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:22:58 2021

@author: patrick
"""
#https://python-packaging.readthedocs.io/en/latest/minimal.html


from binance.client import Client
from binance_data.client import DataClient
from datetime import datetime
import pandas as pd
import warnings
from binance_data.client import DataClient

from binance.client import Client
from datetime import datetime
import pandas as pd
import time
import numpy as np
import warnings
warnings.filterwarnings('ignore')

import os
import sys
import shutil



''' This function creates a list of all currency paris
Input = Base_Curreny pair i.e BTC (We also require "client" to ensure we have binance login)
Output = List of Currency pairs with Base Currency '''
def All_Pairs(base_currency, client):
    exchange_info=client.get_exchange_info() 
    symbols=exchange_info.get('symbols')
    pairs=[symbols[i]['symbol'] for i in range(0,len(symbols))]
    #Get only BASE_cURRENCY Pairs
    return [x for x in pairs if x.endswith(base_currency) ]







''' Downloads and Saves Historical Data
Inputs = List of pairs ,
            time period -  1m,3m,5m,15m,30m,1h,2h,4h,6h,8h,12h
            start and end date - MM/DD/YYYY
            save_path
            remove_individ = "Remove" - will remove the individual csv's created. '
Output = Historical Data as specified. Accessable in save_path folder        '''
def Download_Data(coins,time_period,start_date,end_date,save_path,remove_individ):
    for coin in coins:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(' DOWNLOADING DATA SCRIPT Binance')
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Pair That is Running %s" %coin)
        print("Gonna Store It now")
        #coin_export= re.sub('[/]', '', coin)
        #store_data = DataClient().kline_data([coin],'%s' %time_period,start_date=start_date, end_date=end_date, storage=['csv','%s/' %save_path],progress_statements=True)
        #DataClient().kline_data([coin],'%s' %time_period,start_date=start_date, end_date=end_date, storage=['csv','%s/' %save_path],progress_statements=True)
        DataClient().kline_data([coin], time_period ,start_date=start_date, end_date=end_date, storage=['csv','%s/' %save_path],progress_statements=True)
        print("STORED")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(' FINISHED DOWNLOADING DATA')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    if remove_individ=='Remove':
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(' Deleting Left Over Data')
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        for coin in coins:
            shutil.rmtree(save_path+'/%s_data/' %time_period +coin+'/individual_csvs')
            print("Removed Individual CSVs")
            try:
                shutil.rmtree(save_path+'/%s_data/' %time_period +coin+'/old_concatenated_csvs')
                print("Removed old CSV s")
            except:
                print("There were no old CSV to remove")
        
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(' FINISHED ALL DATA STUFF')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")



def check_working():
    print("Package works - Nice one!")

