import PySimpleGUI as sg
from zip_creator import make_archive

inp1 = sg.Input()
inp2 = sg.Input()
txt1 = sg.Text('Select Files to Compress: ')
txt2 = sg.Text('Select destination Folder: ')
choose1 = sg.FilesBrowse('Choose')
choose2 = sg.FolderBrowse('Choose')
compress = sg.Button('Compress')
output = sg.Text('',key='output')

window = sg.Window('Project 1', layout=[[txt1, inp1, choose1], [txt2, inp2, choose2], [compress,output]])
while True:
    event, values = window.Read()
    filepath = values['Choose'].split(';')
    folder = values['Choose0']
    make_archive(filepath,folder)
    window['output'].update(values='Compressed file generated!!')
window.Close()
