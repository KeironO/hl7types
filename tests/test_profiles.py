"""Tests for conformance profile parsing and registry building using ADT_A31.xml."""
from __future__ import annotations

import textwrap
from pathlib import Path

import pytest
from pydantic import ValidationError

from hl7types import HL7Registry
from hl7types.profiles.builder import build_registry_from_profile
from hl7types.profiles.parser import _parse_usage, parse_profile, parse_tables
from hl7types.profiles.parser.constraints import (
    ProfileConstraints,
    SegGroupConstraint,
    SegmentConstraint,
    Usage,
)

_PROFILE_PATH = Path(__file__).parent / "codecs" / "resources" / "ADT_A31.xml"


@pytest.fixture(scope="module")
def profile() -> ProfileConstraints:
    return parse_profile(_PROFILE_PATH)


@pytest.fixture(scope="module")
def registry(profile: ProfileConstraints) -> HL7Registry:
    r = HL7Registry()
    build_registry_from_profile(profile, r)
    return r


def test_profile_hl7_version(profile: ProfileConstraints):
    assert profile.hl7_version == "2.4"


def test_profile_msg_type(profile: ProfileConstraints):
    assert profile.msg_type == "ADT"


def test_profile_event_type(profile: ProfileConstraints):
    assert profile.event_type == "A31"


def test_profile_msg_struct_id(profile: ProfileConstraints):
    # MsgStructID disambiguates messages that share the same trigger event
    # but use a different segment structure (e.g. A31 reuses ADT_A05).
    assert profile.msg_struct_id == "ADT_A05"


def test_profile_name(profile: ProfileConstraints):
    assert profile.name == "update person information"


def test_profile_has_three_segments(profile: ProfileConstraints):
    assert len(profile.segments) == 3


def test_profile_segment_names(profile: ProfileConstraints):
    names = [s.name for s in profile.segments]
    assert names == ["MSH", "EVN", "PID"]


def test_profile_all_segments_required(profile: ProfileConstraints):
    for seg in profile.segments:
        assert isinstance(seg, SegmentConstraint)
        assert seg.usage == Usage.REQUIRED


def test_profile_pid_has_fields(profile: ProfileConstraints):
    pid = next(s for s in profile.segments if s.name == "PID")
    assert len(pid.fields) > 0


def test_profile_pid_patient_identifier_list_is_required(profile: ProfileConstraints):
    pid = next(s for s in profile.segments if s.name == "PID")
    # PID.3 is field index 2 (0-based) ; Patient Identifier List
    assert pid.fields[2].usage == Usage.REQUIRED


def test_profile_pid_set_id_is_not_used(profile: ProfileConstraints):
    pid = next(s for s in profile.segments if s.name == "PID")
    # PID.1 ; Set ID ; is marked X in this profile
    assert pid.fields[0].usage == Usage.NOT_USED


def test_registry_registers_constrained_pid(registry: HL7Registry):
    constrained = registry.get_segment("PID")
    assert constrained is not None


def test_registry_pid_is_profile_subclass(registry: HL7Registry):
    from hl7types.hl7.v2_4.segments.PID import PID as BasePID

    constrained = registry.get_segment("PID")
    assert constrained is not BasePID
    assert issubclass(constrained, BasePID)


def test_registry_pid_qualname_has_profile_prefix(registry: HL7Registry):
    constrained = registry.get_segment("PID")
    assert "Profile" in constrained.__qualname__


def test_constrained_pid_rejects_not_used_field(registry: HL7Registry):
    # pid_1 (Set ID) is marked X ; any non-None value must raise
    ProfilePID = registry.get_segment("PID")
    from hl7types.hl7.v2_4.datatypes.CX import CX
    from hl7types.hl7.v2_4.datatypes.FN import FN
    from hl7types.hl7.v2_4.datatypes.XPN import XPN

    with pytest.raises(ValidationError):
        ProfilePID(
            pid_1="1",  # X field ; not allowed
            pid_3=[CX(cx_1="12345")],
            pid_5=[XPN(xpn_1=FN(fn_1="Smith"), xpn_2="John")],
        )


def test_constrained_pid_requires_patient_identifier_list(registry: HL7Registry):
    # pid_3 is R ; omitting it must raise
    ProfilePID = registry.get_segment("PID")
    from hl7types.hl7.v2_4.datatypes.FN import FN
    from hl7types.hl7.v2_4.datatypes.XPN import XPN

    with pytest.raises(ValidationError):
        ProfilePID(
            pid_5=[XPN(xpn_1=FN(fn_1="Smith"), xpn_2="John")],
        )


def test_constrained_pid_valid_construction(registry: HL7Registry):
    ProfilePID = registry.get_segment("PID")
    from hl7types.hl7.v2_4.datatypes.CX import CX
    from hl7types.hl7.v2_4.datatypes.FN import FN
    from hl7types.hl7.v2_4.datatypes.TS import TS
    from hl7types.hl7.v2_4.datatypes.XPN import XPN

    pid = ProfilePID(
        pid_3=[CX(cx_1="12345")],
        pid_5=[XPN(xpn_1=FN(fn_1="Smith"), xpn_2="John")],
        pid_7=TS(ts_1="19800101"),
        pid_8="M",
    )
    assert pid.pid_3[0].cx_1 == "12345"
    assert pid.pid_5[0].xpn_2 == "John"
    assert pid.pid_8 == "M"


def test_parse_usage_accepts_full_enum_name_as_fallback():
    # Some profiles spell out the name ("REQUIRED") instead of the
    # abbreviation ("R"). The parser tries both forms.
    assert _parse_usage("REQUIRED") == Usage.REQUIRED
    assert _parse_usage("NOT_USED") == Usage.NOT_USED


def test_parse_usage_raises_for_completely_unknown_value():
    with pytest.raises(ValueError, match="Unknown usage value"):
        _parse_usage("BLAH")


def test_parse_profile_raises_when_static_def_element_is_absent(tmp_path: Path):
    bad = tmp_path / "bad.xml"
    bad.write_text(
        '<?xml version="1.0"?>'
        '<HL7v2xConformanceProfile HL7Version="2.4">'
        "<MetaData Name=\"broken\"/>"
        "</HL7v2xConformanceProfile>"
    )
    with pytest.raises(ValueError, match="HL7v2StaticDEf"):
        parse_profile(bad)


_GROUPED_PROFILE_XML = textwrap.dedent("""\
    <?xml version="1.0"?>
    <HL7v2xConformanceProfile HL7Version="2.5.1">
      <MetaData Name="grouped profile"/>
      <HL7v2xStaticDef MsgType="ORM" EventType="O01" MsgStructID="ORM_O01">
        <Segment Name="MSH" LongName="Message Header" Usage="R" Min="1" Max="1"/>
        <SegGroup Name="PATIENT" LongName="Patient Group" Usage="R" Min="1" Max="1">
          <Segment Name="PID" LongName="Patient ID" Usage="R" Min="1" Max="1"/>
          <SegGroup Name="PATIENT_VISIT" LongName="Patient Visit Group" Usage="O" Min="0" Max="1">
            <Segment Name="PV1" LongName="Patient Visit" Usage="R" Min="1" Max="1"/>
          </SegGroup>
        </SegGroup>
      </HL7v2xStaticDef>
    </HL7v2xConformanceProfile>
""")


def test_parse_profile_seg_group_becomes_seg_group_constraint(tmp_path: Path):
    path = tmp_path / "grouped.xml"
    path.write_text(_GROUPED_PROFILE_XML)
    profile = parse_profile(path)

    assert len(profile.segments) == 2
    msh, patient = profile.segments

    assert isinstance(msh, SegmentConstraint)
    assert msh.name == "MSH"

    assert isinstance(patient, SegGroupConstraint)
    assert patient.name == "PATIENT"
    assert patient.usage == Usage.REQUIRED


def test_parse_profile_seg_group_children_are_parsed(tmp_path: Path):
    path = tmp_path / "grouped.xml"
    path.write_text(_GROUPED_PROFILE_XML)
    profile = parse_profile(path)

    patient = next(c for c in profile.segments if isinstance(c, SegGroupConstraint))
    pid_seg, visit_group = patient.children

    assert isinstance(pid_seg, SegmentConstraint)
    assert pid_seg.name == "PID"
    assert pid_seg.usage == Usage.REQUIRED

    assert isinstance(visit_group, SegGroupConstraint)
    assert visit_group.name == "PATIENT_VISIT"
    assert visit_group.usage == Usage.OPTIONAL
    assert visit_group.children[0].name == "PV1"


_TABLES_XML = textwrap.dedent("""\
    <?xml version="1.0"?>
    <HL7Tables>
      <hl7table id="0001" name="Administrative Sex">
        <tableElement code="F" displayName="Female"/>
        <tableElement code="M" displayName="Male"/>
        <tableElement code="O" displayName="Other"/>
      </hl7table>
      <hl7table id="0136" name="Yes/no Indicator">
        <tableElement code="Y"/>
        <tableElement code="N"/>
      </hl7table>
      <hl7table id="empty_table"/>
      <hl7table name="no_id_table">
        <tableElement code="X"/>
      </hl7table>
    </HL7Tables>
""")


def test_parse_tables_returns_codes_indexed_by_table_id(tmp_path: Path):
    path = tmp_path / "tables.xml"
    path.write_text(_TABLES_XML)
    tables = parse_tables(path)

    assert tables["0001"] == {"F", "M", "O"}
    assert tables["0136"] == {"Y", "N"}


def test_parse_tables_excludes_tables_without_codes_or_without_id(tmp_path: Path):
    path = tmp_path / "tables.xml"
    path.write_text(_TABLES_XML)
    tables = parse_tables(path)

    assert "empty_table" not in tables   # has id but no tableElement children
    assert "no_id_table" not in tables   # has codes but no id attribute
