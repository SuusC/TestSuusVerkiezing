import pandas as pd
import landelijke_uitslag
import provincie_stemmen

def provincie_als_landelijk(provincie):
    a = landelijke_uitslag.landelijke_uitslag(provincie_stemmen.provincie_stemmen(provincie))
    print(a)

provincie_als_landelijk('Limburg')