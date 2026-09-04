import streamlit as st

#region ---Config de la page---

#Bloquer la taille de la sidebar
st.markdown("""
<style>
[data-testid="stSidebar"] {
    width: 320px;
    min-width: 320px;
    max-width: 320px;
}
</style>
""", unsafe_allow_html=True)


pages = {
    "Queue simulator": [
        st.Page("pages/theme_park.py", title="Theme park", default=True)
    ],
    "Other simulation": [
        st.Page("pages/other_simulation.py", title="*More simulations coming soon*")
    ]
}

pg = st.navigation(pages)
pg.run()


with st.sidebar:
    st.divider()
    st.write("*Made with ❤️ by Thomas*")
    st.link_button('Code on GitHub 👾', "https://github.com/Math1720182/MathSim/")

# endregion

#hello

