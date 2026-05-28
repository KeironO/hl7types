"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.3
Class: OBX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class OBX(BaseModel):
    """HL7 v2 OBX segment."""

    obx_1: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_1",
            "set_id_obx",
            "OBX.1",
        ),
        serialization_alias="OBX.1",
        title="Set ID - OBX",
        description="Item #569",
    )

    obx_2: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_2",
            "value_type",
            "OBX.2",
        ),
        serialization_alias="OBX.2",
        title="Value Type",
        description="Item #570 | Table HL70125",
    )

    obx_3: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="Observation Identifier",
        description="Item #571",
    )

    obx_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="Observation Sub-ID",
        description="Item #572",
    )

    obx_5: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_5",
            "observation_value",
            "OBX.5",
        ),
        serialization_alias="OBX.5",
        title="Observation Value",
        description="Item #573",
    )

    obx_6: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="Units",
        description="Item #574",
    )

    obx_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_7",
            "references_range",
            "OBX.7",
        ),
        serialization_alias="OBX.7",
        title="References Range",
        description="Item #575",
    )

    obx_8: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "abnormal_flags",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="Abnormal Flags",
        description="Item #576 | Table HL70078",
    )

    obx_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_9",
            "probability",
            "OBX.9",
        ),
        serialization_alias="OBX.9",
        title="Probability",
        description="Item #577",
    )

    obx_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_10",
            "nature_of_abnormal_test",
            "OBX.10",
        ),
        serialization_alias="OBX.10",
        title="Nature of Abnormal Test",
        description="Item #578 | Table HL70080",
    )

    obx_11: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_11",
            "observ_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="Observ Result Status",
        description="Item #579 | Table HL70085",
    )

    obx_12: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "date_last_obs_normal_values",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Date Last Obs Normal Values",
        description="Item #580",
    )

    obx_13: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_13",
            "user_defined_access_checks",
            "OBX.13",
        ),
        serialization_alias="OBX.13",
        title="User Defined Access Checks",
        description="Item #581",
    )

    obx_14: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_14",
            "date_time_of_the_observation",
            "OBX.14",
        ),
        serialization_alias="OBX.14",
        title="Date/Time of the Observation",
        description="Item #582",
    )

    obx_15: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_15",
            "producer_s_id",
            "OBX.15",
        ),
        serialization_alias="OBX.15",
        title="Producer's ID",
        description="Item #583",
    )

    obx_16: Optional[XCN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_16",
            "responsible_observer",
            "OBX.16",
        ),
        serialization_alias="OBX.16",
        title="Responsible Observer",
        description="Item #584",
    )

    obx_17: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_17",
            "observation_method",
            "OBX.17",
        ),
        serialization_alias="OBX.17",
        title="Observation Method",
        description="Item #936",
    )

    model_config = {"populate_by_name": True}
