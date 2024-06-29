import numpy as np # for the array operations
import tkinter as tk
from tkinter import ttk
from random import *
from db import *
from datetime import datetime, timedelta
from tkinter import messagebox
from color_codes import *
from img_creator import img_creator, painter
color_codes = color_codes


def rgb_to_hex(rgb):
  """Converts an RGB tuple (255, 255, 255) to a hex color string (#FFFFFF)"""
  hex_color = "#" + ''.join(format(val, '02x') for val in rgb)
  return hex_color.upper()

def unique_id():
    last = session.query(daily_emotions).order_by(daily_emotions.unq_id.desc()).first()
    return (last.unq_id + 1)

def emotional_avg(day:daily_emotions):
    mass = 0
    ttotal = np.array((0,0,0))
    t1 , m1 = string_to_ints(day.emotion1)
    # Assuming string_to_ints returns a list of ints and m1
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
    ttotal += t1 * m1
    mass += m1


    t2 = np.array(t2)
    ttotal += t2 * m2
    mass += m2


    t3 = np.array(t3)
    ttotal += t3 * m3
    mass += m3


    t4 = np.array(t4)
    ttotal += t4 * m4
    mass += m4


    t5 = np.array(t5)
    ttotal += t5 * m5
    mass += m5


    t6 = np.array(t6)
    ttotal += t6 * m6
    mass += m6


    t7 = np.array(t7)
    ttotal += t7 * m7
    mass += m7


    t8 = np.array(t8)
    ttotal += t8 * m8
    mass += m8


    t9 = np.array(t9)
    ttotal += t9 * m9
    mass += m9


    t10 = np.array(t10)
    ttotal += t10 * m10
    mass += m10


    t11 = np.array(t11)
    ttotal += t11 * m11
    mass += m11


    t12 = np.array(t12)
    ttotal += t12 * m12
    mass += m12
    if mass == 0:
        mass = 1
    xx = int(ttotal[0]/ mass)
    xy = int(ttotal[1]/ mass)
    xz = int(ttotal[2]/ mass)
    return np.array([xx,xy,xz])
    
def update_momentum():
        last = session.query(daily_emotions).order_by(daily_emotions.unq_id.desc()).first()
        end_index = last.unq_id - 5
        old_data = session.query(daily_emotions).filter(daily_emotions.unq_id >= end_index)
        rgb = np.array((0,0,0))
        density = 0
        for dt in old_data:
           rgb +=  emotional_avg(dt)
           density += 1
           
        momentum_values = [int(rgb[0]/density),int(rgb[1]/density),int(rgb[2]/density)]
        # Update momentum widget with current values
        return momentum_values




class SimpleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Emotion Tracker By: DrLlama")

        # Create 12 scales horizontally
        self.scales = []
        self.labels = []
        text_var = tk.StringVar()
        text_var.set("The color")
        for i in range(12):
            scale = tk.Scale(self.root, from_=0, to=10, orient='horizontal', label=emotions[i])
            scale.grid(row=i, column=0, padx=20, pady=20)
            self.scales.append(scale)
            label = tk.Label(root,  
                             anchor=tk.CENTER,       
                             bg=rgb_to_hex(color_codes[i]),      
                             height=3,              
                             width=15,              
                             bd=3,                  
                             font=("Arial", 10, "bold"), 
                             cursor="hand2",   
                             fg="black",             
                             padx=10,               
                             pady=10,                
                             justify=tk.CENTER,    
                             relief=tk.RAISED,     
                             underline=0,           
                             wraplength=250         
                            )
            label.grid(row=i, column=1, padx=10, pady=10)


        # Button to add to database (simulated action)
        self.add_button = ttk.Button(self.root, text="Add to DB", command=self.add_to_database)
        self.add_button.grid(row=0, column=5, columnspan=3, pady=10)

        # Momentum widget displaying a list of three integers
        moment = update_momentum()
        text_color = [255-moment[0],255-moment[1],255-moment[2]]
        # Create a StringVar to associate with the label
        mom = tk.StringVar()
        mom.set("Calculated Momentum: "+ str(moment))


        label1 = tk.Label(root, 
                 textvariable=mom, 
                 anchor=tk.CENTER,       
                 bg=rgb_to_hex(moment),      
                 height=3,              
                 width=29,              
                 bd=3,                  
                 font=("Arial", 12, "bold"), 
                 cursor="hand2",   
                 fg=rgb_to_hex(text_color),             
                 padx=10,               
                 pady=10,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 underline=0,           
                 wraplength=250         
                )
        label1.grid(row=1, column=5, padx=10, pady=10)


        # Button to create image for the past month
        self.image_button = ttk.Button(self.root, text="Create Image for Past Month", command=self.create_image)
        self.image_button.grid(row=2, column=5, columnspan=3,padx=10, pady=10)

    def add_to_database(self):
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        ex = session.query(daily_emotions.date).filter(daily_emotions.date == current_date)
        access = session.query(literal(True)).filter(ex.exists()).scalar()
        if  access == True:
            messagebox.showwarning("Attention", "A data entry for today already exists. To ensure accurate records, please only submit one entry per day.")   
            
              
        else:
            db_list = []
            data = [scale.get() for scale in self.scales]
            for i in range(len(data)):
                db_list.append(ints_to_string(color_codes[i], data[i]))
            #change this date ________ 
            add = daily_emotions(unique_id(),current_date,db_list[0],db_list[1],db_list[2],db_list[3],db_list[4],db_list[5],db_list[6],db_list[7],db_list[8],db_list[9],db_list[10],db_list[11])
            session.add(add)
            session.commit()
            messagebox.showinfo("", "Data successfully committed to the database.") 



    def create_image(self):
        
        # Get current date and calculate one month ago
        bool , clr = img_creator()
        if bool == True:
            painter(clr)
            messagebox.showinfo("img.jpeg", "Successfully generated a image")
        else:
            messagebox.showwarning("img.jpeg", "Error occurred while creating the image(At least 28 days of entry required!!)")
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleUI(root)
    root.mainloop()
    session.close()
