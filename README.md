# Convertidor de Excel a JSON

Este proyecto contiene un script de Python que transforma un archivo Excel (.xlsx) en un archivo JSON. El script está diseñado para ser utilizado en aplicaciones web que necesitan consumir datos en formato JSON, como proyectos desarrollados con React.

## Requisitos

Antes de ejecutar el script, necesitas tener instalado Python y algunas bibliotecas adicionales. Asegúrate de que tu entorno cumpla con los siguientes requisitos:

- Python 3.x
- Pandas
- OpenPyXL

Puedes instalar las dependencias necesarias con el siguiente comando:

\```bash
pip install pandas openpyxl
\```

## Cómo Usar

Para convertir un archivo Excel en un archivo JSON, sigue estos pasos:

1. **Coloca tu archivo Excel** en el mismo directorio que el script `convert_to_json.py`. Asegúrate de que el archivo se llame `Lista de productos (db).xlsx`.

2. **Abre una terminal o línea de comandos** y navega hasta el directorio donde se encuentra el script.

3. **Ejecuta el siguiente comando**:

\```bash
python3 convert_to_json.py
\```

4. **Revisa el archivo generado** `productos.json` en el mismo directorio para verificar que los datos se han convertido correctamente.

## Formato del Archivo JSON

El archivo JSON generado estará formateado como un array de objetos, donde cada objeto representa un registro del archivo Excel. Este formato es ideal para ser consumido directamente por aplicaciones que utilizan frameworks de JavaScript como React.

## Problemas Comunes y Soluciones

- **Problema de comando Python no encontrado**: Si encuentras errores donde el comando `python` o `python3` no es reconocido, asegúrate de que Python esté correctamente instalado y configurado en tu variable de entorno PATH.

- **Caracteres especiales en el JSON**: Si los caracteres especiales o URLs no se muestran correctamente, verifica que estés utilizando `ensure_ascii=False` en el script de conversión.

---