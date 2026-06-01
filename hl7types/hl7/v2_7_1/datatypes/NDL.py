"""
Profile: urn:hl7-org:v2xml
Release: v2
Version: 2.7.1
Class: NDL
Type: Datatype
"""
from __future__ import annotations

from typing import Optional
from pydantic import AliasChoices, Field
from hl7types.hl7 import HL7Model
from pydantic import field_validator

from .CNN import CNN
from .HD import HD


class NDL(HL7Model):
    """HL7 v2 NDL data type.

    Attributes
    ----------
    ndl_1 : CNN | None
        NDL.1 (opt) - Name (CNN)

    ndl_2 : str | None
        NDL.2 (opt) - Start Date/time (DTM)

    ndl_3 : str | None
        NDL.3 (opt) - End Date/time (DTM)

    ndl_4 : str | None
        NDL.4 (opt) - Point of Care (IS)

    ndl_5 : str | None
        NDL.5 (opt) - Room (IS)

    ndl_6 : str | None
        NDL.6 (opt) - Bed (IS)

    ndl_7 : HD | None
        NDL.7 (opt) - Facility (HD)

    ndl_8 : str | None
        NDL.8 (opt) - Location Status (IS)

    ndl_9 : str | None
        NDL.9 (opt) - Patient Location Type (IS)

    ndl_10 : str | None
        NDL.10 (opt) - Building (IS)

    ndl_11 : str | None
        NDL.11 (opt) - Floor (IS)
    """

    ndl_1: Optional[CNN] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_1",
            "name",
            "NDL.1",
        ),
        serialization_alias="NDL.1",
        title="Name",
    )

    ndl_2: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_2",
            "start_date_time",
            "NDL.2",
        ),
        serialization_alias="NDL.2",
        title="Start Date/time",
    )

    ndl_3: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_3",
            "end_date_time",
            "NDL.3",
        ),
        serialization_alias="NDL.3",
        title="End Date/time",
    )

    ndl_4: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_4",
            "point_of_care",
            "NDL.4",
        ),
        serialization_alias="NDL.4",
        title="Point of Care",
    )

    ndl_5: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_5",
            "room",
            "NDL.5",
        ),
        serialization_alias="NDL.5",
        title="Room",
    )

    ndl_6: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_6",
            "bed",
            "NDL.6",
        ),
        serialization_alias="NDL.6",
        title="Bed",
    )

    ndl_7: Optional[HD] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_7",
            "facility",
            "NDL.7",
        ),
        serialization_alias="NDL.7",
        title="Facility",
    )

    ndl_8: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_8",
            "location_status",
            "NDL.8",
        ),
        serialization_alias="NDL.8",
        title="Location Status",
    )

    ndl_9: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_9",
            "patient_location_type",
            "NDL.9",
        ),
        serialization_alias="NDL.9",
        title="Patient Location Type",
    )

    ndl_10: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_10",
            "building",
            "NDL.10",
        ),
        serialization_alias="NDL.10",
        title="Building",
    )

    ndl_11: Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            "ndl_11",
            "floor",
            "NDL.11",
        ),
        serialization_alias="NDL.11",
        title="Floor",
    )

    @field_validator("ndl_2", "ndl_3", mode='before')
    @classmethod
    def _validate_dtm(cls, v: str) -> str:
        import re
        if not re.fullmatch(r'(\d{4}([01]\d(\d{2}([012]\d([0-5]\d([0-5]\d(\.\d(\d(\d(\d)?)?)?)?)?)?)?)?)?)?([+\-]\d{4})?', v or ''):
            raise ValueError(f"{v!r} is not empty or a valid HL7 datetime")
        return v

    model_config = {"populate_by_name": True}
