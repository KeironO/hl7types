The HL7 Registry
================

Unfortunately, real-world HL7 v2 deployments rarely conform to the specification alone. It is
common to extend  the standard with proprietary Z-segments: custom segments whose names begin
with ``Z`` and which carry data the specification never anticipated.

A ``ZPID`` might carry a specific patient identifier. A ``ZWCC`` might carry workflow
metadata that drives downstream processing in a particular clinical system.

The problem this creates is that a library which only understands the published specification
cannot be used as-is in most production environments. Either the application has to strip
Z-segments before decoding, losing information, or it has to work around the library entirely.

``HL7Registry`` attempts to solves this. It is a lightweight container that maps segment names
and message type identifiers to Pydantic model classes.

When ``decode_er7`` encounters a segment or message type it does not recgonise in the
specification, it consults the registry before giving up.

Registering a Z-segment
------------------------

Define a Pydantic model for the Z-segment and register it against its three-letter name:

.. code-block:: python

   from typing import Optional
   from pydantic import Field
   from hl7types.hl7 import HL7Model
   from hl7types import HL7Registry

   class ZWCC(HL7Model):
       zwcc_1: Optional[str] = Field(None, serialization_alias="ZWCC.1")
       zwcc_2: Optional[str] = Field(None, serialization_alias="ZWCC.2")

   registry = HL7Registry()
   registry.register_segment("ZWCC", ZWCC)

Registering a custom message
-----------------------------

If the receiving application sends a non-standard message type, or if you want to define a custom
message structure that includes Z-segments, register it against a version and message name:

.. code-block:: python

   from typing import Optional
   from hl7types.hl7.v2_5_1.segments import MSA, MSH

   _ZWCC = ZWCC  # local alias required to avoid name shadowing in the model body

   class WCCACKMessage(HL7Model):
       MSH: MSH
       MSA: MSA
       ZWCC: Optional[_ZWCC] = None

   registry.register_message("2.5.1", "ACK", WCCACKMessage)

Decoding with a registry
-------------------------

Pass the registry to ``decode_er7``. The decoder will use it to resolve both the message class
and any Z-segments encountered in the wire:

.. code-block:: python

   from hl7types import decode_er7

   wire = (
       "MSH|^~\\&|WPAS||SEND||20260101120000||ACK|MSG000002|P|2.5.1\r"
       "MSA|AA|MSG000001\r"
       "ZWCC|WPAS|20260101120000\r"
   )

   msg = decode_er7(wire, registry=registry)
   print(msg.ZWCC.zwcc_1)  # "WPAS"

Extending an existing message with inheritance
----------------------------------------------

Rather than defining a message structure from scratch, you can subclass an existing generated
message and add only the fields that differ. This is the preferred approach when a supplier sends a
standard message type but appends one or more Z-segments to it, the base class carries all the
standard segment definitions and validation, and the subclass adds what is specific to that
integration.

.. code-block:: python

   from typing import Optional
   from hl7types.hl7.v2_5_1.messages import ACK

   _ZWCC = ZWCC

   class CustomACK(ACK):
       ZWCC: Optional[_ZWCC] = None

   registry = HL7Registry()
   registry.register_segment("ZWCC", ZWCC)
   registry.register_message("2.5.1", "ACK", CustomACK)


``CustomACK`` inherits ``MSH`` and ``MSA`` from :ref:`ACK <hl7-v2_5_1-ACK>` exactly as defined
in the specification, including all their field-level validation. Only ``ZWCC`` is new. When the
decoder resolves an ACK for version 2.5.1, it will find ``CustomACK`` in the registry and use it
in place of the generated class.

If the same supplier appends Z-segments to multiple message types, each can be subclassed
independently and registered against its own name, all sharing the same ``ZWCC`` segment definition.

Protected segments
------------------

``MSH``, ``FHS``, and ``BHS`` cannot be registered or overridden. These are delimiter-definition
segments: the decoder reads the field separator and encoding characters directly from their raw
bytes before any model is consulted. Allowing them to be replaced would break the decoding
pipeline at its foundation. Attempting to register one raises immediately:

.. code-block:: python

   registry.register_segment("MSH", ZWCC)
   # ValueError: 'MSH' is a delimiter-definition segment and cannot be overridden

Registry isolation
------------------

Each ``HL7Registry`` instance is entirely independent. There is no global mutable state shared
between registries, which means concurrent pipelines serving different integrations can
each maintain their own set of extensions without interference within the same application.
