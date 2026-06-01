"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: AIS
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE


class AIS(HL7Model):
    """HL7 v2 AIS segment.

    Attributes
    ----------
    ais_1 : str
        AIS.1 (req) - Set ID - AIS (SI)

    ais_2 : str | None
        AIS.2 (opt) - Segment Action Code (ID)

    ais_3 : CWE
        AIS.3 (req) - Universal Service Identifier (CWE)

    ais_4 : str | None
        AIS.4 (opt) - Start Date/Time (DTM)

    ais_5 : str | None
        AIS.5 (opt) - Start Date/Time Offset (NM)

    ais_6 : CNE | None
        AIS.6 (opt) - Start Date/Time Offset Units (CNE)

    ais_7 : str | None
        AIS.7 (opt) - Duration (NM)

    ais_8 : CNE | None
        AIS.8 (opt) - Duration Units (CNE)

    ais_9 : CWE | None
        AIS.9 (opt) - Allow Substitution Code (CWE)

    ais_10 : CWE | None
        AIS.10 (opt) - Filler Status Code (CWE)

    ais_11 : list[CWE] | None
        AIS.11 (opt, rep) - Placer Supplemental Service Information (CWE)

    ais_12 : list[CWE] | None
        AIS.12 (opt, rep) - Filler Supplemental Service Information (CWE)
    """

    ais_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "ais_1",
            "set_id_ais",
            "AIS.1",
        ),
        serialization_alias="AIS.1",
        title="Set ID - AIS",
        description="Item #890",
    )

    ais_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_2",
            "segment_action_code",
            "AIS.2",
        ),
        serialization_alias="AIS.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    ais_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "ais_3",
            "universal_service_identifier",
            "AIS.3",
        ),
        serialization_alias="AIS.3",
        title="Universal Service Identifier",
        description="Item #238",
    )

    ais_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_4",
            "start_date_time",
            "AIS.4",
        ),
        serialization_alias="AIS.4",
        title="Start Date/Time",
        description="Item #1202",
    )

    ais_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_5",
            "start_date_time_offset",
            "AIS.5",
        ),
        serialization_alias="AIS.5",
        title="Start Date/Time Offset",
        description="Item #891",
    )

    ais_6: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_6",
            "start_date_time_offset_units",
            "AIS.6",
        ),
        serialization_alias="AIS.6",
        title="Start Date/Time Offset Units",
        description="Item #892",
    )

    ais_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_7",
            "duration",
            "AIS.7",
        ),
        serialization_alias="AIS.7",
        title="Duration",
        description="Item #893",
    )

    ais_8: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_8",
            "duration_units",
            "AIS.8",
        ),
        serialization_alias="AIS.8",
        title="Duration Units",
        description="Item #894",
    )

    ais_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_9",
            "allow_substitution_code",
            "AIS.9",
        ),
        serialization_alias="AIS.9",
        title="Allow Substitution Code",
        description="Item #895 | Table HL70279",
    )

    ais_10: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_10",
            "filler_status_code",
            "AIS.10",
        ),
        serialization_alias="AIS.10",
        title="Filler Status Code",
        description="Item #889 | Table HL70278",
    )

    ais_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_11",
            "placer_supplemental_service_information",
            "AIS.11",
        ),
        serialization_alias="AIS.11",
        title="Placer Supplemental Service Information",
        description="Item #1474 | Table HL70411",
    )

    ais_12: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ais_12",
            "filler_supplemental_service_information",
            "AIS.12",
        ),
        serialization_alias="AIS.12",
        title="Filler Supplemental Service Information",
        description="Item #1475 | Table HL70411",
    )

    @field_validator("ais_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("ais_4", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    @field_validator("ais_5", "ais_7", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = {"populate_by_name": True}
