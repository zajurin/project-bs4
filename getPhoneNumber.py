import openpyxl
import requests
import bs4
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from bs4 import BeautifulSoup

import re

import urllib.request
import phonenumbers


#******* AVOID BEING BLOCKED *******
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


#******* WORKING WITH EXCEL *******
chooseExcel_File = "C:\\Users\\rosenberg\\Desktop\\withPython\\PracticeBS4\\p1\\src\\myAddresses.xlsx"
choose_SHEET_Of_Your_Excel_File = 'Hoja1'

wb = load_workbook(chooseExcel_File, data_only=True)
sh = wb[choose_SHEET_Of_Your_Excel_File]

rowM = sh.max_row

whichCountry = "US"

for r in range(2, rowM+1):
    try:
        #READER OF EXCEL FILE

        #Company Name
        letter_Of_Column_With_Name_Of_Companies = "C"
        letter_Of_Column_With_ADDRESS_Of_Companies = "D"        
        number_Of_Row_With_Name_Of_Companies = r
        string_Of_number_Of_Row_With_Name_Of_Companies = str(r)

        concatenater_Column_With_Number_For_NAME = letter_Of_Column_With_Name_Of_Companies + string_Of_number_Of_Row_With_Name_Of_Companies
        concatenater_Column_With_Number_for_ADDRESS = letter_Of_Column_With_ADDRESS_Of_Companies + string_Of_number_Of_Row_With_Name_Of_Companies
        companyName = sh[concatenater_Column_With_Number_For_NAME].value 
        
        companyAddress = sh[concatenater_Column_With_Number_for_ADDRESS].value
        if companyAddress is None:
            companyAddress = " headquarters"

        print(companyName)#Tell me which Company was reviewed
        print(companyAddress)#Tell me the address of that one

        #CREATING URL FOR GOOGLE SEARCHING
        text = ("phone number of {0} {1} ".format(companyName, companyAddress))
        myCurrentURL = 'https://google.com/search?q=' + text

        #ACCESING TO URL's INFO
        response = requests.get(myCurrentURL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #Look for this tag
        tagSearched = soup.find_all('span', attrs={'class': 'mw31Ze'})# Level 1
        tagSearched2 = soup.find_all('h3', text = re.compile(companyName), attrs = {'class' : 'LC20lb DKV0Md'})# Level 2
        # tagSearched_3 = soup.findAll('h3', text = re.compile(companyName), attrs = {'class' : 'LC20lb DKV0Md'})# Level 3
        if tagSearched:
            print("Fund it")
            for tag in tagSearched:
                companyPhoneNumber = tag.text.strip()
                letter_Of_Column_To_Put_Phone_Number = "E"
                concatenater_Row_With_Column_For_Number = letter_Of_Column_To_Put_Phone_Number + string_Of_number_Of_Row_With_Name_Of_Companies
                sh[concatenater_Row_With_Column_For_Number] = companyPhoneNumber
                wb.save(filename = chooseExcel_File)
        elif tagSearched2:
            print("Level 2")
            if tagSearched2:
                children = tagSearched2.find_children("span" , recursive=False)
                print(children)

# __________
                # for child in children:
                #     new_TD = str(child)
                #     for match in phonenumbers.PhoneNumberMatcher(new_TD, whichCountry):
                #         onlyTheNumber = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
                #         print(onlyTheNumber)
                #         companyPhoneNumber = tag.text.strip()
                #         letter_Of_Column_To_Put_Phone_Number = "E"
                #         concatenater_Row_With_Column_For_Number = letter_Of_Column_To_Put_Phone_Number + string_Of_number_Of_Row_With_Name_Of_Companies
                #         sh[concatenater_Row_With_Column_For_Number] = companyPhoneNumber
                #         print(onlyTheNumber)
                #         wb.save(filename = chooseExcel_File)
                # _____

        # elif tagSearched3:
        #     print("Level 3")
        #     children = tagSearched3.findChildren()
        #     for child in children:
        #         print(child)        
        else:
            print('ELSE')     
                           
  
    except:
        print("Something went wrong")

        