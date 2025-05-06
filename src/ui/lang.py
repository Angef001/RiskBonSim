translations = {
    "fr": {
        "app_title": "📊 RiskBonSim",
        "app_subtitle": "Simulateur interactif de portefeuille obligataire",

        "lang_select": "🌐 Langue / Language",
        "nav_home": "Accueil",
        "nav_bond": "Obligation",
        "nav_portfolio": "Portefeuille",
        "nav_risk": "Risque",

        "link_tuto": "Tutoriel",
        "link_about": "À propos",
        "nav_section": "Navigation",
        "sidebar_info": "Informations",

        # Pour la page d'accueil
        "home_title": "🏠 Bienvenue dans RiskBonSim",
        "home_subtitle": "Une application moderne pour modéliser, simuler et analyser un portefeuille obligataire.",

        "box_flux_title": "💼 Calculer le prix et les flux",
        "box_flux_desc": "Simulez les flux d'une obligation avec ses paramètres : coupon, maturité, fréquence…",

        "box_risk_title": "📉 Risque de marché",
        "box_risk_desc": "Estimez la VaR, appliquez des stress tests, et mesurez les pertes potentielles.",

        "box_duration_title": "📊 Duration & Convexité",
        "box_duration_desc": "Analysez les indicateurs de sensibilité et de courbure du portefeuille.",

        "box_export_title": "📤 Export",
        "box_export_desc": "Téléchargez les données traitées et visualisations en CSV.",


        
        # Section obligation
        "bond_section_title": "💼 Paramètres de l'obligation",
        "bond_label_name": "Nom",
        "bond_label_ytm": "YTM estimé (%)",
        "bond_label_maturity": "Maturité (années)",
        "bond_label_coupon": "Taux du coupon (%)",
        "bond_label_frequency": "Fréquence de paiement",
        "bond_label_price": "Prix de marché (€)",
        "bond_label_discount": "Taux d'actualisation (%)",
        "bond_price_result": "💰 Prix théorique :",
        "bond_flux_title": "📈 Flux futurs",
        "bond_flux_xlabel": "Période",
        "bond_flux_ylabel": "Montant (€)",
        "bond_flux_graphtitle": "Flux futurs",


        # Onglet Portefeuille
        "portfolio_section_title": "📂 Import d’un portefeuille obligataire",
        "portfolio_upload_label": "Choisissez un fichier CSV",
        "portfolio_weight_warning": "⚠️ La somme des pondérations est {somme:.2f} % (doit être 100 %)",
        "portfolio_weight_valid": "✅ Pondérations valides (somme = 100%)",
        "portfolio_loaded": "{nb} obligations chargées ✅",
        "portfolio_table_title": "📋 Détail du portefeuille",
        "portfolio_agg_title": "📐 Indicateurs agrégés",
        "portfolio_export_label": "📥 Exporter en CSV",
        "metric_ytm_mean": "YTM moyen (%)",
        "metric_duration": "Duration modifiée (pondérée)",
        "metric_convexite": "Convexité (pondérée)",


        # Onglet Risque
        "risk_header": "⚠️ Analyse de Risque de Marché",
        "risk_instructions": "👉 Commencez par importer un portefeuille dans l'onglet précédent.",
        "parallel_shock": "📉 Choc parallèle sur les taux",
        "shock_slider": "Amplitude du choc (en points de base)",
        "apply_shock_btn": "Appliquer le choc",
        "init_value": "📊 Valeur initiale",
        "after_shock": "📉 Valeur après choc",
        "loss_label": "🛑 Perte (Δ)",

        "scenario_title": "📉 Scénarios de courbe (Flattening / Steepening)",
        "scenario_select": "Choisir un scénario",
        "scenario_none": "Aucun",
        "amplitude_label": "Amplitude (bps)",
        "scenario_btn": "Appliquer le scénario",

        "csv_curve_upload": "📁 Importer une courbe de taux personnalisée (CSV)",
        "csv_file_label": "Fichier CSV de courbe",
        "curve_loaded": "📈 Courbe chargée :",
        "apply_curve_btn": "💰 Appliquer la courbe CSV au portefeuille",
        "custom_curve_value": "📊 Valeur du portefeuille avec courbe CSV :",
        "curve_before": "Avant",
        "curve_after": "Après",
        "curve_chart_title": "Impact de la courbe CSV",

        "manual_curve": "✍️ Saisir manuellement une courbe de taux",
        "nb_points": "Nombre de points",
        "maturity_x": "Maturité {i} (années)",
        "rate_y": "Taux {i} (%)",
        "manual_plot": "Tracer la courbe manuelle",
        "manual_apply": "💰 Appliquer la courbe au portefeuille",
        "manual_value": "💼 Valeur du portefeuille avec courbe personnalisée :",
        "manual_chart_title": "Impact de la courbe manuelle",

        "var_title": "📉 Calcul de la VaR paramétrique",
        "vol_input": "Volatilités (%) séparées par des virgules",
        "corr_input": "Matrice de corrélation (ligne par ligne, séparée par des virgules)",
        "var_button": "🧮 Calculer la VaR",
        "var_result": "📉 VaR (95%)",

        "hist_title": "📊 Distribution simulée des pertes potentielles (P&L)",
        "hist_button": "📈 Générer l'histogramme",
        "sim_days_label": "Nombre de jours simulés",
        "mean_label": "P&L moyen",
        "min_label": "P&L min",
        "x_label": "P&L (€)",
        "y_label": "Fréquence",
        "graph_title": "Distribution des pertes potentielles (P&L)",


        #Tutoriel
        "tuto_intro_title": "Tutoriel interactif",
        "tuto_intro_text": "Bienvenue dans RiskBonSim ! Ce guide vous accompagne pas à pas pour comprendre le fonctionnement de l'application. Que vous soyez étudiant, enseignant ou analyste, ce tutoriel vous aidera à : modéliser une obligation, importer un portefeuille, analyser les risques, exporter vos résultats…",

        "tuto_bond_title": "1️⃣ Simuler une obligation",
        "tuto_bond_text": "Dans l’onglet « Obligation », entrez les paramètres : nom, coupon, maturité, fréquence. L'application calcule le prix théorique, affiche les flux futurs et vous permet d'explorer la sensibilité au taux. 🧮 Vous pouvez visualiser les flux avec un graphe clair.",

        "tuto_portfolio_title": "2️⃣ Importer un portefeuille CSV",
        "tuto_portfolio_text": "Dans l’onglet « Portefeuille », importez un fichier CSV avec les colonnes attendues. L'application valide les pondérations, calcule YTM, duration, convexité, et affiche une table claire. Les métriques agrégées sont aussi disponibles en haut de page.",

        "tuto_risk_title": "3️⃣ Analyser les risques",
        "tuto_risk_text": "Utilisez l’onglet « Risque » pour appliquer un choc de taux ou simuler des scénarios de courbe (flattening, steepening). Vous pouvez aussi saisir une courbe personnalisée ou importer une courbe depuis un fichier CSV. Enfin, la VaR paramétrique et la distribution simulée P&L permettent d’évaluer les pertes potentielles.",

        "tuto_export_title": "4️⃣ Exporter les résultats",
        "tuto_export_text": "À tout moment, vous pouvez exporter vos données traitées au format CSV. Les tableaux, flux, résultats de VaR ou stress tests sont tous téléchargeables.",

        "tuto_download_label": "Télécharger le PDF complet du tutoriel",
        "tuto_pdf_pending": "PDF bientôt disponible.",

        #A propos
        "about_title": "À propos de RiskBonSim",
        "about_description": "RiskBonSim est un simulateur interactif conçu pour aider étudiants, analystes et enseignants à explorer les risques et caractéristiques d’un portefeuille obligataire.",

        "about_tech_title": "Technologies utilisées",
        "about_tech_streamlit": "Interface construite avec Streamlit pour une expérience fluide et moderne.",
        "about_tech_matplotlib": "Graphiques générés avec Matplotlib pour illustrer les flux et indicateurs.",
        "about_tech_numpy": "Calculs numériques via NumPy (VaR, rendements simulés…).",
        "about_tech_modular": "Architecture modulaire (src/, ui/, risk/, instruments/) pour une bonne maintenabilité.",

        "about_contact_title": "Contact",
        "about_contact_text": "Pour toute suggestion ou retour, contactez-nous via GitHub ou par e-mail.<br><br>📧 Email : <a href='mailto:ange.fogoum@groupe-esigelec.org'>ange.fogoum@groupe-esigelec.org</a><br>🌐 GitHub : <a href='https://github.com/Angef001' target='_blank'>github.com/Angef001</a><br>💼 LinkedIn : <a href='https://www.linkedin.com/in/rostandk916/' target='_blank'>linkedin.com/in/rostandk916</a>"

    },

    "en": {
        "app_title": "📊 RiskBonSim",
        "app_subtitle": "Interactive bond portfolio simulator",

        "lang_select": "🌐 Language / Langue",
        "nav_home": "Home",
        "nav_bond": "Bond",
        "nav_portfolio": "Portfolio",
        "nav_risk": "Risk",
        "sidebar_info": "Information",

        "link_tuto": "Tutorial",
        "link_about": "About",
        "nav_section": "Navigation",

        #Acceuil section
        "home_title": "🏠 Welcome to RiskBonSim",
        "home_subtitle": "A modern app to model, simulate and analyze a bond portfolio.",

        "box_flux_title": "💼 Compute price and cashflows",
        "box_flux_desc": "Simulate bond cashflows based on its parameters: coupon, maturity, frequency…",

        "box_risk_title": "📉 Market risk",
        "box_risk_desc": "Estimate VaR, apply stress tests, and measure potential losses.",

        "box_duration_title": "📊 Duration & Convexity",
        "box_duration_desc": "Analyze the portfolio’s sensitivity and curvature indicators.",

        "box_export_title": "📤 Export",
        "box_export_desc": "Download processed data and visualizations as CSV.",


        # Bond tab
        "bond_section_title": "💼 Bond Parameters",
        "bond_label_name": "Name",
        "bond_label_ytm": "Estimated YTM (%)",
        "bond_label_maturity": "Maturity (years)",
        "bond_label_coupon": "Coupon rate (%)",
        "bond_label_frequency": "Payment frequency",
        "bond_label_price": "Market price (€)",
        "bond_label_discount": "Discount rate (%)",
        "bond_price_result": "💰 Theoretical price:",
        "bond_flux_title": "📈 Future cashflows",
        "bond_flux_xlabel": "Period",
        "bond_flux_ylabel": "Amount (€)",
        "bond_flux_graphtitle": "Future cashflows",


        # Portfolio
        "portfolio_section_title": "📂 Import a bond portfolio",
        "portfolio_upload_label": "Select a CSV file",
        "portfolio_weight_warning": "⚠️ The total weights sum to {somme:.2f}% (must be 100%)",
        "portfolio_weight_valid": "✅ Valid weights (sum = 100%)",
        "portfolio_loaded": "{nb} bonds loaded ✅",
        "portfolio_table_title": "📋 Portfolio details",
        "portfolio_agg_title": "📐 Aggregated metrics",
        "portfolio_export_label": "📥 Export as CSV",
        "metric_ytm_mean": "Average YTM (%)",
        "metric_duration": "Modified Duration (weighted)",
        "metric_convexite": "Convexity (weighted)",

        # Risk
            "risk_header": "⚠️ Market Risk Analysis",
        "risk_instructions": "👉 First, import a portfolio in the previous tab.",
        "parallel_shock": "📉 Parallel Rate Shock",
        "shock_slider": "Shock amplitude (bps)",
        "apply_shock_btn": "Apply Shock",
        "init_value": "📊 Initial Value",
        "after_shock": "📉 Value After Shock",
        "loss_label": "🛑 Loss (Δ)",

        "scenario_title": "📉 Curve Scenarios (Flattening / Steepening)",
        "scenario_select": "Select a scenario",
        "scenario_none": "Aucun",
        "amplitude_label": "Amplitude (bps)",
        "scenario_btn": "Apply Scenario",

        "csv_curve_upload": "📁 Upload a Custom Yield Curve (CSV)",
        "csv_file_label": "Yield curve CSV file",
        "curve_loaded": "📈 Curve loaded:",
        "apply_curve_btn": "💰 Apply CSV curve to portfolio",
        "custom_curve_value": "📊 Portfolio Value with CSV Curve:",
        "curve_before": "Before",
        "curve_after": "After",
        "curve_chart_title": "CSV Curve Impact",

        "manual_curve": "✍️ Enter a Custom Yield Curve",
        "nb_points": "Number of points",
        "maturity_x": "Maturity {i} (years)",
        "rate_y": "Rate {i} (%)",
        "manual_plot": "Plot Manual Curve",
        "manual_apply": "💰 Apply Curve to Portfolio",
        "manual_value": "💼 Portfolio Value with Manual Curve:",
        "manual_chart_title": "Manual Curve Impact",

        "var_title": "📉 Parametric VaR Calculation",
        "vol_input": "Volatilities (%) separated by commas",
        "corr_input": "Correlation matrix (line by line, comma-separated)",
        "var_button": "🧮 Compute VaR",
        "var_result": "📉 VaR (95%)",

        "hist_title": "📊 Simulated Loss Distribution (P&L)",
        "hist_button": "📈 Generate Histogram",
        "sim_days_label": "Number of simulated days",
        "mean_label": "Mean P&L",
        "min_label": "Min P&L",
        "x_label": "P&L (€)",
        "y_label": "Frequency",
        "graph_title": "Simulated Loss Distribution (P&L)",

        #Tutoriel
        "tuto_intro_title": "Interactive Tutorial",
        "tuto_intro_text": "Welcome to RiskBonSim! This guide walks you through each step of using the app. Whether you're a student, teacher, or analyst, this tutorial will help you model bonds, import portfolios, analyze risks, and export your results.",

        "tuto_bond_title": "1️⃣ Simulate a Bond",
        "tuto_bond_text": "In the 'Bond' tab, enter parameters: name, coupon, maturity, frequency. The app computes the theoretical price, shows the future cashflows, and lets you test sensitivity to discount rates. 🧮 You’ll also get a clear bar graph.",

        "tuto_portfolio_title": "2️⃣ Import a Portfolio CSV",
        "tuto_portfolio_text": "In the 'Portfolio' tab, upload a CSV with the required bond data. The app checks weights, computes global metrics (YTM, duration, convexity), and displays them in a clean table along with a summary at the top.",

        "tuto_risk_title": "3️⃣ Risk Analysis",
        "tuto_risk_text": "Use the 'Risk' tab to apply parallel rate shocks or curve scenarios (flattening, steepening). You can also define a manual curve or import one from CSV. Lastly, the VaR and simulated P&L distribution help estimate potential losses.",

        "tuto_export_title": "4️⃣ Export Results",
        "tuto_export_text": "You can export your processed data at any time as a CSV file. Tables, flows, VaR and stress test results are all available for download.",

        "tuto_download_label": "Download the full PDF tutorial",
        "tuto_pdf_pending": "PDF coming soon.",

        #A propos
        "about_title": "About RiskBonSim",
        "about_description": "RiskBonSim is an interactive simulator designed to help students, analysts and teachers explore the risk and structure of bond portfolios.",

        "about_tech_title": "Technologies Used",
        "about_tech_streamlit": "Built with Streamlit for a modern and fluid interface.",
        "about_tech_matplotlib": "Graphs rendered with Matplotlib for cashflows and analytics.",
        "about_tech_numpy": "Numerical computations powered by NumPy (VaR, simulations…).",
        "about_tech_modular": "Modular architecture (src/, ui/, risk/, instruments/) for easy maintenance.",

        "about_contact_title": "Contact",
        "about_contact_text": "For suggestions or feedback, please reach out via GitHub or email.<br><br>📧 Email: <a href='mailto:ange.fogoum@groupe-esigelec.org'>ange.fogoum@groupe-esigelec.org</a><br>🌐 GitHub: <a href='https://github.com/Angef001' target='_blank'>github.com/Angef001</a><br>💼 LinkedIn: <a href='https://www.linkedin.com/in/rostandk916/' target='_blank'>linkedin.com/in/rostandk916</a>"

    }
}
