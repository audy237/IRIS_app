import streamlit as st
st.title("welcome to NGODOBO Cyrille Dasboard for IRIS Work January 2025")
st.subheader("creating dasboard...")
st.write("Hello Word")
st.sidebar.slider('valeur', , 10)
1234
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
