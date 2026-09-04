import streamlit as st

#test

def t(key):

    language = st.session_state.get("language", "fr") #default fr

    return texte.get(key).get(language)

texte = {
    "title" : {
        "fr" : "Simulateur intéractif d'une file d'attente de parc d'attraction",
        "en" : "Interactive theme park queue simulator"
    },
    "header" : {
        "fr" : r"Modèle mathématique : File $M/D^{B}/1$",
        "en" : r"Mathematical model : $M/D^{B}/1$ queue"
    },
    "liste_freq" : {
        "fr" : ["Basse", "Moyenne", "Haute", "Extrême", "Personnalisé"],
        "en" : ["Low", "Mid", "High", "Extrem", "Perso"]
    },
    "liste_freq_expert" : {
        "fr" : ['Basse', 'Moyenne', 'Haute', 'Extrême', 'Silver Star (EP) / Toutatis (PA)', 'Personnalisé'],
        "en" : ['Low', 'Mid', 'High', 'Extrem', 'Silver Star (EP) / Toutatis (PA)', 'Perso']
    },
    "label_methodo": {
        "fr" : "Méthodologie",
        "en" : "Methodology"
    },
    "selectbox" : {
        "fr" : "**Pré-remplir la fréquentation pour observer des résultats réalistes :**",
        "en" : "**Pre-fill attendance to observe realistic results:**"
    },
    "data_queue_parameters" : {
        "fr" : "Paramètres",
        "en" : "Parameters"
    },
    "data_queue_visitor" : {
        "fr" : "Clients / h (λ)",
        "en" : "Visitors / h (λ)"
    },
    "data_queue_opening" : {
        "fr" : "Nombre d'heures d'ouverture (n)",
        "en" : "Operating hours (n)"
    },
    "data_queue_values" : {
        "fr" : "Valeur (à modifier)",
        "en" : "Values (can be modified)"
    },
    "number_car" : {
        "fr" : "Wagon/train",
        "en" : "Car/train"
    },
    "number_visitors" : {
        "fr" : "Nombre visiteurs/wagon",
        "en" : "Passengers/car"
    },
    "queue_title" : {
        "fr" : "### Paramètres de la file 👥",
        "en" : "#### Parameters of the queue 👥"
    },
    "train_title" : {
        "fr" : "### Paramètres des trains 🎢",
        "en" : "#### Parameters of the cars 🎢"
    },
    "toggle_expert" : {
        "fr" : "**Mode expert** 🚀",
        "en" : "**Expert mode** 🚀"
    },
    "toggle_expert_help" : {
        "fr" : "Permet de simuler une journée réaliste avec des pics de fréquentation par heure",
        "en" : "Simulates a realistic day with hourly attendance peaks"
    },
    "panne" : {
        "fr" : "**Simuler une panne**",
        "en" : "**Simulate a breakdown**"
    },
    "panne_duration" : {
        "fr" : "Temps de la panne (min)",
        "en" : "Duration (min)"
    },
    "panne_hour" : {
        "fr" : "Quelle heure ?",
        "en" : "Which hour?"
    },
    "button" : {
        "fr" : "Lancer la simulation",
        "en" : "Run simulation"
    },
    "THRC" : {
        "fr" : "**Capacité théorique de l'attraction (THRC) :**",
        "en" : "**Theoretical Hourly Capacity (THRC):**"
    },
    "status_1" : {
        "fr" :  "**Résolution du modèle mathématique en cours**",
        "en" : "Solving mathematical model..."
    },
    "status_2" : {
        "fr" : "Tirage aléatoire des processus de Poisson (λ)..." ,
        "en" : "Random sampling of Poisson processes (λ)..."
    },
    "status_3" : {
        "fr" : "Simulation de l'ordonnancement des trains et pannes..." ,
        "en" : "Simulating train scheduling and breakdowns..."
    },
    "status_4" : {
        "fr" :  "Estimation de la densité par noyau (KDE) et lissage...",
        "en" : "Kernel Density Estimation (KDE) and smoothing..."
    },
    "status_5" : {
        "fr" : "Simulation terminée ! ✅" ,
        "en" : "Simulation finished! ✅"
    },   
    "graph1_wait" : {
        "fr" : "Temps d'attente en minutes",
        "en" : "Waiting time in minutes"
    },
    "graph1_density" : {
        "fr" : "Densité",
        "en" : "Density"
    },
    "graph1_title" : {
        "fr" : "Densité du temps d'attente",
        "en" : "Wait time density"
    },
    "graph2_hour" : {
        "fr" : "Heure de la journée (h)",
        "en" : "Daytime"
    },
    "graph2_title" : {
        "fr" : "Évolution du temps d'attente au fil de la journée",
        "en" : "Wait time distribution chart"
    }, 
    "mean_wait_time" : { 
        "fr" : "Temps d'attente moyen : ",
        "en" : "Mean waiting time: "

    },
    "charge1" : {
        "fr" : "🟠 Charge élevée",
        "en" : "🟠 High load"
    },
    "charge2" : {
        "fr" : "🟢 Fluide",
        "en" : "🟢 Fluid"
    },
    "time_slot" : {
        "fr" : "Tranche horaire",
        "en" : "Time slot"
    },
    "occupancy" : {
        "fr" : "Taux d'occupation (ρ)",
        "en" : "Occupancy rate (ρ)"
    },
    "queue_status" : {
        "fr" : "État de la file",
        "en" : "Queue status"
    },
    "charge" : {
        "fr" : "de charge",
        "en" : "workload"
    },
    "text_methodo" : {
        "fr":
            r"""
                La simulation suivante utilise un modèle mathématique stochastique de type $M/D^{B}/1$. Mais quésaco que ça ?

                Cette file, écrite en notation de Kendall, sert à analyser un système où des entités (des clients, des paquets de données) arrivent, attendent leur tour, puis sont traitées par un serveur. Cette file est particulièrement adaptée pour décrire les files d'attente de parcs d'attractions. Explication.

                - **M (Markovien / Mémoire nulle)** : les arrivées se font au hasard, comme dans la réalité.

                - **D (Déterministe)** : le temps de traitement/service est fixe et constant. Chaque groupe prend exactement la même durée à être traité. Dans le cas de notre simulation, les trains arrivent à heure fixe.

                - **^B (Batch / Service par lots)** : le serveur traite les éléments par groupes de taille fixe B. Dans notre cas, nous remplissons le train à chaque départ.

                - **1** : il y a un seul serveur dans le système qui suit la tradition : premier arrivé, premier servi. Ici, une seule embarcation à la fois.

                *On estime que l'arrivée des visiteurs suit une loi de Poisson*. **Pourquoi ?** Car elle permet de simuler une arrivée sur un intervalle de temps fixe. Son usage correspond parfaitement à cette situation.

                *On estime que le délai entre deux visiteurs suit une loi exponentielle*. **Pourquoi ?** Car si l'arrivée des visiteurs suit une loi de Poisson alors le temps entre chaque visiteur suivra obligatoirement une loi exponentielle.

                Pour simuler les $\lambda$ (arrivée entre chaque client) de manière aléatoire à chaque calcul, j'ai généré $U$ via un processus uniforme en utilisant numpy. Le reste est calculé manuellement en suivant la formule $T$ d'inversion : $T = -\frac{\ln(U)}{\lambda}$

                La formule $\rho = \frac{\lambda}{\mu}$ permet d'estimer le niveau de charge de la file. Au-delà de 100 %, le temps d'attente tend vers l'infini.

                **Limite de la simulation :** Même en mode expert, le réglage n'est pas assez fin pour simuler des arrivées brutales par groupe ou de manière aléatoire. Aussi, je pars du principe que le train part à heure fixe, parfois totalement rempli si la file est pleine ou non si la file le permet. Dans la réalité, les trains ne partent pas toujours complets, certains groupes ne souhaitant pas se séparer. Pour combler cela, les parcs mettent en place une file « single rider » qui permet de remplir les places vides et d'optimiser la file.
                """
                ,
        "en" : 
            r"""
                The following simulation uses a stochastic mathematical model of type $M/D^{B}/1$. But what on earth is that?

                This queue, written in Kendall's notation, is used to analyze a system where entities (customers, data packets) arrive, wait their turn, and are processed by a server. This model is particularly suited for describing amusement park queues. Here is how it works:

                - **M (Markovian / Memoryless)**: arrivals occur randomly, just like in real life.

                - **D (Deterministic)**: the processing/service time is fixed and constant. Each group takes exactly the same amount of time to be processed. In our simulation, trains arrive at fixed times.

                - **^B (Batch / Bulk service)**: the server processes items in fixed-size groups B. In our case, we fill the train at each departure.

                - **1**: there is only one server in the system following the "first-come, first-served" rule. Here, one vehicle at a time.

                *We assume that visitor arrivals follow a Poisson distribution*. **Why?** Because it allows us to simulate arrivals over a fixed time interval. It fits this situation perfectly.

                *We assume that the delay between two visitors follows an exponential distribution*. **Why?** Because if visitor arrivals follow a Poisson distribution, the inter-arrival time between visitors will automatically follow an exponential distribution.

                To simulate the $\lambda$ (inter-arrival time between each customer) randomly for each calculation, I generated $U$ via a uniform process using NumPy. The rest is calculated manually using the inversion formula for $T$: $T = -\frac{\ln(U)}{\lambda}$

                The formula $\rho = \frac{\lambda}{\mu}$ allows us to estimate the queue's traffic intensity / load factor. Beyond 100%, the waiting time tends toward infinity.

                **Simulation Limitations:** Even in expert mode, the settings are not refined enough to simulate sudden arrivals by groups or completely at random. Also, I assume the train departs at fixed times, sometimes fully loaded if the queue is full, or partially empty if the queue allows it. In reality, trains do not always depart full because some groups prefer not to split up. To solve this, theme parks use a "single rider" line to fill empty seats and optimize the queue.
                """

    },
    "label_help": {
        "fr": "Aide à l'utilisation",
        "en" : "Help"
    },
    "text_help": {
        "fr" : 
            "Vous pouvez utiliser le pré-remplissage pour obtenir des simulations liée à la fréquentation de l'attraction. \n\n" \
            "Le mode expert (contrairement à ce qu'indique son nom n'est pas réservé exclusivement aux experts 😉) vous permet de détailler plus finement la fréquentation de l'attraction heure par heure. " \
            "C'est le mode le plus précis qui vous permet d'avoir un temps d'attente évolutif dans la journée. Si vous gardez une fréquentation fixe, le temps d'attente va continuer de croitre pendant la journée une fois que la charge dépasse 100% ce qui n'est pas réaliste. \n\n" \
            "**Pourquoi quand le modèle est en saturation, le pic d'attente ne tombe pas exactement sur l'heure sélectionné ?** \n\n" \
            "Vous avez l'oeil 🙂 ! L'axe x du graphique représente le temps d'attente avant d'être embarqué. Le système indique pour quel client le temps d'attente va augmenté. Par exemple, lorsque que le système est stable, (pour une panne à 4h) les clients arrivés à 3h55 passent presque immédiatement. Donc, le premier client impacté par la panne est arrivé à 3h59 ou 4h00. Le pic saute pile à 4h." \
            "Lorsque le système sature, la file d'attente est déjà formée et longue, le pic va donc sauté en amont. \n\n" \
            "**Note sur la capacité théorique de l'attraction (THRC) :** Il faut utiliser le THRC pour avoir une simulation réaliste. Sous le THRC, la charge est stable, au dessus, la charge augmente."
        ,
        "en" : 
            r"""
            You can use pre-filling to generate simulations based on the attraction's attendance.

            Expert mode (contrary to what the name suggests, it is not reserved exclusively for experts 😉) allows you to break down attendance hour by hour in greater detail. It is the most accurate mode, giving you a dynamic waiting time throughout the day. If you keep attendance fixed, the waiting time will continue to grow during the day once the capacity exceeds 100%, which is not realistic.

            **Why does the peak wait time not align exactly with the selected hour when the model is saturated?**

            You have a good eye 🙂! The x-axis of the graph represents the wait time before boarding. The system shows which arriving customer will experience an increased wait time. For example, when the system is stable (for a breakdown at 4:00), customers arriving at 3:55 pass almost immediately. Therefore, the first customer affected by the breakdown arrived at 3:59 or 4:00, and the peak appears right at 4:00. However, when the system is saturated, the queue is already long, so the peak shifts earlier.

            **Note on Theoretical Hourly Capacity (THRC):** You should use the THRC to get a realistic simulation. Below the THRC, the load is stable; above it, the load increases.
            """
    },
    "breakdown_help" : {
        "fr" : "Ne pas mettre 14 pour 14h, mettre l'heure par rapport à son temps total d'ouverture, ici 3 pour la 3ème heure sur les 8h d'ouverture",
        "en" : "Do not enter 14 for 2 PM; enter the hour relative to its total opening time (for instance, 3 for the 3rd hour of the 8-hour opening window)."
    }
}

