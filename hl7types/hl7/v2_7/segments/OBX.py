"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7
Class: OBX
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.varies import varies


class OBX(HL7Model):
    """HL7 v2 OBX segment.

    Attributes
    ----------
    obx_1 : str | None
        OBX.1 (opt) - Set ID - OBX (SI)

    obx_2 : str | None
        OBX.2 (opt) - Value Type (ID)

    obx_3 : CWE
        OBX.3 (req) - Observation Identifier (CWE)

    obx_4 : str | None
        OBX.4 (opt) - Observation Sub-ID (ST)

    obx_5 : list[varies] | None
        OBX.5 (opt, rep) - Observation Value (varies)

    obx_6 : CWE | None
        OBX.6 (opt) - Units (CWE)

    obx_7 : str | None
        OBX.7 (opt) - References Range (ST)

    obx_8 : list[CWE] | None
        OBX.8 (opt, rep) - Interpretation Codes (CWE)

    obx_9 : str | None
        OBX.9 (opt) - Probability (NM)

    obx_10 : list[str] | None
        OBX.10 (opt, rep) - Nature of Abnormal Test (ID)

    obx_11 : str
        OBX.11 (req) - Observation Result Status (ID)

    obx_12 : str | None
        OBX.12 (opt) - Effective Date of Reference Range (DTM)

    obx_13 : str | None
        OBX.13 (opt) - User Defined Access Checks (ST)

    obx_14 : str | None
        OBX.14 (opt) - Date/Time of the Observation (DTM)

    obx_15 : CWE | None
        OBX.15 (opt) - Producer's ID (CWE)

    obx_16 : list[XCN] | None
        OBX.16 (opt, rep) - Responsible Observer (XCN)

    obx_17 : list[CWE] | None
        OBX.17 (opt, rep) - Observation Method (CWE)

    obx_18 : list[EI] | None
        OBX.18 (opt, rep) - Equipment Instance Identifier (EI)

    obx_19 : str | None
        OBX.19 (opt) - Date/Time of the Analysis (DTM)

    obx_20 : list[CWE] | None
        OBX.20 (opt, rep) - Observation Site (CWE)

    obx_21 : EI | None
        OBX.21 (opt) - Observation Instance Identifier (EI)

    obx_22 : CNE | None
        OBX.22 (opt) - Mood Code (CNE)

    obx_23 : XON | None
        OBX.23 (opt) - Performing Organization Name (XON)

    obx_24 : XAD | None
        OBX.24 (opt) - Performing Organization Address (XAD)

    obx_25 : XCN | None
        OBX.25 (opt) - Performing Organization Medical Director (XCN)

    obx_26 : str | None
        OBX.26 (opt) - Patient Results Release Category (ID)
    """

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

    obx_2: Optional[str] = Field(
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

    obx_5: Optional[List[varies]] = Field(
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

    obx_6: Optional[CWE] = Field(
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

    obx_8: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "obx_8",
            "interpretation_codes",
            "OBX.8",
        ),
        serialization_alias="OBX.8",
        title="Interpretation Codes",
        description="Item #576",
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

    obx_10: Optional[List[str]] = Field(
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

    obx_12: Optional[str] = Field(
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

    obx_14: Optional[str] = Field(
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

    obx_15: Optional[CWE] = Field(
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

    obx_16: Optional[List[XCN]] = Field(
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

    obx_17: Optional[List[CWE]] = Field(
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

    obx_18: Optional[List[EI]] = Field(
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

    obx_19: Optional[str] = Field(
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

    obx_20: Optional[List[CWE]] = Field(
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

    obx_21: Optional[EI] = Field(
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

    obx_22: Optional[CNE] = Field(
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

    obx_23: Optional[XON] = Field(
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

    obx_24: Optional[XAD] = Field(
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

    obx_25: Optional[XCN] = Field(
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

    obx_26: Optional[str] = Field(
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

    @field_validator("obx_1", mode='before')
    @classmethod
    def _validate_si(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or a non-negative integer")
        return v

    @field_validator("obx_9", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\+|\-)?\d*\.?\d*', v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    @field_validator("obx_12", "obx_14", "obx_19", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
