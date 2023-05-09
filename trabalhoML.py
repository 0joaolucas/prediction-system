# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:46:23 2023

@author: JotaL
"""

import pandas as pd 

import sklearn
import joblib
sklearn.__version__



joblib.__version__

import tkinter as tk


def show_entry_fields():
    X_test = pd.DataFrame(columns=['gender', 'lunch', 'test preparation course',
                                   'reading score', 'writing score', 'race/ethnicity_group A',
                                   'race/ethnicity_group B', 'race/ethnicity_group C',
                                   'race/ethnicity_group D', 'race/ethnicity_group E',
                                   "parental level of education_associate's degree",
                                   "parental level of education_bachelor's degree",
                                   'parental level of education_high school',
                                   "parental level of education_master's degree",
                                   'parental level of education_some college',
                                   'parental level of education_some high school'])
    try:
        p1 = float(e1.get())
        p2 = float(e2.get())
        p3 = float(e3.get())
        p4 = float(e4.get())
        p5 = float(e5.get())
        p6 = float(e6.get())
        p7 = float(e7.get())
        p8 = float(e8.get())
        p9 = float(e9.get())
        p10 = float(e10.get())
        p11 = float(e11.get())
        p12 = float(e12.get())
        p13 = float(e13.get())
        p14 = float(e14.get())
        p15 = float(e15.get())
        p16 = float(e16.get())

        data = {'gender': p1, 'lunch': p2, 'test preparation course': p3, 'reading score': p4,
                'writing score': p5, 'race/ethnicity_group A': p6, 'race/ethnicity_group B': p7,
                'race/ethnicity_group C': p8, 'race/ethnicity_group D': p9,
                'race/ethnicity_group E': p10,
                "parental level of education_associate's degree": p11,
                "parental level of education_bachelor's degree": p12,
                "parental level of education_high school": p13,
                "parental level of education_master's degree": p14,
                "parental level of education_some college": p15,
                "parental level of education_some high school": p16}

        X_test = pd.concat([X_test, pd.DataFrame(data, index=[0])], ignore_index=True)

    except EOFError:
        print("Erro: arquivo vazio ou final do arquivo atingido antes do esperado.")



    import joblib
    filename = 'modelo.pkl'
    loaded_model = joblib.load(filename)

# Agora você pode usar o modelo carregado para fazer previsões em novos dados
    result = loaded_model.predict(X_test)
    
      
    
    tk.Label(master, text=result).grid(row=18)

master = tk.Tk()
master.title("Student Perfomance Prediction System")

label = tk.Label(master, text = 'Student Perfomance Prediction System', bg = 'black', fg = 'white').grid(row=0, columnspan=2)

tk.Label(master, text = 'Digite o código do sexo (0-female, 1-male)                            ').grid(row=1)
tk.Label(master, text = 'Digite o código do lanche (0-free/reduced, 1-standard                 ').grid(row=2)
tk.Label(master, text = 'Digite o código do curso de preparação para teste (0-completed, 1-none').grid(row=3)
tk.Label(master, text = 'Digite sua nota de leitura(reading score)                             ').grid(row=4)
tk.Label(master, text = 'Digite sua nota de escrita(writing score)                             ').grid(row=5)
tk.Label(master, text = 'raça(ethinicity group A) (0-Não , 1-Sim)                              ').grid(row=6)
tk.Label(master, text = 'raça(ethinicity group B) (0-Não , 1-Sim)                              ').grid(row=7)
tk.Label(master, text = 'raça(ethinicity group C) (0-Não , 1-Sim)                              ').grid(row=8)
tk.Label(master, text = 'raça(ethinicity group D) (0-Não , 1-Sim)                              ').grid(row=9)
tk.Label(master, text = 'raça(ethinicity group E) (0-Não , 1-Sim)                              ').grid(row=10)
tk.Label(master, text = 'Nível de educação dos pais - curso técnico superior (0-Não, 1-Sim)    ').grid(row=11)
tk.Label(master, text = 'Nível de educação dos pais - bacharelado (0-Não, 1-Sim)               ').grid(row=12)
tk.Label(master, text = 'Nível de educação dos pais - ensino médio (0-Não, 1-Sim)              ').grid(row=13)
tk.Label(master, text = 'Nível de educação dos pais - mestrado (0-Não, 1-Sim)                  ').grid(row=14)
tk.Label(master, text = 'Nível de educação dos pais - graduação inacabado  (0-Não, 1-Sim)      ').grid(row=15)
tk.Label(master, text = 'Nível de educação dos pais - ensino médio inacabado (0-Não, 1-Sim)    ').grid(row=16)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)
e7 = tk.Entry(master)
e8 = tk.Entry(master)
e9 = tk.Entry(master)
e10 = tk.Entry(master)
e11 = tk.Entry(master)
e12 = tk.Entry(master)
e13 = tk.Entry(master)
e14 = tk.Entry(master)
e15 = tk.Entry(master)
e16 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)
e10.grid(row=10, column=1)
e11.grid(row=11, column=1)
e12.grid(row=12, column=1)
e13.grid(row=13, column=1)
e14.grid(row=14, column=1)
e15.grid(row=15, column=1)
e16.grid(row=16, column=1)

tk.Button(master, text='Predição', command=show_entry_fields).grid()

tk.mainloop()