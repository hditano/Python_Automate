import PySimpleGUI as sg

def Test():
    list = ['Hello', 'World']
    return list

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('', size=(60, 1)),sg.Text('🗖', enable_events=True, key='Max'),sg.Text('X',enable_events=True ,key='Input1')],
            [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Text('', key='Input2')],
            [sg.Button('Ok'), sg.Button('Cancel')]
        ]

# Create the Window
window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel' or event == 'Input1': # if user closes window or clicks cancel
        break
    elif event == 'Max':
        window.maximize()
        state = window.TKroot.state()
        print(state)
        if state == 'zoomed':
            window.minimize()
    elif event == 'Ok':
        window['Input2'].update(Test())
        



window.close()