# Bibliotecas
import io
import metpy
import requests
import numpy as np
import pandas as pd
from PIL import Image
from metpy.io.metar import *
from datetime import timedelta, datetime

def paint_airport(image, lat_airport, lon_airport):

    # Mapas de latitude e longitude do Brasil
    lat_map = np.linspace(-33.750812, 5.235216, 888)
    lon_map = np.linspace(-73.981645, -34.792202, 912)

    # Posicao do aeroporto na imagem
    lat_result = np.abs(lat_map - lat_airport).argmin()
    lon_result = np.abs(lon_map - lon_airport).argmin()

    # Ajuste da latitude
    lat_result = 888 - lat_result

    # Pinta a imagem
    image[lat_result - 10 : lat_result + 10, lon_result - 10 : lon_result + 10 , :] = [148,0,211] # Roxo

    return image

def get_image(url_img: str):

    # Download do binário da imagem
    bin_img = requests.get(url_img).content

    # Lê o binário como stream
    imageStream = io.BytesIO(bin_img)

    # Abre a imagem com PIL
    imageFile = Image.open(imageStream)
    
    # Corta a imagem para apresentar apenas o Brasil
    w = imageFile.width
    h = imageFile.height
    img_brasil = imageFile.crop((1030, 820, w-250, h-620))

    # Converte para numpy (Matrizes RGB)
    img_final = np.array(img_brasil)
    
    return img_final

# Funcao para ajustar dados meteorologicos com falta de informacao temporal
def metar_fix(txt):
    txt = str(txt)
    if txt != None and txt != 'nan':  
        first_position = txt.find('SB')
        second_position = txt[first_position+5:].find(' ')
        final_position = first_position+5+second_position
        if txt[final_position-1] != 'Z':
            txt = txt[:final_position] + 'Z' + txt[final_position:]
        return txt
    

# Conversao do informe metar para uma tabela de dados
def convert_metar(df_met):
    df_final = pd.DataFrame()
    for i, row in df_met.iterrows():
        met, date = row['metar'], row['data_ref']
        try:
            aux = parse_metar_to_dataframe(met, year=int(date[:4]), month=int(date[5:7]))
            # aux.drop('station_id', axis=1, inplace=True)
            # aux.reset_index(inplace=True)
            aux.dropna(axis=0, how='all', inplace=True)
            if aux is not None:
                aux['meta'] = met
                aux['date'] = date
                # return aux
                df_final = pd.concat([df_final, aux])
        except: 
            print(met, date)
            break
    return df_final