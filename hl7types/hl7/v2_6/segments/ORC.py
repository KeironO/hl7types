"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORC
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.PL import PL
from ..datatypes.TQ import TQ
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class ORC(HL7Model):
    """Common Order (S4.5.1).

    Attributes
    ----------
    orc_1 : str
        ORC.1 - Order Control (ID) R S4.5.1.1 | 0119 - Order control codes

    orc_2 : EI | None
        ORC.2 - Placer Order Number (EI) C S10.6.1.24

    orc_3 : EI | None
        ORC.3 - Filler Order Number (EI) C S10.6.1.25

    orc_4 : EI | None
        ORC.4 - Placer Group Number (EI) O S10.6.1.4

    orc_5 : str | None
        ORC.5 - Order Status (ID) O S4.5.1.5 | 0038 - Order status

    orc_6 : str | None
        ORC.6 - Response Flag (ID) O S4.5.1.6 | 0121 - Response flag

    orc_7 : list[TQ] | None
        ORC.7 - Quantity/Timing (TQ) O rep S4.14.4.1

    orc_8 : EIP | None
        ORC.8 - Parent (EIP) O S4.5.1.8

    orc_9 : str | None
        ORC.9 - Date/Time of Transaction (DTM) O S4.5.1.9

    orc_10 : list[XCN] | None
        ORC.10 - Entered By (XCN) O rep S2.14.10.5

    orc_11 : list[XCN] | None
        ORC.11 - Verified By (XCN) O rep S4.5.1.11

    orc_12 : list[XCN] | None
        ORC.12 - Ordering Provider (XCN) O rep S4.5.1.12

    orc_13 : PL | None
        ORC.13 - Enterer's Location (PL) O S4.5.1.13

    orc_14 : list[XTN] | None
        ORC.14 - Call Back Phone Number (XTN) O rep S4.5.1.14

    orc_15 : str | None
        ORC.15 - Order Effective Date/Time (DTM) O S4.5.1.15

    orc_16 : CWE | None
        ORC.16 - Order Control Code Reason (CWE) O S4.5.1.16 | 9999 - no table for CE

    orc_17 : CWE | None
        ORC.17 - Entering Organization (CWE) O S4.5.1.17 | 9999 - no table for CE

    orc_18 : CWE | None
        ORC.18 - Entering Device (CWE) O S4.5.1.18 | 9999 - no table for CE

    orc_19 : list[XCN] | None
        ORC.19 - Action By (XCN) O rep S4.5.1.19

    orc_20 : CWE | None
        ORC.20 - Advanced Beneficiary Notice Code (CWE) O S4.5.1.20 | 0339 - Advanced Beneficiary Notice Code

    orc_21 : list[XON] | None
        ORC.21 - Ordering Facility Name (XON) O rep S4.5.1.21

    orc_22 : list[XAD] | None
        ORC.22 - Ordering Facility Address (XAD) O rep S4.5.1.22

    orc_23 : list[XTN] | None
        ORC.23 - Ordering Facility Phone Number (XTN) O rep S4.5.1.23

    orc_24 : list[XAD] | None
        ORC.24 - Ordering Provider Address (XAD) O rep S4.5.1.24

    orc_25 : CWE | None
        ORC.25 - Order Status Modifier (CWE) O S4.5.1.25 | 9999 - no table for CE

    orc_26 : CWE | None
        ORC.26 - Advanced Beneficiary Notice Override Reason (CWE) C S4.5.1.26 | 0552 - Advanced beneficiary notice override reason

    orc_27 : str | None
        ORC.27 - Filler's Expected Availability Date/Time (DTM) O S4.5.1.27

    orc_28 : CWE | None
        ORC.28 - Confidentiality Code (CWE) O S4.5.1.28 | 0177 - Confidentiality code

    orc_29 : CWE | None
        ORC.29 - Order Type (CWE) O S4.5.1.29 | 0482 - Order Type

    orc_30 : CNE | None
        ORC.30 - Enterer Authorization Mode (CNE) O S4.5.1.30 | 0483 - Authorization Mode

    orc_31 : CWE | None
        ORC.31 - Parent Universal Service Identifier (CWE) O S4.5.1.31
    """

    orc_1: str = Field(
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="Order Control",
        description=(
            "R | Item #00215 | Table 0119 - Order control codes | LEN:2"
        ),
    )

    orc_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order_number",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="Placer Order Number",
        description="C | Item #00216",
    )

    orc_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_3",
            "filler_order_number",
            "ORC.3",
        ),
        serialization_alias="ORC.3",
        title="Filler Order Number",
        description="C | Item #00217",
    )

    orc_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_4",
            "placer_group_number",
            "ORC.4",
        ),
        serialization_alias="ORC.4",
        title="Placer Group Number",
        description="O | Item #00218",
    )

    orc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_5",
            "order_status",
            "ORC.5",
        ),
        serialization_alias="ORC.5",
        title="Order Status",
        description="O | Item #00219 | Table 0038 - Order status | LEN:2",
    )

    orc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_6",
            "response_flag",
            "ORC.6",
        ),
        serialization_alias="ORC.6",
        title="Response Flag",
        description="O | Item #00220 | Table 0121 - Response flag | LEN:1",
    )

    orc_7: Optional[List[TQ]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_7",
            "quantity_timing",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="Quantity/Timing",
        description="O | Item #00221",
    )

    orc_8: Optional[EIP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_8",
            "parent",
            "ORC.8",
        ),
        serialization_alias="ORC.8",
        title="Parent",
        description="O | Item #00222",
    )

    orc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_9",
            "date_time_of_transaction",
            "ORC.9",
        ),
        serialization_alias="ORC.9",
        title="Date/Time of Transaction",
        description="O | Item #00223 | LEN:24",
    )

    orc_10: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_10",
            "entered_by",
            "ORC.10",
        ),
        serialization_alias="ORC.10",
        title="Entered By",
        description="O | Item #00224",
    )

    orc_11: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_11",
            "verified_by",
            "ORC.11",
        ),
        serialization_alias="ORC.11",
        title="Verified By",
        description="O | Item #00225",
    )

    orc_12: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_12",
            "ordering_provider",
            "ORC.12",
        ),
        serialization_alias="ORC.12",
        title="Ordering Provider",
        description="O | Item #00226",
    )

    orc_13: Optional[PL] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="Enterer's Location",
        description="O | Item #00227",
    )

    orc_14: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_14",
            "call_back_phone_number",
            "ORC.14",
        ),
        serialization_alias="ORC.14",
        title="Call Back Phone Number",
        description="O | Item #00228",
    )

    orc_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_15",
            "order_effective_date_time",
            "ORC.15",
        ),
        serialization_alias="ORC.15",
        title="Order Effective Date/Time",
        description="O | Item #00229 | LEN:24",
    )

    orc_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_16",
            "order_control_code_reason",
            "ORC.16",
        ),
        serialization_alias="ORC.16",
        title="Order Control Code Reason",
        description="O | Item #00230 | Table 9999 - no table for CE",
    )

    orc_17: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_17",
            "entering_organization",
            "ORC.17",
        ),
        serialization_alias="ORC.17",
        title="Entering Organization",
        description="O | Item #00231 | Table 9999 - no table for CE",
    )

    orc_18: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_18",
            "entering_device",
            "ORC.18",
        ),
        serialization_alias="ORC.18",
        title="Entering Device",
        description="O | Item #00232 | Table 9999 - no table for CE",
    )

    orc_19: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_19",
            "action_by",
            "ORC.19",
        ),
        serialization_alias="ORC.19",
        title="Action By",
        description="O | Item #00233",
    )

    orc_20: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_20",
            "advanced_beneficiary_notice_code",
            "ORC.20",
        ),
        serialization_alias="ORC.20",
        title="Advanced Beneficiary Notice Code",
        description=(
            "O | Item #01310 | Table 0339 - Advanced Beneficiary Notice Code"
        ),
    )

    orc_21: Optional[List[XON]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_21",
            "ordering_facility_name",
            "ORC.21",
        ),
        serialization_alias="ORC.21",
        title="Ordering Facility Name",
        description="O | Item #01311",
    )

    orc_22: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_22",
            "ordering_facility_address",
            "ORC.22",
        ),
        serialization_alias="ORC.22",
        title="Ordering Facility Address",
        description="O | Item #01312",
    )

    orc_23: Optional[List[XTN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_23",
            "ordering_facility_phone_number",
            "ORC.23",
        ),
        serialization_alias="ORC.23",
        title="Ordering Facility Phone Number",
        description="O | Item #01313",
    )

    orc_24: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_24",
            "ordering_provider_address",
            "ORC.24",
        ),
        serialization_alias="ORC.24",
        title="Ordering Provider Address",
        description="O | Item #01314",
    )

    orc_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_25",
            "order_status_modifier",
            "ORC.25",
        ),
        serialization_alias="ORC.25",
        title="Order Status Modifier",
        description="O | Item #01473 | Table 9999 - no table for CE",
    )

    orc_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_26",
            "advanced_beneficiary_notice_override_reason",
            "ORC.26",
        ),
        serialization_alias="ORC.26",
        title="Advanced Beneficiary Notice Override Reason",
        description=(
            "C | Item #01641 | Table 0552 - Advanced beneficiary notice override "
            "reason"
        ),
    )

    orc_27: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_27",
            "filler_s_expected_availability_date_time",
            "ORC.27",
        ),
        serialization_alias="ORC.27",
        title="Filler's Expected Availability Date/Time",
        description="O | Item #01642 | LEN:24",
    )

    orc_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_28",
            "confidentiality_code",
            "ORC.28",
        ),
        serialization_alias="ORC.28",
        title="Confidentiality Code",
        description="O | Item #00615 | Table 0177 - Confidentiality code",
    )

    orc_29: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_29",
            "order_type",
            "ORC.29",
        ),
        serialization_alias="ORC.29",
        title="Order Type",
        description="O | Item #01643 | Table 0482 - Order Type",
    )

    orc_30: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_30",
            "enterer_authorization_mode",
            "ORC.30",
        ),
        serialization_alias="ORC.30",
        title="Enterer Authorization Mode",
        description="O | Item #01644 | Table 0483 - Authorization Mode",
    )

    orc_31: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_31",
            "parent_universal_service_identifier",
            "ORC.31",
        ),
        serialization_alias="ORC.31",
        title="Parent Universal Service Identifier",
        description="O | Item #02287",
    )

    @field_validator("orc_9", "orc_15", "orc_27", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
