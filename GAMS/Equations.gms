* ==============================================================================
*   - EQUATIONS -
* ==============================================================================


*-------------------------------------------------------------------------------
*-----------------------   COSTS    --------------------------------------------
*-------------------------------------------------------------------------------
*
*----------Biomass cost-----
supplyCost(C,RM)..
         biomassSupplyCost(C,RM) =E= SUM((R,Pa)$(CR(C,R)),
                 BSPa(RM,R,Pa)*BiomassCost(C,R,RM));

*---------Biomass Transporation Cost-----
BiomassTransportCost(RM)..
         TransportCostBiomass(RM) =E=
*---- Fixed Costs
                 SUM ((C,R,Pa)$(CR(C,R)),
                 BSPa(RM,R,Pa)*(FixCostBiomassTruck(C)*DistSupplyPlantATruck(RM,R,Pa) + FixCostBiomassTrain(C)*DistSupplyPlantATrain(RM,R,Pa) + FixCostBiomassShip(C)*DistSupplyPlantAShip(RM,R,Pa)))
            +
*-----Variable Costs
                 SUM((C,R,Pa)$(CR(C,R)),
                 BSPa(RM,R,Pa)*(VarCostBiomassTruck(C)*DistSupplyPlantATruck(RM,R,Pa) + VarCostBiomassTrain(C)*DistSupplyPlantATrain(RM,R,Pa) + VarCostBiomassShip(C)*DistSupplyPlantAShip(RM,R,Pa)));

*-------------------------------------PLANT A-----------------------------------
*--------Plant A cost------------
InvCostPlantA(Pa)..
         PlantACapex(Pa) =E= SUM((RM,SizePa)$(SPa(Pa,SizePa)),
                 CapitalCostPlantA(RM,Pa,SizePa)*UP(Pa,SizePa));

OperatCostPlantA(Pa)..
         PlantAOpex(Pa) =E=
* Fixed Operating Costs
                 SUM((RM,SizePa)$(SPa(Pa,SizePa)),
                 FixOpexPlantA(RM,Pa,SizePa)*UP(Pa,SizePa))
         +
* Variable Operating Costs
                 SUM((RM,SizePa)$(SPa(Pa,SizePa)),
                 VarOpexPlantA(RM,Pa,SizePa)*UP(Pa,SizePa));

*----------Product A cost (supplied to plant B)-----
productACost(PRD,Pa)..
         CostProductA(PRD,Pa) =E= SUM((RM,Pb)$(RMPRD(RM,PRD)),
                 XPaPb(Pa,Pb)*ProductAPrice(RM,Pa,PRD));

byproductACost(Byp,Pa)..
         costByproductA(Byp,Pa) =E= SUM((RM)$(RMB(RM,Byp) and distByp gt 0),
                 byproductProd(RM,Byp,Pa)*byproductAPrice(RM,Pa,Byp));


*---------Plant A product (Ethanol) Transportation Cost-----

productATransportCost(Pa)..
         TransportCostProductA(Pa) =E=
*---- Fixed Costs
                 SUM ((Pb),
                 XPaPb(Pa,Pb)*(FixCostProductATruck(Pa)*DistSupplyPlantBTruck(Pa,Pb) + FixCostProductATrain(Pa)*DistSupplyPlantBTrain(Pa,Pb) + FixCostProductAShip(Pa)*DistSupplyPlantBShip(Pa,Pb)))
            +
*-----Variable Costs
                 SUM((Pb),
                 XPaPb(Pa,Pb)*(VarCostProductATruck(Pa)*DistSupplyPlantBTruck(Pa,Pb) + VarCostProductATrain(Pa)*DistSupplyPlantBTrain(Pa,Pb) + VarCostProductAShip(Pa)*DistSupplyPlantBShip(Pa,Pb)));

**----- Plant A by-products Transportation Cost----

byproductATransportCost(Byp)..
         TransportCostByproductA(Byp) =E=
*---- Fixed Costs
                 SUM ((RM,Pa),
                 byproductProd(RM,Byp,Pa)*FixCostProductATruck(Pa)*distByp)
            +
*-----Variable Costs
                 SUM((RM,Pa)$(distByp gt 0),
                 distByp*byproductProd(RM,Byp,Pa)*VarCostProductATruck(Pa));


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
                         XPbPc(Pb,Pc)*(FixCostProductBTruck(Pb)*DistSupplyPlantCTruck(Pb,Pc) + FixCostProductBTrain(Pb)*DistSupplyPlantCTrain(Pb,Pc) + FixCostProductBShip(Pb)*DistSupplyPlantCShip(Pb,Pc)))
      +
*-----Variable Costs
                 SUM((Pc),
                         XPbPc(Pb,Pc)*(VarCostProductBTruck(Pb)*DistSupplyPlantCTruck(Pb,Pc) + VarCostProductBTrain(Pb)*DistSupplyPlantCTrain(Pb,Pc) + VarCostProductBShip(Pb)*DistSupplyPlantCShip(Pb,Pc)));

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
                 XPcPd(Pc,Pd)*(FixCostProductCTruck(Pc)*DistSupplyPlantDTruck(Pc,Pd) + FixCostProductCTrain(Pc)*DistSupplyPlantDTrain(Pc,Pd) + FixCostProductCShip(Pc)*DistSupplyPlantDShip(Pc,Pd)))
         +
*-----Variable Costs
                 SUM((Pd),
                 XPcPd(Pc,Pd)*(VarCostProductCTruck(Pc)*DistSupplyPlantDTruck(Pc,Pd) + VarCostProductCTrain(Pc)*DistSupplyPlantDTrain(Pc,Pd) + VarCostProductCShip(Pc)*DistSupplyPlantDShip(Pc,Pd)));

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

$ontext
*---------Plant D product (PET) Transportation Cost-----

productDTransportCost(Pd)..
         TransportCostProductD(Pd) =E=
*---- Fixed Costs
                 SUM ((D),XPdD(Pd,D)*(FixCostProductDTruck(Pd)*DistSupplyDemandTruck(Pd,D) + FixCostProductDTrain(Pd)*DistSupplyDemandTrain(Pd,D) + FixCostProductDShip(Pd)*DistSupplyDemandShip(Pd,D)))
         +
*-----Variable Costs
                 SUM((D),
                 XPdD(Pd,D)*(VarCostProductDTruck(Pd)*DistSupplyDemandTruck(Pd,D) + VarCostProductDTrain(Pd)*DistSupplyDemandTrain(Pd,D) + VarCostProductDShip(Pd)*DistSupplyDemandShip(Pd,D)));

$offtext


*-----------------------------OTHER COSTS ------------------------------------------

** PTA Costs
$ontext
costPTA(M)..
         PTAcost(M) =E= SUM((Pd),XMPd(M,Pd)*PTAprice(M));

transportPTAcost(M)..
         PTAtransportCost(M) =E=
                 SUM((Pd), XMPd(M,Pd)*FixCostProductDTruck(Pd)*DistPTAtransp)
                 +
                 SUM((Pd), XMPd(M,Pd)*VarCostProductDTruck(Pd)*DistPTAtransp);
$offtext
**--- Fossil-based PET cost
fossilCost(D)..
         costFossil(D) =E=  XF(D)*fossilPrice(D);


*-------------------------------------------------------------------------------
*-----------------------   EMISSIONS    --------------------------------------------
*-------------------------------------------------------------------------------

* ----- Transportation emissions------------------
biomTransEmi(RM)..
         transEmiBio(RM) =E= SUM((R,Pa),
                 BSPa(RM,R,Pa)*(transEmiTruck*DistSupplyPlantATruck(RM,R,Pa) + transEmiTrain*DistSupplyPlantATrain(RM,R,Pa) + transEmiShip*DistSupplyPlantAShip(RM,R,Pa)));

transProdA(Pa)..
         transProdAemi(Pa) =E= SUM((Pb),
                 XPaPb(Pa,Pb)*(transEmiTruck*DistSupplyPlantBTruck(Pa,Pb) + transEmiTrain*DistSupplyPlantBTrain(Pa,Pb) + transEmiShip*DistSupplyPlantBShip(Pa,Pb)));
transBypA(Pa)..
         transBypAemi(Pa) =E= SUM((RM,Byp)$(RMB(RM,Byp)), distByp*byproductProd(RM,Byp,Pa)*(transEmiTruck));

transProdB(Pb)..
         transProdBemi(Pb) =E= SUM((Pc),
                         XPbPc(Pb,Pc)*(transEmiTruck*DistSupplyPlantCTruck(Pb,Pc) + transEmiTrain*DistSupplyPlantCTrain(Pb,Pc) + transEmiShip*DistSupplyPlantCShip(Pb,Pc)));

transProdC(Pc)..
         transProdCemi(Pc) =E=  SUM((Pd),
                 XPcPd(Pc,Pd)*(transEmiTruck*DistSupplyPlantDTruck(Pc,Pd) + transEmiTrain*DistSupplyPlantDTrain(Pc,Pd) + transEmiShip*DistSupplyPlantDShip(Pc,Pd)));
*transPTA(M)..
*         transpEmiPTA(M) =E= SUM((Pd),XMPd(M,Pd)*distPTAtransp*transEmiTruck);

transFossil(D)..
         fossilTrans(D) =E= XF(D)*distFossil*(transEmiTruck);
transEmi..
         EmissionTransport =E= SUM((RM),transEmiBio(RM)) + SUM((Pa), transProdAemi(Pa)) + SUM((Pa), transBypAemi(Pa)) + SUM((Pb), transProdBemi(Pb)) + SUM((Pc), transProdCemi(Pc)) + SUM((D),fossilTrans(D));

$ontext
transProdD(Pd)..
         transProdDemi(Pd) =E=  SUM((D),
                 XPdD(Pd,D)*(transEmiTruck*DistSupplyDemandTruck(Pd,D) + transEmiTrain*DistSupplyDemandTrain(Pd,D) + transEmiShip*DistSupplyDemandShip(Pd,D)));
$offtext
* -------- Process emissions (LCA) ----------------------

processEmissions..
         emissionsProcess =E=
                 SUM((Pd,RM), plantDemi(Pd,RM)*PETprod(Pd))
                 +
                 SUM((D),fossilEmi*XF(D));

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
                 SUM((D),fossilEmi*XF(D));
$offtext


*-------------------------------------------------------------------------------
*-----------------------   CONSTRAINTS  ----------------------------------------
*-------------------------------------------------------------------------------
*
*----------Biomass availability-
supplyBiomass(C,R,RM)$CR(C,R)..
         SUM((Pa)$(PaRM(Pa,RM)),BSPa(RM,R,Pa))
         =L=
         bioAvailable(C,R,RM);

*----------Biomass Trades-------------
$ontext
biomassExports(R)..
         SUM((I,RM)$(IRE(I,R)),exportBiomassRegions(R,I,RM))
         =E=
         SUM((I,RM)$(IRE(I,R)),extBiomImportPoint(R,I,RM));

exportBound(R)..
         SUM((I,RM)$(IRE(I,R)),exportBiomassRegions(R,I,RM))
         =L=
         SUM((RM),maxBiomExport(R,RM));

biomassImport(I)..
         SUM((R,RM)$(IRE(I,R)),extBiomImportPoint(R,I,RM))
         =E=
         SUM((Pa,SizePa,RM)$(SPa(Pa,SizePa)),extBiomImportPlant(I,Pa,SizePa,RM));

importBiomBound(R)..
         SUM((C,I,RM)$(CI(C,I) and IRE(I,R)),extBiomImportPoint(R,I,RM))
         =L=
         SUM((RM),maxBiomImport(R,RM));
$offtext
*---------------PLANT A-----------------------------------------------------
*----------Plant A conversion-
plantConversion(RM,PRD,Pa)..
         ethanolProd(RM,PRD,Pa) =E= SUM((R),
                 BSPa(RM,R,Pa)*efficiencyPa(RM,PRD));

*--------Plant A by-products
byproductConversion(RM,Byp,Pa)..
         byproductProd(RM,Byp,Pa) =E= SUM((R),
                 BSPa(RM,R,Pa)*yieldBy(RM,Byp));

*----------Plant A Capacity-
plantCapacity(RM,Pa)..
         SUM((R),BSPa(RM,R,Pa)) =L=
         SUM((SizePa)$(SPa(Pa,SizePa) and PaRM(Pa,RM)),capacityPa(Pa)*UP(Pa,SizePa));

plantMinCapacity(RM,Pa)..
         SUM((R),BSPa(RM,R,Pa))
         =G=
         SUM((SizePa)$(SPa(Pa,SizePa) and PaRM(Pa,RM)),capacityPa(Pa)*UP(Pa,SizePa))*0.8;

*------Mass balance Plant A
plantABalance(RM,Pa)..
         SUM((R,PRD),BSPa(RM,R,Pa)*efficiencyPa(RM,PRD))
         =E=
         SUM((Pb),XPaPb(Pa,Pb));

*----------------------PLANT B------------------------------------------------

*---------Plant B Capacity-----
plantBcapacity(Pb)..
        SUM((Pa), XPaPb(Pa,Pb)) =L=
        SUM((SizePb)$(SPb(Pb,SizePb)),capacityPb(Pb)*UPb(Pb,SizePb));

plantBMinCapacity(Pb)..
        SUM((Pa), XPaPb(Pa,Pb))
        =G=
        SUM((SizePb)$(SPb(Pb,SizePb)),capacityPb(Pb)*UPb(Pb,SizePb))*0.8;

*plantA2plantB(RM,Pa)..
*        SUM((Pb),XPaPb(Pa,Pb)) =E= ethanolProd(RM);

*----------Plant B conversion-
plantBConversion(Pb)..
         MEGprod(Pb) =E= SUM((Pa),
                 XPaPb(Pa,Pb)*efficiencyPb(Pb));

*------Mass balance Plant B
plantBBalance(Pb)..
         SUM((Pa),
                 XPaPb(Pa,Pb)*efficiencyPb(Pb))
         =E=
         SUM((Pc),XPbPc(Pb,Pc));

*----------------------PLANT C------------------------------------------------
*---------Plant C Capacity-----
plantCcapacity(Pc)..
         SUM((Pb), XPbPc(Pb,Pc))
         =L=
         SUM((SizePc)$(SPc(Pc,SizePc)),
                  capacityPc(Pc)*UPc(Pc,SizePc));

plantCMinCapacity(Pc)..
         SUM((Pb),XPbPc(Pb,Pc)) =G=
         SUM((SizePc)$(SPc(Pc,SizePc)), capacityPc(Pc)*UPc(Pc,SizePc))*0.8;

*----------Plant C conversion-
plantCConversion(Pc)..
         EGprod(Pc) =E= SUM((Pb),
                 XPbPc(Pb,Pc)*efficiencyPc(Pc));

*------Mass balance Plant C
plantCBalance(Pc)..
         SUM((Pb),
         XPbPc(Pb,Pc)*efficiencyPc(Pc))
         =E=
         SUM((Pd),XPcPd(Pc,Pd));


*----------------------PLANT D------------------------------------------------
*---------Plant D Capacity-----
plantDcapacity(Pd)..
         SUM((Pc),XPcPd(Pc,Pd))
*WPc
*+ SUM((M),XMPd(M,Pd))*WPTA
         =L=
         SUM((SizePd)$(SPd(Pd,SizePd)),
                  capacityPd(Pd)*UPd(Pd,SizePd));

plantDMinCapacity(Pd)..
         SUM((Pc),XPcPd(Pc,Pd))
*WPc
*+ SUM((M),XMPd(M,Pd))*WPTA
         =G=
         SUM((SizePd)$(SPd(Pd,SizePd)), capacityPd(Pd)*UPd(Pd,SizePd))*0.8;

*----------Plant D conversion-
plantDConversion(Pd)..
         PETprod(Pd) =E= SUM((Pc),XPcPd(Pc,Pd)*efficiencyPd(Pd))
*WPc
*+ SUM((M),XMPd(M,Pd))*WPTA
;

*------Mass balance Plant D
plantDBalance(Pd)..
         SUM((Pc),XPcPd(Pc,Pd)*efficiencyPd(Pd))
*WPc
*+ SUM((M),XMPd(M,Pd))*WPTA
         =E=
         SUM((D),XPdD(Pd,D));


*---------------- DEMAND---------------------------------------

*-----Demand Supply

supplyDemand(D)..
         SUM((Pd), XPdD(Pd,D))
         =L=
         capacityD(D);

supplyDemandMin(D)..
        SUM((Pd), XPdD(Pd,D)) =L= capacityD(D)*0.8;

*-----Demand Balance
demandBalance(D)..
         capacityD(D) =E= SUM((Pd), XPdD(Pd,D)) +  XF(D);

*---- Fossil fuel requirement

fossilBasedNeed(D)..
         XF(D) =L= capacityD(D);


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

*demandSelection..
*         SUM((D),UPd(D)) =E= 1;
