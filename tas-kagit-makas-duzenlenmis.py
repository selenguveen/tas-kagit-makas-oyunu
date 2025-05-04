#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 13:51:07 2025

@author: selenguven
"""

#TAS-KAĞIT-MAKAS
import random
def tas_kagit_makas():
    while True: 
        oyuncu_skor = 0
        bilgisayar_skor = 0
        while oyuncu_skor < 3 and bilgisayar_skor < 3:
            secenekler = ["taş", "kağıt", "makas"]
            kullanici_secimi = input("taş, kağıt, makas seçiniz.").lower()
        
            if kullanici_secimi not in secenekler:
                print("Geçersiz İşlem")
                continue
    
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın Seçimi: ", bilgisayar_secimi)
    
            if kullanici_secimi == bilgisayar_secimi:
                print("Berabere.")
        
            elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (kullanici_secimi ==  "makas" and bilgisayar_secimi == "kağıt") or \
                 (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print ("KAZANDINIZ!!")
                oyuncu_skor += 1
            else:
                print("Kaybettiniz, üzgünüm.")
                bilgisayar_skor += 1
            print (f"Skor --> Oyuncu: {oyuncu_skor} - Bilgisayar: {bilgisayar_skor}")
        if oyuncu_skor == 3:
            print("Tebrikler! Oyunu Kazandınız.")
        else: 
            print("Bilgisayar Kazandı!")
    
        devam = input("Devam etmek ister misiniz? (e/h)").lower()
        if devam == "h":
            print("Oyun Bitti.")
            break
        
def menu():
    while True:
        print("\n🎮 TAŞ KAĞIT MAKAS OYUNU 🎮")
        print("1 --> Oyuna Başla")
        print("2 --> Oyundan Çık")
        secim = input("Seçiniz: (1/2)")
        if secim == "1":
            tas_kagit_makas()
        elif secim == "2":
            print("Çıkış Yapılıyor...")
            break
        else:
            print("Yanlış Seçim Yaptınız. Tekrar Seçiniz.")
menu()
