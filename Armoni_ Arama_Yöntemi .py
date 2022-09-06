#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:58:32 2022

@author: barisbalci
"""

import math
import numpy as np
from random import random
.....

#İTERASYON SÜRECİ
for dongu in range(0,durma_kriteri):
    if HMRS>random():
        
#RASTGELE YENİ NOTALARIN ÜRETİLMESİ

    for armoni in range(0,HMS):
        X1new=X1min+random()*(X1maks-X1min)
        X2new=X2min+random()*(X2maks-X2min)
......

else:
    
#HAFIZAYA BAĞLI OLARAK NOTALARIN BİR PERDEDEN ÇALINMASI
        for armoni in range(0,HMS):
            
#OPT:BAşlangıç çözüm matrisi(Armoni belleği)
#OPT(1,k): 1. tasarım değişkeninin başlangıç çözüm matrisinden rassal olarak belirlenen k.armonideki (vektör) değeri
#OPT(2,k): 2. tasatım değişkeninin başlangıç çözüm matrisinden rassal olarak belirlenen k.armonideki(vektör) değeri
      
        k=math.ceil(random()*HMS)
        X1new = OPT[0][k]+(random()-0.5)*PAR*(X1maks-X1min)
        X2new = OPT[0][k]+(random()-0.5)*PAR*(X2maks-X2min)
    
#iterasyon sonu
#deger : tüm sonucunda elde edilen en iyi çözümin amaç fonksiyonu değeri
#sıra: güncellenen OPT matrisinde bu çözümün yer aldığı vektör 

deger=min(OPT[AF][:])
sıra=np.argmin(OPT[AF])
