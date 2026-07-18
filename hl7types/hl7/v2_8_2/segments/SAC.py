"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.8.2
Class: SAC
Type: Segment
"""
from __future__ import annotations

import re

from typing import Optional, List
from pydantic import AliasChoices, ConfigDict, Field, ValidationInfo, field_validator
from hl7types.hl7 import HL7Model
from hl7types.hl7._validators import _apply_dt_fallback

from ..datatypes.CWE import CWE
from ..datatypes.EI import EI
from ..datatypes.NA import NA
from ..datatypes.SN import SN

_RE_DTM = re.compile(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?')
_RE_NM = re.compile(r'(\+|\-)?\d*\.?\d*')


class SAC(HL7Model):
    """Specimen Container detail (S13.4.3).

    Attributes
    ----------
    sac_1 : EI | None
        SAC.1 - External Accession Identifier (EI) O S13.4.3.1

    sac_2 : EI | None
        SAC.2 - Accession Identifier (EI) O S13.4.3.2

    sac_3 : EI | None
        SAC.3 - Container Identifier (EI) C S13.4.3.3

    sac_4 : EI | None
        SAC.4 - Primary (Parent) Container Identifier (EI) C S13.4.3.4

    sac_5 : EI | None
        SAC.5 - Equipment Container Identifier (EI) O S13.4.3.5

    sac_7 : str | None
        SAC.7 - Registration Date/Time (DTM) O S13.4.3.7

    sac_8 : CWE | None
        SAC.8 - Container Status (CWE) O S13.4.3.8 | 0370 - Container Status

    sac_9 : CWE | None
        SAC.9 - Carrier Type (CWE) O S13.4.3.9 | 0378 - Carrier Type

    sac_10 : EI | None
        SAC.10 - Carrier Identifier (EI) O S13.4.3.10

    sac_11 : NA | None
        SAC.11 - Position in Carrier (NA) O S13.4.3.11

    sac_12 : CWE | None
        SAC.12 - Tray Type - SAC (CWE) O S13.4.3.12 | 0379 - Tray Type

    sac_13 : EI | None
        SAC.13 - Tray Identifier (EI) O S13.4.3.13

    sac_14 : NA | None
        SAC.14 - Position in Tray (NA) O S13.4.3.14

    sac_15 : list[CWE] | None
        SAC.15 - Location (CWE) O rep S13.4.3.15 | 9999 - no table for CE

    sac_16 : str | None
        SAC.16 - Container Height (NM) O S13.4.3.16

    sac_17 : str | None
        SAC.17 - Container Diameter (NM) O S13.4.3.17

    sac_18 : str | None
        SAC.18 - Barrier Delta (NM) O S13.4.3.18

    sac_19 : str | None
        SAC.19 - Bottom Delta (NM) O S13.4.3.19

    sac_20 : CWE | None
        SAC.20 - Container Height/Diameter/Delta Units (CWE) O S13.4.3.20 | 9999 - no table for CE

    sac_21 : str | None
        SAC.21 - Container Volume (NM) O S8.8.12.4

    sac_22 : str | None
        SAC.22 - Available Specimen Volume (NM) O S13.4.3.22

    sac_23 : str | None
        SAC.23 - Initial Specimen Volume (NM) O S13.4.3.23

    sac_24 : CWE | None
        SAC.24 - Volume Units (CWE) O S13.4.3.24 | 9999 - no table for CE

    sac_25 : CWE | None
        SAC.25 - Separator Type (CWE) O S13.4.3.25 | 0380 - Separator Type

    sac_26 : CWE | None
        SAC.26 - Cap Type (CWE) O S13.4.3.26 | 0381 - Cap Type

    sac_27 : list[CWE] | None
        SAC.27 - Additive (CWE) O rep S13.4.3.27 | 0371 - Additive/Preservative

    sac_28 : CWE | None
        SAC.28 - Specimen Component (CWE) O S13.4.3.28 | 0372 - Specimen Component

    sac_29 : SN | None
        SAC.29 - Dilution Factor (SN) O S13.4.3.29

    sac_30 : CWE | None
        SAC.30 - Treatment (CWE) O S13.4.3.30 | 0373 - Treatment

    sac_31 : SN | None
        SAC.31 - Temperature (SN) O S13.4.3.31

    sac_32 : str | None
        SAC.32 - Hemolysis Index (NM) O S13.4.3.32

    sac_33 : CWE | None
        SAC.33 - Hemolysis Index Units (CWE) O S13.4.3.33 | 9999 - no table for CE

    sac_34 : str | None
        SAC.34 - Lipemia Index (NM) O S13.4.3.34

    sac_35 : CWE | None
        SAC.35 - Lipemia Index Units (CWE) O S13.4.3.35 | 9999 - no table for CE

    sac_36 : str | None
        SAC.36 - Icterus Index (NM) O S13.4.3.36

    sac_37 : CWE | None
        SAC.37 - Icterus Index Units (CWE) O S13.4.3.37 | 9999 - no table for CE

    sac_38 : str | None
        SAC.38 - Fibrin Index (NM) O S13.4.3.38

    sac_39 : CWE | None
        SAC.39 - Fibrin Index Units (CWE) O S13.4.3.39 | 9999 - no table for CE

    sac_40 : list[CWE] | None
        SAC.40 - System Induced Contaminants (CWE) O rep S13.4.3.40 | 0374 - System Induced Contaminants

    sac_41 : list[CWE] | None
        SAC.41 - Drug Interference (CWE) O rep S13.4.3.41 | 0382 - Drug Interference

    sac_42 : CWE | None
        SAC.42 - Artificial Blood (CWE) O S13.4.3.42 | 0375 - Artificial Blood

    sac_43 : list[CWE] | None
        SAC.43 - Special Handling Code (CWE) O rep S13.4.3.43 | 0376 - Special Handling Code

    sac_44 : list[CWE] | None
        SAC.44 - Other Environmental Factors (CWE) O rep S13.4.3.44 | 0377 - Other Environmental Factors
    """

    sac_1: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_1",
            "external_accession_identifier",
            "SAC.1",
        ),
        serialization_alias="SAC.1",
        title="External Accession Identifier",
        description="O | Item #01329",
    )

    sac_2: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_2",
            "accession_identifier",
            "SAC.2",
        ),
        serialization_alias="SAC.2",
        title="Accession Identifier",
        description="O | Item #01330",
    )

    sac_3: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_3",
            "container_identifier",
            "SAC.3",
        ),
        serialization_alias="SAC.3",
        title="Container Identifier",
        description="C | Item #01331",
    )

    sac_4: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_4",
            "primary_parent_container_identifier",
            "SAC.4",
        ),
        serialization_alias="SAC.4",
        title="Primary (Parent) Container Identifier",
        description="C | Item #01332",
    )

    sac_5: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_5",
            "equipment_container_identifier",
            "SAC.5",
        ),
        serialization_alias="SAC.5",
        title="Equipment Container Identifier",
        description="O | Item #01333",
    )

    sac_7: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_7",
            "registration_date_time",
            "SAC.7",
        ),
        serialization_alias="SAC.7",
        title="Registration Date/Time",
        description="O | Item #01334",
    )

    sac_8: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_8",
            "container_status",
            "SAC.8",
        ),
        serialization_alias="SAC.8",
        title="Container Status",
        description="O | Item #01335 | Table 0370 - Container Status",
    )

    sac_9: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_9",
            "carrier_type",
            "SAC.9",
        ),
        serialization_alias="SAC.9",
        title="Carrier Type",
        description="O | Item #01336 | Table 0378 - Carrier Type",
    )

    sac_10: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_10",
            "carrier_identifier",
            "SAC.10",
        ),
        serialization_alias="SAC.10",
        title="Carrier Identifier",
        description="O | Item #01337",
    )

    sac_11: Optional[NA] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_11",
            "position_in_carrier",
            "SAC.11",
        ),
        serialization_alias="SAC.11",
        title="Position in Carrier",
        description="O | Item #01338",
    )

    sac_12: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_12",
            "tray_type_sac",
            "SAC.12",
        ),
        serialization_alias="SAC.12",
        title="Tray Type - SAC",
        description="O | Item #01339 | Table 0379 - Tray Type",
    )

    sac_13: Optional[EI] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_13",
            "tray_identifier",
            "SAC.13",
        ),
        serialization_alias="SAC.13",
        title="Tray Identifier",
        description="O | Item #01340",
    )

    sac_14: Optional[NA] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_14",
            "position_in_tray",
            "SAC.14",
        ),
        serialization_alias="SAC.14",
        title="Position in Tray",
        description="O | Item #01341",
    )

    sac_15: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_15",
            "location",
            "SAC.15",
        ),
        serialization_alias="SAC.15",
        title="Location",
        description="O | Item #01342 | Table 9999 - no table for CE",
    )

    sac_16: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_16",
            "container_height",
            "SAC.16",
        ),
        serialization_alias="SAC.16",
        title="Container Height",
        description="O | Item #01343",
    )

    sac_17: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_17",
            "container_diameter",
            "SAC.17",
        ),
        serialization_alias="SAC.17",
        title="Container Diameter",
        description="O | Item #01344",
    )

    sac_18: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_18",
            "barrier_delta",
            "SAC.18",
        ),
        serialization_alias="SAC.18",
        title="Barrier Delta",
        description="O | Item #01345",
    )

    sac_19: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_19",
            "bottom_delta",
            "SAC.19",
        ),
        serialization_alias="SAC.19",
        title="Bottom Delta",
        description="O | Item #01346",
    )

    sac_20: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_20",
            "container_height_diameter_delta_units",
            "SAC.20",
        ),
        serialization_alias="SAC.20",
        title="Container Height/Diameter/Delta Units",
        description="O | Item #01347 | Table 9999 - no table for CE",
    )

    sac_21: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_21",
            "container_volume",
            "SAC.21",
        ),
        serialization_alias="SAC.21",
        title="Container Volume",
        description="O | Item #00644",
    )

    sac_22: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_22",
            "available_specimen_volume",
            "SAC.22",
        ),
        serialization_alias="SAC.22",
        title="Available Specimen Volume",
        description="O | Item #01349",
    )

    sac_23: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_23",
            "initial_specimen_volume",
            "SAC.23",
        ),
        serialization_alias="SAC.23",
        title="Initial Specimen Volume",
        description="O | Item #01350",
    )

    sac_24: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_24",
            "volume_units",
            "SAC.24",
        ),
        serialization_alias="SAC.24",
        title="Volume Units",
        description="O | Item #01351 | Table 9999 - no table for CE",
    )

    sac_25: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_25",
            "separator_type",
            "SAC.25",
        ),
        serialization_alias="SAC.25",
        title="Separator Type",
        description="O | Item #01352 | Table 0380 - Separator Type",
    )

    sac_26: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_26",
            "cap_type",
            "SAC.26",
        ),
        serialization_alias="SAC.26",
        title="Cap Type",
        description="O | Item #01353 | Table 0381 - Cap Type",
    )

    sac_27: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_27",
            "additive",
            "SAC.27",
        ),
        serialization_alias="SAC.27",
        title="Additive",
        description="O | Item #00647 | Table 0371 - Additive/Preservative",
    )

    sac_28: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_28",
            "specimen_component",
            "SAC.28",
        ),
        serialization_alias="SAC.28",
        title="Specimen Component",
        description="O | Item #01355 | Table 0372 - Specimen Component",
    )

    sac_29: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_29",
            "dilution_factor",
            "SAC.29",
        ),
        serialization_alias="SAC.29",
        title="Dilution Factor",
        description="O | Item #01356",
    )

    sac_30: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_30",
            "treatment",
            "SAC.30",
        ),
        serialization_alias="SAC.30",
        title="Treatment",
        description="O | Item #01357 | Table 0373 - Treatment",
    )

    sac_31: Optional[SN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_31",
            "temperature",
            "SAC.31",
        ),
        serialization_alias="SAC.31",
        title="Temperature",
        description="O | Item #01358",
    )

    sac_32: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_32",
            "hemolysis_index",
            "SAC.32",
        ),
        serialization_alias="SAC.32",
        title="Hemolysis Index",
        description="O | Item #01359",
    )

    sac_33: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_33",
            "hemolysis_index_units",
            "SAC.33",
        ),
        serialization_alias="SAC.33",
        title="Hemolysis Index Units",
        description="O | Item #01360 | Table 9999 - no table for CE",
    )

    sac_34: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_34",
            "lipemia_index",
            "SAC.34",
        ),
        serialization_alias="SAC.34",
        title="Lipemia Index",
        description="O | Item #01361",
    )

    sac_35: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_35",
            "lipemia_index_units",
            "SAC.35",
        ),
        serialization_alias="SAC.35",
        title="Lipemia Index Units",
        description="O | Item #01362 | Table 9999 - no table for CE",
    )

    sac_36: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_36",
            "icterus_index",
            "SAC.36",
        ),
        serialization_alias="SAC.36",
        title="Icterus Index",
        description="O | Item #01363",
    )

    sac_37: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_37",
            "icterus_index_units",
            "SAC.37",
        ),
        serialization_alias="SAC.37",
        title="Icterus Index Units",
        description="O | Item #01364 | Table 9999 - no table for CE",
    )

    sac_38: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_38",
            "fibrin_index",
            "SAC.38",
        ),
        serialization_alias="SAC.38",
        title="Fibrin Index",
        description="O | Item #01365",
    )

    sac_39: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_39",
            "fibrin_index_units",
            "SAC.39",
        ),
        serialization_alias="SAC.39",
        title="Fibrin Index Units",
        description="O | Item #01366 | Table 9999 - no table for CE",
    )

    sac_40: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_40",
            "system_induced_contaminants",
            "SAC.40",
        ),
        serialization_alias="SAC.40",
        title="System Induced Contaminants",
        description=(
            "O | Item #01367 | Table 0374 - System Induced Contaminants"
        ),
    )

    sac_41: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_41",
            "drug_interference",
            "SAC.41",
        ),
        serialization_alias="SAC.41",
        title="Drug Interference",
        description="O | Item #01368 | Table 0382 - Drug Interference",
    )

    sac_42: Optional[CWE] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_42",
            "artificial_blood",
            "SAC.42",
        ),
        serialization_alias="SAC.42",
        title="Artificial Blood",
        description="O | Item #01369 | Table 0375 - Artificial Blood",
    )

    sac_43: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_43",
            "special_handling_code",
            "SAC.43",
        ),
        serialization_alias="SAC.43",
        title="Special Handling Code",
        description="O | Item #01370 | Table 0376 - Special Handling Code",
    )

    sac_44: Optional[List[CWE]] = Field(
        default=None,
        validation_alias=AliasChoices(
            "sac_44",
            "other_environmental_factors",
            "SAC.44",
        ),
        serialization_alias="SAC.44",
        title="Other Environmental Factors",
        description=(
            "O | Item #01371 | Table 0377 - Other Environmental Factors"
        ),
    )

    @field_validator("sac_7", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str, info: ValidationInfo) -> str:
        if _RE_DTM.fullmatch(v or ''):
            return v
        ctx: dict[str, object] = info.context or {}
        from typing import cast, Callable
        return _apply_dt_fallback(v, parser=cast(Callable[[str], str] | None, ctx.get("dtm_parser")), datatype="DTM", field_path="TS.1")

    @field_validator("sac_16", "sac_17", "sac_18", "sac_19", "sac_21", "sac_22", "sac_23", "sac_32", "sac_34", "sac_36", "sac_38", mode='before')
    @classmethod
    def _validate_nm(cls, v: str) -> str:
        if not _RE_NM.fullmatch(v or ''):
            raise ValueError(f"{v!r} is not empty or numeric")
        return v

    model_config = ConfigDict(populate_by_name=True)
