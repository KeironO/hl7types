hl7types
========

``hl7types`` provides typed, Pydantic-powered Python models for HL7 v2 messages, segments, and
datatypes, with built-in ER7 (pipe-delimited) and XML serialisation. Models are generated directly
from the HL7 specification, giving you full type safety, IDE autocompletion, and validation out of
the box.

HL7 v2 is the most widely deployed healthcare messaging standard in the world, used to exchange
clinical and administrative data between hospital systems, laboratories, pharmacies, and other
healthcare applications.

.. note::

   HL7® is a registered trademark owned by `Health Level Seven International
   <https://www.hl7.org/legal/trademarks.cfm>`_.

Features
--------

- Typed Pydantic v2 models for all HL7 v2 messages, segments, groups, and datatypes.
- ER7 (pipe-delimited) encoding and decoding via ``model_dump_er7`` / ``model_validate_er7``.
- XML encoding and decoding via ``model_dump_xml`` / ``model_validate_xml``.
- Human-readable field aliases alongside positional names and HL7 dot notation (e.g. ``MSH.3``).
- Strict decoding by default. Opt-out lenient mode via ``strict=False``.
- ``HL7Registry`` for registering custom Z-segments and vendor-specific message classes.
- Conformance profile support: parse an HL7 v2 profile XML file and apply its field-level
  constraints to the standard segment classes via the registry.
- ``errs_from_exception`` converts any Pydantic ``ValidationError`` into spec-compliant ``ERR``
  segments, with the correct structure produced automatically for every supported HL7 version.
- HL7 v2.7+ truncation character support: five-character ``MSH.2`` strings (e.g. ``^~\\&#``)
  are parsed, enforced, and round-tripped correctly.

Supported versions
------------------

All major releases of the HL7 v2 specification are available. Each version is exposed as a
sub-package under ``hl7types.hl7.<version>``, where the version string uses underscores in place
of dots, so v2.5.1 is at ``hl7types.hl7.v2_5_1``.

.. toctree::
   :maxdepth: 2
   :caption: Contents
   :hidden:

   getting_started
   decoding
   validation
   registry
   conformance
   errors
   api
   hl7_reference
   changelog
   contributing
