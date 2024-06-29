
from db import *
import numpy as np
from color_codes import *
from PIL import Image 
color_codes = color_codes



def emotional(day:daily_emotions):
    ttotal = []


    t1, m1 = string_to_ints(day.emotion1)
    t2, m2 = string_to_ints(day.emotion2)
    t3, m3 = string_to_ints(day.emotion3)
    t4, m4 = string_to_ints(day.emotion4)
    t5, m5 = string_to_ints(day.emotion5)
    t6, m6 = string_to_ints(day.emotion6)
    t7, m7 = string_to_ints(day.emotion7)
    t8, m8 = string_to_ints(day.emotion8)
    t9, m9 = string_to_ints(day.emotion9)
    t10, m10 = string_to_ints(day.emotion10)
    t11, m11 = string_to_ints(day.emotion11)
    t12, m12 = string_to_ints(day.emotion12)
    #calculations
    t1 = np.array(t1)
    ttotal.append(t1 * m1/10)



    t2 = np.array(t2)
    ttotal.append(t2 * m2/10)



    t3 = np.array(t3)
    ttotal.append(t3 * m3/10)



    t4 = np.array(t4)
    ttotal.append(t4 * m4/10)
    


    t5 = np.array(t5)
    ttotal.append(t5 * m5/10)
   


    t6 = np.array(t6)
    ttotal.append(t6 * m6/10)
 


    t7 = np.array(t7)
    ttotal.append(t7 * m7/10)


    t8 = np.array(t8)
    ttotal.append(t8 * m8/10)



    t9 = np.array(t9)
    ttotal.append(t9 * m9/10)
   


    t10 = np.array(t10)
    ttotal.append(t10 * m10/10)
   


    t11 = np.array(t11)
    ttotal.append(t11 * m11/10)



    t12 = np.array(t12)
    ttotal.append(t12 * m12/10)
    

    return ttotal

def img_creator():
    last = session.query(daily_emotions).order_by(daily_emotions.unq_id.desc()).first()
    if last.unq_id > 28:
       end = last.unq_id-28
       data = session.query(daily_emotions).order_by(daily_emotions.unq_id.desc()).filter(daily_emotions.unq_id > end)
       
       all = []
       for item in data:
          day = emotional(item)
          
          all.append(day)
       return True, all 
    else:
         return False, []



def painter(input):
   input = np.array(input)
   image = np.zeros((800, 2394,3), dtype=np.uint8) 
   if input.shape[0] == 28:
      for i in range(input.shape[0]):
         x = i%7 
         y = i//7
         super_f(image,x,y,input,i)
      imageresul = Image.fromarray(image.astype(np.uint8), 'RGB')
      imageresul.save("28_days.png")

      imageresul.show()
   else:
      print("the number of days is not enough:")
      print(input.shape[0])

def super_f(image,x,y,input,i):
   day = input[i]
   for m in range(1,len(day)):
      first = ((m-1)*31)+ x*341
      last = (m*31) + x*341
      f1 = day[m-1]
      f2 = day[m]
      fdeltar = (f2[0]-f1[0])/30
      fdeltag = (f2[1]-f1[1])/30
      fdeltab = (f2[2]-f1[2])/30
      w = 0
      for xlm in range(first,last):
         for ylm in range(y*200,(y+1)*200):
            
            image[ylm,xlm,0] = int(fdeltar*w + f1[0])
            image[ylm,xlm,1] = int(fdeltag*w + f1[1])
            image[ylm,xlm,2] = int(fdeltab*w + f1[2])
         w += 1  
   
      
