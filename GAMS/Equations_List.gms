* ==============================================================================
*   - EQUATIONS LIST -
* ==============================================================================
equations

*biomassExports(R)                Biomass exports from region RE to region RI
*biomassImport(I)                 Biomass Imports
*importBiomBound(R)                Biomass imports limit
*exportBound(R)                   Limit of biomas export to other regions

supplyCost(Pa)                  biomass supply cost
supplyCostTPA(M)
*supplyBiomassMin(SR,RM)
BiomassTransportCost(Pa)               biomass transportation cost
BiomassTransportCostTPA(M)
InvCostPlantA(Pa)                  Plant A investment cost (CAPEX)
OperatCostPlantA(Pa)               Plant A Operating costs (OPEX)

supplyBiomass(SR,RM)                 biomass availability
supplyBiomassTPA(SR)
*supplyBiomassBOTH(SR)
plantConversion(Pa)                 Ethanol plant efficiency
plantCapacity(RM,Pa)                Plant Capacity
*plantMinCapacity(Pa)             Plant capacity lower bound
plantSelection(SizePa)                      Plant a allocation
*plantArestrict(Pa)                      Number of Plant A
productACost(PRD,Pa)                Product A cost to be supplied tio plant B
productATransportCost(RM,Pa)           Transportation costs of product A
plantABalance(Pa)                   Mass balance Plant A
*supplyBalanceZero(RM,R,Pa)
*plantABalanceZero(RM,Pa,Pb)
byproductConversion(Pa)           By-products conversion in Plant A
byproductACost(Pa)                  cost of byproducts in Plant A
byproductATransportCost(Pa)        Transportation cost of byproducts



plantBcapacity(Pb)                  Plant B capacity
plantBMinCapacity(Pb)               Plant B minimum capacity
plantBConversion(Pb)                Plant B conversion
plantBselection(SizePb)                     Plant B selection
*plantA2plantB(RM,Pa)                   Minimum amount of product A to plant B
InvCostPlantB(Pb)                       CAPEX plant B
OperatCostPlantB(Pb)                OPEX plant B
productBTransportCost(Pb)           Transportation cost of product B to plant C
productBCost(Pb)                    Production cost of product B
plantBBalance(Pb)                   Mass Balance Plant B

plantCcapacity(Pc)                  Plant C capacity
plantCMinCapacity(Pc)               Plant C minimum capacity
plantCConversion(Pc)                Plant C conversion
InvCostPlantC(Pc)                   CAPEX Plant C
OperatCostPlantC(Pc)                OPEX Plant C
productCCost(Pc)                     Production cost product C in plant C
productCTransportCost(Pc)            Transportation cost of product C to plant D
plantCselection(SizePc)                     Plant C selection
plantCBalance(Pc)                   Mass balance plant C

plantDcapacity(Pd)                  Plant D capacity
plantDMinCapacityM(Pd)               Plant C minimum capacity
plantDcapacityPc(Pd)                Min flux plant MEG
plantDCapacityM(Pd)
plantDConversion(Pd)                Plant D conversion
InvCostPlantD(Pd)                   CAPEX Plant D
OperatCostPlantD(Pd)                OPEX Plant D
productDCost(Pd)                     Production cost product D in plant D
productDTransportCost(Pd)            Transportation cost of product D to Demand D
plantDselection(SizePd)                     Plant D selection
plantDBalance(Pd)                   Mass balance plant D
*constraint(Pd)


InvCostTPA(M)                       CAPEX plant TPA
OperatCostTPA(M)                    OPEX Plant TPA



costPTA(M)                          Purchasing cost PTA in location M
transportPTAcost(M)                 Transportation costs of PTA to location Pd
plantMselection                     Selection of Plant M

supplyDemand(D)                     Amount of product C that is supplied to Demand D
supplyDemandMin(D)                  Minimum demand of product C
*demandSelection                     Demand selection
*demandBalance                    Demand Balance
*fossilCost                          Fossil-based product costs
*fossilBasedNeed(D)                  Constraint Demand of fossil based
*transFossil                      Transportation emissions of fossil-PET

biomTransEmi(SR,RM)                     Biomass transportation emissions
biomTransEmiTPA(SR)
transProdA(Pa)                      Product A transportation emissions
*transBypA(Pa)                       Byproducts of Plant A Transportation Emissions
transProdB(Pb)                      Product B transportation emissions
transProdC(Pc)                      Product C transportation emissions
*transProdD(Pd)                      Product C transportation emissions
transPTA(M)                         Transportation emissions from PTA


fossilTPA(M)


locationPTA(M)                          Location of PTA plant
plantConversionTPA(M)
locationPTA(M)
locationPTAmax(M)
balancePTA(M)


transEmi                            Process Emissions

*processEmissionsW(Pd)                 Emissions from the process
*processEmissionsM
processEmissionsSug(Pd)
*EmissionFossil

Profits
EnvironmentalCosts
combine

;
