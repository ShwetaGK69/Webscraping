import bs4
import lxml
import requests
import urllib
import csv
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter
from tkinter import messagebox as mbox



url = ["https://sbi.co.in/web/interest-rates/deposit-rates/retail-domestic-term-deposits",
       "https://www.dcbbank.com/cms/showpage/page/open-fixed-deposit-rates",
       "https://www.federalbank.co.in/deposit-rate",
       "https://www.online.citibank.co.in/products-services/investments/deposits/deposits.htm"]

Bank1='State Bank of India (SBI)'
Bank2='Development Credit Bank (DCB)'
Bank3='Federal Bank'
Bank4='City Bank '
flag=0
global total_days
Rate1=[]
Rate2=[]
Rate3=[]
Rate4=[]
temp=[]

global data1,Amount
global data2,IR1,IR2,IR3,IR4
global data3,e1,e2,e3
global data4
IR1=0.0
IR2=0.0
IR3=0.0
IR4=0.0


#function 1
def create_IR_List(option):
        Rate = []
        for a in option:

            if ('days to' in a[0] and 'days to less than' not in a[0] and 'months' not in a[0]):  # x days to yy days
                b = (a[0].replace('days to', ''))
                b = b.replace('days', '')
                d = b.split(' ', 2)
                r1 = int(d[0])
                r2 = int(d[2]) + 1
                temp = [r1, r2, a[1]]
                Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #
                #    return a[1]


            elif ('days to less than' in a[0] and 'year' in a[0]):  # xxx days to less than 1 year
                b = (a[0].replace('days to less than', ''))
                b = b.replace('year', '')
                d = b.split(' ', 2)
                r1 = int(d[0])
                r2 = (int(d[2]) * 365)

                temp = [r1, r2, a[1]]
                Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #
                #     return a[2]

            elif ('days to less than' in a[0] and 'months' in a[0]):  # xxx days to less than yy months
                b = (a[0].replace('days to less than', ''))
                b = b.replace('months', '')
                d = b.split(' ', 2)

                r1 = int(d[0])
                r2 = (int(d[2]) * 30)

                temp = [r1, r2, a[1]]
                Rate.append(temp)

                # if (total_days in range(r1, r2)):
                #
                #     return a[1]

            elif ('months' in a[0] and 'less than' not in a[0] and 'days' not in a[0] and 'years' not in a[
                0] and 'years' not in a[0] and 'to less then' not in a[0] and 'More' not in a[0] and 'Above' not in a[0]):  # xx months
                b = (a[0].replace('months', ''))
                d = b.split(' ', 2)
                # print(d)
                r1 = int(d[0])

                if (r1 == 12):
                    temp = [365, 366, a[1]]
                    Rate.append(temp)

                elif (r1 == 18):
                    temp = [545, 546, a[1]]
                    Rate.append(temp)
                    # return a[1]

                elif(r1==20):
                    temp = [605, 606, a[1]]
                    Rate.append(temp)

                elif (r1 == 24):
                    temp = [730, 731, a[1]]
                    Rate.append(temp)
                    # return a[1]

                elif (r1 == 36):
                    temp = [1095, 1096, a[1]]
                    Rate.append(temp)
                    # return a[1]

                else:
                    temp = [0, 0, 0.0]
                    Rate.append(temp)

            elif ('months 1 day to less than' in a[0]):  # '12 months 1 day to less than 15 months'
                b = (a[0].replace('months 1 day to less than', ''))
                b = b.replace('months', '')
                d = b.split(' ', 2)

                r1 = int(d[0]) * 30
                r2 = (int(d[2]) * 30)+1
                if(int(d[0])==12 and int(d[2])==15):
                    temp = [366, 455, a[1]]
                    Rate.append(temp)

                else:
                   temp = [r1, r2, a[1]]
                   Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #
                #     return a[1]

            elif ('More than' in a[0] and 'months to less than' in a[0] or 'months to less then' in a[0]):  #  More than 24 months to less then 36 months
                b = (a[0].replace('More than', ''))
                b = b.replace('months to less than', '')
                b = b.replace('to less then', '')
                b = b.replace('months', '')
                b = b.replace('to', '')

                d = b.split(' ', 2)

                r1 = int(int(d[1]) * 30)
                r2 = (int(d[2]) * 30) + 1
                if(int(d[1])==18 and int(d[2])==24):
                    temp = [546, 730, a[1]]
                    Rate.append(temp)
                elif(int(d[1])==24 and int(d[2])==36):
                    temp = [731, 1095, a[1]]
                    Rate.append(temp)


                # if (total_days in range(r1, r2)):
                #     return (a[1])


            elif ('months' in a[0] and 'months to less than' in a[0]):  # xxx months to less than yy months
                b = (a[0].replace('months to less than ', ' '))
                b = b.replace('months', '')
                d = b.split(' ', 2)

                r1 = int(d[0]) * 30
                r2 = (int(d[2]) * 30) + 1
                if(int(d[2])==12):
                    temp = [r1, 365, a[1]]
                    Rate.append(temp)
                elif (int(d[0]) == 15 and int(d[2])==18):
                    temp = [455, 545, a[1]]
                    Rate.append(temp)
                else:
                  temp = [r1, r2, a[1]]
                  Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #     return a[1]

            elif ('year to less than' in a[0] and 'Above' not in a[0]):  # xxx year to less than yy year
                b = (a[0].replace('year to less than', ''))
                b = b.replace('year', '')
                d = b.split(' ', 2)
                r1 = int(d[0]) * 365
                r2 = int(d[2]) * 365
                temp = [r1, r2, a[1]]
                Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #     return a[1]



            elif ('years to less than' in a[0] and 'Above' not in a[0]):  # xxx years to less than yy years
                b = (a[0].replace('years to less than', ''))
                b = b.replace('years', '')
                d = b.split(' ', 2)
                r1 = int(d[0]) * 365
                r2 = int(d[2]) * 365
                temp = [r1, r2, a[1]]
                Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #     return a[1]


            elif ('years and up to' in a[0]):  # xxx years and up to yy years
                b = (a[0].replace('years and up to', ''))
                b = b.replace('years', '')
                d = b.split(' ', 2)
                r1 = int(d[0]) * 365
                r2 = int(d[2]) * 365
                temp = [r1, r2, a[1]]
                Rate.append(temp)
                # if (total_days in range(r1, r2)):
                #     return a[1]

            elif ('Above' in a[0] and 'months' in a[0] and'less than' not in a[0]):  # Above 20 months
                b = (a[0].replace('Above', ''))
                b = (b.replace('months', ''))
                d = b.split(' ', 3)
                r1 = int(d[1])
                if (r1 == 20):
                    r1 = 606
                    r2 = 3600
                    temp = [r1, r2, a[1]]
                    Rate.append(temp)


            elif ('Above 1 year to less than 20 months' in a[0]):  # Above 1 year to less than 20 months
                r1 = 366
                r2 = 605
                temp = [r1, r2, a[1]]
                Rate.append(temp)

            elif ('Above 1 year' in a[0] and 'less than' not in a[0]):  # Above 1 year
                r1 = 366
                r2 = 3651
                temp = [r1, r2, a[1]]
                Rate.append(temp)

            elif ('1096 Days' in a[0] and '>=' in a[0] ):  # >= 1096 Days
                r1 = 1096
                r2 = 3651
                temp = [r1, r2, a[1]]
                Rate.append(temp)

            elif ('year' in a[0] and 'Above' not in a[0]):  # xx year
                b = a[0].replace('year', '')
                d = b.split(' ', 2)
                r1 = int(d[0])
                if (r1 == 1):
                    r1 = 365
                    r2 = 366
                temp = [r1, r2, a[1]]
                Rate.append(temp)

            elif ('More than' in a[0] and 'months to' in a[0]):  # More than xx months to yy months
                b = (a[0].replace('More than', ''))
                b = (b.replace('months to', ''))
                b = (b.replace('months', ''))

                d = b.split(' ', 4)

                r1 = int(d[1])*30
                r2 = int(d[3])*30+1
                if(int(d[1])==36 and int(d[3])==60):
                    temp = [1096, 1826, a[1]]
                    Rate.append(temp)
                elif (int(d[1]) ==60 and int(d[3]) ==120):
                    temp = [1826, 3651, a[1]]
                    Rate.append(temp)

                else:
                    temp = [r1, r2, a[1]]
                    Rate.append(temp)


            elif ('Days' in a[0] and '-' in a[0]):
                b = a[0].replace('Days', '')
                b = b.replace(' ', '')
                b = b.replace('-', ' ')
                d = b.split(' ', 2)
                r1 = int(d[0])
                r2 = int(d[1])+1
                temp = [r1, r2, a[1]]
                Rate.append(temp)

            else:
                temp = [0, 0, 0.0]
                Rate.append(temp)
        return Rate

#   #####################################  Bar Graph Plotting  ###########################################
def draw_Graph(IR1,IR2,IR3,IR4):
        fig, ax = plt.subplots()

        bar_height_IR = [IR1,IR2,IR3, IR4]
        bar_tick_label = ['SBI', 'DCB', 'FEDERAL', 'CITY']
        y_pos = np.arange(len(bar_tick_label))
        bar_label = [str(IR1)+'%',str(IR2)+'%',str(IR3)+'%', str(IR4)+'%']

        bar_plot = plt.bar(y_pos, bar_height_IR, color=['blue', 'red', 'green', 'cyan'])
        plt.xticks(y_pos, bar_tick_label)


        def autolabel(rects):
         for idx, rect in enumerate(bar_plot):
           height = rect.get_height()
           ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                   bar_label[idx],
                   ha='center', va='bottom', rotation=0)


        autolabel(bar_plot)
        plt.ylim(0, 10)

        plt.title('Interest rates w.r.t Banks')
        plt.xlabel('Banks')
        plt.ylabel('Interest Rates')
        plt.show()
###########################  Graph Ends #################################################################

def Accept_Input():
    ######################################### GUI FUNCTIONS #######################
      master = Tk()
      master.title("Investment Management")

      def clearAll():
        # deleting the content from the entry box
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus()


      def createNewWindow(Bank,maxIR,i,Amount,IR1,IR2,IR3,IR4):
           newWindow = tkinter.Toplevel(master)

           label1 = tkinter.Label(newWindow, text=" **** Best Option Recommended By Us  ****",font='Verdana 18 bold italic',bg='white',fg='red').grid(row=1)
           label2 = tkinter.Label(newWindow, text=Bank+" : "+str(maxIR)+" %",font='Helvetica 24 bold',bg='white',fg='black').grid(row=2)
           label3 = tkinter.Label(newWindow, text="Interest Amount : " +str(i),font='Helvetica 24 bold',bg='white',fg='green').grid(row=3)
           Return= (round(float(Amount+i),3))
           label4 = tkinter.Label(newWindow, text="Total Return Amount: "+str(Return),font='Helvetica 24 bold',bg='white',fg='blue').grid(row=4)
           newWindow.configure(bg='white')
           # label =tkinter.Label(newWindow,Text==" **** Result from web scraping  ****",font="Comic Sans MS 12 bold").grid(row=5)
           draw_Graph(IR1,IR2,IR3,IR4)




      def calculate():
            Years = (e1.get())
            Months = (e2.get())
            Amount = (e3.get())
            if(Years=='' or Months=='' or Amount=='' ):
                mbox.showerror("Error", "Enter Valid Credentials")
            if(int(Years) > 9 or int(Months) > 11):
                mbox.showerror("Error", "Enter Valid Credentials")
            if(int(Amount)>=20000000):
                mbox.showerror("Error", "Enter Amount less than 2 crores")
            Years=int(Years)
            Months=float(Months)
            Amount=int(Amount)
            total_days = int((Years * 365) + (Months * 30))
            Period = round((total_days / 365), 4)
            print(Period, total_days, Amount)
            maxIR,Bank,IR1,IR2,IR3,IR4=Searching(total_days)
            Ir=Sorting(IR1, IR2, IR3, IR4)
            print("\n\n*************************   Result from Web Scraping  *****************************\n")
            for i in Ir:
                if (i == IR1):
                    print(Bank1, ' : ', IR1, ' %')
                elif (i == IR2):
                    print(Bank2, ' : ', IR2, ' %')
                elif (i == IR3):
                    print(Bank3, ' : ', IR3, ' %')
                elif (i == IR4):
                    print(Bank4, ' : ', IR4, ' %')
            print('\n***********************************    Best Option Recommended by Us       *************************************\n')
            print(Bank, " : ", maxIR, "%")
            i = round(float((Amount * Period * maxIR) / 100), 3)
            print("Interest Amount: ", i)
            print("Total Return Amount: ", round(float(Amount + i), 3))
            createNewWindow(Bank,maxIR,i,Amount,IR1,IR2,IR3,IR4)





        ###############################################################################################################3#


      Label(master, text='Enter Years',font='Arial 20 bold italic',bg='midnight blue',fg='coral').grid(row=3)
      Label(master, text='Enter Months',font='Arial 20 bold italic',bg='midnight blue',fg='coral').grid(row=4)
      Label(master, text='Enter Amount',font='Arial 20 bold italic',bg='midnight blue',fg='coral').grid(row=5)
      Label(master, text='*******************************************************',bg='midnight blue',fg='cyan').grid(row=6, column=0)
      Label(master, text='*******************************************************',bg='midnight blue',fg='cyan').grid(row=6, column=1)
      Label(master, text='******************************************************',bg='midnight blue',fg='cyan').grid(row=6, column=2)


      image1 = tkinter.PhotoImage(file='b2.png')
      label_for_image = Label(master, image=image1).grid(row=1,column=1)
      button = tkinter.Button(master, text='Close',font='verdana 20 bold', width=15, bd='10', command=master.destroy,bg='black',fg='white').grid(row=7, column=2)
      button = tkinter.Button(master, text='Clear',font='verdana 20 bold', width=15, bd='10', command=clearAll,bg='black',fg='white').grid(row=7, column=1)
      button = tkinter.Button(master, text='Calculate',font='verdana 20 bold', width=15, bd='10', command=calculate,bg='black',fg='white').grid(row=7, column=0)

      e1 = Entry(master)
      e2 = Entry(master)
      e3 = Entry(master)

      e1.grid(row=3, column=1)
      e2.grid(row=4, column=1)
      e3.grid(row=5, column=1)


      master.configure(bg='midnight blue')


      master.mainloop()

#Function 3
def SearchIR(Rate,total_days):
         for i in Rate:
          if(total_days in range(int(i[0]),int(i[1]))):
              ir=i[2].replace('%','')
              ir1=float(ir)
              return ir1

# Function 4   ######################   Finding IR for particular record ###################################

def Searching(total_days):
       IR1 = SearchIR(Rate1,total_days)
       # IR1=int(IR1.replace('%',''))
       IR2 = SearchIR(Rate2,total_days)
       # IR2 = int(IR2.replace('%', ''))
       IR3 = SearchIR(Rate3,total_days)
       # IR3 = int(IR3.replace('%', ''))
       IR4 = SearchIR(Rate4,total_days)
       # IR4 =int(IR4.replace('%', ''))
       # print(IR1,IR2,IR3,IR4)

       maxIR = max(IR1, IR2, IR3, IR4)
       if (maxIR == IR1):
           Bank = Bank1
       elif (maxIR == IR2):
           Bank = Bank2
       elif (maxIR == IR3):
           Bank = Bank3
       elif (maxIR == IR4):
           Bank = Bank4

       return maxIR,Bank,IR1,IR2,IR3,IR4


# Function 5  ######################   Sorting IRs ###################################

def Sorting(IR1,IR2,IR3,IR4):
      Ir = [IR1, IR2, IR3, IR4]
      Ir.sort(reverse=True)
      return Ir


try:

   for i in url:
    data = requests.get(i)
    if(i=='https://sbi.co.in/web/interest-rates/deposit-rates/retail-domestic-term-deposits'):
        data1=data.text
    elif(i=='https://www.dcbbank.com/cms/showpage/page/open-fixed-deposit-rates'):
        data2=data.text
    elif (i == 'https://www.federalbank.co.in/deposit-rate'):
        data3 = data.text
    elif (i == 'https://www.online.citibank.co.in/products-services/investments/deposits/deposits.htm'):
        data4 = data.text
    # if (int(data.status_code) == 200):
    #     flag=flag+1

################################################### For SBI ########################################################
   print("Web Scraping Starts...... ")
   soup1 = bs4.BeautifulSoup(data1, 'lxml')  # parse the text

   tb1 = soup1.find('table', class_='table table-bordered')
   option1=[]

   for link in tb1.find_all('tr'):
    name = link.find_all('td')
    row = [i.text.strip() for i in name]
    option1.append(row)

   option1.remove(option1[0])


   for row in option1:
       del row[3:]
       del row[1]

   Rate1 = create_IR_List(option1)
   # print(Rate1)

   file = open("myfile.csv", 'w',newline='')
   writer=csv.writer(file)
   writer.writerow(['##########   State Bank Of India   #############'])
   writer.writerows(Rate1)


     ################################################ For DCB #######################################################
   soup2 = bs4.BeautifulSoup(data2, 'lxml')  # parse the text
   tb2=soup2.find('table',class_='scrolltableRates')
   # print(tb2)
   option2=[]
   for link in tb2.find_all('tr'):
        name=link.find_all('td')
        row = [i.text.strip() for i in name]

        option2.append(row)

   option2.remove(option2[0])
   option2.remove(option2[0])
   option2.remove(option2[0])

   for row in option2:
     row.remove(row[4])
     row.remove(row[3])
     row.remove(row[2])
     # print(row)
   # print(option2)

   Rate2=create_IR_List(option2)
   writer.writerow(['##########   DCB  #############'])
   writer.writerows(Rate2)

   # print(Rate2)

  ############################################### For Federal ########################################################

   soup3 = bs4.BeautifulSoup(data3, 'html.parser')  # parse the text
   tb3=soup3.find('table', attrs={'style': 'width:98%;text-align:left;font-size: 14px;'})
   # print(tb2)
   option3 = []
   for link in tb3.find_all('tr'):
     name = link.find_all('td')
     row = [i.text.strip() for i in name]
     option3.append(row)
   option3.remove(option3[0])

   Rate3 = create_IR_List(option3)

   # print(Rate3)
   writer.writerow(['##########   Federal  #############'])
   writer.writerows(Rate3)

  ############################################### For City ########################################################

   soup4 = bs4.BeautifulSoup(data4, 'html5lib')  # parse the text

   soup=soup4.find('div',class_="overflow12")
   tb=soup.find('table',class_='clsTable clsTableFont dropshadow rounded tabpad')

   option4=[]

   for link in tb.find_all('tr'):
     name = link.find_all('td')
     row = [i.text.strip() for i in name]
     option4.append(row)

   option4.remove(option4[0])
   option4.remove(option4[0])

   for i in option4:
       del i[2:]
   Rate4 = create_IR_List(option4)

   writer.writerow(['##########   City   #############'])
   writer.writerows(Rate4)

   # print(Rate4)




# ################################### input #############################
   Accept_Input()

except Exception as e:
   print("Web Scraping Not Possible due to Exception !!\n**************************************************************************\n")
   print(e)
   #############################   File Reading  #######################################3##############
   print("Accessing Local File...")
   contents = []
   fields = []
   file = 'myfile.csv'
   with open(file, 'r') as csvfile:
       csvreader = csv.reader(csvfile)

       for row in csvreader:
           contents.append(row)

   for row in contents:
       if ('##########   DCB  #############' in row):
           break
       else:
           Rate1.append(row)

   flag = 0
   for row in contents:
       if ('##########   DCB  #############' in row or flag == 1):
           flag = 1
           if ('##########   Federal  #############' not in row and flag == 1):
               Rate2.append(row)
           else:
               break
   flag = 0
   for row in contents:
       if ('##########   Federal  #############' in row or flag == 1):
           flag = 1
           if ('##########   City   #############' not in row and flag == 1):
               Rate3.append(row)
           else:
               break
   flag = 0
   for row in contents:
       if ('##########   City   #############' in row or flag == 1):
           flag = 1
           Rate4.append(row)

   Rate1.remove(Rate1[0])
   Rate2.remove(Rate2[0])
   Rate3.remove(Rate3[0])
   Rate4.remove(Rate4[0])

   # print(Rate1)
   # print(Rate2)
   # print(Rate3)
   # print(Rate4)

   Accept_Input()









