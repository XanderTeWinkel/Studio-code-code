import openpyxl
import os

def append_to_excel(file_name, data):
    # Check if file exists
    if os.path.exists(file_name):
        # Load the workbook and select the active worksheet
        workbook = openpyxl.load_workbook(file_name)
        sheet = workbook.active
    else:
        # Create a new workbook and sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        # Optionally, add headers if it's a new file
        sheet.append(['Song', 'Artist', 'Duration (s)', 'Genres', 'Danceability', 'Energy', 'Loudness', 'Tempo', 'Acousticness'])

    # Append the data
    sheet.append(data)

    # Save the workbook
    workbook.save(file_name)

# Data you want to write to the file
song_data = ["Don't Stop Me Now - Remastered 2011", 'Queen', 74, 'classic rock, glam rock, rock', 0.563, 0.865, 0.601, 156.271, 0.0472]

# Call the function to append data
append_to_excel("songs.xlsx", song_data)
