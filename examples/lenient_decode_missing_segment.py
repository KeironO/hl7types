"""Show strict and lenient ER7 decoding."""

import warnings

from pydantic import ValidationError

from hl7types import decode_er7
from hl7types.hl7.v2_5_1.messages import ACK

# This ACK is incomplete because the required MSA segment is missing.
incomplete_wire = (
    "MSH|^~\\&|LABORDAI|YSBYTY CWMTAFF|HIS|YSBYTY CWMTAFF|20260301120000||ACK|MSG001|P|2.5.1\r"
)

# This ACK includes the required MSA segment.
complete_wire = (
    "MSH|^~\\&|LABORDAI|YSBYTY CWMTAFF|HIS|YSBYTY CWMTAFF|20260301120000||ACK|MSG001|P|2.5.1\r"
    "MSA|AA|MSG001\r"
)


print("Strict mode")

# Strict decoding is the default.
# Because MSA is missing, this raises a ValidationError.
try:
    decode_er7(incomplete_wire, msg_cls=ACK)
except ValidationError as exc:
    print("Validation failed as expected")
    print("Number of errors:", exc.error_count())

    for error in exc.errors():
        location = " > ".join(str(part) for part in error["loc"])
        print(location + ":", error["msg"])


print("\nLenient mode")

# Lenient decoding is opt-in with strict=False.
# Instead of raising, hl7types creates an empty placeholder for the missing MSA.
with warnings.catch_warnings(record=True) as caught:
    warnings.simplefilter("always")
    msg = decode_er7(incomplete_wire, msg_cls=ACK, strict=False)

print("Decode succeeded")
print("Number of warnings:", len(caught))

for warning in caught:
    print(warning.category.__name__ + ":", warning.message)

# The MSA segment exists on the model, but it did not come from the wire.
# An empty model_fields_set means no MSA fields were decoded.
# Required fields (msa_1, msa_2) are absent on the placeholder; only
# optional fields with defaults are accessible.
print("MSA fields decoded:", msg.MSA.model_fields_set)

# The MSH segment was present, so its fields decoded normally.
print("MSH.10 control ID:", msg.MSH.msh_10)


print("\nmodel_validate_er7")

# The class method has the same strict-by-default behaviour.
try:
    ACK.model_validate_er7(incomplete_wire)
except ValidationError:
    print("ACK.model_validate_er7(wire) raises by default")

# Passing strict=False makes the class method lenient too.
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    msg = ACK.model_validate_er7(incomplete_wire, strict=False)

print("ACK.model_validate_er7(wire, strict=False) returns:", type(msg).__name__)


print("\nComplete message")

# A complete ACK decodes cleanly in strict mode.
msg = decode_er7(complete_wire, msg_cls=ACK)

print("ACK code:", msg.MSA.msa_1)
print("Original control ID:", msg.MSA.msa_2)
