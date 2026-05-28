"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: EHC_E01.PRODUCT_SERVICE_GROUP
Type: Group
"""

from __future__ import annotations

from pydantic import BaseModel, Field

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


class EHC_E01_PRODUCT_SERVICE_GROUP(BaseModel):
    """HL7 v2 EHC_E01.PRODUCT_SERVICE_GROUP group.

    Attributes:
        PSG (PSG): required
        LOC (Optional[List[LOC]]): optional
        PRT (Optional[List[PRT]]): optional
        ROL (Optional[List[ROL]]): optional
        PATIENT_INFO (Optional[List[EHC_E01_PATIENT_INFO]]): optional
        PRODUCT_SERVICE_LINE_ITEM (List[EHC_E01_PRODUCT_SERVICE_LINE_ITEM]): required
        PROCEDURE (Optional[List[EHC_E01_PROCEDURE]]): optional
        IPR (Optional[List[IPR]]): optional
    """

    PSG: _PSG = Field(
        default=...,
        title="PSG",
        description="Required",
    )

    LOC: list[_LOC] | None = Field(
        default=None,
        title="LOC",
        description="Optional, repeating",
    )

    PRT: list[_PRT] | None = Field(
        default=None,
        title="PRT",
        description="Optional, repeating",
    )

    ROL: list[_ROL] | None = Field(
        default=None,
        title="ROL",
        description="Optional, repeating",
    )

    PATIENT_INFO: list[_EHC_E01_PATIENT_INFO] | None = Field(
        default=None,
        title="PATIENT_INFO",
        description="Optional, repeating",
    )

    PRODUCT_SERVICE_LINE_ITEM: list[_EHC_E01_PRODUCT_SERVICE_LINE_ITEM] = Field(
        default=...,
        title="PRODUCT_SERVICE_LINE_ITEM",
        description="Required, repeating",
    )

    PROCEDURE: list[_EHC_E01_PROCEDURE] | None = Field(
        default=None,
        title="PROCEDURE",
        description="Optional, repeating",
    )

    IPR: list[_IPR] | None = Field(
        default=None,
        title="IPR",
        description="Optional, repeating",
    )

    model_config = {"populate_by_name": True}
