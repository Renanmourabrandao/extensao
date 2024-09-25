# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:18:03 2024

@author: Renan
"""

import pandas as pd
from datetime import datetime

dados = {
    'nome':['Vitor Leite Costa','Gustavo Pereira Barros', 'Marcelo Souza Freitas','Felipe Gomes de Araújo','Rodrigo Santana Bezerra','João Henrique Ferreira','Lucas Barros de Oliveira','Bruno Duarte Cardoso','Antônio Souza Alves','Thiago Rodrigues Duarte','Leonardo Queiroz Almeida','João Martins de Souza','Rodrigo Nascimento Silva','Juliana Alves Monteiro','Diego Cardoso Monteiro','Igor Macedo Lima','Paulo Andrade Souza','Miguel Vieira Lopes','Eduardo Lima de Carvalho','José Henrique Batista','Fábio Mendes Andrade','Bruno Eduardo Pereira','Rafael Farias Guedes','Carlos Alberto Silva','Jorge Ribeiro de Farias','Alexandre Guimarães Silva','Rafael Costa Andrade','Danilo Morais Teixeira','Fernanda Lopes Macedo','Bruno Albuquerque Dantas','Renato Araújo Martins','Daniel Oliveira Morais','Victor Carvalho Almeida','Henrique Barbosa Lima','Mariana Fernandes Cardoso','Ricardo Tavares de Souza','Matheus Batista de Souza','Antônio Souza Alves'],
    'cidade': ['Vitória de Santo Antão','Paulista','Caruaru','Caruaru','João Pessoa','Caruaru','Caruaru','Fortaleza','Caruaru','Caruaru','Pesqueira','Mossoró','Garanhuns','Caruaru','Caruaru','Cabo de Santo Agostinho','Jaboatão dos Guararapes','Aracaju','Olinda','Caruaru','Petrolina','Caruaru','Maceió','Caruaru','Salgueiro','Serra Talhada','Caruaru','Carpina','Caruaru','Ipojuca','Recife','Natal','Teresina','Caruaru','Caruaru','Goiana','Belo Jardim','Caruaru',],
    'classe_economica': ['B','A','C','A','B','C','A','B','C','B','C','A','B','A','C','B','A','C','B','A','B','C','A','B','C','B','C','A','B','C','A','B','A','C','B','A','B','C',],
    'data_ultima_compra': ['2020-03-29','2020-07-11','2020-07-21','2020-11-20','2020-11-04','2021-03-12','2021-02-10','2021-02-18','2021-05-08','2021-04-28','2021-07-09','2021-07-24','2021-10-18','2021-10-08','2021-12-05','2021-11-30','2022-01-22','2022-03-30','2022-05-25','2022-08-16','2022-08-15','2022-10-13','2022-09-11','2022-09-19','2022-12-21','2023-01-02','2023-01-30','2023-08-14','2023-06-27','2023-06-03','2023-11-03','2023-10-13','2023-12-20','2024-03-02','2024-04-05','2024-04-17','2024-05-28','2024-05-08']
         }


df = pd.DataFrame(dados)
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_columns', None)


df['data_ultima_compra'] = pd.to_datetime(df['data_ultima_compra'])


pesos_classes = {'A': 1, 'B': 0.6, 'C': 0.4}


hoje = pd.to_datetime('today')
df['dias_desde_ultima_compra'] = (hoje - df['data_ultima_compra']).dt.days


df['peso_tempo'] = df['dias_desde_ultima_compra'] / df['dias_desde_ultima_compra'].max()


df['peso_classe'] = df['classe_economica'].map(pesos_classes)


df['nota_final'] = df['peso_classe'] * df['peso_tempo']


df = df.sort_values(by='nota_final', ascending=False)


print(df[['nome', 'cidade', 'classe_economica', 'data_ultima_compra', 'nota_final']])
