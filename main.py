from data_scraping import get_data
from generate_ppt import create_ppt


ref = input("Enter the name of the song or link of the song :\n")
print('initiating web drivers...')


if ref:
    lyrics = get_data.extraction(ref)

if lyrics :
    create_ppt.make(lyrics)