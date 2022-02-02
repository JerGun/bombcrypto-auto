import autoit
import time

autoit.run("notepad.exe")
time.sleep(1)
autoit.win_wait_active("[CLASS:Notepad]", 3)
time.sleep(1)

autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
time.sleep(1)

autoit.win_close("[CLASS:Notepad]")
time.sleep(1)

autoit.control_click("[Class:#32770]", "Button2")
