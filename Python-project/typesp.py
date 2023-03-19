# module used to design the terminal interface
import curses
import time
import random

# allows to make changes on terminal and restores back to original state
from curses import wrapper

# function to prompt user to start typing
def std_screen(stdscr):

    stdscr.clear()
    stdscr.addstr("Welcome to the terminal interface")
    stdscr.addstr("\nPress any key to continue")
    stdscr.refresh()
    stdscr.getkey()

#function to overwrite the default text by the text typed by the user
def overwrite(stdscr,current_text,target_text,words=0):
   stdscr.addstr(target_text)
   stdscr.addstr(1,0,"words: "+ str(words))

   #enumerate returns the index and the char at that index.so the char is overwritten at the index position i
   for i,c in enumerate(current_text):
      
      #check if the char typed by the user is same as the char at the index position i in the target text.if so its correct denoting green else its wrong denoting red
      correct=target_text[i]
      if c != correct:
        stdscr.addstr(0,i,c,curses.color_pair(1))
      else:
        stdscr.addstr(0,i,c,curses.color_pair(3))

def random_text():
    # this function is used to generate random text to type from txt file
    with open("text.txt") as file:
        text=file.readlines() # returns a list of lines in the file
        return random.choice(text).strip() # returns a random line from the list .strip is used to remove \n from the line present in txt file




def wpm(stdscr):
    # prints the default text to type on screen
    target_text=random_text()
    current_text=[]
    words=0
    # stores the epoch time .the time user has started tying text
    start_time=time.time()

    #this function is used to make the getkey() non blocking. so that the program doesnt wait for the user to press a key.
    stdscr.nodelay(True)

    #this function is used to get the text typed by the user, append it to curtext and then print it on screen
    while True:
      
      #denotes time elapsed till now
      time_taken=max(time.time()-start_time,1)

      #calculates the words per minute.by considering charcters per minute and then dividing by 5 to get words per minute
      words= round((len(current_text)/ (time_taken / 60)/ 5))
     
      #clr scr is imp here bcos to avoid the previous line text to be printed again
      stdscr.clear()

      overwrite(stdscr,current_text,target_text,words)

      #stdscr.addstr(target_text)

    #   for c in current_text:
    #     stdscr.addstr(c,curses.color_pair(1))

      stdscr.refresh()

      if "".join(current_text) == target_text: # join is used to join the list of chars to a string
         stdscr.nodelay(False) # now user needs to enter key to continue further so nodelay is set to false and the program waits for the user to press a key
         break

      # try n except r used in order to avoid the program to crash if the user doesnt press any key bcos of nodelay() fnc.this 
      # is done in order to decrease the wpm of the user if he doesnt type anything 
      try:
       key = stdscr.getkey()
      except:
       continue

      #checks if the key pressed is escape key. which has ascii value 27
      if ord(key) == 27:
        break
      
      #the 3 terms in the tupe r diff possibilities of representing backspace in os. if the char is backspace, then pop the last char from the list
      if key in ('KEY_BACKSPACE','\b',"\x7f"):
        if len(current_text) > 0:
          current_text.pop()

      #this condition to check the size of current text doesnt exceed target text size so that list index out of range error is avoided
      elif len(current_text)<len(target_text):
          # add the char to the list if not a backspace
          current_text.append(key)

# stdscr is the screen object which allows to type on screen by opening a window
def main(stdscr):

    #the id=1, 1st color is the foreground and the 2nd color is the background
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    std_screen(stdscr)

    # continue to play again until user presses escape key
    while True:
     
     wpm(stdscr)
     stdscr.addstr(2,0,"You have completed the typing test..press any key to continue")
     key=stdscr.getkey() # to get key from user to continue

     if ord(key)==27: # if escape key is pressed then break
        break


wrapper(main)


    

