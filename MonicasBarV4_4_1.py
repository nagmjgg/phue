

'''

http://thinkingtkinter.sourceforge.net/

To connect a bridge, you have to use both the ip_address and the username
one example is b=Bridge("192.168.0.20","sew45dsre3435esdwe")
To find the username on a hue bridge on a local ethernet, open the https://discovery.meethue.com/ and write down the id.

usuarios>
[{"id":"ecb5fafffe1d6913","internalipaddress":"192.168.4.30"},{"id":"ecb5fafffe1f2007","internalipaddress":"192.168.4.35"},{"id":"ecb5fafffe1f20c7","internalipaddress":"192.168.4.36"}]

https://developers.meethue.com/develop/get-started-2/

Stairs = 192.168.4.30

[
   {
      "success": {
         "username": "VWvVRF49nXW6YfkqfFDT3hIE6seCQTTB5HvcoKKu"
      }
   }
]

Ejecuto comando lights con mi usuario nuevo
http://192.168.4.30/api/VWvVRF49nXW6YfkqfFDT3hIE6seCQTTB5HvcoKKu/lights

{"1":{"state":{"on":true,"bri":202,"hue":65173,"sat":89,"effect":"none","xy":[0.4857,0.3510],"ct":413,"alert":"select","colormode":"xy","mode":"homeautomation","reachable":true},"swupdate":{"state":"noupdates","lastinstall":"2021-06-13T19:54:41"},"type":"Extended color light","name":"Stairs Hue color lamp 1","modelid":"LCA003","manufacturername":"Signify Netherlands B.V.","productname":"Hue color Lamp","capabilities":{"certified":true,"control":{"mindimlevel":200,"maxlumen":800,"colorgamuttype":"C","colorgamut":[[0.6915,0.3083],[0.1700,0.7000],[0.1532,0.0475]],"ct":{"min":153,"max":500}},"streaming":{"renderer":true,"proxy":true}},"config":{"archetype":"classicbulb","function":"mixed","direction":"omnidirectional","startup":{"mode":"safety","configured":true}},"uniqueid":"00:17:88:01:09:59:a8:65-0b","swversion":"1.76.6","swconfigid":"598716A0","productid":"Philips-LCA003-1-A19ECLv6"},"2":{"state":{"on":true,"bri":202,"hue":0,"sat":254,"effect":"none","xy":[0.6915,0.3083],"ct":153,"alert":"select","colormode":"xy","mode":"homeautomation","reachable":true},"swupdate":{"state":"noupdates","lastinstall":"2021-06-13T19:54:51"},"type":"Extended color light","name":"Stairs Hue color lamp 2","modelid":"LCA003","manufacturername":"Signify Netherlands B.V.","productname":"Hue color Lamp","capabilities":{"certified":true,"control":{"mindimlevel":200,"maxlumen":800,"colorgamuttype":"C","colorgamut":[[0.6915,0.3083],[0.1700,0.7000],[0.1532,0.0475]],"ct":{"min":153,"max":500}},"streaming":{"renderer":true,"proxy":true}},"config":{"archetype":"classicbulb","function":"mixed","direction":"omnidirectional","startup":{"mode":"safety","configured":true}},"uniqueid":"00:17:88:01:09:5d:ee:aa-0b","swversion":"1.76.6","swconfigid":"598716A0","productid":"Philips-LCA003-1-A19ECLv6"},"3":{"state":{"on":true,"bri":202,"hue":1102,"sat":253,"effect":"none","xy":[0.6679,0.3254],"ct":153,"alert":"select","colormode":"xy","mode":"homeautomation","reachable":true},"swupdate":{"state":"noupdates","lastinstall":"2021-06-13T19:54:47"},"type":"Extended color light","name":"Stairs Hue color Lamp 3","modelid":"LCA003","manufacturername":"Signify Netherlands B.V.","productname":"Hue color Lamp","capabilities":{"certified":true,"control":{"mindimlevel":200,"maxlumen":800,"colorgamuttype":"C","colorgamut":[[0.6915,0.3083],[0.1700,0.7000],[0.1532,0.0475]],"ct":{"min":153,"max":500}},"streaming":{"renderer":true,"proxy":true}},"config":{"archetype":"sultanbulb","function":"mixed","direction":"omnidirectional","startup":{"mode":"safety","configured":true}},"uniqueid":"00:17:88:01:09:5d:ec:e1-0b","swversion":"1.76.6","swconfigid":"598716A0","productid":"Philips-LCA003-1-A19ECLv6"},"4":{"state":{"on":true,"bri":202,"hue":0,"sat":254,"effect":"none","xy":[0.6915,0.3083],"ct":153,"alert":"select","colormode":"xy","mode":"homeautomation","reachable":true},"swupdate":{"state":"noupdates","lastinstall":"2021-06-13T19:54:44"},"type":"Extended color light","name":"Stairs Hue color Lamp 4","modelid":"LCA003","manufacturername":"Signify Netherlands B.V.","productname":"Hue color Lamp","capabilities":{"certified":true,"control":{"mindimlevel":200,"maxlumen":800,"colorgamuttype":"C","colorgamut":[[0.6915,0.3083],[0.1700,0.7000],[0.1532,0.0475]],"ct":{"min":153,"max":500}},"streaming":{"renderer":true,"proxy":true}},"config":{"archetype":"classicbulb","function":"mixed","direction":"omnidirectional","startup":{"mode":"safety","configured":true}},"uniqueid":"00:17:88:01:09:5d:f5:d7-0b","swversion":"1.76.6","swconfigid":"598716A0","productid":"Philips-LCA003-1-A19ECLv6"}}


Center = 192.168.4.36

[
   {
      "success": {
         "username": "CpFcYyysWmNClDpIgEayDru1JdF4iHvYwkFiNKbj"
      }
   }
]


Entrance = 192.168.4.35

[
   {
      "success": {
         "username": "KAImBShLUywht8EcB6DKjk5IuqwLmNrUWliULlZt"
      }
   }
]

Examples>
https://github.com/studioimaginaire/phue/tree/master/examples
https://github.com/studioimaginaire/phue/blob/master/examples/rgb_colors.py

Pick Colors...
https://www.rapidtables.com/web/color/RGB_Color.html
https://www.codewithharry.com/videos/python-gui-tkinter-hindi-25
https://python.hotexamples.com/examples/phue/Bridge/set_light/python-bridge-set_light-method-examples.html
'''
#import schedule
from phue import *
from phue import Bridge
import time
import random
from tkinter import *
from tkinter import colorchooser
import tkinter as tk
import threading

random_flag = True
schedule_flag = False
pause_time = 5
one_light_pause = 2
transition_pause = 5
transitions_qty = 20

automatic_mode_pause = 180
version = "_V4_4_1"


def create_btn(mode):
    cmd = lambda: self.list.config(selectmode=mode)
    return tk.Button(self, command=cmd,
                     text=mode.capitalize())

main_window = Tk()

lights_bright_value = 200

active = False

def online():
    global active
    active = True
    print("Online")

    bridge_stairs = "192.168.4.30"
    bridge_stairs_user = "VWvVRF49nXW6YfkqfFDT3hIE6seCQTTB5HvcoKKu"
    bridge_center = "192.168.4.36"
    bridge_center_user = "CpFcYyysWmNClDpIgEayDru1JdF4iHvYwkFiNKbj"
    bridge_entrance = "192.168.4.35"
    bridge_entrance_user = "KAImBShLUywht8EcB6DKjk5IuqwLmNrUWliULlZt"

    b = Bridge(bridge_stairs, bridge_stairs_user)
    b.connect()

    c = Bridge(bridge_center, bridge_center_user)
    c.connect()

    d = Bridge(bridge_entrance, bridge_entrance_user)
    d.connect()

    b.get_api()
    c.get_api()
    d.get_api()

    b.set_light([1, 2, 3, 4], 'on', True)
    c.set_light([1, 2, 3, 4], 'on', True)
    d.set_light([1, 2, 3, 4], 'on', True)

    b.set_light([1, 2, 3, 4], 'bri', lights_bright_value)
    c.set_light([1, 2, 3, 4], 'bri', lights_bright_value)
    d.set_light([1, 2, 3, 4], 'bri', lights_bright_value)

    set_lights_config()
# Set brightness of lamp 1 to max
'''
for i in range(1,4):
    b.set_light(i, 'on', True)
'''
def offline():
    global active
    active = False
    print("Offline")

def running():
    print(">", end="")

def set_lights_config():
    print("Set lights config")
    if active == True:
        bright_value = lights_bright_value.get()
        #print(bright_value)
        b.set_light([1,2,3,4], 'on', True)
        c.set_light([1,2,3,4], 'on', True)
        d.set_light([1,2,3,4], 'on', True)
        b.set_light([1,2,3,4], 'bri', bright_value)
        c.set_light([1,2,3,4], 'bri', bright_value)
        d.set_light([1,2,3,4], 'bri', bright_value)
    else:
        print("Not Active, ", end="")


def color_all(color=25000):
    running()
    if active == True:
        b.set_light([1, 2, 3, 4], 'hue', color)
        c.set_light([1, 2, 3, 4], 'hue', color)
        d.set_light([1, 2, 3, 4], 'hue', color)
    else:
        print("Not Active, ", end="")

def set_light_bri(qty,light=[1, 2, 3, 4]):
    if active == True:
        b.set_light(light, 'bri', qty)
        c.set_light(light, 'bri', qty)
        d.set_light(light, 'bri', qty)
    else:
        print("Not Active, ", end="")

def set_light_xy(array_x_y,light=[1, 2, 3, 4],bright=lights_bright_value):
    if active == True:
        b.set_light(light, 'xy', array_x_y)
        c.set_light(light, 'xy', array_x_y)
        d.set_light(light, 'xy', array_x_y)
    else:
        print("Not Active, ", end="")

def set_one_light_xy(array_x_y,light=[1, 2, 3, 4],bridge=random.randint(1,4),bright=lights_bright_value):
    if active == True:
        if bridge==1:
            b.set_light(light, 'xy', array_x_y)
            b.set_light(light, 'bri', bright)
        if bridge==2:
            c.set_light(light, 'xy', array_x_y)
            c.set_light(light, 'bri', bright)
        if bridge==3:
            d.set_light(light, 'xy', array_x_y)
            d.set_light(light, 'bri', bright)
    else:
        print("Not Active, ", end="")

def rgb_xy(Red,Green,Blue):
    X = 0.4124 * Red + 0.3576 * Green + 0.1805 * Blue  # Stack Overflow code
    Y = 0.2126 * Red + 0.7152 * Green + 0.0722 * Blue
    Z = 0.0193 * Red + 0.1192 * Green + 0.9505 * Blue

    xx = X / (X + Y + Z)
    yy = Y / (X + Y + Z)

    return [xx, yy]

def toRGB(Red,Green,Blue):
    running()
    array_x_y = rgb_xy(Red,Green,Blue)
    set_light_xy(array_x_y)

    #print(xx,yy)
    #set_light_xy([xx,yy])


def random_color(initial=25000,final=60000,times=10):

    if active == True:
        if random_flag:
            running()
            #print("Random flag_active")
            global pause_time

            Red = random.randint(1, 254)
            Green = random.randint(1, 254)
            Blue = random.randint(1, 254)
            array_x_y = rgb_xy(Red, Green, Blue)
            set_light_xy(array_x_y)

            main_window.after(pause_time*1000,random_color)
    else:
        print("Not Active, ", end="")
        
def start_random_color():
    """Stop scanning by setting the global flag to False."""
    global random_flag
    random_flag = True
    random_color()

def stop_random_color():
    """Stop scanning by setting the global flag to False."""
    global random_flag
    random_flag = False

def toRGB_random_one_light(Red,Green,Blue):

    Red = random.randint(1, 254)
    Green = random.randint(1, 254)
    Blue = random.randint(1, 254)

    array_x_y = rgb_xy(Red,Green,Blue)

    #print(xx,yy)
    for i in range(transitions_qty):
        running()
        set_light_bri(random.randint(50,255))
        set_light_xy(array_x_y)

        global pause_time
        #time.sleep(pause_time)
        main_window.after(pause_time*1000)

def toRGB_random_one_by_one_light():

    for i in range(transitions_qty*3):
        running()

        Red = random.randint(1, 254)
        Green = random.randint(1, 254)
        Blue = random.randint(1, 254)

        array_x_y = rgb_xy(Red, Green, Blue)

        light=random.randint(1,4)
        bridge=random.randint(1,3)
        bright=random.randint(50,200)

        set_one_light_xy(array_x_y,light,bridge,bright)

        main_window.after(one_light_pause*1000)

def toRGB_random_color_one_light():

    for i in range(transitions_qty):
        running()
        Red = random.randint(1,254)
        Green = random.randint(1,254)
        Blue = random.randint(1,254)

        array_x_y = rgb_xy(Red,Green,Blue)

        set_light_bri(random.randint(50, 255))

        set_light_xy(array_x_y)

        main_window.after(one_light_pause)

def colombian_colors_transition():

    colombian_colors = ((255,255,0),(0,0,255),(255,0,0))

    for times in range(transitions_qty):
        for i in colombian_colors:
            running()
            #print(i)
            global pause_time

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            #print(rx, gx, bx)

            array_x_y = rgb_xy(rx,gx,bx)
            set_light_xy(array_x_y)

            main_window.after(transition_pause*1000)

def usa_colors_transition():
    #pastel_colors = ((200,0,205),(0,0,226),(255,228,225),(255,182,174),(255,244,225))

    usa_colors = ((255,255,255),(255,0,0),(0,0,255))

    for times in range(transitions_qty):
        for i in usa_colors:
            running()
            #print(i)
            global pause_time

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            #print(rx, gx, bx)

            array_x_y = rgb_xy(rx,gx,bx)
            set_light_xy(array_x_y)

            main_window.after(transition_pause*1000)

def dark_colors_transition_yellow_violet_blue():

    #yellow - violet - ocean blue
    dark_colors = ((234, 252, 21),(181,5,218),(4,247,240),)

    for times in range(transitions_qty):
        for i in dark_colors:
            running()
            #print(i)
            global pause_time

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            #print(rx, gx, bx)

            array_x_y = rgb_xy(rx,gx,bx)
            set_light_xy(array_x_y)
            #time.sleep(pause_time)
            main_window.after(transition_pause*1000)

def dark_colors_transition_blue():

    dark_colors = ((37, 254, 243),(0,0,255))

    for times in range(transitions_qty):
        for i in dark_colors:
            running()
            #print(i)
            global pause_time

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            #print(rx, gx, bx)

            array_x_y = rgb_xy(rx,gx,bx)
            set_light_xy(array_x_y)
            #time.sleep(pause_time)
            main_window.after(transition_pause*1000)

def dark_colors_transition_yellow_green():

    dark_colors = ((244, 251, 4),(0,255,0))

    for times in range(transitions_qty):
        for i in dark_colors:
            running()
            global pause_time

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            #print(rx, gx, bx)

            array_x_y = rgb_xy(rx,gx,bx)
            set_light_xy(array_x_y)
            #time.sleep(pause_time)
            main_window.after(transition_pause*1000)

# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    #print(color_code)
    rcolor = color_code[0][0]
    gcolor = color_code[0][1]
    bcolor = color_code[0][2]
    #print(rcolor,gcolor,bcolor)
    colors = (rcolor, gcolor, bcolor)
    return colors

def choosed_color_light():
    color=choose_color()
    array_x_y = rgb_xy(color[0], color[1], color[2])
    set_light_xy(array_x_y)

def switch(i):
    if i == 1:
        print("Dark Colors Transition Blue")
        dark_colors_transition_blue()
    if i == 2:
        print("Dark Colors Transition Yellow - Violet - Blue")
        dark_colors_transition_yellow_violet_blue()
    if i == 3:
        print("Dark Colors Transition Yellow - Green")
        dark_colors_transition_yellow_green()
    if i == 4:
        print("Random Colors All Lights")
        start_random_color()
        stop_random_color()
    if i == 5:
        print("Red")
        array_x_y = rgb_xy(255,0,0)
        set_light_xy(array_x_y)
    if i == 6:
        print("Green")
        array_x_y = rgb_xy(255,0,0)
        set_light_xy(array_x_y)
    if i == 7:
        print("Blue")
        array_x_y = rgb_xy(255,0,0)
        set_light_xy(array_x_y)
    if i == 8:
        print("Colombian Colors Transition")
        colombian_colors_transition()
    if i == 9:
        print("USA Color Transition")
        usa_colors_transition()
    if i == 10:
        print("Random One Light Red")
        toRGB_random_one_light(255,0,0)
    if i == 11:
        print("Random One Light Green")
        toRGB_random_one_light(0,255,0)
    if i == 12:
        print("Random One Light Blue")
        toRGB_random_one_light(0,0,255)
    if i == 13:
        print("Random One Light")
        toRGB_random_color_one_light()
    if i == 14:
        print("Random One by one Light")
        toRGB_random_one_by_one_light()

def automatic_mode():
    if schedule_flag == True:
        automatic_option = random.randint(1, 14)
        print(" *******************************")
        print(" ************ Automatic Option: ",automatic_option)
        print(" *******************************")
        switch(automatic_option)
        main_window.after(automatic_mode_pause*1000, automatic_mode)
    else:
        print("Automatic Mode Off")

def start_automatic_mode():
    global schedule_flag
    schedule_flag = True
    automatic_mode()
    print("Starting Automatic Mode")

def stop_automatic_mode():
    global schedule_flag
    print("Automatic Mode Stopped")
    schedule_flag = False

pos_x_main_window=1000
pos_y_main_window=600

font_btn=("Arial Bold", 12)
font_title=("Arial Bold", 22)

#----------------------
# Active Configuration
#----------------------
online_btn = Button(main_window, text="Online", command=online, bg="light green")
online_btn.place(x=2, y=2)

offline_btn = Button(main_window, text="Offline", command=offline, bg="light blue")
offline_btn.place(x=50, y=2)

#----------------------
# Bright Configuration
#----------------------
lights_bright_value=IntVar()
lights_bright_value=200

lights_bright_lbl = Label(main_window, text="Bright")
lights_bright_lbl.place(x=750,y=90)

lights_bright_value = IntVar()
lights_bright = Scale(main_window, from_=0, to=254, orient=HORIZONTAL, variable=lights_bright_value, length=200)
lights_bright.place(x=750, y=120)
lights_bright.set(200)

bright_btn = Button(main_window, text="Change Bright", command=set_lights_config, font=font_btn)
bright_btn.place(x=750, y=180)

text_geometry=""+str(pos_x_main_window)+"x"+str(pos_y_main_window)
#print(text_geometry)

#----------------------
# Automatic window
#----------------------

#working on it...


#**************************
# Main Title
#**************************

main_window.geometry(text_geometry)
main_window.title("Monica's Bar"+version)
main_window.configure(bg="black")

#...pack(side=LEFT, expand=True, fill=BOTH, ipadx=10, ipady=4)

lbl_title = Label(main_window, text="Monica´s Bar pHue Lights App",font=font_title, bg="black", fg="white" )
lbl_title.place(x=300,y=2)

#**************************
# Fixed colors
#**************************

btn_red = Button(main_window, text="Red", bg="red", command=lambda : toRGB(255,0,0), font=font_btn, width=8)
btn_red.place(x=20,y=50)

btn_green = Button(main_window, text="Green", bg="green", command=lambda : toRGB(0,255,0), font=font_btn, width=8)
btn_green.place(x=120,y=50)

btn_blue = Button(main_window, text="Blue", bg="blue", command=lambda : toRGB(0,0,255), font=font_btn, width=8)
btn_blue.place(x=220,y=50)

btn_yellow = Button(main_window, text="Yellow", bg="yellow", command=lambda : toRGB(255,255,0), font=font_btn, width=8)
btn_yellow.place(x=320,y=50)

btn_white = Button(main_window, text="White", bg="white", command=lambda : toRGB(255,255,255), font=font_btn, width=8)
btn_white.place(x=420,y=50)

btn_white = Button(main_window, text="Purple", bg="purple", command=lambda : toRGB(127,0,255), font=font_btn, width=8)
btn_white.place(x=520,y=50)

btn_white = Button(main_window, text="Pink", bg="pink", command=lambda : toRGB(255,255,255), font=font_btn, width=8)
btn_white.place(x=620,y=50)

btn_light_green = Button(main_window, text="light Green", bg="light green", command=lambda : toRGB(62,254,56), font=font_btn, width=8)
btn_light_green.place(x=720,y=50)

#**************************
# Random colors
#**************************

btn_random = Button(main_window, text="Random Colors", command=start_random_color, font=font_btn, width=15)
btn_random.place(x=20,y=100)

stop_random_color_btn = Button(main_window, text="Stop Random Colors", bg="red", command=stop_random_color,
                               font=font_btn, width=20)

stop_random_color_btn.place(x=200,y=100)

#**************************
# Flags transitions
#**************************

btn_colombian_colors = Button(main_window, text="Colombian Colors", bg="light green",
                           command=colombian_colors_transition, font=font_btn, width=15)
btn_colombian_colors.place(x=20,y=150)

btn_usa_colors = Button(main_window, text="USA Colors", bg="light blue",
                           command=usa_colors_transition, font=font_btn, width=15)
btn_usa_colors.place(x=20,y=200)

#**************************
# Transitions
#**************************

btn_color_transition_yellow_violet_blue = Button(main_window, text="Yellow - violet - blue", bg="light yellow",
                           command=dark_colors_transition_yellow_violet_blue, font=font_btn, width=15)
btn_color_transition_yellow_violet_blue.place(x=200,y=200)

btn_color_transition_blue = Button(main_window, text="Dark Blue - Light blue", bg="light blue",
                           command=dark_colors_transition_blue, font=font_btn, width=15)
btn_color_transition_blue.place(x=350,y=200)

btn_color_transition_yellow_green = Button(main_window, text="Yellow - Green", bg="light green",
                           command=dark_colors_transition_yellow_green, font=font_btn, width=15)
btn_color_transition_yellow_green.place(x=500,y=200)

#**************************
# Choose color
#**************************

btn_choose_color = Button(main_window, text="Choose Color", bg="white",
                          command=choosed_color_light, font=font_btn, width=15)
btn_choose_color.place(x=20,y=250)

#**************************
# one light
#**************************

btn_one_light_random_red = Button(main_window, text="Random One light red", bg="Red",
                                  command= lambda: toRGB_random_one_light(255,0,0), font=font_btn, width=20)
btn_one_light_random_red.place(x=20,y=300)

btn_one_light_random_green = Button(main_window, text="Random One light green", bg="Green",
                                    command= lambda: toRGB_random_one_light(0,255,0), font=font_btn, width=20)
btn_one_light_random_green.place(x=220,y=300)

btn_one_light_random_blue = Button(main_window, text="Random One light blue", bg="Blue",
                                   command= lambda: toRGB_random_one_light(0,0,255), font=font_btn, width=20)
btn_one_light_random_blue.place(x=420,y=300)

btn_one_light_random_color = Button(main_window, text="Random One light color", bg="violet",
                                   command= lambda: toRGB_random_color_one_light(), font=font_btn, width=20)
btn_one_light_random_color.place(x=620,y=300)

btn_one_by_one_light_random_color = Button(main_window, text="Random One by One light color", bg="RoyalBlue3",
                                   command= lambda: toRGB_random_one_by_one_light(), font=font_btn, width=20)
btn_one_by_one_light_random_color.place(x=20,y=350)

#**************************
# Automatic mode
#**************************


btn_automatic_mode = Button(main_window, text="Automatic", bg="light yellow",
                            command=start_automatic_mode, font=font_btn, width=15)
btn_automatic_mode.place(x=20,y=450)

btn_stop_automatic_mode = Button(main_window, text="Stop Automatic", bg="red",
                                 command=stop_automatic_mode, font=font_btn, width=15)
btn_stop_automatic_mode.place(x=180,y=450)


main_window.mainloop()