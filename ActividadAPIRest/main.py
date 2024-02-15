import json
import pandas as pd
from datetime import datetime

def Empleados(empleados):
    fechaActual = datetime.now()
    mesAno = fechaActual.strftime("%b-%Y")

    df = pd.DataFrame(empleados)

    df['salary'] = df['salary'].replace(r'[\$,]', '', regex=True).astype(float)

    df['salary'] = df.apply(lambda row: f"{row['salary'] * 1.1:.2f}€" if row['age'] < 30 else f"{row['salary']:.2f}€", axis=1)
    df = df[df['proyect'] != 'GRONK']

    excelNombre = f"pagos-empleados-{mesAno}.xlsx"
    df.to_excel(excelNombre, index=False)

    print(f"Archivo Excel '{excelNombre}' creado con éxito.")

if __name__ == "__main__":

    with open('empleados.json', 'r') as file:
        empleados = json.load(file)


    Empleados(empleados)