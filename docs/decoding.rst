Decoding ER7
============

``hl7types`` decodes ER7 wire strings into fully typed Pydantic models through a multi-stage
pipeline.

Segment splitting
-----------------

The first step of the encoder is splitting the ER7 wire string into individual segment strings. The HL7 v2
specification mandates a carriage return (``\r``) as the segment terminator. In
practice the decoder is tolerant of ``\n`` and ``\r\n`` as well, but any system producing or
consuming HL7 over a real interface will use ``\r``.

Encoding character detection
-----------------------------

Before any field can be parsed, the decoder needs to know which characters serve as delimiters.
These are declared in the opening delimiter segment,  always :ref:`MSH <hl7-v2_5_1-MSH>`,
:ref:`FHS <hl7-v2_5_1-FHS>`, or :ref:`BHS <hl7-v2_5_1-BHS>`.

The field separator is read directly from position 3 of the segment string (not from a parsed
field,  it cannot be, since it defines how fields are parsed). The remaining four encoding
characters,  component separator, repetition separator, escape character, and subcomponent
separator,  are read from the next field, conventionally ``^~\&``.

The defaults are:

- ``|``: field separator
- ``^``: component separator
- ``~``: repetition separator
- ``\``: escape character
- ``&``: subcomponent separator

Non-standard delimiters are fully supported. If a message arrives with a different field separator
the decoder detects it from the raw bytes and applies it consistently throughout.

Message type resolution
-----------------------

When no message class is provided to ``decode_er7``, the decoder resolves one automatically by
inspecting :ref:`MSH <hl7-v2_5_1-MSH>`:

- **MSH.9** carries the message type and trigger event (e.g. ``ADT^A01^ADT_A01``). The decoder
  prefers the third component (the explicit structure name) if present, otherwise constructs it
  from the first two components.
- **MSH.12** carries the HL7 version (e.g. ``2.5.1``), which determines which version sub-package
  to import from.

The resolved class is then imported dynamically, so passing an ER7 wire string containing
``MSH.9 = ADT^A01`` and ``MSH.12 = 2.5.1`` will automatically load
``hl7types.hl7.v2_5_1.messages.ADT_A01``. An unknown version or message type raises a
``ValueError`` at this point rather than at field access time.

Field and component parsing
----------------------------

With encoding characters known and a model class resolved, each segment is tokenised and matched
against the model's field positions. Field positions are derived from the Pydantic
``serialization_alias`` on each field,  ``MSH.9`` maps to position 9, ``PID.3`` to position 3,
and so on.

The parsing hierarchy mirrors the HL7 wire hierarchy:

1. **Fields** are split on the field separator (``|``).
2. **Repetitions** within a field are split on the repetition separator (``~``). Trailing empty
   repetitions are dropped rather than preserved as empty strings.
3. **Components** within a repetition are split on the component separator (``^``).
4. **Subcomponents** within a component are split on the subcomponent separator (``&``).

Whether a field is expected to be a scalar, a composite datatype (another ``HL7Model``), or a
list of either is determined entirely by the type annotations on the model,  no runtime
configuration is needed.

Escape sequences
-----------------

Escape sequences in field values are resolved after tokenisation. The five standard sequences are:

- ``\F\`` to ``|`` (field separator)
- ``\S\`` to ``^`` (component separator)
- ``\T\`` to ``&`` (subcomponent separator)
- ``\R\`` to ``~`` (repetition separator)
- ``\E\`` to ``\`` (escape character)

This behaviour is derived from HAPI (the reference Java HL7 implementation). Unknown escape
sequences,  such as ``\H\``, ``\N\``, or ``\.br\``, which are presentation-layer formatting
hints are left untouched rather than raising an error.

See :doc:`validation` for details on field-level validation and strict verses lenient decoding.
