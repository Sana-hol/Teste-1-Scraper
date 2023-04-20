import time
import pandas as pd
import os.path
import datetime
from urlextract import URLExtract
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv


url = "https://www.linkedin.com/jobs/search?location=Brasil&geoId=106057199&f_E=1&f_JT=F&position=1&pageNum=0"
path = "K:\ProjetosPython\Projetos\Desafio\GUILHERME RAMONE"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.set_window_size(1700, 1400)
time.sleep(3)




urnVagas = []




urn = []   #urn da vaga
urls = []   #url da vaga
nome = []   #nome da vaga
nomempr = []    #nome da empresa
linkempr = []   #link da empresa
datapos = []    #data da postagem da vaga
nivexp = []     #nivel experiencia da vaga
tipcon = []     #tipo de contratação
locemp = []     #local da sede da empresa
numcont = []    #numero de candidatos para a vaga
horascrape = [] #horario do scrape
linkinsc = []   #link da inscrição da vaga
numf = []       #numeros funcionarios da empresa
nums = []       #numero seguidores da empresa
flag = 0






if not os.path.exists('Scraping - Guilherme Ramone Fontenele.csv'):
   dict = {'URL da vaga': url, 'Nome vaga': nome, 'Nome da empresa': nomempr, 'URL da empresa': linkempr,
           'Tipo de contratação': tipcon, 'Nivel de experiencia': nivexp, 'Numero de candidaturas': numcont,
           'Data da postagem': datapos, 'Horario do scrape': horascrape, 'Numero de funcionarios': numf,
           'Numero de seguidores': nums, 'local empresa': locemp, 'URL da candidatura': linkinsc, 'urn':urn}
   df = pd.DataFrame(dict)
   df.to_csv('Scraping - Guilherme Ramone Fontenele.csv', index=False)
   time.sleep(3)
data = pd.read_csv('Scraping - Guilherme Ramone Fontenele.csv', encoding='cp1252')
urnscvs = data['urn'].tolist()
print(urnscvs)
if urnscvs != urnVagas:
   for element in urnscvs:
       if element not in urnVagas:
           urnVagas.append(element)
       else:
           continue
else:
   pass
print(urnVagas)
flag = len(set(urnVagas)) == len(urnVagas)
if(flag):
   print("List contains all unique elements")
else:
   print("List contains does not contains all unique elements")
while len(urnVagas) < 3000:
   driver.switch_to.window(driver.window_handles[0])
   urls = nome = nomempr = linkempr = tipcon = nivexp = numcont = datapos = horascrape = numf = nums = locemp = linkinsc = urn = 0
   try:
        if "neterror" in driver.find_element(By.XPATH, f'//body[contains(@class, "neterror")]').get_attribute("class"):
            for x in range(3, 0, -1):
                try:
                    driver.switch_to.window(driver.window_handles[x])
                    driver.close()
                except:
                    pass
   except:
       pass




   if "authwall" not in driver.current_url:
       vagasnovas = driver.find_elements(By.XPATH, "//li/div[contains(@class, 'bas')]")
       urn = 0
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       try:
           load_more_vagas = driver.find_element(By.XPATH, '//button[@aria-label="Ver mais vagas"]')
           load_more_vagas.click()
       except:
           pass
       for vagas in vagasnovas:
           try:
               if vagas.get_attribute("data-entity-urn") not in urnVagas:




                   urnVagas.append(vagas.get_attribute("data-entity-urn"))
                   urn = vagas.get_attribute("data-entity-urn")
                   ls = urnVagas.index(urn)
                   pass




               else:
                   if all(x in vagasnovas for x in urnVagas):
                       driver.execute_script("window.scrollTo(0, -40);")
                       time.sleep(.5)
                       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                       time.sleep(.5)
                       vagasnovas = driver.find_elements(By.XPATH, "//li/div[contains(@class, 'bas')]")


                   else:
                       continue




                   continue




               driver.find_element(By.XPATH, f"//*[contains(@data-entity-urn,'{urn}')]").click()
               time.sleep(.2)
               driver.find_element(By.XPATH, f"//*[contains(@data-entity-urn,'{urn}')]").click()
               time.sleep(0.5)
               urls = driver.find_element(By.XPATH, f"//div[2]/section/div/div[1]/div/a").get_attribute("href")
               nome = driver.find_element(By.XPATH, f"//*[contains(@data-entity-urn,'{urn}')]/div/h3").text
               nomempr = driver.find_element(By.XPATH, f"//*[contains(@data-entity-urn,'{urn}')]/div/h4/a").text
               linkempr = driver.find_element(By.XPATH, "//div/h4/div[1]/span[1]/a").get_attribute("href")
               linkempr = linkempr.removesuffix("?trk=public_jobs_topcard-org-name")
               datapos = driver.find_element(By.XPATH, f"//*[contains(@data-entity-urn,'{urn}')]/div/div/time").text
               nivexp = driver.find_element(By.XPATH, f"//div/ul/li[1]/span").text
               tipcon = driver.find_element(By.XPATH, f"//div/ul/li[2]/span").text
               try:
                   numcont = driver.find_element(By.XPATH, f"//h4/div[2]/span[2]").text
               except:
                   numcont = driver.find_element(By.XPATH, f"//h4/div[2]/figure/figcaption").text
               numcont = ''.join(i for i in numcont if i.isdigit() or i in '-./\\')
               locemp = driver.find_element(By.XPATH, f"//h4/div[1]/span[2]").text
               horascrape = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
               driver.execute_script("window.open('');")
               driver.switch_to.window(driver.window_handles[1])
               driver.get(urls)
               time.sleep(2.5)
               if "authwall" not in driver.current_url:


                   nivexp = driver.find_element(By.XPATH, f'//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[1]/span').text
                   tipcon = driver.find_element(By.XPATH, f'//*[@id="main-content"]/section[1]/div/div/section[1]/div/ul/li[2]/span').text
                   hml = driver.page_source
                   soup = BeautifulSoup(hml, 'lxml')
                   lik = soup.find("code", {"id": 'applyUrl'})
                   extractor = URLExtract()
                   linkinsc = extractor.find_urls(str(lik))
                   driver.find_element(By.XPATH, "//div[1]/span[1]/a").click()
                   driver.switch_to.window(driver.window_handles[2])
                   time.sleep(2.5)


                   numf = driver.find_element(By.XPATH, f"//*[contains(@data-tracking-control-name,'org-employees_cta_face-pile-cta')]").text
                   numf = ''.join(i for i in str(numf) if i.isdigit() or i in '-./\\')
                   hml = driver.page_source
                   soup = BeautifulSoup(hml, 'lxml')
                   nums = soup.find("h3", {"class": 'top-card-layout__first-subline font-sans text-md leading-open text-color-text-low-emphasis'})
                   nums = ''.join(i for i in str(nums) if i.isdigit() or i in '-./\\').removeprefix("3----------/").removesuffix("/3")


                   for x in range(3, 0, -1):
                       try:
                           driver.switch_to.window(driver.window_handles[x])
                           driver.close()
                       except:
                           pass
                   dataToCsv = (urls, nome, nomempr, linkempr, tipcon, nivexp, numcont, datapos, horascrape, numf, nums, locemp, linkinsc, urn)
                   print(dataToCsv)


                   with open('Scraping - Guilherme Ramone Fontenele.csv', 'a', newline='', encoding='cp1252') as file:
                       writer = csv.writer(file)
                       writer.writerow(dataToCsv)


                   urls = nome = nomempr = linkempr = tipcon = nivexp = numcont = datapos = horascrape = numf = nums = locemp = linkinsc = urn = 0


               else:


                   for x in range(3, 0, -1):
                       try:
                           driver.switch_to.window(driver.window_handles[x])
                           driver.close()
                       except:
                           pass








                   continue


           except:


               for x in range(3, 0, -1):
                   try:
                       driver.switch_to.window(driver.window_handles[x])
                       driver.close()
                   except:
                       pass


               pass




   else:
       for x in range(3, 0, -1):
           try:
               driver.switch_to.window(driver.window_handles[x])
               driver.close()
           except:
               pass