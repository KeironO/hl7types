"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: RF1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CQ import CQ
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class RF1(HL7Model):
    """Referral Information (S11.8.1).

    Attributes
    ----------
    rf1_1 : CWE | None
        RF1.1 - Referral Status (CWE) O S11.8.1.1 | 0283 - Referral Status

    rf1_2 : CWE | None
        RF1.2 - Referral Priority (CWE) O S11.8.1.2 | 0280 - Referral Priority

    rf1_3 : CWE | None
        RF1.3 - Referral Type (CWE) O S11.8.1.3 | 0281 - Referral Type

    rf1_4 : list[CWE] | None
        RF1.4 - Referral Disposition (CWE) O rep S11.8.1.4 | 0282 - Referral Disposition

    rf1_5 : CWE | None
        RF1.5 - Referral Category (CWE) O S11.8.1.5 | 0284 - Referral Category

    rf1_6 : EI
        RF1.6 - Originating Referral Identifier (EI) R S11.8.1.6

    rf1_7 : str | None
        RF1.7 - Effective Date (DTM) O S11.8.1.7

    rf1_8 : str | None
        RF1.8 - Expiration Date (DTM) O S11.8.1.8

    rf1_9 : str | None
        RF1.9 - Process Date (DTM) O S11.8.1.9

    rf1_10 : list[CWE] | None
        RF1.10 - Referral Reason (CWE) O rep S11.8.1.10 | 0336 - Referral Reason

    rf1_11 : list[EI] | None
        RF1.11 - External Referral Identifier (EI) O rep S11.8.1.11

    rf1_12 : CWE | None
        RF1.12 - Referral Documentation Completion Status (CWE) O S11.8.1.12 | 0865 - Referral Documentation Completion Status

    rf1_13 : str | None
        RF1.13 - Planned Treatment Stop Date (DTM) O S11.8.1.13

    rf1_14 : str | None
        RF1.14 - Referral Reason Text (ST) O S11.8.1.14

    rf1_15 : CQ | None
        RF1.15 - Number of Authorized Treatments/Units (CQ) O S11.8.1.15

    rf1_16 : CQ | None
        RF1.16 - Number of Used Treatments/Units (CQ) O S11.8.1.16

    rf1_17 : CQ | None
        RF1.17 - Number of Schedule Treatments/Units (CQ) O S11.8.1.17

    rf1_19 : XON | None
        RF1.19 - Authorized Provider (XON) O S11.8.1.19

    rf1_20 : XCN | None
        RF1.20 - Authorized Health Professional (XCN) O S11.8.1.20

    rf1_21 : str | None
        RF1.21 - Source Text (ST) O S11.8.1.21

    rf1_22 : str | None
        RF1.22 - Source Date (DTM) O S11.8.1.22

    rf1_23 : XTN | None
        RF1.23 - Source Phone (XTN) O S11.8.1.23

    rf1_24 : str | None
        RF1.24 - Comment (ST) O S11.8.1.24

    rf1_25 : str | None
        RF1.25 - Action Code (ID) O S11.8.1.25 | 0206 - Segment Action Code
    """

    rf1_1: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_1",
            "referral_status",
            "RF1.1",
        ),
        serialization_alias="RF1.1",
        title="Referral Status",
        description="O | Item #01137 | Table 0283 - Referral Status",
    )

    rf1_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_2",
            "referral_priority",
            "RF1.2",
        ),
        serialization_alias="RF1.2",
        title="Referral Priority",
        description="O | Item #01138 | Table 0280 - Referral Priority",
    )

    rf1_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_3",
            "referral_type",
            "RF1.3",
        ),
        serialization_alias="RF1.3",
        title="Referral Type",
        description="O | Item #01139 | Table 0281 - Referral Type",
    )

    rf1_4: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_4",
            "referral_disposition",
            "RF1.4",
        ),
        serialization_alias="RF1.4",
        title="Referral Disposition",
        description="O | Item #01140 | Table 0282 - Referral Disposition",
    )

    rf1_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_5",
            "referral_category",
            "RF1.5",
        ),
        serialization_alias="RF1.5",
        title="Referral Category",
        description="O | Item #01141 | Table 0284 - Referral Category",
    )

    rf1_6: EI = Field(
        validation_alias=AliasChoices(
            "rf1_6",
            "originating_referral_identifier",
            "RF1.6",
        ),
        serialization_alias="RF1.6",
        title="Originating Referral Identifier",
        description="R | Item #01142",
    )

    rf1_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_7",
            "effective_date",
            "RF1.7",
        ),
        serialization_alias="RF1.7",
        title="Effective Date",
        description="O | Item #01143",
    )

    rf1_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_8",
            "expiration_date",
            "RF1.8",
        ),
        serialization_alias="RF1.8",
        title="Expiration Date",
        description="O | Item #01144",
    )

    rf1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_9",
            "process_date",
            "RF1.9",
        ),
        serialization_alias="RF1.9",
        title="Process Date",
        description="O | Item #01145",
    )

    rf1_10: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_10",
            "referral_reason",
            "RF1.10",
        ),
        serialization_alias="RF1.10",
        title="Referral Reason",
        description="O | Item #01228 | Table 0336 - Referral Reason",
    )

    rf1_11: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_11",
            "external_referral_identifier",
            "RF1.11",
        ),
        serialization_alias="RF1.11",
        title="External Referral Identifier",
        description="O | Item #01300",
    )

    rf1_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_12",
            "referral_documentation_completion_status",
            "RF1.12",
        ),
        serialization_alias="RF1.12",
        title="Referral Documentation Completion Status",
        description=(
            "O | Item #02262 | Table 0865 - Referral Documentation Completion "
            "Status"
        ),
    )

    rf1_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_13",
            "planned_treatment_stop_date",
            "RF1.13",
        ),
        serialization_alias="RF1.13",
        title="Planned Treatment Stop Date",
        description="O | Item #03400 | LEN:24",
    )

    rf1_14: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_14",
            "referral_reason_text",
            "RF1.14",
        ),
        serialization_alias="RF1.14",
        title="Referral Reason Text",
        description="O | Item #03401 | LEN:60",
    )

    rf1_15: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_15",
            "number_of_authorized_treatments_units",
            "RF1.15",
        ),
        serialization_alias="RF1.15",
        title="Number of Authorized Treatments/Units",
        description="O | Item #03402",
    )

    rf1_16: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_16",
            "number_of_used_treatments_units",
            "RF1.16",
        ),
        serialization_alias="RF1.16",
        title="Number of Used Treatments/Units",
        description="O | Item #03403",
    )

    rf1_17: Optional[CQ] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_17",
            "number_of_schedule_treatments_units",
            "RF1.17",
        ),
        serialization_alias="RF1.17",
        title="Number of Schedule Treatments/Units",
        description="O | Item #03404",
    )

    rf1_19: Optional[XON] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_19",
            "authorized_provider",
            "RF1.19",
        ),
        serialization_alias="RF1.19",
        title="Authorized Provider",
        description="O | Item #03406",
    )

    rf1_20: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_20",
            "authorized_health_professional",
            "RF1.20",
        ),
        serialization_alias="RF1.20",
        title="Authorized Health Professional",
        description="O | Item #03407",
    )

    rf1_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_21",
            "source_text",
            "RF1.21",
        ),
        serialization_alias="RF1.21",
        title="Source Text",
        description="O | Item #03408 | LEN:60",
    )

    rf1_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_22",
            "source_date",
            "RF1.22",
        ),
        serialization_alias="RF1.22",
        title="Source Date",
        description="O | Item #03409 | LEN:24",
    )

    rf1_23: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_23",
            "source_phone",
            "RF1.23",
        ),
        serialization_alias="RF1.23",
        title="Source Phone",
        description="O | Item #03410",
    )

    rf1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_24",
            "comment",
            "RF1.24",
        ),
        serialization_alias="RF1.24",
        title="Comment",
        description="O | Item #03411 | LEN:250",
    )

    rf1_25: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_25",
            "action_code",
            "RF1.25",
        ),
        serialization_alias="RF1.25",
        title="Action Code",
        description=(
            "O | Item #03412 | Table 0206 - Segment Action Code | LEN:1"
        ),
    )

    @field_validator("rf1_7", "rf1_8", "rf1_9", "rf1_13", "rf1_22", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        import re
        if re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    model_config = {"populate_by_name": True}
