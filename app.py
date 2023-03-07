import streamlit as st

st.write("""
# Chatbot
Es-tu positif au COVID-19?!
""")


def douleur():
    with st.form("douleur"):
        radio_val = st.radio(
            "Douleur?",
            (
                "Abdomen",
                "Gorge",
                "Poitrine",
                "Aucune"
            )
        )
        submitted = st.form_submit_button("Valider")
        if submitted:
            return radio_val


def fievre():
    with st.form("fievre"):
        radio_val = st.radio(
            "Fièvre?",
            (
                "Oui",
                "Non"
            )
        )
        submitted = st.form_submit_button("Valider")
        if submitted:
            return radio_val


def toux():
    with st.form("toux"):
        radio_val = st.radio(
            "Toux?",
            (
                "Oui",
                "Non"
            )
        )
        submitted = st.form_submit_button("Valider")
        if submitted:
            return radio_val


match douleur():
    case "Abdomen":
        st.write("Diagnostic: **appendicite**")
    case "Gorge":
        match fievre():
            case "Oui":
                st.write("Diagnostic: **rhume**")
            case "Non":
                st.write("Diagnostic: **mal de gorge**")
    case "Poitrine":
        st.write("Diagnostic: **infarctus**")
    case "Aucune":
        match toux():
            case "Oui":
                match fievre():
                    case "Oui":
                        st.write("Diagnostic: **refroidissement**")
                    case "Non":
                        st.write("Diagnostic: **rhume**")
            case "Non":
                st.write("Rien")
