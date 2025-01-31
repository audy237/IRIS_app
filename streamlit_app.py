import streamlit as st
st.title("welcome to NGODOBO Cyrille Dasboard for IRIS Work January 2025")
st.subheader("creating dasboard...")
st.write("Hello Word")
st.sidebar.slider('valeur', 0, 10)
treamlit --help
streamlit run your_script.py
streamlit hello
streamlit config show
$ streamlit cache clear
$ streamlit docs
streamlit --version
pip uninstall streamlit
pip install streamlit-nightly --upgrade
"""
Ceci est un texte.
"""
"Ceci est aussi un texte."
1234
df
st.text('Texte avec st.text')
st.markdown('Texte avec st.markdown')
st.latex(r'e^{i\pi} + 1 = 0')
st.write('Objets: ', df, mon_variable, fonction, keras)
st.title('Mon titre')
st.header('Mon en-tête')
st.subheader('Mon sous-titre')
st.code('for i in range(8): \n print(i)')
st.dataframe(data)
st.table(data.iloc[0:10])
st.json({'foo': 'bar', 'fu': 'he'})
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.graphviz_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.map(data)
st.image('header.png')
st.audio(data)
st.video(data)
st.button('Cliquez ici')
st.checkbox('Cochez-moi')
st.radio('Radio', [1, 2, 3])
st.selectbox('Sélectionnez', [1, 2, 3])
st.multiselect('Multisélection', [1, 2, 3])
st.slider('Faites glisser', min_value=0, max_value=10)
st.text_input('Entrez du texte')
st.number_input('Entrez un nombre')
st.date_input('Entrez une date')
st.time_input('Entrez une heure')
st.file_uploader('Téléchargez un fichier')
st.beta_color_picker('Choisissez une couleur')
valeur_slider = st.slider('Valeur du slider', 0, 10)
st.stop()
st.echo()
with st.echo('code'):
    st.write('Ce code sera à la fois exécuté et imprimé')
  st.progress(variable_de_progression_de_1_à_100)

with st.spinner(text='En cours')
    time.sleep(5)
    st.success('Terminé !')

st.balloons()

st.error('Message d\'erreur')
st.warning('Message d\'avertissement')
st.info('Message d\'information')
st.success('Message de succès')

st.exception(e)
my_placeholder = st.empty()
my_placeholder.text("Texte remplacé !")

st.help(pandas.DataFrame)

st.get_option(clé)
st.set_option(clé, valeur)

st.beta_set_page_config(layout="wide")
data_generator = st.experimental_data_editor(data)
my_table = st.table(df)
my_table.add_rows(df2)

my_chart = st.line_chart(df)
my_chart.add_rows(df2)
@st.cache_data
def foo(bar):
    # Muter bar
    return data

# Premier appel
data = foo(ref1) 
# Deuxième appel
data2 = foo(ref2) # Pas exécuté car les arguments sont les mêmes

# Débogage
st.experimental_rerun()
