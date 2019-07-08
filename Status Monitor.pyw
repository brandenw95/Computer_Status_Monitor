import win32print
import socket
import psutil
import time
import yagmail
import smtplib
import platform
import time
import datetime
import getpass
import os
import subprocess

PRINTER_ERROR_STATES = (
    win32print.PRINTER_STATUS_NO_TONER,
    win32print.PRINTER_STATUS_NOT_AVAILABLE,
    win32print.PRINTER_STATUS_OFFLINE,
    win32print.PRINTER_STATUS_OUT_OF_MEMORY,
    win32print.PRINTER_STATUS_OUTPUT_BIN_FULL,
    win32print.PRINTER_STATUS_PAGE_PUNT,
    win32print.PRINTER_STATUS_PAPER_JAM,
    win32print.PRINTER_STATUS_PAPER_OUT,
    win32print.PRINTER_STATUS_PAPER_PROBLEM,
)


def printer_errorneous_state(printer, error_states=PRINTER_ERROR_STATES):
    prn_opts = win32print.GetPrinter(printer)
    status_opts = prn_opts[18]
    for error_state in error_states:
        if status_opts & error_state:
            return error_state
    return 0

def printer_check():

    printer_name = "EPSON ET-16500 Series"
    printer_name_1 = "HP OfficeJet Pro 6970"
    prn = win32print.OpenPrinter(printer_name_1)
    error = printer_errorneous_state(prn)
    if error:
        print("ERROR occurred: ", error)
        email(error)
    else:
        print("Printer        OK...")
        

    win32print.ClosePrinter(prn)

def internet_check():

    host = "8.8.8.8"
    port = 53
    timeout = 3
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print("Conectivity    OK...")
        return True
    except Exception as ex:
        print(ex.message)
        email(ex.message)
        return False

def check_system():


    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory()[2]
    
    if cpu >= 80:
        
        cpu_error = "CPU usage too high ==> " + str(cpu) + "%"
        print(cpu_error)
        email(cpu_error)

    elif mem >= 80:
        
        mem_error = "Memory utilization too high ==> " + str(mem) + "%"
        print(mem_error)
        email(mem_error)

    else:
        print("CPU Usage      OK...")
        print("Memory Usage   OK...")

def email(error):

    computer_name = platform.node()
    ip = socket.gethostbyname(computer_name) 
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    FROM = "branden8570@gmail.com"
    TO = "branden@prostreet.ca"
    msg = "(" + timestamp + ")" + " Error posted below: \n ------------------------------------ \n\n" + error + "\n\n------------------------------------"
    subject = "Something went wrong with " + computer_name + " (" + ip + ")"

    yag = yagmail.SMTP(FROM, 'Branden_2016')
    yag.send(TO, subject, msg)

def add_to_startup(file_path=""):

    USER_NAME = getpass.getuser()
    
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

def ping_internal_computer(hostname, ip):

    response = subprocess.run("ping -n 1 " + ip)
    #response = os.system("ping -n 1 " + ip)

    #and then check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        error = hostname + " is down"
        email(error)
        print(hostname, 'is down!')
        

def main():
    
    #add_to_startup()
    #count = 0
    #while(True):

        #printer_check()
        #internet_check()
        #check_system()
        #count = count + 1
        #print(count)
        #time.sleep(30)
    printer_check()
    internet_check()
    check_system()
    print("")
    ping_internal_computer("FC-3", "192.168.0.172")
    print("")
    ping_internal_computer("FC-2", "192.168.0.168")
    print("")
    ping_internal_computer("FC-1", "192.168.0.186")
    print("")
    ping_internal_computer("tyler-office", "192.168.0.157")
        
        

if __name__ == "__main__":
    main()