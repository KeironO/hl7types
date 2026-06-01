"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8
Class: ACC
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN


class ACC(HL7Model):
    """HL7 v2 ACC segment.

    Attributes
    ----------
    acc_1 : str | None
        ACC.1 (opt) - Accident Date/Time (DTM)

    acc_2 : CWE | None
        ACC.2 (opt) - Accident Code (CWE)

    acc_3 : str | None
        ACC.3 (opt) - Accident Location (ST)

    acc_4 : CWE | None
        ACC.4 (opt) - Auto Accident State (CWE)

    acc_5 : str | None
        ACC.5 (opt) - Accident Job Related Indicator (ID)

    acc_6 : str | None
        ACC.6 (opt) - Accident Death Indicator (ID)

    acc_7 : XCN | None
        ACC.7 (opt) - Entered By (XCN)

    acc_8 : str | None
        ACC.8 (opt) - Accident Description (ST)

    acc_9 : str | None
        ACC.9 (opt) - Brought In By (ST)

    acc_10 : str | None
        ACC.10 (opt) - Police Notified Indicator (ID)

    acc_11 : XAD | None
        ACC.11 (opt) - Accident Address (XAD)

    acc_12 : str | None
        ACC.12 (opt) - Degree of patient liability (NM)

    acc_13 : list[EI] | None
        ACC.13 (opt, rep) - Accident Identifier (EI)
    """

    acc_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_1",
            "accident_date_time",
            "ACC.1",
        ),
        serialization_alias="ACC.1",
        title="Accident Date/Time",
        description="Item #527",
    )

    acc_2: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_2",
            "accident_code",
            "ACC.2",
        ),
        serialization_alias="ACC.2",
        title="Accident Code",
        description="Item #528 | Table HL70050",
    )

    acc_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_3",
            "accident_location",
            "ACC.3",
        ),
        serialization_alias="ACC.3",
        title="Accident Location",
        description="Item #529",
    )

    acc_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_4",
            "auto_accident_state",
            "ACC.4",
        ),
        serialization_alias="ACC.4",
        title="Auto Accident State",
        description="Item #812 | Table HL70347",
    )

    acc_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_5",
            "accident_job_related_indicator",
            "ACC.5",
        ),
        serialization_alias="ACC.5",
        title="Accident Job Related Indicator",
        description="Item #813 | Table HL70136",
    )

    acc_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_6",
            "accident_death_indicator",
            "ACC.6",
        ),
        serialization_alias="ACC.6",
        title="Accident Death Indicator",
        description="Item #814 | Table HL70136",
    )

    acc_7: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_7",
            "entered_by",
            "ACC.7",
        ),
        serialization_alias="ACC.7",
        title="Entered By",
        description="Item #224",
    )

    acc_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_8",
            "accident_description",
            "ACC.8",
        ),
        serialization_alias="ACC.8",
        title="Accident Description",
        description="Item #1503",
    )

    acc_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_9",
            "brought_in_by",
            "ACC.9",
        ),
        serialization_alias="ACC.9",
        title="Brought In By",
        description="Item #1504",
    )

    acc_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_10",
            "police_notified_indicator",
            "ACC.10",
        ),
        serialization_alias="ACC.10",
        title="Police Notified Indicator",
        description="Item #1505 | Table HL70136",
    )

    acc_11: Optional[XAD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_11",
            "accident_address",
            "ACC.11",
        ),
        serialization_alias="ACC.11",
        title="Accident Address",
        description="Item #1853",
    )

    acc_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_12",
            "degree_of_patient_liability",
            "ACC.12",
        ),
        serialization_alias="ACC.12",
        title="Degree of patient liability",
        description="Item #2374",
    )

    acc_13: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "acc_13",
            "accident_identifier",
            "ACC.13",
        ),
        serialization_alias="ACC.13",
        title="Accident Identifier",
        description="Item #3338",
    )

    @field_validator("acc_1", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("acc_12", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
