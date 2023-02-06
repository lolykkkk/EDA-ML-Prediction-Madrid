# HOLA, COMENCEMOS CON LA APP

#-------------------- LIBRERÍAS NECESARIAS-------------------------#
from ctypes import alignment
import fire
from matplotlib.pyplot import FixedFormatter, colorbar
from pytz_deprecation_shim import fixed_offset_timezone
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly_express as px
import plotly.graph_objects as go
import time
import base64
import requests
from streamlit_option_menu import option_menu
st.set_option('deprecation.showPyplotGlobalUse', False)

#para que no nos aparezcan ciertos mensajes de error
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# Surpress warnings:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn




#---------------------------- COSAS QUE PODEMOS USAR EN TODA NUESTRA APP ----------------------------

#------------------ CONFIGURACIÓN DE PÁGINA ----------------

st.set_page_config(page_title="AIRBNB EN MADRID | SILVILIO",
        layout="centered",
        page_icon="🏠",
        )


# Creo una hoja de estilo para toda la página
st.markdown(
    f"""
    <style>
    [data-testid="stHeader"] {{
    background-color: rgba(0, 0, 0, 0);
    }}
    [data-testid="stSidebar"]{{                 
    background-color: rgba(0, 0, 0, 0);
    border: 0.5px solid #ff4b4b;
        }}
    [data-testid="stMarkdownContainer"]{{                 
    color: #ff5a60;
        }}
    .menu .nav-item .nav-link.active[data-v-4323f8ce] {{
    background-color: #dddad;
    }}
    </style>
    """
 , unsafe_allow_html=True)



#Establecemos la imagen de fondo de la app
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
     <style>
        .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("Imágenes/background3.png")



# Leemos el Dataset
df = pd.read_csv("airbnb_anuncios.csv")



### ---------------   PREPROCESAMIENTO    -------------------  ### 

# Borramos las variables que no nos interesan
df.drop(['name','id','host_name','last_review'], axis=1, inplace=True)

df["price"]= df["price"].astype(float)
df['price'] = df['price'].round(2)




#------------------ COMIENZA NUESTRA APP  -----------------------------------------------------

#Imagen con efecto máscara de recorte usada como título.
st.image("Imágenes/transparente.png", width="120%", use_column_width=True)


#Menú horizontal
menu = option_menu(

    menu_title=None,
    options=["Contexto", "Dataframe", "EDA", "Mapas", "Modelo"],
    icons= ["house", "table", "clipboard-plus", "pin-map", "wrench"],
    default_index=0,
    orientation="horizontal",
    
)



#------------------ NAVEGANDO POR EL MENÚ  -----------------------------------------------------


###################### MENU INTRODUCCIÓN contexto ################################

#Título
if menu =="Contexto":
    st.markdown("<h2 style='text-align: center; color: #ff5a60;'>Introducción</h2>" ,unsafe_allow_html=True) #título


    #Comienza el párrafo introductorio
    st.markdown(
                             """
    <div style="border: 0px solid #ff5a60; padding: 10px; color: #000000;">

    **Airbnb** es una plataforma que permite a los usuarios alquilar viviendas o habitaciones de manera temporal.
    La empresa se fundó en 2008, lleva funcionando en Madrid desde 2009 y desde entonces ha crecido enormemente.
    Hasta el punto de generar varios debates y controversias, que han provocado que se ponga el foco en cómo está afectando 
    a la oferta de alojamiento en la ciudad.
    """, unsafe_allow_html=True)

    st.image(r"Imágenes\captura periódico.PNG")     # Imagen para romper la dinámica de todo texto
    st.write(
            "<div style='text-align:right;color:red;font-size:12px'>businessinsider.es</div>",
            unsafe_allow_html=True)
    st.markdown(
                             """
    <div style="border: 0px solid #ff5a60; padding: 10px; color: #000000;">
    En este proyecto nos enfocaremos en comprender mejor la presencia de Airbnb en Madrid.
    El objetivo será utilizar los datos de la plataforma para analizar tendencias en el número de viviendas disponibles, precios, ubicaciones,
    y cómo estos factores están afectando al mercado del alojamiento en la ciudad.
    Por último, se creará un modelo predictivo que puede ayudar a los propietarios a establecer precios realistas para sus propiedades. 
    """, unsafe_allow_html=True)
    

    
    # Termino mi pestaña de Contexto con una imagen de Madrid generada de forma random 

    # Mi llave de acceso de la API de Unplash (web de fotos libres de derechos)
    access_key = "95x8luVRq3rRplbhZUaHJHWESu4D1lwNvGLmVpEn4rk"

    def get_random_photo():
        """
        Esta función hace una solicitud a la API de Unsplash para obtener
        una foto aleatoria de Madrid. Devuelve la URL de la foto.
        """
        # Realiza una solicitud GET a la API de Unsplash para obtener una foto aleatoria de Madrid
        response = requests.get(f"https://api.unsplash.com/photos/random?query=Madrid+ciudad&client_id={access_key}")

        # Obtiene los datos JSON de la respuesta
        data = response.json()

        # Coge como resultado la URL de la foto
        return data["urls"]["regular"]


    def main():
        """
        Esta función crea una variable para almacenar la URL de la foto,
        la muestra en la pantalla con una leyenda, y también crea
        un botón para generar una nueva imagen.
        """
        # Crear la variable photo_url y asignarle el resultado de la función get_random_photo()
        photo_url = get_random_photo()

        
        # Mostrar imagen y leyenda
        photo = st.image(photo_url, width=500, use_column_width=True)
        st.write(
            "<div style='text-align:right;color:red;font-size:14px'>Imagen autogenerada con la API de Unplash</div>",
            unsafe_allow_html=True)
        # Mostrar botón "Generar otra imagen"
        if st.button("Generar otra imagen random de Madrid"):
            # Asignar nuevo valor a la variable photo_url
            #photo_url = get_random_photo()
            # Reemplazar la imagen por la nueva
            photo.image(photo_url, width=500, use_column_width=True)
            
    if __name__ == "__main__":
        main()      # Esta línea de código comprueba si se ejecuta el archivo como un programa independiente.



###################### MENU DATAFRAME ################################

if menu == "Dataframe": 
    
    # Volvemos a cargar otra imagen de fondo, porque el sidebar mueve el contenido, y tenemos que cambiar nuestro fondo.
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
            .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local(r"Imágenes\background5.png")   

    # Título
    st.markdown("<h2 style='text-align: center; color: #ff5a60;'>Dataframe</h2>" ,unsafe_allow_html=True)


    #-------------------------    SIDEBAR       -----------------------------

   
    with st.sidebar:
        #Imagen que sirve de título
        st.image(r"Imágenes\sidebar.png")

        # Elección de barrio
        st.markdown("<h2 style='color: #ff5a60;'>Barrio: </h2>" ,unsafe_allow_html=True)
        seleccion_barrio = st.multiselect("", df["neighbourhood_group"].unique(), default=["Centro"])
            

        # Elección de Tipo de habitación
        st.markdown("<h2 style='color: #ff5a60;'>Tipo de habitación: </h2>" ,unsafe_allow_html=True)
        seleccion_habitacion = st.multiselect("", df["room_type"].unique(), default=["Entire home/apt"])


        # Elección de precio
        st.markdown("<h2 style='color: #ff5a60;'>Precio: </h2>" ,unsafe_allow_html=True)
        precio = df["price"].unique().tolist()
        seleccion_precio = st.slider("", min_value= 8 , max_value = 1100, value= (8, 1100))


        # Elección de número de reviews
        st.markdown("<h2 style='color: #ff5a60;'>Número de reviews: </h2>" ,unsafe_allow_html=True)
        reviews = df["number_of_reviews"].unique().tolist()
        seleccion_reviews = st.slider("", min_value= 0 , max_value = 133, value= (0, 133))


        # Elección de mínimo de noches
        st.markdown("<h2 style='color: #ff5a60;'>Mínimo noches: </h2>" ,unsafe_allow_html=True)
        noches = df["minimum_nights"].unique().tolist()
        seleccion_noches = st.slider("", min_value= 1 , max_value = 90, value= (1, 90))


    # En el código de selección de filas, verifica si show_full_df es True
    seleccion_df = df.query("neighbourhood_group == @seleccion_barrio & room_type == @seleccion_habitacion & price >= @seleccion_precio[0] & price <= @seleccion_precio[1] & number_of_reviews >= @seleccion_reviews[0] & number_of_reviews <= @seleccion_reviews[1] & minimum_nights >= @seleccion_noches[0] & minimum_nights <= @seleccion_noches[1]")
    st.dataframe(seleccion_df)
     
    # Indicamos después de cada filtrado los resultados obtenidos debajo.
    resultado_df = seleccion_df.shape[0]
    st.write(f"<div style='color: #ff5a60; text-align:center;'>Resultados obtenidos: <b>{resultado_df}</b></div>", unsafe_allow_html=True)
   

    




###################### MENÚ ANÁLISIS EXPLORATORIO DE DATOS ################################

if menu == "EDA":

    # Título
    st.markdown("<h2 style='text-align: center; color: #ff5a60;'>Análisis exploratorio</h2>" ,unsafe_allow_html=True) #título

    # Recurso de título de gráfica que se usará mucho en la página
    st.markdown("""
        <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Correlación de variables</p>
        """, unsafe_allow_html=True)

    # Comentario gráfica de correlación
    st.markdown("""
    <p style="text-align: left; color: black;">
    Esta gráfica nos muestra la correlación entre las diferentes variables del dataset utilizando el método Kendall.
    Es útil para explorar los patrones de relación entre ellas y ver si hay alguna significativa.
    La realidad es que no encontramos ninguna correlación importante.
    """, unsafe_allow_html=True)

    # Gráfica de correlación
    corr = df.corr(method='kendall')
    plt.figure(figsize=(14,7))
    sns.heatmap(corr, annot=True, cmap="YlOrRd" )
    st.pyplot() 
    

    # Separación
    
    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True) # línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


    # Título alojamientos según el barrio
    st.markdown("""
        <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Distribución de los alojamientos según el barrio</p>
        """, unsafe_allow_html=True)

    # Comentario alojamientos según el barrio
    st.markdown("""
    <p style="text-align: left; color: black;">
    Esta gráfica de barras muestra la distribución de los grupos de barrios en la base de datos de Airbnb Madrid.
    Se puede ver claramente cuáles son los barrios más populares para los huéspedes de Airbnb, donde la gran mayoría
    se encuentran en Centro.
    """, unsafe_allow_html=True)

    # Gráfica alojamientos según el barrio
    fig = go.Figure(data=[go.Bar(
            x=df['neighbourhood_group'].value_counts().index,
            y=df['neighbourhood_group'].value_counts(),
            text=df['neighbourhood_group'].value_counts(),
            marker=dict(color='white')
            )])
    fig.update_layout(title='Neighbourhood Group',
                 plot_bgcolor="#ff5a60",
                 )
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")
    ),
    yaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")))
    st.plotly_chart(fig)


    # Separación
   
    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True)
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    

    # Título de alojamientos según el barrio sin agrupar
    st.markdown("""
        <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Distribución de los alojamientos según el barrio sin agrupar</p>
        """, unsafe_allow_html=True)

    # Comentario de alojamientos según el barrio sin agrupar
    st.markdown("""
    <p style="text-align: left; color: black;">
    Esta gráfica de barras muestra la distribución de los grupos de barrios por separado y sin agrupar.
    Parecido al gráfico anterior, se puede ver cuáles son los barrios más populares para los huéspedes de Airbnb.
    Los barrios más populares son Embajadores, Universidad, Palacio, Sol, Justicia y Cortes.
    """, unsafe_allow_html=True)


    # Gráfica de alojamientos según el barrio sin agrupar
    fig = go.Figure(data=[go.Bar(
    x=df['neighbourhood'].value_counts().index,
    y=df['neighbourhood'].value_counts(),
    marker=dict(color='white')
    )])

    fig.update_layout(title='Neighbourhood',
                    plot_bgcolor="#ff5a60",
                    width=690,
                    height=600)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")
    ),
    yaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")))
    
    st.plotly_chart(fig)

    
    # Separación
    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True) #línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


    # Título de tipo de habitaciones
    st.markdown("""
        <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Representación de los tipos de habitación que se ofertan</p>
        """, unsafe_allow_html=True)

    # Comentario tipo de habitaciones
    st.markdown("""
    <p style="text-align: left; color: black;">
    Podemos ver representado a continuación la distribución de los tipos de habitaciones de Airbnb Madrid.
    Observamos claramente que el tipo de alojamiento más popular es la casa entera, seguida de la habitación privada.
    Y a menor nivel, encontramos las habitaciones de hoteles dentro de la plataforma y la habitación compartida. 
    """, unsafe_allow_html=True)

    # Gráfica tipo de habitaciones
    fig = go.Figure(data=[go.Bar(
    x=df['room_type'].value_counts().index,
    y=df['room_type'].value_counts(),
    marker=dict(color='white')
    )])

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")
    ),
    yaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")))
    fig.update_layout(title='Room Type',
                plot_bgcolor="#ff5a60",
                 width=690,
                 height=400)
    st.plotly_chart(fig)


    # Separación
    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True) #línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    # Título de disponibilidad de los alojamientos
    st.markdown("""
        <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Disponibilidad de los alojamientos por barrios</p>
        """, unsafe_allow_html=True)

    # Comentario de disponibilidad de los alojamientos
    st.markdown("""
    <p style="text-align: left; color: black;">
    Esta gráfica de cajas muestra la disponibilidad de los alojamiento en los distintos barrios de Madrid.
    Se pueden ver los cuartiles para cada vecindario, lo que nos da una idea de la variabilidad de la disponibilidad de alojamiento.
    A su vez, este gráfico representa la media de días que están los alojamientos disponibles para cada barrio.
    """, unsafe_allow_html=True)

    # Gráfica de disponibilidad de los alojamientos
    fig = px.box(df, x='neighbourhood_group', y='availability_365')
    fig.update_layout(title='Availability by Neighbourhood Group')
    
    fig.update_traces(marker=dict(line=dict(color='white', width=2)))

    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")
    ),
    yaxis=dict(title=dict(font=dict(color="#ff5a60")),
    tickfont=dict(color="#ff5a60")))
    fig.update_layout(title='Room Type',
                plot_bgcolor="#ff5a60",
                 width=690,
                 height=500)
    st.plotly_chart(fig)


 #-------------





  
###################### MENÚ MAPAS ################################

if menu =="Mapas":

    #Título
    st.markdown("<h2 style='text-align: center; color: #ff5a60;'>Mapas interactivos</h2>" ,unsafe_allow_html=True) #título

    # Crea una lista de opciones para seleccionar el mapa que queramos
    options = ["Mapa Madrid: [Grupos de barrios]", "Mapa Madrid: [Barrios]", "Mapa Madrid: [Tipos de alojamiento]", "Mapa Madrid: [Disponibilidad]", "Mapa Madrid: [Precio]"]

    # Crea un selectbox con las opciones
    selected_option = st.selectbox("Selecciona el tipo de mapa:", options)

    # Crea un boton para ejecutar la accion
    if selected_option == "Mapa Madrid: [Grupos de barrios]":

            # Mostrar mapa 1
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='neighbourhood_group',
            color_discrete_sequence=px.colors.sequential.Plasma)
            fig.update_layout(mapbox_style='open-street-map',
            paper_bgcolor="rgba(0,0,0,0)",
                 xaxis=dict(title=dict(font=dict(color="#ff5a60"))),
                 yaxis=dict(title=dict(font=dict(color="#ff5a60"))))
            fig.update_layout(legend=dict(font=dict(color='#ff5a60')))
            fig.update_layout(mapbox_zoom=9)
            fig.update_layout(shapes=[
            dict(
                type='rect',xref='paper',yref='paper',x0=0, y0=0,x1=1,y1=1,line=dict(color="#ff5a60",width=2))])
        
            st.plotly_chart(fig)

            # Título mapa 1
            st.markdown("""
            <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mapa interactivo de Madrid distribuido por grupos de barrios</p>
            """, unsafe_allow_html=True)

            # Comentario mapa 1
            st.markdown("""
            <p style="text-align: left; color: black;">
            Con este mapa de dispersión de Mapbox podemos ubicar todos los alojamientos de Airbnb Madrid.
            De un rápido vistazo podemos ver como se colorean los diferentes barrios en los que está distribuida nuestra variable.
            
            """, unsafe_allow_html=True)


            
    elif selected_option == "Mapa Madrid: [Barrios]":
            
            # Mostrar mapa 2
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='neighbourhood',
            color_discrete_sequence=px.colors.sequential.Plasma)
            fig.update_layout(mapbox_style='open-street-map',
            paper_bgcolor="rgba(0,0,0,0)",
                 xaxis=dict(title=dict(font=dict(color="#ff5a60"))),
                 yaxis=dict(title=dict(font=dict(color="#ff5a60"))))
            fig.update_layout(legend=dict(font=dict(color='#ff5a60')))
            fig.update_layout(mapbox_zoom=9)
            fig.update_layout(shapes=[
            dict(
                type='rect',xref='paper',yref='paper',x0=0, y0=0,x1=1,y1=1,line=dict(color="#ff5a60",width=2))])
            
            st.plotly_chart(fig)

            # Título mapa 2
            st.markdown("""
            <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mapa interactivo de Madrid distribuido por los barrios independientes</p>
            """, unsafe_allow_html=True)

            # Comentario mapa 2
            st.markdown("""
            <p style="text-align: left; color: black;">
            De igual manera, con este mapa interactivo de dispersión podemos ver la distribución de los alojamientos por los diferentes barrios.
            """, unsafe_allow_html=True)



            
    elif selected_option == "Mapa Madrid: [Tipos de alojamiento]":
            
            # Mostrar mapa 3
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude',color='room_type',
            color_discrete_sequence=px.colors.qualitative.Dark2)
            fig.update_layout(mapbox_style='open-street-map',
            paper_bgcolor="rgba(0,0,0,0)",
                 xaxis=dict(title=dict(font=dict(color="#ff5a60"))),
                 yaxis=dict(title=dict(font=dict(color="#ff5a60"))))
            fig.update_layout(legend=dict(font=dict(color='#ff5a60')))
            fig.update_layout(mapbox_zoom=9)
            fig.update_layout(shapes=[
            dict(
                type='rect',xref='paper',yref='paper',x0=0, y0=0,x1=1,y1=1,line=dict(color="#ff5a60",width=2))])

            st.plotly_chart(fig)

            # título mapa 3
            st.markdown("""
            <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mapa interactivo de Madrid distribuido por los tipos de alojamiento</p>
            """, unsafe_allow_html=True)

            # Comentario mapa 3
            st.markdown("""
            <p style="text-align: left; color: black;">
            De esta manera podemos ver la distribución de las casas por el tipo de alojamiento. Lo interesante será encontrar
            algún patrón que nos muestre por qué en determinadas zonas hay un tipo de alojamiento o no. En este caso, podemos detectar
            que la opción de habitación privada es más común en las afueras de la ciudad. 
            """, unsafe_allow_html=True)


            
    elif selected_option == "Mapa Madrid: [Disponibilidad]":
            
            # Mostrar mapa 4
            fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='availability_365',
            color_discrete_sequence=px.colors.qualitative.Dark2)
            fig.update_layout(mapbox_style='open-street-map')
            fig.update_layout(mapbox_style='open-street-map',
                    paper_bgcolor="rgba(0,0,0,0)",
                        xaxis=dict(title=dict(font=dict(color="#ff5a60"))),
                        yaxis=dict(title=dict(font=dict(color="#ff5a60"))))
            fig.update_layout(mapbox_zoom=9)
            fig.update_layout(shapes=[
                    dict(
                        type='rect',xref='paper',yref='paper',x0=0, y0=0,x1=1,y1=1,line=dict(color="#ff5a60",width=2))])
            fig.update_layout(mapbox_style='open-street-map', coloraxis_colorbar=dict(
            titlefont=dict(size=12, color='#ff5a60'),
            tickfont=dict(size=14, color='#ff5a60')
                ))

            st.plotly_chart(fig)

            # Título mapa 4
            st.markdown("""
            <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mapa interactivo de Madrid distribuido por la disponibilidad de los alojamientos</p>
            """, unsafe_allow_html=True)

            # Comentario mapa 4
            st.markdown("""
            <p style="text-align: left; color: black;">
            En este caso observamos la ubicación de los alojamientos de Airbnb Madrid a lo largo del mapa por su disponibilidad.
            Se usó el color para representar el nivel de disponibilidad, con colores más oscuros indicando una menor disponibilidad.
            Es complicado identificar un patrón en especial que nos indique que en una determinada zona los alquileres
            tienen más disponibilidad o menos al año.
            """, unsafe_allow_html=True)
            

    elif selected_option == "Mapa Madrid: [Precio]":


        # Trataremos los precios desorbitados como errores y procedemos a limpiar los valores atípicos para la columna "price".
        def eliminar_outliers_columna(dataset, columna):
            # Calcular los cuartiles
            Q1 = dataset[columna].quantile(0.25)
            Q3 = dataset[columna].quantile(0.75)
            IQR = Q3 - Q1

            # Identificar los outliers
            outliers = (dataset[columna] < (Q1 - 1.5 * IQR)) | (dataset[columna] > (Q3 + 1.5 * IQR))
            
            # Eliminar los outliers
            dataset_sin_outliers = dataset[~outliers]
            return dataset_sin_outliers

        # Aplicamos la función para quitar los valores atípicos
        df_sin_outliers = eliminar_outliers_columna(df, "price")

        # Importamos la librería para preprocesar la columna price
        from sklearn.preprocessing import MinMaxScaler
        # Usamos el minmaxscaler para normalizar la variable
        scaler = MinMaxScaler()
        df_sin_outliers['price'] = scaler.fit_transform(df_sin_outliers[['price']])

        # Mostrar mapa 5
        fig = px.scatter_mapbox(df_sin_outliers, lat='latitude', lon='longitude', color='price',
        color_continuous_scale=px.colors.diverging.RdYlGn)
        fig.update_layout(mapbox_style='open-street-map')
        fig.update_layout(mapbox_style='open-street-map',
                    paper_bgcolor="rgba(0,0,0,0)",
                        xaxis=dict(title=dict(font=dict(color="#ff5a60"))),
                        yaxis=dict(title=dict(font=dict(color="#ff5a60"))))
        fig.update_layout(mapbox_zoom=9)
        fig.update_layout(shapes=[
                    dict(
                        type='rect',xref='paper',yref='paper',x0=0, y0=0,x1=1,y1=1,line=dict(color="#ff5a60",width=2))])
        fig.update_layout(mapbox_style='open-street-map', coloraxis_colorbar=dict(
        titlefont=dict(size=12, color='#ff5a60'),
        tickfont=dict(size=14, color='#ff5a60')
                ))
        st.plotly_chart(fig)

        # Título mapa 5
        st.markdown("""
            <p style="text-align: left; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mapa interactivo de Madrid distribuido por el precio de los alojamientos</p>
            """, unsafe_allow_html=True)

        # Comentario mapa 5
        st.markdown("""
            <p style="text-align: left; color: black;">
            Antes de realizar este gráfico, he tenido que preprocesar la variable price, ya que es común que algunos propietarios
            pongan en la plataforma precios desorbitados que dificultan el análisis.
            Por un lado, he eliminado los valores atípicos y, por otro, he escalado los precios de los alojamientos al rango
            entre 0 y 1. De esta manera normalizo los datos para que sea más sencilla su visualización y manipulación.
            """, unsafe_allow_html=True)




###################### MENÚ MODELO ################################

if menu =="Modelo":

    # Llamamos a la función para volver a cambiar la imagen de fondo
    add_bg_from_local(r"Imágenes\background5.png")


    # Título
    st.markdown("<h2 style='text-align: center; color: #ff5a60;'>Modelo de predicción con Fast Machine Learning</h2>" ,unsafe_allow_html=True) #título
    


    ##### MODELO DE PREDICCIÓN #### ----------------

    # Importamos librerías necesarias
    import random 
    from sklearn.cluster import KMeans 
    from sklearn.datasets import make_blobs
    import pycaret
    from pycaret.regression import *


    ## No sin antes, PREPROCESAMIENTO #####
    #Hago copia de seguridad del dataframe
    df_new = df

    # Creo una nueva variable aplicando una etiqueta numérica a cada barrio.
    df_new['neighbourhood_labels'] = df['neighbourhood'].astype('category').cat.codes

    #Para saber qué etiqueta tiene cada barrio creo otro dataframe solo con esa información.
    labels_df = pd.DataFrame(columns=['neighbourhood', 'neighbourhood_labels'])
    #recorrer los barrios
    for neighbourhood in df['neighbourhood'].unique():
        # asignar etiqueta
        labels_df.loc[len(labels_df)] = [neighbourhood, df[df['neighbourhood'] == neighbourhood]['neighbourhood_labels'].iloc[0]]

    #Creo un diccionario de etiquetas para room_type
    room_type_labels = {'Entire home/apt': 0, 'Private room': 1, 'Hotel room': 2, "Shared room": 3}

   
    #Lo aplico al df
    df_new['room_type_num'] = df['room_type'].map(room_type_labels)

    df_new = df_new[['price', 'neighbourhood_labels', 'room_type_num', "availability_365", "minimum_nights", "calculated_host_listings_count", "number_of_reviews", "reviews_per_month"]]
    
    

    #### Cargamos el modelo creado ####
    model =  load_model('modelo_airbnb_madrid_fastml_bueno')



    ## ----------------- SIDEBAR ----------
    # Datos de entrada  
    with st.sidebar:

        # Selección del barrio
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Selección de barrio</p>
        """, unsafe_allow_html=True)
        neighbourhood_labels =  st.text_input("Más abajo podrás ver el nº de cada barrio  **|**  **Ingresa un número del 0 al 126:**", "0")
        neighbourhood_labels = float(neighbourhood_labels)
        
        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
        

        # Selección del tipo de habitación
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Tipo de habitación</p>
        """, unsafe_allow_html=True)
        room_type_num =  st.text_input("Entire home: 0, Private room: 1, Hotel room: 2, Shared room: 3  **|**  **Ingresa un número del 0 al 3:** ", "0")
        room_type_num = float(room_type_num)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    

        # Selección de la disponibilidad
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Disponibilidad de la vivienda</p>
        """, unsafe_allow_html=True)
        availability_365 =  st.text_input("Ingresa un número del 1 al 365: ", "1")
        availability_365 = float(availability_365)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


        # Selección del mínimo de noches
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Mínimo de noches</p>
        """, unsafe_allow_html=True)
        minimum_nights =  st.text_input("Ingresa un número del 1 al 30: ", "1")
        minimum_nights = float(minimum_nights)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


        # Selección del nº total de casas del anfitrión
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Nº total de casas del anfitrión</p>
        """, unsafe_allow_html=True)
        calculated_host_listings_count =  st.text_input("Ingresa un número del 1 al 100: ", "1")
        calculated_host_listings_count = float(calculated_host_listings_count)
        
        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)


        # Selección nº de reviews
        st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Nº de reviews</p>
        """, unsafe_allow_html=True)
        number_of_reviews =  st.text_input("Ingresa un número del 0 al 500: ", "0")
        number_of_reviews = float(number_of_reviews)

        st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)




    # Ahora fuera del sidebar, introducimos las variables con los datos de entrada
    data = {
        'neighbourhood_labels': neighbourhood_labels,
        'room_type_num': room_type_num,
        'availability_365': availability_365,
        'minimum_nights': minimum_nights,
        'calculated_host_listings_count': calculated_host_listings_count,
        'number_of_reviews': number_of_reviews,
        }

    # Convertir los datos de entrada en un DataFrame de Pandas
    input_data = pd.DataFrame([data])


    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True) # Separación




    ###### Textos de esta pestaña

    st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Modelo: Light Gradient Boosting Machine</p>
        """, unsafe_allow_html=True)

    # Explicación del modelo
    st.markdown("""
    <p style="text-align: left; color: black;">La elección del método de Fast Machine Learning para entrenar
    un modelo de predicción ayudó a aumentar la precisión de los resultados y reducir el tiempo de entrenamiento.
    """, unsafe_allow_html=True)
     
    st.markdown("""
    <p style="text-align: left; color: black;">De todos los diferentes modelos que analizó este sistema,
    el mejor modelo resultó ser <b>Light Gradient Boosting Machine (LightGBM)</b>.
    ¿Por qué? De todos era el que tenía el menor error medio absoluto (MAE) y el menor error cuadrático medio (MSE).
    Además, también tenía el mejor rendimiento en el coeficiente de determinación (R2).
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True) #línea
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)

    
    # Creamos un botón
    if st.button("Realizar predicción con los datos de entrada elegidos"):
            # Realizar la predicción
            prediction = model.predict(input_data).round(2)

            # Mostrar el resultado
            resultado = st.text_input("**Resultado de la predicción:**", f"El precio previsto por noche es de  {prediction[0]} €")

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.markdown("<hr style='color:#ff5a60;background-color:#ff5a60;height:1px;'/>", unsafe_allow_html=True) #línea

    st.markdown("""
    <p style="text-align: left; color: black;">
    Light Gradient Boosting Machine (LightGBM) es un algoritmo de aprendizaje automático supervisado. En este caso, lo usamos
    para predecir el precio de alquiler de las propiedades de Airbnb en Madrid.
    Esto se logra mediante el entrenamiento del modelo con los datos del dataset, como las reviews, el barrio,
    el tipo de habitación, el número de noches mínimas y la disponibilidad.
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: left; color: black;">
    Una vez entrenado, el modelo puede predecir
    el precio de un alquiler de Airbnb según sus características y datos de entrada.
    Esto puede ayudar a los propietarios a establecer precios de alquiler realistas para sus propiedades de Airbnb.
    """, unsafe_allow_html=True)


    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
   
    # Ponemos las dos columnas aclaratorias con los diccionarios de elección
    col1, col2= st.columns(2)
    with col1:
        st.caption(":red[Leyenda del barrio con su etiqueta]")
        # st.markdown("""
        # <p style="text-align: left; color: #ff5a60; font-size: 20px;">Diccionario del barrio con su etiqueta</p>
        # """, unsafe_allow_html=True),
        st.dataframe(labels_df)

    with col2:
        st.caption(":red[Diccionario del tipo de habitación con su etiqueta]")
        room_type_labels


    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True) # Dejamos espacio
    

    ## ----------- Comenzamos con más información y texto sobre el modelo --------------

    st.markdown("""
        <p style="text-align: center; color: #ffffff; background-color: #ff5a60; font-size: 20px;">Más información sobre el modelo</p>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <p style="text-align: left; color: black;">
    Un valor de 0.4816 para el R2 indica que el modelo explica aproximadamente el 48% de la variabilidad de los precios
    de los pisos de Airbnb.
    Se puede decir que el modelo tiene una buena capacidad de predicción con un R2 cercano a 0.5, lo que indica que
    el modelo explica alrededor del 50% de la variabilidad en los precios de los pisos de Airbnb. 
    """, unsafe_allow_html=True)

    st.image("Imágenes/captura1.PNG")
    st.image("Imágenes/captura3.PNG")

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: left; color: black;">
    Además, los errores obtenidos son aceptables, con un MAE y RMSE de 19.3011 y 26.6900 respectivamente,
    lo que sugiere que el modelo se comporta de manera estable y consistente en su predicción de precios.
    Un valor de 19.3011 significa que, en promedio, el modelo está prediciendo el precio de los pisos de
    Airbnb con un error de 19.3011 unidades monetarias.
    """, unsafe_allow_html=True)

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.image("Imágenes/captura2.PNG")

    st.markdown("<p>&nbsp;</p>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align: left; color: black;">
    En resumen, el modelo LightGBM es un buen ajuste para el proyecto y se puede considerar una opción adecuada
    para la predicción de precios de pisos de Airbnb. Se pueden seguir investigando otras técnicas de modelado
    o mejorando los features para mejorar aún más el desempeño del modelo.
    """, unsafe_allow_html=True)

