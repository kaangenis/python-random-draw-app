from mainUi import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


emptyList = []
def scrapeData():
    driver = webdriver.Chrome()

    url = ui.lnedt_Post.text()
    driver.get(url)

    print("Sayfaya Erişildi.")
    time.sleep(5)

    stringSource = ['/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/h3/div/a']

    k = 0
    while k!= 20:
        for a in stringSource:
            val = a % k
            elements = driver.find_elements(By.XPATH, val)
            for b in elements:
                print(k, '-', b.text)
                ui.tablo_Katilimcilar.append(b.text)
                emptyList.append(b.text)

        k = k + 1

    print(emptyList)


def pickRandom():
    random.shuffle(emptyList)
    print(emptyList)
    result = random.choice(emptyList)
    print(result)
    ui.tablo_Kazananlar.append(result)
    """
    result = random.choice(emptyList)
    ui.tablo_Kazananlar.append(result)
    print(result)
    """



def clearAll():
    ui.tablo_Kazananlar.clear()
    ui.tablo_Katilimcilar.clear()
    ui.lnedt_Post.clear()


def closeApp():
    sys.exit(app.exec_())




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainApp()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.btn_KisileriCek.clicked.connect(scrapeData)
    ui.btn_Sonuclar.clicked.connect(pickRandom)
    ui.btn_Sifirla.clicked.connect(clearAll)
    ui.btn_Cikis.clicked.connect(closeApp)

    sys.exit(app.exec_())