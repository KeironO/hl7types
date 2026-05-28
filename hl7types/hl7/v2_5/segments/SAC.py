"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.5
Class: SAC
Type: Segment
"""

from __future__ import annotations

from pydantic import AliasChoices, BaseModel, Field

from ..datatypes.CE import CE
from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NA import NA
from ..datatypes.SN import SN
from ..datatypes.SPS import SPS
from ..datatypes.TS import TS


class SAC(BaseModel):
    """HL7 v2 SAC segment."""

    sac_1: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_1",
            "external_accession_identifier",
            "SAC.1",
        ),
        serialization_alias="SAC.1",
        title="External Accession Identifier",
        description="Item #1329",
    )

    sac_2: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_2",
            "accession_identifier",
            "SAC.2",
        ),
        serialization_alias="SAC.2",
        title="Accession Identifier",
        description="Item #1330",
    )

    sac_3: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_3",
            "container_identifier",
            "SAC.3",
        ),
        serialization_alias="SAC.3",
        title="Container Identifier",
        description="Item #1331",
    )

    sac_4: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_4",
            "primary_parent_container_identifier",
            "SAC.4",
        ),
        serialization_alias="SAC.4",
        title="Primary (parent) Container Identifier",
        description="Item #1332",
    )

    sac_5: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_5",
            "equipment_container_identifier",
            "SAC.5",
        ),
        serialization_alias="SAC.5",
        title="Equipment Container Identifier",
        description="Item #1333",
    )

    sac_6: SPS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_6",
            "specimen_source",
            "SAC.6",
        ),
        serialization_alias="SAC.6",
        title="Specimen Source",
        description="Item #249",
    )

    sac_7: TS | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_7",
            "registration_date_time",
            "SAC.7",
        ),
        serialization_alias="SAC.7",
        title="Registration Date/Time",
        description="Item #1334",
    )

    sac_8: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_8",
            "container_status",
            "SAC.8",
        ),
        serialization_alias="SAC.8",
        title="Container Status",
        description="Item #1335 | Table HL70370",
    )

    sac_9: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_9",
            "carrier_type",
            "SAC.9",
        ),
        serialization_alias="SAC.9",
        title="Carrier Type",
        description="Item #1336 | Table HL70378",
    )

    sac_10: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_10",
            "carrier_identifier",
            "SAC.10",
        ),
        serialization_alias="SAC.10",
        title="Carrier Identifier",
        description="Item #1337",
    )

    sac_11: NA | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_11",
            "position_in_carrier",
            "SAC.11",
        ),
        serialization_alias="SAC.11",
        title="Position in Carrier",
        description="Item #1338",
    )

    sac_12: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_12",
            "tray_type_sac",
            "SAC.12",
        ),
        serialization_alias="SAC.12",
        title="Tray Type - SAC",
        description="Item #1339 | Table HL70379",
    )

    sac_13: EI | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_13",
            "tray_identifier",
            "SAC.13",
        ),
        serialization_alias="SAC.13",
        title="Tray Identifier",
        description="Item #1340",
    )

    sac_14: NA | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_14",
            "position_in_tray",
            "SAC.14",
        ),
        serialization_alias="SAC.14",
        title="Position in Tray",
        description="Item #1341",
    )

    sac_15: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_15",
            "location",
            "SAC.15",
        ),
        serialization_alias="SAC.15",
        title="Location",
        description="Item #1342",
    )

    sac_16: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_16",
            "container_height",
            "SAC.16",
        ),
        serialization_alias="SAC.16",
        title="Container Height",
        description="Item #1343",
    )

    sac_17: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_17",
            "container_diameter",
            "SAC.17",
        ),
        serialization_alias="SAC.17",
        title="Container Diameter",
        description="Item #1344",
    )

    sac_18: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_18",
            "barrier_delta",
            "SAC.18",
        ),
        serialization_alias="SAC.18",
        title="Barrier Delta",
        description="Item #1345",
    )

    sac_19: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_19",
            "bottom_delta",
            "SAC.19",
        ),
        serialization_alias="SAC.19",
        title="Bottom Delta",
        description="Item #1346",
    )

    sac_20: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_20",
            "container_height_diameter_delta_units",
            "SAC.20",
        ),
        serialization_alias="SAC.20",
        title="Container Height/Diameter/Delta Units",
        description="Item #1347",
    )

    sac_21: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_21",
            "container_volume",
            "SAC.21",
        ),
        serialization_alias="SAC.21",
        title="Container Volume",
        description="Item #644",
    )

    sac_22: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_22",
            "available_specimen_volume",
            "SAC.22",
        ),
        serialization_alias="SAC.22",
        title="Available Specimen Volume",
        description="Item #1349",
    )

    sac_23: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_23",
            "initial_specimen_volume",
            "SAC.23",
        ),
        serialization_alias="SAC.23",
        title="Initial Specimen Volume",
        description="Item #1350",
    )

    sac_24: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_24",
            "volume_units",
            "SAC.24",
        ),
        serialization_alias="SAC.24",
        title="Volume Units",
        description="Item #1351",
    )

    sac_25: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_25",
            "separator_type",
            "SAC.25",
        ),
        serialization_alias="SAC.25",
        title="Separator Type",
        description="Item #1352 | Table HL70380",
    )

    sac_26: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_26",
            "cap_type",
            "SAC.26",
        ),
        serialization_alias="SAC.26",
        title="Cap Type",
        description="Item #1353 | Table HL70381",
    )

    sac_27: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_27",
            "additive",
            "SAC.27",
        ),
        serialization_alias="SAC.27",
        title="Additive",
        description="Item #647 | Table HL70371",
    )

    sac_28: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_28",
            "specimen_component",
            "SAC.28",
        ),
        serialization_alias="SAC.28",
        title="Specimen Component",
        description="Item #1355",
    )

    sac_29: SN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_29",
            "dilution_factor",
            "SAC.29",
        ),
        serialization_alias="SAC.29",
        title="Dilution Factor",
        description="Item #1356",
    )

    sac_30: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_30",
            "treatment",
            "SAC.30",
        ),
        serialization_alias="SAC.30",
        title="Treatment",
        description="Item #1357 | Table HL70373",
    )

    sac_31: SN | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_31",
            "temperature",
            "SAC.31",
        ),
        serialization_alias="SAC.31",
        title="Temperature",
        description="Item #1358",
    )

    sac_32: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_32",
            "hemolysis_index",
            "SAC.32",
        ),
        serialization_alias="SAC.32",
        title="Hemolysis Index",
        description="Item #1359",
    )

    sac_33: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_33",
            "hemolysis_index_units",
            "SAC.33",
        ),
        serialization_alias="SAC.33",
        title="Hemolysis Index Units",
        description="Item #1360",
    )

    sac_34: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_34",
            "lipemia_index",
            "SAC.34",
        ),
        serialization_alias="SAC.34",
        title="Lipemia Index",
        description="Item #1361",
    )

    sac_35: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_35",
            "lipemia_index_units",
            "SAC.35",
        ),
        serialization_alias="SAC.35",
        title="Lipemia Index Units",
        description="Item #1362",
    )

    sac_36: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_36",
            "icterus_index",
            "SAC.36",
        ),
        serialization_alias="SAC.36",
        title="Icterus Index",
        description="Item #1363",
    )

    sac_37: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_37",
            "icterus_index_units",
            "SAC.37",
        ),
        serialization_alias="SAC.37",
        title="Icterus Index Units",
        description="Item #1364",
    )

    sac_38: str | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_38",
            "fibrin_index",
            "SAC.38",
        ),
        serialization_alias="SAC.38",
        title="Fibrin Index",
        description="Item #1365",
    )

    sac_39: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_39",
            "fibrin_index_units",
            "SAC.39",
        ),
        serialization_alias="SAC.39",
        title="Fibrin Index Units",
        description="Item #1366",
    )

    sac_40: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_40",
            "system_induced_contaminants",
            "SAC.40",
        ),
        serialization_alias="SAC.40",
        title="System Induced Contaminants",
        description="Item #1367 | Table HL70374",
    )

    sac_41: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_41",
            "drug_interference",
            "SAC.41",
        ),
        serialization_alias="SAC.41",
        title="Drug Interference",
        description="Item #1368 | Table HL70382",
    )

    sac_42: CE | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_42",
            "artificial_blood",
            "SAC.42",
        ),
        serialization_alias="SAC.42",
        title="Artificial Blood",
        description="Item #1369 | Table HL70375",
    )

    sac_43: list[CWE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_43",
            "special_handling_code",
            "SAC.43",
        ),
        serialization_alias="SAC.43",
        title="Special Handling Code",
        description="Item #1370 | Table HL70376",
    )

    sac_44: list[CE] | None = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_44",
            "other_environmental_factors",
            "SAC.44",
        ),
        serialization_alias="SAC.44",
        title="Other Environmental Factors",
        description="Item #1371 | Table HL70377",
    )

    model_config = {"populate_by_name": True}
