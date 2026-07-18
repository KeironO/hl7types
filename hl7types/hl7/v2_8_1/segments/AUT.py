"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: AUT
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CP import CP
from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.MO import MO
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')


class AUT(HL7Model):
    """Authorization Information (S11.8.2).

    Attributes
    ----------
    aut_1 : CWE | None
        AUT.1 - Authorizing Payor, Plan ID (CWE) O S11.8.2.1 | 0072 - Insurance Plan ID

    aut_2 : CWE
        AUT.2 - Authorizing Payor, Company ID (CWE) R S11.8.2.2 | 0285 - Insurance Company ID Codes

    aut_3 : str | None
        AUT.3 - Authorizing Payor, Company Name (ST) O S11.8.2.3

    aut_4 : str | None
        AUT.4 - Authorization Effective Date (DTM) O S11.8.2.4

    aut_5 : str | None
        AUT.5 - Authorization Expiration Date (DTM) O S11.8.2.5

    aut_6 : EI | None
        AUT.6 - Authorization Identifier (EI) C S11.8.2.6

    aut_7 : CP | None
        AUT.7 - Reimbursement Limit (CP) O S11.8.2.7

    aut_8 : CQ | None
        AUT.8 - Requested Number of Treatments (CQ) O S11.8.2.8

    aut_9 : CQ | None
        AUT.9 - Authorized Number of Treatments (CQ) O S11.8.2.9

    aut_10 : str | None
        AUT.10 - Process Date (DTM) O S11.8.1.9

    aut_11 : list[CWE] | None
        AUT.11 - Requested Discipline(s) (CWE) O rep S11.8.2.11

    aut_12 : list[CWE] | None
        AUT.12 - Authorized Discipline(s) (CWE) O rep S11.8.2.12

    aut_13 : CWE
        AUT.13 - Authorization Referral Type (CWE) R S11.8.2.13

    aut_14 : CWE | None
        AUT.14 - Approval Status (CWE) O S11.8.2.14

    aut_15 : str | None
        AUT.15 - Planned Treatment Stop Date (DTM) O S11.8.2.15

    aut_16 : CWE | None
        AUT.16 - Clinical Service (CWE) O S11.8.2.16

    aut_17 : str | None
        AUT.17 - Reason Text (ST) O S11.8.2.17

    aut_18 : CQ | None
        AUT.18 - Number of Authorized Treatments/Units (CQ) O S11.8.2.18

    aut_19 : CQ | None
        AUT.19 - Number of Used Treatments/Units (CQ) O S11.8.2.19

    aut_20 : CQ | None
        AUT.20 - Number of Schedule Treatments/Units (CQ) O S11.8.2.20

    aut_21 : CWE | None
        AUT.21 - Encounter Type (CWE) O S11.8.2.21

    aut_22 : MO | None
        AUT.22 - Remaining Benefit Amount (MO) O S11.8.2.22

    aut_23 : XON | None
        AUT.23 - Authorized Provider (XON) O S11.8.2.23

    aut_24 : XCN | None
        AUT.24 - Authorized Health Professional (XCN) O S11.8.2.24

    aut_25 : str | None
        AUT.25 - Source Text (ST) O S11.8.2.25

    aut_26 : str | None
        AUT.26 - Source Date (DTM) O S11.8.2.26

    aut_27 : XTN | None
        AUT.27 - Source Phone (XTN) O S11.8.2.27

    aut_28 : str | None
        AUT.28 - Comment (ST) O S11.8.2.28

    aut_29 : str | None
        AUT.29 - Action Code (ID) O S11.8.2.29 | 0206 - Segment Action Code
    """

    aut_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_1",
            "authorizing_payor_plan_id",
            "AUT.1",
        ),
        serialization_alias="AUT.1",
        title="Authorizing Payor, Plan ID",
        description="O | Item #01146 | Table 0072 - Insurance Plan ID",
    )

    aut_2: CWE = Field(
        validation_alias=AliasChoices(
            "aut_2",
            "authorizing_payor_company_id",
            "AUT.2",
        ),
        serialization_alias="AUT.2",
        title="Authorizing Payor, Company ID",
        description="R | Item #01147 | Table 0285 - Insurance Company ID Codes",
    )

    aut_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_3",
            "authorizing_payor_company_name",
            "AUT.3",
        ),
        serialization_alias="AUT.3",
        title="Authorizing Payor, Company Name",
        description="O | Item #01148",
    )

    aut_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_4",
            "authorization_effective_date",
            "AUT.4",
        ),
        serialization_alias="AUT.4",
        title="Authorization Effective Date",
        description="O | Item #01149",
    )

    aut_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_5",
            "authorization_expiration_date",
            "AUT.5",
        ),
        serialization_alias="AUT.5",
        title="Authorization Expiration Date",
        description="O | Item #01150",
    )

    aut_6: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_6",
            "authorization_identifier",
            "AUT.6",
        ),
        serialization_alias="AUT.6",
        title="Authorization Identifier",
        description="C | Item #01151",
    )

    aut_7: Optional[CP] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_7",
            "reimbursement_limit",
            "AUT.7",
        ),
        serialization_alias="AUT.7",
        title="Reimbursement Limit",
        description="O | Item #01152",
    )

    aut_8: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_8",
            "requested_number_of_treatments",
            "AUT.8",
        ),
        serialization_alias="AUT.8",
        title="Requested Number of Treatments",
        description="O | Item #01153",
    )

    aut_9: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_9",
            "authorized_number_of_treatments",
            "AUT.9",
        ),
        serialization_alias="AUT.9",
        title="Authorized Number of Treatments",
        description="O | Item #01154",
    )

    aut_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_10",
            "process_date",
            "AUT.10",
        ),
        serialization_alias="AUT.10",
        title="Process Date",
        description="O | Item #01145",
    )

    aut_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_11",
            "requested_discipline_s",
            "AUT.11",
        ),
        serialization_alias="AUT.11",
        title="Requested Discipline(s)",
        description="O | Item #02375",
    )

    aut_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_12",
            "authorized_discipline_s",
            "AUT.12",
        ),
        serialization_alias="AUT.12",
        title="Authorized Discipline(s)",
        description="O | Item #02376",
    )

    aut_13: CWE = Field(
        validation_alias=AliasChoices(
            "aut_13",
            "authorization_referral_type",
            "AUT.13",
        ),
        serialization_alias="AUT.13",
        title="Authorization Referral Type",
        description="R | Item #03413",
    )

    aut_14: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_14",
            "approval_status",
            "AUT.14",
        ),
        serialization_alias="AUT.14",
        title="Approval Status",
        description="O | Item #03414",
    )

    aut_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_15",
            "planned_treatment_stop_date",
            "AUT.15",
        ),
        serialization_alias="AUT.15",
        title="Planned Treatment Stop Date",
        description="O | Item #03415 | LEN:24",
    )

    aut_16: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_16",
            "clinical_service",
            "AUT.16",
        ),
        serialization_alias="AUT.16",
        title="Clinical Service",
        description="O | Item #03416",
    )

    aut_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_17",
            "reason_text",
            "AUT.17",
        ),
        serialization_alias="AUT.17",
        title="Reason Text",
        description="O | Item #03417 | LEN:60",
    )

    aut_18: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_18",
            "number_of_authorized_treatments_units",
            "AUT.18",
        ),
        serialization_alias="AUT.18",
        title="Number of Authorized Treatments/Units",
        description="O | Item #03418",
    )

    aut_19: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_19",
            "number_of_used_treatments_units",
            "AUT.19",
        ),
        serialization_alias="AUT.19",
        title="Number of Used Treatments/Units",
        description="O | Item #03419",
    )

    aut_20: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_20",
            "number_of_schedule_treatments_units",
            "AUT.20",
        ),
        serialization_alias="AUT.20",
        title="Number of Schedule Treatments/Units",
        description="O | Item #03420",
    )

    aut_21: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_21",
            "encounter_type",
            "AUT.21",
        ),
        serialization_alias="AUT.21",
        title="Encounter Type",
        description="O | Item #03421",
    )

    aut_22: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_22",
            "remaining_benefit_amount",
            "AUT.22",
        ),
        serialization_alias="AUT.22",
        title="Remaining Benefit Amount",
        description="O | Item #03422",
    )

    aut_23: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_23",
            "authorized_provider",
            "AUT.23",
        ),
        serialization_alias="AUT.23",
        title="Authorized Provider",
        description="O | Item #03423",
    )

    aut_24: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_24",
            "authorized_health_professional",
            "AUT.24",
        ),
        serialization_alias="AUT.24",
        title="Authorized Health Professional",
        description="O | Item #03424",
    )

    aut_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_25",
            "source_text",
            "AUT.25",
        ),
        serialization_alias="AUT.25",
        title="Source Text",
        description="O | Item #03425 | LEN:60",
    )

    aut_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_26",
            "source_date",
            "AUT.26",
        ),
        serialization_alias="AUT.26",
        title="Source Date",
        description="O | Item #03426 | LEN:24",
    )

    aut_27: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_27",
            "source_phone",
            "AUT.27",
        ),
        serialization_alias="AUT.27",
        title="Source Phone",
        description="O | Item #03427",
    )

    aut_28: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_28",
            "comment",
            "AUT.28",
        ),
        serialization_alias="AUT.28",
        title="Comment",
        description="O | Item #03428 | LEN:254",
    )

    aut_29: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aut_29",
            "action_code",
            "AUT.29",
        ),
        serialization_alias="AUT.29",
        title="Action Code",
        description=(
            "O | Item #03429 | Table 0206 - Segment Action Code | LEN:1"
        ),
    )

    @field_validator("aut_4", "aut_5", "aut_10", "aut_15", "aut_26", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = ConfigDict(populate_by_name=True)
