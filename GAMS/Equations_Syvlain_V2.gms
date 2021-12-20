* ==============================================================================
*   - EQUATIONS -
* ==============================================================================


*-------------------------------------------------------------------------------
*-----------------------   COSTS    --------------------------------------------
*-------------------------------------------------------------------------------
*
*----------Biomass cost-----
******* Supply to Plant A
supplyCost(Pa)..
         biomassSupplyCost(Pa) =E= SUM((SR,RM)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),
                 BSPa(SR,RM,Pa)*BiomassCost(SR,RM));


**////// 100% bioPET

******* Supply to Plant TPA
supplyCostTPA(M)..
         biomassSupplyCostTPA(M) =E= SUM((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0),
                 BSM(SR,M)*BiomassCostTPA(SR))*selectPET;




*---------Biomass Transporation Cost-----
******* Transportation to Plant A
BiomassTransportCost(Pa)..
         TransportCostBiomass(Pa) =E=
*---- Fixed Costs
                 SUM ((SR,RM)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),
                 BSPa(SR,RM,Pa)*(FixCostBiomassTruck(RM,SR)*DistSupplyPlantATruck(RM,SR,Pa)
                         + FixCostBiomassTrain(RM,SR)*DistSupplyPlantATrain(RM,SR,Pa)))
            +
*-----Variable Costs
                 SUM((SR,RM)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),
                 BSPa(SR,RM,Pa)*(VarCostBiomassTruck(RM,SR)*DistSupplyPlantATruck(RM,SR,Pa)
                         + VarCostBiomassTrain(RM,SR)*DistSupplyPlantATrain(RM,SR,Pa)));

***///// 100% BioPEt


******* Transportation to Plant TPA
BiomassTransportCostTPA(M)..
         TransportCostBiomassTPA(M) =E=
*---- Fixed Costs
                 SUM ((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0),
                 BSM(SR,M)*(FixCostBiomassTruckTPA(SR)*DistSupplyPlantATruckTPA(SR,M)
                         + FixCostBiomassTrainTPA(SR)*DistSupplyPlantATrainTPA(SR,M)))*selectPET
            +
*-----Variable Costs
                 SUM((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0),
                 BSM(SR,M)*(VarCostBiomassTruckTPA(SR)*DistSupplyPlantATruckTPA(SR,M)
                         + VarCostBiomassTrainTPA(SR)*DistSupplyPlantATrainTPA(SR,M)))*selectPET;

*-------------------------------------PLANT A-----------------------------------
*--------Plant A cost------------
InvCostPlantA(Pa)..
         PlantACapex(Pa) =E= SUM((RM,SizePa)$(SPa(Pa,SizePa) and PaRM(RM,Pa)),
                 CapitalCostPlantA(RM,Pa,SizePa)*UP(Pa,SizePa));

OperatCostPlantA(Pa)..
         PlantAOpex(Pa) =E=
* Fixed Operating Costs
                 SUM((RM,SizePa)$(SPa(Pa,SizePa) and PaRM(RM,Pa)),
                 FixOpexPlantA(RM,Pa,SizePa)*UP(Pa,SizePa))
         +
* Variable Operating Costs
                 SUM((RM,SizePa)$(SPa(Pa,SizePa) and PaRM(RM,Pa)),
                 VarOpexPlantA(RM,Pa,SizePa)*UP(Pa,SizePa));

*----------Product A cost (supplied to plant B)-----
productACost(PRD,Pa)..
         CostProductA(PRD,Pa) =E= SUM((RM,Pb)$(RMPRD(RM,PRD) and PaRM(RM,Pa)),
                 XPaPb(Pa,Pb)*ProductAPrice(RM,Pa,PRD));

byproductACost(Pa)..
         costByproductA(Pa) =E= SUM((RM,Byp)$(RMB(RM,Byp) and PaRM(RM,Pa) and distByp gt 0),
                 byproductProd(Pa)*byproductAPrice(RM,Pa,Byp));


*---------Plant A product (Ethanol) Transportation Cost-----

productATransportCost(RM,Pa)..
         TransportCostProductA(RM,Pa) =E=
*---- Fixed Costs
                 SUM ((Pb)$(PaRM(RM,Pa)),
                 XPaPb(Pa,Pb)*(FixCostProductATruck(Pa)*DistSupplyPlantBTruck(Pa,Pb) + FixCostProductATrain(Pa)*DistSupplyPlantBTrain(Pa,Pb)))
            +
*-----Variable Costs
                 SUM((Pb)$(PaRM(RM,Pa)),
                 XPaPb(Pa,Pb)*(VarCostProductATruck(Pa)*DistSupplyPlantBTruck(Pa,Pb) + VarCostProductATrain(Pa)*DistSupplyPlantBTrain(Pa,Pb)));

**----- Plant A by-products Transportation Cost----

byproductATransportCost(Pa)..
         TransportCostByproductA(Pa) =E=
*---- Fixed Costs
                 SUM ((RM)$(PaRM(RM,Pa)),
                 byproductProd(Pa)*FixCostProductATruck(Pa)*distByp)
            +
*-----Variable Costs
                 SUM((RM)$(PaRM(RM,Pa) and distByp gt 0),
                 distByp*byproductProd(Pa)*VarCostProductATruck(Pa));


*-----------------------------PLANT B ------------------------------------------

*--------Plant B cost------------
InvCostPlantB(Pb)..
         PlantBCapex(Pb) =E= SUM((C,SizePb)$(SPb(Pb,SizePb) and PbC(Pb,C)),
                 CapitalCostPlantB(Pb,C,SizePb)*UPb(Pb,SizePb));

OperatCostPlantB(Pb)..
         PlantBOpex(Pb) =E=
* Fixed Operating Costs
                 SUM((C,SizePb)$(SPb(Pb,SizePb) and PbC(Pb,C)),
                         FixOpexPlantB(Pb,C,SizePb)*UPb(Pb,SizePb))
         +
* Variable Operating Costs
                SUM((C,SizePb)$(SPb(Pb,SizePb) and PbC(Pb,C)),
                         VarOpexPlantB(Pb,C,SizePb)*UPb(Pb,SizePb));

*----------Product B cost (supplied to plant C)-----
productBCost(Pb)..
         CostProductB(Pb) =E= SUM((Pc),
                 XPbPc(Pb,Pc)*ProductBPrice(Pb));


*---------Plant B product (MEG) Transportation Cost-----

productBTransportCost(Pb)..
         TransportCostProductB(Pb) =E=
*---- Fixed Costs
                 SUM ((Pc),
                         XPbPc(Pb,Pc)*(FixCostProductBTruck(Pb)*DistSupplyPlantCTruck(Pb,Pc) + FixCostProductBTrain(Pb)*DistSupplyPlantCTrain(Pb,Pc)))
      +
*-----Variable Costs
                 SUM((Pc),
                         XPbPc(Pb,Pc)*(VarCostProductBTruck(Pb)*DistSupplyPlantCTruck(Pb,Pc) + VarCostProductBTrain(Pb)*DistSupplyPlantCTrain(Pb,Pc)));

*-----------------------------PLANT C ------------------------------------------

*--------Plant C cost------------

InvCostPlantC(Pc)..
         PlantCCapex(Pc) =E= SUM((C,SizePc)$(SPc(Pc,SizePc) and PcC(Pc,C)),
                 CapitalCostPlantc(Pc,C,SizePc)*UPc(Pc,SizePc));

OperatCostPlantC(Pc)..
         PlantCOpex(Pc) =E=
* Fixed Operating Costs
                 SUM((C,SizePc)$(SPc(Pc,SizePc) and PcC(Pc,C)),
                         FixOpexPlantC(Pc,C,SizePc)*UPc(Pc,SizePc))
        +
*Variable Operating Costs
                 SUM((C,SizePc)$(SPc(Pc,SizePc) and PcC(Pc,C)),
                         VarOpexPlantC(Pc,C,SizePc)*UPc(Pc,SizePc));

*----------Product C cost (supplied to Plant D)-----
productCCost(Pc)..
         CostProductC(Pc) =E= SUM((Pd),
                  XPcPd(Pc,Pd)*ProductCPriceEG(Pc));


*---------Plant C product (PET) Transportation Cost-----

productCTransportCost(Pc)..
         TransportCostProductC(Pc) =E=
*---- Fixed Costs
                 SUM ((Pd),
                 XPcPd(Pc,Pd)*(FixCostProductCTruck(Pc)*DistSupplyPlantDTruck(Pc,Pd) + FixCostProductCTrain(Pc)*DistSupplyPlantDTrain(Pc,Pd)))
         +
*-----Variable Costs
                 SUM((Pd),
                 XPcPd(Pc,Pd)*(VarCostProductCTruck(Pc)*DistSupplyPlantDTruck(Pc,Pd) + VarCostProductCTrain(Pc)*DistSupplyPlantDTrain(Pc,Pd)));

*------------------------------------------------------------------------------------
*------------------------PLANT D------------------------------------------------------

*--------Plant D cost------------

InvCostPlantD(Pd)..
         PlantDCapex(Pd) =E= SUM((C,SizePd)$(SPd(Pd,SizePd) and PdC(Pd,C)),
                 CapitalCostPlantD(Pd,C,SizePd)*UPd(Pd,SizePd));

OperatCostPlantD(Pd)..
         PlantDOpex(Pd) =E=
* Fixed Operating Costs
                 SUM((C,SizePd)$(SPd(Pd,SizePd) and PdC(Pd,C)),
                         FixOpexPlantD(Pd,C,SizePd)*UPd(Pd,SizePd))
        +
*Variable Operating Costs
                 SUM((C,SizePd)$(SPd(Pd,SizePd) and PdC(Pd,C)),
                         VarOpexPlantD(Pd,C,SizePd)*UPd(Pd,SizePd));

*----------Product D cost (supplied to Demand(D))-----
productDCost(Pd)..
         CostProductD(Pd) =E= SUM((D),
                  XPdD(Pd,D)*ProductDPrice(Pd));


*---------Plant D product (PET) Transportation Cost to PRe-form Plants -----

productDTransportCost(Pd)..
         TransportCostProductD(Pd) =E=
*---- Fixed Costs
                 SUM ((D),
                 XPdD(Pd,D)*(FixCostProductDTruck(Pd)*DistSupplyDemandTruck(Pd,D) + FixCostProductDTrain(Pd)*DistSupplyDemandTrain(Pd,D)))
         +
*-----Variable Costs
                 SUM((D),
                 XPdD(Pd,D)*(VarCostProductDTruck(Pd)*DistSupplyDemandTruck(Pd,D) + VarCostProductDTrain(Pd)*DistSupplyDemandTrain(Pd,D)));


*-----------------------------------------------------------------------------------------------
*---------------------------------PLANT TPA------------------------------------------------------

*------- Plant Costs -----

InvCostTPA(M)..
         TPACapex(M) =E= SUM((C,SizeM)$(SM(M,SizeM) and MC(M,C)),
                 CapitalCostTPA(M,C,SizeM)*UM(M,SizeM));

OperatCostTPA(M)..
         TPAOpex(M) =E=
* Fixed Operating Costs
                 SUM((C,SizeM)$(SM(M,SizeM) and MC(M,C)),
                         FixOpexTPA(M,C,SizeM)*UM(M,SizeM))
        +
*Variable Operating Costs
                 SUM((C,SizeM)$(SM(M,SizeM) and MC(M,C)),
                         VarOpexTPA(M,C,SizeM)*UM(M,SizeM));

**------ TPA Costs ------

costPTA(M)..
         PTAcost(M) =E= SUM((Pd),XMPd(M,Pd)*PTAprice(M));

** ---- Transportation Costs to Plant D

transportPTAcost(M)..
         PTAtransportCost(M) =E=

* --- Fixed Costs
                SUM ((Pd),
                XMPd(M,Pd)*(FixCostTPATruck(M)*DistSupplyPDTruck(M,Pd) + FixCostTPATrain(M)*DistSupplyPDTrain(M,Pd)))
         +
*-----Variable Costs
                SUM((Pd),
                XMPd(M,Pd)*(VarCostTPATruck(M)*DistSupplyPDTruck(M,Pd) + VarCostTPATrain(M)*DistSupplyPDTrain(M,Pd)));

*-----------------------------OTHER COSTS ------------------------------------------
$ontext
**--- Fossil-based PET cost
fossilCost(D)..
         costFossil(D) =E=  XF(D)*fossilPrice(D);
$offtext

*-------------------------------------------------------------------------------
*-----------------------   EMISSIONS    --------------------------------------------
*-------------------------------------------------------------------------------

* ----- Transportation emissions------------------
biomTransEmi(SR,RM)..
         transEmiBio(SR,RM) =E= SUM((Pa)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0 and  bioAvailable(SR,RM) gt 0),
                 BSPa(SR,RM,Pa)*(transEmiTruck*DistSupplyPlantATruck(RM,SR,Pa) + transEmiTrain*DistSupplyPlantATrain(RM,SR,Pa)));


***///// 100% BioPET


biomTransEmiTPA(SR)..
         transEmiBioTPA(SR) =E= SUM((M)$(DistSupplyPlantATruckTPA(SR,M) gt 0 and  bioAvailableTPA(SR) gt 0),
                 BSM(SR,M)*(transEmiTruck*DistSupplyPlantATruckTPA(SR,M) + transEmiTrain*DistSupplyPlantATrainTPA(SR,M)))*selectPET;




transProdA(Pa)..
         transProdAemi(Pa) =E= SUM((Pb),
                 XPaPb(Pa,Pb)*(transEmiTruck*DistSupplyPlantBTruck(Pa,Pb) + transEmiTrain*DistSupplyPlantBTrain(Pa,Pb)));
*transBypA(Pa)..
*         transBypAemi(Pa) =E=  distByp*byproductProd(Pa)*(transEmiTruck);

transProdB(Pb)..
         transProdBemi(Pb) =E= SUM((Pc),
                         XPbPc(Pb,Pc)*(transEmiTruck*DistSupplyPlantCTruck(Pb,Pc) + transEmiTrain*DistSupplyPlantCTrain(Pb,Pc)));

transProdC(Pc)..
         transProdCemi(Pc) =E=  SUM((Pd),
                 XPcPd(Pc,Pd)*(transEmiTruck*DistSupplyPlantDTruck(Pc,Pd) + transEmiTrain*DistSupplyPlantDTrain(Pc,Pd)));
transPTA(M)..
         transpEmiPTA(M) =E= SUM((Pd),XMPd(M,Pd)*(transEmiTruck*DistSupplyPDTruck(M,Pd) + transEmiTrain*DistSupplyPDTrain(M,Pd)));
$ontext
transProdD(Pd)..
         transProdDemi(Pd) =E=  SUM((D),
                 XPdD(Pd,D)*(transEmiTruck*DistSupplyDemandTruck(Pd,D) + transEmiTrain*DistSupplyDemandTrain(Pd,D) + transEmiShip*DistSupplyDemandShip(Pd,D)));
$offtext
*transFossil..
*         fossilTrans =E= SUM((D),XF(D)*distFossil*(transEmiTruck));
transEmi..
         EmissionTransport =E=
         SUM((SR,RM),transEmiBio(SR,RM)) + SUM((Pa), transProdAemi(Pa))

*SUM((Pa), transBypAemi(Pa))
         + SUM((Pb), transProdBemi(Pb))
         +
         SUM((Pc), transProdCemi(Pc))
*+ SUM((Pd), transProdDemi(Pd))
         +
         SUM((M), transpEmiPTA(M))

        + SUM((SR),transEmiBioTPA(SR))
;
*+ SUM((D),fossilTrans(D));

* -------- PROCESS EMISSIONS (LCA) ----------------------
$ontext
processEmissionsW(Pd)..
         emissionsProcessW(Pd) =E=
                 SUM((RM), plantDemiW30(Pd,RM)*PETprod(Pd));

processEmissionsM..
         emissionsProcessM =E=
                 SUM((Pd,RM), plantDemiM30(Pd,RM)*PETprod(Pd));
$offtext
processEmissionsSug(Pd)..
         emissionsProcessSug(Pd) =E=
                 SUM((RM), plantDemiSug100(Pd,RM)*PETprod(Pd));



*                 +
*                 SUM((D),fossilEmi*XF(D));

$ontext
                 SUM((R,Pa)$(PaRM(Pa,RM)), plantAemi(Pa,RM)*BSPa(RM,R,Pa))
                 +
                 SUM((Pa,Pb),plantBemi(Pb,RM)*XPaPb(Pa,Pb))
                 +
                 SUM((Pb,Pc), plantCemi(Pc,RM)*XPbPc(Pb,Pc))
                 +
                 SUM((Pc,Pd), plantDemi(Pd,RM)*XPcPd(Pc,Pd))
                 +
                 SUM((M,Pd),PTAemission*XMPd(M,Pd))
                 +
$offtext

*EmissionFossil..
*                FossilEmissions =E= SUM((D),fossilEmi*XF(D));



*-------------------------------------------------------------------------------
*-----------------------   CONSTRAINTS  ----------------------------------------
*-------------------------------------------------------------------------------
*
*----------Biomass availability-

****** When you have different feedstock (one for MEG and other for TPA)

supplyBiomass(SR,RM)$(bioAvailable(SR,RM) gt 5000)..
         SUM((Pa)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),
                 BSPa(SR,RM,Pa))
         =L=
         bioAvailable(SR,RM);

**///// For TPA when 100% bioPET


supplyBiomassTPA(SR)$(bioAvailableTPA(SR) gt 5000)..
         SUM((M)$(DistSupplyPlantATruckTPA(SR,M) gt 0),
                 BSM(SR,M))*selectPET
         =L=
         bioAvailableTPA(SR)*selectPET;

$ontext
***** When you have the same feedstock for MEG and TPA

supplyBiomassBOTH(SR)$(bioAvailableTPA(SR) gt 5000)..
         SUM((RM,Pa)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),
                 BSPa(SR,RM,Pa))
+
         SUM((M)$(DistSupplyPlantATruckTPA(SR,M) gt 0),
                 BSM(SR,M))
         =L=
         bioAvailableTPA(SR);
$offtext
*----------Biomass Trades-------------

*---------------PLANT A-----------------------------------------------------
*----------Plant A conversion-

plantConversion(Pa)..
         ethanolProd(Pa) =E= SUM((SR,RM,PRD)$(RMPRD(RM,PRD) and PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0 and bioAvailable(SR,RM) gt 0),
                 BSPa(SR,RM,Pa)*efficiencyPa(RM,PRD));
$ontext
plantConversion(RM,PRD,Pa)..
         ethanolProd(RM,PRD,Pa) =E= SUM((R)$(PaRM(Pa,RM) and RMPRD(RM,PRD)),
                 BSPa(RM,R,Pa)*efficiencyPa(RM,PRD));
$offtext
*--------Plant A by-products

byproductConversion(Pa)..
         byproductProd(Pa) =E= SUM((SR,RM,Byp)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0 and bioAvailable(SR,RM) gt 0
                                 ), BSPa(SR,RM,Pa)*yieldBy(RM,Byp));
$ontext
byproductConversion(RM,Byp,Pa)..
         byproductProd(RM,Byp,Pa) =E= SUM((R)$(PaRM(Pa,RM)),
                 BSPa(RM,R,Pa)*yieldBy(RM,Byp));
$offtext

*----------Plant A Capacity-

plantCapacity(RM,Pa)..
         SUM((SR)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0 and bioAvailable(SR,RM) gt 0),
                 BSPa(SR,RM,Pa))
          =L=
         SUM((PRD,SizePa)$(SPa(Pa,SizePa)),capacityPa(Pa)*UP(Pa,SizePa)/efficiencyPa(RM,PRD));



$ontext
plantMinCapacity(Pa)..
         SUM((SR,RM)$(PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0),BSPa(SR,RM,Pa))
         =G=
         SUM((RM,PRD,SizePa)$(SPa(Pa,SizePa)),capacityPa(Pa)*UP(Pa,SizePa)/efficiencyPa(RM,PRD))*0;


plantCapacity(RM,Pa)..
         SUM((R)$(PaRM(Pa,RM)),BSPa(RM,R,Pa)) =L=
         SUM((SizePa)$(SPa(Pa,SizePa)),capacityPa(Pa)*UP(Pa,SizePa));

plantMinCapacity(RM,Pa)..
         SUM((R)$(PaRM(Pa,RM)),BSPa(RM,R,Pa))
         =G=
         SUM((SizePa)$(SPa(Pa,SizePa)),capacityPa(Pa)*UP(Pa,SizePa))*0;
$offtext
*------Mass balance Plant A

plantABalance(Pa)..
         SUM((SR,RM,PRD)$(RMPRD(RM,PRD) and PaRM(RM,Pa) and DistSupplyPlantATruck(RM,SR,Pa) gt 0 and bioAvailable(SR,RM) gt 0)
                 ,BSPa(SR,RM,Pa)*efficiencyPa(RM,PRD))
         =E=
         SUM((Pb),XPaPb(Pa,Pb));
$ontext
plantABalance(RM,Pa)$(PaRM(Pa,RM))..
         SUM((R,PRD)$RMPRD(RM,PRD),BSPa(RM,R,Pa)*efficiencyPa(RM,PRD))
         =E=
         SUM((Pb),XPaPb(Pa,Pb));



supplyBalanceZero(RM,R,Pa)$(NotPaRM(Pa,RM))..
         BSPa(RM,R,Pa) =E= 0;

plantABalanceZero(RM,Pa,Pb)$(NotPaRM(Pa,RM))..
         XPaPb(Pa,Pb) =E= 0;

$offtext
*----------------------PLANT B------------------------------------------------

*---------Plant B Capacity-----
plantBcapacity(Pb)..
        SUM((Pa), XPaPb(Pa,Pb)) =L=
        SUM((SizePb)$(SPb(Pb,SizePb)),capacityPb(Pb)*UPb(Pb,SizePb)/efficiencyPb(Pb));

plantBMinCapacity(Pb)..
        SUM((Pa), XPaPb(Pa,Pb))
        =G=
        SUM((SizePb)$(SPb(Pb,SizePb)),capacityPb(Pb)*UPb(Pb,SizePb))*0;

*plantA2plantB(RM,Pa)..
*        SUM((Pb),XPaPb(Pa,Pb)) =E= ethanolProd(RM);

*----------Plant B conversion-
plantBConversion(Pb)..
         MEGprod(Pb) =E= SUM((Pa), XPaPb(Pa,Pb)*efficiencyPb(Pb));

*------Mass balance Plant B
plantBBalance(Pb)..
         SUM((Pa),XPaPb(Pa,Pb)*efficiencyPb(Pb))
         =E=
         SUM((Pc),XPbPc(Pb,Pc));

*----------------------PLANT C------------------------------------------------
*---------Plant C Capacity-----
plantCcapacity(Pc)..
         SUM((Pb), XPbPc(Pb,Pc))
         =L=
         SUM((SizePc)$(SPc(Pc,SizePc)), capacityPc(Pc)*UPc(Pc,SizePc)/efficiencyPc(Pc));

plantCMinCapacity(Pc)..
         SUM((Pb),XPbPc(Pb,Pc)) =G=
         SUM((SizePc)$(SPc(Pc,SizePc)), capacityPc(Pc)*UPc(Pc,SizePc))*0;

*----------Plant C conversion-
plantCConversion(Pc)..
         EGprod(Pc) =E= SUM((Pb),
                 XPbPc(Pb,Pc)*efficiencyPc(Pc));

*------Mass balance Plant C
plantCBalance(Pc)..
         SUM((Pb), XPbPc(Pb,Pc)*efficiencyPc(Pc))
         =E=
         SUM((Pd), XPcPd(Pc,Pd));

*---------- Plant PTA-----------------------------------

***** For 30% Biobased PET - Fossil TPA

fossilTPA(M)..
         SUM((Pd),XMPd(M,Pd))*NoSelectPET
         =L=
         SUM((SizeM)$(SM(M,SizeM)),capacityM(M)*UM(M,SizeM))*NoSelectPET;


******* For 100% bioPET   - Biobased TPA

plantConversionTPA(M)..
         TPAProd(M) =E= SUM((SR,RM)$(DistSupplyPlantATruckTPA(SR,M) gt 0 and bioAvailableTPA(SR) gt 0),
                 BSM(SR,M))*TPAyield*selectPET;

locationPTA(M)..
         SUM((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0 and bioAvailableTPA(SR) gt 0),BSM(SR,M))*selectPET
         =L=
         SUM((SizeM)$(SM(M,SizeM)),capacityM(M)*UM(M,SizeM))*selectPET/WPTA;

locationPTAmax(M)..
         SUM((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0),BSM(SR,M))*selectPET
         =G=
         SUM((SizeM)$(SM(M,SizeM)),capacityM(M)*UM(M,SizeM))*0*selectPET;

balancePTA(M)..
         SUM((SR)$(DistSupplyPlantATruckTPA(SR,M) gt 0),BSM(SR,M))*TPAyield*selectPET
         =E=
         SUM((Pd),XMPd(M,Pd))*selectPET;




*----------------------PLANT D------------------------------------------------
*---------Plant D Capacity-----

plantDcapacity(Pd)..
         SUM((Pc),XPcPd(Pc,Pd)) + SUM((M),XMPd(M,Pd))
         =L=
         SUM((SizePd)$(SPd(Pd,SizePd)), capacityPd(Pd)*UPd(Pd,SizePd));

plantDcapacityM(Pd)..
         SUM((M),XMPd(M,Pd))
         =E=
         SUM((Pc),XPcPd(Pc,Pd))*(0.7/0.3);

plantDCapacityPc(Pd)..
         SUM((Pc),XPcPd(Pc,Pd))
         =L=
         SUM((SizePd)$(SPd(Pd,SizePd)), capacityPd(Pd)*UPd(Pd,SizePd))*WPc;


plantDMinCapacityM(Pd)..
         SUM((M),XMPd(M,Pd))
         =L=
         SUM((SizePd)$(SPd(Pd,SizePd)), capacityPd(Pd)*UPd(Pd,SizePd))*WPTA;
         ;

*----------Plant D conversion-
plantDConversion(Pd)..
         PETprod(Pd) =E= SUM((Pc),XPcPd(Pc,Pd)) + SUM((M), XMPd(M,Pd)) ;


*------Mass balance Plant D

plantDBalance(Pd)..
         SUM((Pc),XPcPd(Pc,Pd)) + SUM((M),XMPd(M,Pd))
         =E=
         SUM((D),XPdD(Pd,D));

*constraint(Pd)..
*         PETprod(Pd) =E= SUM((SizePd)$(SPd(Pd,SizePd)),capacityPd(Pd)*UPd(Pd,SizePd));

*---------------- DEMAND---------------------------------------

*-----Demand Supply

supplyDemand(D)..
         SUM((Pd), XPdD(Pd,D))
*+ XF(D)
         =L=
         capacityD(D);

supplyDemandMin(D)..
        SUM((Pd), XPdD(Pd,D)) =G= capacityD(D)*0.9;
$ontext
*-----Demand Balance
demandBalance..
         SUM((D),capacityD(D)) =E= SUM((Pd,D), XPdD(Pd,D));
$offtext
*---- Fossil fuel requirement
*fossilBasedNeed(D)..
*         XF(D) =L= capacityD(D);


*----------Binary variable---------------------------------------------------
*plantArestrict(Pa)..
*         SUM((SizePa)$(SPa(Pa,SizePa)),UP(Pa,SizePa)) =G= 5;

plantSelection(SizePa)..
         SUM((Pa),UP(Pa,SizePa)) =L= numberPlantA;

plantBselection(SizePb)..
         SUM((Pb),UPb(Pb,SizePb)) =L= numberPlantB;

plantCselection(SizePc)..
         SUM((Pc),UPc(Pc,SizePc)) =L= numberPlantC;

plantDselection(SizePd)..
         SUM((Pd),UPd(Pd,SizePd)) =L= numberPlantD;

plantMselection(SizeM)..
         SUM((M),UM(M,SizeM)) =L= numberPlantM;


*SUM((Pc,SizePc),UPc(Pc,SizePc))
*demandSelection..
*         SUM((D),UPd(D)) =E= 1;

