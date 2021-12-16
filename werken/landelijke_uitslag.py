import pandas as pd
def landelijke_uitslag(uitslagenDF):
    """
    Bereken de landelijke uitslag van de Tweede Kamerverkiezingen in het aantal
    stemmen dat iedere partij heeft gekregen, en de zetels die dat oplevert.
    Return dataframe met de uitslagen.
    """
    aantal_zetels = 150
    totaal_stemmen = uitslagenDF['GeldigeStemmen'].sum()
    kiesdeler = int(totaal_stemmen / aantal_zetels + 0.5)

    zetelsDF = pd.DataFrame(columns=['stemmen', 'zetels'],
                            index=uitslagenDF.columns[10:])

    # Bereken het aantal stemmen en volledige zetels voor elke partij
    for partij in uitslagenDF.columns[10:]:
        partij_stemmen = int(uitslagenDF[partij].sum())
        zetelsDF.loc[partij, 'stemmen'] = partij_stemmen

        aantal_volle_zetels = int(partij_stemmen / kiesdeler)
        zetelsDF.loc[partij, 'zetels'] = aantal_volle_zetels

    # Haal de partijen die niet minstens 1 volledige zetel hebben gehaald uit het primaire DF,
    # zodat ze niet meegaan in de berekening van de restzetels. Sla ze op in hun eigen DF.
    idx_partijen_zonder_zetels = zetelsDF[zetelsDF['zetels'] == 0].index
    partijen_zonder_zetels = zetelsDF.loc[idx_partijen_zonder_zetels]
    zetelsDF = zetelsDF.drop(idx_partijen_zonder_zetels)

    zetelsDF.insert(2, 'stemmen per zetel', [0] * len(zetelsDF.index))

    # Toekenning restzetels
    restzetels = 150 - zetelsDF['zetels'].sum()
    zetelsDF['stemmen per zetel'] = zetelsDF['stemmen'] / (zetelsDF['zetels'] + 1)
    zetelsDF['stemmen per zetel'] = pd.to_numeric(zetelsDF['stemmen per zetel'])

    while restzetels > 0:
        i_max = zetelsDF['stemmen per zetel'].idxmax()  # index (partijnaam) van hoogste aantal stemmen per zetel
        zetelsDF.loc[i_max, 'zetels'] += 1
        zetelsDF.loc[i_max, 'stemmen per zetel'] = zetelsDF.loc[i_max, 'stemmen'] / (zetelsDF.loc[i_max, 'zetels'] + 1)
        restzetels -= 1

    zetelsDF = zetelsDF.drop('stemmen per zetel', axis=1)
    zetelsDF = pd.concat([zetelsDF, partijen_zonder_zetels])

    return zetelsDF