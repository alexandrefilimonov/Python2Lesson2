#!/usr/bin/python
# -*- coding: Windows-1250 -*-
import os, sys
import csv

#1. Read values from 3 files
def get_data(files_list) :
    #???????????? ???????
    manufacturer_in_byte = b'\xd0\x98\xd0\xb7\xd0\xb3\xd0\xbe\xd1\x82\xd0\xbe\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b'
    #???????? ?? 
    os_name_in_byte = b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5\xd0\x9e\xd0\xa1' 
    #??? ???????? 
    product_code_in_byte = b'\xd0\xa2\xd0\xb8\xd0\xbf \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b'
    #??? ???????
    system_type_in_byte = b'\xd0\xa2\xd0\xb8\xd0\xbf \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b'
    #2. create 4 lists with 3 values from .txt files
    os_prod_list = []
    os_name_list = [] 
    os_code_list = [] 
    os_type_list = []

    for file in files_list:	
        with open(file, 'r') as f: #, encoding='utf8', errors='ignore'
            reader = csv.reader(f)
            i =0
            for row in list(reader):        
                s = row[0]
                if(manufacturer_in_byte==s[0:20].encode('Utf-8')) : #11	
                    os_prod_list.append(s[21:].strip())
                if(product_code_in_byte==s[0:12].encode('Utf-8')) : #8
                    os_code_list.append(s[13:].strip()) 
                if(system_type_in_byte==s[0:11].encode('Utf-8')) : #13
                    os_type_list.append(s[12:].strip())
                if(os_name_in_byte==s[0:11].encode('Utf-8')) : #1
                    os_name_list.append(s[12:].strip())				
                i+=1	
				
    #3. create data for ouput file 
    titles=['???????????? ???????','???????? ??','??? ????????','??? ???????']
    #data_rows = [[os_prod_list],[os_name_list],[os_code_list],[os_type_list]]
    data = [titles]
    for i in range(0,3):
        row = [os_prod_list[i],os_name_list[i],os_code_list[i],os_type_list[i]]	
        data.append(row)	
    return data 	

#4. 
def write_to_csv(file_name, data) :
    with open(file_name, 'w', encoding='utf8') as f:
        writer = csv.writer(f) 
        for row in data: 
            writer.writerow(row) 

files_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
data = get_data(files_list)
write_to_csv('main3.txt', data)


