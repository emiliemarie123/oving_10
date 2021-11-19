# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:19:16 2021

@author: Emilie Marie
"""

import unittest

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.quiz = Quiz("TestSpørmål 1",["Alt1","Alt2"], 1)
        
    def test_sjekk_feil_svar(self):
        self.assertFalse(self.quiz.sjekk_svar(1))
    
    def test_sjekk_riktig_svar(self):
        self.assertTrue(self.quiz.sjekk_svar(2))
    
    def test_korrekt_svar_tekst_riktig(self):
        self.assertEqual(self.quiz.korrekt_svar_tekst(), "Alt2")
    
    def test_korrekt_svar_tekst_feil(self):
        self.assertNotEqual(self.quiz.korrekt_svar_tekst(), "Alt1")
            

#Innhold fra Øving 9 Start

#self for å rope på variabler 

class Quiz: #grunnmur
    
    def __init__(self, spørsmål, alternativ, svar = 0): #init = hovedbrikker (spørsmål, alternativ, svar)
        self.spørsmål = spørsmål
        self.alternativ = alternativ
        self.svar = svar #ikke starte på 0
        
    def __str__(self): #skrive ut class
        utskrift = self.spørsmål + "\n" 
        for index, verdi in enumerate(self.alternativ): #index, verdi i en liste
            utskrift += f"{index + 1}) {verdi}\n" #alternativene (index + verdi)
        return utskrift # gi utskrift
    
    def sjekk_svar(self, riktig_svar):
        if riktig_svar - 1 == self.svar:
            return True
        else: 
            return False
        
    def korrekt_svar_tekst(self):
        korrekt_svar = self.alternativ[self.svar]
        return korrekt_svar
    

spiller_1_poeng = []
spiller_2_poeng = []
    

def start_spill(spillere):
    with open ("sporsmaalsfil.txt", "r", encoding="UTF8") as fil:
        for linje in fil:
            linje = linje.split(":")
            alternativ = linje[2].replace("[", " ").replace("]", " ")   
            quiz_spørsmål = Quiz(linje[0],alternativ.split(","),int(linje[1]))
            print(quiz_spørsmål)
            
                        
            for spiller in spillere:
                svar = int(input("Skriv inn svaret til "+spiller.navn+": "))
                if quiz_spørsmål.sjekk_svar(svar):
                    print("\n"+spiller.navn+": Korrekt")
                    spiller.poengsum += 1
                else:
                    print("\n"+spiller.navn+": Feil")
            
   
            input("Trykk enter for å fortsette\n")
        
        vinner = max(spillere, key=lambda spiller: spiller.poengsum)
        print("Spilleren med flest poeng og som vant \"Heile sjiden\" er: "+vinner.navn)
            
        
        


#Innhold fra øving 9 slutt.

        
class Spiller:
    #konstruktør
    def __init__(self, navn, poengsum = 0):
        self.navn = navn
        self.poengsum = poengsum


def main():        
    spillere = lag_spillere()
    print("Starter spill med:")
    for spiller in spillere:
        print("Navn: "+spiller.navn+" Poengsum: "+str(spiller.poengsum))
        
    start_spill(spillere)
    

def lag_spillere():
    antall = int(input("Legg inn antall spillere: "))
    spiller_liste = []
    for nr in range(antall):
        name = input("Navn på spiller "+ str(nr+1) +":")
        spiller_liste.append(Spiller(name))
        
    return spiller_liste


def kjor_unittest():
    tests = unittest.TestLoader().loadTestsFromTestCase(TestQuiz)
    unittest.TextTestRunner(verbosity = 2).run(tests)


if __name__ == "__main__":
    kjor_unittest()
    main()    




    
    