# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:22:41 2018

@author: weiping
"""

import matplotlib.pyplot as plt
import numpy as np





class visual:
    fig_size=(10,10)
    DPI=100
    fontsize=17
    loc='upper right'
    def __init__(self,data_x,data_y):
        self.data_x=data_x
        self.data_y=data_y
        self.FIG, self.AX = plt.subplots(figsize=visual.fig_size,dpi=visual.DPI)
        self.xmin, self.xmax=np.min(data_x), np.max(data_x)
        self.ymin, self.ymax=np.min(data_y), np.max(data_y)
        self.fontsize = visual.fontsize
        self.loc = visual.loc

    def set_lim(self,start,end,flag):  #flag=0:x轴，flog=1:y轴
        if flag == 0:
            self.AX.set_xlim(left = start, right=end)
        elif flag == 1:
            self.AX.set_ylim(bottom = start, top = end)
        else:
            print("flag could only be 0 or 1, pls try again:")

    def PLOT(self,color='black',linestyle='--',linewidth=1,marker='.',label=' '):
        self.AX.plot(self.data_x,self.data_y,color=color,linestyle=linestyle
                ,linewidth=linewidth,marker=marker,label=label)

        self.AX.legend(fontsize=self.fontsize,loc=self.loc)
        self.AX.grid(True,alpha=0.3)

    def horizontal_line(self, y=0, x_min=0, x_max=0, colors='black',linestyles='solid',label=None):
        y,x_min,x_max = self.ymax, self.xmin,self.xmax
        if label == None:
            label = r'{0:}'.format(y)
        self.AX.hlines(y,x_min,x_max,colors=colors,linestyles=linestyles,label=label)
        self.AX.legend()

    def vertical_line(self, x=0, y_min=0, y_max=0, colors='black',linestyles='solid',label=None):
        x,y_min,y_max = self.xmax, self.ymin,self.ymax
        if label == None:
            label = r'{0:}'.format(x)
        self.AX.vlines(x,y_min,y_max,colors=colors,linestyles=linestyles,label=label)
        self.AX.legend()

    def set_label(self,text=' ',fontsize=0,flag=0):
        if fontsize == 0:
            fontsize = self.fontsize
        if flag==0:
            self.AX.set_xlabel(text,fontsize=fontsize)
        else:
            self.AX.set_ylabel(text,fontsize=fontsize)

    def SHOW(self):
        self.FIG.show()

    def save(self,name,Format=None):
        if Format == None:
            Format = 'pdf'
        self.FIG.savefig(name+'.'+Format,format=Format)


    # an addition function providing hints
    def tips(self):
        print('fig_size=(10,10); DPI=100;fontsize=17;loc="upper right";\n')
        print('set_lim(self,start,end,flag);\n')
        print('PLOT(self,color='black',linestyle='--',linewidth=1,marker='.',label=' ');\n')
        print('horizontal_line(self, y=0, x_min=0, x_max=0, colors='black',linestyles='solid',label=None);\n')
        print('vertical_line(self, x=0, y_min=0, y_max=0, colors='black',linestyles='solid',label=None);\n')
        print('set_label(self,text=' ',fontsize=0,flag=0);\n')
        print('SHOW(self);\n')
        print('save(self,name,Format=None);\n')
