"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.1
Class: OBX
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.varies import varies
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON


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

    obx_3: CWE = Field(
        default=...,
        validation_alias=AliasChoices(
            "obx_3",
            "observation_identifier",
            "OBX.3",
        ),
        serialization_alias="OBX.3",
        title="Observation Identifier",
        description="Item #571 | Table HL79999",
    )

    obx_4: str | None = Field(
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

    obx_5: list[varies] | None = Field(
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

    obx_6: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_6",
            "units",
            "OBX.6",
        ),
        serialization_alias="OBX.6",
        title="Units",
        description="Item #574 | Table HL79999",
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

    obx_8: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "interpretation_codes",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="Interpretation Codes",
        description="Item #576 | Table HL70078",
    )

    obx_9: str | None = Field(
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

    obx_10: list[str] | None = Field(
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

    obx_12: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_12",
            "effective_date_of_reference_range",
            "OBX.12",
        ),
        serialization_alias="OBX.12",
        title="Effective Date of Reference Range",
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

    obx_14: str | None = Field(
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

    obx_15: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_15",
            "producer_s_id",
            "OBX.15",
        ),
        serialization_alias="OBX.15",
        title="Producer's ID",
        description="Item #583 | Table HL79999",
    )

    obx_16: list[XCN] | None = Field(
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

    obx_17: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_17",
            "observation_method",
            "OBX.17",
        ),
        serialization_alias="OBX.17",
        title="Observation Method",
        description="Item #936 | Table HL79999",
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

    obx_19: str | None = Field(
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

    obx_20: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_20",
            "observation_site",
            "OBX.20",
        ),
        serialization_alias="OBX.20",
        title="Observation Site",
        description="Item #2179 | Table HL70163",
    )

    obx_21: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_21",
            "observation_instance_identifier",
            "OBX.21",
        ),
        serialization_alias="OBX.21",
        title="Observation Instance Identifier",
        description="Item #2180",
    )

    obx_22: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_22",
            "mood_code",
            "OBX.22",
        ),
        serialization_alias="OBX.22",
        title="Mood Code",
        description="Item #2182 | Table HL70725",
    )

    obx_23: XON | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_23",
            "performing_organization_name",
            "OBX.23",
        ),
        serialization_alias="OBX.23",
        title="Performing Organization Name",
        description="Item #2283",
    )

    obx_24: XAD | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_24",
            "performing_organization_address",
            "OBX.24",
        ),
        serialization_alias="OBX.24",
        title="Performing Organization Address",
        description="Item #2284",
    )

    obx_25: XCN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_25",
            "performing_organization_medical_director",
            "OBX.25",
        ),
        serialization_alias="OBX.25",
        title="Performing Organization Medical Director",
        description="Item #2285",
    )

    obx_26: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_26",
            "patient_results_release_category",
            "OBX.26",
        ),
        serialization_alias="OBX.26",
        title="Patient Results Release Category",
        description="Item #2313 | Table HL70909",
    )

    obx_27: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_27",
            "root_cause",
            "OBX.27",
        ),
        serialization_alias="OBX.27",
        title="Root Cause",
        description="Item #3308 | Table HL70914",
    )

    obx_28: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_28",
            "local_process_control",
            "OBX.28",
        ),
        serialization_alias="OBX.28",
        title="Local Process Control",
        description="Item #3309 | Table HL70915",
    )

    obx_29: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_29",
            "observation_type",
            "OBX.29",
        ),
        serialization_alias="OBX.29",
        title="Observation Type",
        description="Item #3432 | Table HL70936",
    )

    model_config = {"populate_by_name": True}
