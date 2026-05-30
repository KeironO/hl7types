import importlib

_NAMES = {
    'ACK', 'ADT_A01', 'ADT_A02', 'ADT_A03', 'ADT_A05', 'ADT_A06', 'ADT_A09',
    'ADT_A12', 'ADT_A15', 'ADT_A16', 'ADT_A17', 'ADT_A20', 'ADT_A21',
    'ADT_A24', 'ADT_A37', 'ADT_A38', 'ADT_A39', 'ADT_A43', 'ADT_A44',
    'ADT_A45', 'ADT_A50', 'ADT_A52', 'ADT_A54', 'ADT_A60', 'ADT_A61',
    'BAR_P01', 'BAR_P02', 'BAR_P05', 'BAR_P06', 'BAR_P10', 'BAR_P12',
    'BPS_O29', 'BRP_O30', 'BRT_O32', 'BTS_O31', 'CCF_I22', 'CCI_I22',
    'CCM_I21', 'CCQ_I19', 'CCR_I16', 'CCU_I20', 'CQU_I19', 'CRM_C01',
    'CSU_C09', 'DFT_P03', 'DFT_P11', 'EAC_U07', 'EAN_U09', 'EAR_U08',
    'EHC_E01', 'EHC_E02', 'EHC_E04', 'EHC_E10', 'EHC_E12', 'EHC_E13',
    'EHC_E15', 'EHC_E20', 'EHC_E21', 'EHC_E24', 'ESR_U02', 'ESU_U01',
    'INR_U06', 'INU_U05', 'LSU_U12', 'MDM_T01', 'MDM_T02', 'MFK_M01',
    'MFN_M02', 'MFN_M04', 'MFN_M05', 'MFN_M06', 'MFN_M07', 'MFN_M08',
    'MFN_M09', 'MFN_M10', 'MFN_M11', 'MFN_M12', 'MFN_M13', 'MFN_M15',
    'MFN_M16', 'MFN_M17', 'MFN_Znn', 'NMD_N02', 'OMB_O27', 'OMD_O03',
    'OMG_O19', 'OMI_O23', 'OML_O21', 'OML_O33', 'OML_O35', 'OML_O39',
    'OMN_O07', 'OMP_O09', 'OMS_O05', 'OPL_O37', 'OPR_O38', 'OPU_R25',
    'ORA_R33', 'ORB_O28', 'ORD_O04', 'ORG_O20', 'ORI_O24', 'ORL_O22',
    'ORL_O34', 'ORL_O36', 'ORL_O40', 'ORN_O08', 'ORP_O10', 'ORS_O06',
    'ORU_R01', 'ORU_R30', 'OSM_R26', 'OUL_R22', 'OUL_R23', 'OUL_R24',
    'PEX_P07', 'PGL_PC6', 'PMU_B01', 'PMU_B03', 'PMU_B04', 'PMU_B07',
    'PMU_B08', 'PPG_PCG', 'PPP_PCB', 'PPR_PC1', 'PPT_PCL', 'PPV_PCA',
    'PRR_PC5', 'PTR_PCF', 'QBP_E03', 'QBP_E22', 'QBP_Q11', 'QBP_Q13',
    'QBP_Q15', 'QBP_Q21', 'QBP_Qnn', 'QBP_Z73', 'QCN_J01', 'QRY_PC4',
    'QSB_Q16', 'QVR_Q17', 'RAS_O17', 'RCI_I05', 'RCL_I06', 'RDE_O11',
    'RDR_RDR', 'RDS_O13', 'RDY_K15', 'REF_I12', 'RGV_O15', 'RPA_I08',
    'RPI_I01', 'RPI_I04', 'RPL_I02', 'RPR_I03', 'RQA_I08', 'RQC_I05',
    'RQI_I01', 'RQP_I04', 'RRA_O18', 'RRD_O14', 'RRE_O12', 'RRG_O16',
    'RRI_I12', 'RSP_E03', 'RSP_E22', 'RSP_K11', 'RSP_K21', 'RSP_K22',
    'RSP_K23', 'RSP_K25', 'RSP_K31', 'RSP_K32', 'RSP_Z82', 'RSP_Z86',
    'RSP_Z88', 'RSP_Z90', 'RTB_K13', 'RTB_Knn', 'RTB_Z74', 'SDR_S31',
    'SDR_S32', 'SIU_S12', 'SLR_S28', 'SRM_S01', 'SRR_S01', 'SSR_U04',
    'SSU_U03', 'STC_S33', 'TCU_U10', 'UDM_Q05', 'VXU_V04'
}


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _NAMES:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
