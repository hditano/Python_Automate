import eel
import webview
from time import sleep


eel.init('web')
eel.start('hello.html', size=(1216, 739),mode=None, block=False)


webview.create_window('Title', 'web/hello.html', frameless=True, easy_drag=False)

webview.start()