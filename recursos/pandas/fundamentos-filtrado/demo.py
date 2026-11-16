import pandas as pd

# Cargar el marco de datos
df = pd.read_csv('GoogleApps.csv')


# ¿Cuál es el nombre de la primera aplicación en el conjunto de datos?
df['App'].head(1)
# alternativa: df.iloc[0]['App']


# ¿A qué categoría pertenece la última aplicación del conjunto de datos?
df['Category'].tail(1)
# alternativa: df.iloc[-1]['Category']


# ¿Cuántas columnas hay en el conjunto de datos?
df.shape[1]
# alternativa: len(df.columns)


# ¿Qué tipo de datos se almacenan en cada una de las columnas?
df.info()
# alternativa: df.dtypes


# Especifique la media aritmética y la mediana del tamaño de la aplicación (Size)
media_size = df['Size'].mean()
mediana_size = df['Size'].median()


# ¿Cuánto cuesta la aplicación más cara?
df['Price'].max()


# * Especifique la media aritmética y la mediana del número de instalaciones de aplicaciones (Installs)
media_installs = df['Installs'].mean()
mediana_installs = df['Installs'].median()
