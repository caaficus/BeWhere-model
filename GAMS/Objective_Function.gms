* ==============================================================================
*   - OBJECTIVE FUNCTION -
* ==============================================================================


*--------------------------------- PROFITS ----------------------------------
Profits..
         PROFIT =E=

*                       SUM((Pd), CostProductD(Pd))

                      SUM((Pa),biomassSupplyCost(Pa)) + SUM((Pa), TransportCostBiomass(Pa))

                 +
                      SUM((Pa), PlantACapex(Pa)) + SUM((Pa), PlantAOpex(Pa))

*                 +    SUM((PRD,Pa),CostProductA(PRD,Pa))
                 - SUM((Pa),costByproductA(Pa))

                 +    SUM((RM,Pa), TransportCostProductA(RM,Pa))
* + SUM((Pa),TransportCostByproductA(Pa))

                 +
                      SUM((Pb), PlantBCapex(Pb)) + SUM((Pb), PlantBOpex(Pb))
*                 + SUM((Pb),CostProductB(Pb))

                 +    SUM((Pb), TransportCostProductB(Pb))

                 +
                      SUM((Pc), PlantCCapex(Pc)) + SUM((Pc), PlantCOpex(Pc))
*                 + SUM((Pc), CostProductC(Pc))

                 +    SUM((Pc), TransportCostProductC(Pc))

                 +
                      SUM((Pd), PlantDCapex(Pd)) + SUM((Pd), PlantDOpex(Pd)) + SUM((Pd), TransportCostProductD(Pd))

                 +
                      SUM((M), TPACapex(M)) + SUM((M), TPAOpex(M))  + SUM((M),PTAtransportCost(M))

                  +       SUM((M),biomassSupplyCostTPA(M)) + SUM((M), TransportCostBiomassTPA(M))

;
*------------------------------- EMISSIONS ALLOWANCE --------------------------------
EnvironmentalCosts..
         ENVCOSTS =E=
                  ( SUM((Pd),emissionsProcessSug(Pd)))*carbonPriceETS
                   +
                  EmissionTransport*carbonPriceETS;


*------------------------------ OBJECTIVE FUNCTION -----------------------------
combine..
         COMBINEEQUATIONS =E= PROFIT + ENVCOSTS;

************************************
FILE cplexOpt/ cplex.opt /;
PUT cplexOpt;
PUT "PARALLELMODE = 1"/;
PUT "threads=2"/;
PUTCLOSE cplexOpt;
************************************
MODEL facilityLocation  /ALL/;
facilityLocation.ITERLIM   =     10000000;
facilityLocation.RESLIM    =     100000;
facilityLocation.NODLIM    =     1000000;
facilityLocation.OPTCA     =     0;
facilityLocation.OPTCR     =     0.01;
facilityLocation.CHEAT     =     0;
facilityLocation.CUTOFF    =     1E+20;
facilityLocation.TRYINT    =     .01;
facilityLocation.OPTFILE   =     1;
facilityLocation.PRIOROPT  =     0;
facilityLocation.workspace =     16000;
facilityLocation.SCALEOPT =      1;
************************************
SOLVE facilityLocation USING MIP MINIMIZING COMBINEEQUATIONS;
