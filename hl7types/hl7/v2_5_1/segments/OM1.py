"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5.1
Class: OM1
Type: Segment
"""
from __future__ import annotations

from typing import Optional, List
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.TS import TS
from ..datatypes.TX import TX
from ..datatypes.XAD import XAD
from ..datatypes.XTN import XTN


class OM1(HL7Model):
    """HL7 v2 OM1 segment.

    Attributes
    ----------
    om1_1 : str
        OM1.1 (req) - Sequence Number - Test/Observation Master File (NM)

    om1_2 : CE
        OM1.2 (req) - Producer's Service/Test/Observation ID (CE)

    om1_3 : list[str] | None
        OM1.3 (opt, rep) - Permitted Data Types (ID)

    om1_4 : str
        OM1.4 (req) - Specimen Required (ID)

    om1_5 : CE
        OM1.5 (req) - Producer ID (CE)

    om1_6 : TX | None
        OM1.6 (opt) - Observation Description (TX)

    om1_7 : CE | None
        OM1.7 (opt) - Other Service/Test/Observation IDs for the Observation (CE)

    om1_8 : list[str]
        OM1.8 (req, rep) - Other Names (ST)

    om1_9 : str | None
        OM1.9 (opt) - Preferred Report Name for the Observation (ST)

    om1_10 : str | None
        OM1.10 (opt) - Preferred Short Name or Mnemonic for Observation (ST)

    om1_11 : str | None
        OM1.11 (opt) - Preferred Long Name for the Observation (ST)

    om1_12 : str | None
        OM1.12 (opt) - Orderability (ID)

    om1_13 : list[CE] | None
        OM1.13 (opt, rep) - Identity of Instrument Used to Perform this Study (CE)

    om1_14 : list[CE] | None
        OM1.14 (opt, rep) - Coded Representation of Method (CE)

    om1_15 : str | None
        OM1.15 (opt) - Portable Device Indicator (ID)

    om1_16 : list[CE] | None
        OM1.16 (opt, rep) - Observation Producing Department/Section (CE)

    om1_17 : XTN | None
        OM1.17 (opt) - Telephone Number of Section (XTN)

    om1_18 : str
        OM1.18 (req) - Nature of Service/Test/Observation (IS)

    om1_19 : CE | None
        OM1.19 (opt) - Report Subheader (CE)

    om1_20 : str | None
        OM1.20 (opt) - Report Display Order (ST)

    om1_21 : TS | None
        OM1.21 (opt) - Date/Time Stamp for any change in Definition for the Observation (TS)

    om1_22 : TS | None
        OM1.22 (opt) - Effective Date/Time of Change (TS)

    om1_23 : str | None
        OM1.23 (opt) - Typical Turn-Around Time (NM)

    om1_24 : str | None
        OM1.24 (opt) - Processing Time (NM)

    om1_25 : list[str] | None
        OM1.25 (opt, rep) - Processing Priority (ID)

    om1_26 : str | None
        OM1.26 (opt) - Reporting Priority (ID)

    om1_27 : list[CE] | None
        OM1.27 (opt, rep) - Outside Site(s) Where Observation may be Performed (CE)

    om1_28 : list[XAD] | None
        OM1.28 (opt, rep) - Address of Outside Site(s) (XAD)

    om1_29 : XTN | None
        OM1.29 (opt) - Phone Number of Outside Site (XTN)

    om1_30 : CWE | None
        OM1.30 (opt) - Confidentiality Code (CWE)

    om1_31 : CE | None
        OM1.31 (opt) - Observations Required to Interpret the Observation (CE)

    om1_32 : TX | None
        OM1.32 (opt) - Interpretation of Observations (TX)

    om1_33 : CE | None
        OM1.33 (opt) - Contraindications to Observations (CE)

    om1_34 : list[CE] | None
        OM1.34 (opt, rep) - Reflex Tests/Observations (CE)

    om1_35 : TX | None
        OM1.35 (opt) - Rules that Trigger Reflex Testing (TX)

    om1_36 : CE | None
        OM1.36 (opt) - Fixed Canned Message (CE)

    om1_37 : TX | None
        OM1.37 (opt) - Patient Preparation (TX)

    om1_38 : CE | None
        OM1.38 (opt) - Procedure Medication (CE)

    om1_39 : TX | None
        OM1.39 (opt) - Factors that may Affect the Observation (TX)

    om1_40 : list[str] | None
        OM1.40 (opt, rep) - Service/Test/Observation Performance Schedule (ST)

    om1_41 : TX | None
        OM1.41 (opt) - Description of Test Methods (TX)

    om1_42 : CE | None
        OM1.42 (opt) - Kind of Quantity Observed (CE)

    om1_43 : CE | None
        OM1.43 (opt) - Point Versus Interval (CE)

    om1_44 : TX | None
        OM1.44 (opt) - Challenge Information (TX)

    om1_45 : CE | None
        OM1.45 (opt) - Relationship Modifier (CE)

    om1_46 : CE | None
        OM1.46 (opt) - Target Anatomic Site Of Test (CE)

    om1_47 : CE | None
        OM1.47 (opt) - Modality Of Imaging Measurement (CE)
    """

    om1_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_1",
            "sequence_number_test_observation_master_file",
            "OM1.1",
        ),
        serialization_alias="OM1.1",
        title="Sequence Number - Test/Observation Master File",
        description="Item #586",
    )

    om1_2: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_2",
            "producer_s_service_test_observation_id",
            "OM1.2",
        ),
        serialization_alias="OM1.2",
        title="Producer's Service/Test/Observation ID",
        description="Item #587 | Table HL79999",
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
        description="Item #588 | Table HL70125",
    )

    om1_4: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_4",
            "specimen_required",
            "OM1.4",
        ),
        serialization_alias="OM1.4",
        title="Specimen Required",
        description="Item #589 | Table HL70136",
    )

    om1_5: CE = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_5",
            "producer_id",
            "OM1.5",
        ),
        serialization_alias="OM1.5",
        title="Producer ID",
        description="Item #590 | Table HL79999",
    )

    om1_6: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_6",
            "observation_description",
            "OM1.6",
        ),
        serialization_alias="OM1.6",
        title="Observation Description",
        description="Item #591",
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
        description="Item #592 | Table HL79999",
    )

    om1_8: List[str] = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_8",
            "other_names",
            "OM1.8",
        ),
        serialization_alias="OM1.8",
        title="Other Names",
        description="Item #593",
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
        description="Item #594",
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
        description="Item #595",
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
        description="Item #596",
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
        description="Item #597 | Table HL70136",
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
        description="Item #598 | Table HL79999",
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
        description="Item #599 | Table HL79999",
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
        description="Item #600 | Table HL70136",
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
        description="Item #601 | Table HL79999",
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
        description="Item #602",
    )

    om1_18: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "om1_18",
            "nature_of_service_test_observation",
            "OM1.18",
        ),
        serialization_alias="OM1.18",
        title="Nature of Service/Test/Observation",
        description="Item #603 | Table HL70174",
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
        description="Item #604 | Table HL79999",
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
        description="Item #605",
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
        description="Item #606",
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
        description="Item #607",
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
        description="Item #608",
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
        description="Item #609",
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
        description="Item #610 | Table HL70168",
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
        description="Item #611 | Table HL70169",
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
        description="Item #612 | Table HL79999",
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
        description="Item #613",
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
        description="Item #614",
    )

    om1_30: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_30",
            "confidentiality_code",
            "OM1.30",
        ),
        serialization_alias="OM1.30",
        title="Confidentiality Code",
        description="Item #615 | Table HL70177",
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
        description="Item #616 | Table HL79999",
    )

    om1_32: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_32",
            "interpretation_of_observations",
            "OM1.32",
        ),
        serialization_alias="OM1.32",
        title="Interpretation of Observations",
        description="Item #617",
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
        description="Item #618 | Table HL79999",
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
        description="Item #619 | Table HL79999",
    )

    om1_35: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_35",
            "rules_that_trigger_reflex_testing",
            "OM1.35",
        ),
        serialization_alias="OM1.35",
        title="Rules that Trigger Reflex Testing",
        description="Item #620",
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
        description="Item #621 | Table HL79999",
    )

    om1_37: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_37",
            "patient_preparation",
            "OM1.37",
        ),
        serialization_alias="OM1.37",
        title="Patient Preparation",
        description="Item #622",
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
        description="Item #623 | Table HL79999",
    )

    om1_39: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_39",
            "factors_that_may_affect_the_observation",
            "OM1.39",
        ),
        serialization_alias="OM1.39",
        title="Factors that may Affect the Observation",
        description="Item #624",
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
        description="Item #625",
    )

    om1_41: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_41",
            "description_of_test_methods",
            "OM1.41",
        ),
        serialization_alias="OM1.41",
        title="Description of Test Methods",
        description="Item #626",
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
        description="Item #937 | Table HL70254",
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
        description="Item #938 | Table HL70255",
    )

    om1_44: Optional[TX] = Field(
        default=None,
        validation_alias=AliasChoices(
            "om1_44",
            "challenge_information",
            "OM1.44",
        ),
        serialization_alias="OM1.44",
        title="Challenge Information",
        description="Item #939 | Table HL70256",
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
        description="Item #940 | Table HL70258",
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
        description="Item #941 | Table HL79999",
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
        description="Item #942 | Table HL70259",
    )

    model_config = {"populate_by_name": True}
