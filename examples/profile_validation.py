"""Validate an HL7 message against a conformance profile."""

import warnings
from pathlib import Path

from pydantic import ValidationError

from hl7types import HL7Registry, decode_er7
from hl7types.profiles.builder import build_registry_from_profile
from hl7types.profiles.parser import parse_profile

# This example uses the ADT_A31 XML profile from the test fixtures.
#
# The profile constrains a standard HL7 v2.4 ADT_A05 message structure.
# In this profile, PID.3 is required and PID.1 is marked as not used.
profile_path = Path(__file__).parent.parent / "tests" / "codecs" / "resources" / "ADT_A31.xml"


if not profile_path.exists():
    raise FileNotFoundError(
        f"Profile fixture not found: {profile_path}\nRun this example from the repository root."
    )


# Parse the XML conformance profile.
profile = parse_profile(profile_path)

print("Profile:", profile.name)
print("HL7 version:", profile.hl7_version)
print("Message:", profile.msg_type + "^" + profile.event_type)
print("Structure:", profile.msg_struct_id)


# Build a registry from the profile.
#
# The registry contains constrained segment classes generated from the profile.
# Passing this registry to decode_er7 makes the decoder use those constraints.
registry = HL7Registry()
build_registry_from_profile(profile, registry)


print("\nValid message")

# This message satisfies the profile.
#
# PID.3 is present, so the required patient identifier is available.
# PID.1 is omitted, which is correct because the profile marks it as not used.
valid_wire = (
    "MSH|^~\\&|HIS|HOSPITAL|ADT|HOSPITAL|20260101090000||ADT^A31^ADT_A05|MSG001|P|2.4\r"
    "EVN||20260101090000\r"
    "PID|||MRN001^^^HOSPITAL^MR||JONES^BRYNN\r"
)

with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    msg = decode_er7(valid_wire, registry=registry, strict=False)

print("Decoded as:", type(msg).__name__)
print("PID.3 MRN:", msg.PID.pid_3[0].cx_1)

for warning in caught:
    print("Warning:", warning.message)


print("\nInvalid message")

# This message violates the profile.
#
# PID.1 has a value, but the profile marks PID.1 as X, meaning "not used".
# The profile-constrained PID class therefore raises a ValidationError.
invalid_wire = (
    "MSH|^~\\&|HIS|HOSPITAL|ADT|HOSPITAL|20260101090000||ADT^A31^ADT_A05|MSG002|P|2.4\r"
    "EVN||20260101090000\r"
    "PID|1||MRN001^^^HOSPITAL^MR||JONES^BRYNN\r"
)

try:
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        decode_er7(invalid_wire, registry=registry, strict=False)
except ValidationError as exc:
    print("Validation failed as expected")
    print("Number of errors:", exc.error_count())

    for error in exc.errors():
        location = " > ".join(str(part) for part in error["loc"])
        print(location + ":", error["msg"])


print("\nConstrained segment class")

# The profile builder registers a constrained PID class in the registry.
#
# This class replaces the standard PID segment when messages are decoded
# through this registry.
constrained_pid = registry.get_segment("PID")

if constrained_pid is None:
    print("No PID constraints were registered")
else:
    print("PID class:", constrained_pid.__qualname__)
