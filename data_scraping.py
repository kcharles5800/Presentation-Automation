from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to scrape the required data and return it in a list 

class get_data:



    def extraction(search_input) :

        driver = webdriver.Chrome()

        # handling those unwanted errors (current bugg in the chrome driver)

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)

        if search_input[slice(0,5)] == 'https':

            try :
                driver.get(search_input)
            except :
                print('No access to the internet')
                sleep(1)
                print('operation terminated')
                return 0
            driver.implicitly_wait(10)  

        else :
            try :
                driver.get('https://tamilchristiansongs.in/')
            except :
                print('No access to the internet')
                sleep(1)
                print('operation terminated')
                return 0
            driver.implicitly_wait(10)

            WebDriverWait(driver,timeout=10).until(EC.presence_of_all_elements_located((By.ID,"keyword")))
            search_content = driver.find_element(By.ID,"keyword")
            search_content.send_keys(search_input)

            driver.implicitly_wait(5)

            # searching for the song & loading the lyrics page
            try :
                table_content = driver.find_element(By.CLASS_NAME,"toast-body")
            except :
                print('The song was not found')
                print('check your input and try again..')
                return 0
            
            items_list = table_content.find_element(By.TAG_NAME,"ul")
            required_song = items_list.find_element(By.TAG_NAME,"li")
            song_tag = required_song.find_element(By.TAG_NAME,"a")
            song_tag.click()

        # scraping the the lyrics from the webpage

        # English lyrics 
        eng_lyrics = []                      # list will store the lyrics in english
        WebDriverWait(driver,timeout=10).until(EC.presence_of_all_elements_located((By.ID,"tamilroman")))
        english_lyrics = driver.find_element(By.ID,"tamilroman")
        english_lyrics = english_lyrics.find_element(By.ID,"roman_tamiltext")
        english_lyrics = english_lyrics.find_elements(By.TAG_NAME,"p")
        for i in range(len(english_lyrics)) :
            if ((i == 0)and(len(english_lyrics[i].text.split("\n")) == 1)):
                continue
            paragraph_lines = english_lyrics[i].text.split("\n")
            if(len(paragraph_lines) == 1) :
                paragraph_lines.append("")
            eng_lyrics += paragraph_lines

            if len(eng_lyrics)%2 :
                eng_lyrics.append('')

        # Tamil lyrics
        tam_lyrics = []                      # list will store the lyrics in tamil
        tamil_lyrics = driver.find_element(By.ID,"tamiltext")
        tamil_lyrics = tamil_lyrics.find_elements(By.TAG_NAME,"p")
        for i in range(len(tamil_lyrics)) :
            if ((i == 0)and(len(tamil_lyrics[i].text.split("\n")) == 1)):
                continue
            paragraph_lines = tamil_lyrics[i].text.split("\n")
            if(len(paragraph_lines) == 1) :
                paragraph_lines.append("")
            tam_lyrics += paragraph_lines

            if len(tam_lyrics)%2 :
                tam_lyrics.append('')

        driver.quit()

        # edge case : if the english lyrics is repeated in the tamil container

        for i in range(1,len(tam_lyrics)):
            if tam_lyrics[i] == eng_lyrics[i] and tam_lyrics[i] != '':
                tam_lyrics = tam_lyrics[0:i]
                eng_lyrics = eng_lyrics[0:i]
                break;

        print("data extraction complete...")

        return [tam_lyrics,eng_lyrics]   #list of list for both lyrics 