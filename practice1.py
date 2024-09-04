import FreeSimpleGUI as sg

text1 = sg.Text("Enter Feet:")
text2= sg.Text("Enter Inches:")
input1 = sg.Input()
input2=sg.Input()
convertButton = sg.Button("Convert")
window = sg.Window("Convertor",layout=[[text1,input1],[text2,input2]])
window.read()
window.close()