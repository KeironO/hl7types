"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.2
Class: PV2
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE

_RE_DT = re.compile(r'(\d{4}([01]\d(\d{2})?)?)?')


class PV2(HL7Model):
    """PATIENT VISIT - additional information (S3.3.4).

    Attributes
    ----------
    pv2_1 : str | None
        PV2.1 - Prior Pending Location (CM) NA S3.3.4.1

    pv2_2 : CE | None
        PV2.2 - Accommodation Code (CE) NA S3.3.4.2 | 0129 - ACCOMODATION CODE

    pv2_3 : CE | None
        PV2.3 - Admit Reason (CE) NA S3.3.4.3

    pv2_4 : CE | None
        PV2.4 - Transfer Reason (CE) NA S3.3.4.4

    pv2_5 : list[str] | None
        PV2.5 - Patient Valuables (ST) NA rep S3.3.4.5

    pv2_6 : str | None
        PV2.6 - Patient Valuables Location (ST) NA S3.3.4.6

    pv2_7 : str | None
        PV2.7 - Visit User Code (ID) NA S3.3.4.7 | 0130 - VISIT USER CODE

    pv2_8 : str | None
        PV2.8 - Expected Admit Date (DT) NA S3.3.4.8

    pv2_9 : str | None
        PV2.9 - Expected Discharge Date (DT) NA S3.3.4.9
    """

    pv2_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_1",
            "prior_pending_location",
            "PV2.1",
        ),
        serialization_alias="PV2.1",
        title="Prior Pending Location",
        description="NA | Item #00181",
    )

    pv2_2: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_2",
            "accommodation_code",
            "PV2.2",
        ),
        serialization_alias="PV2.2",
        title="Accommodation Code",
        description="NA | Item #00182 | Table 0129 - ACCOMODATION CODE",
    )

    pv2_3: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_3",
            "admit_reason",
            "PV2.3",
        ),
        serialization_alias="PV2.3",
        title="Admit Reason",
        description="NA | Item #00183",
    )

    pv2_4: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_4",
            "transfer_reason",
            "PV2.4",
        ),
        serialization_alias="PV2.4",
        title="Transfer Reason",
        description="NA | Item #00184",
    )

    pv2_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_5",
            "patient_valuables",
            "PV2.5",
        ),
        serialization_alias="PV2.5",
        title="Patient Valuables",
        description="NA | Item #00185 | LEN:25",
    )

    pv2_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_6",
            "patient_valuables_location",
            "PV2.6",
        ),
        serialization_alias="PV2.6",
        title="Patient Valuables Location",
        description="NA | Item #00186 | LEN:25",
    )

    pv2_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_7",
            "visit_user_code",
            "PV2.7",
        ),
        serialization_alias="PV2.7",
        title="Visit User Code",
        description="NA | Item #00187 | Table 0130 - VISIT USER CODE | LEN:2",
    )

    pv2_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_8",
            "expected_admit_date",
            "PV2.8",
        ),
        serialization_alias="PV2.8",
        title="Expected Admit Date",
        description="NA | Item #00188 | LEN:8",
    )

    pv2_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "pv2_9",
            "expected_discharge_date",
            "PV2.9",
        ),
        serialization_alias="PV2.9",
        title="Expected Discharge Date",
        description="NA | Item #00189 | LEN:8",
    )

    @field_validator("pv2_8", "pv2_9", mode='before')
    @classmethod
    def _validate_dt(cls, v: str) -> str:
        if not _RE_DT.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 date (YYYY[MM[DD]])")
        return v

    model_config = ConfigDict(populate_by_name=True)
