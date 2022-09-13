import pandas as pd
import os
import re
from flask_app.models.product import Product
from tqdm import tqdm


dir_root = os.getcwd()
lista_precios_auto = pd.read_excel(os.path.join(dir_root, 'data\\Di_Lista Precios Mayo 23 2022 clientes.xlsx'))
lista_precios_lv = pd.read_excel(os.path.join(dir_root, 'data\\Lista de Precios SI EP_FY22 JUNIO.xlsx'), sheet_name='Lista de Precios EP FY22')

print(lista_precios_auto.shape, lista_precios_lv.shape)
print(lista_precios_auto.head())
print(lista_precios_lv.head())
print(lista_precios_auto.columns)

lista_precios_auto['descripcion'] = lista_precios_auto.Beschreibung.apply(lambda x: re.findall(r"(?:.*)\\(.*)",x)[0])
lista_precios_auto['fabricante_id'] = int(1)
lista_precios_lv['fabricante_id'] = int(1)
lista_precios_auto['empresa_id'] = int(2)
lista_precios_lv['empresa_id'] = int(2)
lista_precios_auto['stock'] = int(100)
lista_precios_lv['stock'] = int(100)
lista_precios_auto.rename(columns={'MLFB Print with opcion':'codigo_fabricante',
                                   'Precio may - Jun 2022':'precio'}, inplace=True)
lista_precios_lv.rename(columns={'MLFB':'codigo_fabricante',
                                 'PVP FY22_JUNIO':'precio'}, inplace=True)
productos = pd.merge(lista_precios_auto, lista_precios_lv, on=['codigo_fabricante', 'precio', 'stock', 'empresa_id', 'fabricante_id'], how='outer')
print(productos.shape, lista_precios_auto.shape, lista_precios_lv.shape)
print(productos.columns)
productos['product_type_id'] = None
productos.product_type_id[productos.codigo_fabricante.str.contains('6SL|6SE')] = 2
productos.product_type_id[productos.codigo_fabricante.str.contains('3RT|3RV|3RU')] = 1
productos.product_type_id[productos.codigo_fabricante.str.contains('3VM|3VA|3WT')] = 4
productos.product_type_id[productos.codigo_fabricante.str.contains('6ED|6ES7|6AV')] = 3
print(productos.columns)
# productos_out = productos.dropna()
productos_out = productos[['codigo_fabricante', 'descripcion', 'precio', 'stock', 'product_type_id', 'fabricante_id', 'empresa_id']]
productos_out = productos_out[~productos_out.product_type_id.isna()]
print(productos_out.shape)
print(productos_out.head())

data = {}

for i in tqdm(range(len(productos_out))):
    for col in productos_out.columns:
        data[col] = productos_out[col].iloc[i]
    Product.save(data)        

