import streamlit as st
import numpy as np
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import base64
import os
import time
from translation import texte, t


#region Language selection

if not "language" in st.session_state:
    st.session_state["language"] = "fr"

with st.sidebar:
    language_selected = st.radio("**Language**", ["Français 🇫🇷", "English 🇺🇸"])

if language_selected == "Français 🇫🇷":
    st.session_state["language"] = "fr"
else:
    st.session_state["language"] = "en"

# endregion


#region ---Config de la page----

st.set_page_config(page_title="Interactive theme park queue", layout = "wide")

st.header(t("title"), text_alignment = "center")
st.subheader(t("header"), text_alignment = "center", help = "Let's gooo ! 🚀🎢")
st.write("")


#Expander méthodo/aide
col1, col2 = st.columns(2)

with col1:
    expander1 = st.expander(label = t("label_methodo")) #t for the def traduction in translation
    expander1.write(t("text_methodo"))
    
with col2:
    expander2 = st.expander(label = t("label_help"))
    expander2.write(t("text_help"))

st.divider()

#region Initialisation des variables session_state

if "calculer" not in st.session_state:
    st.session_state["calculer"] = None
if "moyenne" not in st.session_state:
    st.session_state["moyenne"] = None
if "liste_moyenne" not in st.session_state:
    st.session_state["liste_attente"] = []
if "rho" not in st.session_state:
    st.session_state["rho"] = 0
if "expert" not in st.session_state:
    st.session_state.expert = False

# endregion

#region Data Editor / Mode expert / Panne

#Selectbox
liste_frequentation = t("liste_freq")
liste_frequentation_expert = t("liste_freq_expert")

if not st.session_state.expert:
    choix_data = st.selectbox(t("selectbox"), 
                            options = liste_frequentation, 
                            width = 450,
                            key = "select_normal")
    if liste_frequentation.index(choix_data) == 0:
        df_lambda = 800
        df_h_ouverture = 8
        df_nombre_train = 40
        df_nombre_wagon = 5
        df_nombre_visiteur_wagon = 10
    if liste_frequentation.index(choix_data) == 1:
        df_lambda = 1300
        df_h_ouverture = 8
        df_nombre_train = 35
        df_nombre_wagon = 5
        df_nombre_visiteur_wagon = 8 
    if liste_frequentation.index(choix_data) == 2:
        df_lambda = 1500
        df_h_ouverture = 8
        df_nombre_train = 30
        df_nombre_wagon = 5
        df_nombre_visiteur_wagon = 10
    if liste_frequentation.index(choix_data) == 3:
        df_lambda = 2500
        df_h_ouverture = 8
        df_nombre_train = 40
        df_nombre_wagon = 5
        df_nombre_visiteur_wagon = 10
    if liste_frequentation.index(choix_data) == 4:
        df_lambda = 0
        df_h_ouverture = 0
        df_nombre_train = 0
        df_nombre_wagon = 0
        df_nombre_visiteur_wagon = 0

    donnees_file = pd.DataFrame(
        {  
            t("data_queue_parameters"): [
                t("data_queue_visitor"),
                t("data_queue_opening"),
            ],
            t("data_queue_values"): [df_lambda,  df_h_ouverture]
        }
    )

    donnees_train = pd.DataFrame(
        {  
            t("data_queue_parameters"): [
                "Train/h (μ)",
                t("number_car"),
                t("number_visitors")
            ],
            t("data_queue_values"): [df_nombre_train, df_nombre_wagon, df_nombre_visiteur_wagon]
        }
    )

else:
    choix_data_expert = st.selectbox(f"{t("selectbox")} **(mode expert)**", 
                            options = liste_frequentation_expert, 
                            width = 490,
                            index = 4,
                            key = "select_expert")
    if liste_frequentation_expert.index(choix_data_expert) == 0:
        h1 = 800
        h2 = 850
        h3 = 850
        h4 = 800
        h5 = 750
        h6 = 900
        h7 = 900
        h8 = 850
        h9 = 750
        h10 = 600
    if liste_frequentation_expert.index(choix_data_expert) == 1:
        h1 = 1000
        h2 = 1100
        h3 = 1200
        h4 = 1100
        h5 = 1000
        h6 = 1200
        h7 = 1200
        h8 = 1150
        h9 = 1000
        h10 = 850
    if liste_frequentation_expert.index(choix_data_expert) == 2:
        h1 = 1300
        h2 = 1400
        h3 = 1400
        h4 = 1300
        h5 = 1250
        h6 = 1500
        h7 = 1500
        h8 = 1450
        h9 = 1200
        h10 = 800
    if liste_frequentation_expert.index(choix_data_expert) == 3:
        h1 = 1800
        h2 = 1900
        h3 = 1900
        h4 = 2000
        h5 = 2100
        h6 = 2000
        h7 = 2100
        h8 = 2000
        h9 = 1800
        h10 = 1700
    if liste_frequentation_expert.index(choix_data_expert) == 4:
        h1 = 1400
        h2 = 2100
        h3 = 2300
        h4 = 1600
        h5 = 2000
        h6 = 2200
        h7 = 1900
        h8 = 1500
        h9 = 1100
        h10 = 600
    if liste_frequentation_expert.index(choix_data_expert) == 5:
        h1 = 0
        h2 = 0
        h3 = 0
        h4 = 0
        h5 = 0
        h6 = 0
        h7 = 0
        h8 = 0
        h9 = 0
        h10 = 0
    
    donnees_file_expert = pd.DataFrame(
        {  
            t("data_queue_parameters"): [
                f"{t("data_queue_visitor")} - 10h-11h",
                f"{t("data_queue_visitor")} - 11h-12h",
                f"{t("data_queue_visitor")} - 12h-13h",
                f"{t("data_queue_visitor")} - 13h-14h",
                f"{t("data_queue_visitor")} - 14h-15h",
                f"{t("data_queue_visitor")} - 15h-16h",
                f"{t("data_queue_visitor")} - 16h-17h",
                f"{t("data_queue_visitor")} - 17h-18h",
                f"{t("data_queue_visitor")} - 18h-19h",
                f"{t("data_queue_visitor")} - 19h-20h"
            ],
            t("data_queue_values"): [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]
        }
    )

    donnees_train_expert = pd.DataFrame(
        {  
            t("data_queue_parameters"): [
                "Train/h (μ)",
                t("number_car"),
                t("number_visitors")
            ],
            t("data_queue_values"): [60, 7, 4]
        }
    )

liste_lambdas = []

col1, col2 = st.columns(2)

#Data editor
with col1:

    titre, mode_expert = st.columns([1.9,1])
    with titre:
        st.write(t("queue_title"))
    with mode_expert:
        st.write("")
        st.toggle(t("toggle_expert"), help = t("toggle_expert_help"), key = "expert")
    if st.session_state.expert:
        tableau_modifie_file_expert = st.data_editor(donnees_file_expert, hide_index = True)
        liste_lambdas = tableau_modifie_file_expert[t("data_queue_values")].tolist()
        N_expert = sum(liste_lambdas)
    else:
        tableau_modifie_file = st.data_editor(donnees_file, hide_index = True)
        lambda_value = tableau_modifie_file.iloc[0][t("data_queue_values")]
        N = int(tableau_modifie_file.iloc[1][t("data_queue_values")]) * lambda_value

    col1_panne, col2_panne, col3_panne = st.columns([2,1.6,1.5])

    heure_debut_panne = 0
    heure_fin_panne = 0

    #Panne checkbox
    with col1_panne:
        panne = st.checkbox(t("panne"))
        if panne:
            with col2_panne:
                duree_panne = st.number_input(t("panne_duration"), value = 30)
            with col3_panne:
                heure_debut_panne = st.number_input(t("panne_hour"), value = 3, help = t("breakdown_help"))
                heure_debut_panne_min = heure_debut_panne*60
                heure_fin_panne = heure_debut_panne_min + duree_panne

    st.button(t("button"), width = 500, type = "primary", key = "button")

with col2:
    st.write(t("train_title"))
    if st.session_state.expert:
        tableau_modifie_train = st.data_editor(donnees_train_expert, hide_index = True)
    else:
        tableau_modifie_train = st.data_editor(donnees_train, hide_index = True)

    nbr_train = tableau_modifie_train.iloc[0][t("data_queue_values")]
    nbr_wagon = tableau_modifie_train.iloc[1][t("data_queue_values")]
    nbr_client_wagon = tableau_modifie_train.iloc[2][t("data_queue_values")]

    THRC = nbr_train * (nbr_wagon * nbr_client_wagon)

    st.write(f"{t("THRC")} {THRC}")

    #Affichage chargement
    if st.session_state.button:
        with st.status(t("status_1"), expanded=True) as status:
            
            st.write(t("status_2"))
            time.sleep(0.3) 
            st.write(t("status_3"))
            time.sleep(0.3)
            st.write(t("status_4"))
            time.sleep(0.3)
            st.write(t("status_5"))
            

nombre_total_visiteur_par_train = nbr_wagon * nbr_client_wagon
nombre_total_visiteur_par_heure = nombre_total_visiteur_par_train * nbr_train

# endregion

#region ---CALCULS M/D^B/1-----

if st.session_state.button:
    if st.session_state.expert:

        temps_arrive = []

        #Calcul des lambda pour mode expert (temps arrivé entre deux clients)
        for i in range(len(liste_lambdas)):
            lambda_valeur = liste_lambdas[i]
            
            if lambda_valeur > 0:
                lambda_min = lambda_valeur / 60
            
                U = np.random.uniform(0, 1, size=int(lambda_valeur))

                temps_entre_clients = -(1 / lambda_min) * np.log(U)
                
                temps_dans_tranche = np.cumsum(temps_entre_clients)
                
                heure_debut_tranche = i * 60 # Shifted to prevent visitors arriving after the first time slot from starting back at 0, adding the time already elapsed.
                temps_arrive_tranche = heure_debut_tranche + temps_dans_tranche

                for temps in temps_arrive_tranche:
                    temps_arrive.append(temps)

        #region Algo mode expert
        st.session_state["liste_attente"] = []
        #Variables algo
        liste_attente_temp = []
        total_depart_journee = nbr_train * N_expert
        intervalle = 60 / nbr_train
        t_depart = []
        temps_arrive_temp = temps_arrive.copy()
        liste_visiteurs_monte = []

        #Algorithme
        for i in range(total_depart_journee):
            t_depart.append(intervalle*i)

        for heure_depart in t_depart:

            if panne and (heure_debut_panne_min <= heure_depart < heure_fin_panne):
                continue
            else:
                liste_visiteurs_monte = []

                for k in range(min(nombre_total_visiteur_par_train, len(temps_arrive_temp))):
                    if temps_arrive_temp[k] < heure_depart:
                        liste_visiteurs_monte.append(temps_arrive_temp[k])
                    else:
                        break

                for temps_arrive_visiteur in liste_visiteurs_monte:
                    temps_attente = heure_depart - temps_arrive_visiteur
                    liste_attente_temp.append(temps_attente)

                temps_arrive_temp = temps_arrive_temp[len(liste_visiteurs_monte):]
                

        donnees_rho = []
            
        st.session_state['temps_arrive'] = temps_arrive
        st.session_state["liste_attente"] = liste_attente_temp
        st.session_state["moyenne"] = np.mean(liste_attente_temp)
        st.session_state["rho"] = donnees_rho

        st.divider()


        #endregion

        #region Graphiques et métriques mode expert

        if st.session_state["moyenne"] != None:

            col1, col2, col3 = st.columns([2,2,1])

            with col1:

                #Graphique 1
                fig, ax = plt.subplots(figsize=(7,3))
                sns.kdeplot(st.session_state["liste_attente"], cut=0)

                ax.set_xlabel(t("graph1_wait"))
                ax.set_ylabel(t("graph1_density"))
                ax.set_title(t("graph1_title"))
                st.pyplot(fig)

            with col2:
                nb_visiteurs_servis = len(st.session_state['liste_attente'])

                temps_arrive_servis = np.array(st.session_state['temps_arrive'][:nb_visiteurs_servis])

                df = pd.DataFrame({
                    'heure_exact': temps_arrive_servis / 60,
                    'liste_attente': st.session_state['liste_attente']
                })

                fig2, ax = plt.subplots(figsize=(7,3))
                df['attente_lisse'] = df['liste_attente'].rolling(100).mean()
                ax.plot(df['heure_exact'], df['attente_lisse'])
                ax.set_xlabel(t("graph2_hour"))
                ax.set_ylabel(t("graph1_wait"))
                ax.set_title(t("graph2_title"))
                st.pyplot(fig2)

            with col3:
                st.metric(
                    label = t("mean_wait_time"),
                    value = f"{round(st.session_state['moyenne'],1)}min",
                    width = "content"
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                capacite_par_min = (nbr_train * nombre_total_visiteur_par_train) / 60

                creneaux = [
                    "10h-11h", "11h-12h", "12h-13h", "13h-14h", "14h-15h",
                    "15h-16h", "16h-17h", "17h-18h", "18h-19h", "19h-20h"
                ]

                donnees_rho = []

                for i in range(len(liste_lambdas)):
                    lambda_heure = liste_lambdas[i]
                    lambda_min = lambda_heure / 60
                    rho = lambda_min / capacite_par_min
                    
                    if rho >= 1:
                        statut = "🔴 Saturation"
                    elif rho >= 0.8:
                        statut = t("charge1")
                    else:
                        statut = t("charge2")
                        
                    donnees_rho.append({
                        t("time_slot"): creneaux[i],
                        t("data_queue_visitor"): lambda_heure,
                        t("occupancy"): f"{rho:.2f}",
                        t("queue_status"): statut
                    })
                    
                df_rho = pd.DataFrame(donnees_rho)
                st.dataframe(df_rho, hide_index=True, use_container_width=True)

        #endregion

    else:


        N = int(N)
        U_arrive = np.random.uniform(0,1, size = N)

        #Temps entre arrivé des clients (loi Exp) calcul lambda
        lambda_value_min = lambda_value / 60
        temps_arrive_entre_deux_client = -(1/lambda_value_min) * np.log(U_arrive) #Inverse Transform Method
        temps_arrive = np.cumsum(temps_arrive_entre_deux_client)

        #region Algo mode normal

        st.session_state["liste_attente"] = []
        #Variables algo
        liste_attente_temp = []
        total_depart_journee = nbr_train * N
        intervalle = 60 / nbr_train
        t_depart = []
        temps_arrive_temp = temps_arrive.copy()
        liste_visiteurs_monte = []

        #Algorithme
        for i in range(total_depart_journee):
            t_depart.append(intervalle*i)

        for heure_depart in t_depart:

            if panne and (heure_debut_panne_min <= heure_depart < heure_fin_panne):
                continue
            else:
                liste_visiteurs_monte = []

                for k in range(min(nombre_total_visiteur_par_train, len(temps_arrive_temp))):
                    if temps_arrive_temp[k] < heure_depart:
                        liste_visiteurs_monte.append(temps_arrive_temp[k])
                    else:
                        break

                for temps_arrive_visiteur in liste_visiteurs_monte:
                    temps_attente = heure_depart - temps_arrive_visiteur
                    liste_attente_temp.append(temps_attente)

                temps_arrive_temp = temps_arrive_temp[len(liste_visiteurs_monte):]


        capacite_par_min = (nbr_train * nombre_total_visiteur_par_train) / 60  
        rho_calcule = lambda_value_min / capacite_par_min

        st.session_state['temps_arrive'] = temps_arrive
        st.session_state["liste_attente"] = liste_attente_temp
        st.session_state["moyenne"] = np.mean(liste_attente_temp)
        st.session_state["rho"] = rho_calcule

        #endregion


    # endregion

    # region ---Affichage graphiques et métriques---

        st.divider()

        if st.session_state["moyenne"] != None:

            col1, col2, col3, col4 = st.columns([2,2,0.1,1])

            with col1:

                #Graphique 1
                fig, ax = plt.subplots(figsize=(7,4))
                sns.kdeplot(st.session_state["liste_attente"], cut=0)

                ax.set_xlabel(t("graph1_wait"))
                ax.set_ylabel(t("graph1_density"))
                ax.set_title(t("graph1_title"))
                st.pyplot(fig)

            with col2:
                #Graphique 2
                df = pd.DataFrame({
                    'heure_exact': st.session_state['temps_arrive'] / 60,
                    'liste_attente': st.session_state['liste_attente']
                })

                fig2, ax = plt.subplots(figsize=(7,4))
                df['attente_lisse'] = df['liste_attente'].rolling(100).mean()
                ax.plot(df['heure_exact'], df['attente_lisse'])
                ax.set_xlabel(t("graph2_hour"))
                ax.set_ylabel(t("graph1_wait"))
                ax.set_title(t("graph2_title"))
                st.pyplot(fig2)

            with col4:

                st.write("")
                
                st.metric(
                    label = t("mean_wait_time"),
                    value = f"{round(st.session_state['moyenne'],1)} min",
                    width = "stretch"
                )
                
                rho = st.session_state["rho"]
                delta_color = "red" if rho >= 1 else "green"

                st.metric(
                    label = r"Score $\rho = \frac{\lambda}{\text{ }\mu}$",
                    value=f"{rho:.3f}",
                    delta = f"{(rho*100):.1f}% {t("charge")}",
                    delta_color = delta_color,
                    width = "stretch"
                )

        # endregion

