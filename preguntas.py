"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    num_filas = len(tbl0)
    return int(num_filas)


def pregunta_02():
    num_columnas = len(tbl0.columns)
    return int(num_columnas)


def pregunta_03():
    conteo_por_letra = tbl0["_c1"].value_counts().sort_index()
    return conteo_por_letra


def pregunta_04():
    promedios = tbl0.groupby("_c1")["_c2"].mean()
    return promedios


def pregunta_05():
    max = tbl0.groupby("_c1")["_c2"].max()
    return max


def pregunta_06():
    unicoc4 = sorted(tbl1["_c4"].str.upper().unique().tolist())
    return unicoc4


def pregunta_07():
    suma = tbl0.groupby("_c1")["_c2"].sum()
    return suma


def pregunta_08():
    tbl0n = tbl0.assign(suma=tbl0["_c0"] + tbl0["_c2"])
    return tbl0n


def pregunta_09():
    tbl0["year"] = pd.to_datetime(tbl0["_c3"], errors='coerce').dt.year.fillna(1999).astype(int).astype(str)
    return tbl0


def pregunta_10():
    tbl0_agrupado= tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(sorted(x.astype(str)))).reset_index()
    tbl0_agrupado["_c1"] = tbl0_agrupado["_c1"].astype(str)
    tbl0_agrupado.set_index("_c1", inplace=True)
    tbl0_agrupado.index.name = "_c0"
    return tbl0_agrupado


def pregunta_11():
    tbl1_agrupado = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(sorted(x))).reset_index()
    tbl1_agrupado.columns = ["_c0", "_c4"]
    return tbl1_agrupado


def pregunta_12():
    tbl2 = pd.read_csv("tbl2.tsv", sep='\t')
    tbl2['_c5'] = tbl2['_c5a'] + ':' + tbl2['_c5b'].astype(str)
    tbl2_agrupado = tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    tbl2_agrupado['_c5'] = tbl2_agrupado['_c5'].astype(str)
    tbl2_agrupado.columns = ['_c0', '_c5']
    return tbl2_agrupado


def pregunta_13():
    tbl_join = pd.merge(tbl0, tbl2, on="_c0")
    suma = tbl_join.groupby("_c1")["_c5b"].sum()
    suma.index.name = "_c1"
    suma.name = "_c5b" 
    return suma
