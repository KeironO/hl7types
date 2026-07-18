"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: RDE_O11.ORDER
Type: Group
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import ConfigDict, Field
from hl7types.hl7 import HL7Model

from ..segments.BLG import BLG
from ..segments.CDO import CDO
from ..segments.CTI import CTI
from ..segments.FT1 import FT1
from ..segments.NTE import NTE
from ..segments.ORC import ORC
from ..segments.PRT import PRT
from ..segments.RXC import RXC
from ..segments.RXE import RXE
from ..segments.RXR import RXR

from .RDE_O11_OBSERVATION import RDE_O11_OBSERVATION
from .RDE_O11_ORDER_DETAIL import RDE_O11_ORDER_DETAIL
from .RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER import RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER
from .RDE_O11_TIMING import RDE_O11_TIMING
from .RDE_O11_TIMING_ENCODED import RDE_O11_TIMING_ENCODED

_BLG = BLG
_CDO = CDO
_CTI = CTI
_FT1 = FT1
_NTE = NTE
_ORC = ORC
_PRT = PRT
_RDE_O11_OBSERVATION = RDE_O11_OBSERVATION
_RDE_O11_ORDER_DETAIL = RDE_O11_ORDER_DETAIL
_RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER = RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER
_RDE_O11_TIMING = RDE_O11_TIMING
_RDE_O11_TIMING_ENCODED = RDE_O11_TIMING_ENCODED
_RXC = RXC
_RXE = RXE
_RXR = RXR


class RDE_O11_ORDER(HL7Model):
    """HL7 v2 RDE_O11.ORDER group.

    Attributes:
        ORC (ORC): Common Order, required
        PRT (Optional[List[PRT]]): Participation Information, optional
        TIMING (Optional[List[RDE_O11_TIMING]]): optional
        ORDER_DETAIL (Optional[RDE_O11_ORDER_DETAIL]): optional
        RXE (RXE): Pharmacy/Treatment Encoded Order, required
        NTE (Optional[List[NTE]]): Notes and Comments, optional
        TIMING_ENCODED (List[RDE_O11_TIMING_ENCODED]): required
        PHARMACY_TREATMENT_INFUSION_ORDER (Optional[List[RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER]]): optional
        RXR (List[RXR]): Pharmacy/Treatment Route, required
        RXC (Optional[List[RXC]]): Pharmacy/Treatment Component Order, optional
        CDO (Optional[List[CDO]]): Cumulative Dosage, optional
        OBSERVATION (Optional[List[RDE_O11_OBSERVATION]]): optional
        FT1 (Optional[List[FT1]]): Financial Transaction, optional
        BLG (Optional[BLG]): Billing, optional
        CTI (Optional[List[CTI]]): Clinical Trial Identification, optional
    """

    ORC: _ORC = Field(
        title="ORC",
        description="Common Order",
    )

    PRT: Optional[List[_PRT]] = Field(
        default=None,
        title="PRT",
        description="Participation Information",
    )

    TIMING: Optional[List[_RDE_O11_TIMING]] = Field(
        default=None,
        title="TIMING",
    )

    ORDER_DETAIL: Optional[_RDE_O11_ORDER_DETAIL] = Field(
        default=None,
        title="ORDER_DETAIL",
    )

    RXE: _RXE = Field(
        title="RXE",
        description="Pharmacy/Treatment Encoded Order",
    )

    NTE: Optional[List[_NTE]] = Field(
        default=None,
        title="NTE",
        description="Notes and Comments",
    )

    TIMING_ENCODED: List[_RDE_O11_TIMING_ENCODED] = Field(
        min_length=1,
        title="TIMING_ENCODED",
    )

    PHARMACY_TREATMENT_INFUSION_ORDER: Optional[List[_RDE_O11_PHARMACY_TREATMENT_INFUSION_ORDER]] = Field(
        default=None,
        title="PHARMACY_TREATMENT_INFUSION_ORDER",
    )

    RXR: List[_RXR] = Field(
        min_length=1,
        title="RXR",
        description="Pharmacy/Treatment Route",
    )

    RXC: Optional[List[_RXC]] = Field(
        default=None,
        title="RXC",
        description="Pharmacy/Treatment Component Order",
    )

    CDO: Optional[List[_CDO]] = Field(
        default=None,
        title="CDO",
        description="Cumulative Dosage",
    )

    OBSERVATION: Optional[List[_RDE_O11_OBSERVATION]] = Field(
        default=None,
        title="OBSERVATION",
    )

    FT1: Optional[List[_FT1]] = Field(
        default=None,
        title="FT1",
        description="Financial Transaction",
    )

    BLG: Optional[_BLG] = Field(
        default=None,
        title="BLG",
        description="Billing",
    )

    CTI: Optional[List[_CTI]] = Field(
        default=None,
        title="CTI",
        description="Clinical Trial Identification",
    )

    model_config = ConfigDict(populate_by_name=True)
