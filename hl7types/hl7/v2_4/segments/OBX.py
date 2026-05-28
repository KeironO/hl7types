"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OBX
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.EI import EI
from ..datatypes.TS import TS
from ..datatypes.XCN import XCN


class OBX(BaseModel):
    """HL7 v2 OBX segment."""

    obx_1: str | None = Field(
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

    obx_2: str | None = Field(
        default=None,
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

    obx_4: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_4",
            "observation_sub_id",
            "OBX.4",
        ),
        serialization_alias="OBX.4",
        title="Observation Sub-Id",
        description="Item #572",
    )

    obx_5: list[str] | None = Field(
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

    obx_6: CE | None = Field(
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

    obx_7: str | None = Field(
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

    obx_8: str | None = Field(
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

    obx_9: list[str] | None = Field(
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

    obx_10: str | None = Field(
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
            "observation_result_status",
            "OBX.11",
        ),
        serialization_alias="OBX.11",
        title="Observation Result Status",
        description="Item #579 | Table HL70085",
    )

    obx_12: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "date_last_observation_normal_value",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Date Last Observation Normal Value",
        description="Item #580",
    )

    obx_13: str | None = Field(
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

    obx_14: TS | None = Field(
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

    obx_15: CE | None = Field(
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

    obx_16: XCN | None = Field(
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

    obx_17: list[CE] | None = Field(
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

    obx_18: list[EI] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_18",
            "equipment_instance_identifier",
            "OBX.18",
        ),
        serialization_alias="OBX.18",
        title="Equipment Instance Identifier",
        description="Item #1479",
    )

    obx_19: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_19",
            "date_time_of_the_analysis",
            "OBX.19",
        ),
        serialization_alias="OBX.19",
        title="Date/Time of the Analysis",
        description="Item #1480",
    )

    model_config = {"populate_by_name": True}
