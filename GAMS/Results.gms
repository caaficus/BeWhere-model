* ==============================================================================
*   - RESULTS -
* ==============================================================================


********************************************************************************
FILE resultCost /resultCost4.txt/;
         PUT resultCost;
         PUT "%---- Resolution ------"/;
********************************************************************************
         PUT "MODELSTAT = "
         PUT facilityLocation.MODELSTAT:6:0
         PUT ";"/;
*
         PUT "SOLVESTAT = "
         PUT facilityLocation.SOLVESTAT:6:0
         PUT ";"/;
*
         PUT "RESUSD = "
         PUT facilityLocation.RESUSD:6:0
         PUT ";"/;
********************************************************************************
         PUT "%---- ECONOMIC ----"/;
********************************************************************************
         PUT "TOTAL SYSTEMS COST  = "
         PUT (COMBINEEQUATIONS.L):20:6/;
         PUT "];"/;

         PUT "PET PRODUCTION COSTS = "
         PUT ";"/;
         PUT (SUM((Pd),CostProductD.L(Pd))):20:6/;
         PUT ";"/;

********************************************************************************
         PUT "%-----TOTAL PROCESS COST-----"/;
         PUT ( PROFIT.L):20:6/;
         PUT ";"/;

         PUT "%-----TOTAL EMISSIONS COST----"/;
         PUT (ENVCOSTS.L):20:6/;
         PUT ";"/;


         PUT "%-----TRANSPORTATION EMISSIONS-----"/;
         PUT (EmissionTransport.L):20:6/;
         PUT ";"/;

         PUT "%-----PROCESS EMISSIONS----"/;
         PUT (SUM((Pd),emissionsProcessSug.L(Pd))):20:6/;
         PUT ";"/;


********************************************************************************
         PUT "%---- Biomass ----"/;
********************************************************************************
         PUT "BIOMASS COST  = "
         PUT ";"/;
         LOOP((Pa)$(biomassSupplyCost.L(Pa) gt 0), PUT "[" Pa.TL:40:0","  biomassSupplyCost.L(Pa):20:6"],"/);
         PUT ";"/;

         PUT "BIOMASS COST TPA = "
         PUT ";"/;
         LOOP((M)$(biomassSupplyCostTPA.L(M) gt 0), PUT "[" M.TL:40:0","  biomassSupplyCostTPA.L(M):20:6"],"/);
         PUT ";"/;

         PUT "BIOMASS SUPPLY COST  = "
         PUT ";"/;
         LOOP((Pa)$(TransportCostBiomass.L(Pa) gt 0), PUT "[" Pa.TL:40:0","  TransportCostBiomass.L(Pa):20:6"],"/);
         PUT ";"/;

         PUT "BIOMASS SUPPLY COST TPA = "
         PUT ";"/;
         LOOP((M)$(TransportCostBiomassTPA.L(M) gt 0), PUT "[" M.TL:40:0","  TransportCostBiomassTPA.L(M):20:6"],"/);
         PUT ";"/;

         PUT "Supply_to_Pa  = "
         PUT ";"/;
         LOOP((SR,RM,Pa)$(BSPa.L(SR,RM,Pa) gt 0 and PaRM(RM,Pa)), PUT "[" SR.TL:15:0", " RM.TL:15:0"," Pa.TL:15:0","  BSPa.L(SR,RM,Pa):20:6"],"/);
         PUT ";"/;
*
         PUT "Pa_to_Pb  = "
          PUT ";"/;
         LOOP((Pa,Pb)$(XPaPb.L(Pa,Pb) gt 0), PUT "[" Pa.TL:15:0", " Pb.TL:15:0","  XPaPb.L(Pa,Pb):20:6"],"/);
         PUT ";"/;

         PUT "Pb_to_Pc  = "
          PUT ";"/;
         LOOP((Pb,Pc)$(XPbPc.L(Pb,Pc) gt 0), PUT "[" Pb.TL:15:0", " Pc.TL:14:0", "  XPbPc.L(Pb,Pc):20:6"],"/);
         PUT ";"/;

         PUT "Pc_to_PD  = "
          PUT ";"/;
         LOOP((Pc,Pd)$(XPcPd.L(Pc,Pd) gt 0), PUT "[" Pc.TL:15:0", " Pd.TL:15:0","  XPcPd.L(Pc,Pd):20:6"],"/);
         PUT ";"/;

         PUT "Pd_to_D  = "
          PUT ";"/;
         LOOP((Pd,D)$(XPdD.L(Pd,D) gt 0), PUT "[" Pd.TL:15:0", " D.TL:6:0", "  XPdD.L(Pd,D):20:6"],"/);
         PUT ";"/;

         PUT "M_to_Pd  = "
          PUT ";"/;
         LOOP((M,Pd)$(XMPd.L(M,Pd) gt 0), PUT "[" M.TL:15:0", " Pd.TL:15:0","  XMPd.L(M,Pd):20:6"],"/);
         PUT ";"/;

         PUT "Supply_to_TPA  = "
         PUT ";"/;
         LOOP((SR,M)$(BSM.L(SR,M) gt 0), PUT "[" SR.TL:15:0", " M.TL:15:0","  BSM.L(SR,M):20:6"],"/);
         PUT ";"/;

         PUT "PET MASSFLOW = "
         PUT ";"/;
         PUT (SUM((Pd),PETprod.L(Pd))):20:6/;
         PUT ";"/;

         PUT "TPA MASSFLOW = "
         PUT ";"/;
         PUT (SUM((M),TPAProd.L(M))):20:6/;
         PUT ";"/;

         PUT "byproduct cost = "
         PUT ";"/;
         LOOP((Pa)$(costByproductA.L(Pa) gt 0), PUT "[" Pa.TL:15:0","  (costByproductA.L(Pa)):20:6"],"/);
         PUT ";"/;

********************************************************************************
         PUT "%---- TECHNOECONOMIC ASSESSMENT ----"/;
********************************************************************************


         PUT "CAPEX AND OPEX  = "
         PUT ";"/;
         LOOP((Pa)$(PlantACapex.L(Pa) gt 0 and PlantAOpex.L(Pa) gt 0), PUT "[" Pa.TL:15:0","  (PlantACapex.L(Pa)):20:6", "  (PlantAOpex.L(Pa) ):20:6"],"/);
         PUT ";"/;

         LOOP((Pb)$(PlantBCapex.L(Pb) gt 0 and PlantBOpex.L(Pb) gt 0), PUT "[" Pb.TL:15:0","  (PlantBCapex.L(Pb)):20:6", "  (PlantBOpex.L(Pb)):20:6"],"/);
         PUT ";"/;

         LOOP((Pc)$(PlantCCapex.L(Pc) gt 0 and PlantCOpex.L(Pc) gt 0), PUT "[" Pc.TL:15:0","  (PlantCCapex.L(Pc)):20:6","  (PlantCOpex.L(Pc)):20:6"],"/);
         PUT ";"/;

         LOOP((Pd)$(PlantDCapex.L(Pd) gt 0 and PlantDOpex.L(Pd) gt 0), PUT "[" Pd.TL:15:0","  (PlantDCapex.L(Pd)):20:6","  (PlantDOpex.L(Pd)):20:6"],"/);
         PUT ";"/;

         LOOP((M)$(TPACapex.L(M) gt 0 and TPAOpex.L(M) gt 0), PUT "[" M.TL:15:0","  (TPACapex.L(M)):20:6","  (TPAOpex.L(M)):20:6"],"/);
         PUT ";"/;

         PUT "TRANSPORTATION COSTS  = "
         PUT ";"/;
         LOOP((Pa)$(SUM((RM),TransportCostProductA.L(RM,Pa)) gt 0 and TransportCostByproductA.L(Pa) gt 0), PUT "[" Pa.TL:15:0","  (SUM((RM), TransportCostProductA.L(RM,Pa))):20:6","  (TransportCostByproductA.L(Pa)):20:6"],"/);
         PUT ";"/;

         LOOP((Pb)$(TransportCostProductB.L(Pb) gt 0), PUT "[" Pb.TL:15:0","  (TransportCostProductB.L(Pb)):20:6"],"/);
         PUT ";"/;

         LOOP((Pc)$(TransportCostProductC.L(Pc) gt 0), PUT "[" Pc.TL:15:0","  (TransportCostProductC.L(Pc)):20:6"],"/);
         PUT ";"/;

         LOOP((Pd)$(TransportCostProductD.L(Pd) gt 0), PUT "[" Pd.TL:15:0","  (TransportCostProductD.L(Pd)):20:6"],"/);
         PUT ";"/;

         LOOP((M)$(PTATransportCost.L(M) gt 0), PUT "[" M.TL:15:0","  (PTATransportCost.L(M)):20:6"],"/);
         PUT ";"/;
$ontext
         PUT "Emissions process per Plant D = "
         PUT ";"/;
         LOOP((Pd)$(emissionsProcessW.L(Pd) gt 0), PUT "[" Pd.TL:15:0","  (emissionsProcessW.L(Pd)):20:6"],"/);
         PUT ";"/;
$offtext
         PUT "Emissions process per Plant D = "
         PUT ";"/;
         LOOP((Pd)$(emissionsProcessSug.L(Pd) gt 0), PUT "[" Pd.TL:15:0","  (emissionsProcessSug.L(Pd)):20:6"],"/);
         PUT ";"/;




*         PUT "TOTAL COST = "
*         PUT (TOTCOST.L):20:6/;
*         PUT "];"/;



$ontext
********************************************************************************
         PUT "%---- Biomass ----"/;
********************************************************************************
         PUT "SYSTEMS COST  = "
         LOOP((RM,Pa,Pb,Pc,Pd,D,T,SizePa,SizePb,SizePc,SizePd)$(UP.L(Pa,SizePa) and UPb.L(Pb,SizePb) and UPc.L(Pc,SizePc) and UPd.L(Pd,SizePd) gt 0),
         PUT "[" RM.TL:15:0"," Pa.TL:15:0"," Pb.TL:15:0"," Pc.TL:15:0"," D.TL:6:0"," T.TL:15:0"," UP.L(Pa,SizePa):20:6", " UPb.L(Pb,SizePb):20:6", " UPc.L(Pc,SizePc):20:6"," UPd.L(Pd,SizePd):20:6"],"/);
         PUT "];"/;

$offtext






