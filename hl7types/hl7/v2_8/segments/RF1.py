"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
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
from ..datatypes.MO import MO
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class RF1(HL7Model):
    """HL7 v2 RF1 segment.

    Attributes
    ----------
    rf1_1 : CWE | None
        RF1.1 (opt) - Referral Status (CWE)

    rf1_2 : CWE | None
        RF1.2 (opt) - Referral Priority (CWE)

    rf1_3 : CWE | None
        RF1.3 (opt) - Referral Type (CWE)

    rf1_4 : list[CWE] | None
        RF1.4 (opt, rep) - Referral Disposition (CWE)

    rf1_5 : CWE | None
        RF1.5 (opt) - Referral Category (CWE)

    rf1_6 : EI
        RF1.6 (req) - Originating Referral Identifier (EI)

    rf1_7 : str | None
        RF1.7 (opt) - Effective Date (DTM)

    rf1_8 : str | None
        RF1.8 (opt) - Expiration Date (DTM)

    rf1_9 : str | None
        RF1.9 (opt) - Process Date (DTM)

    rf1_10 : list[CWE] | None
        RF1.10 (opt, rep) - Referral Reason (CWE)

    rf1_11 : list[EI] | None
        RF1.11 (opt, rep) - External Referral Identifier (EI)

    rf1_12 : CWE | None
        RF1.12 (opt) - Referral Documentation Completion Status (CWE)

    rf1_13 : str | None
        RF1.13 (opt) - Planned Treatment Stop Date (DTM)

    rf1_14 : str | None
        RF1.14 (opt) - Referral Reason Text (ST)

    rf1_15 : CQ | None
        RF1.15 (opt) - Number of Authorized Treatments/Units (CQ)

    rf1_16 : CQ | None
        RF1.16 (opt) - Number of Used Treatments/Units (CQ)

    rf1_17 : CQ | None
        RF1.17 (opt) - Number of Schedule Treatments/Units (CQ)

    rf1_18 : MO | None
        RF1.18 (opt) - Remaining Benefit Amount (MO)

    rf1_19 : XON | None
        RF1.19 (opt) - Authorized Provider (XON)

    rf1_20 : XCN | None
        RF1.20 (opt) - Authorized Health Professional (XCN)

    rf1_21 : str | None
        RF1.21 (opt) - Source Text (ST)

    rf1_22 : str | None
        RF1.22 (opt) - Source Date (DTM)

    rf1_23 : XTN | None
        RF1.23 (opt) - Source Phone (XTN)

    rf1_24 : str | None
        RF1.24 (opt) - Comment (ST)

    rf1_25 : str | None
        RF1.25 (opt) - Action Code (ID)
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
        description="Item #1137 | Table HL70283",
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
        description="Item #1138 | Table HL70280",
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
        description="Item #1139 | Table HL70281",
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
        description="Item #1140 | Table HL70282",
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
        description="Item #1141 | Table HL70284",
    )

    rf1_6: EI = Field(
        validation_alias=AliasChoices(
            "rf1_6",
            "originating_referral_identifier",
            "RF1.6",
        ),
        serialization_alias="RF1.6",
        title="Originating Referral Identifier",
        description="Item #1142",
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
        description="Item #1143",
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
        description="Item #1144",
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
        description="Item #1145",
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
        description="Item #1228 | Table HL70336",
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
        description="Item #1300",
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
        description="Item #2262 | Table HL70865",
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
        description="Item #3400",
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
        description="Item #3401",
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
        description="Item #3402",
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
        description="Item #3403",
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
        description="Item #3404",
    )

    rf1_18: Optional[MO] = Field(
        default=None,
        validation_alias=AliasChoices(
            "rf1_18",
            "remaining_benefit_amount",
            "RF1.18",
        ),
        serialization_alias="RF1.18",
        title="Remaining Benefit Amount",
        description="Item #3405",
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
        description="Item #3406",
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
        description="Item #3407",
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
        description="Item #3408",
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
        description="Item #3409",
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
        description="Item #3410",
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
        description="Item #3411",
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
        description="Item #3412 | Table HL70206",
    )

    @field_validator("rf1_7", "rf1_8", "rf1_9", "rf1_13", "rf1_22", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
