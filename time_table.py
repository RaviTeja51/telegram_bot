from telegram.ext import Updater,CommandHandler
import telegram,datetime,re,os
from openpyxl import load_workbook # A python library to work with Excel xlsx/xlsm/xltx/xltm files.


#loads the workbook( like a pointer for the spread_sheet, storing it in wb) in read only mode
wb = load_workbook(filename =  'TIME_TABLE.xlsx')


#to get the active sheet in the work book
sheet = wb.get_sheet_by_name('timetable')

def main():
    '''
     This is the main funtion which send the message to the user
    '''

    #using environment variable for security purpose
    bot = telegram.Bot(token = os.environ['token'])
    mssg = get_schedule()
    with open("chat_id.txt") as f:
        #to read all lines in the file
        c = f.readlines()
    #using the regex module to create regular expression object for a string ending with digits, to get the chat id
    id1  = re.compile(r'\d{9}$')

    for i in c:
        try:
            print("Sending message...")
            id = id1.search(i)
            id = id.group()
            name = i
            bot.send_message(chat_id=(id),text=mssg)
            print(f"Message sent to user {name}")

        except:
            exit("It didn't work")




def get_weekday():
    '''
      The objective of the fuction is to return the current day of the week
    '''

    #the datetime.datetime.today().weekday returns an integer i.e 0 for monday...6 for sunday
    v = datetime.datetime.today().weekday()
    days = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
    current_day = days[v]
    return(current_day)


def get_schedule():
    '''
       The objective of this function is to get the daily time table and to format it along with the timings.
    '''

    #calls the function get_weekday for geting the current weekday
    current_day = get_weekday()
    row = 0
    time_table = []

    #To get the row number of the current day from the spread sheet
    for i in range(5,10):
        if sheet[f'A{i}'].value == current_day:
            row = i

    #to get the class
    for rows in sheet[f'B{row}':f'H{row}']:
        for cell in rows:
            #to replace none with "no class", because an empty cell is treated as none
            if not cell.value:
                time_table.append("NO_CLASS")
            else:
                time_table.append(cell.value)

    time = []
    #to get the class timings
    for rows in sheet['B3':'H3']:
        for cell in rows:
            time.append(cell.value)

    schedule = ""
    #to format time_table and time as a storing
    for i,j in zip(time_table,time):
        schedule += j+  "     " + i + "\n"

    return(schedule)



if __name__ == '__main__':
    main()
