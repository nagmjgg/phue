

'''
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



'''
from phue import *
from phue import Bridge
import time
import random
from tkinter import *
from tkinter import colorchooser
import tkinter as tk
import threading


main_window = Tk()




class ButtonNotPressedException(Exception):
    """
    Tried to `create_new_user` without pressing the button on the Hue Bridge
    """
    msg = "Link button was not pressed"

bridge_stairs = "192.168.4.30"
bridge_stairs_user = "VWvVRF49nXW6YfkqfFDT3hIE6seCQTTB5HvcoKKu"
bridge_center = "192.168.4.36"
bridge_center_user = "CpFcYyysWmNClDpIgEayDru1JdF4iHvYwkFiNKbj"
bridge_entrance = "192.168.4.35"
bridge_entrance_user = "KAImBShLUywht8EcB6DKjk5IuqwLmNrUWliULlZt"

active = 0

if active == 1:
    b = Bridge(bridge_stairs, bridge_stairs_user)
    b.connect()

    c = Bridge(bridge_center, bridge_center_user)
    c.connect()

    d = Bridge(bridge_entrance, bridge_entrance_user)
    d.connect()

    b.get_api()
    c.get_api()
    d.get_api()



    # Set brightness of lamp 1 to max
    '''
    for i in range(1,4):
        b.set_light(i, 'on', True)
    '''
    b.set_light([1,2,3,4], 'on', True)
    c.set_light([1,2,3,4], 'on', True)
    d.set_light([1,2,3,4], 'on', True)

def color_green_all():
    color=25000
    b.set_light([1,2,3,4], 'hue', color)
    c.set_light([1,2,3,4], 'hue', color)
    d.set_light([1,2,3,4], 'hue', color)

def color_red_all():
    color = 65000
    b.set_light([1,2,3,4], 'hue', color)
    c.set_light([1,2,3,4], 'hue', color)
    d.set_light([1,2,3,4], 'hue', color)

def color_yellow_all():
    color = 100
    b.set_light([1,2,3,4], 'hue', color)
    c.set_light([1,2,3,4], 'hue', color)
    d.set_light([1,2,3,4], 'hue', color)

def color_all(color=25000):
    b.set_light([1, 2, 3, 4], 'hue', color)
    c.set_light([1, 2, 3, 4], 'hue', color)
    d.set_light([1, 2, 3, 4], 'hue', color)

random_flag = 1
def random_color(initial=25000,final=60000,pause_time=2,times=10):
    def run_random():
        while (random_flag == 1):
            print("Random flag_active")
            light_color = int(random.randint(initial, final))
            event = threading.Event()
            event.wait(pause_time)
            color_all(light_color)
            print(light_color)
            if random_flag == 0:
                break

    thread = threading.Thread(target=run_random)
    print("thread ok")
    thread.start()

def toRGB(Red,Green,Blue):
    X = 0.4124*Red + 0.3576*Green + 0.1805*Blue # Stack Overflow code
    Y = 0.2126*Red + 0.7152*Green + 0.0722*Blue
    Z = 0.0193*Red + 0.1192*Green + 0.9505*Blue

    xx = X / (X + Y + Z)
    yy = Y / (X + Y + Z)

    print(xx,yy)


    b.set_light([1,2,3,4], 'xy', [xx,yy])
    c.set_light([1,2,3,4], 'xy', [xx,yy])
    d.set_light([1,2,3,4], 'xy', [xx,yy])

def toRGB_random_one_light(Red,Green,Blue):
    X = 0.4124*Red + 0.3576*Green + 0.1805*Blue # Stack Overflow code
    Y = 0.2126*Red + 0.7152*Green + 0.0722*Blue
    Z = 0.0193*Red + 0.1192*Green + 0.9505*Blue

    xx = X / (X + Y + Z)
    yy = Y / (X + Y + Z)

    print(xx,yy)
    b.set_light([1, 2, 3, 4], 'bri', random.randint(50,256))
    c.set_light([1, 2, 3, 4], 'bri', random.randint(50,256))
    d.set_light([1, 2, 3, 4], 'bri', random.randint(50,256))
    b.set_light([random.randint(1,5)], 'xy', [xx,yy])
    c.set_light([random.randint(1,5)], 'xy', [xx,yy])
    d.set_light([random.randint(1,5)], 'xy', [xx,yy])



def random_one_light():
    random_flag_one_light = 1

    def random_color(initial=25000, final=60000, pause_time=2, times=10):
        def run_random():
            while (random_flag_one_light == 1):
                event = threading.Event()
                event.wait(pause_time)


                if random_flag == 0:
                    break

        thread = threading.Thread(target=run_random)
        print("thread ok")
        thread.start()

def rgb_colors():

    red = (255,0,0)
    green = (0,255,0)
    blue = (0,0,255)  #38673
    purple = (127,0,255)
    pink = (255,0,255)
    yellow = (255,255,0)


def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb





def colombian_colors_transition():
    #pastel_colors = ((200,0,205),(0,0,226),(255,228,225),(255,182,174),(255,244,225))

    colombian_colors = ((255,255,0),(0,0,255),(255,0,0))

    for times in range(10):
        for i in colombian_colors:
            print(i)
            pause_time = 2

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            print(rx, gx, bx)

            toRGB(rx,gx,bx)


            time.sleep(1)
            #event = threading.Event()
            #event.wait(pause_time)

def usa_colors_transition():
    #pastel_colors = ((200,0,205),(0,0,226),(255,228,225),(255,182,174),(255,244,225))

    usa_colors = ((255,255,255),(255,0,0),(0,0,255))

    for times in range(10):
        for i in usa_colors:
            print(i)
            pause_time = 2

            rx = int(i[0])
            gx = int(i[1])
            bx = int(i[2])

            print(rx, gx, bx)

            toRGB(rx,gx,bx)


            time.sleep(1)
            #event = threading.Event()
            #event.wait(pause_time)

#Convertion to RGB works fine ... bg=_from_rgb((0, 10, 255))
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline=_from_rgb((0,255,0)),
            fill=_from_rgb((255,0,0)), width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60,
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0,
            extent=210, outline="#f11", fill="#1f1", width=2)

        points = [150, 100, 200, 120, 240, 180, 210,
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='#f11',
            fill='#1f1', width=2)

        canvas.pack(fill=BOTH, expand=1)



# Function that will be invoked when the
# button will be clicked in the main window
def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose color")
    print(color_code)
    rcolor = color_code[0][0]
    gcolor = color_code[0][1]
    bcolor = color_code[0][2]
    print(rcolor,gcolor,bcolor)
    colors = (rcolor, gcolor, bcolor)
    return colors

def choosed_color_light():
    color=choose_color()
    toRGB(color[0], color[1], color[2])

pos_x_main_window=1000
pos_y_main_window=700

text_geometry=""+str(pos_x_main_window)+"x"+str(pos_y_main_window)
print(text_geometry)

main_window.geometry(text_geometry)
main_window.title("Monica's Bar")
main_window.configure(bg="black")

font_btn=("Arial Bold", 12)
font_title=("Arial Bold", 22)

#...pack(side=LEFT, expand=True, fill=BOTH, ipadx=10, ipady=4)

lbl_title = Label(main_window, text="Monica´s Bar pHue Lights App",font=font_title, bg="black", fg="white" )
lbl_title.place(x=300,y=2)

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

btn_random = Button(main_window, text="Random", command=random_color, font=font_btn, width=8)
btn_random.place(x=20,y=100)

random_flag_btn = Checkbutton(main_window, text="random active", variable=random_flag, onvalue=1, offvalue=0)
random_flag_btn.place(x=103,y=100)
print(random_flag)

btn_colombian_colors = Button(main_window, text="Colombian Colors", bg="light green",
                           command=colombian_colors_transition, font=font_btn, width=15)
btn_colombian_colors.place(x=20,y=150)

btn_usa_colors = Button(main_window, text="USA Colors", bg="light blue",
                           command=usa_colors_transition, font=font_btn, width=15)
btn_usa_colors.place(x=20,y=200)


btn_choose_color = Button(main_window, text="Choose Color", bg="white", command=choosed_color_light, font=font_btn, width=15)
btn_choose_color.place(x=20,y=250)

btn_one_light_random_red = Button(main_window, text="Random Color One light", bg="Red", command= lambda: toRGB_random_one_light(255,0,0), font=font_btn, width=20)
btn_one_light_random_red.place(x=20,y=300)

btn_one_light_random_green = Button(main_window, text="Random Color One light", bg="Green", command= lambda: toRGB_random_one_light(0,255,0), font=font_btn, width=20)
btn_one_light_random_green.place(x=220,y=300)

btn_one_light_random_blue = Button(main_window, text="Random Color One light", bg="Blue", command= lambda: toRGB_random_one_light(0,0,255), font=font_btn, width=20)
btn_one_light_random_blue.place(x=420,y=300)

lbl_preselected_colors = Label(main_window, text="Preselected Colors", font=font_btn)
lbl_preselected_colors.place(x=20, y = 360)

xx=20
yy=400
for i in range(0,256,51):
    for j in range(0, 256, 51):
        for k in range(0, 256, 51):
            button = tk.Button(main_window, text="   ", bg=_from_rgb((k,j,i)), command= lambda : toRGB(k,j,i))
            print("i",i,"j:",j,"k:",k)
            if xx > 900:
                xx = 20
                yy += 50
                button.place(x=xx,y=yy)

            else:
                xx += 20
                button.place(x=xx, y=yy)



#color_green_all()
#random_color(0,65
# 000,5,50)
#bg=_from_rgb((0, 10, 255)))
#ex = Example()


#Canvas *****************************************


'''
canvas = Canvas()
for i in range(2):
    random_a = random.randint(0,255)
    random_b = random.randint(0, 255)
    random_c = random.randint(0, 255)

    canvas.create_oval(20, 300, 60, 340, outline=_from_rgb((255,255,255)),
                       fill=_from_rgb((random_a,random_b,random_c)), width=2)
    print("luz 1 a:",random_a," b:",random_b, "c: ",random_c)


    canvas.create_oval(70, 300, 110, 340, outline=_from_rgb((255, 255, 255)),
                     fill=_from_rgb((random_a, random_b, random_c)), width=2)
    print("luz 2 a:", random_a, " b:", random_b, "c: ", random_c)

    canvas.pack()

    canvas.update()

    event = threading.Event()
    event.wait(1)
'''




#color_z = tk.colorchooser()

main_window.mainloop()