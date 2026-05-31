import importlib

_all_ = {
    'ACK', 'ADT_A01', 'ADT_A02', 'ADT_A03', 'ADT_A06', 'ADT_A09', 'ADT_A12',
    'ADT_A16', 'ADT_A17', 'ADT_A18', 'ADT_A20', 'ADT_A24', 'ADT_A30',
    'ADT_A38', 'ADT_A39', 'ADT_A43', 'ADT_A45', 'ADT_A50', 'ARD_A19',
    'BAR_P01', 'BAR_P02', 'BAR_P06', 'CRM_C01', 'CSU_C09', 'DFT_P03',
    'DOC_T12', 'DSR_Q01', 'DSR_Q03', 'EDR_Q01', 'EQQ_Q01', 'ERP_Q01',
    'MDM_T01', 'MDM_T02', 'MFK_M01', 'MFK_M02', 'MFN_M01', 'MFN_M02',
    'MFN_M03', 'MFN_M05', 'MFN_M06', 'MFN_M07', 'MFN_M08', 'MFN_M09',
    'MFN_M10', 'MFN_M11', 'OMD_O01', 'OMN_O01', 'OMS_O01', 'ORD_O02',
    'ORF_R04', 'ORM_O01', 'ORN_O02', 'ORR_O02', 'ORU_R01', 'OSQ_Q06',
    'OSR_Q06', 'PEX_P07', 'PGL_PC6', 'PIN_I07', 'PPG_PCG', 'PPP_PCB',
    'PPR_PC1', 'PPT_PCL', 'PPV_PCA', 'PRR_PC5', 'PTR_PCF', 'QCK_Q02',
    'QRY_A19', 'QRY_PC4', 'QRY_Q01', 'QRY_Q02', 'QRY_R02', 'QRY_T12',
    'RAR_RAR', 'RAS_O01', 'RCI_I05', 'RCL_I06', 'RDE_O01', 'RDO_O01',
    'RDR_RDR', 'RDS_O01', 'REF_I12', 'RER_RER', 'RGR_RGR', 'RGV_O01',
    'ROR_ROR', 'RPA_I08', 'RPI_I01', 'RPL_I02', 'RQA_I08', 'RQC_I05',
    'RQC_I06', 'RQI_I01', 'RQP_I04', 'RQQ_Q01', 'RRA_O02', 'RRD_O02',
    'RRG_O02', 'RRI_I12', 'RRO_O02', 'SIU_S12', 'SPQ_Q01', 'SQM_S25',
    'SQR_S25', 'SRM_S01', 'SRR_S01', 'SUR_P09', 'TBR_Q01', 'UDM_Q05',
    'VQQ_Q01', 'VXQ_V01', 'VXR_V03', 'VXU_V04', 'VXX_V02'
}  # type: ignore


def __getattr__(name: str):  # type: ignore[misc]
    if name not in _all_:
        raise AttributeError(f'module {__name__!r} has no attribute {name!r}')
    mod = importlib.import_module(f'.{name}', __name__)
    return getattr(mod, name)
