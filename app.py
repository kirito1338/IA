from datetime import date
import streamlit as st
from PIL import Image
import pandas as pd
import scipy as sc
import seaborn as snb
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

try:
    fichier = 'BeansDataSet.csv'
    data = pd.read_csv(fichier)
except:
    st.error('Erreur de lecture du fichier')

st.sidebar.title('Navigation')
menu = st.sidebar.selectbox('Choisir un volet', ['Accueil', 'Apercu des donnees', 'Correlation', 'Visualisation', 'Rapport'])

if menu == 'Accueil':
    st.markdown("""
        <div style='text-align:center;'>
        <h1> Analyse des ventes par region </h1>
        </div>
        """, unsafe_allow_html=True)
    st.subheader('Apercu des donnees')
    st.dataframe(data)

elif menu == 'Apercu des donnees':
    st.header('Apercu des donnees')
    st.subheader('Premieres 10 lignes')
    st.dataframe(data.head(10))
    
    st.subheader('Dernieres 10 lignes')
    st.dataframe(data.tail(10))
    
    st.subheader('Statistiques descriptives')
    st.write(data.describe())
    
    st.subheader('Transactions par region')
    region_counts = data['Region'].value_counts()
    st.write(region_counts)
    
    st.subheader("Moyenne des ventes par region")

    mean_sales = data.groupby('Region').mean(numeric_only=True)
    st.write(mean_sales)

    st.subheader('Somme des ventes par region')

    sum_sales = data.groupby('Region').sum(numeric_only=True)
    st.write(sum_sales)

elif menu == 'Correlation':
    st.header('Etude de correlation')
    
    st.subheader('Matrice de Correlation')
    
    st.subheader('Tableau de correlation')
    st.write(data.corr(numeric_only=True))
    figure_corr, ax_corr = plt.subplots(figsize=(15, 15))
    snb.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f', ax=ax_corr)
    st.pyplot(figure_corr)

elif menu == 'Visualisation':
    st.header('Visualisation des ventes')
        
    st.subheader('Histogrammes')
    data.hist(figsize=(12, 8), bins=20)
    st.pyplot(plt.gcf())
    
    st.subheader('Ventes moyennes par region')
    fig1, ax1 = plt.subplots(figsize=(9, 6))
    mean_sales = data.groupby('Region').mean(numeric_only=True)
    mean_sales.reset_index().plot(x='Region', kind='bar', ax=ax1, title="Moyenne des ventes par region")
    st.pyplot(fig1)
    
    st.subheader('Ventes totales par region')
    fig2, ax2 = plt.subplots(figsize=(9, 6))
    sum_sales = data.groupby('Region').sum(numeric_only=True)
    sum_sales.reset_index().plot(x='Region', kind='bar', ax=ax2, title="Somme des ventes par region")
    st.pyplot(fig2)
    
    st.subheader('Densite des ventes')
    data.plot(kind='density', subplots=True, figsize=(12, 8))
    st.pyplot(plt.gcf())
    
    st.subheader('Boites a moustaches')
    data.plot(kind='box', subplots=True, figsize=(12, 8))
    st.pyplot(plt.gcf())
    
    st.subheader("Repartition des ventes pour une region")
    fig_pie, ax_pie = plt.subplots()
    data['Region'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax_pie)
    ax_pie.set_ylabel('')
    st.pyplot(fig_pie)

    st.subheader('Repartition des ventes de chaque region')

    sum_sales = data.groupby('Region').sum(numeric_only=True)
    for region in sum_sales.index:
            fig, ax = plt.subplots()
            sum_sales.loc[region].plot(kind='pie', autopct='%1.1f%%', startangle=90, ax=ax, title=f"Ventes pour {region}")
            ax.set_ylabel('')
            st.pyplot(fig)
    
    st.subheader('Matrice de dispersion')
    scatter_matrix(data, figsize=(12, 12))
    st.pyplot(plt.gcf())
    
    st.subheader('Pairplot')
    
    graphe = snb.pairplot(data, hue='Region')
    st.pyplot(graphe.fig)

else:
    st.title("Rapport d'analyse des ventes")
    st.write("Les donnees montrent que Robusta et Arabica dominent largement les ventes, representant respectivement jusqu'a"
    " 30 000 unite pour Robusta et 35 000 unite pour Arabica dans les periodes de forte demande. En revanche, des produits comme"
    " Cappuccino et Lungo connaissent des ventes bien plus faibles, avec des chiffres oscillant autour de 1 000 a 3 000 unite. "
    "Les ventes en ligne surpassent celles des magasins physiques, les produits en ligne representant plus de 80% du total des ventes."
    " Les ventes dans la region South sont nettement plus importantes que dans le North, ou les volumes de vente sont environ 2 a 3 fois"
    " moins eleves. Par exemple, dans le South, Robusta et Arabica enregistrent des volumes de vente allant jusqu'a 50 000 unite combinees,"
    " tandis que dans le North, ces chiffres n'excedent pas 15 000 unite. Les pics de vente pour Robusta et Arabica peuvent atteindre plus"
    " de 30 000 unite sur certaines periodes, tandis que les ventes de Cappuccino dans la region South ne depassent generalement pas 2 000 unite."
    " Il est recommande de renforcer les strategies marketing pour promouvoir les produits phares comme Robusta et Arabica,"
    " et d'explorer des actions pour dynamiser les ventes de Cappuccino et Lungo, notamment dans les magasins physiques.")
    st.title("Rapport de recommandations")
    st.write("Il est recommande de concentrer les efforts marketing sur les produits phares tels que Robusta et Arabica,"
    " qui dominent les ventes, avec des volumes atteignant jusqu'a 30 000 a 35 000 unite. Des promotions ciblees en ligne et en magasin,"
    " ainsi que des campagnes publicitaires, devraient etre mises en place pour stimuler encore la demande. Par ailleurs,"
    " bien que les ventes en ligne representent plus de 80% du total des ventes,"
    " il est crucial de dynamiser les ventes en magasin en proposant des offres speciaux et des evenements."
    " Les produits moins populaires, comme Cappuccino et Lungo, pourraient beneficier de promotions pour stimuler leur demande."
    " Une analyse plus approfondie des tendances saisonnieres et des evenements speciaux permettrait d’anticiper les pics de vente"
    " et d'optimiser les strategies de marketing en consequence. Il serait egalement benefique d'ameliorer l'approvisionnement et"
    " la distribution pour repondre a la demande accrue des produits populaires, en particulier pendant les periodes de forte demande.")
