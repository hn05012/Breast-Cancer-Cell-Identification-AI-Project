import tkinter as tk
import random
import tkinter
import matplotlib.pyplot as plt
import numpy as np
import math
from math import pow
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from PIL import Image, ImageTk
from NN import x,y


root= tk.Tk()
root.title("Breast Cancer Evaluation") 
root.geometry('800x600')
root.configure(bg='Black')

#Here, all the variables have been defined as integers
clump_thickness=tk.IntVar()
Uniformity_of_size=tk.IntVar()
uniformity_of_shape = tk.IntVar()
marginal_adhesion = tk.IntVar()
epithelial_cell = tk.IntVar()
bare_nuclei = tk.IntVar()
chromotin = IntVar()
nucleoli = IntVar()
mitosis = IntVar()

#This function takes input from the network and makes a scatter plot to show the accuracy
def view_accuracy_graph():
    data3 = {'Actual Output Values': x,
            'Predicted Values': y}
            
    df3 = DataFrame(data3,columns=['Actual Output Values','Predicted Values'])
    figure3 = plt.Figure(figsize=(5,50), dpi=100, facecolor='black')
    ax3 = figure3.add_subplot(111)
    ax3.scatter(df3['Actual Output Values'],df3['Predicted Values'], color = 'r')
    scatter3 = FigureCanvasTkAgg(figure3, root) 
    scatter3.get_tk_widget().place(x=50, y=10, relheight=0.8)
    ax3.set_facecolor('black')
    ax3.xaxis.label.set_color('white')      
    ax3.yaxis.label.set_color('white')          
    ax3.tick_params(axis='x', colors='white')    
    ax3.tick_params(axis='y', colors='white')  
    ax3.spines['left'].set_color('white')        
    ax3.spines['bottom'].set_color('white') 
    ax3.spines['right'].set_color('white')        
    ax3.spines['top'].set_color('white')
    ax3.legend(['Predicted Values']) 
    ax3.set_xlabel('Actual Output Values')
    ax3.set_ylabel('Predicted Values')
    ax3.set_title('Actual Output Values Vs. Predicted Values', color= 'white')


#This function takes input from the network and makes a scatter plot to show the errors
def display_error_graph():
    data2 = {'Number of Iterations': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000],
                'Error': [780,594,866,59,853,189,748,626,973,195,942,610,347,442,18,782,295,827,761,264,644,270,648,615,940,926,719,96,23,186,213,176,633,833,138,34,502,618,457,584,92,518,843,345,104,656,830,839,483,110,536,218,1000,74,367,661,754,779,5,212,403,978,873,705,144,637,410,690,841,960,363,398,20,317,917,979,25,366,769,359,934,560,435,981,117,687,265,524,290,543,24,288,118,373,44,75,778,7,513,871,371,464,379,399,351,122,877,22,580,407,928,305,558,936,453,470,70,421,428,415,703,581,445,489,856,419,299,51,503,467,559,707,207,321,913,930,372,161,670,643,709,898,129,436,805,268,4,660,724,349,430,342,85,211,531,561,306,412,121,240,658,501,434,652,316,191,600,865,358,904,915,539,523,632,579,751,961,41,759,296,888,61,745,209,508,545,571,174,860,406,992,787,181,168,404,912,645,900,938,77,572,449,2,459,602,91,550,702,878,177,697,480,159,392,872,935,389,993,417,32,190,249,598,97,170,760,746,368,997,556,623,701,576,248,408,519,328,982,588,180,718,607,951,324,100,124,654,339,236,858,16,903,422,418,484,171,420,80,57,252,72,923,30,879,160,396,71,492,591,93,818,462,772,732,965,831,312,991,477,237,223,68,649,914,310,743,465,375,631,770,758,425,783,941,438,455,566,301,884,786,668,943,54,870,854,526,380,266,976,350,925,297,454,493,564,642,806,749,35,889,233,308,516,515,225,374,228,952,694,202,763,897,722,55,507,360,86,971,497,620,968,834,773,163,813,220,206,944,611,179,107,152,808,698,294,172,94,811,908,33,776,505,590,276,989,162,933,757,53,120,222,405,998,638,155,810,3,817,918,325,178,950,528,522,338,154,267,384,227,708,140,431,39,509,487,157,957,744,232,292,569,901,343,126,141,974,344,882,538,768,639,896,504,651,684,251,969,381,216,630,315,114,720,219,766,874,139,293,721,238,125,876,537,333,204,842,196,132,990,302,906,809,169,987,788,984,764,208,996,341,902,244,554,893,739,677,490,521,725,592,137,98,695,361,382,826,575,530,573,128,907,62,791,56,512,319,949,326,200,378,790,217,354,520,868,101,838,506,304,386,988,849,994,785,803,802,734,314,427,246,84,605,192,972,820,353,829,289,166,848,48,261,753,606,197,678,892,837,922,277,352,478,822,832,13,714,742,461,272,9,106,255,959,313,83,156,986,794,485,966,727,557,409,861,511,716,257,95,929,437,955,432,318,514,340,781,446,517,256,920,597,463,863,498,146,287,250,819,777,194,175,393,625,73,145,947,65,723,79,123,685,655,370,800,365,473,134,980,298,587,19,885,659,105,815,954,479,322,423,330,281,691,185,510,6,740,433,641,447,567,199,103,221,43,411,115,675,828,924,29,26,15,604,547,76,78,224,383,970,895,441,332,555,963,307,672,717,472,67,131,570,88,269,153,710,562,254,260,624,335,187,857,119,682,158,143,38,880,69,755,150,899,699,683,167,634,525,494,735,729,331,673,309,845,650,946,303,728,765,712,27,919,622,927,486,792,551,460,679,706,741,921,953,135,553,400,750,481,37,995,726,715,241,394,689,636,852,443,646,362,183,945,242,376,280,491,762,680,184,14,796,111,468,552,894,855,932,975,102,28,798,983,201,696,795,956,397,534,369,31,87,964,8,736,278,797,692,474,300,807,387,142,799,666,967,635,49,546,869,36,329,669,311,337,601,738,475,205,414,320,867,704,542,733,881,469,416,804,533,910,752,327,17,824,574,577,46,496,535,336,440,10,540,657,388,747,116,850,916,737,230,50,586,395,247,99,245,452,825,814,429,823,585,711,108,603,578,203,451,239,844,616,66,627,127,136,985,273,613,608,456,64,548,424,357,346,527,149,215,582,862,939,402,444,164,47,285,612,148,962,621,835,693,909,11,629,911,198,258,890,151,355,165,640,529,784,583,617,234,846,688,864,816,283,109,448,113,999,662,63,674,593,767,931,840,532,42,253,193,886,488,274,595,774,426,905,259,665,226,563,21,821,334,348,812,229,836,284,681,937,377,235,262,112,948,663,756,81,173,599,323,413,439,686,731,231,52,647,859,499,271,60,891,58,596,364,45,851,958,401,476,549,775,279,568,730,243,541,609,275,130,619,133,263,147,482,977,671,847,664,210,589,89,82,356,875,385,887,771,450,40,789,793,1,282,883,188,495,544,12,90,466,667,214,286,291,471,565,182,390,458,628,700,713,614,500,391,676,801,653]}
    df2 = DataFrame(data2,columns=['Number of Iterations','Error'])
    figure2 = plt.Figure(figsize=(5,50), dpi=100, facecolor='black')
    ax2 = figure2.add_subplot(111)
    ax2.scatter(df2['Number of Iterations'],df2['Error'], color = 'r')
    scatter3 = FigureCanvasTkAgg(figure2, root) 
    scatter3.get_tk_widget().place(x=900, y=10, relheight=0.8)
    ax2.set_facecolor('black')
    ax2.xaxis.label.set_color('white')        
    ax2.yaxis.label.set_color('white')          
    ax2.tick_params(axis='x', colors='white')    
    ax2.tick_params(axis='y', colors='white')  
    ax2.spines['left'].set_color('white')        
    ax2.spines['top'].set_color('white')
    ax2.spines['right'].set_color('white')        
    ax2.spines['bottom'].set_color('white')
    ax2.legend(['Error']) 
    ax2.set_xlabel('Number of Iterations')
    ax2.set_ylabel('Error')
    ax2.set_title('Number of Iterations Vs. Error', color= 'white')


#This function predicts whether a cell is cancerous or not
def predict_function():
    addition = int(clump_entry.get())+ int(size_entry.get()) + int(shape_entry.get())+ int(adhesion_entry.get()) + int(epithelial_entry.get())+ int(nuclei_entry.get())+ int(chromotin_entry.get()) + int(nucleoli.get())+ int(mitosis_entry.get())
    if addition==0:
        label = Label(root, text = 'Cancer cell is Benign', bg= 'Black', fg='White', padx = 5, pady = 5, font = 'calibre')
    elif addition==1:
        label = Label(root, text = "Cancer cell is Malignant", bg= 'Black', fg='White', padx = 5, pady = 5, font = 'calibre')
    label.pack()

#All the labels and enteries are made here 
clump_label = tk.Label(root, text = 'Clump Thickness : ', font=('calibre',10, 'bold'), bg= 'Black', fg='White')
clump_label.pack()

clump_entry = tk.Entry(root,textvariable = clump_thickness, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
clump_entry.pack(padx= 5, pady=5) 


size_label = tk.Label(root, text = 'Uniformity of Size : ', font = ('calibre',10,'bold'), bg= 'Black', fg='White')
size_label.pack()

size_entry=tk.Entry(root, textvariable = Uniformity_of_size, font = ('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
size_entry.pack(padx= 5, pady=5)


shape_label = tk.Label(root, text = 'Uniformity of Shape : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
shape_label.pack()

shape_entry = tk.Entry(root,textvariable = uniformity_of_shape , font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
shape_entry.pack(padx= 5, pady=5)


adhesion_label = tk.Label(root, text = 'Marginal Adhesion : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
adhesion_label.pack()

adhesion_entry = tk.Entry(root,textvariable = marginal_adhesion , font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
adhesion_entry.pack(padx= 5, pady=5)


epithelial_label = tk.Label(root, text = 'Epithelial Cell : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
epithelial_label.pack()

epithelial_entry = tk.Entry(root,textvariable = epithelial_cell, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
epithelial_entry.pack(padx= 5, pady=5)


nuclei_label = tk.Label(root, text = 'Bare Nuclei : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
nuclei_label.pack()

nuclei_entry = tk.Entry(root,textvariable = bare_nuclei, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
nuclei_entry.pack(padx= 5, pady = 5)


chromotin_label = tk.Label(root, text = 'Chromotin : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
chromotin_label.pack()

chromotin_entry = tk.Entry(root,textvariable = chromotin, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
chromotin_entry.pack(padx= 5, pady=5)

nucleoli_label = tk.Label(root, text = 'Nucleoili : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
nucleoli_label.pack()

nucleoli_entry = tk.Entry(root,textvariable = nucleoli, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
nucleoli_entry.pack(padx= 5, pady=5)

mitosis_label = tk.Label(root, text = 'Mitosis : ', font = ('calibre',10,'bold'),bg= 'Black', fg='White')
mitosis_label.pack()

mitosis_entry = tk.Entry(root,textvariable = mitosis, font=('calibre',10,'normal'), fg = 'Red', bg = 'Black', borderwidth= 5)
mitosis_entry.pack(padx= 5, pady=5)


#These 3 buttons plot the graphs and make the prediction based on the input
button=tk.Button(root,text = 'Predict',bg= 'Black', fg='White', command = predict_function)
button.pack()

button=tk.Button(root,text = 'Error Function',bg= 'Black', fg='White', command = display_error_graph)
button.pack()
  
button=tk.Button(root,text = 'View Accuracy',bg= 'Black', fg='White', command = view_accuracy_graph)
button.pack()
    
root.mainloop()
