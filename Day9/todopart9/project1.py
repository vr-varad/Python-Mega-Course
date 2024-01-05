import PySimpleGUI as sg
inp1 = sg.InputText()
inp2 = sg.InputText()
txt1 = sg.Text('Select Files to Compress: ')
txt2 = sg.Text('Select destination Folder: ')
btn1 = sg.Button('Choose')
btn2 = sg.Button('Choose')
btn3 = sg.Button('Compress')

window = sg.Window('Project 1',layout=[[[txt1,inp1,btn1],[txt2,inp2,btn2],[btn3]]])
window.Read()
window.Close()