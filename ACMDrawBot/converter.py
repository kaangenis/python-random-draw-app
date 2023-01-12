from PyQt5 import uic

with open('mainUi.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('main.ui', fout)