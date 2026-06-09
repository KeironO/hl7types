Validation
==========

``hl7types`` applies validation at two distinct levels: structural validation, which checks that
required segments and fields are present in a message, and field-level validation, which checks
that individual field values conform to the format defined by the HL7 specification.

Both levels apply regardless of how a model is constructed. Whether you decode a message from a
wire string or build one programmatically by passing values to a model constructor, the same
validators run. A value that would be rejected during decoding will be rejected at construction
time too, and vice versa.

.. code-block:: python

   from pydantic import ValidationError
   from hl7types.hl7.v2_5_1.datatypes import DT

   # Accepted,  valid HL7 date
   d = DT(value="20260101")

   # Rejected,  invalid format, whether from wire or code
   try:
       DT(value="01-01-2026")
   except ValidationError as e:
       print(e)

Strict and lenient decoding
--------------------------------------

Once the decoder has parsed the wire string, it passes the collected field data to Pydantic's
``model_validate``. Whether missing required segments and fields cause an error or are silently
tolerated is controlled by the ``strict`` parameter.

**Strict mode** (``strict=True``, the default) performs structural validation: any required
segment or field that is absent from the wire causes Pydantic to raise a ``ValidationError``
immediately, with a precise error message identifying every missing field. This is the safest
option when you control both ends of the interface and can rely on the sender conforming to the
specification. Strict mode is the default for ``decode_er7``, ``model_validate_er7``, and
``decode_er7_segment``.

**Lenient mode** (``strict=False``) is opt-in and designed for integration with real-world
systems that routinely omit technically required fields,  a common reality in HL7 v2 deployments.
Rather than raising, the decoder injects placeholder values for any missing required field before
calling ``model_validate``:

- Missing required scalar fields receive an empty string (``""``).
- Missing required composite fields receive an empty dict (``{}``), which Pydantic constructs
  into a zero-value model instance.
- Missing required repeating fields receive an empty list (``[]``).

A ``UserWarning`` is emitted for every segment where placeholders were injected, listing the
affected field names. This means lenient decoding never silently discards information,  the
warning tells you exactly what was missing.

.. code-block:: python

   import warnings
   from hl7types import decode_er7
   from pydantic import ValidationError

   # Strict (default),  raises ValidationError on missing required segments
   try:
       msg = decode_er7(wire)
   except ValidationError as e:
       print(e)

   # Lenient (opt-in),  injects placeholders and warns
   with warnings.catch_warnings(record=True) as caught:
       msg = decode_er7(wire, strict=False)
       for w in caught:
           print(w.message)

The same ``strict`` parameter is accepted by ``model_validate_er7`` on any ``HL7Model`` subclass
and by ``decode_er7_segment`` for single-segment decoding. All three default to ``strict=True``.

Field-level validation
-----------------------

Field-level validation is independent of strict mode, it runs regardless, and always raises
``ValidationError`` on a format violation. This validation is baked directly into the generated
model classes as Pydantic ``@field_validator`` methods. Because the validators live on the model
itself rather than in the decoder, they fire identically whether a value arrives from a decoded
wire string, is passed to the constructor directly, or is loaded via ``model_validate`` from a
dict.

For most primitive types,  ``ST``, ``TX``, ``FT``, ``ID``, ``IS``,  the only constraint is
``max_length``. For structured primitive types, the validators apply regex patterns taken verbatim
from HAPI's ``DefaultValidationWithoutTNBuilder``, the reference Java HL7 implementation. The
patterns use ``re.fullmatch``, meaning the entire value must conform,  a partial match is a
failure.

.. list-table::
   :header-rows: 1
   :widths: auto

   * - HL7 type
     - Accepts
     - Valid examples
   * - ``SI`` (Sequence ID)
     - Empty or a non-negative integer
     - ``1``, ``42``, ``""``
   * - ``NM`` (Numeric)
     - Empty or a signed decimal
     - ``42``, ``-3.14``, ``+100``, ``.5``, ``""``
   * - ``DT`` (Date)
     - ``YYYY``, ``YYYYMM``, or ``YYYYMMDD``
     - ``2026``, ``202601``, ``20260101``
   * - ``TM`` (Time)
     - ``HH`` through ``HHMMSS.SSSS``, with optional ``+/-HHMM`` timezone
     - ``12``, ``1230``, ``123045``, ``123045.1234``, ``123045+0100``
   * - ``DTM`` (Date/Time)
     - Any truncated datetime from ``YYYY`` up to ``YYYYMMDDHHMMSS.SSSS``, with optional timezone
     - ``2026``, ``20260101``, ``202601011230``, ``20260101123045.1234+0100``
   * - ``NULLDT``
     - Must be empty,  this is a withdrawn datatype
     - ``""``

Pre-v2.5 timestamp handling
-----------------------------

In HL7 versions before v2.5, the ``TS`` (timestamp) datatype exposes its first component
(``TS.1``) with a base type of ``ST`` in the XSD rather than a dedicated datetime type. The
code generator detects this by field name and applies a dedicated pre-v2.5 datetime pattern to
those fields, ensuring consistent validation behaviour across all supported versions without
requiring any special handling at runtime.
