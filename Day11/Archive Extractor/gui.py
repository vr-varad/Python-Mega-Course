import PySimpleGUI as sg
from zip_extractor import  extract_archive

inp1 = sg.Input()
inp2 = sg.Input()
text1 = sg.Text('Select ZIP folder: ')
text2 = sg.Text('Select Extraction Location: ')
choose1 = sg.FilesBrowse('Choose', key='archive')
choose2 = sg.FolderBrowse('Choose', key='folder')
extract = sg.Button('Extract')
output = sg.Text('', key='output')

window = sg.Window(title='Archive Extractor',
                   layout=[[text1, inp1, choose1], [text2, inp2, choose2], [extract, output]])

while True:
    event, values = window.read()
    archive_path = values['archive']
    dest_dir = values['folder']
    print(archive_path,dest_dir)
    extract_archive(archive_path,dest_dir)
    window['output'].update(value='Extraction Completed')
window.close()
