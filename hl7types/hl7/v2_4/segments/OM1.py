"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.4
Class: OM1
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, field_validator
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.TS import TS
from ..datatypes.XAD import XAD
from ..datatypes.XTN import XTN

_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class OM1(HL7Model):
    """General Segment (S8.8.3).

    Attributes
    ----------
    om1_1 : str
        OM1.1 - Sequence Number - Test/ Observation Master File (NM) R S8.8.9.1

    om1_2 : CE
        OM1.2 - Producer's Service/Test/Observation ID (CE) R S8.8.3.2 | 9999 - for unknown CE data elements

    om1_3 : list[str] | None
        OM1.3 - Permitted Data Types (ID) O rep S8.8.3.3 | 0125 - Value type

    om1_4 : str
        OM1.4 - Specimen Required (ID) R S8.8.3.4 | 0136 - Yes/no indicator

    om1_5 : CE
        OM1.5 - Producer ID (CE) R S8.8.3.5 | 9999 - for unknown CE data elements

    om1_6 : str | None
        OM1.6 - Observation Description (TX) O S8.8.3.6

    om1_7 : CE | None
        OM1.7 - Other Service/Test/Observation IDs for the Observation (CE) O S8.8.3.7 | 9999 - for unknown CE data elements

    om1_8 : list[str]
        OM1.8 - Other Names (ST) R rep S8.8.3.8

    om1_9 : str | None
        OM1.9 - Preferred Report Name for the Observation (ST) O S8.8.3.9

    om1_10 : str | None
        OM1.10 - Preferred Short Name or Mnemonic for Observation (ST) O S8.8.3.10

    om1_11 : str | None
        OM1.11 - Preferred Long Name for the Observation (ST) O S8.8.3.11

    om1_12 : str | None
        OM1.12 - Orderability (ID) O S8.8.3.12 | 0136 - Yes/no indicator

    om1_13 : list[CE] | None
        OM1.13 - Identity of Instrument Used to Perform this Study (CE) O rep S8.8.3.13 | 9999 - for unknown CE data elements

    om1_14 : list[CE] | None
        OM1.14 - Coded Representation of Method (CE) O rep S8.8.3.14 | 9999 - for unknown CE data elements

    om1_15 : str | None
        OM1.15 - Portable Device Indicator (ID) O S8.8.3.15 | 0136 - Yes/no indicator

    om1_16 : list[CE] | None
        OM1.16 - Observation Producing Department/Section (CE) O rep S8.8.3.16 | 9999 - for unknown CE data elements

    om1_17 : XTN | None
        OM1.17 - Telephone Number of Section (XTN) O S8.8.3.17

    om1_18 : str
        OM1.18 - Nature of Service/Test/Observation (IS) R S8.8.3.18 | 0174 - Nature of service/test/observation

    om1_19 : CE | None
        OM1.19 - Report Subheader (CE) O S8.8.3.19 | 9999 - for unknown CE data elements

    om1_20 : str | None
        OM1.20 - Report Display Order (ST) O S8.8.3.20

    om1_21 : TS | None
        OM1.21 - Date/Time Stamp for any change in Definition for the Observation (TS) O S8.8.3.21

    om1_22 : TS | None
        OM1.22 - Effective Date/Time of Change (TS) O S8.8.9.19

    om1_23 : str | None
        OM1.23 - Typical Turn-Around Time (NM) O S8.8.3.23

    om1_24 : str | None
        OM1.24 - Processing Time (NM) O S8.8.3.24

    om1_25 : list[str] | None
        OM1.25 - Processing Priority (ID) O rep S8.8.3.25 | 0168 - Processing priority

    om1_26 : str | None
        OM1.26 - Reporting Priority (ID) O S8.8.3.26 | 0169 - Reporting priority

    om1_27 : list[CE] | None
        OM1.27 - Outside Site(s) Where Observation may be Performed (CE) O rep S8.8.3.27 | 9999 - for unknown CE data elements

    om1_28 : list[XAD] | None
        OM1.28 - Address of Outside Site(s) (XAD) O rep S8.8.3.28

    om1_29 : XTN | None
        OM1.29 - Phone Number of Outside Site (XTN) O S8.8.3.29

    om1_30 : str | None
        OM1.30 - Confidentiality Code (IS) O S8.8.3.30 | 0177 - Confidentiality code

    om1_31 : CE | None
        OM1.31 - Observations Required to Interpret the Observation (CE) O S8.8.3.31 | 9999 - for unknown CE data elements

    om1_32 : str | None
        OM1.32 - Interpretation of Observations (TX) O S8.8.3.32

    om1_33 : CE | None
        OM1.33 - Contraindications to Observations (CE) O S8.8.3.33 | 9999 - for unknown CE data elements

    om1_34 : list[CE] | None
        OM1.34 - Reflex Tests/Observations (CE) O rep S8.8.3.34 | 9999 - for unknown CE data elements

    om1_35 : str | None
        OM1.35 - Rules that Trigger Reflex Testing (TX) O S8.8.3.35

    om1_36 : CE | None
        OM1.36 - Fixed Canned Message (CE) O S8.8.3.36 | 9999 - for unknown CE data elements

    om1_37 : str | None
        OM1.37 - Patient Preparation (TX) O S8.8.3.37

    om1_38 : CE | None
        OM1.38 - Procedure Medication (CE) O S8.8.3.38 | 9999 - for unknown CE data elements

    om1_39 : str | None
        OM1.39 - Factors that may Affect Affect the Observation (TX) O S8.8.3.39

    om1_40 : list[str] | None
        OM1.40 - Service/Test/Observation Performance Schedule (ST) O rep S8.8.3.40

    om1_41 : str | None
        OM1.41 - Description of Test Methods (TX) O S8.8.3.41

    om1_42 : CE | None
        OM1.42 - Kind of Quantity Observed (CE) O S8.8.3.42 | 0254 - Kind of quantity

    om1_43 : CE | None
        OM1.43 - Point Versus Interval (CE) O S8.8.3.43 | 0255 - Duration categories

    om1_44 : str | None
        OM1.44 - Challenge Information (TX) O S8.8.3.44 | 0256 - Time delay post challenge

    om1_45 : CE | None
        OM1.45 - Relationship Modifier (CE) O S8.8.3.45 | 0258 - Relationship modifier

    om1_46 : CE | None
        OM1.46 - Target Anatomic Site Of Test (CE) O S8.8.3.46 | 9999 - for unknown CE data elements

    om1_47 : CE | None
        OM1.47 - Modality Of Imaging Measurement (CE) O S8.8.3.47 | 0259 - Modality
    """

    om1_1: str = Field(
        validation_alias=AliasChoices(
            "om1_1",
            "sequence_number_test_observation_master_file",
            "OM1.1",
        ),
        serialization_alias="OM1.1",
        title="Sequence Number - Test/ Observation Master File",
        description="R | Item #00586 | LEN:4",
    )

    om1_2: CE = Field(
        validation_alias=AliasChoices(
            "om1_2",
            "producer_s_service_test_observation_id",
            "OM1.2",
        ),
        serialization_alias="OM1.2",
        title="Producer's Service/Test/Observation ID",
        description=(
            "R | Item #00587 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_3: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_3",
            "permitted_data_types",
            "OM1.3",
        ),
        serialization_alias="OM1.3",
        title="Permitted Data Types",
        description="O | Item #00588 | Table 0125 - Value type | LEN:12",
    )

    om1_4: str = Field(
        validation_alias=AliasChoices(
            "om1_4",
            "specimen_required",
            "OM1.4",
        ),
        serialization_alias="OM1.4",
        title="Specimen Required",
        description="R | Item #00589 | Table 0136 - Yes/no indicator | LEN:1",
    )

    om1_5: CE = Field(
        validation_alias=AliasChoices(
            "om1_5",
            "producer_id",
            "OM1.5",
        ),
        serialization_alias="OM1.5",
        title="Producer ID",
        description=(
            "R | Item #00590 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_6",
            "observation_description",
            "OM1.6",
        ),
        serialization_alias="OM1.6",
        title="Observation Description",
        description="O | Item #00591",
    )

    om1_7: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_7",
            "other_service_test_observation_ids_for_the_observation",
            "OM1.7",
        ),
        serialization_alias="OM1.7",
        title="Other Service/Test/Observation IDs for the Observation",
        description=(
            "O | Item #00592 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_8: List[str] = Field(
        min_length=1,
        validation_alias=AliasChoices(
            "om1_8",
            "other_names",
            "OM1.8",
        ),
        serialization_alias="OM1.8",
        title="Other Names",
        description="R | Item #00593 | LEN:200",
    )

    om1_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_9",
            "preferred_report_name_for_the_observation",
            "OM1.9",
        ),
        serialization_alias="OM1.9",
        title="Preferred Report Name for the Observation",
        description="O | Item #00594 | LEN:30",
    )

    om1_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_10",
            "preferred_short_name_or_mnemonic_for_observation",
            "OM1.10",
        ),
        serialization_alias="OM1.10",
        title="Preferred Short Name or Mnemonic for Observation",
        description="O | Item #00595 | LEN:8",
    )

    om1_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_11",
            "preferred_long_name_for_the_observation",
            "OM1.11",
        ),
        serialization_alias="OM1.11",
        title="Preferred Long Name for the Observation",
        description="O | Item #00596 | LEN:200",
    )

    om1_12: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_12",
            "orderability",
            "OM1.12",
        ),
        serialization_alias="OM1.12",
        title="Orderability",
        description="O | Item #00597 | Table 0136 - Yes/no indicator | LEN:1",
    )

    om1_13: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_13",
            "identity_of_instrument_used_to_perform_this_study",
            "OM1.13",
        ),
        serialization_alias="OM1.13",
        title="Identity of Instrument Used to Perform this Study",
        description=(
            "O | Item #00598 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_14: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_14",
            "coded_representation_of_method",
            "OM1.14",
        ),
        serialization_alias="OM1.14",
        title="Coded Representation of Method",
        description=(
            "O | Item #00599 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_15: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_15",
            "portable_device_indicator",
            "OM1.15",
        ),
        serialization_alias="OM1.15",
        title="Portable Device Indicator",
        description="O | Item #00600 | Table 0136 - Yes/no indicator | LEN:1",
    )

    om1_16: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_16",
            "observation_producing_department_section",
            "OM1.16",
        ),
        serialization_alias="OM1.16",
        title="Observation Producing Department/Section",
        description=(
            "O | Item #00601 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_17: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_17",
            "telephone_number_of_section",
            "OM1.17",
        ),
        serialization_alias="OM1.17",
        title="Telephone Number of Section",
        description="O | Item #00602",
    )

    om1_18: str = Field(
        validation_alias=AliasChoices(
            "om1_18",
            "nature_of_service_test_observation",
            "OM1.18",
        ),
        serialization_alias="OM1.18",
        title="Nature of Service/Test/Observation",
        description=(
            "R | Item #00603 | Table 0174 - Nature of service/test/observation | "
            "LEN:1"
        ),
    )

    om1_19: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_19",
            "report_subheader",
            "OM1.19",
        ),
        serialization_alias="OM1.19",
        title="Report Subheader",
        description=(
            "O | Item #00604 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_20: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_20",
            "report_display_order",
            "OM1.20",
        ),
        serialization_alias="OM1.20",
        title="Report Display Order",
        description="O | Item #00605 | LEN:20",
    )

    om1_21: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_21",
            "date_time_stamp_for_any_change_in_definition_for_the_observation",
            "OM1.21",
        ),
        serialization_alias="OM1.21",
        title=(
            "Date/Time Stamp for any change in Definition for the Observation"
        ),
        description="O | Item #00606",
    )

    om1_22: Optional[TS] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_22",
            "effective_date_time_of_change",
            "OM1.22",
        ),
        serialization_alias="OM1.22",
        title="Effective Date/Time of Change",
        description="O | Item #00607",
    )

    om1_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_23",
            "typical_turn_around_time",
            "OM1.23",
        ),
        serialization_alias="OM1.23",
        title="Typical Turn-Around Time",
        description="O | Item #00608 | LEN:20",
    )

    om1_24: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_24",
            "processing_time",
            "OM1.24",
        ),
        serialization_alias="OM1.24",
        title="Processing Time",
        description="O | Item #00609 | LEN:20",
    )

    om1_25: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_25",
            "processing_priority",
            "OM1.25",
        ),
        serialization_alias="OM1.25",
        title="Processing Priority",
        description=(
            "O | Item #00610 | Table 0168 - Processing priority | LEN:40"
        ),
    )

    om1_26: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_26",
            "reporting_priority",
            "OM1.26",
        ),
        serialization_alias="OM1.26",
        title="Reporting Priority",
        description="O | Item #00611 | Table 0169 - Reporting priority | LEN:5",
    )

    om1_27: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_27",
            "outside_site_s_where_observation_may_be_performed",
            "OM1.27",
        ),
        serialization_alias="OM1.27",
        title="Outside Site(s) Where Observation may be Performed",
        description=(
            "O | Item #00612 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_28: Optional[List[XAD]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_28",
            "address_of_outside_site_s",
            "OM1.28",
        ),
        serialization_alias="OM1.28",
        title="Address of Outside Site(s)",
        description="O | Item #00613",
    )

    om1_29: Optional[XTN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_29",
            "phone_number_of_outside_site",
            "OM1.29",
        ),
        serialization_alias="OM1.29",
        title="Phone Number of Outside Site",
        description="O | Item #00614",
    )

    om1_30: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_30",
            "confidentiality_code",
            "OM1.30",
        ),
        serialization_alias="OM1.30",
        title="Confidentiality Code",
        description=(
            "O | Item #00615 | Table 0177 - Confidentiality code | LEN:1"
        ),
    )

    om1_31: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_31",
            "observations_required_to_interpret_the_observation",
            "OM1.31",
        ),
        serialization_alias="OM1.31",
        title="Observations Required to Interpret the Observation",
        description=(
            "O | Item #00616 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_32",
            "interpretation_of_observations",
            "OM1.32",
        ),
        serialization_alias="OM1.32",
        title="Interpretation of Observations",
        description="O | Item #00617",
    )

    om1_33: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_33",
            "contraindications_to_observations",
            "OM1.33",
        ),
        serialization_alias="OM1.33",
        title="Contraindications to Observations",
        description=(
            "O | Item #00618 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_34: Optional[List[CE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_34",
            "reflex_tests_observations",
            "OM1.34",
        ),
        serialization_alias="OM1.34",
        title="Reflex Tests/Observations",
        description=(
            "O | Item #00619 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_35: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_35",
            "rules_that_trigger_reflex_testing",
            "OM1.35",
        ),
        serialization_alias="OM1.35",
        title="Rules that Trigger Reflex Testing",
        description="O | Item #00620",
    )

    om1_36: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_36",
            "fixed_canned_message",
            "OM1.36",
        ),
        serialization_alias="OM1.36",
        title="Fixed Canned Message",
        description=(
            "O | Item #00621 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_37: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_37",
            "patient_preparation",
            "OM1.37",
        ),
        serialization_alias="OM1.37",
        title="Patient Preparation",
        description="O | Item #00622",
    )

    om1_38: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_38",
            "procedure_medication",
            "OM1.38",
        ),
        serialization_alias="OM1.38",
        title="Procedure Medication",
        description=(
            "O | Item #00623 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_39: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_39",
            "factors_that_may_affect_affect_the_observation",
            "OM1.39",
        ),
        serialization_alias="OM1.39",
        title="Factors that may Affect Affect the Observation",
        description="O | Item #00624",
    )

    om1_40: Optional[List[str]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_40",
            "service_test_observation_performance_schedule",
            "OM1.40",
        ),
        serialization_alias="OM1.40",
        title="Service/Test/Observation Performance Schedule",
        description="O | Item #00625 | LEN:60",
    )

    om1_41: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_41",
            "description_of_test_methods",
            "OM1.41",
        ),
        serialization_alias="OM1.41",
        title="Description of Test Methods",
        description="O | Item #00626",
    )

    om1_42: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_42",
            "kind_of_quantity_observed",
            "OM1.42",
        ),
        serialization_alias="OM1.42",
        title="Kind of Quantity Observed",
        description="O | Item #00937 | Table 0254 - Kind of quantity",
    )

    om1_43: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_43",
            "point_versus_interval",
            "OM1.43",
        ),
        serialization_alias="OM1.43",
        title="Point Versus Interval",
        description="O | Item #00938 | Table 0255 - Duration categories",
    )

    om1_44: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_44",
            "challenge_information",
            "OM1.44",
        ),
        serialization_alias="OM1.44",
        title="Challenge Information",
        description="O | Item #00939 | Table 0256 - Time delay post challenge",
    )

    om1_45: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_45",
            "relationship_modifier",
            "OM1.45",
        ),
        serialization_alias="OM1.45",
        title="Relationship Modifier",
        description="O | Item #00940 | Table 0258 - Relationship modifier",
    )

    om1_46: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_46",
            "target_anatomic_site_of_test",
            "OM1.46",
        ),
        serialization_alias="OM1.46",
        title="Target Anatomic Site Of Test",
        description=(
            "O | Item #00941 | Table 9999 - for unknown CE data elements"
        ),
    )

    om1_47: Optional[CE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_47",
            "modality_of_imaging_measurement",
            "OM1.47",
        ),
        serialization_alias="OM1.47",
        title="Modality Of Imaging Measurement",
        description="O | Item #00942 | Table 0259 - Modality",
    )

    @field_validator("om1_1", "om1_23", "om1_24", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
