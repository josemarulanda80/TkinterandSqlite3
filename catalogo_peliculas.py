# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 14:02:03 2022

@author: josem
"""

import tkinter as tk
from client.gui_app import Frame,barra_menu
def main():
    root=tk.Tk()
    root.title('Catalogo de peliculas')
    #Icono
    root.iconbitmap('img/logo.ico')
    root.resizable(0,0)
    #Crear barra de menú
    barra_menu(root)
    #configurar tamaño de la pantalla
    app=Frame(root=root)

    app.mainloop()

if __name__ == '__main__':
    main()
    
    