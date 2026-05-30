"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: SHP
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.TX import TX


class SHP(HL7Model):
    """HL7 v2 SHP segment.

    Attributes
    ----------
    shp_1 : EI
        SHP.1 (req) - Shipment ID (EI)

    shp_2 : list[EI] | None
        SHP.2 (opt, rep) - Internal Shipment ID (EI)

    shp_3 : CWE | None
        SHP.3 (opt) - Shipment Status (CWE)

    shp_4 : str
        SHP.4 (req) - Shipment Status Date/Time (DTM)

    shp_5 : TX | None
        SHP.5 (opt) - Shipment Status Reason (TX)

    shp_6 : CWE | None
        SHP.6 (opt) - Shipment Priority (CWE)

    shp_7 : list[CWE] | None
        SHP.7 (opt, rep) - Shipment Confidentiality (CWE)

    shp_8 : str | None
        SHP.8 (opt) - Number of Packages in Shipment (NM)

    shp_9 : list[CWE] | None
        SHP.9 (opt, rep) - Shipment Condition (CWE)

    shp_10 : list[CWE] | None
        SHP.10 (opt, rep) - Shipment Handling Code (CWE)

    shp_11 : list[CWE] | None
        SHP.11 (opt, rep) - Shipment Risk Code (CWE)
    """

    shp_1: EI = Field(
        default=...,
        validation_alias=AliasChoices(
            "shp_1",
            "shipment_id",
            "SHP.1",
        ),
        serialization_alias="SHP.1",
        title="Shipment ID",
        description="Item #2317",
    )

    shp_2: Optional[List[EI]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_2",
            "internal_shipment_id",
            "SHP.2",
        ),
        serialization_alias="SHP.2",
        title="Internal Shipment ID",
        description="Item #2318",
    )

    shp_3: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_3",
            "shipment_status",
            "SHP.3",
        ),
        serialization_alias="SHP.3",
        title="Shipment Status",
        description="Item #2319 | Table HL70905",
    )

    shp_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "shp_4",
            "shipment_status_date_time",
            "SHP.4",
        ),
        serialization_alias="SHP.4",
        title="Shipment Status Date/Time",
        description="Item #2320",
    )

    shp_5: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_5",
            "shipment_status_reason",
            "SHP.5",
        ),
        serialization_alias="SHP.5",
        title="Shipment Status Reason",
        description="Item #2321",
    )

    shp_6: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_6",
            "shipment_priority",
            "SHP.6",
        ),
        serialization_alias="SHP.6",
        title="Shipment Priority",
        description="Item #2322 | Table HL70906",
    )

    shp_7: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_7",
            "shipment_confidentiality",
            "SHP.7",
        ),
        serialization_alias="SHP.7",
        title="Shipment Confidentiality",
        description="Item #2323 | Table HL70907",
    )

    shp_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_8",
            "number_of_packages_in_shipment",
            "SHP.8",
        ),
        serialization_alias="SHP.8",
        title="Number of Packages in Shipment",
        description="Item #2324",
    )

    shp_9: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_9",
            "shipment_condition",
            "SHP.9",
        ),
        serialization_alias="SHP.9",
        title="Shipment Condition",
        description="Item #2325 | Table HL70544",
    )

    shp_10: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_10",
            "shipment_handling_code",
            "SHP.10",
        ),
        serialization_alias="SHP.10",
        title="Shipment Handling Code",
        description="Item #2326 | Table HL70376",
    )

    shp_11: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "shp_11",
            "shipment_risk_code",
            "SHP.11",
        ),
        serialization_alias="SHP.11",
        title="Shipment Risk Code",
        description="Item #2327 | Table HL70489",
    )

    model_config = {"populate_by_name": True}
