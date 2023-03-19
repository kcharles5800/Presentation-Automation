from time import sleep

import pyautogui as gui
import pyperclip


class create_ppt:

# Function to automate the creation of the presentation using microsoft powerpoint in a windows machine

    def make(lyrics):

        # a greeting and a warning message
        sleep(2)
        print('initiating second phase...')

        # variables to make my work easy

        slides_count = int(len(lyrics[1])/2)
        directory_path = r"" # the directory where you wanna save the presentation

        # opening the powerpoint software

        gui.hotkey('win','r')
        gui.write('powerpnt')
        gui.press('enter')
        sleep(2)

        # creating a new pptx file

        gui.hotkey('ctrl','n')
        sleep(2)
        gui.press('tab')
        # gui.press('tab')
        # gui.press('tab')
        # gui.write('Damask',0.04)
        # gui.sleep(1)
        # gui.press('right')
        gui.press('right')
        sleep(1)
        gui.press('enter')
        gui.sleep(3)
        gui.press('enter',2)
        sleep(2)

        # changing the size of the textboxes

        # gui.click(1167,359)
        # sleep(1)
        gui.click(1097,358)
        gui.drag(0,-115,0.4,button='right')
        sleep(0.5)
        gui.click(1580,435)
        gui.drag(174,0,0.4,button='right')
        sleep(0.5)
        gui.click(612,435)
        gui.drag(-174,0,0.4,button='right')
        sleep(0.5)
        gui.click(1096,616)
        gui.drag(0,-70,0.4,button='right')
        sleep(0.5)

        gui.click(1097,801)
        sleep(0.5)

        gui.click(1097,801)
        gui.drag(0,150,0.4,button='right')
        sleep(0.5)
        gui.click(1582,778)
        gui.drag(170,0,0.4,button='right')
        sleep(0.5)
        gui.click(612,782)
        gui.drag(-170,0,0.4,button='right')
        sleep(0.5)

        gui.click(1090,458)
        gui.hotkey('ctrl','shift',',')
        gui.hotkey('ctrl','shift',',')

        gui.click(972,126)
        gui.press('down',2)
        gui.press('enter')


        # formatting the english liness
        
        gui.click(1101,690)
        gui.hotkey('ctrl','shift','.')
        gui.hotkey('ctrl','shift','.')
        gui.hotkey('ctrl','shift','.')
        gui.hotkey('ctrl','shift','.')

        gui.hotkey('ctrl','a')
        sleep(0.5)
        gui.hotkey('ctrl','b')
        gui.click(521,126)
        gui.write('Baskerville')
        gui.press('enter')

        # generating the required number of slides

        gui.click(120,294) 
        gui.hotkey('ctrl','c')

        for i in range(slides_count-1) :
            gui.hotkey('ctrl','v')

        sleep(1)
        gui.press('up',slides_count-1)

        # entering the lyrics in the textboxes and formatting it 

        for i in range(0,len(lyrics[1]),2) :
            gui.click(1090,458)
            sleep(0.5)
            pyperclip.copy(lyrics[0][i])
            # sleep(1)
            gui.hotkey('ctrl','v')
            gui.press('end')
            gui.press('enter')
            pyperclip.copy(lyrics[0][i+1])
            # sleep(1)
            gui.hotkey('ctrl','v')
            if lyrics[0][i+1] == '' :
                gui.press('backspace')
            sleep(0.5)
            gui.click(1101,690)
            sleep(0.5)
            gui.write(lyrics[1][i])
            sleep(0.5)
            gui.press('end')
            gui.press('enter')
            gui.write(lyrics[1][i+1])
            if lyrics[1][i+1] == '' :
                gui.press('backspace')
            sleep(0.5)


            gui.hotkey('ctrl','a')
            gui.click(628,162)
            gui.press('down',3)
            gui.press('enter')

            gui.press('esc',2)
            gui.press('down')

        # name the ppt and save the ppt in the required directory 

        gui.hotkey('ctrl','s')

        sleep(0.5)  
        gui.press('tab',4)
        gui.press('enter')
        sleep(0.5)
        gui.press('tab') 
        gui.press('down',4)
        gui.press('enter')
        sleep(0.5)
        gui.press('backspace')
        gui.write(lyrics[1][0])
        gui.click(564,69)
        gui.write(directory_path,0.02)
        sleep(0.5)
        gui.press('enter')
        for i in range (5):
            gui.hotkey('shift','tab')

        gui.press('enter')
        sleep(1)

        # minimize the powerpoint and give a message

        gui.click(1780,18)
        sleep(0.5)

        print('The required presentation is ready.')