from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options


inmo = input("Introduce la URL: ")
DRIVER_PATH = './chromedriver.exe'
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=option)
driver.get(inmo)


#Clear Chromedriver notes and errors before showing results
os.system('cls||clear')

title = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[1]/div[1]/h1"))).text
address = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[4]/div/ul/li[4]/span[2]"))).text
price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[1]/div[2]/div[3]/div[2]"))).text
location = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[4]/div/ul/li[4]/span[2]"))).text
size = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[4]/div/ul/li[6]/span[2]"))).text
rooms = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[1]/div[2]/div[2]/ul/li[2]"))).text
baths = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[1]/div[2]/div[2]/ul/li[1]"))).text
description = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/section[3]"))).text

#Split location variable to print Zona_location and Poblacion_location
zona_location, sep_location, poblacion_location = location.partition(' / ')
#Split description variable to avoid new paragraph
head, sep, tail = description.partition('.\n')

print(f"Título: {title}\n")
print(f"Zona: {zona_location}\n")
print(f"Población: {poblacion_location}\n")
print(f"Tamaño: {size}\n")
print(f"Habitaciones: {rooms}\n")
print(f"Baños: {baths}\n")
print(f"Precio: {price}\n")
print(f"Descripción: {head}{tail}")


