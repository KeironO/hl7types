import importlib
import sys
import types

_all_ = {
    'ACK', 'ADT_A01', 'ADT_A02', 'ADT_A03', 'ADT_A04', 'ADT_A05', 'ADT_A06',
    'ADT_A07', 'ADT_A08', 'ADT_A09', 'ADT_A10', 'ADT_A11', 'ADT_A12',
    'ADT_A13', 'ADT_A14', 'ADT_A15', 'ADT_A16', 'ADT_A17', 'ADT_A18',
    'ADT_A20', 'ADT_A21', 'ADT_A22', 'ADT_A23', 'ADT_A24', 'ADT_A25',
    'ADT_A26', 'ADT_A27', 'ADT_A28', 'ADT_A29', 'ADT_A30', 'ADT_A31',
    'ADT_A32', 'ADT_A33', 'ADT_A34', 'ADT_A35', 'ADT_A36', 'ADT_A37',
    'ADT_A38', 'ADT_A39', 'ADT_A40', 'ADT_A41', 'ADT_A42', 'ADT_A43',
    'ADT_A44', 'ADT_A45', 'ADT_A46', 'ADT_A47', 'ADT_A48', 'ADT_A49',
    'ADT_A50', 'ADT_A51', 'ARD_A19', 'BAR_P01', 'BAR_P02', 'BAR_P05',
    'BAR_P06', 'CRM_C01', 'CRM_C02', 'CRM_C03', 'CRM_C04', 'CRM_C05',
    'CRM_C06', 'CRM_C07', 'CRM_C08', 'CSU_C09', 'CSU_C10', 'CSU_C11',
    'CSU_C12', 'DFT_P03', 'DOC_T12', 'DSR_Q01', 'DSR_Q03', 'EDR_Q01',
    'EQQ_Q01', 'ERP_Q01', 'MDM_T01', 'MDM_T02', 'MDM_T03', 'MDM_T04',
    'MDM_T05', 'MDM_T06', 'MDM_T07', 'MDM_T08', 'MDM_T09', 'MDM_T10',
    'MDM_T11', 'MFK_M01', 'MFK_M02', 'MFN_M01', 'MFN_M02', 'MFN_M03',
    'MFN_M04', 'MFN_M05', 'MFN_M06', 'MFN_M07', 'MFN_M08', 'MFN_M09',
    'MFN_M10', 'MFN_M11', 'OMD_O01', 'OMN_O01', 'OMS_O01', 'ORD_O02',
    'ORF_R04', 'ORM_O01', 'ORN_O02', 'ORR_O02', 'ORU_R01', 'OSQ_Q06',
    'OSR_Q06', 'PEX_P07', 'PEX_P08', 'PGL_PC6', 'PGL_PC7', 'PGL_PC8',
    'PIN_I07', 'PPG_PCG', 'PPG_PCH', 'PPG_PCJ', 'PPP_PCB', 'PPP_PCC',
    'PPP_PCD', 'PPR_PC1', 'PPR_PC2', 'PPR_PC3', 'PPT_PCL', 'PPV_PCA',
    'PRR_PC5', 'PTR_PCF', 'QCK_Q02', 'QRY_A19', 'QRY_PC4', 'QRY_PC9',
    'QRY_PCE', 'QRY_PCK', 'QRY_Q01', 'QRY_Q02', 'QRY_R02', 'QRY_T12',
    'RAR_RAR', 'RAS_O01', 'RCI_I05', 'RCL_I06', 'RDE_O01', 'RDO_O01',
    'RDR_RDR', 'RDS_O01', 'REF_I12', 'REF_I13', 'REF_I14', 'REF_I15',
    'RER_RER', 'RGR_RGR', 'RGV_O01', 'ROR_ROR', 'RPA_I08', 'RPI_I01',
    'RPL_I02', 'RQA_I08', 'RQA_I09', 'RQA_I10', 'RQA_I11', 'RQC_I05',
    'RQC_I06', 'RQI_I01', 'RQI_I02', 'RQI_I03', 'RQP_I04', 'RQQ_Q01',
    'RRA_O02', 'RRD_O02', 'RRG_O02', 'RRI_I12', 'RRO_O02', 'SIU_S12',
    'SIU_S13', 'SIU_S14', 'SIU_S15', 'SIU_S16', 'SIU_S17', 'SIU_S18',
    'SIU_S19', 'SIU_S20', 'SIU_S21', 'SIU_S22', 'SIU_S23', 'SIU_S24',
    'SIU_S26', 'SPQ_Q01', 'SQM_S25', 'SQR_S25', 'SRM_S01', 'SRM_S02',
    'SRM_S03', 'SRM_S04', 'SRM_S05', 'SRM_S06', 'SRM_S07', 'SRM_S08',
    'SRM_S09', 'SRM_S10', 'SRM_S11', 'SRR_S01', 'SUR_P09', 'TBR_Q01',
    'UDM_Q05', 'VQQ_Q01', 'VXQ_V01', 'VXR_V03', 'VXU_V04', 'VXX_V02'
}  # type: ignore


class _LazyModule(types.ModuleType):
    def __getattr__(self, name: str):  # type: ignore[misc]
        if name not in _all_:
            raise AttributeError(f'module {self.__name__!r} has no attribute {name!r}')
        mod = importlib.import_module(f'.{name}', self.__name__)
        cls = getattr(mod, name)
        self.__dict__[name] = cls
        return cls

    def __setattr__(self, name: str, value) -> None:  # type: ignore[override]
        if name in _all_ and isinstance(value, types.ModuleType):
            self.__dict__[name] = getattr(value, name)
        else:
            self.__dict__[name] = value


sys.modules[__name__].__class__ = _LazyModule
