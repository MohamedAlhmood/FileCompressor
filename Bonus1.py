from importlib.metadata import files

import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose",key='files')

label2= sg.Text("Select Destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key='folder')
compressButton = sg.Button("Compress")
window  = sg.Window("File Compressor", finalize=True, layout=[[label1,input1,choose_button1],[label2,input2,choose_button2],[compressButton]])
while True:
    event,values=window.read()
    print(event)
    print(values)
    filepath = values['files'].split(';')
    folder = values['folder']
    print("file ",filepath)
    match event:
        case sg.WIN_CLOSED:
            break
window.close()