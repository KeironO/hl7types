"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: AIP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.XCN import XCN


class AIP(HL7Model):
    """HL7 v2 AIP segment.

    Attributes
    ----------
    aip_1 : str
        AIP.1 (req) - Set ID - AIP (SI)

    aip_2 : str | None
        AIP.2 (opt) - Segment Action Code (ID)

    aip_3 : list[XCN] | None
        AIP.3 (opt, rep) - Personnel Resource ID (XCN)

    aip_4 : CWE | None
        AIP.4 (opt) - Resource Type (CWE)

    aip_5 : CWE | None
        AIP.5 (opt) - Resource Group (CWE)

    aip_6 : str | None
        AIP.6 (opt) - Start Date/Time (DTM)

    aip_7 : str | None
        AIP.7 (opt) - Start Date/Time Offset (NM)

    aip_8 : CNE | None
        AIP.8 (opt) - Start Date/Time Offset Units (CNE)

    aip_9 : str | None
        AIP.9 (opt) - Duration (NM)

    aip_10 : CNE | None
        AIP.10 (opt) - Duration Units (CNE)

    aip_11 : CWE | None
        AIP.11 (opt) - Allow Substitution Code (CWE)

    aip_12 : CWE | None
        AIP.12 (opt) - Filler Status Code (CWE)
    """

    aip_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "aip_1",
            "set_id_aip",
            "AIP.1",
        ),
        serialization_alias="AIP.1",
        title="Set ID - AIP",
        description="Item #906",
    )

    aip_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_2",
            "segment_action_code",
            "AIP.2",
        ),
        serialization_alias="AIP.2",
        title="Segment Action Code",
        description="Item #763 | Table HL70206",
    )

    aip_3: Optional[List[XCN]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_3",
            "personnel_resource_id",
            "AIP.3",
        ),
        serialization_alias="AIP.3",
        title="Personnel Resource ID",
        description="Item #913",
    )

    aip_4: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_4",
            "resource_type",
            "AIP.4",
        ),
        serialization_alias="AIP.4",
        title="Resource Type",
        description="Item #907 | Table HL70182",
    )

    aip_5: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_5",
            "resource_group",
            "AIP.5",
        ),
        serialization_alias="AIP.5",
        title="Resource Group",
        description="Item #899",
    )

    aip_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_6",
            "start_date_time",
            "AIP.6",
        ),
        serialization_alias="AIP.6",
        title="Start Date/Time",
        description="Item #1202",
    )

    aip_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_7",
            "start_date_time_offset",
            "AIP.7",
        ),
        serialization_alias="AIP.7",
        title="Start Date/Time Offset",
        description="Item #891",
    )

    aip_8: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_8",
            "start_date_time_offset_units",
            "AIP.8",
        ),
        serialization_alias="AIP.8",
        title="Start Date/Time Offset Units",
        description="Item #892",
    )

    aip_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_9",
            "duration",
            "AIP.9",
        ),
        serialization_alias="AIP.9",
        title="Duration",
        description="Item #893",
    )

    aip_10: Optional[CNE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_10",
            "duration_units",
            "AIP.10",
        ),
        serialization_alias="AIP.10",
        title="Duration Units",
        description="Item #894",
    )

    aip_11: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_11",
            "allow_substitution_code",
            "AIP.11",
        ),
        serialization_alias="AIP.11",
        title="Allow Substitution Code",
        description="Item #895 | Table HL70279",
    )

    aip_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "aip_12",
            "filler_status_code",
            "AIP.12",
        ),
        serialization_alias="AIP.12",
        title="Filler Status Code",
        description="Item #889 | Table HL70278",
    )

    model_config = {"populate_by_name": True}
