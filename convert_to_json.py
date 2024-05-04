import pandas as pd
import json

def excel_to_json(excel_file_path, json_file_path):
    # Leer el archivo Excel
    df = pd.read_excel(excel_file_path)
    
    # Convertir el DataFrame a una lista
    records = df.to_dict(orient='records')
    
    # Convertir la lista a JSON
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=4)

# Función para convertir un archivo en específico
excel_to_json('Lista de productos (db).xlsx', 'productos.json')
