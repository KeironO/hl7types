"""Decode an ACK message that contains a custom Z-segment."""

from pydantic import Field

from hl7types import HL7Model, HL7Registry, decode_er7
from hl7types.hl7.v2_5_1.messages import ACK


# Define a custom ZPAS segment.
#
# Z-segments are local, non-standard HL7 extensions. They are commonly used
# when an organisation or vendor needs to send data that is not represented
# by the base HL7 specification.
class ZPAS(HL7Model):
    zpas_1: str | None = Field(None, serialization_alias="ZPAS.1")  # appointment ID
    zpas_2: str | None = Field(None, serialization_alias="ZPAS.2")  # appointment date
    zpas_3: str | None = Field(None, serialization_alias="ZPAS.3")  # clinic code


# Avoid Python 3.14+ name-shadowing when a field has the same name as its type.
# This lets the message class below use `ZPAS` as the HL7 segment name while
# still referring safely to the Python class.
_ZPAS = ZPAS


# Extend the standard ACK message with the custom segment.
#
# The base ACK model already knows about standard segments such as MSH and MSA.
# This subclass adds an optional ZPAS segment so messages containing that local
# extension can be decoded into a typed model.
class ACKWithAppointment(ACK):
    ZPAS: _ZPAS | None = None


# HL7 wire text containing the custom ZPAS segment.
#
# MSH.9 identifies the message type as ACK, and MSH.12 identifies the HL7
# version as 2.5.1. The registry below uses those values to resolve the
# message class to ACKWithAppointment.
wire = (
    "MSH|^~\\&|HIS|YSBYTY CWMTAFF|LABORDAI|YSBYTY CWMTAFF|20260301120000||ACK|MSG000001|P|2.5.1\r"
    "MSA|AA|MSG000001\r"
    "ZPAS|APT20260301001|20260401090000|CLINIG DRAIG GOCH\r"
)


# Register the custom segment and the extended ACK message.
#
# Without this registry, the decoder would not know how to interpret ZPAS or
# which message class to use for an ACK message that includes the extension.
registry = HL7Registry()
registry.register_segment("ZPAS", ZPAS)
registry.register_message("2.5.1", "ACK", ACKWithAppointment)


# Decode using the custom registry.
#
# The decoder reads MSH.9 and MSH.12, finds the registered ACKWithAppointment
# class, and then uses the registered ZPAS segment model for the ZPAS line.
msg = decode_er7(wire, registry=registry)


# Read standard ACK fields from the typed model.
print("Message type:", type(msg).__name__)
print("ACK code:", msg.MSA.msa_1)
print("Control ID:", msg.MSA.msa_2)


# Read the custom ZPAS fields from the same typed model.
print("Appointment ID:", msg.ZPAS.zpas_1)
print("Appointment date:", msg.ZPAS.zpas_2)
print("Clinic:", msg.ZPAS.zpas_3)


# Encode the message back to ER7.
#
# This demonstrates that the custom segment is preserved and can be written
# back out to HL7 wire format after decoding.
print("\nRe-encoded:")
for segment in msg.model_dump_er7().split("\r"):
    print(segment)


# Registries are independent.
#
# This is useful when different systems, feeds or pipelines use different local
# extensions. Registering ZPAS in one registry does not affect another registry.
registry2 = HL7Registry()
print("\nregistry2 knows ZPAS:", registry2.get_segment("ZPAS") is not None)
print("registry knows ZPAS:", registry.get_segment("ZPAS") is not None)
