
import pyautogui as pt
import time
import getpass

print('\033[32m')
print("******** *        *       *       *      * ********* * * * *       ")
print("*        *        *      * *      *    *   *         *      *      ")
print("*        *        *     *   *     *  *     *         *       *     ")
print("******** **********    *******    **       ********* *      *      ")
print("*        *        *   *       *   *  *     *         *   *         ")
print("*        *        *  *         *  *    *   *         *     *       ") 
print("******** *        * *           * *      * ********* *       *     ") 

print('\033[36m')
#password chek session!#============================================================================
key=("din101")

pw=getpass.getpass("Enter your password: ")

print('\033[31m')
while pw != key:
    pw=getpass.getpass("Enter incorrect password: ")

print('\033[32m'+"Password is correct!")    

print('\033[36m')
#spam sender chosose session!#=================================================================================
N = ("")
print("                         ")
limit = input("Enter msg limit: ")

while limit == N:
    limit = input("Enter msg limit: ")
print("                          ")

n = ("")
    
message = input ("Enter message: ")

while message == n:  
    message = input ("Enter message: ")

 
#spam sender session!#=========================================================================================
i = 0

time.sleep(4)   
print('\033[31m')
while i<int(limit):

    pt.typewrite(message)
    pt.press("enter")

    i+=1

#devaloper detais#=====================================================================================
print('\033[31m')
print("                                ")
print("..................DEVELOPER IS RASINDU KUMARASIRI..................")
