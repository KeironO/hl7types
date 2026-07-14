"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: EHC_E01.PRODUCT_SERVICE_GROUP
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import Field
from hl7types.hl7 import HL7Model

from ..segments.IPR import IPR
from ..segments.LOC import LOC
from ..segments.PRT import PRT
from ..segments.PSG import PSG
from ..segments.ROL import ROL

from .EHC_E01_PATIENT_INFO import EHC_E01_PATIENT_INFO
from .EHC_E01_PROCEDURE import EHC_E01_PROCEDURE
from .EHC_E01_PRODUCT_SERVICE_LINE_ITEM import EHC_E01_PRODUCT_SERVICE_LINE_ITEM

_EHC_E01_PATIENT_INFO = EHC_E01_PATIENT_INFO
_EHC_E01_PROCEDURE = EHC_E01_PROCEDURE
_EHC_E01_PRODUCT_SERVICE_LINE_ITEM = EHC_E01_PRODUCT_SERVICE_LINE_ITEM
_IPR = IPR
_LOC = LOC
_PRT = PRT
_PSG = PSG
_ROL = ROL


class EHC_E01_PRODUCT_SERVICE_GROUP(HL7Model):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): Product/Service Group, required
        LOC (Optional[List[LOC]]): Location Identification, optional
        PRT (Optional[List[PRT]]): Participation Information, optional
        ROL (Optional[List[ROL]]): Role, optional
        PATIENT_INFO (Optional[List[EHC_E01_PATIENT_INFO]]): optional
        PRODUCT_SERVICE_LINE_ITEM (List[EHC_E01_PRODUCT_SERVICE_LINE_ITEM]): required
        PROCEDURE (Optional[List[EHC_E01_PROCEDURE]]): optional
        IPR (Optional[List[IPR]]): Invoice Processing Results, optional
    """

    PSG: _PSG = Field(
        title="PSG",
        description="Product/Service Group",
    )

    LOC: Optional[List[_LOC]] = Field(
        default=None,
        title="LOC",
        description="Location Identification",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    ROL: Optional[List[_ROL]] = Field(
        default=None,
        title="ROL",
        description="Role",
    )

    PATIENT_INFO: Optional[List[_EHC_E01_PATIENT_INFO]] = Field(
        default=None,
        title="PATIENT_INFO",
    )

    PRODUCT_SERVICE_LINE_ITEM: List[_EHC_E01_PRODUCT_SERVICE_LINE_ITEM] = Field(
        min_length=1,
        title="PRODUCT_SERVICE_LINE_ITEM",
    )

    PROCEDURE: Optional[List[_EHC_E01_PROCEDURE]] = Field(
        default=None,
        title="PROCEDURE",
    )

    IPR: Optional[List[_IPR]] = Field(
        default=None,
        title="IPR",
        description="Invoice Processing Results",
    )

    model_config = {"populate_by_name": True}
