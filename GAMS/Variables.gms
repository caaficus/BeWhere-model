* ==============================================================================
*   - VARIABLES -
* ==============================================================================
binary variable
          UP(Pa,SizePa)                      binary variable for the plant a
          UPb(Pb,SizePb)                        binary variable for plant B
          UPc(Pc,SizePc)                        binary variable for plant C
          UPd(Pd,SizePd)                        binary variable for plant D
          UM(M,SizeM)                                 binary variable for plant TPA
*          UPd(D)                         binary variable for Demand
positive variables
         BSPa(SR,RM,Pa)                    amount of biomass from supply s to plant a
         BSM(SR,M)
         biomassSupplyCost(Pa)           cost of the biomass at the each plant a
         biomassSupplyCostTPA(M)
         TransportCostBiomass(Pa)          cost of biomass transportation
         TransportCostBiomassTPA(M)
         ethanolProd(Pa)                   Ethanol plant efficiency
         PlantACapex(Pa)                   Plant A CAPEX
         PlantAOpex(Pa)                    Plant A OPEX
         CostProductA(PRD,Pa)                      Production cost product A
         TransportCostProductA(RM,Pa)         Transportation cost product A
         byproductProd(Pa)              Conversion of byproduct in Plant A
         costByproductA(Pa)                Cost of byproducts in the Plant A
         TransportCostByproductA(Pa)      Transportation cost byproducts

         PlantBCapex                       Plant B CAPEX
         PlantBOpex(Pb)                    Plant B OPEX
         XPaPb(Pa,Pb)                    Amount of product A going to plant B
         MEGprod(Pb)                       Amount product B (MEG) produced
         CostProductB(Pb)                      Production cost of product B
         XPbPc(Pb,Pc)                    Amount of product B gpoing to Plant C
         TransportCostProductB(Pb)         Transportation cost of product B
*
         XPcPd(Pc,Pd)                      Amount of product C that is demanded plant D
         EGprod(Pc)                       Production of product C (PET)
         PlantCCapex(Pc)                   CAPEX Plant C
         PlantCOpex(Pc)                    OPEX Plant C
         CostProductC(Pc)                   Production cost product C in plant C
         TransportCostProductC(Pc)          Transportation costs of product C

         XPdD(Pd,D)                      Amount of product D that is demanded in D
         PETprod(Pd)                       Production of product D (PET)
         PlantDCapex(Pd)                   CAPEX Plant D
         PlantDOpex(Pd)                    OPEX Plant D
         CostProductD(Pd)                   Production cost product D in plant D
         TransportCostProductD(Pd)          Transportation costs of product D to pre-form PET

         TPACapex(M)                        CAPEX Plant TPA
         TPAOpex(M)                         OPEX Plant TPA


         PTAcost(M)                        Purchase cost of PTA in location M
         PTAtransportCost(M)               Transportation costs of TPA to plant D
         XMPd(M,Pd)                        Amount of PTA that is deliver to Pd
         TPAProd(M)
*         totalDemand(D)                    Total Demand balance (bioPET + fossil)
         XF(D)                             Amount of fossil-based product to supply Demand D
*         costFossil                        Fossil-based product costs
*         fossilTrans                    Transportation emissions of fossil_PEt

         transEmiBio(SR,RM)                    Biomass transportation emissions
         transEmiBioTPA(SR)
         transProdAemi(Pa)                 Product A transportation emissions
         transBypAemi(Pa)                  Byproduct of Plant A transportation emissions
         transProdBemi(Pb)                 Product B transportation emissions
         transProdCemi(Pc)                 Product C transportation emissions
         transProdDemi(Pd)                 Product D transportation emissions
         transpEmiPTA(M)                   Transportation emissions of PTA

*         emissionsProcessW(Pd)               Emissions from the process
*         emissionsProcessM
         emissionsProcessSug(Pd)
         EmissionTransport

*         FossilEmissions
*----- Trades

*         exportBiomassRegions(R,I,RM)    Amount of biomass that can be exported from one region to another
*         extBiomImportPoint(R,I,RM)             Amount of biomass imported from other country to harbor
*         extBiomImportPlant(I,Pa,SizePa,RM)    Amount of biomass imported from harbor to Plant A

variables
         PROFIT
         ENVCOSTS
         COMBINEEQUATIONS

;
