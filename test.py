from plyer import notification
import os, time


while True :
    
    notification.notify(
        title="Hello!",
        message=f"Notification sent from {os.getcwd()}.",
        app_icon = os.path.join(os.getcwd(), 'syringe.ico'),
        timeout = 15

    )
    print("Sleeping!")
    time.sleep(10)



