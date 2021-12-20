# -*- coding: utf-8 -*-
"""
Created on Mon Oct 02 21:23:00 2017

@author: leduc
"""
# Import the libraries

import numpy as np
import pandas as pd

#############

# function that select the columns under a certain criteria
def SelectPoints(df_In, df_Col, ColumnCriteria):   
    column = range(ColumnCriteria.shape[0])
    df_temp=np.concatenate([df_In.values[df_In.values[::,df_Col] == ColumnCriteria.values[cc,0],::] for cc in column])
    return pd.DataFrame(df_temp)

# function that select the rows under a certain criteria
def SelectPointsRow(df_In, df_Row, ColumnCriteria):   
    column = range(ColumnCriteria.shape[0])
    df_temp=np.concatenate([df_In.values[::,df_In.values[df_Row,::] == ColumnCriteria.values[cc,0]] for cc in column],axis=1)
    return pd.DataFrame(df_temp)

#%% functions used in creating the data files
def create_parameter_file(file_name,letter,data_frame):
    column = range(data_frame.shape[1])
    row = range(data_frame.shape[0])
    
    f = open(file_name, 'w')
    for rr in row:
        for cc in column:
            if cc<len(letter)-1:
                f.write("%s." %((letter[cc])+str(data_frame.values[rr,cc]).strip("[u'']"))) 
            if cc==len(letter)-1:
                f.write("%s" %((letter[cc])+str(data_frame.values[rr,cc]).strip("[u'']")))
            if cc==len(letter):
                f.write("\t%f" %(data_frame.values[rr,cc]))
        f.write("\n")
    f.close()
    
def create_parameter_file_no_strip(file_name,letter,data_frame):
    column = range(data_frame.shape[1])
    row = range(data_frame.shape[0])
    
    f = open(file_name, 'w')
    for rr in row:
        for cc in column:
            if cc<len(letter)-1:
                f.write("%s." %((letter[cc])+str(data_frame.values[rr,cc]))) 
            if cc==len(letter)-1:
                f.write("%s" %((letter[cc])+str(data_frame.values[rr,cc])))
            if cc==len(letter):
                f.write("\t%f" %(data_frame.values[rr,cc]))
        f.write("\n")
    f.close()


    
    

def create_parameter_fullName_file(file_name,data_frame):
    column = range(data_frame.shape[1])
    row = range(data_frame.shape[0])
    
    f = open(file_name, 'w')
    for rr in row:
        for cc in column:
            f.write(str(data_frame.values[rr,cc]).strip("[u'']"))            
            if cc==len(data_frame):
                f.write("\t%f" %(data_frame.values[rr,cc]))
        f.write("\n")
    f.close()

def create_parameter_file_numbers(file_name,letter,data_frame):
    column = range(data_frame.shape[1])
    row = range(data_frame.shape[0])
    
    f = open(file_name, 'w')
    for rr in row:
        for cc in column:
            if cc<len(letter)-1:
                f.write("%s." %((letter[cc])+str(int(data_frame.values[rr,cc])).strip("[u'']"))) 
            if cc==len(letter)-1:
                f.write("%s" %((letter[cc])+str(int(data_frame.values[rr,cc])).strip("[u'']")))
            if cc==len(letter):
                f.write("\t%f" %(data_frame.values[rr,cc]))
        f.write("\n")
    f.close()






def create_parameter_filex2(filename,letter,dataframe):
    row=range(dataframe.shape[0])
    cc=dataframe.shape[1]
    dataframe[list(range(len(letter)))]=dataframe[list(range(len(letter)))].astype(int) 
    dataframe[list(range(len(letter)))]=letter+dataframe[list(range(len(letter)))].astype(str) #Append letters to dataframe
    f=open(filename,'w')    
    for rr in row:
        if cc==1:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'\n')
        if cc==2:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'\t'+str(dataframe[1][rr])+'\n')
        if cc==3:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'\t'+str(dataframe[2][rr])+'\n')
        if cc==4:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'\t'+str(dataframe[3][rr])+'\n')
        if cc==5:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'\t'+str(dataframe[4][rr])+'\n')
        if cc==6:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'\t'+str(dataframe[5][rr])+'\n')
        if cc==7:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'.'+str(dataframe[5][rr]).strip("[u'']")+'\t'+str(dataframe[6][rr])+'\n')       
    f.close() 



def create_parameter_filex3(filename,letter,dataframe):
    row=range(dataframe.shape[0])
    cc=dataframe.shape[1]
    #dataframe[list(range(len(letter)))]=dataframe[list(range(len(letter)))].astype(int) 
    dataframe[list(range(len(letter)))]=letter+dataframe[list(range(len(letter)))].astype(str) #Append letters to dataframe
    f=open(filename,'w')    
    for rr in row:
        if cc==1:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'\n')
        if cc==2:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'\t'+str(dataframe[1][rr])+'\n')
        if cc==3:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'\t'+str(dataframe[2][rr])+'\n')
        if cc==4:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'\t'+str(dataframe[3][rr])+'\n')
        if cc==5:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'\t'+str(dataframe[4][rr])+'\n')
        if cc==6:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'\t'+str(dataframe[5][rr])+'\n')
        if cc==7:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'.'+str(dataframe[5][rr]).strip("[u'']")+'\t'+str(dataframe[6][rr])+'\n')       
        if cc==8:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'.'+str(dataframe[5][rr]).strip("[u'']")+'.'+str(dataframe[6][rr]).strip("[u'']")+'\t'+str(dataframe[7][rr])+'\n') 
        if cc==9:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'.'+str(dataframe[5][rr]).strip("[u'']")+'.'+str(dataframe[6][rr]).strip("[u'']")+'.'+str(dataframe[7][rr]).strip("[u'']")+'\t'+str(dataframe[8][rr])+'\n')             
        if cc==10:
            f.write(str(dataframe[0][rr]).strip("[u'']")+'.'+str(dataframe[1][rr]).strip("[u'']")+'.'+str(dataframe[2][rr]).strip("[u'']")+'.'+str(dataframe[3][rr]).strip("[u'']")+'.'+str(dataframe[4][rr]).strip("[u'']")+'.'+str(dataframe[5][rr]).strip("[u'']")+'.'+str(dataframe[6][rr]).strip("[u'']")+'.'+str(dataframe[7][rr]).strip("[u'']")+'.'+str(dataframe[8][rr]).strip("[u'']")+'\t'+str(dataframe[9][rr])+'\n') 
    f.close()  



def create_data_file(data_frame,filename):
    #    np.savetxt(filename, data_frame_out,fmt='{0: <{1}}'.format("%s", 6))
    np.savetxt(filename, data_frame,fmt='%-6s')    

    