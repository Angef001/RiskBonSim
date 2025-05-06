import streamlit as st
import matplotlib.pyplot as plt
from src.instruments.obligation import Obligation
from src.io.import_csv import charger_portefeuille_csv
import io
import urllib.parse
import pandas as pd
from src.risk.historique import simuler_rendements, calculer_pnl_hist
from src.ui.lang import translations
from src.risk.var import calculer_var_parametrique
from PIL import Image
import numpy as np

st.set_page_config(page_title="RiskBonSim", layout="wide")

st.markdown("""
    <style>
    .info-section {
        padding-top: 40px;
    }
    .info-button {
        background-color: #e9ecef;
        color: #1c1c1c;
        border: none;
        padding: 10px 16px;
        text-align: left;
        border-radius: 8px;
        font-size: 15px;
        width: 100%;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .info-button:hover {
        background-color: #d0d4da;
        color: black;
    }
    .info-button span {
        margin-left: 8px;
    }
    </style>
""", unsafe_allow_html=True)



# Logo
logo = Image.open("assets/logo.png")
st.sidebar.image(logo, width=150)

# Langue
langue = st.sidebar.selectbox("🌐 Langue / Language", options=["fr", "en"], index=0)
t = translations[langue]

st.title(t["app_title"])
st.markdown(
    f"<h4 style='text-align: center; color: grey;'>{t['app_subtitle']}</h4>",
    unsafe_allow_html=True
)

# Navigation
onglet = st.sidebar.radio("📁 Navigation", [t["nav_home"], t["nav_bond"], t["nav_portfolio"], t["nav_risk"]])


# Bloc Information dans la sidebar
st.sidebar.markdown(
    f"""
    <style>
        .info-section {{
            margin-top: 60px;
        }}
        .info-title {{
            font-weight: 600;
            font-size: 16px;
            color: #ffffff;
            margin-bottom: 10px;
        }}
        .info-button {{
            background-color: #f0f2f6;
            color: #1c1c1c;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px 15px;
            width: 100%;
            text-align: left;
            font-size: 15px;
        }}
        .info-button:hover {{
            background-color: #e4e6eb;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# Section affichée dans la sidebar
st.sidebar.markdown(f"<div class='info-section'><div class='info-title'>ℹ️ {t['sidebar_info']}</div>", unsafe_allow_html=True)

# Boutons stylisés avec logique normale Streamlit
if st.sidebar.button(f"❓ {t['link_tuto']}", key="btn_tuto"):
    onglet = "Tutoriel"
if st.sidebar.button(f"ℹ️ {t['link_about']}", key="btn_apropos"):
    onglet = "Apropos"

st.sidebar.markdown("</div>", unsafe_allow_html=True)



# Accueil
if onglet == t["nav_home"]:
    st.markdown(
        f"""
        <style>
            .feature-box {{
                padding: 20px;
                border-radius: 10px;
                height: 180px;
            }}
        </style>
        <h1 style='text-align: center; color: #aab2c8;'>{t["home_title"]}</h1>
        <p style='text-align: center; font-size: 18px; color: #aab2c8;'>
            {t["home_subtitle"]}
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class='feature-box' style='background-color: #edf4ff;'>
                <h3 style='color: #3b5bdb;'>{t["box_flux_title"]}</h3>
                <p style='font-size: 15px; color: #444;'>{t["box_flux_desc"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class='feature-box' style='background-color: #fff3bf; margin-top: 20px;'>
                <h3 style='color: #e67700;'>{t["box_risk_title"]}</h3>
                <p style='font-size: 15px; color: #444;'>{t["box_risk_desc"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class='feature-box' style='background-color: #e8f8f5;'>
                <h3 style='color: #0b7285;'>{t["box_duration_title"]}</h3>
                <p style='font-size: 15px; color: #444;'>{t["box_duration_desc"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class='feature-box' style='background-color: #fde2e4; margin-top: 20px;'>
                <h3 style='color: #c2255c;'>{t["box_export_title"]}</h3>
                <p style='font-size: 15px; color: #444;'>{t["box_export_desc"]}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# Obligation
elif onglet == t["nav_bond"]:
    st.markdown(
        """
        <style>
            .box {
                background-color: #f8f9fc;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 1px 6px rgba(0, 0, 0, 0.05);
            }
            .title {
                color: #3b5bdb;
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown(f"<div class='title'>{t['bond_section_title']}</div>", unsafe_allow_html=True)

    nom = st.text_input(t["bond_label_name"], value="OAT 2030")
    maturite = st.slider(t["bond_label_maturity"], 1, 30, 5)
    coupon = st.slider(t["bond_label_coupon"], 0.0, 10.0, 5.0)
    frequence = st.selectbox(t["bond_label_frequency"], [1, 2, 4], index=0)
    prix = st.number_input(t["bond_label_price"], value=100.0)
    taux = st.slider(t["bond_label_discount"], 0.0, 15.0, 4.0) / 100
    st.markdown("</div>", unsafe_allow_html=True)

    oblig = Obligation(nom, maturite, coupon, frequence, prix)
    prix_calcule = oblig.calculer_prix(taux)
    flux = oblig.obtenir_flux()

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.success(f"{t['bond_price_result']} **{prix_calcule:.2f} €**")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.subheader(t["bond_flux_title"])
    fig, ax = plt.subplots(figsize=(6, 2.5))
    ax.bar(range(1, len(flux)+1), flux, color='#74c0fc')
    ax.set_xlabel(t["bond_flux_xlabel"])
    ax.set_ylabel(t["bond_flux_ylabel"])
    ax.set_title(t["bond_flux_graphtitle"])
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)



# Portefeuille
elif onglet == t["nav_portfolio"]:
    st.markdown(
        """
        <style>
            .box {
                background-color: #f8f9fc;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 1px 6px rgba(0, 0, 0, 0.05);
            }
            .title {
                color: #3b5bdb;
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='box'>", unsafe_allow_html=True)
    st.markdown(f"<div class='title'>{t['portfolio_section_title']}</div>", unsafe_allow_html=True)
    fichier = st.file_uploader(t["portfolio_upload_label"], type=["csv"])
    st.markdown("</div>", unsafe_allow_html=True)

    if fichier:
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(fichier.getvalue())
            chemin_temp = tmp.name

        obligations = charger_portefeuille_csv(chemin_temp)

        # Pondérations
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        somme_poids = sum(o.poids for o in obligations)
        if abs(somme_poids - 100) > 0.01:
            st.warning(t["portfolio_weight_warning"].format(somme=somme_poids))
        else:
            st.success(t["portfolio_weight_valid"])
        st.success(t["portfolio_loaded"].format(nb=len(obligations)))
        st.markdown("</div>", unsafe_allow_html=True)

        # Tableau
        data = [{
            t["bond_label_name"]: o.nom,
            t["bond_label_maturity"]: o.maturite,
            t["bond_label_coupon"]: o.coupon,
            t["bond_label_price"]: o.prix,
            t["bond_label_ytm"]: round(o.calculer_ytm() * 100, 2)
        } for o in obligations]


        df = pd.DataFrame(data)

        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='title'>{t['portfolio_table_title']}</div>", unsafe_allow_html=True)
        st.dataframe(df)
        st.markdown("</div>", unsafe_allow_html=True)

        # Agrégats
        ytms = [o.calculer_ytm() for o in obligations]
        duration_ponderee = sum(o.poids / 100 * o.calculer_duration_modifiee(y) for o, y in zip(obligations, ytms))
        convexite_ponderee = sum(o.poids / 100 * o.calculer_convexite(y) for o, y in zip(obligations, ytms))

        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='title'>{t['portfolio_agg_title']}</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric(t["metric_ytm_mean"], f"{100 * sum(ytms) / len(ytms):.2f}")
        col2.metric(t["metric_duration"], f"{duration_ponderee:.2f}")
        col3.metric(t["metric_convexite"], f"{convexite_ponderee:.2f}")
        st.markdown("</div>", unsafe_allow_html=True)

        # Export
        st.markdown("<div class='box'>", unsafe_allow_html=True)
        st.download_button(
            label=t["portfolio_export_label"],
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="portefeuille_export.csv",
            mime="text/csv"
        )
        st.markdown("</div>", unsafe_allow_html=True)



# Risque
elif onglet == t["nav_risk"]:
    st.markdown(
        """
        <style>
            .box {
                background-color: #f8f9fc;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 25px;
                box-shadow: 0px 1px 6px rgba(0, 0, 0, 0.05);
            }
            .title {
                color: #e67700;
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 12px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<div class='box'><div class='title'>{t['parallel_shock']}</div>", unsafe_allow_html=True)
    choc_bps = st.slider(t["shock_slider"], -300, 300, 100, step=25)

    if st.button(f"{t['apply_shock_btn']}"):
        obligations = charger_portefeuille_csv("data/portefeuille.csv")
        taux_originaux = [o.calculer_ytm() for o in obligations]
        taux_choc = [t + choc_bps / 10000 for t in taux_originaux]
        valeur_initiale = sum(o.calculer_prix(t) for o, t in zip(obligations, taux_originaux))
        valeur_apres_choc = sum(o.calculer_prix(t) for o, t in zip(obligations, taux_choc))
        perte = valeur_initiale - valeur_apres_choc
        col1, col2, col3 = st.columns(3)
        col1.metric(t["init_value"], f"{valeur_initiale:,.2f} €")
        col2.metric(t["after_shock"], f"{valeur_apres_choc:,.2f} €")
        col3.metric(t["loss_label"], f"{perte:,.2f} €")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><div class='title'>{t['scenario_title']}</div>", unsafe_allow_html=True)
    scenario = st.selectbox(
        t["scenario_select"],
        [t["scenario_none"], "Bear Flattening", "Bull Steepening"]
    )


    amplitude_bps = st.slider(t["amplitude_label"], 0, 300, 100, step=25)

    if scenario != "Aucun" and st.button(t["scenario_btn"]):
        obligations = charger_portefeuille_csv("data/portefeuille.csv")
        ytms = [o.calculer_ytm() for o in obligations]
        durations = [o.maturite for o in obligations]
        chocs = [(amplitude_bps / 10000 * (d / max(durations))) if scenario == "Bear Flattening"
                 else (-amplitude_bps / 10000 * (1 - d / max(durations)))
                 for d in durations]
        taux_apres_choc = [y + c for y, c in zip(ytms, chocs)]
        valeur_init = sum(o.calculer_prix(y) for o, y in zip(obligations, ytms))
        valeur_choc = sum(o.calculer_prix(y) for o, y in zip(obligations, taux_apres_choc))
        perte = valeur_init - valeur_choc
        col1, col2, col3 = st.columns(3)
        col1.metric(t["init_value"], f"{valeur_init:,.2f} €")
        col2.metric(t["after_shock"], f"{valeur_choc:,.2f} €")
        col3.metric(t["loss_label"], f"{perte:,.2f} €")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><div class='title'>{t['var_title']}</div>", unsafe_allow_html=True)
    vol_input = st.text_input(t["vol_input"], "5,6,4")
    corr_input = st.text_area(t["corr_input"], "1,0.3,0.2\n0.3,1,0.25\n0.2,0.25,1")

    if st.button(t["var_button"]):
        obligations = charger_portefeuille_csv("data/portefeuille.csv")
        valeurs = [o.prix for o in obligations]
        poids = [o.poids / 100 for o in obligations]
        volatilites = [float(v.strip()) / 100 for v in vol_input.split(",")]
        correlation = [list(map(float, row.split(","))) for row in corr_input.strip().split("\n")]
        var = calculer_var_parametrique(valeurs, poids, volatilites, correlation)
        st.metric(t["var_result"], f"{var:,.2f} €")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><div class='title'>{t['hist_title']}</div>", unsafe_allow_html=True)
    nb_jours = st.slider(t["sim_days_label"], 100, 1000, 250)
    if st.button(t["hist_button"]):
        obligations = charger_portefeuille_csv("data/portefeuille.csv")
        valeurs = [o.prix for o in obligations]
        poids = [o.poids / 100 for o in obligations]
        valeur_totale = sum(valeurs)
        rendements = simuler_rendements(nb_jours=nb_jours, nb_actifs=len(obligations))
        pnl = calculer_pnl_hist(rendements, poids, valeur_totale)
        st.write(f"📉 {t['mean_label']} : {pnl.mean():.2f} €")
        st.write(f"🛑 {t['min_label']} : {pnl.min():.2f} €")
        fig, ax = plt.subplots(figsize=(6, 2.5))
        ax.hist(pnl, bins=30, color='orange', edgecolor='black')
        ax.set_title(t["graph_title"])
        ax.set_xlabel(t["x_label"])
        ax.set_ylabel(t["y_label"])
        st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

#Tutoriel
elif onglet == "Tutoriel":
    st.markdown(
        """
        <style>
            .box {
                background-color: #f8f9fc;
                padding: 25px;
                border-radius: 10px;
                margin-bottom: 30px;
                box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.06);
            }
            .box h3 {
                color: #5c7cfa;
                margin-bottom: 15px;
            }
            .box p {
                font-size: 16px;
                color: #333;
                line-height: 1.6;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<h2 style='text-align:center;'>📘 {t['tuto_intro_title']}</h2>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>📘 {t['tuto_intro_title']}</h3><p>{t['tuto_intro_text']}</p></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>💼 {t['tuto_bond_title']}</h3><p>{t['tuto_bond_text']}</p></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>📂 {t['tuto_portfolio_title']}</h3><p>{t['tuto_portfolio_text']}</p></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>⚠️ {t['tuto_risk_title']}</h3><p>{t['tuto_risk_text']}</p></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>📤 {t['tuto_export_title']}</h3><p>{t['tuto_export_text']}</p></div>", unsafe_allow_html=True)

    # Bouton de téléchargement PDF
    import os

    pdf_path = "assets/tutoriel_riskbonsim.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        st.download_button(
            label=f"📄 {t['tuto_download_label']}",
            data=PDFbyte,
            file_name="RiskBonSim_Tutoriel.pdf",
            mime="application/pdf",
            key="download_tuto_pdf"
        )
    else:
        st.info(f"📄 {t['tuto_pdf_pending']}")




#A propos
elif onglet == "Apropos":
    st.markdown(
        """
        <style>
            .box {
                background-color: #f8f9fc;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 25px;
                box-shadow: 0px 1px 6px rgba(0, 0, 0, 0.05);
            }
            .box h3 {
                color: #3b5bdb;
                margin-bottom: 10px;
            }
            .box p {
                font-size: 15px;
                color: #444;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(f"<div class='box'><h3>ℹ️ {t['about_title']}</h3><p>{t['about_description']}</p></div>", unsafe_allow_html=True)

    st.markdown(f"""
        <div class='box'>
            <h3>🛠️ {t['about_tech_title']}</h3>
            <ul style="color:#444; font-size:15px; line-height:1.6;">
                <li>🔧 {t['about_tech_streamlit']}</li>
                <li>📊 {t['about_tech_matplotlib']}</li>
                <li>🧮 {t['about_tech_numpy']}</li>
                <li>📁 {t['about_tech_modular']}</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<div class='box'><h3>📬 {t['about_contact_title']}</h3><p>{t['about_contact_text']}</p></div>", unsafe_allow_html=True)
