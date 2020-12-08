from time import sleep

from selenium import webdriver

def ConnexionAdminGoListeCoiffeur():
    driver = webdriver.Chrome(executable_path='Driver\chromedriver.exe')
    driver.maximize_window()
    driver.get("https://esig-sandbox.ch/team20_5_v2/login")
#Entrer des coordonnées de l'admin
    #Entrer du mail
    eleMailAdmin = driver.find_element_by_name('mailconnection')
    eleMailAdmin.clear()
    eleMailAdmin.send_keys('elv-komivi.assm@eduge.ch')

    #Entrer du mot de passe
    eleMotdePasseAdmin = driver.find_element_by_name('mdpconnection')
    eleMotdePasseAdmin.clear()
    eleMotdePasseAdmin.send_keys('root')

    #Connexion
    eleSeConnecter = driver.find_element_by_id('formConnection')
    eleSeConnecter.click()

    #AllersurListeCoiffeur
    driver.get("https://esig-sandbox.ch/team20_5_v2/creercoiffeur")

    sleep(945984560)
    driver.close()


if __name__ == "__main__":
    ConnexionAdminGoListeCoiffeur()