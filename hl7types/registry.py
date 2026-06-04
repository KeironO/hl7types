from __future__ import annotations

from pydantic import BaseModel

_PROTECTED_SEGMENTS = {"MSH", "FHS", "BHS"}


class HL7Registry:
    """Registry for custom HL7 v2 segment and message classes.

    Real-world HL7 deployments commonly extend the specification with
    vendor-specific Z-segments. ``HL7Registry`` maps segment names and
    message type identifiers to Pydantic model classes so that
    :func:`hl7types.decode_er7` can resolve them during decoding.

    Each registry instance is entirely independent — there is no shared
    global state — so concurrent pipelines with different vendor extensions
    can each hold their own registry without interference.

    Examples
    --------
    >>> from typing import Optional
    >>> from pydantic import Field
    >>> from hl7types.hl7 import HL7Model
    >>> from hl7types.hl7.v2_5_1.messages import ACK
    >>> from hl7types import HL7Registry
    >>>
    >>> class ZWCC(HL7Model):
    ...     zwcc_1: Optional[str] = Field(None, serialization_alias="ZWCC.1")
    ...
    >>> _ZWCC = ZWCC
    >>>
    >>> class VendorACK(ACK):
    ...     ZWCC: Optional[_ZWCC] = None
    ...
    >>> registry = HL7Registry()
    >>> registry.register_segment("ZWCC", ZWCC)
    >>> registry.register_message("2.5.1", "ACK", VendorACK)
    """

    def __init__(self) -> None:
        self._segments: dict[str, type[BaseModel]] = {}
        self._messages: dict[tuple[str, str], type[BaseModel]] = {}

    def register_segment(self, name: str, cls: type[BaseModel], *, override: bool = False) -> None:
        """Register a custom segment class against its three-letter name.

        Parameters
        ----------
        name : str
            The HL7 segment name, e.g. ``"ZWCC"``. Must not be one of the
            protected delimiter-definition segments (``MSH``, ``FHS``,
            ``BHS``) unless ``override`` is ``True``.
        cls : type[BaseModel]
            The Pydantic model class to use when this segment is encountered
            during decoding.
        override : bool
            If ``True``, bypass protection for delimiter-definition segments
            (``MSH``, ``FHS``, ``BHS``). Defaults to ``False``.

        Raises
        ------
        ValueError
            If ``name`` is a protected delimiter-definition segment and
            ``override`` is ``False``.
        """
        if name in _PROTECTED_SEGMENTS and not override:
            raise ValueError(f"{name!r} is a delimiter-definition segment and cannot be overridden")
        self._segments[name] = cls

    def get_segment(self, name: str) -> type[BaseModel] | None:
        """Look up a registered segment class by name.

        Parameters
        ----------
        name : str
            The HL7 segment name to look up.

        Returns
        -------
        type[BaseModel] or None
            The registered class, or ``None`` if no class is registered for
            that name.
        """
        return self._segments.get(name)

    def has_segment_class(self, cls: type[BaseModel]) -> bool:
        """Return whether a class is registered as a segment.

        Parameters
        ----------
        cls : type[BaseModel]
            The class to check.

        Returns
        -------
        bool
            ``True`` if ``cls`` is registered as a segment in this registry.
        """
        return cls in self._segments.values()

    def register_message(self, version: str, name: str, cls: type[BaseModel]) -> None:
        """Register a custom message class against a version and message name.

        Parameters
        ----------
        version : str
            The HL7 version string as it appears in MSH.12, e.g. ``"2.5.1"``.
        name : str
            The message structure name as it appears in MSH.9, e.g. ``"ACK"``
            or ``"ADT_A01"``.
        cls : type[BaseModel]
            The Pydantic model class to use when this message type is decoded
            for the given version.
        """
        self._messages[(version, name)] = cls

    def get_message(self, version: str, name: str) -> type[BaseModel] | None:
        """Look up a registered message class by version and name.

        Parameters
        ----------
        version : str
            The HL7 version string, e.g. ``"2.5.1"``.
        name : str
            The message structure name, e.g. ``"ACK"``.

        Returns
        -------
        type[BaseModel] or None
            The registered class, or ``None`` if no class is registered for
            that version and name combination.
        """
        return self._messages.get((version, name))


_default_registry = HL7Registry()


def register_segment(name: str, cls: type[BaseModel]) -> None:
    _default_registry.register_segment(name, cls)


def register_message(version: str, name: str, cls: type[BaseModel]) -> None:
    _default_registry.register_message(version, name, cls)
