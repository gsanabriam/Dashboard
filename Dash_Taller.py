def DashBoard ():
  %matplotlib inline
  ##Instaladores
  !pip install pyshp
  !pip install geopandas
  !pip install --upgrade shapely
  !pip install --upgrade descartes

  ## Librerias
  from urllib.request import urlopen
  from zipfile import ZipFile
  from io import BytesIO
  import shapefile
  import geopandas as geopandas
  from shapely.geometry import shape  
  import pandas as pd
  import requests
  import matplotlib.pyplot as plt
  from matplotlib.collections import PatchCollection
  from matplotlib.patches import Circle
  from IPython.display import HTML, display_html, display
  import seaborn as sns
  import numpy as np
  from matplotlib import cm
  from matplotlib import colors
  import ipywidgets as widgets
  from ipywidgets import interact, interactive
  from IPython.display import display

  #Carga base de datos
  file1 ="https://github.com/acabezad/Dashboard/snies_Consolidado_2015_a_2018_p1.xlsx"
  file2 ="https://github.com/acabezad/Dashboard/snies_Consolidado_2015_a_2018_p2.xlsx"
  df = pd.read_excel(file1, na_values = "n/a")
  df_x = pd.read_excel(file2, na_values = "n/a")

  df.append(df_x)

   #Reenombrar titulos de la base de datos
  df2= df.rename(columns={'Código de \nla Institución  ':'COD_INSTITUCION',
                        'IES PADRE':'IES_PADRE',
                        'Institución de Educación Superior (IES)':'INSTITUCION',
                        'Principal\n o\nSeccional':'PRINCIPAL_SECCIONAL',
                        'Sector IES':'SECOTR_IES',
                        'Caracter IES':'CARACTER_IES',
                        'Código del \ndepartamento\n(IES)':'DPTO',
                        'Departamento de \ndomicilio de la IES':'DPTO_IES',
                        'Código del \nMunicipio\n(IES)':'COD_MUNICIPIO_IES',
                        'Municipio de\ndomicilio de la IES':'MUNICIPIO_IES',
                        'Código \nSNIES del\nprograma':'CODIGO_PROGRAMA',
                        'Programa Académico':'PROGRAMA_ACADEMICO',
                        'Nivel Académico':'NIVEL_ACADEMICO',
                        'Nivel de Formación' :'NIVEL_FORMACION',
                        'Metodología':'METODOLOGIA',
                        'Área de Conocimiento':'AREA_CONOCIMIENTO',
                        'Núcleo Básico del Conocimiento (NBC)':'NUCLEO_CONOCIMIENTO',
                        'Código del \nDepartamento\n(Programa)':'COD_DPTO_PROGRAMA',
                        'Departamento de oferta del programa':'DPTO_PROGRAMA',
                        'Código del \nMunicipio\n(Programa)':'COD_MUNICIPIO_PROGRAMA',
                        'Municipio de oferta del programa':'MUNICIPIO_PROGRAMA',
                        'Id Género':'ID_GENERO',
                        'Género':'GENERO' ,
                        'Matriculados 2015':'MATRICULADOS'
                        })
  
  # Todos los campos los vuelve minuscula
  df2=df2.apply(lambda x: x.str.lower() if(x.dtype == "object") else x)

  #Ajusta Genero
  df2["GENERO"]=[i.replace("femenino","mujer") for i in df2["GENERO"]]
  df2["GENERO"]=[i.replace("masculino","hombre") for i in df2["GENERO"]]

  #Ajusta Nivel Formación
  df2["NIVEL_FORMACION"]=[i.replace("formacion tecnica profesional","tecnica") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("especialización médico quirúrgica","especializacion") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("especialización universitaria","especializacion") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("maestría","maestria") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("tecnológica","tecnologica") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("formación técnica profesional","tecnica") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("especialización tecnologica","especializacion") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("especialización técnico profesional","especializacion") for i in df2["NIVEL_FORMACION"]]
  df2["NIVEL_FORMACION"]=[i.replace("especialización tecnológica","especializacion") for i in df2["NIVEL_FORMACION"]]

  #Ajusta Caracter IES
  df2["CARACTER_IES"]=[i.replace("institución técnica profesional","institucion tecnica profesional") for i in df2["CARACTER_IES"]]
  df2["CARACTER_IES"]=[i.replace("institución tecnológica","institucion tecnologica") for i in df2["CARACTER_IES"]]
  df2["CARACTER_IES"]=[i.replace("institución universitaria/escuela tecnológica","institucion universitaria/escuela tecnologica") for i in df2["CARACTER_IES"]]
  
  #Ajusta Metodologia
  df2.METODOLOGIA=df2.METODOLOGIA.replace({"virtual":"distancia (virtual)"})

  #Ajusta Area de conocimiento
  df2["AREA_CONOCIMIENTO"]=[i.replace("ingeniería, arquitectura, urbanismo y afines","ingenieria arquitectura urbanismo y afines") for i in df2["AREA_CONOCIMIENTO"]]
  df2["AREA_CONOCIMIENTO"]=[i.replace("matemáticas y ciencias naturales","matematicas y ciencias naturales") for i in df2["AREA_CONOCIMIENTO"]]
  df2["AREA_CONOCIMIENTO"]=[i.replace("agronomía, veterinaria y afines","agronomia veterinaria y afines") for i in df2["AREA_CONOCIMIENTO"]]
  df2["AREA_CONOCIMIENTO"]=[i.replace("ciencias de la educación","ciencias de la educacion") for i in df2["AREA_CONOCIMIENTO"]]
  df2["AREA_CONOCIMIENTO"]=[i.replace("economía, administración, contaduría y afines","economia administracion contaduria y afines") for i in df2["AREA_CONOCIMIENTO"]]

  #######--------------Gráficos---------------------#####
  tb=dfp = df2.groupby('NIVEL_FORMACION').MATRICULADOS.sum().reset_index('NIVEL_FORMACION')
  tb['NIVEL_FORMACION'] = tb['NIVEL_FORMACION'].astype('str')
  normdata = colors.Normalize(min(tb['MATRICULADOS']), max(tb['MATRICULADOS']))
  colormap = cm.get_cmap("Blues")
  colores =colormap(normdata(tb['MATRICULADOS']))
  
  #Mostrar pie
  plt.pie(tb['MATRICULADOS'], labels=tb['NIVEL_FORMACION'], autopct="%0.1f %%", colors=colores)
  plt.axis("equal")
  plt.show()

  #Gráfica Area conocimiento
  display(HTML('<center><h1> AREA DE CONOCIMIENTO  </h1></Center>'))
  ax = sns.catplot(y="MATRICULADOS", x="AREA_CONOCIMIENTO", kind='bar',data=df2, aspect=4)
                   
  # Tendencia por año vs metodologia de estudio
  display(HTML('<right><h1>METODOLOGIA POR AÑO </h1></right>'))
  sns.relplot(x="Año", y="MATRICULADOS", hue="METODOLOGIA", ci=False, kind='line',data=df2)

  #Tabla
  display(HTML('<right><h1>CARRERAS POR CIUDAD </h1></right>'))

  class select:
      def __init__(self,  dd, dd2=None):
          self.dd=pd.DataFrame(dd)
          self.dd2=pd.DataFrame(dd2)
          
      def Dpto(self,c):
          df2=self.dd[(self.dd["DPTO_IES"]==c)] 
          valor2=widgets.Dropdown(description='Ciudad:', value=None, options=df2['MUNICIPIO_IES'].unique().tolist())
          interact(self.ciud, e=valor2)

      def ciud(self,e):
          df2=self.dd[(self.dd["MUNICIPIO_IES"]==e)] 
          if (e != None):
              df3=pd.DataFrame(df2.groupby([ 'PROGRAMA_ACADEMICO','NUCLEO_CONOCIMIENTO','Semestre'])['MATRICULADOS'].sum().reset_index(['Semestre','PROGRAMA_ACADEMICO','NUCLEO_CONOCIMIENTO']))
              display (df3)        
      
      def mostarDpto(self):
          valor=widgets.Dropdown(description='Dpto:', value=None, options=self.dd['DPTO_IES'].unique().tolist())
          interact(self.Dpto, c=valor)

  cs=select(df2)
  cs.mostarDpto()

  #Libreria archivos
  import requests
  import zipfile
  # función para descargar y guardar archivo
  def save_file(url, file_name):
    r = requests.get(url)
    with open(file_name, 'wb') as f:
        f.write(r.content)

   #Importa base de mapas
  scol = 'https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json'
  save_file(scol, 'col.json')
  col_1 = geopandas.read_file('col.json')
  col_1['DPTO']=col_1['DPTO'].astype('int')

  def f(NFF):
    #Genera dataframe
    dfp = df2[df2['NIVEL_FORMACION']==NFF].groupby('DPTO').MATRICULADOS.sum().reset_index('DPTO')
    
    loc= col_1.merge(dfp, how = 'left')
    
    loc['MATRICULADOS'].fillna(1, inplace = True)

    loc['MP']=np.log(loc['MATRICULADOS'])  
    
    display(HTML('<right><h1>Matriculados por Departamento </h1></right>'))
    loc.plot(figsize=(18, 9), column=np.log(loc['MATRICULADOS']), legend=True, cmap='jet') # jet, hot, prism, cividis
    for idx, row in loc.iterrows():
        p = row['geometry'].centroid.coords[0]
        plt.text(p[0], p[1], row['NOMBRE_DPT'].title(), horizontalalignment='center', fontsize=8)
    plt.axis('off')

    
  NF=widgets.Dropdown(
      options=df2.NIVEL_FORMACION.unique().tolist(),
      description='Nivel Educativo:',
      disabled=False,)
  interact(f,NFF=NF)

