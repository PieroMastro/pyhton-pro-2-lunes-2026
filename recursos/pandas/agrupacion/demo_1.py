import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# 1. ¿Cuántas aplicaciones hay en la 'Category' 'BUSINESS'?
business_count = df[df['Category'] == 'BUSINESS'].shape
# Alternativa con value_counts(): df['Category'].value_counts().get('BUSINESS', 0)
print("1. Apps en BUSINESS:", business_count)

# 2. ¿Cuál es la relación de aplicaciones para adolescentes ('Teen') y las destinadas para niños mayores de 10 años ('Everyone 10+')?
# Redondee la respuesta a la centésima más cercana.
teen_count = df[df['Content Rating'] == 'Teen'].shape[0]
everyone_10_count = df[df['Content Rating'] == 'Everyone 10+'].shape[0]
ratio_teen_e10 = round(teen_count / everyone_10_count, 2)
print("2. Relación Teen / Everyone 10+:", ratio_teen_e10)

# 3.1 ¿Cuál es el 'Rating' promedio de aplicaciones 'Paid'?
# Redondee la respuesta a la centésima más cercana.
paid_mean_rating = df[df['Type'] == 'Paid']['Rating'].mean()
print("3.1 Rating promedio Paid:", round(paid_mean_rating, 2))

# 3.2 ¿Cuánto más bajo es el 'Rating' promedio de aplicaciones 'Free' que el promedio de valoración de las aplicaciones 'Paid'?
# Redondee la respuesta a la centésima más cercana.
free_mean_rating = df[df['Type'] == 'Free']['Rating'].mean()
diff_rating = round(paid_mean_rating - free_mean_rating, 2)
print("3.2 Diferencia (Paid - Free):", diff_rating)

# 4. ¿Cuál es el 'Size' (tamaño) mínimo y máximo en la 'Category' 'COMICS'?
# Redondee la respuesta a la centésima más cercana.
comics_size = df[df['Category'] == 'COMICS']['Size']
min_size = round(comics_size.min(), 2)
max_size = round(comics_size.max(), 2)
print(f"4. Size en COMICS -> Mínimo: {min_size} | Máximo: {max_size}")

# Bonificación 1. ¿Cuántas aplicaciones tienen un 'Rating' estrictamente superior a 4.5 en la 'Category' 'FINANCE'?
finance_high_rating = df[(df['Category'] == 'FINANCE')
                         & (df['Rating'] > 4.5)].shape[0]
print("Bonificación 1. Apps en FINANCE con Rating > 4.5:", finance_high_rating)

# Bonificación 2. ¿Cuál es la relación de juegos 'Free' y 'Paid' con un 'Rating' superior a 4.9?
games_top = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]
free_games_top = games_top[games_top['Type'] == 'Free'].shape[0]
paid_games_top = games_top[games_top['Type'] == 'Paid'].shape[0]

ratio_games = round(free_games_top / paid_games_top,
                    2) if paid_games_top > 0 else "Infinito (0 Paid)"
print(
    f"Bonificación 2. Juegos Free ({free_games_top}) vs Paid ({paid_games_top}) con Rating > 4.9 -> Relación: {ratio_games}")
