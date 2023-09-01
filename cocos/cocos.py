import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import statistics as stats
from cocos.utils.errors import *
plt.style.use('seaborn')

class Cocos:
    def __init__(self,file_data):
        self.data_list = ['month', 'ph', 'potassium','phosphorus','nitrogen']
        self.verify_file_data(file_data)
        self.minerate_data()
    
    
    
    def verify_file_data(self,file_data):
        if os.path.isfile(file_data):
            file_type = file_data.split('.')[-1]
            if 'osd' or 'xlsx' in file_type:
                self.data = pd.read_excel(file_data)
                for key in self.data_list:
                    if not (key in self.data):
                        raise KeyDataNotFound(key,file_data)
            else:
                raise FileIsNotExcelType(file_data,file_type)
        else:
            raise FileNotFound(file_data)
        
    
    
    def minerate_data(self):
        dicts_minerate = {'data_base':self.data}
        for key in self.data_list:
            data_key = self.data[key]
            dicts_minerate[key] = {'mean':stats.mean(data_key)}
            dicts_minerate[key]['std'] = stats.stdev(data_key)
        self.dict_data = dicts_minerate
        
        
        
    def __getitem__(self, key):
        if key in self.data:
            return self.dict_data[key]
        else:
            list_key = list(self.dict_data.keys())
            raise KeyError(f"A chave '{key}' não existe no dicionário personalizado. As chaves disponíveis são: {list_key} ")

        
    
    def _plot_ph(self):
        data = self.data[::2]
        data.plot(x='month',y='ph',kind='bar')

        mean_ph = self.dict_data['ph']['mean']
        std_ph = self.dict_data['ph']['std']

        if mean_ph >= 6.:
            line_mean = 'green'
            comment = 'O solo está saudável!'
            comment_title ='Saudável!'

        if mean_ph < 6.:
            line_mean = 'red'
            comment = 'O solo está doente!\n por favor, aumente a quantidade nitrogênio\ne potássio no solo!'
            comment_title = 'Perigo!'

        label_plot = f'média do ph [ph={stats.mean(data["ph"]):.2f}]\n{comment}'
        label_std = f'desvio padrão do ph \n[ph = {std_ph:.2f}]'
        title_plot = f'Variação do Ph do Solo\nresumo: {comment_title}'

        median_ph = np.array([mean_ph for _ in data['ph']])
        
        plt_ = plt
        plt_.title(title_plot,fontweight='bold')
        plt_.plot(median_ph,'--',label=label_plot,color=line_mean)
        plt_.plot(median_ph+std_ph,'--',lw=.4,label=label_std,color=line_mean)
        plt_.plot(median_ph-std_ph,'--',lw=.4,color=line_mean)
        legend = plt_.legend(frameon=1)
        frame = legend.get_frame()
        frame.set_facecolor('white')
        
        return plt_


    def _plot_nitro(self):
        data = self.data[::2]
        data.plot(x='month',y='nitrogen',kind='bar')

        mean_ph = self.dict_data['nitrogen']['mean']
        std_ph = self.dict_data['nitrogen']['std']

        if mean_ph <= .3:
            line_mean = 'green'
            comment = 'O solo está saudável!'
            comment_title ='Saudável!'

        if mean_ph > .3:
            line_mean = 'red'
            comment = 'O solo está doente!'
            comment_title = 'Perigo!'

        label_plot = f'média do Nitrogen [nitrogen={stats.mean(data["nitrogen"]):.2f}]\n{comment}'
        label_std = f'desvio padrão do Nitrogen \n[nitrogen = {std_ph:.2f}]'
        title_plot = f'Variação do Nitrogen do Solo\nresumo: {comment_title}'

        median_ph = np.array([mean_ph for _ in data['ph']])
        
        plt_ = plt
        plt_.title(title_plot,fontweight='bold')
        plt_.plot(median_ph,'--',label=label_plot,color=line_mean)
        plt_.plot(median_ph+std_ph,'--',lw=.4,label=label_std,color=line_mean)
        plt_.plot(median_ph-std_ph,'--',lw=.4,color=line_mean)
        legend = plt_.legend(frameon=1)
        frame = legend.get_frame()
        frame.set_facecolor('white')
        
        return plt_
    
    def plot_by_key(self,key,plt=plt):
        if key=='ph':
            return self._plot_ph()
        if key=='nitrogen':
            return self._plot_nitro()
        data = self.data
        data = data[::2]
        data.plot(x='month',y=key,kind='bar')

        mean_key = self.dict_data[key]['mean']
        std_key = self.dict_data[key]['std']

        label_plot = f'média do {key} [{key} = {mean_key:.2f}]'
        label_std = f'desvio padrão do {key} \n[{key} = {std_key:.2f}]'
        title_plot = f'Variação do {key} do Solo\n'

        median_key = np.array([mean_key for _ in data['ph']])

        plt_ = plt
        plt_.title(title_plot,fontweight='bold')
        plt_.plot(median_key,'--',label=label_plot,color='green')
        plt_.plot(median_key+std_key,'--',lw=.4,label=label_std,color='green')
        plt_.plot(median_key-std_key,'--',lw=.4,color='green')
        legend = plt_.legend(frameon=1)
        frame = legend.get_frame()
        frame.set_facecolor('white')

        return plt_





