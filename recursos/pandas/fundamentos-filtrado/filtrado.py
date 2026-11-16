import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# ¿Cuál es el precio de la aplicación de pago más barata (tipo == 'Pagada')?
df[df['Type'] == 'Paid']['Price'].min()


# ¿Cuál es el número medio de instalaciones para las aplicaciones de la categoría "ART_AND_DESIGN"?
df[df['Category'] == 'ART_AND_DESIGN']['Installs'].mean()


# ¿Cuánto más es el número máximo de Reseñas para aplicaciones gratuitas (tipo == 'Gratis') que el número máximo de Reseñas para aplicaciones pagas (Tipo == 'Pagado')?
max_free = df[df['Type'] == 'Free']['Reviews'].max()
max_paid = df[df['Type'] == 'Paid']['Reviews'].max()
diferencia = max_free - max_paid


# ¿Cuál es el tamaño mínimo de una aplicación para adolescentes (Clasificación de contenido == 'Adolescente')?
df[df['Content Rating'] == 'Teen']['Size'].min()


# * ¿Cuál es la categoría de una aplicación que tiene la mayor cantidad de reseñas?
df[df['Reviews'] == df['Reviews'].max()]['Category']


# * ¿Cuál es la calificación media de las aplicaciones cuyo precio supera los $ 20 y el número de instalaciones es superior a 10,000?
filtro = (df['Price'] > 20) & (df['Installs'] > 10000)
df[filtro]['Rating'].mean()
