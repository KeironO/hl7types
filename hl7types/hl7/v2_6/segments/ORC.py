"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.6
Class: ORC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CNE import CNE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.EIP import EIP
from ..datatypes.PL import PL
from ..datatypes.TQ import TQ
from ..datatypes.XAD import XAD
from ..datatypes.XCN import XCN
from ..datatypes.XON import XON
from ..datatypes.XTN import XTN


class ORC(BaseModel):
    """HL7 v2 ORC segment."""

    orc_1: str = Field(
        default=...,
        validation_alias=AliasChoices(
            "orc_1",
            "order_control",
            "ORC.1",
        ),
        serialization_alias="ORC.1",
        title="Order Control",
        description="Item #215 | Table HL70119",
    )

    orc_2: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_2",
            "placer_order_number",
            "ORC.2",
        ),
        serialization_alias="ORC.2",
        title="Placer Order Number",
        description="Item #216",
    )

    orc_3: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_3",
            "filler_order_number",
            "ORC.3",
        ),
        serialization_alias="ORC.3",
        title="Filler Order Number",
        description="Item #217",
    )

    orc_4: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_4",
            "placer_group_number",
            "ORC.4",
        ),
        serialization_alias="ORC.4",
        title="Placer Group Number",
        description="Item #218",
    )

    orc_5: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_5",
            "order_status",
            "ORC.5",
        ),
        serialization_alias="ORC.5",
        title="Order Status",
        description="Item #219 | Table HL70038",
    )

    orc_6: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_6",
            "response_flag",
            "ORC.6",
        ),
        serialization_alias="ORC.6",
        title="Response Flag",
        description="Item #220 | Table HL70121",
    )

    orc_7: list[TQ] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_7",
            "quantity_timing",
            "ORC.7",
        ),
        serialization_alias="ORC.7",
        title="Quantity/Timing",
        description="Item #221",
    )

    orc_8: EIP | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_8",
            "parent",
            "ORC.8",
        ),
        serialization_alias="ORC.8",
        title="Parent",
        description="Item #222",
    )

    orc_9: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_9",
            "date_time_of_transaction",
            "ORC.9",
        ),
        serialization_alias="ORC.9",
        title="Date/Time of Transaction",
        description="Item #223",
    )

    orc_10: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_10",
            "entered_by",
            "ORC.10",
        ),
        serialization_alias="ORC.10",
        title="Entered By",
        description="Item #224",
    )

    orc_11: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_11",
            "verified_by",
            "ORC.11",
        ),
        serialization_alias="ORC.11",
        title="Verified By",
        description="Item #225",
    )

    orc_12: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_12",
            "ordering_provider",
            "ORC.12",
        ),
        serialization_alias="ORC.12",
        title="Ordering Provider",
        description="Item #226",
    )

    orc_13: PL | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_13",
            "enterer_s_location",
            "ORC.13",
        ),
        serialization_alias="ORC.13",
        title="Enterer's Location",
        description="Item #227",
    )

    orc_14: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_14",
            "call_back_phone_number",
            "ORC.14",
        ),
        serialization_alias="ORC.14",
        title="Call Back Phone Number",
        description="Item #228",
    )

    orc_15: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_15",
            "order_effective_date_time",
            "ORC.15",
        ),
        serialization_alias="ORC.15",
        title="Order Effective Date/Time",
        description="Item #229",
    )

    orc_16: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_16",
            "order_control_code_reason",
            "ORC.16",
        ),
        serialization_alias="ORC.16",
        title="Order Control Code Reason",
        description="Item #230 | Table HL79999",
    )

    orc_17: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_17",
            "entering_organization",
            "ORC.17",
        ),
        serialization_alias="ORC.17",
        title="Entering Organization",
        description="Item #231 | Table HL79999",
    )

    orc_18: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_18",
            "entering_device",
            "ORC.18",
        ),
        serialization_alias="ORC.18",
        title="Entering Device",
        description="Item #232 | Table HL79999",
    )

    orc_19: list[XCN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_19",
            "action_by",
            "ORC.19",
        ),
        serialization_alias="ORC.19",
        title="Action By",
        description="Item #233",
    )

    orc_20: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_20",
            "advanced_beneficiary_notice_code",
            "ORC.20",
        ),
        serialization_alias="ORC.20",
        title="Advanced Beneficiary Notice Code",
        description="Item #1310 | Table HL70339",
    )

    orc_21: list[XON] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_21",
            "ordering_facility_name",
            "ORC.21",
        ),
        serialization_alias="ORC.21",
        title="Ordering Facility Name",
        description="Item #1311",
    )

    orc_22: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_22",
            "ordering_facility_address",
            "ORC.22",
        ),
        serialization_alias="ORC.22",
        title="Ordering Facility Address",
        description="Item #1312",
    )

    orc_23: list[XTN] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_23",
            "ordering_facility_phone_number",
            "ORC.23",
        ),
        serialization_alias="ORC.23",
        title="Ordering Facility Phone Number",
        description="Item #1313",
    )

    orc_24: list[XAD] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_24",
            "ordering_provider_address",
            "ORC.24",
        ),
        serialization_alias="ORC.24",
        title="Ordering Provider Address",
        description="Item #1314",
    )

    orc_25: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_25",
            "order_status_modifier",
            "ORC.25",
        ),
        serialization_alias="ORC.25",
        title="Order Status Modifier",
        description="Item #1473 | Table HL79999",
    )

    orc_26: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_26",
            "advanced_beneficiary_notice_override_reason",
            "ORC.26",
        ),
        serialization_alias="ORC.26",
        title="Advanced Beneficiary Notice Override Reason",
        description="Item #1641 | Table HL70552",
    )

    orc_27: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_27",
            "filler_s_expected_availability_date_time",
            "ORC.27",
        ),
        serialization_alias="ORC.27",
        title="Filler's Expected Availability Date/Time",
        description="Item #1642",
    )

    orc_28: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_28",
            "confidentiality_code",
            "ORC.28",
        ),
        serialization_alias="ORC.28",
        title="Confidentiality Code",
        description="Item #615 | Table HL70177",
    )

    orc_29: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_29",
            "order_type",
            "ORC.29",
        ),
        serialization_alias="ORC.29",
        title="Order Type",
        description="Item #1643 | Table HL70482",
    )

    orc_30: CNE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_30",
            "enterer_authorization_mode",
            "ORC.30",
        ),
        serialization_alias="ORC.30",
        title="Enterer Authorization Mode",
        description="Item #1644 | Table HL70483",
    )

    orc_31: CWE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "orc_31",
            "parent_universal_service_identifier",
            "ORC.31",
        ),
        serialization_alias="ORC.31",
        title="Parent Universal Service Identifier",
        description="Item #2287",
    )

    model_config = {"populate_by_name": True}
