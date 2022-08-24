import tkinter as tk
from tkinter import *
from turtle import width
from PIL import Image, ImageTk
import random

def mainTab():
    global root
    root = Tk()
    root.title("Algorithm Vizualiser")

    wdt = 700
    hit = 400
    app_wdt = root.winfo_screenwidth()
    app_hit = root.winfo_screenheight()

    x = (app_wdt/2) - (wdt/2)
    y = (app_hit/2) - (hit/2)
    root.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
    root.resizable(0,0)
    root.config(bg="#A172FF")



    def Sorting():
        mainTabLabel.destroy()
        SortingButton.destroy()
        #PathfindingButton.destroy()
        root.destroy()
        ##########################################

        


        ##### M E T H O D S #####


        def Back():
            root_Sorting.destroy()
            mainTab()
            


        def swap(pos_0, pos_1):
            columnI1, _, columnI2, _ = work_space.coords(pos_0)
            columnII1, _, columnII2, _ = work_space.coords(pos_1)
            work_space.move(pos_0, columnII1-columnI1, 0)
            work_space.move(pos_1, columnI2-columnII2, 0)


        temp = None

        #Insertion Sort
        def _insertion_sort():
            global columnList
            global lengthList

            for i in range(len(lengthList)):
                cursor = lengthList[i]
                cursorBar = columnList[i]
                position = i

                while position > 0 and lengthList[position - 1] > cursor:
                    lengthList[position] = lengthList[position - 1]
                    columnList[position], columnList[position - 1] = columnList[position - 1], columnList[position]
                    swap(columnList[position], columnList[position - 1])
                    yield
                    position -= 1

                lengthList[position] = cursor
                columnList[position] = cursorBar
                swap(columnList[position], cursorBar)

            
        #Bubble Sort
        def _bubble_sort():
            global columnList
            global lengthList

            for i in range(len(lengthList) - 1):
                for j in range(len(lengthList) - i - 1):
                    if(lengthList[j] > lengthList[j + 1]):
                        lengthList[j], lengthList[j + 1] = lengthList[j + 1], lengthList[j]
                        columnList[j], columnList[j + 1] = columnList[j + 1], columnList[j]
                        swap(columnList[j + 1], columnList[j])
                        yield


        #Selection Sort            
        def _selection_sort():
            global columnList    
            global lengthList

            for i in range(len(lengthList)):
                min = i
                for j in range(i + 1 ,len(lengthList)):
                    if(lengthList[j] < lengthList[min]):
                        min = j
                lengthList[min], lengthList[i] = lengthList[i] ,lengthList[min]
                columnList[min] , columnList[i] = columnList[i] , columnList[min]
                swap(columnList[min] , columnList[i])        
                yield



        #Triggering Fuctions

        def insertion_sort():     
            global temp
            temp = _insertion_sort()
            animate()

        def selection_sort():     
            global temp
            temp = _selection_sort()
            animate()

        def bubble_sort():     
            global temp
            temp = _bubble_sort()
            animate()  


        #Animation Function
        def animate():      
            global temp
            if temp is not None:
                try:
                    next(temp)
                    root_Sorting.after(10, animate)    
                except StopIteration:            
                    temp = None
                finally:
                    root_Sorting.after_cancel(animate)



        #Generator function for generating data
        def generate():
            global columnList
            global lengthList
            work_space.delete('all')
            column_start = 5
            column_end = 15
            columnList = []
            lengthList = []

            #Creating a rectangle
            for column in range(1, 60):
                randomY = random.randint(10, 360)
                column = work_space.create_rectangle(column_start, randomY, column_end, 365, fill='#a1d46a')
                columnList.append(column)
                column_start += 10
                column_end += 10

            #Getting length of the bar and appending into length list
            for column in columnList:
                column = work_space.coords(column)
                length = column[3] - column[1]
                lengthList.append(length)

            
            




        global root_Sorting
        root_Sorting = Tk()
        root_Sorting.title("Algorithm Vizualiser")

        wdt = 700
        hit = 400
        app_wdt = root_Sorting.winfo_screenwidth()
        app_hit = root_Sorting.winfo_screenheight()

        x = (app_wdt/2) - (wdt/2)
        y = (app_hit/2) - (hit/2)
        root_Sorting.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
        root_Sorting.resizable(0,0)
        root_Sorting.config(bg="#A172FF")







        #Making a Canvas within the window to display contents
        work_space = tk.Canvas(root_Sorting, width='700', height='350')
        work_space.grid(column=0,row=0, columnspan = 50)



        #Buttons
        insert_btn = tk.Button(root_Sorting, text='Insertion Sort', command=insertion_sort, font=('Impact', 12), width=12, height=1)
        select_btn = tk.Button(root_Sorting, text='Selection Sort', command=selection_sort, font=('Impact', 12), width=12, height=1)
        bubble_btn = tk.Button(root_Sorting, text='Bubble Sort', command=bubble_sort, font=('Impact', 12), width=12, height=1)
        shuf_btn = tk.Button(root_Sorting, text='Shuffle', command=generate, bg = "#42f593", font=('Impact', 12), width=10, height=1)
        back_btn = tk.Button(root_Sorting, text='Back', command=Back, bg = "#ff0000", font=('Impact', 12), width=12, height=1)
        shuf_btn.grid(column=4, row=1)
        insert_btn.grid(column=3,row=1)
        select_btn.grid(column=2,row=1)
        bubble_btn.grid(column=1,row=1)
        back_btn.grid(column=0,row=1)


        generate()

    








    

    mainTabLabel=Label(root, text='WELCOME TO SORTING ALGORITHMS VISUALIZER', font=('Impact',25), bg="#FA0E4D")
    mainTabLabel.pack()
    SortingButton=Button(root, text='   SORTING ALGORITHMS   ', font=('Impact',20), bg="#6ad4ad", command=Sorting)
    SortingButton.place(x= 200, y=80)
    #PathfindingButton=Button(root, text=' PATHFINDING ALGORITHMS  ', font=('Impact',20), bg="#6ad4ad")
    #PathfindingButton.place(x= 350, y=80)

    
    load_sort = Image.open("Sorting_Algorithm_Icon.png")
    #load_path = Image.open("path_finding_algorithm_icon.png")
    render_sort = ImageTk.PhotoImage(load_sort)
    #render_path = ImageTk.PhotoImage(load_path)
    img_sort = Label(image=render_sort, borderwidth=0)
    #img_path = Label(image=render_path, borderwidth=0)
    img_sort.image = render_sort
    #img_path.image = render_path
    img_sort.place(x=250, y=170) 
    #img_path.place(x=410, y=170) 

    


mainTab()
root.mainloop()