Conformance Profiles
====================

The HL7 v2 specification is deliberately permissive. Most fields are optional, many fields
accept free-text values, and the same information can often be expressed in several different
ways. This flexibility makes the standard adaptable to a wide range of use cases, but it also
means that two systems can each produce perfectly valid HL7 messages and still fail to
interoperate, because each made different assumptions about what the other would send.

Conformance profiles address this problem by constraining a base message specification for a
specific use case or integration. A profile eliminates ambiguity by declaring precisely which
fields are required, which are forbidden, what coded values are permitted, and what length limits
apply. Both the sending and receiving system can independently validate their implementation
against the same profile, giving each side a concrete and verifiable claim of conformance before
go-live.

A profile captures both the static structure of the message (field usage, cardinality, length,
permitted table values) and enough metadata to identify the message type, version, and the
context it is intended for.

How it works
------------

The conformance profile support in ``hl7types`` is built entirely on top of ``HL7Registry``. The
registry is the same mechanism used to register Z-segments and custom message classes, and it
works well for this use case too: swapping in a constrained subclass in place of a standard
generated one, transparently, without changing any decoding or validation code.

When ``build_registry_from_profile`` runs, it walks the profile's segment tree and for each
segment that has constraints worth enforcing, it dynamically creates a Pydantic subclass of the
standard generated segment with the appropriate field overrides applied. That subclass is then
registered in the registry under the segment's three-letter name.

From that point on, every part of the system that consults the registry, ``decode_er7``,
direct model construction using a retrieved class, or any downstream validation, automatically
picks up the constrained version. No specialised profile-aware decoding path is needed. The
profile constraints are just Pydantic field definitions, and Pydantic enforces them the same way
it enforces everything else.

The full registry feature set is also available alongside profiles. You can register Z-segments
and custom message classes in the same registry that holds your profile-constrained segments and
they all work together. A single registry can represent a complete interface specification: the
message structure, any vendor extensions, and the field-level conformance rules, all resolved in
one place during decoding.

Profile files
-------------

Conformance profiles are encoded as XML files with a schema defined by the HL7 organisation.
They can be authored by hand, but in practice they are usually generated using a tool such as
the HL7 Messaging Workbench, which provides a structured editor for defining constraints and can
export the finished profile to the XML format that ``hl7types`` expects.

A profile file looks like this:

.. code-block:: xml

   <HL7v2xConformanceProfile HL7Version="2.5" ProfileType="HL7">
     <MetaData Name="test a01 spec" OrgName="" Version="" Status="" />
     <Encodings>
       <Encoding>ER7</Encoding>
     </Encodings>
     <DynamicDef AccAck="NE" AppAck="AL" MsgAckMode="Deferred" />
     <HL7v2xStaticDef MsgType="ADT" EventType="A01" MsgStructID="ADT_A01" Role="Sender">
       <Segment Name="MSH" LongName="Message Header" Usage="R" Min="1" Max="1">
         <Field Name="Field Separator" Usage="R" Min="1" Max="1" Datatype="ST" Length="1" ItemNo="00001" />
         ...
       </Segment>
       <Segment Name="PID" LongName="Patient Identification" Usage="R" Min="1" Max="1">
         <Field Name="Patient Identifier List" Usage="R" Min="1" Max="*" Datatype="CX" Length="20" ItemNo="00106" />
         ...
       </Segment>
     </HL7v2xStaticDef>
   </HL7v2xConformanceProfile>

The tables file is separate and lists the permitted codes for each referenced table:

.. code-block:: xml

   <Specification SpecName="admit - visit notification" HL7Version="2.4">
     <hl7tables>
       <hl7table id="0001" name="Administrative sex">
         <tableElement code="A" description="Ambiguous" />
         <tableElement code="F" description="Female" />
         <tableElement code="M" description="Male" />
         <tableElement code="N" description="Not applicable" />
         <tableElement code="O" description="Other" />
         <tableElement code="U" description="Unknown" />
       </hl7table>
       ...
     </hl7tables>
   </Specification>

Parsing a profile
-----------------

Profiles are parsed from the HL7 v2 conformance profile XML format with ``parse_profile``:

.. code-block:: python

   from hl7types.profiles.parser import parse_profile

   profile = parse_profile("/path/to/ADT_A01.xml")

   print(profile.hl7_version)   # e.g. "2.5"
   print(profile.msg_type)      # e.g. "ADT"
   print(profile.event_type)    # e.g. "A01"

The returned ``ProfileConstraints`` object holds the full tree of segment and field constraints
defined in the profile.

Parsing tables
--------------

Profiles often reference coded tables that restrict what values a field may carry. These are
supplied separately as a tables XML file and parsed with ``parse_tables``:

.. code-block:: python

   from hl7types.profiles.parser import parse_tables

   tables = parse_tables("/path/to/sampleTables.xml")

The result is a ``dict[str, set[str]]`` mapping each table ID to the set of valid codes. Pass
this to ``build_registry_from_profile`` to have table constraints enforced at validation time.

Building a registry from a profile
------------------------------------

``build_registry_from_profile`` walks the parsed profile and registers a constrained subclass
for each segment that has field-level rules. Segments with no constraints are left as-is:

.. code-block:: python

   from hl7types import HL7Registry, decode_er7
   from hl7types.profiles.builder import build_registry_from_profile
   from hl7types.profiles.parser import parse_profile, parse_tables

   tables = parse_tables("/path/to/sampleTables.xml")
   profile = parse_profile("/path/to/ADT_A01.xml")

   registry = HL7Registry()
   build_registry_from_profile(profile, registry, tables=tables)

   msg = decode_er7(wire, registry=registry, strict=True)

When ``decode_er7`` resolves a segment, it consults the registry and uses the constrained class
if one is registered. Field usage, length, and table constraints from the profile are then
enforced by Pydantic as part of normal model validation.

What constraints are applied
-----------------------------

Each field in a profile carries a usage value that defines whether the field must be present,
may be present, or must be absent. The full set of usage values defined by the HL7 specification
is:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Value
     - Name
     - Meaning
   * - ``R``
     - Required
     - The field must be present and non-empty. A missing value is a conformance failure.
   * - ``RE``
     - Required but may be empty
     - The field must be present in the message but may carry an empty value.
   * - ``O``
     - Optional
     - The field may be present or absent. No constraint is applied.
   * - ``C``
     - Conditional
     - The field is required or optional depending on the value of another field. The predicate
       is defined in the profile but is not currently enforced at the field level.
   * - ``B``
     - Backward compatible
     - The field exists for compatibility with an earlier version and should not be used in new
       implementations. No constraint is applied.
   * - ``X``
     - Not used
     - The field must not be present. Any value raises a ``ValidationError``.

The builder applies the following rules from the profile to each field:

- **Required** (``R``) - the field is made non-optional. A missing value raises a
  ``ValidationError``.
- **Not used** (``X``) - the field type is set to ``None``. Any value present raises a
  ``ValidationError``.
- **Max length** - a ``max_length`` constraint is added to string fields.
- **Table** - an ``AfterValidator`` is added that rejects any value not present in the
  referenced table. Only applied when the table ID appears in the tables dict passed to
  ``build_registry_from_profile``.

Usage values ``O``, ``C``, ``B``, and ``RE`` produce no field-level constraint beyond what the
base class already enforces.

Constrained segment classes are named with a prefix followed by the segment name. The default
prefix is ``Profile``, giving names like ``ProfilePID`` and ``ProfileMSH``.

Inspecting constrained classes
-------------------------------

After building the registry you can pull out any constrained segment class directly with
``get_segment`` and compare it against the base class to confirm the profile was applied:

.. code-block:: python

   from hl7types.hl7.v2_5.segments.PID import PID as BasePID

   ConformedPID = registry.get_segment("PID")

   print(BasePID)        # <class 'hl7types.hl7.v2_5.segments.PID.PID'>
   print(ConformedPID)   # <class 'hl7types.hl7.v2_5.segments.PID.ProfilePID'>

``get_segment`` returns ``None`` if no constrained class was registered for that name, which
happens when the profile defines no constraints that differ from the base class. In that case
the decoder falls back to the standard generated class automatically.

You can also use the constrained class directly to build segments programmatically and have the
profile rules enforced at construction time rather than at decode time:

.. code-block:: python

   from hl7types.hl7.v2_5.datatypes.CX import CX
   from hl7types.hl7.v2_5.datatypes.XPN import XPN
   from hl7types.hl7.v2_5.datatypes.FN import FN
   from hl7types.hl7.v2_5.datatypes.HD import HD

   ConformedPID = registry.get_segment("PID")

   pid = ConformedPID(
       pid_3=[CX(cx_1="M03131", cx_4=HD(hd_1="WPAS"), cx_5="PI")],
       pid_5=[XPN(xpn_1=FN(fn_1="Jones"), xpn_2="Will")],
       pid_8="M",
   )

Any field that violates the profile, a value outside a permitted table, a string exceeding the
maximum length, or a required field left empty, raises a ``ValidationError`` immediately without
needing to round-trip through ER7.
