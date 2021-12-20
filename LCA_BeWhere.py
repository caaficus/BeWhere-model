# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:13:08 2019

@author: Carlos
"""
#%% Import libraries
import pandas as pd
import numpy as np
import bewhere as bwr
#%% Set the location of working datasets

file_location="I:/OPTIMIZATION/Beaver/Data/"
file_destination="I:/OPTIMIZATION/Beaver/txt_file_beaver/"

file_name="Test_LCA_BeWhereV3.xlsx"


#%% Sets

#Set Countries
print('Creation of the sets...')

print('   ...Read countries dataset')
countries =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Countries', usecols='A:U')
print('      ...Create countries set')
bwr.create_parameter_file(file_destination+'set-country.txt',
                          ['C-'], pd.concat([pd.DataFrame([
                                  countries['ADM0_NAME'].values[rr] 
    for rr in range(countries.shape[0])])]))

#Set Regions

print('   ...Read regions dataset')
regions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Regions', usecols='A:U')
print('      ...Create regions set')
bwr.create_parameter_file(file_destination+'set-region.txt',
                          ['R-'], pd.concat([pd.DataFrame([
                                  regions['NUTS2_region'].values[rr] 
    for rr in range(regions.shape[0])])]))

#Set SubRegions

print('   ...Read subregions dataset')
subregions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Subregions', usecols='A:U')
print('      ...Create subregions set')
bwr.create_parameter_file(file_destination+'set-subregion.txt',
                          ['SR-'], pd.concat([pd.DataFrame([
                                  subregions['Subregions'].values[rr] 
    for rr in range(subregions.shape[0])])]))

# Set Import regions
print('      ...Create import regions set')
bwr.create_parameter_file(file_destination+'set-import-region.txt',
                          ['RI-'], pd.concat([pd.DataFrame([
                                  regions['NUTS2_region'].values[rr] 
    for rr in range(regions.shape[0])])]))

# Set Export regions
print('      ...Create export regions set')
bwr.create_parameter_file(file_destination+'set-export-region.txt',
                          ['RE-'], pd.concat([pd.DataFrame([
                                  regions['NUTS2_region'].values[rr] 
    for rr in range(regions.shape[0])])]))
#Set Supply

#print('   ...Read the biomass availability dataset')
#Biomass_supply =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_available', usecols='A:U')
#print('      ...Create the biomass supply set')
#bwr.create_parameter_file(file_destination+'set-supply.txt',
#                          ['S'], pd.concat([pd.DataFrame([
#                                  Biomass_supply['ID_number'].values[rr] 
#    for rr in range(Biomass_supply.shape[0])])]))

# Set Material
print('   ...Read the raw material dataset')
raw_material =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='List of feedstock', usecols='A:U')
print('      ...Create the raw material set')
bwr.create_parameter_file(file_destination+'set-raw-material.txt',
                          ['RM-'], pd.concat([pd.DataFrame([
                                  raw_material['Raw material'].values[rr] 
    for rr in range(raw_material.shape[0])
    if raw_material['Raw material used'].values[rr]==1])]))

#Set Import points

print('   ...Read the import points dataset')
import_points =  pd.read_excel(file_location+file_name, skiprows=0, sheet_name='Ports_ID', usecols='A:U')
print('      ...Create the import points set')
bwr.create_parameter_file(file_destination+'set-import-points.txt',
                          ['I-'], pd.concat([pd.DataFrame([
                                  import_points['grid_id_40'].values[rr]
    for rr in range(import_points.shape[0])
    if import_points['grid_id_40'].values[rr]>0])]))

#Set Raw Material Import points

print('   ...Read the raw material import points dataset')
raw_points =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Bio_import_points', usecols='A:U')
print('      ...Create the import points set')
bwr.create_parameter_file(file_destination+'set-raw-material-import-points.txt',
                          ['IRM-'], pd.concat([pd.DataFrame([
                                  raw_points['Feedstock_location'].values[rr]
    for rr in range(raw_points.shape[0])
    if raw_points['Feedstock_location'].values[rr]>0])]))

#
# Set Plant A
print('   ...Read the plant location dataset')
plant_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Plant_location', usecols='A:U')
print('      ...Create the plant location set')
bwr.create_parameter_file(file_destination+'set-plantA.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([
                                  plant_location['ID_number'].values[rr] 
   for rr in range(plant_location.shape[0])])]))

# Set Plant A - Main products
print('   ...Read the products dataset')
product_prod =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='B')
print('      ...Create the products set')
bwr.create_parameter_file(file_destination+'set-products.txt',
                          ['PRD-'], pd.concat([pd.DataFrame([
                                  product_prod.columns[cc] 
   for cc in range(product_prod.shape[1])])]))


# Set Plant A - byproducts
print('   ...Read the byproducts dataset')
byproduct_prod =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='C:U')
print('      ...Create the byproducts set')
bwr.create_parameter_file(file_destination+'set-byproducts.txt',
                          ['Byp-'], pd.concat([pd.DataFrame([
                                  byproduct_prod.columns[cc] 
   for cc in range(byproduct_prod.shape[1])])]))

#Set Plant A Size
print('   ...Read the plant size dataset')
plantA_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='P_size', usecols='A:U')
print('      ...Create the plant size set')
bwr.create_parameter_file(file_destination+'set-size-plantA.txt',
                          ['SizePa-'], pd.concat([pd.DataFrame([
                                  plantA_size['ID'].values[rr] 
   for rr in range(plantA_size.shape[0])])]))

#Set Transportation Mode
print('   ...Read the transportation types dataset')
trans_type =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Supply_Trans', usecols='A:U')
print('      ...Create the transportation set')
bwr.create_parameter_file(file_destination+'set-transport.txt',
                          ['T-'], pd.concat([pd.DataFrame([
                                  trans_type.columns[cc]
    for cc in range(1,trans_type.shape[1])])]))


# Set Plant B
print('   ...Read the plant location dataset')
plantB_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pb_location', usecols='A:U')
print('      ...Create the plant location set')
bwr.create_parameter_file(file_destination+'set-plantB.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([
                                  plantB_location['ID_plantB'].values[rr] 
   for rr in range(plantB_location.shape[0])])]))

#Set Plant B Size
print('   ...Read the plant size dataset')
plantB_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantB_size', usecols='A:U')
print('      ...Create the plant size set')
bwr.create_parameter_file(file_destination+'set-size-plantB.txt',
                          ['SizePb-'], pd.concat([pd.DataFrame([
                                  plantB_size['ID'].values[rr] 
   for rr in range(plantB_size.shape[0])])]))


# Set Plant C
print('   ...Read the plant location dataset')
plantC_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pc_location', usecols='A:U')
print('      ...Create the plant location set')
bwr.create_parameter_file(file_destination+'set-plantC.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([
                                  plantC_location['ID_plantC'].values[rr] 
   for rr in range(plantC_location.shape[0])])]))

#Set Plant C Size
print('   ...Read the plant size dataset')
plantC_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantC_size', usecols='A:U')
print('      ...Create the plant size set')
bwr.create_parameter_file(file_destination+'set-size-plantC.txt',
                          ['SizePc-'], pd.concat([pd.DataFrame([
                                  plantC_size['ID'].values[rr] 
   for rr in range(plantC_size.shape[0])])]))

# Set Plant D
print('   ...Read the plant location dataset')
plantD_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pd_location', usecols='A:U')
print('      ...Create the plant location set')
bwr.create_parameter_file(file_destination+'set-plantD.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([
                                  plantD_location['ID_plantD'].values[rr] 
   for rr in range(plantD_location.shape[0])])]))

#Set Plant D Size
print('   ...Read the plant size dataset')
plantD_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantD_size', usecols='A:U')
print('      ...Create the plant size set')
bwr.create_parameter_file(file_destination+'set-size-plantD.txt',
                          ['SizePd-'], pd.concat([pd.DataFrame([
                                  plantD_size['ID'].values[rr] 
   for rr in range(plantD_size.shape[0])])]))

# Set demand D
print('   ...Read the demand dataset')
demand_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Demand', usecols='A:U')
print('      ...Create the demand set')
bwr.create_parameter_file(file_destination+'set-demand.txt',
                          ['D-'], pd.concat([pd.DataFrame([
                                  demand_location['ID_Demand'].values[rr] 
   for rr in range(demand_location.shape[0])])]))

# Set PTa Plant
PTA_location =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PTA_price', usecols='A')
print('      ...Create the plant location set')
bwr.create_parameter_file(file_destination+'set-plantPTA.txt',
                          ['M-'], pd.concat([pd.DataFrame([
                                  PTA_location['PTA_location'].values[rr] 
   for rr in range(PTA_location.shape[0])])]))

#Set Plant TPA Size
print('   ...Read the plant TPA size dataset')
plantTPA_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantTPA_size', usecols='A:U')
print('      ...Create the plant TPA size set')
bwr.create_parameter_file(file_destination+'set-size-plantTPA.txt',
                          ['SizeM-'], pd.concat([pd.DataFrame([
                                  plantTPA_size['ID'].values[rr] 
   for rr in range(plantTPA_size.shape[0])])]))



#%%  SET RELATIONS

#Set - Relation Country - Regions

print('   ...relation countries - regions')
country_regions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='CR', usecols='A:JJ')
bwr.create_parameter_file(file_destination+'set-country-region-relation.txt',
                          ['C-','R-'], pd.concat([pd.DataFrame([[
                                  country_regions['Country'].values[rr],
                                  country_regions.columns[cc]] 
    for rr in range(country_regions.shape[0])
    for cc in range(1,country_regions.shape[1])
    if country_regions.values[rr,cc]==1])]))

#Set - Relation supply - Transportation mode

print('   ...relation Supply location-transport')
supply_transport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Supply_Trans', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-supply-transport-relation.txt',
                          ['R-','T-'], pd.concat([pd.DataFrame([[
                                  supply_transport['supply_ID'].values[rr],
                                  supply_transport.columns[cc]] 
    for rr in range(supply_transport.shape[0])
    for cc in range(1,supply_transport.shape[1])
    if supply_transport.values[rr,cc]==1])]))

#Set - Relation Country - Raw material

print('   ...relation country-feedstock')
country_feedstock =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Pa_RM_dyn', usecols='A:AY')
bwr.create_parameter_file(file_destination+'set-plantA-biomass-relation.txt',
                          ['RM-','Pa-'], pd.concat([pd.DataFrame([[
                                  country_feedstock['Feedstock'].values[rr],
                                  country_feedstock.columns[cc]] 
    for rr in range(country_feedstock.shape[0])
    for cc in range(1,country_feedstock.shape[1])
    if country_feedstock.values[rr,cc]==1])]))

#Set - No Relation Country - Raw material

print('   ...No relation country-feedstock')
nocountry_feedstock =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='NotPa_RM_dyn', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantA-biomass-norelation.txt',
                          ['Pa-','RM-'], pd.concat([pd.DataFrame([[
                                  nocountry_feedstock['plantA_ID'].values[rr],
                                  nocountry_feedstock.columns[cc]] 
    for rr in range(nocountry_feedstock.shape[0])
    for cc in range(1,nocountry_feedstock.shape[1])
    if nocountry_feedstock.values[rr,cc]==1])]))

#Set - Relation Import regions - Export regions

print('   ...relation import-export regions')
ri_re =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='IRE', usecols='A:JJ')
bwr.create_parameter_file(file_destination+'set-import-export-relation.txt',
                          ['I-','R-'], pd.concat([pd.DataFrame([[
                                  ri_re['Regions'].values[rr],
                                  ri_re.columns[cc]] 
    for rr in range(ri_re.shape[0])
    for cc in range(1,ri_re.shape[1])
    if ri_re.values[rr,cc]==1])]))


#Set - Relation Country - Import points

print('   ...relation countries - import points')
country_import =  pd.read_excel(file_location+file_name, skiprows=0, sheet_name='Ports_ID', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-country-import-points-relation.txt',
                          ['C-','I-'], pd.concat([pd.DataFrame([[
                                  country_import['Country'].values[rr],
                                  country_import['grid_id_40'].values[rr]]
    for rr in range(country_import.shape[0])])]))

#Set - Relation Country - Raw Material Import points

#print('   ...relation countries - raw material import points')
#country_rawimport =  pd.read_excel(file_location+file_name, skiprows=0, sheet_name='Bio_import_points', usecols='B:C')
#bwr.create_parameter_file(file_destination+'set-country-raw-material-import-points-relation.txt',
#                          ['C-','IRM-'], pd.concat([pd.DataFrame([[
#                                  country_rawimport['Country'].values[rr],
#                                  country_rawimport['Feedstock_location'].values[rr]]
#    for rr in range(country_rawimport.shape[0])])]))

#Set - Raw Material - Raw Material Import points

#print('   ...relation feedstock - raw material import points')
#feedstock_rawimport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Bio_import_points', usecols='C:G')
#bwr.create_parameter_file(file_destination+'set-raw-material-import-points-relation.txt',
#                          ['IRM-','RM-'], pd.concat([pd.DataFrame([[
#                                  feedstock_rawimport['Feedstock_location'].values[rr],
#                                  feedstock_rawimport.columns[cc]] 
#    for rr in range(feedstock_rawimport.shape[0])
#    for cc in range(1,feedstock_rawimport.shape[1])
#    if feedstock_rawimport.values[rr,cc]>0])]))



# Relation Plant A - Transport

#print('   ...relation Plant A location-transport')
#plantA_transport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_Trans', usecols='A:U')
#bwr.create_parameter_file(file_destination+'set-plantA-transport-relation.txt',
#                          ['Pa-','T-'], pd.concat([pd.DataFrame([[
#                                  plantA_transport['plantA_ID'].values[rr],
#                                  plantA_transport.columns[cc]] 
#    for rr in range(plantA_transport.shape[0])
#    for cc in range(1,plantA_transport.shape[1])
#    if plantA_transport.values[rr,cc]==1])]))

# Relation Plant A location - Size

print('   ...relation Plant A location-size')
plantA_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Pa_size', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantA-size-relation.txt',
                          ['Pa-','SizePa-'], pd.concat([pd.DataFrame([[
                                  plantA_size['plantA_ID'].values[rr],
                                  plantA_size.columns[cc]] 
    for rr in range(plantA_size.shape[0])
    for cc in range(1,plantA_size.shape[1])
    if plantA_size.values[rr,cc]==1])]))

# Relation Plant A location - Country

print('   ...relation Plant A location-country')
plantA_country =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_distri', usecols='A:AD')
bwr.create_parameter_file(file_destination+'set-plantA-country-relation.txt',
                          ['Pa-','C-'], pd.concat([pd.DataFrame([[
                                  plantA_country['plant_ID'].values[rr],
                                  plantA_country.columns[cc]] 
    for rr in range(plantA_country.shape[0])
    for cc in range(1,plantA_country.shape[1])
    if plantA_country.values[rr,cc]==1])]))

# Relation products plant A - raw material
print('   ...relation products plant A-raw material')
pd_raw =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='A:B')
bwr.create_parameter_file(file_destination+'set-raw-material-product-relation.txt',
                          ['RM-','PRD-'], pd.concat([pd.DataFrame([[
                                  pd_raw['Feedstock'].values[rr],
                                  pd_raw.columns[cc]] 
    for rr in range(pd_raw.shape[0])
    for cc in range(1,pd_raw.shape[1])
    if pd_raw.values[rr,cc]>0])]))

#Relation byproduct plant A - raw material
print('   ...relation byproducts plant A-raw material')
bypd_raw =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='A,C:U')
bwr.create_parameter_file(file_destination+'set-raw-material-byproduct-relation.txt',
                          ['RM-','Byp-'], pd.concat([pd.DataFrame([[
                                  bypd_raw['Feedstock'].values[rr],
                                  bypd_raw.columns[cc]] 
    for rr in range(bypd_raw.shape[0])
    for cc in range(1,bypd_raw.shape[1])
    if bypd_raw.values[rr,cc]>0])]))

#Relation byproduct plant A - raw material
print('   ...relation byproducts plant A-transportation')
bypd_trans =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Byp_Trans', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-byproduct-transportation-relation.txt',
                          ['Byp-','T-'], pd.concat([pd.DataFrame([[
                                  bypd_trans['ID'].values[rr],
                                  bypd_trans.columns[cc]] 
    for rr in range(bypd_trans.shape[0])
    for cc in range(1,bypd_trans.shape[1])
    if bypd_trans.values[rr,cc]>0])]))

# Relation Plant B  - Transport

#print('   ...relation Plant B location-transport')
#plantB_transport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_Trans', usecols='A:U')
#bwr.create_parameter_file(file_destination+'set-plantB-transport-relation.txt',
#                          ['Pb-','T-'], pd.concat([pd.DataFrame([[
#                                  plantB_transport['plantB_ID'].values[rr],
#                                  plantB_transport.columns[cc]] 
#    for rr in range(plantB_transport.shape[0])
#    for cc in range(1,plantB_transport.shape[1])
#    if plantB_transport.values[rr,cc]==1])]))


# Relation Plant B location - Size

print('   ...relation Plant B location-size')
plantB_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Pb_size', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantB-size-relation.txt',
                          ['Pb-','SizePb-'], pd.concat([pd.DataFrame([[
                                  plantB_size['plantB_location'].values[rr],
                                  plantB_size.columns[cc]] 
    for rr in range(plantB_size.shape[0])
    for cc in range(1,plantB_size.shape[1])
    if plantB_size.values[rr,cc]==1])]))


# Relation Plant B location - Country

print('   ...relation Plant B location-country')
plantB_country =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_distri', usecols='A:AD')
bwr.create_parameter_file(file_destination+'set-plantB-country-relation.txt',
                          ['Pb-','C-'], pd.concat([pd.DataFrame([[
                                  plantB_country['plant_ID'].values[rr],
                                  plantB_country.columns[cc]] 
    for rr in range(plantB_country.shape[0])
    for cc in range(1,plantB_country.shape[1])
    if plantB_country.values[rr,cc]==1])]))


# Relation Plant C location - Size

print('   ...relation Plant C location-size')
plantC_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Pc_size', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantC-size-relation.txt',
                          ['Pc-','SizePc-'], pd.concat([pd.DataFrame([[
                                  plantC_size['plantC_location'].values[rr],
                                  plantC_size.columns[cc]] 
    for rr in range(plantC_size.shape[0])
    for cc in range(1,plantC_size.shape[1])
    if plantC_size.values[rr,cc]==1])]))

# Relation Plant C location - Country

print('   ...relation Plant C location-country')
plantC_country =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_distri', usecols='A:AD')
bwr.create_parameter_file(file_destination+'set-plantC-country-relation.txt',
                          ['Pc-','C-'], pd.concat([pd.DataFrame([[
                                  plantC_country['plant_ID'].values[rr],
                                  plantC_country.columns[cc]] 
    for rr in range(plantC_country.shape[0])
    for cc in range(1,plantC_country.shape[1])
    if plantC_country.values[rr,cc]==1])]))


# Relation Plant C  - Transport

#print('   ...relation Plant C location-transport')
#plantC_transport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_Trans', usecols='A:U')
#bwr.create_parameter_file(file_destination+'set-plantC-transport-relation.txt',
#                          ['Pc-','T-'], pd.concat([pd.DataFrame([[
#                                  plantC_transport['plantC_ID'].values[rr],
#                                  plantC_transport.columns[cc]] 
#    for rr in range(plantC_transport.shape[0])
#    for cc in range(1,plantC_transport.shape[1])
#    if plantC_transport.values[rr,cc]==1])]))

# Relation Plant d location - Size

print('   ...relation Plant D location-size')
plantD_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Pd_size', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantD-size-relation.txt',
                          ['Pd-','SizePd-'], pd.concat([pd.DataFrame([[
                                  plantD_size['plantD_location'].values[rr],
                                  plantD_size.columns[cc]] 
    for rr in range(plantD_size.shape[0])
    for cc in range(1,plantD_size.shape[1])
    if plantD_size.values[rr,cc]==1])]))

# Relation Plant D location - Country

print('   ...relation Plant D location-country')
plantD_country =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_distri', usecols='A:AD')
bwr.create_parameter_file(file_destination+'set-plantD-country-relation.txt',
                          ['Pd-','C-'], pd.concat([pd.DataFrame([[
                                  plantD_country['plant_ID'].values[rr],
                                  plantD_country.columns[cc]] 
    for rr in range(plantD_country.shape[0])
    for cc in range(1,plantD_country.shape[1])
    if plantD_country.values[rr,cc]==1])]))


# Relation Plant D  - Transport

print('   ...relation Plant D location-transport')
plantd_transport =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_Trans', usecols='A:U')
bwr.create_parameter_file(file_destination+'set-plantD-transport-relation.txt',
                          ['Pd-','T-'], pd.concat([pd.DataFrame([[
                                  plantd_transport['plantD_ID'].values[rr],
                                  plantd_transport.columns[cc]] 
    for rr in range(plantd_transport.shape[0])
    for cc in range(1,plantd_transport.shape[1])
    if plantd_transport.values[rr,cc]==1])]))


# Relation Plant TPA location - Size

#print('   ...relation Plant TPA location-size')
#plantTPA_size =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PTA_size', usecols='A:U')
#bwr.create_parameter_file(file_destination+'set-plantTPA-size-relation.txt',
#                          ['M-','SizeM-'], pd.concat([pd.DataFrame([[
#                                  plantTPA_size['plantTPA_location'].values[rr],
#                                  plantTPA_size.columns[cc]] 
#    for rr in range(plantTPA_size.shape[0])
#    for cc in range(1,plantTPA_size.shape[1])
#    if plantTPA_size.values[rr,cc]==1])]))

# Relation Plant TPA location - Country

print('   ...relation Plant TPA location-country')
plantTPA_country =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_distri', usecols='A:AD')
bwr.create_parameter_file(file_destination+'set-plantTPA-country-relation.txt',
                          ['M-','C-'], pd.concat([pd.DataFrame([[
                                  plantTPA_country['plant_ID'].values[rr],
                                  plantTPA_country.columns[cc]] 
    for rr in range(plantTPA_country.shape[0])
    for cc in range(1,plantTPA_country.shape[1])
    if plantTPA_country.values[rr,cc]==1])]))


#####################################
#%% Parameters
print('      ...Create the biomass supply parameter')
Biomass_supply =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_available', usecols='A:F')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-availability.txt',
                          ['SR-','RM-'], pd.concat([pd.DataFrame([[
                                  Biomass_supply['Subregion'].values[rr],
                                  Biomass_supply.columns[cc],
                                  round(Biomass_supply.values[rr,cc],2)]
    for rr in range(Biomass_supply.shape[0])
    for cc in range(1,Biomass_supply.shape[1])
    if Biomass_supply.values[rr,cc]>0])]))

print('      ...Create the biomass supply parameter to TPA plant')
Biomass_supply_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_available_orginal', usecols='A,C')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-availability-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  Biomass_supply_TPA['Subregion'].values[rr],
                                  round(Biomass_supply_TPA.values[rr,cc],2)]
    for rr in range(Biomass_supply_TPA.shape[0])
    for cc in range(1,Biomass_supply_TPA.shape[1])
    if Biomass_supply_TPA.values[rr,cc]>0])]))


##Biomass imports
#print('   ...Read the biomass imports dataset')
#biomass_imports =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_imports', usecols='A:U')
#
#print('      ...Create the biomass imports parameter')
#bwr.create_parameter_filex3(file_destination+'parameter-biomass-imports.txt',
#                          ['R-','RM-'], pd.concat([pd.DataFrame([[
#                                  biomass_imports['Region'].values[rr],
#                                  biomass_imports.columns[cc],
#                                  round(biomass_imports.values[rr,cc],2)]
#    for rr in range(biomass_imports.shape[0])
#    for cc in range(2,biomass_imports.shape[1])
#    if biomass_imports.values[rr,cc]>0])]))
#
##Biomass exports
#print('   ...Read the biomass exports dataset')
#biomass_exports =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_exports', usecols='A:U')
#
#print('      ...Create the biomass imports parameter')
#bwr.create_parameter_filex3(file_destination+'parameter-biomass-exports.txt',
#                          ['R-','RM-'], pd.concat([pd.DataFrame([[
#                                  biomass_exports['Region'].values[rr],
#                                  biomass_exports.columns[cc],
#                                  round(biomass_exports.values[rr,cc],2)]
#    for rr in range(biomass_exports.shape[0])
#    for cc in range(2,biomass_exports.shape[1])
#    if biomass_exports.values[rr,cc]>0])]))

#Biomass Supply cost
print('   ...Read the biomass cost dataset')
biomass_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_cost', usecols='A:U')

print('      ...Create the biomass supply cost parameter')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-cost.txt',
                          ['SR-','RM-'], pd.concat([pd.DataFrame([[
                                  biomass_cost['Subregion'].values[rr],
                                  biomass_cost.columns[cc],
                                  biomass_cost.values[rr,cc]]
    for rr in range(biomass_cost.shape[0])
    for cc in range(1,biomass_cost.shape[1])
    if biomass_cost.values[rr,cc]>0])]))


print('   ...Read the biomass cost dataset for TPA plant')
biomass_cost_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Biomass_cost_Dataset', usecols='B,D')

print('      ...Create the biomass supply cost parameter')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-cost-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  biomass_cost_TPA['Subregion'].values[rr],
                                  biomass_cost_TPA.values[rr,cc]]
    for rr in range(biomass_cost_TPA.shape[0])
    for cc in range(1,biomass_cost_TPA.shape[1])
    if biomass_cost_TPA.values[rr,cc]>0])]))

# Fixed Transportation Cost to Plant A
supply_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Fix_Biom_Trans_Cost_Orig', usecols='A:B,E')

print('      ...Create fixed product A transportation cost - Truck')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-fixed-transportation-cost-truck.txt',
                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
                                  supply_transportation_cost_truck['Feedstock'].values[rr],
                                  supply_transportation_cost_truck['Subregion'].values[rr],
                                  supply_transportation_cost_truck.values[rr,cc]]
    for rr in range(supply_transportation_cost_truck.shape[0])
    for cc in range(2,supply_transportation_cost_truck.shape[1])
    if supply_transportation_cost_truck.values[rr,cc]>0])]))

supply_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Fix_Biom_Trans_Cost_Orig', usecols='A:B,F')

print('      ...Create fixed product A transportation cost - Train')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-fixed-transportation-cost-train.txt',
                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
                                  supply_transportation_cost_train['Feedstock'].values[rr],
                                  supply_transportation_cost_train['Subregion'].values[rr],
                                  supply_transportation_cost_train.values[rr,cc]]
    for rr in range(supply_transportation_cost_train.shape[0])
    for cc in range(2,supply_transportation_cost_train.shape[1])
    if supply_transportation_cost_train.values[rr,cc]>0])]))


# Fixed Transportation Cost to Plant TPA
supply_transportation_cost_truck_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Fix_Biom_Trans_Cost_Orig', usecols='B,E')

print('      ...Create fixed product A transportation cost - Truck - TPA')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-fixed-transportation-cost-truck-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  supply_transportation_cost_truck_TPA['Subregion'].values[rr],
                                  supply_transportation_cost_truck_TPA.values[rr,cc]]
    for rr in range(supply_transportation_cost_truck_TPA.shape[0])
    for cc in range(1,supply_transportation_cost_truck_TPA.shape[1])
    if supply_transportation_cost_truck_TPA.values[rr,cc]>0])]))

supply_transportation_cost_train_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Fix_Biom_Trans_Cost_Orig', usecols='B,F')

print('      ...Create fixed product A transportation cost - Train - TPA')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-fixed-transportation-cost-train-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  supply_transportation_cost_train_TPA['Subregion'].values[rr],
                                  supply_transportation_cost_train_TPA.values[rr,cc]]
    for rr in range(supply_transportation_cost_train_TPA.shape[0])
    for cc in range(1,supply_transportation_cost_train_TPA.shape[1])
    if supply_transportation_cost_train_TPA.values[rr,cc]>0])]))



#supply_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Fix_Biom_Trans_Cost_Orig', usecols='A:B,H')
#
#print('      ...Create fixed product A transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-biomass-fixed-transportation-cost-ship.txt',
#                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
#                                  supply_transportation_cost_ship['Feedstock'].values[rr],
#                                  supply_transportation_cost_ship['Subregion'].values[rr],
#                                  supply_transportation_cost_ship.values[rr,cc]]
#    for rr in range(supply_transportation_cost_ship.shape[0])
#    for cc in range(2,supply_transportation_cost_ship.shape[1])
#    if supply_transportation_cost_ship.values[rr,cc]>0])]))

# Cost of Variable transport for product A to plant B

print('   ...Variable transportation cost of product A')
biomass_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Var_Biom_Trans_Cost_Orig', usecols='A:B,E')

print('      ...Variable transportation cost of product A - Truck')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-variable-transportation-cost-truck.txt',
                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
                                  biomass_var_transportation_cost_truck['Feedstock'].values[rr],
                                  biomass_var_transportation_cost_truck['Subregion'].values[rr],
                                  round(biomass_var_transportation_cost_truck.values[rr,cc],3)]
    for rr in range(biomass_var_transportation_cost_truck.shape[0])
    for cc in range(2,biomass_var_transportation_cost_truck.shape[1])
    if biomass_var_transportation_cost_truck.values[rr,cc]>0])]))


print('   ...Variable transportation cost of product A')
biomass_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Var_Biom_Trans_Cost_Orig', usecols='A:B,F')

print('      ...Variable transportation cost of product A - Train')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-variable-transportation-cost-train.txt',
                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
                                  biomass_var_transportation_cost_train['Feedstock'].values[rr],
                                  biomass_var_transportation_cost_train['Subregion'].values[rr],
                                  round(biomass_var_transportation_cost_train.values[rr,cc],3)]
    for rr in range(biomass_var_transportation_cost_train.shape[0])
    for cc in range(2,biomass_var_transportation_cost_train.shape[1])
    if biomass_var_transportation_cost_train.values[rr,cc]>0])]))


# Cost of Variable transport from Supply to Plant TPA

print('   ...Variable transportation cost of product A')
biomass_var_transportation_cost_truck_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Var_Biom_Trans_Cost_Orig', usecols='B,E')

print('      ...Variable transportation cost of product A - Truck')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-variable-transportation-cost-truck-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  biomass_var_transportation_cost_truck_TPA['Subregion'].values[rr],
                                  round(biomass_var_transportation_cost_truck_TPA.values[rr,cc],3)]
    for rr in range(biomass_var_transportation_cost_truck_TPA.shape[0])
    for cc in range(1,biomass_var_transportation_cost_truck_TPA.shape[1])
    if biomass_var_transportation_cost_truck_TPA.values[rr,cc]>0])]))


print('   ...Variable transportation cost of product A')
biomass_var_transportation_cost_train_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Var_Biom_Trans_Cost_Orig', usecols='B,F')

print('      ...Variable transportation cost of product A - Train')
bwr.create_parameter_filex3(file_destination+'parameter-biomass-variable-transportation-cost-train-TPA.txt',
                          ['SR-'], pd.concat([pd.DataFrame([[
                                  biomass_var_transportation_cost_train_TPA['Subregion'].values[rr],
                                  round(biomass_var_transportation_cost_train_TPA.values[rr,cc],3)]
    for rr in range(biomass_var_transportation_cost_train_TPA.shape[0])
    for cc in range(1,biomass_var_transportation_cost_train_TPA.shape[1])
    if biomass_var_transportation_cost_train_TPA.values[rr,cc]>0])]))


#print('   ...Variable transportation cost of product A')
#biomass_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Var_Biom_Trans_Cost_Orig', usecols='A:B,H')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-biomass-variable-transportation-cost-ship.txt',
#                          ['RM-','SR-'], pd.concat([pd.DataFrame([[
#                                  biomass_var_transportation_cost_ship['Feedstock'].values[rr],
#                                  biomass_var_transportation_cost_ship['Subregion'].values[rr],
#                                  round(biomass_var_transportation_cost_ship.values[rr,cc],3)]
#    for rr in range(biomass_var_transportation_cost_ship.shape[0])
#    for cc in range(2,biomass_var_transportation_cost_ship.shape[1])
#    if biomass_var_transportation_cost_ship.values[rr,cc]>0])]))

# Distance Supply Biomass to Plant A - TRUCK

print('   ...Distance Biomass to Plant A')
dist_plantA_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_S_to_Pa_dyn_Truck', usecols='A:AJ')

print('   ...distance from Biomass to plant A - Truck')
bwr.create_parameter_filex3(file_destination+'parameter-distance-supply-plantA-truck.txt',
                            ['RM-','SR-','Pa-'],pd.concat([pd.DataFrame([[
                                  dist_plantA_truck['Feedstock'].values[rr],
                                  dist_plantA_truck['ID'].values[rr],
                                  dist_plantA_truck.columns[cc],
                                  (dist_plantA_truck.values[rr,cc]/1000)]
    for rr in range(dist_plantA_truck.shape[0])
    for cc in range(2,dist_plantA_truck.shape[1])
    if dist_plantA_truck.values[rr,cc]>0])]))

# Distance Supply Biomass to Plant A - TRAIN

print('   ...Distance Biomass to Plant A')
dist_plantA_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_S_to_Pa_dyn_Train', usecols='A:AJ')

print('   ...distance from Biomass to plant A - Train')
bwr.create_parameter_filex3(file_destination+'parameter-distance-supply-plantA-train.txt',
                            ['RM-','SR-','Pa-'],pd.concat([pd.DataFrame([[
                                  dist_plantA_train['Feedstock'].values[rr],
                                  dist_plantA_train['ID'].values[rr],
                                  dist_plantA_train.columns[cc],
                                  (dist_plantA_train.values[rr,cc]/1000)]
    for rr in range(dist_plantA_train.shape[0])
    for cc in range(2,dist_plantA_train.shape[1])
    if dist_plantA_train.values[rr,cc]>0])]))

# Distance Supply Biomass to Plant TPA - TRUCK

print('   ...Distance Biomass to Plant A')
dist_plantA_truck_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_S_to_TPA_dyn_Truck', usecols='B:AJ')

print('   ...distance from Biomass to plant A - Truck')
bwr.create_parameter_filex3(file_destination+'parameter-distance-supply-plantA-truck-TPA.txt',
                            ['SR-','M-'],pd.concat([pd.DataFrame([[
                                  dist_plantA_truck_TPA['ID'].values[rr],
                                  dist_plantA_truck_TPA.columns[cc],
                                  (dist_plantA_truck_TPA.values[rr,cc]/1000)]
    for rr in range(dist_plantA_truck_TPA.shape[0])
    for cc in range(1,dist_plantA_truck_TPA.shape[1])
    if dist_plantA_truck_TPA.values[rr,cc]>0])]))

# Distance Supply Biomass to Plant TPA - TRAIN

print('   ...Distance Biomass to Plant A')
dist_plantA_train_TPA =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_S_to_TPA_dyn_Train', usecols='B:AJ')

print('   ...distance from Biomass to plant A - Train')
bwr.create_parameter_filex3(file_destination+'parameter-distance-supply-plantA-train-TPA.txt',
                            ['SR-','M-'],pd.concat([pd.DataFrame([[
                                  dist_plantA_train_TPA['ID'].values[rr],
                                  dist_plantA_train_TPA.columns[cc],
                                  (dist_plantA_train_TPA.values[rr,cc]/1000)]
    for rr in range(dist_plantA_train_TPA.shape[0])
    for cc in range(1,dist_plantA_train_TPA.shape[1])
    if dist_plantA_train_TPA.values[rr,cc]>0])]))

## Distance Biomass to Plant A - SHIP
#
#print('   ...Distance Biomass to plant A')
#dist_plantA_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_S_to_Pa_dyn_Ship', usecols='A:AJ')
#
#print('   ...distance from Biomass to plant A - Ship')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-supply-plantA-ship.txt',
#                             ['RM-','SR-','Pa-'],pd.concat([pd.DataFrame([[
#                                  dist_plantA_ship['Feedstock'].values[rr],
#                                  dist_plantA_ship['ID'].values[rr],
#                                  dist_plantA_ship.columns[cc],
#                                  (dist_plantA_ship.values[rr,cc]/1000)]
#    for rr in range(dist_plantA_ship.shape[0])
#    for cc in range(2,dist_plantA_ship.shape[1])
#    if dist_plantA_ship.values[rr,cc]>0])]))

#%% PLANT A 

#Cost of Plant A - CaPEX 

print('   ...CAPEX - Plant A')
plantA_capex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantA_cap', usecols='A:U')

print('      ...CAPEX - Plant A')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-capex.txt',
                          ['RM-','Pa-','SizePa-'], pd.concat([pd.DataFrame([[
                                  plantA_capex['Feedstock'].values[rr],
                                  plantA_capex['ID_plant'].values[rr],
                                  plantA_capex.columns[cc],
                                  round(plantA_capex.values[rr,cc],2)]
    for rr in range(plantA_capex.shape[0])
    for cc in range(2,plantA_capex.shape[1])
    if plantA_capex.values[rr,cc]>0])]))

#Fixed and Variable OPEX - Plant A
print('   ...Fixed OPEX - Plant A')
plantA_fix_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantA_fix_op', usecols='A:U')

print('      ...Fixed Opex - Plant A')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-fixed-opex.txt',
                          ['RM-','Pa-','SizePa-'], pd.concat([pd.DataFrame([[
                                  plantA_fix_opex['Feedstock'].values[rr],
                                  plantA_fix_opex['ID_plant'].values[rr],
                                  plantA_fix_opex.columns[cc],
                                  round(plantA_fix_opex.values[rr,cc],2)]
    for rr in range(plantA_fix_opex.shape[0])
    for cc in range(2,plantA_fix_opex.shape[1])
    if plantA_fix_opex.values[rr,cc]>0])]))

print('   ...Fixed OPEX - Plant A')
plantA_var_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PlantA_var_op', usecols='A:U')

print('      ...Variable Opex - Plant A')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-variable-opex.txt',
                          ['RM-','Pa-','SizePa-'], pd.concat([pd.DataFrame([[
                                  plantA_var_opex['Feedstock'].values[rr],
                                  plantA_var_opex['ID_plant'].values[rr],
                                  plantA_var_opex.columns[cc],
                                  round(plantA_var_opex.values[rr,cc],2)]
    for rr in range(plantA_var_opex.shape[0])
    for cc in range(2,plantA_var_opex.shape[1])
    if plantA_var_opex.values[rr,cc]>0])]))


#Ethanol Plant Efficiency

print('   ...Read the ethanol plant efficiency dataset')
ethanol_efficiency =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='A:B')

print('      ...Create the ethanol plant efficiency parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-efficiency.txt',
                          ['RM-','PRD-'], pd.concat([pd.DataFrame([[
                                  ethanol_efficiency['Feedstock'].values[rr],
                                  ethanol_efficiency.columns[cc],
                                  ethanol_efficiency.values[rr,cc]]
    for rr in range(ethanol_efficiency.shape[0])
    for cc in range(1,ethanol_efficiency.shape[1])
    if ethanol_efficiency.values[rr,cc]>0])]))

#By-product conversion yield in Plant A
print('   ...Read the byproducts conversion dataset')
byproduct_form =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_eff', usecols='A,C:U')

print('      ...Create the byproducts conversion parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-byproduct-efficiency.txt',
                          ['RM-','Byp-'], pd.concat([pd.DataFrame([[
                                  byproduct_form['Feedstock'].values[rr],
                                  byproduct_form.columns[cc],
                                  byproduct_form.values[rr,cc]]
    for rr in range(byproduct_form.shape[0])
    for cc in range(1,byproduct_form.shape[1])
    if byproduct_form.values[rr,cc]>0])]))

#Ethanol Plant Capacity

print('   ...Read the ethanol plant capacity dataset')
plantA_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Plant_location', usecols='B,I')

print('      ...Create the ethanol plant capacity parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-capacity.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  plantA_capacity['ID_number'].values[rr],
                                  plantA_capacity['Dyn'].values[rr]]
    for rr in range(plantA_capacity.shape[0])
    if plantA_capacity['Dyn'].values[rr]>0])]))


#Ethanol Plant Capacity - PROSPECTIVE

print('   ...Read the ethanol plant capacity dataset')
plantA_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Plant_location', usecols='B,K')

print('      ...Create the ethanol plant capacity parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantA-capacity-prospective.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  plantA_capacity['ID_number'].values[rr],
                                  round(plantA_capacity['Dyn_Prosp_Cap'].values[rr],2)]
    for rr in range(plantA_capacity.shape[0])
    if plantA_capacity['Dyn_Prosp_Cap'].values[rr]>0])]))


# Production cost of product A 

print('   ...Product A cost')
productA_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_price_dyn', usecols='A:C')

print('      ...Product A cost')
bwr.create_parameter_filex3(file_destination+'parameter-productA-cost.txt',
                          ['RM-','Pa-','PRD-'], pd.concat([pd.DataFrame([[
                                  productA_cost['Feedstock'].values[rr],
                                  productA_cost['pA_location'].values[rr],
                                  productA_cost.columns[cc],
                                  productA_cost.values[rr,cc]]
    for rr in range(0,productA_cost.shape[0])
    for cc in range(2,productA_cost.shape[1])
    if productA_cost.values[rr,cc]>0])]))

#By-products Cost in Plant A

print('   ...Product A cost')
productA_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_price_dyn', usecols='A:B,D:F')

print('      ...Product A cost')
bwr.create_parameter_filex3(file_destination+'parameter-byproductA-cost.txt',
                          ['RM-','Pa-','Byp-'], pd.concat([pd.DataFrame([[
                                  productA_cost['Feedstock'].values[rr],
                                  productA_cost['pA_location'].values[rr],
                                  productA_cost.columns[cc],
                                  round(productA_cost.values[rr,cc],2)]
    for rr in range(productA_cost.shape[0])
    for cc in range(2,productA_cost.shape[1])
    if productA_cost.values[rr,cc]>0])]))

#Product A Fixed Transportation Cost to Plant B
print('   ..Product A transportation cost')
productA_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_fix_trans_cost', usecols='A,C')

print('      ...Create fixed product A transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productA-fixed-transportation-cost-truck.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  productA_transportation_cost_truck['plantA_location'].values[rr],
                                  productA_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productA_transportation_cost_truck.shape[0])
    if productA_transportation_cost_truck['Truck'].values[rr]>0])]))

#Product A Fixed Transportation Cost to Plant B
print('   ..Product A transportation cost')
productA_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_fix_trans_cost', usecols='A,D')

print('      ...Create fixed product A transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productA-fixed-transportation-cost-train.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  productA_transportation_cost_train['plantA_location'].values[rr],
                                  productA_transportation_cost_train['Train'].values[rr]]
    for rr in range(productA_transportation_cost_train.shape[0])
    if productA_transportation_cost_train['Train'].values[rr]>0])]))

#Product A Fixed Transportation Cost to Plant B
#print('   ..Product A transportation cost')
#productA_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed product A transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-productA-fixed-transportation-cost-ship.txt',
#                          ['Pa-'], pd.concat([pd.DataFrame([[
#                                  productA_transportation_cost_ship['plantA_location'].values[rr],
#                                  productA_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productA_transportation_cost_ship.shape[0])
#    if productA_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport for product A to plant B

print('   ...Variable transportation cost of product A')
productA_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productA-variable-transportation-cost-truck.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  productA_var_transportation_cost_truck['plantA_location'].values[rr],
                                  productA_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productA_var_transportation_cost_truck.shape[0])
    if productA_var_transportation_cost_truck['Truck'].values[rr]>0])]))


print('   ...Variable transportation cost of product A')
productA_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_var_trans_cost', usecols='A,D')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productA-variable-transportation-cost-train.txt',
                          ['Pa-'], pd.concat([pd.DataFrame([[
                                  productA_var_transportation_cost_train['plantA_location'].values[rr],
                                  productA_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(productA_var_transportation_cost_train.shape[0])
    if productA_var_transportation_cost_train['Train'].values[rr]>0])]))

#print('   ...Variable transportation cost of product A')
#productA_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodA_var_trans_cost', usecols='A,E')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-productA-variable-transportation-cost-ship.txt',
#                          ['Pa-'], pd.concat([pd.DataFrame([[
#                                  productA_var_transportation_cost_ship['plantA_location'].values[rr],
#                                  productA_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productA_var_transportation_cost_ship.shape[0])
#    if productA_var_transportation_cost_ship['Ship'].values[rr]>0])]))

# Distance Plant A to Plant B - TRUCK

print('   ...Distance Plant A to Plant B')
dist_plantB_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pa_to_Pb_Truck', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantA-plantB-truck.txt',
                            ['Pa-','Pb-'],pd.concat([pd.DataFrame([[
                                  dist_plantB_truck['Location'].values[rr],
                                  dist_plantB_truck.columns[cc],
                                  dist_plantB_truck.values[rr,cc]]
    for rr in range(dist_plantB_truck.shape[0])
    for cc in range(1,dist_plantB_truck.shape[1])
    if dist_plantB_truck.values[rr,cc]>0])]))

# Distance Plant A to Plant B - TRAIN

print('   ...Distance Plant A to Plant B')
dist_plantB_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pa_to_Pb_Train', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantA-plantB-train.txt',
                            ['Pa-','Pb-'],pd.concat([pd.DataFrame([[
                                  dist_plantB_train['Location'].values[rr],
                                  dist_plantB_train.columns[cc],
                                  dist_plantB_train.values[rr,cc]]
    for rr in range(dist_plantB_train.shape[0])
    for cc in range(1,dist_plantB_train.shape[1])
    if dist_plantB_train.values[rr,cc]>0])]))

## Distance Plant A to Plant B - SHIP
#
#print('   ...Distance Plant A to Plant B')
#dist_plantB_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pa_to_Pb_Ship', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantA-plantB-ship.txt',
#                            ['Pa-','Pb-'],pd.concat([pd.DataFrame([[
#                                  dist_plantB_ship['Location'].values[rr],
#                                  dist_plantB_ship.columns[cc],
#                                  dist_plantB_ship.values[rr,cc]]
#    for rr in range(dist_plantB_ship.shape[0])
#    for cc in range(1,dist_plantB_ship.shape[1])
#    if dist_plantB_ship.values[rr,cc]>0])]))

#%% PLANT B

# Plant B Capacity

print('   ...Plant B capacity')
plantB_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pb_location', usecols='A,G')

print('      ...Plant B capacity')
bwr.create_parameter_filex3(file_destination+'parameter-plantB-capacity.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  plantB_capacity['ID_plantB'].values[rr],
                                  plantB_capacity['Ethylene Capacity'].values[rr]]
    for rr in range(plantB_capacity.shape[0])
    if plantB_capacity['Ethylene Capacity'].values[rr]>0])]))

# Plant B efficiency
print('   ...Plant B capacity')
plantB_efficiency =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pb_parameters', usecols='A,E:U')

print('      ...Create the ethanol plant efficiency parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantB-efficiency.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  plantB_efficiency['plant_location'].values[rr],
                                  plantB_efficiency['plantB_efficiency'].values[rr]]
    for rr in range(plantB_efficiency.shape[0])
    if plantB_efficiency['plantB_efficiency'].values[rr]>0])]))


#Cost of Plant B - CaPEX 

print('   ...CAPEX - Plant B')
plantB_capex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_cap', usecols='A:U')

print('      ...CAPEX - Plant B')
bwr.create_parameter_filex3(file_destination+'parameter-plantB-capex.txt',
                          ['Pb-','C-','SizePb-'], pd.concat([pd.DataFrame([[
                                  plantB_capex['plantB_location'].values[rr],
                                  plantB_capex['Country'].values[rr],
                                  plantB_capex.columns[cc],
                                  round(plantB_capex.values[rr,cc],2)]
    for rr in range(plantB_capex.shape[0])
    for cc in range(2,plantB_capex.shape[1])
    if plantB_capex.values[rr,cc]>0])]))

#Cost of Plant B - Fixed OPEX

print('   ...Fixed OPEX - Plant B')
plantB_fix_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_fix_opex', usecols='A:U')

print('      ...Fixed Opex - Plant B')
bwr.create_parameter_filex3(file_destination+'parameter-plantB-fixed-opex.txt',
                           ['Pb-','C-','SizePb-'], pd.concat([pd.DataFrame([[
                                  plantB_fix_opex['plantB_location'].values[rr],
                                  plantB_fix_opex['Country'].values[rr],
                                  plantB_fix_opex.columns[cc],
                                  round(plantB_fix_opex.values[rr,cc],2)]
    for rr in range(plantB_fix_opex.shape[0])
    for cc in range(2,plantB_fix_opex.shape[1])
    if plantB_fix_opex.values[rr,cc]>0])]))


#Cost of Plant B - Variable OPEX

print('   ...Variable OPEX - Plant B')
plantB_var_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_var_opex', usecols='A:U')

print('      ...Variable Opex - Plant B')
bwr.create_parameter_filex3(file_destination+'parameter-plantB-variable-opex.txt',
                          ['Pb-','C-','SizePb-'], pd.concat([pd.DataFrame([[
                                  plantB_var_opex['plantB_location'].values[rr],
                                  plantB_var_opex['Country'].values[rr],
                                  plantB_var_opex.columns[cc],
                                  round(plantB_var_opex.values[rr,cc],2)]
    for rr in range(plantB_var_opex.shape[0])
    for cc in range(2,plantB_var_opex.shape[1])
    if plantB_var_opex.values[rr,cc]>0])]))

# Production cost of product B to be transported to Plant C

print('   ...Product B cost')
productB_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_price', usecols='A:U')

print('      ...Product B cost')
bwr.create_parameter_filex3(file_destination+'parameter-productB-cost.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  productB_cost['pB_location'].values[rr],
                                  productB_cost['Price'].values[rr]]
    for rr in range(productB_cost.shape[0])
    if productB_cost['Price'].values[rr]>0])]))

#Product B Fixed Transportation Cost to Plant C
print('   ..Product B transportation cost')
productB_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_fix_trans_cost', usecols='A,C')

print('      ...Create fixed product B transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productB-fixed-transportation-cost-truck.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  productB_transportation_cost_truck['plantB_location'].values[rr],
                                  productB_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productB_transportation_cost_truck.shape[0])
    if productB_transportation_cost_truck['Truck'].values[rr]>0])]))


print('   ..Product B transportation cost')
productB_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_fix_trans_cost', usecols='A,D')

print('      ...Create fixed product A transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productB-fixed-transportation-cost-train.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  productB_transportation_cost_train['plantB_location'].values[rr],
                                  productB_transportation_cost_train['Train'].values[rr]]
    for rr in range(productB_transportation_cost_train.shape[0])
    if productB_transportation_cost_train['Train'].values[rr]>0])]))


#print('   ..Product B transportation cost')
#productB_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed product A transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-productB-fixed-transportation-cost-ship.txt',
#                          ['Pb-'], pd.concat([pd.DataFrame([[
#                                  productB_transportation_cost_ship['plantB_location'].values[rr],
#                                  productB_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productB_transportation_cost_ship.shape[0])
#    if productB_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport for product B to plant C

print('   ...Variable transportation cost of product B')
productB_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productB-variable-transportation-cost-truck.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  productB_var_transportation_cost_truck['plantB_location'].values[rr],
                                  productB_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productB_var_transportation_cost_truck.shape[0])
    if productB_var_transportation_cost_truck['Truck'].values[rr]>0])]))


print('   ...Variable transportation cost of product A')
productB_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_var_trans_cost', usecols='A,D')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productB-variable-transportation-cost-train.txt',
                          ['Pb-'], pd.concat([pd.DataFrame([[
                                  productB_var_transportation_cost_train['plantB_location'].values[rr],
                                  productB_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(productB_var_transportation_cost_train.shape[0])
    if productB_var_transportation_cost_train['Train'].values[rr]>0])]))

#print('   ...Variable transportation cost of product A')
#productB_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodB_var_trans_cost', usecols='A,E')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-productB-variable-transportation-cost-ship.txt',
#                          ['Pb-'], pd.concat([pd.DataFrame([[
#                                  productB_var_transportation_cost_ship['plantB_location'].values[rr],
#                                  productB_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productB_var_transportation_cost_ship.shape[0])
#    if productB_var_transportation_cost_ship['Ship'].values[rr]>0])]))

# Distance Plant B to Plant C - TRUCK

print('   ...Distance Plant A to Plant B')
dist_plantC_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pb_to_Pc_Truck', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantB-plantC-truck.txt',
                            ['Pb-','Pc-'],pd.concat([pd.DataFrame([[
                                  dist_plantC_truck['Location'].values[rr],
                                  dist_plantC_truck.columns[cc],
                                  dist_plantC_truck.values[rr,cc]]
    for rr in range(dist_plantC_truck.shape[0])
    for cc in range(1,dist_plantC_truck.shape[1])
    if dist_plantC_truck.values[rr,cc]>0])]))

# Distance Plant A to Plant B - TRAIN

print('   ...Distance Plant A to Plant B')
dist_plantC_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pb_to_Pc_Train', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantB-plantC-train.txt',
                            ['Pb-','Pc-'],pd.concat([pd.DataFrame([[
                                  dist_plantC_train['Location'].values[rr],
                                  dist_plantC_train.columns[cc],
                                  dist_plantC_train.values[rr,cc]]
    for rr in range(dist_plantC_train.shape[0])
    for cc in range(1,dist_plantC_train.shape[1])
    if dist_plantC_train.values[rr,cc]>0])]))

# Distance Plant A to Plant B - SHIP

#print('   ...Distance Plant A to Plant B')
#dist_plantC_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pb_to_Pc_Ship', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantB-plantC-ship.txt',
#                            ['Pb-','Pc-'],pd.concat([pd.DataFrame([[
#                                  dist_plantC_ship['Location'].values[rr],
#                                  dist_plantC_ship.columns[cc],
#                                  dist_plantC_ship.values[rr,cc]]
#    for rr in range(dist_plantC_ship.shape[0])
#    for cc in range(1,dist_plantC_ship.shape[1])
#    if dist_plantC_ship.values[rr,cc]>0])]))


#%% PLANT C

# Plant C Capacity

print('   ...Plant C capacity')
plantC_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pc_location', usecols='A,G')

print('      ...Plant C capacity')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-capacity.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  plantC_capacity['ID_plantC'].values[rr],
                                  plantC_capacity['Ethylene Oxide Capacity'].values[rr]]
    for rr in range(plantC_capacity.shape[0])
    if plantC_capacity['Ethylene Oxide Capacity'].values[rr]>0])]))

# Plant C efficiency

print('   ...Plant C efficiency-EO')
plantC_efficiency =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pc_parameters', usecols='A,E')

print('      ...Create efficiency parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-efficiency-EO.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  plantC_efficiency['plant_location'].values[rr],
                                  plantC_efficiency['EO_eff'].values[rr]]
    for rr in range(plantC_efficiency.shape[0])
    if plantC_efficiency['EO_eff'].values[rr]>0])]))

# Plant C efficiency

print('   ...Plant C efficiency-EG')
plantC_efficiencyEG =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pc_parameters', usecols='A,F')

print('      ...Create efficiency parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-efficiency-EG.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  plantC_efficiencyEG['plant_location'].values[rr],
                                  plantC_efficiencyEG['EG_eff'].values[rr]]
    for rr in range(plantC_efficiencyEG.shape[0])
    if plantC_efficiencyEG['EG_eff'].values[rr]>0])]))

#Cost of Plant C - CAPEX

print('   ...CAPEX - Plant C')
plantC_capex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_cap', usecols='A:U')

print('      ...CAPEX - Plant C')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-capex.txt',
                          ['Pc-','C-','SizePc-'], pd.concat([pd.DataFrame([[
                                  plantC_capex['plantC_location'].values[rr],
                                  plantC_capex['Country'].values[rr],
                                  plantC_capex.columns[cc],
                                  round(plantC_capex.values[rr,cc],2)]
    for rr in range(plantC_capex.shape[0])
    for cc in range(2,plantC_capex.shape[1])
    if plantC_capex.values[rr,cc]>0])]))

#Cost of Plant C - Fixed OPEX

print('   ...Fixed OPEX - Plant C')
plantC_fix_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_fix_opex', usecols='A:U')

print('      ...Fixed Opex - Plant C')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-fixed-opex.txt',
                          ['Pc-','C-','SizePc-'], pd.concat([pd.DataFrame([[
                                  plantC_fix_opex['plantC_location'].values[rr],
                                  plantC_fix_opex['Country'].values[rr],
                                  plantC_fix_opex.columns[cc],
                                  round(plantC_fix_opex.values[rr,cc],2)]
    for rr in range(plantC_fix_opex.shape[0])
    for cc in range(2,plantC_fix_opex.shape[1])
    if plantC_fix_opex.values[rr,cc]>0])]))

#Cost of Plant C - Variable OPEX

print('   ...Variable OPEX - Plant C')
plantC_var_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_var_opex', usecols='A:U')

print('      ...Variable Opex - Plant C')
bwr.create_parameter_filex3(file_destination+'parameter-plantC-variable-opex.txt',
                          ['Pc-','C-','SizePc-'], pd.concat([pd.DataFrame([[
                                  plantC_var_opex['plantC_location'].values[rr],
                                  plantC_var_opex['Country'].values[rr],
                                  plantC_var_opex.columns[cc],
                                  round(plantC_var_opex.values[rr,cc],2)]
    for rr in range(plantC_var_opex.shape[0])
    for cc in range(2,plantC_var_opex.shape[1])
    if plantC_var_opex.values[rr,cc]>0])]))


# Production cost of product C to be transported to Demand D

#print('   ...Product C cost-EO')
#productC_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_price', usecols='A,E')
#
#print('      ...Product C cost')
#bwr.create_parameter_filex3(file_destination+'parameter-productC-cost-EO.txt',
#                          ['Pc-'], pd.concat([pd.DataFrame([[
#                                  productC_cost['pC_location'].values[rr],
#                                  round(productC_cost['P_EO'].values[rr],2)]
#    for rr in range(productC_cost.shape[0])
#    if productC_cost['P_EO'].values[rr]>0])]))


# Production cost of product C to be transported to Demand D

print('   ...Product C cost-EG')
productC_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_price', usecols='A,F')

print('      ...Product C cost')
bwr.create_parameter_filex3(file_destination+'parameter-productC-cost-EG.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  productC_cost['pC_location'].values[rr],
                                  round(productC_cost['P_EG'].values[rr],2)]
    for rr in range(productC_cost.shape[0])
    if productC_cost['P_EG'].values[rr]>0])]))

#Product C Fixed Transportation Cost to Plant D
print('   ..Product B transportation cost')
productC_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_fix_trans_cost', usecols='A,C')

print('      ...Create fixed product B transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productC-fixed-transportation-cost-truck.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  productC_transportation_cost_truck['plantC_location'].values[rr],
                                  productC_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productC_transportation_cost_truck.shape[0])
    if productC_transportation_cost_truck['Truck'].values[rr]>0])]))


print('   ..Product B transportation cost')
productC_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_fix_trans_cost', usecols='A,D')

print('      ...Create fixed product A transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productC-fixed-transportation-cost-train.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  productC_transportation_cost_train['plantC_location'].values[rr],
                                  productC_transportation_cost_train['Train'].values[rr]]
    for rr in range(productC_transportation_cost_train.shape[0])
    if productC_transportation_cost_train['Train'].values[rr]>0])]))


#print('   ..Product B transportation cost')
#productC_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed product A transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-productC-fixed-transportation-cost-ship.txt',
#                          ['Pc-'], pd.concat([pd.DataFrame([[
#                                  productC_transportation_cost_ship['plantC_location'].values[rr],
#                                  productC_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productC_transportation_cost_ship.shape[0])
#    if productC_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport for product B to plant C

print('   ...Variable transportation cost of product B')
productC_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productC-variable-transportation-cost-truck.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  productC_var_transportation_cost_truck['plantC_location'].values[rr],
                                  productC_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productC_var_transportation_cost_truck.shape[0])
    if productC_var_transportation_cost_truck['Truck'].values[rr]>0])]))


print('   ...Variable transportation cost of product A')
productC_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_var_trans_cost', usecols='A,D')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productC-variable-transportation-cost-train.txt',
                          ['Pc-'], pd.concat([pd.DataFrame([[
                                  productC_var_transportation_cost_train['plantC_location'].values[rr],
                                  productC_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(productC_var_transportation_cost_train.shape[0])
    if productC_var_transportation_cost_train['Train'].values[rr]>0])]))
#
#print('   ...Variable transportation cost of product A')
#productC_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodC_var_trans_cost', usecols='A,E')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-productC-variable-transportation-cost-ship.txt',
#                          ['Pc-'], pd.concat([pd.DataFrame([[
#                                  productC_var_transportation_cost_ship['plantC_location'].values[rr],
#                                  productC_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productC_var_transportation_cost_ship.shape[0])
#    if productC_var_transportation_cost_ship['Ship'].values[rr]>0])]))

# Distance Plant B to Plant C - TRUCK

print('   ...Distance Plant A to Plant B')
dist_plantD_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pc_to_Pd_Truck', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantC-plantD-truck.txt',
                            ['Pc-','Pd-'],pd.concat([pd.DataFrame([[
                                  dist_plantD_truck['Location'].values[rr],
                                  dist_plantD_truck.columns[cc],
                                  dist_plantD_truck.values[rr,cc]]
    for rr in range(dist_plantD_truck.shape[0])
    for cc in range(1,dist_plantD_truck.shape[1])
    if dist_plantD_truck.values[rr,cc]>0])]))

# Distance Plant A to Plant B - TRAIN

print('   ...Distance Plant A to Plant B')
dist_plantD_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pc_to_Pd_Train', usecols='A:Z')

print('   ...distance from Plant A to plant B')
bwr.create_parameter_filex3(file_destination+'parameter-distance-plantC-plantD-train.txt',
                            ['Pc-','Pd-'],pd.concat([pd.DataFrame([[
                                  dist_plantD_train['Location'].values[rr],
                                  dist_plantD_train.columns[cc],
                                  dist_plantD_train.values[rr,cc]]
    for rr in range(dist_plantD_train.shape[0])
    for cc in range(1,dist_plantD_train.shape[1])
    if dist_plantD_train.values[rr,cc]>0])]))

# Distance Plant A to Plant B - SHIP

#print('   ...Distance Plant A to Plant B')
#dist_plantD_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pc_to_Pd_Ship', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantC-plantD-ship.txt',
#                            ['Pc-','Pd-'],pd.concat([pd.DataFrame([[
#                                  dist_plantD_ship['Location'].values[rr],
#                                  dist_plantD_ship.columns[cc],
#                                  dist_plantD_ship.values[rr,cc]]
#    for rr in range(dist_plantD_ship.shape[0])
#    for cc in range(1,dist_plantD_ship.shape[1])
#    if dist_plantD_ship.values[rr,cc]>0])]))


#%% PLANT D

# Plant D Capacity

print('   ...Plant D capacity')
plantD_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pd_location', usecols='A,G')

print('      ...Plant D capacity')
bwr.create_parameter_filex3(file_destination+'parameter-plantD-capacity.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  plantD_capacity['ID_plantD'].values[rr],
                                  plantD_capacity['PET Capacity'].values[rr]]
    for rr in range(plantD_capacity.shape[0])
    if plantD_capacity['PET Capacity'].values[rr]>0])]))

# Plant D efficiency

print('   ...Plant D efficiency')
plantD_efficiency =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='pd_parameters', usecols='A,E')

print('      ...Create efficiency parameter')
bwr.create_parameter_filex3(file_destination+'parameter-plantD-efficiency.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  plantD_efficiency['plant_location'].values[rr],
                                  plantD_efficiency['PET_eff'].values[rr]]
    for rr in range(plantD_efficiency.shape[0])
    if plantD_efficiency['PET_eff'].values[rr]>0])]))


#Cost of Plant D - CAPEX

print('   ...CAPEX - Plant D')
plantD_capex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_cap', usecols='A:U')

print('      ...CAPEX - Plant ')
bwr.create_parameter_filex3(file_destination+'parameter-plantD-capex.txt',
                          ['Pd-','C-','SizePd-'], pd.concat([pd.DataFrame([[
                                  plantD_capex['plantD_location'].values[rr],
                                  plantD_capex['Country'].values[rr],
                                  plantD_capex.columns[cc],
                                  round(plantD_capex.values[rr,cc],2)]
    for rr in range(plantD_capex.shape[0])
    for cc in range(2,plantD_capex.shape[1])
    if plantD_capex.values[rr,cc]>0])]))

#Cost of Plant D - Fixed OPEX

print('   ...Fixed OPEX - Plant D')
plantD_fix_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_fix_opex', usecols='A:U')

print('      ...Fixed Opex - Plant D')
bwr.create_parameter_filex3(file_destination+'parameter-plantD-fixed-opex.txt',
                          ['Pd-','C-','SizePd-'], pd.concat([pd.DataFrame([[
                                  plantD_fix_opex['plantD_location'].values[rr],
                                  plantD_fix_opex['Country'].values[rr],
                                  plantD_fix_opex.columns[cc],
                                  round(plantD_fix_opex.values[rr,cc],2)]
    for rr in range(plantD_fix_opex.shape[0])
    for cc in range(2,plantD_fix_opex.shape[1])
    if plantD_fix_opex.values[rr,cc]>0])]))

#Cost of Plant D - Variable OPEX

print('   ...Variable OPEX - Plant D')
plantD_var_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_var_opex', usecols='A:U')

print('      ...Variable Opex - Plant D')
bwr.create_parameter_filex3(file_destination+'parameter-plantD-variable-opex.txt',
                          ['Pd-','C-','SizePd-'], pd.concat([pd.DataFrame([[
                                  plantD_var_opex['plantD_location'].values[rr],
                                  plantD_var_opex['Country'].values[rr],
                                  plantD_var_opex.columns[cc],
                                  round(plantD_var_opex.values[rr,cc],2)]
    for rr in range(plantD_var_opex.shape[0])
    for cc in range(2,plantD_var_opex.shape[1])
    if plantD_var_opex.values[rr,cc]>0])]))


# Production cost of product D to be transported to Demand D

print('   ...Product D cost')
productD_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_price', usecols='A,D')

print('      ...Product D cost')
bwr.create_parameter_filex3(file_destination+'parameter-productD-cost.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  productD_cost['pD_location'].values[rr],
                                  round(productD_cost['P_PET'].values[rr],2)]
    for rr in range(productD_cost.shape[0])
    if productD_cost['P_PET'].values[rr]>0])]))


#Product D Fixed Transportation Cost to Demand
productD_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_fix_trans_cost', usecols='A,C')

print('      ...Create fixed product B transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productD-fixed-transportation-cost-truck.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  productD_transportation_cost_truck['plantD_location'].values[rr],
                                  productD_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productD_transportation_cost_truck.shape[0])
    if productD_transportation_cost_truck['Truck'].values[rr]>0])]))


productD_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_fix_trans_cost', usecols='A,D')

print('      ...Create fixed product A transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-productD-fixed-transportation-cost-train.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  productD_transportation_cost_train['plantD_location'].values[rr],
                                  productD_transportation_cost_train['Train'].values[rr]]
    for rr in range(productD_transportation_cost_train.shape[0])
    if productD_transportation_cost_train['Train'].values[rr]>0])]))


#productD_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed product A transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-productD-fixed-transportation-cost-ship.txt',
#                          ['Pd-'], pd.concat([pd.DataFrame([[
#                                  productD_transportation_cost_ship['plantD_location'].values[rr],
#                                  productD_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productD_transportation_cost_ship.shape[0])
#    if productD_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport for product B to plant C

productD_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productD-variable-transportation-cost-truck.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  productD_var_transportation_cost_truck['plantD_location'].values[rr],
                                  productD_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(productD_var_transportation_cost_truck.shape[0])
    if productD_var_transportation_cost_truck['Truck'].values[rr]>0])]))


productD_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_var_trans_cost', usecols='A,D')

print('      ...Variable transportation cost of product A')
bwr.create_parameter_filex3(file_destination+'parameter-productD-variable-transportation-cost-train.txt',
                          ['Pd-'], pd.concat([pd.DataFrame([[
                                  productD_var_transportation_cost_train['plantD_location'].values[rr],
                                  productD_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(productD_var_transportation_cost_train.shape[0])
    if productD_var_transportation_cost_train['Train'].values[rr]>0])]))

#productD_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='prodD_var_trans_cost', usecols='A,E')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-productD-variable-transportation-cost-ship.txt',
#                          ['Pd-'], pd.concat([pd.DataFrame([[
#                                  productD_var_transportation_cost_ship['plantD_location'].values[rr],
#                                  productD_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(productD_var_transportation_cost_ship.shape[0])
#    if productD_var_transportation_cost_ship['Ship'].values[rr]>0])]))

## Distance Plant B to Plant C - TRUCK
#
#print('   ...Distance Plant D to Demand')
#dist_demand_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Truck', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-Demand-truck.txt',
#                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
#                                  dist_demand_truck['Location'].values[rr],
#                                  dist_demand_truck.columns[cc],
#                                  dist_demand_truck.values[rr,cc]]
#    for rr in range(dist_demand_truck.shape[0])
#    for cc in range(1,dist_demand_truck.shape[1])
#    if dist_demand_truck.values[rr,cc]>0])]))
#
## Distance Plant A to Plant B - TRAIN
#
#print('   ...Distance Plant A to Plant B')
#dist_demand_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Train', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-Demand-train.txt',
#                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
#                                  dist_demand_train['Location'].values[rr],
#                                  dist_demand_train.columns[cc],
#                                  dist_demand_train.values[rr,cc]]
#    for rr in range(dist_demand_train.shape[0])
#    for cc in range(1,dist_demand_train.shape[1])
#    if dist_demand_train.values[rr,cc]>0])]))
#
## Distance Plant A to Plant B - SHIP
#
#
#dist_demand_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Ship', usecols='A:Z')
#
#print('   ...distance from Plant A to plant B')
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-demand-ship.txt',
#                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
#                                  dist_demand_ship['Location'].values[rr],
#                                  dist_demand_ship.columns[cc],
#                                  dist_demand_ship.values[rr,cc]]
#    for rr in range(dist_demand_ship.shape[0])
#    for cc in range(1,dist_demand_ship.shape[1])
#    if dist_demand_ship.values[rr,cc]>0])]))

#%% TPA PLANT PARAMETERS

# Capacity plant  PTA

PTA_capacity =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PTA_price', usecols='A,E')

print('      ...Plant PTa capacity cost')
bwr.create_parameter_filex3(file_destination+'parameter-capacity-PTA.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  PTA_capacity['PTA_location'].values[rr],
                                  round(PTA_capacity['Capacity'].values[rr],2)]
    for rr in range(PTA_capacity.shape[0])
    if PTA_capacity['Capacity'].values[rr]>0])]))


# Price PTA

PTA_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='PTA_price', usecols='A,D')

print('      ...Fossil-based alternative cost')
bwr.create_parameter_filex3(file_destination+'parameter-PTA-cost.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  PTA_cost['PTA_location'].values[rr],
                                  round(PTA_cost['P_PTA'].values[rr],2)]
    for rr in range(PTA_cost.shape[0])
    if PTA_cost['P_PTA'].values[rr]>0])]))


#Cost of Plant TPA - CAPEX

print('   ...CAPEX - Plant TPA')
plantTPA_capex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_cap', usecols='A:U')

print('      ...CAPEX - Plant TPA')
bwr.create_parameter_filex3(file_destination+'parameter-plantTPA-capex.txt',
                          ['M-','C-','SizeM-'], pd.concat([pd.DataFrame([[
                                  plantTPA_capex['plantTPA_location'].values[rr],
                                  plantTPA_capex['Country'].values[rr],
                                  plantTPA_capex.columns[cc],
                                  round(plantTPA_capex.values[rr,cc],2)]
    for rr in range(plantTPA_capex.shape[0])
    for cc in range(2,plantTPA_capex.shape[1])
    if plantTPA_capex.values[rr,cc]>0])]))

#Cost of Plant TPA - Fixed OPEX

print('   ...Fixed OPEX - Plant TPA')
plantTPA_fix_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_fix_opex', usecols='A:U')

print('      ...Fixed Opex - Plant TPA')
bwr.create_parameter_filex3(file_destination+'parameter-plantTPA-fixed-opex.txt',
                          ['M-','C-','SizeM-'], pd.concat([pd.DataFrame([[
                                  plantTPA_fix_opex['plantTPA_location'].values[rr],
                                  plantTPA_fix_opex['Country'].values[rr],
                                  plantTPA_fix_opex.columns[cc],
                                  round(plantTPA_fix_opex.values[rr,cc],2)]
    for rr in range(plantTPA_fix_opex.shape[0])
    for cc in range(2,plantTPA_fix_opex.shape[1])
    if plantTPA_fix_opex.values[rr,cc]>0])]))

#Cost of Plant TPA - Variable OPEX

print('   ...Variable OPEX - Plant TPA')
plantTPA_var_opex =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_var_opex', usecols='A:U')

print('      ...Variable Opex - Plant TPA')
bwr.create_parameter_filex3(file_destination+'parameter-plantTPA-variable-opex.txt',
                          ['M-','C-','SizeM-'], pd.concat([pd.DataFrame([[
                                  plantTPA_var_opex['plantTPA_location'].values[rr],
                                  plantTPA_var_opex['Country'].values[rr],
                                  plantTPA_var_opex.columns[cc],
                                  round(plantTPA_var_opex.values[rr,cc],2)]
    for rr in range(plantTPA_var_opex.shape[0])
    for cc in range(2,plantTPA_var_opex.shape[1])
    if plantTPA_var_opex.values[rr,cc]>0])]))


#TPA Fixed Transportation Cost to PET
TPA_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_fix_trans_cost', usecols='A,C')

print('      ...Create fixed TPA transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-TPA-fixed-transportation-cost-truck.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  TPA_transportation_cost_truck['plantTPA_location'].values[rr],
                                  TPA_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(TPA_transportation_cost_truck.shape[0])
    if TPA_transportation_cost_truck['Truck'].values[rr]>0])]))


TPA_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_fix_trans_cost', usecols='A,D')

print('      ...Create fixed TPA transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-TPA-fixed-transportation-cost-train.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  TPA_transportation_cost_train['plantTPA_location'].values[rr],
                                  TPA_transportation_cost_train['Train'].values[rr]]
    for rr in range(TPA_transportation_cost_train.shape[0])
    if TPA_transportation_cost_train['Train'].values[rr]>0])]))


#TPA_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed TPA transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-TPA-fixed-transportation-cost-ship.txt',
#                          ['M-'], pd.concat([pd.DataFrame([[
#                                  TPA_transportation_cost_ship['plantTPA_location'].values[rr],
#                                  TPA_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(TPA_transportation_cost_ship.shape[0])
#    if TPA_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport for TPA to plant D

TPA_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of TPA')
bwr.create_parameter_filex3(file_destination+'parameter-TPA-variable-transportation-cost-truck.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  TPA_var_transportation_cost_truck['plantTPA_location'].values[rr],
                                  TPA_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(TPA_var_transportation_cost_truck.shape[0])
    if TPA_var_transportation_cost_truck['Truck'].values[rr]>0])]))


TPA_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_var_trans_cost', usecols='A,D')

print('      ...Variable transportation cost of TPA')
bwr.create_parameter_filex3(file_destination+'parameter-TPA-variable-transportation-cost-train.txt',
                          ['M-'], pd.concat([pd.DataFrame([[
                                  TPA_var_transportation_cost_train['plantTPA_location'].values[rr],
                                  TPA_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(TPA_var_transportation_cost_train.shape[0])
    if TPA_var_transportation_cost_train['Train'].values[rr]>0])]))

#TPA_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='TPA_var_trans_cost', usecols='A,E')
#
#print('      ...Variable transportation cost of product A')
#bwr.create_parameter_filex3(file_destination+'parameter-TPA-variable-transportation-cost-ship.txt',
#                          ['M-'], pd.concat([pd.DataFrame([[
#                                  TPA_var_transportation_cost_ship['plantTPA_location'].values[rr],
#                                  TPA_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(TPA_var_transportation_cost_ship.shape[0])
#    if TPA_var_transportation_cost_ship['Ship'].values[rr]>0])]))

# Distance Plant TPA to PLant D - TRUCK

print('   ...Distance Plant TPA to Plant D')
dist_plantTPA_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_TPA_to_Pd_Truck', usecols='A:Z')

bwr.create_parameter_filex3(file_destination+'parameter-distance-plantTPA-plantD-truck.txt',
                            ['M-','Pd-'],pd.concat([pd.DataFrame([[
                                  dist_plantTPA_truck['Location'].values[rr],
                                  dist_plantTPA_truck.columns[cc],
                                  dist_plantTPA_truck.values[rr,cc]]
    for rr in range(dist_plantTPA_truck.shape[0])
    for cc in range(1,dist_plantTPA_truck.shape[1])
    if dist_plantTPA_truck.values[rr,cc]>0])]))

# Distance Plant TPA to Plant D - TRAIN

print('   ...Distance Plant TPA to Plant D')
dist_plantTPA_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_TPA_to_Pd_Train', usecols='A:Z')

bwr.create_parameter_filex3(file_destination+'parameter-distance-plantTPA-plantD-train.txt',
                            ['M-','Pd-'],pd.concat([pd.DataFrame([[
                                  dist_plantTPA_train['Location'].values[rr],
                                  dist_plantTPA_train.columns[cc],
                                  dist_plantTPA_train.values[rr,cc]]
    for rr in range(dist_plantTPA_train.shape[0])
    for cc in range(1,dist_plantTPA_train.shape[1])
    if dist_plantTPA_train.values[rr,cc]>0])]))

# Distance Plant TPA to Plant D - SHIP

#print('   ...Distance Plant TPA to Plant D')
#dist_plantTPA_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_TPA_to_Pd_Ship', usecols='A:Z')
#
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantTPA-plantD-ship.txt',
#                            ['M-','Pd-'],pd.concat([pd.DataFrame([[
#                                  dist_plantTPA_ship['Location'].values[rr],
#                                  dist_plantTPA_ship.columns[cc],
#                                  dist_plantTPA_ship.values[rr,cc]]
#    for rr in range(dist_plantTPA_ship.shape[0])
#    for cc in range(1,dist_plantTPA_ship.shape[1])
#    if dist_plantTPA_ship.values[rr,cc]>0])]))

#%% PLANT PRE-FORM PET

# Price fossil-based polymer

#print('   ...Fossil-based alternative cost')
#fossil_cost =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='fossil_based_price', usecols='A:U')
#
#print('      ...Fossil-based alternative cost')
#bwr.create_parameter_filex3(file_destination+'parameter-fossil-cost.txt',
#                          ['D-'], pd.concat([pd.DataFrame([[
#                                  fossil_cost['ID_number'].values[rr],
#                                  fossil_cost['Price'].values[rr]]
#    for rr in range(fossil_cost.shape[0])
#    if fossil_cost['Price'].values[rr]>0])]))


# Demand requirements

print('   ...Demand requirements')
demand_need =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Demand', usecols='A,G')

print('      ...Demand requirements')
bwr.create_parameter_filex3(file_destination+'parameter-demand.txt',
                          ['D-'], pd.concat([pd.DataFrame([[
                                  demand_need['ID_Demand'].values[rr],
                                  demand_need['Capacity'].values[rr]*2]
    for rr in range(demand_need.shape[0])
    if demand_need['Capacity'].values[rr]>0])]))


# Fixed Transportation Cost of PET to PRE-form plants

D_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_fix_trans_cost', usecols='A,C')

print('      ...Create fixed Demand transportation cost')
bwr.create_parameter_filex3(file_destination+'parameter-demand-fixed-transportation-cost-truck.txt',
                          ['D-'], pd.concat([pd.DataFrame([[
                                  D_transportation_cost_truck['Demand_location'].values[rr],
                                  D_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(D_transportation_cost_truck.shape[0])
    if D_transportation_cost_truck['Truck'].values[rr]>0])]))


D_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_fix_trans_cost', usecols='A,D')

bwr.create_parameter_filex3(file_destination+'parameter-demand-fixed-transportation-cost-train.txt',
                          ['D-'], pd.concat([pd.DataFrame([[
                                  D_transportation_cost_train['Demand_location'].values[rr],
                                  D_transportation_cost_train['Train'].values[rr]]
    for rr in range(D_transportation_cost_train.shape[0])
    if D_transportation_cost_train['Train'].values[rr]>0])]))


#D_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_fix_trans_cost', usecols='A,E')
#
#print('      ...Create fixed D transportation cost')
#bwr.create_parameter_filex3(file_destination+'parameter-demand-fixed-transportation-cost-ship.txt',
#                          ['D-'], pd.concat([pd.DataFrame([[
#                                  D_transportation_cost_ship['Demand_location'].values[rr],
#                                  D_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(D_transportation_cost_ship.shape[0])
#    if D_transportation_cost_ship['Ship'].values[rr]>0])]))

# Cost of Variable transport from PET to pre-form plant

D_var_transportation_cost_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_var_trans_cost', usecols='A,C')

print('      ...Variable transportation cost of D')
bwr.create_parameter_filex3(file_destination+'parameter-demand-variable-transportation-cost-truck.txt',
                          ['D-'], pd.concat([pd.DataFrame([[
                                  D_var_transportation_cost_truck['Demand_location'].values[rr],
                                  D_var_transportation_cost_truck['Truck'].values[rr]]
    for rr in range(D_var_transportation_cost_truck.shape[0])
    if D_var_transportation_cost_truck['Truck'].values[rr]>0])]))


D_var_transportation_cost_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_var_trans_cost', usecols='A,D')


bwr.create_parameter_filex3(file_destination+'parameter-demand-variable-transportation-cost-train.txt',
                          ['D-'], pd.concat([pd.DataFrame([[
                                  D_var_transportation_cost_train['Demand_location'].values[rr],
                                  D_var_transportation_cost_train['Train'].values[rr]]
    for rr in range(D_var_transportation_cost_train.shape[0])
    if D_var_transportation_cost_train['Train'].values[rr]>0])]))

#D_var_transportation_cost_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dem_var_trans_cost', usecols='A,E')
#
#
#bwr.create_parameter_filex3(file_destination+'parameter-demand-variable-transportation-cost-ship.txt',
#                          ['D-'], pd.concat([pd.DataFrame([[
#                                  D_var_transportation_cost_ship['Demand_location'].values[rr],
#                                  D_var_transportation_cost_ship['Ship'].values[rr]]
#    for rr in range(D_var_transportation_cost_ship.shape[0])
#    if D_var_transportation_cost_ship['Ship'].values[rr]>0])]))

# Distance Plant D to Demand - TRUCK

print('   ...Distance Plant D to Plant Demand')
dist_plantD_truck =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Truck', usecols='A:Z')

bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-Demand-truck.txt',
                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
                                  dist_plantD_truck['Location'].values[rr],
                                  dist_plantD_truck.columns[cc],
                                  dist_plantD_truck.values[rr,cc]]
    for rr in range(dist_plantD_truck.shape[0])
    for cc in range(1,dist_plantD_truck.shape[1])
    if dist_plantD_truck.values[rr,cc]>0])]))

# Distance Plant D to Demand - TRAIN

print('   ...Distance Plant D to Plant Demand')
dist_plantD_train =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Train', usecols='A:Z')

bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-Demand-train.txt',
                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
                                  dist_plantD_train['Location'].values[rr],
                                  dist_plantD_train.columns[cc],
                                  dist_plantD_train.values[rr,cc]]
    for rr in range(dist_plantD_train.shape[0])
    for cc in range(1,dist_plantD_train.shape[1])
    if dist_plantD_train.values[rr,cc]>0])]))

# Distance Plant D to Plant Demand - SHIP

#print('   ...Distance Plant D to Plant Demand')
#dist_plantD_ship =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='Dist_Pd_to_D_Ship', usecols='A:Z')
#
#bwr.create_parameter_filex3(file_destination+'parameter-distance-plantD-Demand-ship.txt',
#                            ['Pd-','D-'],pd.concat([pd.DataFrame([[
#                                  dist_plantD_ship['Location'].values[rr],
#                                  dist_plantD_ship.columns[cc],
#                                  dist_plantD_ship.values[rr,cc]]
#    for rr in range(dist_plantD_ship.shape[0])
#    for cc in range(1,dist_plantD_ship.shape[1])
#    if dist_plantD_ship.values[rr,cc]>0])]))


#%% EMISSIONS

##%%
print('   ...transport emissions')
transport_emissionsW = pd.read_excel(file_location+file_name, skiprows=1, sheet_name='emi_transp', usecols='A:D')
bwr.create_parameter_filex3(file_destination+'parameter-emissions-transport.txt',
                            ['T-'],pd.concat([pd.DataFrame([[
                                  transport_emissionsW['Transport'].values[rr],
                                  round(transport_emissionsW['Value'].values[rr],6)]
    for rr in range(transport_emissionsW.shape[0])
    if transport_emissionsW['Value'].values[rr]>0])]))

#print('   ...transport emissions')
#transport_emissionsSB = pd.read_excel(file_location+file_name, skiprows=1, sheet_name='trans_emi_R_to_Pa', usecols='A,E:G')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-transport-RM2.txt',
#                            ['R-','T-'],pd.concat([pd.DataFrame([[
#                                  transport_emissionsSB['Country'].values[rr],
#                                  transport_emissionsSB.columns[cc],
#                                  round(transport_emissionsSB.values[rr,cc],2)]
#    for rr in range(transport_emissionsSB.shape[0])
#    for cc in range(1,transport_emissionsSB.shape[1])])]))
##    if transport_emissionsSB.values[rr,cc]>0])]))
#
#print('   ...transport emissions')
#transport_emissionsM = pd.read_excel(file_location+file_name, skiprows=1, sheet_name='trans_emi_R_to_Pa', usecols='A,H:J')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-transport-RM3.txt',
#                            ['R-','T-'],pd.concat([pd.DataFrame([[
#                                  transport_emissionsM['Country'].values[rr],
#                                  transport_emissionsM.columns[cc],
#                                  round(transport_emissionsM.values[rr,cc],2)]
#    for rr in range(transport_emissionsM.shape[0])
#    for cc in range(1,transport_emissionsM.shape[1])])]))
##    if transport_emissionsM.values[rr,cc]>0])]))

##Emissions transportation product A to plant B
#print('   ..Product A transportation emissions')
#productA_transp_emi =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='trans_emi_Pa_to_Pb', usecols='A,C:U')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-transportation-productA.txt',
#                          ['Pb-','T-'], pd.concat([pd.DataFrame([[
#                                  productA_transp_emi['Pb_location'].values[rr],
#                                  productA_transp_emi.columns[cc],
#                                  round(productA_transp_emi.values[rr,cc],2)]
#    for rr in range(productA_transp_emi.shape[0])
#    for cc in range(2,productA_transp_emi.shape[1])
#    if productA_transp_emi.values[rr,cc]>0])]))
#
#
##Emissions transportation product B to plant C
#print('   ..Product B transportation emissions')
#productB_transp_emi =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='trans_emi_Pb_to_Pc', usecols='A,C:U')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-transportation-productB.txt',
#                          ['Pc-','T-'], pd.concat([pd.DataFrame([[
#                                  productB_transp_emi['Pc_location'].values[rr],
#                                  productB_transp_emi.columns[cc],
#                                  round(productB_transp_emi.values[rr,cc],2)]
#    for rr in range(productB_transp_emi.shape[0])
#    for cc in range(2,productB_transp_emi.shape[1])
#    if productB_transp_emi.values[rr,cc]>0])]))
#
##Emissions transportation product C to plant D
#print('   ..Product C transportation emissions')
#productC_transp_emi =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='trans_emi_Pc_to_Pd', usecols='A,C:U')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-transportation-productC.txt',
#                          ['Pd-','T-'], pd.concat([pd.DataFrame([[
#                                  productC_transp_emi['Pd_location'].values[rr],
#                                  productC_transp_emi.columns[cc],
#                                  round(productC_transp_emi.values[rr,cc],2)]
#    for rr in range(productC_transp_emi.shape[0])
#    for cc in range(2,productC_transp_emi.shape[1])
#    if productC_transp_emi.values[rr,cc]>0])]))

# Emissions of the process

#plantA_emissions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantA_emi', usecols='A:U')
#print('      ...Plant A emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantA.txt',
#                          ['Pa-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantA_emissions['plantA_ID'].values[rr],
#                                  plantA_emissions.columns[cc],
#                                  round(plantA_emissions.values[rr,cc],2)]
#    for rr in range(plantA_emissions.shape[0])
#    for cc in range(1,plantA_emissions.shape[1])
#    if plantA_emissions.values[rr,cc]>0])]))
#
#plantB_emissions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantB_emi', usecols='A:U')
#print('      ...Plant B emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantB.txt',
#                          ['Pb-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantB_emissions['plantB_ID'].values[rr],
#                                  plantB_emissions.columns[cc],
#                                  round(plantB_emissions.values[rr,cc],2)]
#    for rr in range(plantB_emissions.shape[0])
#    for cc in range(1,plantB_emissions.shape[1])
#    if plantB_emissions.values[rr,cc]>0])]))
#
#plantC_emissions =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantC_emi', usecols='A:U')
#print('      ...Plant C emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantC.txt',
#                          ['Pc-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantC_emissions['plantC_ID'].values[rr],
#                                  plantC_emissions.columns[cc],
#                                  round(plantC_emissions.values[rr,cc],2)]
#    for rr in range(plantC_emissions.shape[0])
#    for cc in range(1,plantC_emissions.shape[1])
#    if plantC_emissions.values[rr,cc]>0])]))

# Plant D emissions from Wheat
#
#plantD_emissions30 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_30', usecols='A:B')
#print('      ...Plant D emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-30%-wheat.txt',
#                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantD_emissions30['plantD_ID'].values[rr],
#                                  plantD_emissions30.columns[cc],
#                                  round(plantD_emissions30.values[rr,cc],2)]
#    for rr in range(plantD_emissions30.shape[0])
#    for cc in range(1,plantD_emissions30.shape[1])
#    if plantD_emissions30.values[rr,cc]>0])]))
#
#plantD_emissions100 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_100', usecols='A:B')
#print('      ...Plant D emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-100%-wheat.txt',
#                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantD_emissions100['plantD_ID'].values[rr],
#                                  plantD_emissions100.columns[cc],
#                                  round(plantD_emissions100.values[rr,cc],2)]
#    for rr in range(plantD_emissions100.shape[0])
#    for cc in range(1,plantD_emissions100.shape[1])
#    if plantD_emissions100.values[rr,cc]>0])]))

## Plant D emissions from Maize
#
#plantD_emissions30 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_30', usecols='A,D')
#print('      ...Plant D emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-30%-maize.txt',
#                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantD_emissions30['plantD_ID'].values[rr],
#                                  plantD_emissions30.columns[cc],
#                                  round(plantD_emissions30.values[rr,cc],2)]
#    for rr in range(plantD_emissions30.shape[0])
#    for cc in range(1,plantD_emissions30.shape[1])
#    if plantD_emissions30.values[rr,cc]>0])]))
#
#plantD_emissions100 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_100', usecols='A,D')
#print('      ...Plant D emissions')
#bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-100%-maize.txt',
#                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
#                                  plantD_emissions100['plantD_ID'].values[rr],
#                                  plantD_emissions100.columns[cc],
#                                  round(plantD_emissions100.values[rr,cc],2)]
#    for rr in range(plantD_emissions100.shape[0])
#    for cc in range(1,plantD_emissions100.shape[1])
#    if plantD_emissions100.values[rr,cc]>0])]))

# Plant D emissions from Sugar Beet

plantD_emissions30 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_30', usecols='A,C')
print('      ...Plant D emissions')
bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-30%-sugB.txt',
                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
                                  plantD_emissions30['plantD_ID'].values[rr],
                                  plantD_emissions30.columns[cc],
                                  round(plantD_emissions30.values[rr,cc],2)]
    for rr in range(plantD_emissions30.shape[0])
    for cc in range(1,plantD_emissions30.shape[1])
    if plantD_emissions30.values[rr,cc]>0])]))

plantD_emissions100 =  pd.read_excel(file_location+file_name, skiprows=1, sheet_name='plantD_emi_100', usecols='A,C')
print('      ...Plant D emissions')
bwr.create_parameter_filex3(file_destination+'parameter-emissions-plantD-100%-sugB.txt',
                          ['Pd-','RM-'], pd.concat([pd.DataFrame([[
                                  plantD_emissions100['plantD_ID'].values[rr],
                                  plantD_emissions100.columns[cc],
                                  round(plantD_emissions100.values[rr,cc],2)]
    for rr in range(plantD_emissions100.shape[0])
    for cc in range(1,plantD_emissions100.shape[1])
    if plantD_emissions100.values[rr,cc]>0])]))