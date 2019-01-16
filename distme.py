from tkinter import *
import random


class Startupwindow:
# Creates the total card var for the game 
    player_cards = 8
    opp_cards = 8

    def __init__(self,master):
        #create the home page
        self.master = master
        self.title = self.master.title("Storage Trumps")
        self.background = self.master.configure(background="dark blue")
        self.maintitle = Label(self.master, text="Storage Trump", bg="dark blue", fg="white", font="none 30 bold").pack()
        self.picturefile = PhotoImage(file="Storage Trump\\Capture.GIF")
        Label(self.master, image= self.picturefile , bg = "blue").pack()
        Label(self.master, text =" Player 1 : Enter your name", bg="dark blue", fg="white",font ="none 16 bold").pack()
        self.textbox = Entry(self.master, width= 45, bg="white")
        self.textbox.pack()
        button = Button(self.master, text="START", command = lambda : self.gamewindow(master))
        button.pack()


    def gamewindow(self,master):
        # updates the card total 
        player_score  = Startupwindow.player_cards
        computer_score = Startupwindow.opp_cards

        # creates a new window if the card totals are not 0 
        if player_score > 0:
            if computer_score > 0:

                master.withdraw()
                self.newwindow = Toplevel(self.master)
                self.newwindow.geometry("1500x800")
                background = self.newwindow.configure(background="dark blue")
                maintitle = Label(self.newwindow, text="Storage Trump", bg="dark blue", fg="white",font="none 30 bold").grid(row =0 , columnspan =8)
                self.instructions = "Players choose which item they think will beat their opponents card. Whoever has the best value wins then goes again. Drawn values are carried over to the next go. The game ends when one player has all the cards."
                label_instructions = Label(self.newwindow, text= self.instructions,bg = "dark blue", fg="white", font ="none 12 ").grid(row =1 , columnspan = 8 )
                player_info = Label(self.newwindow, text=self.textbox.get() +" / Cards = " + str(Startupwindow.player_cards) , bg="dark blue", fg="white", font="none 16 bold").grid(row=2, column = 0)
                opp_info = Label(self.newwindow, text= "Computer / Cards = "+ str(Startupwindow.opp_cards), bg="dark blue", fg="white", font="none 16 bold").grid(row =2 , column =7 )

                player_number = self.pick_card()
                opp_number = self.opp_pick_card()

                while player_number == opp_number :
                    player_number = self.pick_card()
                    opp_number = self.opp_pick_card()

                player_devicepath = Charactertics.device_list[player_number].path
                opp_devicepath = Charactertics.device_list[opp_number].path
                self.picturefile2 = PhotoImage(file=player_devicepath)
                self.picturefile3 = PhotoImage(file=opp_devicepath)
                player_Image = Label(self.newwindow, image=self.picturefile2).grid(row = 3, column =0)
                opp_Image = Label(self.newwindow, image=self.picturefile3).grid(row = 3, column =7)
                capacity = Button(self.newwindow, text= "Capacity", command= lambda : self.pick_capacity(player_number,opp_number)).grid(row = 3, column=2)
                speed = Button(self.newwindow,text="Speed", command = lambda : self.pick_speed(player_number,opp_number)).grid(row = 3,column=3)
                portability = Button(self.newwindow,text="Portability", command = lambda : self.pick_portability(player_number,opp_number)).grid(row = 3,column=4)
                reliability = Button(self.newwindow,text="Reliability", command = lambda : self.pick_reliability(player_number,opp_number)).grid(row = 3,column=5)
                price = Button(self.newwindow,text="Price", command = lambda : self.pick_price(player_number,opp_number)).grid(row = 3,column=6)

    # Depends who wins the game 
        if int(computer_score) == 0 :
            message_title = " You have won the game"
            messge = " Press Okay to quit the game"
            self.end_pop_up(message_title, messge)

        elif int(player_score) == 0 :
            message_title = " You have lost the game"
            messge = " Press Okay to quit the game"
            self.end_pop_up(message_title, messge)




    def pick_card(self):
        # picks a random device from the device list in class Characterisitic for player
        maxrange = len(Charactertics.device_list) - 1
        number =random.randint(0,maxrange)
        return number

    def opp_pick_card(self):
        # picks a random device from the device list in class Characterisitic for Computer
        maxrange = len(Charactertics.device_list) - 1
        number = random.randint(0, maxrange)
        return number

    def pick_capacity(self,player_card,opp_card):
        # comapares the two capacity spec and changes the card total 
        self.full_player_info = Charactertics.device_list[player_card].capacity
        self.full_opp_info = Charactertics.device_list[opp_card].capacity
        player_info = [ parts for parts in self.full_player_info.split() ]
        opp_info = [ parts for parts in self.full_opp_info.split()]
        self.player_capacity_number = int(player_info[0])
        self.computer_capacity_number = int(opp_info[0])


        if player_info[1] == "TB" and opp_info[1] == "GB"  or opp_info[1] == "MB"  or opp_info[1] == "KB":
            message_title = "Player 1 wins"
            message =  "Player 1 wins" + "\n" + "Capacity" +"\n"+ Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_info
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif player_info[1] == "GB" and opp_info[1] == "MB"  or opp_info[1] == "KB":
            message_title = "Player 1 wins"
            message = "Player 1 wins" + "\n" + "Capacity" +"\n"+  Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_info
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif player_info[1] == "MB" and  opp_info[1] == "KB":
            message_title = "Player 1 wins"
            message = "Player 1 wins" + "\n" + "Capacity" +"\n"+  Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_info
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif player_info[1] == opp_info[1]:

            if self.player_capacity_number > self.computer_capacity_number :
                message_title = "Player 1 wins"
                message = "Player 1 wins" + "\n" + "Capacity" +"\n"+  Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " +  self.full_opp_info
                Startupwindow.player_cards += 1
                Startupwindow.opp_cards -= 1

            elif self.player_capacity_number == self.computer_capacity_number :
                message_title = "Draw"
                message = "Draw" + "\n" + "Capacity" +"\n"+ Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " +  self.full_opp_info

            elif self.player_capacity_number < self.computer_capacity_number :
                message_title = "Computer Wins"
                message = "Computer wins" + "\n" + "Capacity" +"\n"+ Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_info
                Startupwindow.player_cards -= 1
                Startupwindow.opp_cards += 1

            else :
                message_title = "Error"
                message = "There has been an error"

        else :
            message_title = "Computer Wins77"
            message = "Computer wins" + "\n" + "Capacity" +"\n"+ Charactertics.device_list[player_card].name + " : " + self.full_player_info + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_info
            Startupwindow.player_cards -= 1
            Startupwindow.opp_cards += 1

        self.pop_up(message_title,message)

    def pick_speed(self,player_card,opp_card):
        # comapares the two speed spec and changes the card total 
        self.full_player_speed = Charactertics.device_list[player_card].speed
        self.full_opp_speed = Charactertics.device_list[opp_card].speed
        player_info = [parts for parts in self.full_player_speed.split()]
        opp_info = [parts for parts in self.full_opp_speed.split()]
        player_speed = int(player_info[0])
        computer_speed = int(opp_info[0])

        if player_info[1] == "MB" and opp_info[1] == "KB":
            message_title = "Player 1 wins"
            message =  "Player 1 wins" + "\n" + "Speed" +"\n"+  Charactertics.device_list[player_card].name + " : " + self.full_player_speed + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_speed
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif player_info[1]  == opp_info[1] :

            if player_speed > computer_speed :
                message_title = "Player 1 wins"
                message = "Player 1 wins" + "\n" + "Speed" +"\n"+ Charactertics.device_list[player_card].name + " : " + self.full_player_speed + "\n " + Charactertics.device_list[opp_card].name + " : " +  self.full_opp_speed
                Startupwindow.player_cards += 1
                Startupwindow.opp_cards -= 1

            elif player_speed == computer_speed :
                message_title = "Draw"
                message = "Draw" + "\n" + "Speed" +"\n"+Charactertics.device_list[player_card].name + " : " + self.full_player_speed + "\n " + Charactertics.device_list[opp_card].name + " : " +  self.full_opp_speed

            elif player_speed < computer_speed:
                message_title = "Computer Wins"
                message = "Computer wins" + "\n" + "Speed" +"\n"+Charactertics.device_list[player_card].name + " : " + self.full_player_speed + "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_speed
                Startupwindow.player_cards -= 1
                Startupwindow.opp_cards += 1

            else :
                message_title = "Error"
                message = "There has been an error"

        else :
            message_title = "Computer Wins"
            message = "Computer wins" + "\n" + "Speed" +"\n"+Charactertics.device_list[player_card].name + " : " + self.full_player_speed+ "\n " + Charactertics.device_list[opp_card].name + " : " + self.full_opp_speed
            Startupwindow.player_cards -= 1
            Startupwindow.opp_cards += 1

        self.pop_up(message_title,message)

    def pick_portability(self,player_card,opp_card):

        # comapares the two portability spec and changes the card total 
        self.full_player_port = Charactertics.device_list[player_card].portability
        self.full_opp_port = Charactertics.device_list[opp_card].portability
        self.full_player_port = int(self.full_player_port)
        self.full_opp_port = int(self.full_opp_port )

        if self.full_player_port > self.full_opp_port:
            message_title = "Player 1 wins"
            message = "Player 1 wins" + "\n" + "Portability" +"\n"+Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_port) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_port)
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif self.full_player_port == self.full_opp_port:
            message_title = "Draw"
            message = "Draw" + "\n" + "Portability" +"\n"+Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_port) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_port)

        elif self.full_player_port < self.full_opp_port:
            message_title = "Computer Wins"
            message = "Computer wins" + "\n" + "Portability" +"\n"+ Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_port) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_port)
            Startupwindow.player_cards -= 1
            Startupwindow.opp_cards += 1

        else:
            message_title = "Error"
            message = "There has been an error"

        self.pop_up(message_title, message)


    def pick_reliability(self,player_card,opp_card):
        # comapares the two reliability spec and changes the card total 
        self.full_player_rel= Charactertics.device_list[player_card].reliability
        self.full_opp_rel = Charactertics.device_list[opp_card].reliability


        if int(self.full_player_rel) > int(self.full_opp_rel):
            message_title = "Player 1 wins"
            message = "Player 1 wins" + "\n" + "Reliability" +"\n"+ Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_rel) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_rel)
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif int(self.full_player_rel) == int(self.full_opp_rel):
            message_title = "Draw"
            message = "Draw" + "\n" + "Reliability" +"\n"+  Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_rel) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_rel)

        elif int(self.full_player_rel) < int(self.full_opp_rel):
            message_title = "Computer Wins"
            message = "Computer wins" + "\n" + "Reliability" +"\n"+ Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_rel) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_rel)
            Startupwindow.player_cards -= 1
            Startupwindow.opp_cards += 1

        else:
            message_title = "Error"
            message = "There has been an error"

        self.pop_up(message_title, message)

    def pick_price(self,player_card,opp_card):
        # comapares the two price spec and changes the card total 
        self.full_player_price = Charactertics.device_list[player_card].price
        self.full_opp_price = Charactertics.device_list[opp_card].price

        if float(self.full_player_price) < float(self.full_opp_price):
            message_title = "Player 1 wins"
            message = "Player 1 wins" + "\n" + "Price" +"\n"+  Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_price) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_price)
            Startupwindow.player_cards += 1
            Startupwindow.opp_cards -= 1

        elif float(self.full_player_price) == float(self.full_opp_price):
            message_title = "Draw"
            message = "Draw" + "\n" + "Price" +"\n"+   Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_price) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_price)

        elif float(self.full_player_price) > float(self.full_opp_price):
            message_title = "Computer Wins"
            message = "Computer wins" + "\n" + "Price" +"\n"+   Charactertics.device_list[
                player_card].name + " : " + str(self.full_player_price) + "\n " + Charactertics.device_list[
                          opp_card].name + " : " + str(self.full_opp_price)
            Startupwindow.player_cards -= 1
            Startupwindow.opp_cards += 1

        self.pop_up(message_title, message)

    def pop_up(self,message_title,message):
        # This is the pop up message that happens when the comparison is completed 
        self.popup = Tk()
        self.popup.wm_title(message_title)
        label = Label(self.popup, text=message, font=" None 16 bold")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(self.popup, text="Okay", command= self.destory_popup)
        B1.pack()

    def end_pop_up(self, message_title, message):
        # This is the pop up message that happens when one of the total cards are 0 
        self.popup = Tk()
        self.popup.wm_title(message_title)
        label = Label(self.popup, text=message, font=" None 16 bold")
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(self.popup, text="Okay", command=self.popup_quit)
        B1.pack()

    def popup_quit(self):
        # This quits the games once the end pop up message's button is clicked 
        quit()

    def destory_popup(self):
        # This destroys the pop up box, removes the old window and then goes back to the game window 
        self.popup.destroy()
        self.newwindow.withdraw()
        self.gamewindow(self.master)


class Charactertics:

    device_list = []
#ASSIGNING THE CHARACTERS OF THE STORAGE DEVICES
    def __init__(self,name,capacity,speed,portability,reliability, price , path):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.portability = portability
        self.reliability = reliability
        self.price = price
        self.path = path
        Charactertics.device_list.append(self)




# CREATING STORAGE DEVICES

scanDisk = Charactertics("Memory Card","64 GB","30 MB",5,3,0.54,"Storage Trump\\memorycard.gif")
internalHD = Charactertics("Internal Hard Drive","3 TB","120 MB",1,4.5,0.03,"Storage Trump\\internalharddrive.gif")
CD = Charactertics("CD","700 MB","1200 KB",4,2,0.14,"Storage Trump\\cd.gif")
flash = Charactertics("USB","256 GB","1200 KB",5,4,0.93,"Storage Trump\\flash.gif")
DVD = Charactertics("DVD","9 GB","33 MB",4,2,0.25,"Storage Trump\\dvd.gif")
solidstate =Charactertics("Solid State Drive","750 GB","520 MB",1,4.5,0.99,"Storage Trump\\solidstate.gif")
blueRay = Charactertics("Blu-Ray","50 GB","72 MB",4,2,1.02,"Storage Trump\\Blue-ray.gif")

# Starts the GUI 
root = Tk()
mainpage = Startupwindow(root)
root.mainloop()
