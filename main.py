import streamlit as st
import pandas as pd

df = pd.read_csv("AI_Student_Life_india.csv")

st.write("""# Impacto da ia na vida do estudante""") # markdown

st.write("### Com a evolução constante da IA, este recurso vem sendo cada vez mais usado no cenário estudantil, com isso, " \
"torna-se cada vez mais necessário possuir mais informações em relação ao seu propósito, uso diário e o seu público ")
st.write("## Questões éticas")
st.write("### Questões éticas também serão analisadas neste estudo, tendo em vista que muitos estudantes se aproveitam do uso de IA para a realização de trabalhos" \
"o que nem sempre é um problema, no entanto, a transparência em relação ao uso deve ser levada em consideração, devido ao fato de muitos estudantes utilizarem" \
"de programas para tentar \"Humanizar\" seu trabalho impactando também no seu aprendizado em relação ao conteúdo")


atributos = ["Estudantes","Education_Level","City","AI_Tool_Used","Impact_on_Grades","Satisfaction_Level"]
atributos_selecionados = st.multiselect("Escolha o atributo para visualizar",atributos)
#Caso tenha selecionado Grau de educação
if "Education_Level" in atributos_selecionados:
    
    st.header("Niveis de educação")
    
        #Contador de estudantes
    st.subheader("Quantidade de estudantes por grau")

    contador_Ensino = (df["Education_Level"].value_counts())
    st.bar_chart(contador_Ensino)

    nivel_comum = contador_Ensino.index[0]
    
    st.write(f"### O nível de escolaridade que mais utiliza ia é :green[{nivel_comum}] ")
        #Estudantes usando IA
    st.subheader("Média de estudantes que usam IA")
    
        #Variaveis para verificar média
    media_Estudantes_IA = df.groupby("Education_Level")["Daily_Usage_Hours"].mean()
    grupo_que_mais_usa = media_Estudantes_IA.idxmax()
    
    st.bar_chart(media_Estudantes_IA)
    
    st.write(f"O grupo que utiliza ia por mais tempo é :green[{grupo_que_mais_usa}], com uma média de {media_Estudantes_IA.max():.1f} horas")
        #IA favorita de cada grupo
    st.header("IA mais usada por cada grupo")
    most_used_ai_by_education = df.groupby('Education_Level')['AI_Tool_Used'].value_counts().reset_index(name='Count')
    most_used_ai_by_education = most_used_ai_by_education.loc[most_used_ai_by_education.groupby('Education_Level')['Count'].idxmax()]
    st.bar_chart(most_used_ai_by_education,x="Education_Level",y="Count",color="AI_Tool_Used")

#Caso tenha selecionado Ferramenta Utilizada
if "AI_Tool_Used" in atributos_selecionados:
        #IAs mais utilizadas em cada tópico
        st.header("Ferramenta Utilizada")
    
    # Pergunta: Para que cada ferramenta é mais usada?
        st.subheader("Distribuição de Propósito por Ferramenta")
    

        analise_ferramenta = df.groupby(['AI_Tool_Used', 'Purpose']).size().reset_index(name='Quantidade')
    

        st.bar_chart(analise_ferramenta, x="AI_Tool_Used", y="Quantidade", color="Purpose")

        #Ferramenta mais usada diariamente
        st.subheader("Horas diarias de ferramenta")
        horas_Diarias = df.groupby("AI_Tool_Used")["Daily_Usage_Hours"].sum()
        horas_Diarias_nome = horas_Diarias.idxmax()
        st.bar_chart(horas_Diarias)
        st.write(f"### A IA mais utilizada é :green[{horas_Diarias_nome}] com ao todo :green[{horas_Diarias.max()}] horas diarias")
#Caso tenha selecionado cidade
if "City" in atributos_selecionados:
      
      st.header("Aspectos das cidades")
        #Cidade que mais usa ia
      st.subheader("Qual cidade usa mais IA?")

      contador_cidade = df.groupby("City")["AI_Tool_Used"].count()
      st.bar_chart(contador_cidade)
      st.write(f"A cidade que mais usa IA é :green[{contador_cidade.idxmax()}] com :green[{contador_cidade.max()}] usuarios registrados ")

        #IA MAIS USADA EM CADA CIDADE
      st.subheader("Qual a IA mais usada em cada cidade")
      
      ai_Cada_Cidade = df.groupby("City")["AI_Tool_Used"].value_counts().reset_index(name='Count')
      ai_Cada_Cidade = ai_Cada_Cidade.loc[ai_Cada_Cidade.groupby("City")["Count"].idxmax()]

      st.bar_chart(data = ai_Cada_Cidade,x="City",y="Count",color="AI_Tool_Used")

      #Qual cidade possui mais universitários
      #Variaveis pra cada
      Universitarios_Cidade = df[df.Education_Level == "University"].groupby("City")["Student_ID"].count()
      Escola_Cidade = df[df.Education_Level == "School"].groupby("City")["Student_ID"].count()
      Colegiais_Cidade = df[df.Education_Level == "College"].groupby("City")["Student_ID"].count()
      Media_Cidade = df.groupby("City").size().mean()

      st.write(f"A cidade que possui mais universitários é a :green[{Universitarios_Cidade.idxmax()}] com :green[{Universitarios_Cidade.max()} estudantes] ao todo")
      st.write(f"A cidade que possui mais Colegiais é a :green[{Colegiais_Cidade.idxmax()}] com :green[{Colegiais_Cidade.max()} estudantes] ao todo")
      st.write(f"A cidade que possui mais alunos de escola é a :green[{Escola_Cidade.idxmax()}] com :green[{Escola_Cidade.max()} estudantes] ao todo")
      st.write(f"A média de estudantes que utilizam de IA por cidade é :green[{Media_Cidade:.0f}]")
if "Estudantes" in atributos_selecionados:
      st.header("Atributos dos estudantes")
      #Genero que mais usa IA
      st.subheader("Qual gênero mais utiliza da IA para estudos?")

      contagem_genero = df['Gender'].value_counts()
      st.bar_chart(contagem_genero)
      st.write(f"O genero que mais utiliza IA é o :green[{contagem_genero.idxmax()}]")
      #Idade que mais usa IA
      st.subheader("Qual idade mais utiliza de IA?")

      contagem_Idade = df['Age'].value_counts()

      st.bar_chart(contagem_Idade)
      st.write(f":green[{contagem_Idade.idxmax()}] anos é a idade que mais utiliza da IA para estudos")


st.write("""
# Obrigado         
        """) # markdown