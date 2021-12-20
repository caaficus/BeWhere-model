# Biobased PET BeWhere model

The BeWhere model is based on a mixed integer linear programming (MILP) and is written in the commercial software GAMS, using CPLEX as a solver. The aim of the model is to minimize the costs of the entire supply chain, including biomass harvest, biomass transportation, conversion processes, and transportation and delivery of products. The model takes into account locations and quantities of both feedstock supply and demand. Fossil CO2 emissions are considered by including a cost for emitting fossil CO2. In this study, carbon tax was considered as carbon-pricing policy. The model will choose the least costly pathways from one set of feedstock supply points to a specific production plant and further to a set of demand points. The output from the model includes the location of a set of plants, the flows of feedstock and products between different regions, and the costs and CO2 emissions of the supply chain. 

In this repository, the reader will find three main file packages: Input dataset (*Excel file*), interface between Excel and GAMS (*Python files*) and the optimization model (*GAMS files*).

## Input Dataset (Excel file)

This [file](https://github.com/caaficus/BeWhere-model/blob/main/Test_LCA_BeWhereV3.xlsx) contains the input data (mass balances, economic parameters, and greenhouse gas emissions) of the biobased polyethylene terephthalate (PET) supply chain. In the first tab of the excel file, there is a general structure of the information presented in the file. 

## Interface between Excel and GAMS

These two python files are used to convert the input data into a format readable for GAMS. 

1. [bewhere.py](https://github.com/caaficus/BeWhere-model/blob/main/bewhere.py): Define functions to import data from Excel to a .txt file format (readable by GAMS. 

2. [LCA_BeWhere.py](https://github.com/caaficus/BeWhere-model/blob/main/LCA_BeWhere.py): Import data in the Excel file to .txt format

## Optimization model (GAMS)

The optimization model in GAMS consists of [7 files](https://github.com/caaficus/BeWhere-model/tree/main/GAMS). These files describe the parameters, sets, variables, equations, and model formulation for the production of biobased PET. A brief description of each file is given below:

1. [Set_parameters](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Set_Parameters.gms): Input data from the Excel file in the .txt format. 
2. [Variables](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Variables.gms): Variables of the optimization model.
3. [Equations](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Equations_Syvlain_V2.gms): Mass balances, constraint balances, and general equations of the optimization model.
4. [Equation_list](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Equations_List.gms): List of equations used in the optimization model.
5. [Objective_function](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Objective_Function.gms): Optimization model formulation (economic and environmental criteria).
6. [Results](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/Results.gms): Results reporting format.
7. [GAMS files compiler](https://github.com/caaficus/BeWhere-model/blob/main/GAMS/LCA_BeWhere_BioPlastic_Start.gms): Compile the previous GAMS files to run the optimization model.

# Authors

The BeWhere model was developed by [Sylvain Leduc](https://iiasa.ac.at/web/home/research/researchPrograms/EcosystemsServicesandManagement/-Leduc--Sylvain-.en.html) during his [PhD thesis](https://www.diva-portal.org/smash/get/diva2:989798/FULLTEXT01.pdf).

The BeWhere model was adapted to the biobased PET supply chain by [Carlos García-Velásquez](https://ppp.maastrichtuniversity.nl/users/c.garciavelasquez?language=en) during the summer school 2019 in the International Institute of Applied Science Analysis (IIASA). 

