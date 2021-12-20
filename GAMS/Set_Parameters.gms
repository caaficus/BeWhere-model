* ==============================================================================
*   - SETS -
* ==============================================================================
set R region /
$include txt_file_beaver/set-region.txt
/;

set SR subregion /
$include txt_file_beaver/set-subregion.txt
/;

$ontext
set RE region-exports /
$include txt_file_beaver/set-region-exports.txt
/;

set RI region-imports /
$include txt_file_beaver/set-region-imports.txt
/;
$offtext
set C country /
$include txt_file_beaver/set-country.txt
/;

$ontext
set S supply /
$include txt_file_beaver/set-supply.txt
/;
$offtext

set RM raw material /
$include txt_file_beaver/set-raw-material.txt
/;

set T transport /
$include txt_file_beaver/set-transport.txt
/;

$ONTEXT
set I import points /
$include txt_file_beaver/set-import-points.txt
/;

set IRM raw material import points /
$include txt_file_beaver/set-raw-material-import-points.txt
/;
$OFFTEXT

set Pa first process plant /
$include txt_file_beaver/set-plantA.txt
/;

set PRD products /
$include txt_file_beaver/set-products.txt
/;

set Byp byproducts /
$include txt_file_beaver/set-byproducts.txt
/;

set SizePa size Plant A /
$include txt_file_beaver/set-size-plantA.txt
/;

set Pb second process plant /
$include txt_file_beaver/set-plantB.txt
/;

set SizePb size Plant B /
$include txt_file_beaver/set-size-plantB.txt
/;

set Pc third process plant /
$include txt_file_beaver/set-plantC.txt
/;

set SizePc size Plant C /
$include txt_file_beaver/set-size-plantC.txt
/;

set Pd forth process plant D /
$include txt_file_beaver/set-plantD.txt
/;

set SizePd size Plant D /
$include txt_file_beaver/set-size-plantD.txt
/;

set D demand /
$include txt_file_beaver/set-demand.txt
/;

set M PTA plant/
$include txt_file_beaver/set-plantPTA.txt
/;

set SizeM size Plant TPA /
$include txt_file_beaver/set-size-plantTPA.txt
/;

* ==============================================================================
*   - RELATIONS -
* ==============================================================================

set CR(C,R) country-region relation /
$include txt_file_beaver/set-country-region-relation.txt
/;

set RT(R,T) supply-transport relation /
$include txt_file_beaver/set-supply-transport-relation.txt
/;

set PaRM(RM,Pa) plant A-raw material relation /
$include txt_file_beaver/set-plantA-biomass-relation.txt
/;


set NotPaRM(Pa,RM) plant A-raw material No relation /
$include txt_file_beaver/set-plantA-biomass-norelation.txt
/;

$ontext
set IRE(I,R) import-export-region relation /
$include txt_file_beaver/set-import-export-relation.txt
/;

set CI(C,I) country-import points relation /
$include txt_file_beaver/set-country-import-points-relation.txt
/;

set CIRM(C,IRM) country-raw material import points relation /
$include txt_file_beaver/set-country-raw-material-import-points-relation.txt
/;

set RMIP(IRM,RM) raw material-import points relation /
$include txt_file_beaver/set-raw-material-import-points-relation.txt
/;


set PaT(Pa,T) plantA-transport relation /
$include txt_file_beaver/set-plantA-transport-relation.txt
/;
$offtext
set SPa(Pa,SizePa) plantA-size relation /
$include txt_file_beaver/set-plantA-size-relation.txt
/;

set RMPRD(RM,PRD) raw material-product relation /
$include txt_file_beaver/set-raw-material-product-relation.txt
/;

set RMB(RM,Byp) raw material-byproduct relation /
$include txt_file_beaver/set-raw-material-byproduct-relation.txt
/;

set BypT(Byp,T)  byproduct-transportation relation /
$include txt_file_beaver/set-byproduct-transportation-relation.txt
/;


set SPb(Pb,SizePb) plantB-size relation /
$include txt_file_beaver/set-plantB-size-relation.txt
/;

set PbC(Pb,C)   plantB-country relation /
$include txt_file_beaver/set-plantB-country-relation.txt
/;

set PcC(Pc,C)   plantC-country relation /
$include txt_file_beaver/set-plantC-country-relation.txt
/;


set SPc(Pc,SizePc) plantC-size relation /
$include txt_file_beaver/set-plantC-size-relation.txt
/;

set PdC(Pd,C)   plantD-country relation /
$include txt_file_beaver/set-plantD-country-relation.txt
/;


set SPd(Pd,SizePd) plantD-size relation /
$include txt_file_beaver/set-plantD-size-relation.txt
/;

set SM(M,SizeM) plantTPA-size relation /
$include txt_file_beaver/set-plantTPA-size-relation.txt
/;

set MC(M,C)   plantTPA-country relation /
$include txt_file_beaver/set-plantTPA-country-relation.txt
/;



* ==============================================================================
*   - PARAMETERS -
* ==============================================================================
*
******   Resources  *******
*

parameter   BiomassCost(SR,RM)/
$include txt_file_beaver/parameter-biomass-cost.txt
/;

parameter   BiomassCostTPA(SR)/
$include txt_file_beaver/parameter-biomass-cost-TPA.txt
/;

parameter bioAvailable(SR,RM)/
$include txt_file_beaver/parameter-biomass-availability.txt
/;

parameter bioAvailableTPA(SR)/
$include txt_file_beaver/parameter-biomass-availability-TPA.txt
/;

$ontext
parameter maxBiomImport(R,RM)/
$include txt_file_beaver/parameter-biomass-imports.txt
/;

parameter maxBiomExport(R,RM)/
$include txt_file_beaver/parameter-biomass-exports.txt
/;
$offtext
parameter FixCostBiomassTruck(RM,SR)/
$include txt_file_beaver/parameter-biomass-fixed-transportation-cost-truck.txt
/;

parameter FixCostBiomassTrain(RM,SR)/
$include txt_file_beaver/parameter-biomass-fixed-transportation-cost-train.txt
/;

parameter FixCostBiomassTruckTPA(SR)/
$include txt_file_beaver/parameter-biomass-fixed-transportation-cost-truck-TPA.txt
/;

parameter FixCostBiomassTrainTPA(SR)/
$include txt_file_beaver/parameter-biomass-fixed-transportation-cost-train-TPA.txt
/;

parameter VarCostBiomassTruck(RM,SR)/
$include txt_file_beaver/parameter-biomass-variable-transportation-cost-truck.txt
/;

parameter VarCostBiomassTrain(RM,SR)/
$include txt_file_beaver/parameter-biomass-variable-transportation-cost-train.txt
/;

parameter VarCostBiomassTruckTPA(SR)/
$include txt_file_beaver/parameter-biomass-variable-transportation-cost-truck-TPA.txt
/;

parameter VarCostBiomassTrainTPA(SR)/
$include txt_file_beaver/parameter-biomass-variable-transportation-cost-train-TPA.txt
/;

parameter DistSupplyPlantATruck(RM,SR,Pa)/
$include txt_file_beaver/parameter-distance-supply-plantA-truck.txt
/;

parameter DistSupplyPlantATrain(RM,SR,Pa)/
$include txt_file_beaver/parameter-distance-supply-plantA-train.txt
/;

parameter DistSupplyPlantATruckTPA(SR,M)/
$include txt_file_beaver/parameter-distance-supply-plantA-truck-TPA.txt
/;

parameter DistSupplyPlantATrainTPA(SR,M)/
$include txt_file_beaver/parameter-distance-supply-plantA-train-TPA.txt
/;

******   Plant A  *******

parameter ProductAPrice(RM,Pa,PRD)/
$include txt_file_beaver/parameter-productA-cost.txt
/;

parameter byproductAPrice(RM,Pa,Byp)/
$include txt_file_beaver/parameter-byproductA-cost.txt
/;

parameter efficiencyPa(RM,PRD)/
$include txt_file_beaver/parameter-plantA-efficiency.txt
/;

parameter yieldBy(RM,Byp)/
$include txt_file_beaver/parameter-plantA-byproduct-efficiency.txt
/;

parameter capacityPa(Pa)/
$include txt_file_beaver/parameter-plantA-capacity.txt
/;

parameter capacityPaPR(Pa)/
$include txt_file_beaver/parameter-plantA-capacity-prospective.txt
/;

parameter CapitalCostPlantA(RM,Pa,SizePa)/
$include txt_file_beaver/parameter-plantA-capex.txt
/;

parameter FixOpexPlantA(RM,Pa,SizePa)/
$include txt_file_beaver/parameter-plantA-fixed-opex.txt
/;

parameter VarOpexPlantA(RM,Pa,SizePa)/
$include txt_file_beaver/parameter-plantA-variable-opex.txt
/;

parameter FixCostProductATruck(Pa)/
$include txt_file_beaver/parameter-productA-fixed-transportation-cost-truck.txt
/;

parameter FixCostProductATrain(Pa)/
$include txt_file_beaver/parameter-productA-fixed-transportation-cost-train.txt
/;


parameter VarCostProductATruck(Pa)/
$include txt_file_beaver/parameter-productA-variable-transportation-cost-truck.txt
/;

parameter VarCostProductATrain(Pa)/
$include txt_file_beaver/parameter-productA-variable-transportation-cost-train.txt
/;


parameter DistSupplyPlantBTruck(Pa,Pb)/
$include txt_file_beaver/parameter-distance-plantA-plantB-truck.txt
/;

parameter DistSupplyPlantBTrain(Pa,Pb)/
$include txt_file_beaver/parameter-distance-plantA-plantB-train.txt
/;


******   Plant B  *******

parameter   ProductBPrice(Pb)/
$include txt_file_beaver/parameter-productB-cost.txt
/;

parameter capacityPb(Pb)/
$include txt_file_beaver/parameter-plantB-capacity.txt
/;

parameter efficiencyPb(Pb)/
$include txt_file_beaver/parameter-plantB-efficiency.txt
/;

parameter CapitalCostPlantB(Pb,C,SizePb)/
$include txt_file_beaver/parameter-plantB-capex.txt
/;

parameter FixOpexPlantB(Pb,C,SizePb)/
$include txt_file_beaver/parameter-plantB-fixed-opex.txt
/;

parameter VarOpexPlantB(Pb,C,SizePb)/
$include txt_file_beaver/parameter-plantB-variable-opex.txt
/;

parameter FixCostProductBTruck(Pb)/
$include txt_file_beaver/parameter-productB-fixed-transportation-cost-truck.txt
/;

parameter FixCostProductBTrain(Pb)/
$include txt_file_beaver/parameter-productB-fixed-transportation-cost-train.txt
/;

parameter VarCostProductBTruck(Pb)/
$include txt_file_beaver/parameter-productB-variable-transportation-cost-truck.txt
/;

parameter VarCostProductBTrain(Pb)/
$include txt_file_beaver/parameter-productB-variable-transportation-cost-train.txt
/;


parameter DistSupplyPlantCTruck(Pb,Pc)/
$include txt_file_beaver/parameter-distance-plantB-plantC-truck.txt
/;

parameter DistSupplyPlantCTrain(Pb,Pc)/
$include txt_file_beaver/parameter-distance-plantB-plantC-train.txt
/;


******   Plant C  *******

parameter   ProductCPriceEG(Pc)/
$include txt_file_beaver/parameter-productC-cost-EG.txt
/;

parameter capacityPc(Pc)/
$include txt_file_beaver/parameter-plantC-capacity.txt
/;

parameter efficiencyPc(Pc)/
$include txt_file_beaver/parameter-plantC-efficiency-EG.txt
/;

parameter CapitalCostPlantc(Pc,C,SizePc)/
$include txt_file_beaver/parameter-plantC-capex.txt
/;

parameter FixOpexPlantC(Pc,C,SizePc)/
$include txt_file_beaver/parameter-plantC-fixed-opex.txt
/;

parameter VarOpexPlantC(Pc,C,SizePc)/
$include txt_file_beaver/parameter-plantC-variable-opex.txt
/;

parameter FixCostProductCTruck(Pc)/
$include txt_file_beaver/parameter-productC-fixed-transportation-cost-truck.txt
/;

parameter FixCostProductCTrain(Pc)/
$include txt_file_beaver/parameter-productC-fixed-transportation-cost-train.txt
/;


parameter VarCostProductCTruck(Pc)/
$include txt_file_beaver/parameter-productC-variable-transportation-cost-truck.txt
/;

parameter VarCostProductCTrain(Pc)/
$include txt_file_beaver/parameter-productC-variable-transportation-cost-train.txt
/;


parameter DistSupplyPlantDTruck(Pc,Pd)/
$include txt_file_beaver/parameter-distance-plantC-plantD-truck.txt
/;

parameter DistSupplyPlantDTrain(Pc,Pd)/
$include txt_file_beaver/parameter-distance-plantC-plantD-train.txt
/;


******   Plant D  *******

parameter   ProductDPrice(Pd)/
$include txt_file_beaver/parameter-productD-cost.txt
/;

parameter capacityPd(Pd)/
$include txt_file_beaver/parameter-plantD-capacity.txt
/;

parameter efficiencyPd(Pd)/
$include txt_file_beaver/parameter-plantD-efficiency.txt
/;

parameter CapitalCostPlantD(Pd,C,SizePd)/
$include txt_file_beaver/parameter-plantD-capex.txt
/;

parameter FixOpexPlantD(Pd,C,SizePd)/
$include txt_file_beaver/parameter-plantD-fixed-opex.txt
/;

parameter VarOpexPlantD(Pd,C,SizePd)/
$include txt_file_beaver/parameter-plantD-variable-opex.txt
/;

parameter FixCostProductDTruck(Pd)/
$include txt_file_beaver/parameter-productD-fixed-transportation-cost-truck.txt
/;

parameter VarCostProductDTruck(Pd)/
$include txt_file_beaver/parameter-productD-variable-transportation-cost-truck.txt
/;

parameter FixCostProductDTrain(Pd)/
$include txt_file_beaver/parameter-productD-fixed-transportation-cost-train.txt
/;

parameter VarCostProductDTrain(Pd)/
$include txt_file_beaver/parameter-productD-variable-transportation-cost-train.txt
/;


parameter DistSupplyDemandTruck(Pd,D)/
$include txt_file_beaver/parameter-distance-plantD-demand-truck.txt
/;

parameter DistSupplyDemandTrain(Pd,D)/
$include txt_file_beaver/parameter-distance-plantD-demand-train.txt
/;



****** Plant TPA******

parameter   PTAprice(M)/
$include txt_file_beaver/parameter-PTA-cost.txt
/;

parameter   CapacityM(M)/
$include txt_file_beaver/parameter-capacity-PTA.txt
/;

parameter CapitalCostTPA(M,C,SizeM)/
$include txt_file_beaver/parameter-plantTPA-capex.txt
/;

parameter FixOpexTPA(M,C,SizeM)/
$include txt_file_beaver/parameter-plantTPA-fixed-opex.txt
/;

parameter VarOpexTPA(M,C,SizeM)/
$include txt_file_beaver/parameter-plantTPA-variable-opex.txt
/;

parameter FixCostTPATruck(M)/
$include txt_file_beaver/parameter-TPA-fixed-transportation-cost-truck.txt
/;

parameter VarCostTPATruck(M)/
$include txt_file_beaver/parameter-TPA-variable-transportation-cost-truck.txt
/;

parameter FixCostTPATrain(M)/
$include txt_file_beaver/parameter-TPA-fixed-transportation-cost-train.txt
/;


parameter VarCostTPATrain(M)/
$include txt_file_beaver/parameter-TPA-variable-transportation-cost-train.txt
/;


parameter DistSupplyPDTruck(M,Pd)/
$include txt_file_beaver/parameter-distance-plantTPA-plantD-truck.txt
/;

parameter DistSupplyPDTrain(M,Pd)/
$include txt_file_beaver/parameter-distance-plantTPA-plantD-train.txt
/;



******** Other Parameters*****

parameter capacityD(D)/
$include txt_file_beaver/parameter-demand.txt
/;
$ontext
parameter fossilPrice(D)/
$include txt_file_beaver/parameter-fossil-cost.txt
/;
$offtext


******** EMISSIONS*******
$ontext
parameter transEmiPa2Pb(Pb,T)/
$include txt_file_beaver/parameter-emissions-transportation-productA.txt
/;

parameter transEmiPb2Pc(Pc,T)/
$include txt_file_beaver/parameter-emissions-transportation-productB.txt
/;

parameter transEmiPc2Pd(Pd,T)/
$include txt_file_beaver/parameter-emissions-transportation-productC.txt
/;


parameter transEmi(T)/
$include txt_file_beaver/parameter-emissions-transport.txt
/;
$offtext
$ontext
parameter transEmiRM2(R,T)/
$include txt_file_beaver/parameter-emissions-transport-RM2.txt
/;

parameter transEmiRM3(R,T)/
$include txt_file_beaver/parameter-emissions-transport-RM3.txt
/;

parameter plantAemi(Pa,RM)/
$include txt_file_beaver/parameter-emissions-plantA.txt
/;

parameter plantBemi(Pb,RM)/
$include txt_file_beaver/parameter-emissions-plantB.txt
/;

parameter plantCemi(Pc,RM)/
$include txt_file_beaver/parameter-emissions-plantC.txt
/;
$offtext

$ontext
parameter plantDemiW30(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-30%-wheat.txt
/;

parameter plantDemiW100(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-100%-wheat.txt
/;


parameter plantDemiM30(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-30%-maize.txt
/;

parameter plantDemiM100(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-100%-maize.txt
/;
$offtext
parameter plantDemiSug30(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-30%-sugB.txt
/;

parameter plantDemiSug100(Pd,RM)/
$include txt_file_beaver/parameter-emissions-plantD-100%-sugB.txt
/;


*/// SCALARS ////*-----------

Scalar distByp "Transportation distance byproducts" /100/;
*Scalar capacityD "Demand for PET in Europe (ton/year)" /4000000/
Scalar transEmiTruck "Emissions from truck - diesel - ton CO2/tkm" /0.000164/;
Scalar transEmiTrain "Emissions from train - ton CO2/tkm" /0.0000578/;
Scalar transEmiShip "Emissions from ship - ton CO2/tkm" /0.0000476/;
Scalar fossilEmi "Emissions of PET production from fossil fuels - ton CO2/ton PET" /2.99/;
Scalar distFossil "Distance fossil-PET to demand - Km" /500/;
Scalar numberPlantA "Number of plants A" /34/;
Scalar numberPlantB "Number of plants B" /21/;
Scalar numberPlantC "Number of plants C" /9/;
Scalar numberPlantD "Number of plants D" /9/;
Scalar numberPlantM "Number of plants TPA" /6/;
Scalar DistPTAtransp "Distance from the PTA location to plant D" /200/;
Scalar PTAemission "Emission from PTA production process - tons CO2/tons PTA"/1.2/;
Scalar WPc "Weight fraction of Ethylene Glycol to produce PET" /0.3/;
Scalar WPTA "Weight fraction of PTa to produce PET"/0.7/;
Scalar carbonTax "Tax on burning fossil fuels" /25/;
Scalar carbonPriceETS "Carbon price based on ETS auction in EUR/ton CO2" /25/;
Scalar TPAyield "Conversion of sugar beet to TPA - ton TPA/ton sugB" /0.23/;
Scalar SelectPET "Factor to select 100% biobased PET" /1/;
Scalar NoSelectPET " Factor for 30%BioPEt" /0/;
