v2.5 Messages
=============

.. _hl7-v2_5-ACK:

.. py:class:: hl7types.hl7.v2_5.messages.ACK.ACK
   :noindex:

   HL7 v2 ACK message.

ACK
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating

.. _hl7-v2_5-ADR_A19:

.. py:class:: hl7types.hl7.v2_5.messages.ADR_A19.ADR_A19
   :noindex:

   HL7 v2 ADR_A19 message.

ADR_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_5-ADR_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-ADT_A01:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A01.ADT_A01
   :noindex:

   HL7 v2 ADT_A01 message.

ADT_A01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_5-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_5-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_5-UB1>`]
     - optional
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_5-UB2>`]
     - optional
     - UB2: Optional
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_5-PDA>`]
     - optional
     - PDA: Optional

.. _hl7-v2_5-ADT_A02:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A02.ADT_A02
   :noindex:

   HL7 v2 ADT_A02 message.

ADT_A02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_5-PDA>`]
     - optional
     - PDA: Optional

.. _hl7-v2_5-ADT_A03:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A03.ADT_A03
   :noindex:

   HL7 v2 ADT_A03 message.

ADT_A03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_5-ADT_A03_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A03_INSURANCE <hl7-v2_5-ADT_A03_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_5-PDA>`]
     - optional
     - PDA: Optional

.. _hl7-v2_5-ADT_A05:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A05.ADT_A05
   :noindex:

   HL7 v2 ADT_A05 message.

ADT_A05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_5-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_5-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_5-UB1>`]
     - optional
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_5-UB2>`]
     - optional
     - UB2: Optional

.. _hl7-v2_5-ADT_A06:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A06.ADT_A06
   :noindex:

   HL7 v2 ADT_A06 message.

ADT_A06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_5-MRG>`]
     - optional
     - MRG: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_5-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_5-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_5-UB1>`]
     - optional
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_5-UB2>`]
     - optional
     - UB2: Optional

.. _hl7-v2_5-ADT_A09:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A09.ADT_A09
   :noindex:

   HL7 v2 ADT_A09 message.

ADT_A09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating

.. _hl7-v2_5-ADT_A12:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A12.ADT_A12
   :noindex:

   HL7 v2 ADT_A12 message.

ADT_A12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_5-DG1>`]
     - optional
     - DG1: Optional

.. _hl7-v2_5-ADT_A15:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A15.ADT_A15
   :noindex:

   HL7 v2 ADT_A15 message.

ADT_A15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating

.. _hl7-v2_5-ADT_A16:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A16.ADT_A16
   :noindex:

   HL7 v2 ADT_A16 message.

ADT_A16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A16_PROCEDURE <hl7-v2_5-ADT_A16_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A16_INSURANCE <hl7-v2_5-ADT_A16_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional

.. _hl7-v2_5-ADT_A17:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A17.ADT_A17
   :noindex:

   HL7 v2 ADT_A17 message.

ADT_A17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating

.. _hl7-v2_5-ADT_A18:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A18.ADT_A18
   :noindex:

   HL7 v2 ADT_A18 message.

ADT_A18
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_5-MRG>`
     - required
     - MRG: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_5-ADT_A20:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A20.ADT_A20
   :noindex:

   HL7 v2 ADT_A20 message.

ADT_A20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``NPU``
     -
     - :ref:`NPU <hl7-v2_5-NPU>`
     - required
     - NPU: Required

.. _hl7-v2_5-ADT_A21:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A21.ADT_A21
   :noindex:

   HL7 v2 ADT_A21 message.

ADT_A21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating

.. _hl7-v2_5-ADT_A24:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A24.ADT_A24
   :noindex:

   HL7 v2 ADT_A24 message.

ADT_A24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_5-PV1>`]
     - optional
     - PV1: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating

.. _hl7-v2_5-ADT_A30:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A30.ADT_A30
   :noindex:

   HL7 v2 ADT_A30 message.

ADT_A30
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_5-MRG>`
     - required
     - MRG: Required

.. _hl7-v2_5-ADT_A37:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A37.ADT_A37
   :noindex:

   HL7 v2 ADT_A37 message.

ADT_A37
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_5-PV1>`]
     - optional
     - PV1: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating

.. _hl7-v2_5-ADT_A38:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A38.ADT_A38
   :noindex:

   HL7 v2 ADT_A38 message.

ADT_A38
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_5-OBX>`]]
     - optional
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional

.. _hl7-v2_5-ADT_A39:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A39.ADT_A39
   :noindex:

   HL7 v2 ADT_A39 message.

ADT_A39
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_5-ADT_A39_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-ADT_A43:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A43.ADT_A43
   :noindex:

   HL7 v2 ADT_A43 message.

ADT_A43
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_5-ADT_A43_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-ADT_A45:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A45.ADT_A45
   :noindex:

   HL7 v2 ADT_A45 message.

ADT_A45
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``MERGE_INFO``
     -
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_5-ADT_A45_MERGE_INFO>`]
     - required
     - MERGE_INFO: Required, repeating

.. _hl7-v2_5-ADT_A50:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A50.ADT_A50
   :noindex:

   HL7 v2 ADT_A50 message.

ADT_A50
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_5-MRG>`
     - required
     - MRG: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required

.. _hl7-v2_5-ADT_A52:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A52.ADT_A52
   :noindex:

   HL7 v2 ADT_A52 message.

ADT_A52
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional

.. _hl7-v2_5-ADT_A54:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A54.ADT_A54
   :noindex:

   HL7 v2 ADT_A54 message.

ADT_A54
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional

.. _hl7-v2_5-ADT_A60:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A60.ADT_A60
   :noindex:

   HL7 v2 ADT_A60 message.

ADT_A60
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_5-PV1>`]
     - optional
     - PV1: Optional
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``IAM``
     -
     - Optional[List[:ref:`IAM <hl7-v2_5-IAM>`]]
     - optional
     - IAM: Optional, repeating

.. _hl7-v2_5-ADT_A61:

.. py:class:: hl7types.hl7.v2_5.messages.ADT_A61.ADT_A61
   :noindex:

   HL7 v2 ADT_A61 message.

ADT_A61
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional

.. _hl7-v2_5-BAR_P01:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P01.BAR_P01
   :noindex:

   HL7 v2 BAR_P01 message.

BAR_P01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - List[:ref:`BAR_P01_VISIT <hl7-v2_5-BAR_P01_VISIT>`]
     - required
     - VISIT: Required, repeating

.. _hl7-v2_5-BAR_P02:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P02.BAR_P02
   :noindex:

   HL7 v2 BAR_P02 message.

BAR_P02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_5-BAR_P02_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-BAR_P05:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P05.BAR_P05
   :noindex:

   HL7 v2 BAR_P05 message.

BAR_P05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - List[:ref:`BAR_P05_VISIT <hl7-v2_5-BAR_P05_VISIT>`]
     - required
     - VISIT: Required, repeating

.. _hl7-v2_5-BAR_P06:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P06.BAR_P06
   :noindex:

   HL7 v2 BAR_P06 message.

BAR_P06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_5-BAR_P06_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-BAR_P10:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P10.BAR_P10
   :noindex:

   HL7 v2 BAR_P10 message.

BAR_P10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``GP1``
     -
     - :ref:`GP1 <hl7-v2_5-GP1>`
     - required
     - GP1: Required
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`BAR_P10_PROCEDURE <hl7-v2_5-BAR_P10_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating

.. _hl7-v2_5-BAR_P12:

.. py:class:: hl7types.hl7.v2_5.messages.BAR_P12.BAR_P12
   :noindex:

   HL7 v2 BAR_P12 message.

BAR_P12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`BAR_P12_PROCEDURE <hl7-v2_5-BAR_P12_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating

.. _hl7-v2_5-BPS_O29:

.. py:class:: hl7types.hl7.v2_5.messages.BPS_O29.BPS_O29
   :noindex:

   HL7 v2 BPS_O29 message.

BPS_O29
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`BPS_O29_PATIENT <hl7-v2_5-BPS_O29_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`BPS_O29_ORDER <hl7-v2_5-BPS_O29_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-BRP_O30:

.. py:class:: hl7types.hl7.v2_5.messages.BRP_O30.BRP_O30
   :noindex:

   HL7 v2 BRP_O30 message.

BRP_O30
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`BRP_O30_RESPONSE <hl7-v2_5-BRP_O30_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-BRT_O32:

.. py:class:: hl7types.hl7.v2_5.messages.BRT_O32.BRT_O32
   :noindex:

   HL7 v2 BRT_O32 message.

BRT_O32
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`BRT_O32_RESPONSE <hl7-v2_5-BRT_O32_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-BTS_O31:

.. py:class:: hl7types.hl7.v2_5.messages.BTS_O31.BTS_O31
   :noindex:

   HL7 v2 BTS_O31 message.

BTS_O31
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`BTS_O31_PATIENT <hl7-v2_5-BTS_O31_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`BTS_O31_ORDER <hl7-v2_5-BTS_O31_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-CRM_C01:

.. py:class:: hl7types.hl7.v2_5.messages.CRM_C01.CRM_C01
   :noindex:

   HL7 v2 CRM_C01 message.

CRM_C01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PATIENT``
     -
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5-CRM_C01_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-CSU_C09:

.. py:class:: hl7types.hl7.v2_5.messages.CSU_C09.CSU_C09
   :noindex:

   HL7 v2 CSU_C09 message.

CSU_C09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PATIENT``
     -
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_5-CSU_C09_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-DFT_P03:

.. py:class:: hl7types.hl7.v2_5.messages.DFT_P03.DFT_P03
   :noindex:

   HL7 v2 DFT_P03 message.

DFT_P03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_5-PV1>`]
     - optional
     - PV1: Optional
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_5-DFT_P03_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER: Optional, repeating
   * - ``FINANCIAL``
     -
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_5-DFT_P03_FINANCIAL>`]
     - required
     - FINANCIAL: Required, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_5-DFT_P03_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional

.. _hl7-v2_5-DFT_P11:

.. py:class:: hl7types.hl7.v2_5.messages.DFT_P11.DFT_P11
   :noindex:

   HL7 v2 DFT_P11 message.

DFT_P11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_5-ROL>`]]
     - optional
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_5-PV1>`]
     - optional
     - PV1: Optional
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_5-PV2>`]
     - optional
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_5-DB1>`]]
     - optional
     - DB1: Optional, repeating
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_5-DFT_P11_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_5-DRG>`]
     - optional
     - DRG: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`DFT_P11_INSURANCE <hl7-v2_5-DFT_P11_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``FINANCIAL``
     -
     - List[:ref:`DFT_P11_FINANCIAL <hl7-v2_5-DFT_P11_FINANCIAL>`]
     - required
     - FINANCIAL: Required, repeating

.. _hl7-v2_5-DOC_T12:

.. py:class:: hl7types.hl7.v2_5.messages.DOC_T12.DOC_T12
   :noindex:

   HL7 v2 DOC_T12 message.

DOC_T12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``RESULT``
     -
     - List[:ref:`DOC_T12_RESULT <hl7-v2_5-DOC_T12_RESULT>`]
     - required
     - RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-DSR_Q01:

.. py:class:: hl7types.hl7.v2_5.messages.DSR_Q01.DSR_Q01
   :noindex:

   HL7 v2 DSR_Q01 message.

DSR_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_5-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-DSR_Q03:

.. py:class:: hl7types.hl7.v2_5.messages.DSR_Q03.DSR_Q03
   :noindex:

   HL7 v2 DSR_Q03 message.

DSR_Q03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_5-MSA>`]
     - optional
     - MSA: Optional
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_5-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-EAC_U07:

.. py:class:: hl7types.hl7.v2_5.messages.EAC_U07.EAC_U07
   :noindex:

   HL7 v2 EAC_U07 message.

EAC_U07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``COMMAND``
     -
     - List[:ref:`EAC_U07_COMMAND <hl7-v2_5-EAC_U07_COMMAND>`]
     - required
     - COMMAND: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-EAN_U09:

.. py:class:: hl7types.hl7.v2_5.messages.EAN_U09.EAN_U09
   :noindex:

   HL7 v2 EAN_U09 message.

EAN_U09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``NOTIFICATION``
     -
     - List[:ref:`EAN_U09_NOTIFICATION <hl7-v2_5-EAN_U09_NOTIFICATION>`]
     - required
     - NOTIFICATION: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-EAR_U08:

.. py:class:: hl7types.hl7.v2_5.messages.EAR_U08.EAR_U08
   :noindex:

   HL7 v2 EAR_U08 message.

EAR_U08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``COMMAND_RESPONSE``
     -
     - List[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_5-EAR_U08_COMMAND_RESPONSE>`]
     - required
     - COMMAND_RESPONSE: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-EDR_R07:

.. py:class:: hl7types.hl7.v2_5.messages.EDR_R07.EDR_R07
   :noindex:

   HL7 v2 EDR_R07 message.

EDR_R07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_5-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-EQQ_Q04:

.. py:class:: hl7types.hl7.v2_5.messages.EQQ_Q04.EQQ_Q04
   :noindex:

   HL7 v2 EQQ_Q04 message.

EQQ_Q04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQL``
     -
     - :ref:`EQL <hl7-v2_5-EQL>`
     - required
     - EQL: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-ERP_R09:

.. py:class:: hl7types.hl7.v2_5.messages.ERP_R09.ERP_R09
   :noindex:

   HL7 v2 ERP_R09 message.

ERP_R09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``ERQ``
     -
     - :ref:`ERQ <hl7-v2_5-ERQ>`
     - required
     - ERQ: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-ESR_U02:

.. py:class:: hl7types.hl7.v2_5.messages.ESR_U02.ESR_U02
   :noindex:

   HL7 v2 ESR_U02 message.

ESR_U02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-ESU_U01:

.. py:class:: hl7types.hl7.v2_5.messages.ESU_U01.ESU_U01
   :noindex:

   HL7 v2 ESU_U01 message.

ESU_U01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``ISD``
     -
     - Optional[List[:ref:`ISD <hl7-v2_5-ISD>`]]
     - optional
     - ISD: Optional, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-INR_U06:

.. py:class:: hl7types.hl7.v2_5.messages.INR_U06.INR_U06
   :noindex:

   HL7 v2 INR_U06 message.

INR_U06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``INV``
     -
     - List[:ref:`INV <hl7-v2_5-INV>`]
     - required
     - INV: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-INU_U05:

.. py:class:: hl7types.hl7.v2_5.messages.INU_U05.INU_U05
   :noindex:

   HL7 v2 INU_U05 message.

INU_U05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``INV``
     -
     - List[:ref:`INV <hl7-v2_5-INV>`]
     - required
     - INV: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-LSU_U12:

.. py:class:: hl7types.hl7.v2_5.messages.LSU_U12.LSU_U12
   :noindex:

   HL7 v2 LSU_U12 message.

LSU_U12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``EQP``
     -
     - List[:ref:`EQP <hl7-v2_5-EQP>`]
     - required
     - EQP: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-MDM_T01:

.. py:class:: hl7types.hl7.v2_5.messages.MDM_T01.MDM_T01
   :noindex:

   HL7 v2 MDM_T01 message.

MDM_T01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER: Optional, repeating
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_5-TXA>`
     - required
     - TXA: Required

.. _hl7-v2_5-MDM_T02:

.. py:class:: hl7types.hl7.v2_5.messages.MDM_T02.MDM_T02
   :noindex:

   HL7 v2 MDM_T02 message.

MDM_T02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_5-PV1>`
     - required
     - PV1: Required
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER: Optional, repeating
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_5-TXA>`
     - required
     - TXA: Required
   * - ``OBSERVATION``
     -
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_5-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION: Required, repeating

.. _hl7-v2_5-MFK_M01:

.. py:class:: hl7types.hl7.v2_5.messages.MFK_M01.MFK_M01
   :noindex:

   HL7 v2 MFK_M01 message.

MFK_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_5-MFA>`]]
     - optional
     - MFA: Optional, repeating

.. _hl7-v2_5-MFN_M01:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M01.MFN_M01
   :noindex:

   HL7 v2 MFN_M01 message.

MFN_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF``
     -
     - List[:ref:`MFN_M01_MF <hl7-v2_5-MFN_M01_MF>`]
     - required
     - MF: Required, repeating

.. _hl7-v2_5-MFN_M02:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M02.MFN_M02
   :noindex:

   HL7 v2 MFN_M02 message.

MFN_M02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_STAFF``
     -
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_5-MFN_M02_MF_STAFF>`]
     - required
     - MF_STAFF: Required, repeating

.. _hl7-v2_5-MFN_M03:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M03.MFN_M03
   :noindex:

   HL7 v2 MFN_M03 message.

MFN_M03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_TEST``
     -
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_5-MFN_M03_MF_TEST>`]
     - required
     - MF_TEST: Required, repeating

.. _hl7-v2_5-MFN_M04:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M04.MFN_M04
   :noindex:

   HL7 v2 MFN_M04 message.

MFN_M04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_CDM``
     -
     - List[:ref:`MFN_M04_MF_CDM <hl7-v2_5-MFN_M04_MF_CDM>`]
     - required
     - MF_CDM: Required, repeating

.. _hl7-v2_5-MFN_M05:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M05.MFN_M05
   :noindex:

   HL7 v2 MFN_M05 message.

MFN_M05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_LOCATION``
     -
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_5-MFN_M05_MF_LOCATION>`]
     - required
     - MF_LOCATION: Required, repeating

.. _hl7-v2_5-MFN_M06:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M06.MFN_M06
   :noindex:

   HL7 v2 MFN_M06 message.

MFN_M06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_CLIN_STUDY``
     -
     - List[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_5-MFN_M06_MF_CLIN_STUDY>`]
     - required
     - MF_CLIN_STUDY: Required, repeating

.. _hl7-v2_5-MFN_M07:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M07.MFN_M07
   :noindex:

   HL7 v2 MFN_M07 message.

MFN_M07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_CLIN_STUDY_SCHED``
     -
     - List[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_5-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - required
     - MF_CLIN_STUDY_SCHED: Required, repeating

.. _hl7-v2_5-MFN_M08:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M08.MFN_M08
   :noindex:

   HL7 v2 MFN_M08 message.

MFN_M08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_TEST_NUMERIC``
     -
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_5-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     - MF_TEST_NUMERIC: Required, repeating

.. _hl7-v2_5-MFN_M09:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M09.MFN_M09
   :noindex:

   HL7 v2 MFN_M09 message.

MFN_M09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_TEST_CATEGORICAL``
     -
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_5-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     - MF_TEST_CATEGORICAL: Required, repeating

.. _hl7-v2_5-MFN_M10:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M10.MFN_M10
   :noindex:

   HL7 v2 MFN_M10 message.

MFN_M10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_TEST_BATTERIES``
     -
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_5-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     - MF_TEST_BATTERIES: Required, repeating

.. _hl7-v2_5-MFN_M11:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M11.MFN_M11
   :noindex:

   HL7 v2 MFN_M11 message.

MFN_M11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_TEST_CALCULATED``
     -
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_5-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     - MF_TEST_CALCULATED: Required, repeating

.. _hl7-v2_5-MFN_M12:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M12.MFN_M12
   :noindex:

   HL7 v2 MFN_M12 message.

MFN_M12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_OBS_ATTRIBUTES``
     -
     - List[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_5-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - required
     - MF_OBS_ATTRIBUTES: Required, repeating

.. _hl7-v2_5-MFN_M13:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M13.MFN_M13
   :noindex:

   HL7 v2 MFN_M13 message.

MFN_M13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MFE``
     -
     - List[:ref:`MFE <hl7-v2_5-MFE>`]
     - required
     - MFE: Required, repeating

.. _hl7-v2_5-MFN_M15:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_M15.MFN_M15
   :noindex:

   HL7 v2 MFN_M15 message.

MFN_M15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_INV_ITEM``
     -
     - List[:ref:`MFN_M15_MF_INV_ITEM <hl7-v2_5-MFN_M15_MF_INV_ITEM>`]
     - required
     - MF_INV_ITEM: Required, repeating

.. _hl7-v2_5-MFN_Znn:

.. py:class:: hl7types.hl7.v2_5.messages.MFN_Znn.MFN_Znn
   :noindex:

   HL7 v2 MFN_Znn message.

MFN_Znn
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_SITE_DEFINED``
     -
     - List[MFN_ZnnMF_SITE_DEFINED]
     - required
     - MF_SITE_DEFINED: Required, repeating

.. _hl7-v2_5-MFQ_M01:

.. py:class:: hl7types.hl7.v2_5.messages.MFQ_M01.MFQ_M01
   :noindex:

   HL7 v2 MFQ_M01 message.

MFQ_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-MFR_M01:

.. py:class:: hl7types.hl7.v2_5.messages.MFR_M01.MFR_M01
   :noindex:

   HL7 v2 MFR_M01 message.

MFR_M01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_QUERY``
     -
     - List[:ref:`MFR_M01_MF_QUERY <hl7-v2_5-MFR_M01_MF_QUERY>`]
     - required
     - MF_QUERY: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-MFR_M04:

.. py:class:: hl7types.hl7.v2_5.messages.MFR_M04.MFR_M04
   :noindex:

   HL7 v2 MFR_M04 message.

MFR_M04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_QUERY``
     -
     - List[:ref:`MFR_M04_MF_QUERY <hl7-v2_5-MFR_M04_MF_QUERY>`]
     - required
     - MF_QUERY: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-MFR_M05:

.. py:class:: hl7types.hl7.v2_5.messages.MFR_M05.MFR_M05
   :noindex:

   HL7 v2 MFR_M05 message.

MFR_M05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_QUERY``
     -
     - List[:ref:`MFR_M05_MF_QUERY <hl7-v2_5-MFR_M05_MF_QUERY>`]
     - required
     - MF_QUERY: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-MFR_M06:

.. py:class:: hl7types.hl7.v2_5.messages.MFR_M06.MFR_M06
   :noindex:

   HL7 v2 MFR_M06 message.

MFR_M06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_QUERY``
     -
     - List[:ref:`MFR_M06_MF_QUERY <hl7-v2_5-MFR_M06_MF_QUERY>`]
     - required
     - MF_QUERY: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-MFR_M07:

.. py:class:: hl7types.hl7.v2_5.messages.MFR_M07.MFR_M07
   :noindex:

   HL7 v2 MFR_M07 message.

MFR_M07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_5-MFI>`
     - required
     - MFI: Required
   * - ``MF_QUERY``
     -
     - List[:ref:`MFR_M07_MF_QUERY <hl7-v2_5-MFR_M07_MF_QUERY>`]
     - required
     - MF_QUERY: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-NMD_N02:

.. py:class:: hl7types.hl7.v2_5.messages.NMD_N02.NMD_N02
   :noindex:

   HL7 v2 NMD_N02 message.

NMD_N02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     -
     - List[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_5-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES: Required, repeating

.. _hl7-v2_5-NMQ_N01:

.. py:class:: hl7types.hl7.v2_5.messages.NMQ_N01.NMQ_N01
   :noindex:

   HL7 v2 NMQ_N01 message.

NMQ_N01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRY_WITH_DETAIL``
     -
     - Optional[:ref:`NMQ_N01_QRY_WITH_DETAIL <hl7-v2_5-NMQ_N01_QRY_WITH_DETAIL>`]
     - optional
     - QRY_WITH_DETAIL: Optional
   * - ``CLOCK_AND_STATISTICS``
     -
     - List[:ref:`NMQ_N01_CLOCK_AND_STATISTICS <hl7-v2_5-NMQ_N01_CLOCK_AND_STATISTICS>`]
     - required
     - CLOCK_AND_STATISTICS: Required, repeating

.. _hl7-v2_5-NMR_N01:

.. py:class:: hl7types.hl7.v2_5.messages.NMR_N01.NMR_N01
   :noindex:

   HL7 v2 NMR_N01 message.

NMR_N01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QRD``
     -
     - Optional[:ref:`QRD <hl7-v2_5-QRD>`]
     - optional
     - QRD: Optional
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     -
     - List[:ref:`NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_5-NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES_ALT: Required, repeating

.. _hl7-v2_5-OMB_O27:

.. py:class:: hl7types.hl7.v2_5.messages.OMB_O27.OMB_O27
   :noindex:

   HL7 v2 OMB_O27 message.

OMB_O27
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMB_O27_PATIENT <hl7-v2_5-OMB_O27_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMB_O27_ORDER <hl7-v2_5-OMB_O27_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OMD_O03:

.. py:class:: hl7types.hl7.v2_5.messages.OMD_O03.OMD_O03
   :noindex:

   HL7 v2 OMD_O03 message.

OMD_O03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMD_O03_PATIENT <hl7-v2_5-OMD_O03_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER_DIET``
     -
     - List[:ref:`OMD_O03_ORDER_DIET <hl7-v2_5-OMD_O03_ORDER_DIET>`]
     - required
     - ORDER_DIET: Required, repeating
   * - ``ORDER_TRAY``
     -
     - Optional[List[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_5-OMD_O03_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY: Optional, repeating

.. _hl7-v2_5-OMG_O19:

.. py:class:: hl7types.hl7.v2_5.messages.OMG_O19.OMG_O19
   :noindex:

   HL7 v2 OMG_O19 message.

OMG_O19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMG_O19_PATIENT <hl7-v2_5-OMG_O19_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMG_O19_ORDER <hl7-v2_5-OMG_O19_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OMI_O23:

.. py:class:: hl7types.hl7.v2_5.messages.OMI_O23.OMI_O23
   :noindex:

   HL7 v2 OMI_O23 message.

OMI_O23
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMI_O23_PATIENT <hl7-v2_5-OMI_O23_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMI_O23_ORDER <hl7-v2_5-OMI_O23_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OML_O21:

.. py:class:: hl7types.hl7.v2_5.messages.OML_O21.OML_O21
   :noindex:

   HL7 v2 OML_O21 message.

OML_O21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O21_PATIENT <hl7-v2_5-OML_O21_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OML_O21_ORDER <hl7-v2_5-OML_O21_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OML_O33:

.. py:class:: hl7types.hl7.v2_5.messages.OML_O33.OML_O33
   :noindex:

   HL7 v2 OML_O33 message.

OML_O33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O33_PATIENT <hl7-v2_5-OML_O33_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OML_O33_SPECIMEN <hl7-v2_5-OML_O33_SPECIMEN>`]
     - required
     - SPECIMEN: Required, repeating

.. _hl7-v2_5-OML_O35:

.. py:class:: hl7types.hl7.v2_5.messages.OML_O35.OML_O35
   :noindex:

   HL7 v2 OML_O35 message.

OML_O35
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O35_PATIENT <hl7-v2_5-OML_O35_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OML_O35_SPECIMEN <hl7-v2_5-OML_O35_SPECIMEN>`]
     - required
     - SPECIMEN: Required, repeating

.. _hl7-v2_5-OMN_O07:

.. py:class:: hl7types.hl7.v2_5.messages.OMN_O07.OMN_O07
   :noindex:

   HL7 v2 OMN_O07 message.

OMN_O07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMN_O07_PATIENT <hl7-v2_5-OMN_O07_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMN_O07_ORDER <hl7-v2_5-OMN_O07_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OMP_O09:

.. py:class:: hl7types.hl7.v2_5.messages.OMP_O09.OMP_O09
   :noindex:

   HL7 v2 OMP_O09 message.

OMP_O09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMP_O09_PATIENT <hl7-v2_5-OMP_O09_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMP_O09_ORDER <hl7-v2_5-OMP_O09_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-OMS_O05:

.. py:class:: hl7types.hl7.v2_5.messages.OMS_O05.OMS_O05
   :noindex:

   HL7 v2 OMS_O05 message.

OMS_O05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMS_O05_PATIENT <hl7-v2_5-OMS_O05_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMS_O05_ORDER <hl7-v2_5-OMS_O05_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-ORB_O28:

.. py:class:: hl7types.hl7.v2_5.messages.ORB_O28.ORB_O28
   :noindex:

   HL7 v2 ORB_O28 message.

ORB_O28
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORB_O28_RESPONSE <hl7-v2_5-ORB_O28_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORD_O04:

.. py:class:: hl7types.hl7.v2_5.messages.ORD_O04.ORD_O04
   :noindex:

   HL7 v2 ORD_O04 message.

ORD_O04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORD_O04_RESPONSE <hl7-v2_5-ORD_O04_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORF_R04:

.. py:class:: hl7types.hl7.v2_5.messages.ORF_R04.ORF_R04
   :noindex:

   HL7 v2 ORF_R04 message.

ORF_R04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`ORF_R04_QUERY_RESPONSE <hl7-v2_5-ORF_R04_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-ORG_O20:

.. py:class:: hl7types.hl7.v2_5.messages.ORG_O20.ORG_O20
   :noindex:

   HL7 v2 ORG_O20 message.

ORG_O20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORG_O20_RESPONSE <hl7-v2_5-ORG_O20_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORI_O24:

.. py:class:: hl7types.hl7.v2_5.messages.ORI_O24.ORI_O24
   :noindex:

   HL7 v2 ORI_O24 message.

ORI_O24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORI_O24_RESPONSE <hl7-v2_5-ORI_O24_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORL_O22:

.. py:class:: hl7types.hl7.v2_5.messages.ORL_O22.ORL_O22
   :noindex:

   HL7 v2 ORL_O22 message.

ORL_O22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O22_RESPONSE <hl7-v2_5-ORL_O22_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORL_O34:

.. py:class:: hl7types.hl7.v2_5.messages.ORL_O34.ORL_O34
   :noindex:

   HL7 v2 ORL_O34 message.

ORL_O34
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O34_RESPONSE <hl7-v2_5-ORL_O34_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORL_O36:

.. py:class:: hl7types.hl7.v2_5.messages.ORL_O36.ORL_O36
   :noindex:

   HL7 v2 ORL_O36 message.

ORL_O36
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O36_RESPONSE <hl7-v2_5-ORL_O36_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORM_O01:

.. py:class:: hl7types.hl7.v2_5.messages.ORM_O01.ORM_O01
   :noindex:

   HL7 v2 ORM_O01 message.

ORM_O01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_5-ORM_O01_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`ORM_O01_ORDER <hl7-v2_5-ORM_O01_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-ORN_O08:

.. py:class:: hl7types.hl7.v2_5.messages.ORN_O08.ORN_O08
   :noindex:

   HL7 v2 ORN_O08 message.

ORN_O08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORN_O08_RESPONSE <hl7-v2_5-ORN_O08_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORP_O10:

.. py:class:: hl7types.hl7.v2_5.messages.ORP_O10.ORP_O10
   :noindex:

   HL7 v2 ORP_O10 message.

ORP_O10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORP_O10_RESPONSE <hl7-v2_5-ORP_O10_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORR_O02:

.. py:class:: hl7types.hl7.v2_5.messages.ORR_O02.ORR_O02
   :noindex:

   HL7 v2 ORR_O02 message.

ORR_O02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORR_O02_RESPONSE <hl7-v2_5-ORR_O02_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORS_O06:

.. py:class:: hl7types.hl7.v2_5.messages.ORS_O06.ORS_O06
   :noindex:

   HL7 v2 ORS_O06 message.

ORS_O06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORS_O06_RESPONSE <hl7-v2_5-ORS_O06_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-ORU_R01:

.. py:class:: hl7types.hl7.v2_5.messages.ORU_R01.ORU_R01
   :noindex:

   HL7 v2 ORU_R01 message.

ORU_R01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PATIENT_RESULT``
     -
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_5-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-ORU_R30:

.. py:class:: hl7types.hl7.v2_5.messages.ORU_R30.ORU_R30
   :noindex:

   HL7 v2 ORU_R30 message.

ORU_R30
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``VISIT``
     -
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_5-ORU_R30_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``ORC``
     -
     - :ref:`ORC <hl7-v2_5-ORC>`
     - required
     - ORC: Required
   * - ``OBR``
     -
     - :ref:`OBR <hl7-v2_5-OBR>`
     - required
     - OBR: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``TIMING_QTY``
     -
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_5-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY: Optional, repeating
   * - ``OBSERVATION``
     -
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_5-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION: Required, repeating

.. _hl7-v2_5-OSQ_Q06:

.. py:class:: hl7types.hl7.v2_5.messages.OSQ_Q06.OSQ_Q06
   :noindex:

   HL7 v2 OSQ_Q06 message.

OSQ_Q06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-OSR_Q06:

.. py:class:: hl7types.hl7.v2_5.messages.OSR_Q06.OSR_Q06
   :noindex:

   HL7 v2 OSR_Q06 message.

OSR_Q06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``RESPONSE``
     -
     - Optional[:ref:`OSR_Q06_RESPONSE <hl7-v2_5-OSR_Q06_RESPONSE>`]
     - optional
     - RESPONSE: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-OUL_R21:

.. py:class:: hl7types.hl7.v2_5.messages.OUL_R21.OUL_R21
   :noindex:

   HL7 v2 OUL_R21 message.

OUL_R21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_5-NTE>`]
     - optional
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R21_PATIENT <hl7-v2_5-OUL_R21_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``VISIT``
     -
     - Optional[:ref:`OUL_R21_VISIT <hl7-v2_5-OUL_R21_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``ORDER_OBSERVATION``
     -
     - List[:ref:`OUL_R21_ORDER_OBSERVATION <hl7-v2_5-OUL_R21_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-OUL_R22:

.. py:class:: hl7types.hl7.v2_5.messages.OUL_R22.OUL_R22
   :noindex:

   HL7 v2 OUL_R22 message.

OUL_R22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_5-NTE>`]
     - optional
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R22_PATIENT <hl7-v2_5-OUL_R22_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``VISIT``
     -
     - Optional[:ref:`OUL_R22_VISIT <hl7-v2_5-OUL_R22_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OUL_R22_SPECIMEN <hl7-v2_5-OUL_R22_SPECIMEN>`]
     - required
     - SPECIMEN: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-OUL_R23:

.. py:class:: hl7types.hl7.v2_5.messages.OUL_R23.OUL_R23
   :noindex:

   HL7 v2 OUL_R23 message.

OUL_R23
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_5-NTE>`]
     - optional
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R23_PATIENT <hl7-v2_5-OUL_R23_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``VISIT``
     -
     - Optional[:ref:`OUL_R23_VISIT <hl7-v2_5-OUL_R23_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OUL_R23_SPECIMEN <hl7-v2_5-OUL_R23_SPECIMEN>`]
     - required
     - SPECIMEN: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-OUL_R24:

.. py:class:: hl7types.hl7.v2_5.messages.OUL_R24.OUL_R24
   :noindex:

   HL7 v2 OUL_R24 message.

OUL_R24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_5-NTE>`]
     - optional
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R24_PATIENT <hl7-v2_5-OUL_R24_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``VISIT``
     -
     - Optional[:ref:`OUL_R24_VISIT <hl7-v2_5-OUL_R24_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OUL_R24_ORDER <hl7-v2_5-OUL_R24_ORDER>`]
     - required
     - ORDER: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-PEX_P07:

.. py:class:: hl7types.hl7.v2_5.messages.PEX_P07.PEX_P07
   :noindex:

   HL7 v2 PEX_P07 message.

PEX_P07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_5-PEX_P07_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``EXPERIENCE``
     -
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_5-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE: Required, repeating

.. _hl7-v2_5-PGL_PC6:

.. py:class:: hl7types.hl7.v2_5.messages.PGL_PC6.PGL_PC6
   :noindex:

   HL7 v2 PGL_PC6 message.

PGL_PC6
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_5-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``GOAL``
     -
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_5-PGL_PC6_GOAL>`]
     - required
     - GOAL: Required, repeating

.. _hl7-v2_5-PMU_B01:

.. py:class:: hl7types.hl7.v2_5.messages.PMU_B01.PMU_B01
   :noindex:

   HL7 v2 PMU_B01 message.

PMU_B01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_5-STF>`
     - required
     - STF: Required
   * - ``PRA``
     -
     - Optional[List[:ref:`PRA <hl7-v2_5-PRA>`]]
     - optional
     - PRA: Optional, repeating
   * - ``ORG``
     -
     - Optional[List[:ref:`ORG <hl7-v2_5-ORG>`]]
     - optional
     - ORG: Optional, repeating
   * - ``AFF``
     -
     - Optional[List[:ref:`AFF <hl7-v2_5-AFF>`]]
     - optional
     - AFF: Optional, repeating
   * - ``LAN``
     -
     - Optional[List[:ref:`LAN <hl7-v2_5-LAN>`]]
     - optional
     - LAN: Optional, repeating
   * - ``EDU``
     -
     - Optional[List[:ref:`EDU <hl7-v2_5-EDU>`]]
     - optional
     - EDU: Optional, repeating
   * - ``CER``
     -
     - Optional[List[:ref:`CER <hl7-v2_5-CER>`]]
     - optional
     - CER: Optional, repeating

.. _hl7-v2_5-PMU_B03:

.. py:class:: hl7types.hl7.v2_5.messages.PMU_B03.PMU_B03
   :noindex:

   HL7 v2 PMU_B03 message.

PMU_B03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_5-STF>`
     - required
     - STF: Required

.. _hl7-v2_5-PMU_B04:

.. py:class:: hl7types.hl7.v2_5.messages.PMU_B04.PMU_B04
   :noindex:

   HL7 v2 PMU_B04 message.

PMU_B04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_5-STF>`
     - required
     - STF: Required
   * - ``PRA``
     -
     - Optional[List[:ref:`PRA <hl7-v2_5-PRA>`]]
     - optional
     - PRA: Optional, repeating
   * - ``ORG``
     -
     - Optional[List[:ref:`ORG <hl7-v2_5-ORG>`]]
     - optional
     - ORG: Optional, repeating

.. _hl7-v2_5-PMU_B07:

.. py:class:: hl7types.hl7.v2_5.messages.PMU_B07.PMU_B07
   :noindex:

   HL7 v2 PMU_B07 message.

PMU_B07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_5-STF>`
     - required
     - STF: Required
   * - ``PRA``
     -
     - Optional[:ref:`PRA <hl7-v2_5-PRA>`]
     - optional
     - PRA: Optional
   * - ``CERTIFICATE``
     -
     - Optional[List[:ref:`PMU_B07_CERTIFICATE <hl7-v2_5-PMU_B07_CERTIFICATE>`]]
     - optional
     - CERTIFICATE: Optional, repeating

.. _hl7-v2_5-PMU_B08:

.. py:class:: hl7types.hl7.v2_5.messages.PMU_B08.PMU_B08
   :noindex:

   HL7 v2 PMU_B08 message.

PMU_B08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_5-EVN>`
     - required
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_5-STF>`
     - required
     - STF: Required
   * - ``PRA``
     -
     - Optional[:ref:`PRA <hl7-v2_5-PRA>`]
     - optional
     - PRA: Optional
   * - ``CER``
     -
     - Optional[List[:ref:`CER <hl7-v2_5-CER>`]]
     - optional
     - CER: Optional, repeating

.. _hl7-v2_5-PPG_PCG:

.. py:class:: hl7types.hl7.v2_5.messages.PPG_PCG.PPG_PCG
   :noindex:

   HL7 v2 PPG_PCG message.

PPG_PCG
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_5-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_5-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY: Required, repeating

.. _hl7-v2_5-PPP_PCB:

.. py:class:: hl7types.hl7.v2_5.messages.PPP_PCB.PPP_PCB
   :noindex:

   HL7 v2 PPP_PCB message.

PPP_PCB
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_5-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_5-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY: Required, repeating

.. _hl7-v2_5-PPR_PC1:

.. py:class:: hl7types.hl7.v2_5.messages.PPR_PC1.PPR_PC1
   :noindex:

   HL7 v2 PPR_PC1 message.

PPR_PC1
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_5-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``PROBLEM``
     -
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_5-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM: Required, repeating

.. _hl7-v2_5-PPT_PCL:

.. py:class:: hl7types.hl7.v2_5.messages.PPT_PCL.PPT_PCL
   :noindex:

   HL7 v2 PPT_PCL message.

PPT_PCL
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PPT_PCL_PATIENT <hl7-v2_5-PPT_PCL_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-PPV_PCA:

.. py:class:: hl7types.hl7.v2_5.messages.PPV_PCA.PPV_PCA
   :noindex:

   HL7 v2 PPV_PCA message.

PPV_PCA
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PPV_PCA_PATIENT <hl7-v2_5-PPV_PCA_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-PRR_PC5:

.. py:class:: hl7types.hl7.v2_5.messages.PRR_PC5.PRR_PC5
   :noindex:

   HL7 v2 PRR_PC5 message.

PRR_PC5
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PRR_PC5_PATIENT <hl7-v2_5-PRR_PC5_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-PTR_PCF:

.. py:class:: hl7types.hl7.v2_5.messages.PTR_PCF.PTR_PCF
   :noindex:

   HL7 v2 PTR_PCF message.

PTR_PCF
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``PATIENT``
     -
     - List[:ref:`PTR_PCF_PATIENT <hl7-v2_5-PTR_PCF_PATIENT>`]
     - required
     - PATIENT: Required, repeating

.. _hl7-v2_5-QBP_K13:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_K13.QBP_K13
   :noindex:

   HL7 v2 QBP_K13 message.

QBP_K13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`QBP_K13_ROW_DEFINITION <hl7-v2_5-QBP_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Q11:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Q11.QBP_Q11
   :noindex:

   HL7 v2 QBP_Q11 message.

QBP_Q11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Q13:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Q13.QBP_Q13
   :noindex:

   HL7 v2 QBP_Q13 message.

QBP_Q13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_5-RDF>`]
     - optional
     - RDF: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Q15:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Q15.QBP_Q15
   :noindex:

   HL7 v2 QBP_Q15 message.

QBP_Q15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Q21:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Q21.QBP_Q21
   :noindex:

   HL7 v2 QBP_Q21 message.

QBP_Q21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Qnn:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Qnn.QBP_Qnn
   :noindex:

   HL7 v2 QBP_Qnn message.

QBP_Qnn
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_5-RDF>`]
     - optional
     - RDF: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QBP_Z73:

.. py:class:: hl7types.hl7.v2_5.messages.QBP_Z73.QBP_Z73
   :noindex:

   HL7 v2 QBP_Z73 message.

QBP_Z73
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required

.. _hl7-v2_5-QCK_Q02:

.. py:class:: hl7types.hl7.v2_5.messages.QCK_Q02.QCK_Q02
   :noindex:

   HL7 v2 QCK_Q02 message.

QCK_Q02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - Optional[:ref:`QAK <hl7-v2_5-QAK>`]
     - optional
     - QAK: Optional

.. _hl7-v2_5-QCN_J01:

.. py:class:: hl7types.hl7.v2_5.messages.QCN_J01.QCN_J01
   :noindex:

   HL7 v2 QCN_J01 message.

QCN_J01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QID``
     -
     - :ref:`QID <hl7-v2_5-QID>`
     - required
     - QID: Required

.. _hl7-v2_5-QRY:

.. py:class:: hl7types.hl7.v2_5.messages.QRY.QRY
   :noindex:

   HL7 v2 QRY message.

QRY
~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional

.. _hl7-v2_5-QRY_A19:

.. py:class:: hl7types.hl7.v2_5.messages.QRY_A19.QRY_A19
   :noindex:

   HL7 v2 QRY_A19 message.

QRY_A19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional

.. _hl7-v2_5-QRY_PC4:

.. py:class:: hl7types.hl7.v2_5.messages.QRY_PC4.QRY_PC4
   :noindex:

   HL7 v2 QRY_PC4 message.

QRY_PC4
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional

.. _hl7-v2_5-QRY_Q01:

.. py:class:: hl7types.hl7.v2_5.messages.QRY_Q01.QRY_Q01
   :noindex:

   HL7 v2 QRY_Q01 message.

QRY_Q01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QRY_Q02:

.. py:class:: hl7types.hl7.v2_5.messages.QRY_Q02.QRY_Q02
   :noindex:

   HL7 v2 QRY_Q02 message.

QRY_Q02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QRY_R02:

.. py:class:: hl7types.hl7.v2_5.messages.QRY_R02.QRY_R02
   :noindex:

   HL7 v2 QRY_R02 message.

QRY_R02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - :ref:`QRF <hl7-v2_5-QRF>`
     - required
     - QRF: Required

.. _hl7-v2_5-QSB_Q16:

.. py:class:: hl7types.hl7.v2_5.messages.QSB_Q16.QSB_Q16
   :noindex:

   HL7 v2 QSB_Q16 message.

QSB_Q16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-QVR_Q17:

.. py:class:: hl7types.hl7.v2_5.messages.QVR_Q17.QVR_Q17
   :noindex:

   HL7 v2 QVR_Q17 message.

QVR_Q17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``QBP``
     -
     - Optional[:ref:`QVR_Q17_QBP <hl7-v2_5-QVR_Q17_QBP>`]
     - optional
     - QBP: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RAR_RAR:

.. py:class:: hl7types.hl7.v2_5.messages.RAR_RAR.RAR_RAR
   :noindex:

   HL7 v2 RAR_RAR message.

RAR_RAR
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``DEFINITION``
     -
     - List[:ref:`RAR_RAR_DEFINITION <hl7-v2_5-RAR_RAR_DEFINITION>`]
     - required
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RAS_O17:

.. py:class:: hl7types.hl7.v2_5.messages.RAS_O17.RAS_O17
   :noindex:

   HL7 v2 RAS_O17 message.

RAS_O17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RAS_O17_PATIENT <hl7-v2_5-RAS_O17_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RAS_O17_ORDER <hl7-v2_5-RAS_O17_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-RCI_I05:

.. py:class:: hl7types.hl7.v2_5.messages.RCI_I05.RCI_I05
   :noindex:

   HL7 v2 RCI_I05 message.

RCI_I05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RCI_I05_PROVIDER <hl7-v2_5-RCI_I05_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RCI_I05_OBSERVATION <hl7-v2_5-RCI_I05_OBSERVATION>`]]
     - optional
     - OBSERVATION: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RCL_I06:

.. py:class:: hl7types.hl7.v2_5.messages.RCL_I06.RCL_I06
   :noindex:

   HL7 v2 RCL_I06 message.

RCL_I06
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RCL_I06_PROVIDER <hl7-v2_5-RCL_I06_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_5-DSP>`]]
     - optional
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RDE_O11:

.. py:class:: hl7types.hl7.v2_5.messages.RDE_O11.RDE_O11
   :noindex:

   HL7 v2 RDE_O11 message.

RDE_O11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_5-RDE_O11_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDE_O11_ORDER <hl7-v2_5-RDE_O11_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-RDR_RDR:

.. py:class:: hl7types.hl7.v2_5.messages.RDR_RDR.RDR_RDR
   :noindex:

   HL7 v2 RDR_RDR message.

RDR_RDR
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``DEFINITION``
     -
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_5-RDR_RDR_DEFINITION>`]
     - required
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RDS_O13:

.. py:class:: hl7types.hl7.v2_5.messages.RDS_O13.RDS_O13
   :noindex:

   HL7 v2 RDS_O13 message.

RDS_O13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDS_O13_PATIENT <hl7-v2_5-RDS_O13_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDS_O13_ORDER <hl7-v2_5-RDS_O13_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-RDY_K15:

.. py:class:: hl7types.hl7.v2_5.messages.RDY_K15.RDY_K15
   :noindex:

   HL7 v2 RDY_K15 message.

RDY_K15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_5-DSP>`]]
     - optional
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-REF_I12:

.. py:class:: hl7types.hl7.v2_5.messages.REF_I12.REF_I12
   :noindex:

   HL7 v2 REF_I12 message.

REF_I12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_5-RF1>`]
     - optional
     - RF1: Optional
   * - ``AUTHORIZATION_CONTACT``
     -
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_5-REF_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT: Optional
   * - ``PROVIDER_CONTACT``
     -
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_5-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_5-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_5-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_5-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_5-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RER_RER:

.. py:class:: hl7types.hl7.v2_5.messages.RER_RER.RER_RER
   :noindex:

   HL7 v2 RER_RER message.

RER_RER
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``DEFINITION``
     -
     - List[:ref:`RER_RER_DEFINITION <hl7-v2_5-RER_RER_DEFINITION>`]
     - required
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RGR_RGR:

.. py:class:: hl7types.hl7.v2_5.messages.RGR_RGR.RGR_RGR
   :noindex:

   HL7 v2 RGR_RGR message.

RGR_RGR
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``DEFINITION``
     -
     - List[:ref:`RGR_RGR_DEFINITION <hl7-v2_5-RGR_RGR_DEFINITION>`]
     - required
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RGV_O15:

.. py:class:: hl7types.hl7.v2_5.messages.RGV_O15.RGV_O15
   :noindex:

   HL7 v2 RGV_O15 message.

RGV_O15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RGV_O15_PATIENT <hl7-v2_5-RGV_O15_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RGV_O15_ORDER <hl7-v2_5-RGV_O15_ORDER>`]
     - required
     - ORDER: Required, repeating

.. _hl7-v2_5-ROR_ROR:

.. py:class:: hl7types.hl7.v2_5.messages.ROR_ROR.ROR_ROR
   :noindex:

   HL7 v2 ROR_ROR message.

ROR_ROR
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``DEFINITION``
     -
     - List[:ref:`ROR_ROR_DEFINITION <hl7-v2_5-ROR_ROR_DEFINITION>`]
     - required
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RPA_I08:

.. py:class:: hl7types.hl7.v2_5.messages.RPA_I08.RPA_I08
   :noindex:

   HL7 v2 RPA_I08 message.

RPA_I08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_5-RF1>`]
     - optional
     - RF1: Optional
   * - ``AUTHORIZATION_1``
     -
     - Optional[:ref:`RPA_I08_AUTHORIZATION_1 <hl7-v2_5-RPA_I08_AUTHORIZATION_1>`]
     - optional
     - AUTHORIZATION_1: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_5-RPA_I08_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_5-RPA_I08_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_5-RPA_I08_PROCEDURE>`]
     - required
     - PROCEDURE: Required, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_5-RPA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_5-RPA_I08_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RPI_I01:

.. py:class:: hl7types.hl7.v2_5.messages.RPI_I01.RPI_I01
   :noindex:

   HL7 v2 RPI_I01 message.

RPI_I01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_5-RPI_I01_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_5-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RPI_I04:

.. py:class:: hl7types.hl7.v2_5.messages.RPI_I04.RPI_I04
   :noindex:

   HL7 v2 RPI_I04 message.

RPI_I04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPI_I04_PROVIDER <hl7-v2_5-RPI_I04_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_5-RPI_I04_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RPL_I02:

.. py:class:: hl7types.hl7.v2_5.messages.RPL_I02.RPL_I02
   :noindex:

   HL7 v2 RPL_I02 message.

RPL_I02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_5-RPL_I02_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_5-DSP>`]]
     - optional
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RPR_I03:

.. py:class:: hl7types.hl7.v2_5.messages.RPR_I03.RPR_I03
   :noindex:

   HL7 v2 RPR_I03 message.

RPR_I03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPR_I03_PROVIDER <hl7-v2_5-RPR_I03_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - Optional[List[:ref:`PID <hl7-v2_5-PID>`]]
     - optional
     - PID: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RQA_I08:

.. py:class:: hl7types.hl7.v2_5.messages.RQA_I08.RQA_I08
   :noindex:

   HL7 v2 RQA_I08 message.

RQA_I08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_5-RF1>`]
     - optional
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_5-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_5-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_5-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE: Optional
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_5-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_5-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_5-RQA_I08_VISIT>`]
     - optional
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RQC_I05:

.. py:class:: hl7types.hl7.v2_5.messages.RQC_I05.RQC_I05
   :noindex:

   HL7 v2 RQC_I05 message.

RQC_I05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQC_I05_PROVIDER <hl7-v2_5-RQC_I05_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RQI_I01:

.. py:class:: hl7types.hl7.v2_5.messages.RQI_I01.RQI_I01
   :noindex:

   HL7 v2 RQI_I01 message.

RQI_I01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PROVIDER``
     -
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_5-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_5-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RQP_I04:

.. py:class:: hl7types.hl7.v2_5.messages.RQP_I04.RQP_I04
   :noindex:

   HL7 v2 RQP_I04 message.

RQP_I04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PROVIDER``
     -
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_5-RQP_I04_PROVIDER>`]
     - required
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RQQ_Q09:

.. py:class:: hl7types.hl7.v2_5.messages.RQQ_Q09.RQQ_Q09
   :noindex:

   HL7 v2 RQQ_Q09 message.

RQQ_Q09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``ERQ``
     -
     - :ref:`ERQ <hl7-v2_5-ERQ>`
     - required
     - ERQ: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RRA_O18:

.. py:class:: hl7types.hl7.v2_5.messages.RRA_O18.RRA_O18
   :noindex:

   HL7 v2 RRA_O18 message.

RRA_O18
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRA_O18_RESPONSE <hl7-v2_5-RRA_O18_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-RRD_O14:

.. py:class:: hl7types.hl7.v2_5.messages.RRD_O14.RRD_O14
   :noindex:

   HL7 v2 RRD_O14 message.

RRD_O14
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRD_O14_RESPONSE <hl7-v2_5-RRD_O14_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-RRE_O12:

.. py:class:: hl7types.hl7.v2_5.messages.RRE_O12.RRE_O12
   :noindex:

   HL7 v2 RRE_O12 message.

RRE_O12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_5-RRE_O12_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-RRG_O16:

.. py:class:: hl7types.hl7.v2_5.messages.RRG_O16.RRG_O16
   :noindex:

   HL7 v2 RRG_O16 message.

RRG_O16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRG_O16_RESPONSE <hl7-v2_5-RRG_O16_RESPONSE>`]
     - optional
     - RESPONSE: Optional

.. _hl7-v2_5-RRI_I12:

.. py:class:: hl7types.hl7.v2_5.messages.RRI_I12.RRI_I12
   :noindex:

   HL7 v2 RRI_I12 message.

RRI_I12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_5-MSA>`]
     - optional
     - MSA: Optional
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_5-RF1>`]
     - optional
     - RF1: Optional
   * - ``AUTHORIZATION_CONTACT``
     -
     - Optional[:ref:`RRI_I12_AUTHORIZATION_CONTACT <hl7-v2_5-RRI_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT: Optional
   * - ``PROVIDER_CONTACT``
     -
     - List[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_5-RRI_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_5-ACC>`]
     - optional
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_5-DG1>`]]
     - optional
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_5-DRG>`]]
     - optional
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_5-AL1>`]]
     - optional
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_5-RRI_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RRI_I12_OBSERVATION <hl7-v2_5-RRI_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`RRI_I12_PATIENT_VISIT <hl7-v2_5-RRI_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating

.. _hl7-v2_5-RSP_K11:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_K11.RSP_K11
   :noindex:

   HL7 v2 RSP_K11 message.

RSP_K11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RSP_K11_ROW_DEFINITION <hl7-v2_5-RSP_K11_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_K21:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_K21.RSP_K21
   :noindex:

   HL7 v2 RSP_K21 message.

RSP_K21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[List[:ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_5-RSP_K21_QUERY_RESPONSE>`]]
     - optional
     - QUERY_RESPONSE: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_K23:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_K23.RSP_K23
   :noindex:

   HL7 v2 RSP_K23 message.

RSP_K23
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_5-RSP_K23_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_K25:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_K25.RSP_K25
   :noindex:

   HL7 v2 RSP_K25 message.

RSP_K25
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``STAFF``
     -
     - List[:ref:`RSP_K25_STAFF <hl7-v2_5-RSP_K25_STAFF>`]
     - required
     - STAFF: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_K31:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_K31.RSP_K31
   :noindex:

   HL7 v2 RSP_K31 message.

RSP_K31
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``RESPONSE``
     -
     - List[:ref:`RSP_K31_RESPONSE <hl7-v2_5-RSP_K31_RESPONSE>`]
     - required
     - RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_Q11:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_Q11.RSP_Q11
   :noindex:

   HL7 v2 RSP_Q11 message.

RSP_Q11
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``QUERY_RESULT_CLUSTER``
     -
     - Optional[:ref:`RSP_Q11_QUERY_RESULT_CLUSTER <hl7-v2_5-RSP_Q11_QUERY_RESULT_CLUSTER>`]
     - optional
     - QUERY_RESULT_CLUSTER: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_Z82:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_Z82.RSP_Z82
   :noindex:

   HL7 v2 RSP_Z82 message.

RSP_Z82
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_5-RSP_Z82_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_Z86:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_Z86.RSP_Z86
   :noindex:

   HL7 v2 RSP_Z86 message.

RSP_Z86
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_5-RSP_Z86_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RSP_Z88:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_Z88.RSP_Z88
   :noindex:

   HL7 v2 RSP_Z88 message.

RSP_Z88
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_5-RSP_Z88_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_5-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_5-RSP_Z90:

.. py:class:: hl7types.hl7.v2_5.messages.RSP_Z90.RSP_Z90
   :noindex:

   HL7 v2 RSP_Z90 message.

RSP_Z90
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_5-RCP>`
     - required
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_5-RSP_Z90_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_5-DSC>`
     - required
     - DSC: Required

.. _hl7-v2_5-RTB_K13:

.. py:class:: hl7types.hl7.v2_5.messages.RTB_K13.RTB_K13
   :noindex:

   HL7 v2 RTB_K13 message.

RTB_K13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RTB_Knn:

.. py:class:: hl7types.hl7.v2_5.messages.RTB_Knn.RTB_Knn
   :noindex:

   HL7 v2 RTB_Knn message.

RTB_Knn
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-RTB_Z74:

.. py:class:: hl7types.hl7.v2_5.messages.RTB_Z74.RTB_Z74
   :noindex:

   HL7 v2 RTB_Z74 message.

RTB_Z74
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_5-QPD>`
     - required
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_5-RTB_Z74_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-SIU_S12:

.. py:class:: hl7types.hl7.v2_5.messages.SIU_S12.SIU_S12
   :noindex:

   HL7 v2 SIU_S12 message.

SIU_S12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SCH``
     -
     - :ref:`SCH <hl7-v2_5-SCH>`
     - required
     - SCH: Required
   * - ``TQ1``
     -
     - Optional[List[:ref:`TQ1 <hl7-v2_5-TQ1>`]]
     - optional
     - TQ1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES: Required, repeating

.. _hl7-v2_5-SPQ_Q08:

.. py:class:: hl7types.hl7.v2_5.messages.SPQ_Q08.SPQ_Q08
   :noindex:

   HL7 v2 SPQ_Q08 message.

SPQ_Q08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``SPR``
     -
     - :ref:`SPR <hl7-v2_5-SPR>`
     - required
     - SPR: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_5-RDF>`]
     - optional
     - RDF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-SQM_S25:

.. py:class:: hl7types.hl7.v2_5.messages.SQM_S25.SQM_S25
   :noindex:

   HL7 v2 SQM_S25 message.

SQM_S25
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``REQUEST``
     -
     - Optional[:ref:`SQM_S25_REQUEST <hl7-v2_5-SQM_S25_REQUEST>`]
     - optional
     - REQUEST: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-SQR_S25:

.. py:class:: hl7types.hl7.v2_5.messages.SQR_S25.SQR_S25
   :noindex:

   HL7 v2 SQR_S25 message.

SQR_S25
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``SCHEDULE``
     -
     - Optional[List[:ref:`SQR_S25_SCHEDULE <hl7-v2_5-SQR_S25_SCHEDULE>`]]
     - optional
     - SCHEDULE: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-SRM_S01:

.. py:class:: hl7types.hl7.v2_5.messages.SRM_S01.SRM_S01
   :noindex:

   HL7 v2 SRM_S01 message.

SRM_S01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``ARQ``
     -
     - :ref:`ARQ <hl7-v2_5-ARQ>`
     - required
     - ARQ: Required
   * - ``APR``
     -
     - Optional[:ref:`APR <hl7-v2_5-APR>`]
     - optional
     - APR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_5-NTE>`]]
     - optional
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES: Required, repeating

.. _hl7-v2_5-SRR_S01:

.. py:class:: hl7types.hl7.v2_5.messages.SRR_S01.SRR_S01
   :noindex:

   HL7 v2 SRR_S01 message.

SRR_S01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_5-ERR>`]]
     - optional
     - ERR: Optional, repeating
   * - ``SCHEDULE``
     -
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_5-SRR_S01_SCHEDULE>`]
     - optional
     - SCHEDULE: Optional

.. _hl7-v2_5-SSR_U04:

.. py:class:: hl7types.hl7.v2_5.messages.SSR_U04.SSR_U04
   :noindex:

   HL7 v2 SSR_U04 message.

SSR_U04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``SPECIMEN_CONTAINER``
     -
     - List[:ref:`SSR_U04_SPECIMEN_CONTAINER <hl7-v2_5-SSR_U04_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-SSU_U03:

.. py:class:: hl7types.hl7.v2_5.messages.SSU_U03.SSU_U03
   :noindex:

   HL7 v2 SSU_U03 message.

SSU_U03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``SPECIMEN_CONTAINER``
     -
     - List[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_5-SSU_U03_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-SUR_P09:

.. py:class:: hl7types.hl7.v2_5.messages.SUR_P09.SUR_P09
   :noindex:

   HL7 v2 SUR_P09 message.

SUR_P09
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``FACILITY``
     -
     - List[:ref:`SUR_P09_FACILITY <hl7-v2_5-SUR_P09_FACILITY>`]
     - required
     - FACILITY: Required, repeating

.. _hl7-v2_5-TBR_R08:

.. py:class:: hl7types.hl7.v2_5.messages.TBR_R08.TBR_R08
   :noindex:

   HL7 v2 TBR_R08 message.

TBR_R08
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_5-ERR>`]
     - optional
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_5-QAK>`
     - required
     - QAK: Required
   * - ``RDF``
     -
     - :ref:`RDF <hl7-v2_5-RDF>`
     - required
     - RDF: Required
   * - ``RDT``
     -
     - List[:ref:`RDT <hl7-v2_5-RDT>`]
     - required
     - RDT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-TCU_U10:

.. py:class:: hl7types.hl7.v2_5.messages.TCU_U10.TCU_U10
   :noindex:

   HL7 v2 TCU_U10 message.

TCU_U10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_5-EQU>`
     - required
     - EQU: Required
   * - ``TEST_CONFIGURATION``
     -
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_5-TCU_U10_TEST_CONFIGURATION>`]
     - required
     - TEST_CONFIGURATION: Required, repeating
   * - ``ROL``
     -
     - Optional[:ref:`ROL <hl7-v2_5-ROL>`]
     - optional
     - ROL: Optional

.. _hl7-v2_5-UDM_Q05:

.. py:class:: hl7types.hl7.v2_5.messages.UDM_Q05.UDM_Q05
   :noindex:

   HL7 v2 UDM_Q05 message.

UDM_Q05
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``URD``
     -
     - :ref:`URD <hl7-v2_5-URD>`
     - required
     - URD: Required
   * - ``URS``
     -
     - Optional[:ref:`URS <hl7-v2_5-URS>`]
     - optional
     - URS: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_5-DSP>`]
     - required
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-VQQ_Q07:

.. py:class:: hl7types.hl7.v2_5.messages.VQQ_Q07.VQQ_Q07
   :noindex:

   HL7 v2 VQQ_Q07 message.

VQQ_Q07
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``VTQ``
     -
     - :ref:`VTQ <hl7-v2_5-VTQ>`
     - required
     - VTQ: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_5-RDF>`]
     - optional
     - RDF: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_5-DSC>`]
     - optional
     - DSC: Optional

.. _hl7-v2_5-VXQ_V01:

.. py:class:: hl7types.hl7.v2_5.messages.VXQ_V01.VXQ_V01
   :noindex:

   HL7 v2 VXQ_V01 message.

VXQ_V01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional

.. _hl7-v2_5-VXR_V03:

.. py:class:: hl7types.hl7.v2_5.messages.VXR_V03.VXR_V03
   :noindex:

   HL7 v2 VXR_V03 message.

VXR_V03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`VXR_V03_PATIENT_VISIT <hl7-v2_5-VXR_V03_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`VXR_V03_INSURANCE <hl7-v2_5-VXR_V03_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ORDER``
     -
     - Optional[List[:ref:`VXR_V03_ORDER <hl7-v2_5-VXR_V03_ORDER>`]]
     - optional
     - ORDER: Optional, repeating

.. _hl7-v2_5-VXU_V04:

.. py:class:: hl7types.hl7.v2_5.messages.VXU_V04.VXU_V04
   :noindex:

   HL7 v2 VXU_V04 message.

VXU_V04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_5-PID>`
     - required
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_5-PD1>`]
     - optional
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_5-NK1>`]]
     - optional
     - NK1: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`VXU_V04_PATIENT <hl7-v2_5-VXU_V04_PATIENT>`]
     - optional
     - PATIENT: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_5-GT1>`]]
     - optional
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_5-VXU_V04_INSURANCE>`]]
     - optional
     - INSURANCE: Optional, repeating
   * - ``ORDER``
     -
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_5-VXU_V04_ORDER>`]]
     - optional
     - ORDER: Optional, repeating

.. _hl7-v2_5-VXX_V02:

.. py:class:: hl7types.hl7.v2_5.messages.VXX_V02.VXX_V02
   :noindex:

   HL7 v2 VXX_V02 message.

VXX_V02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_5-MSH>`
     - required
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_5-MSA>`
     - required
     - MSA: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_5-SFT>`]]
     - optional
     - SFT: Optional, repeating
   * - ``QRD``
     -
     - :ref:`QRD <hl7-v2_5-QRD>`
     - required
     - QRD: Required
   * - ``QRF``
     -
     - Optional[:ref:`QRF <hl7-v2_5-QRF>`]
     - optional
     - QRF: Optional
   * - ``PATIENT``
     -
     - List[:ref:`VXX_V02_PATIENT <hl7-v2_5-VXX_V02_PATIENT>`]
     - required
     - PATIENT: Required, repeating
