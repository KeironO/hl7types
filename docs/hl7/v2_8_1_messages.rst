v2.8.1 Messages
===============

.. _hl7-v2_8_1-ACK:

.. py:class:: hl7types.hl7.v2_8_1.messages.ACK.ACK
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating

.. _hl7-v2_8_1-ADT_A01:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A01.ADT_A01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_8_1-ADT_A01_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_8_1-ADT_A01_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     -
     - UB2: Optional
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     -
     - PDA: Optional

.. _hl7-v2_8_1-ADT_A02:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A02.ADT_A02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     -
     - PDA: Optional

.. _hl7-v2_8_1-ADT_A03:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A03.ADT_A03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_8_1-ADT_A03_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A03_INSURANCE <hl7-v2_8_1-ADT_A03_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``PDA``
     -
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     -
     - PDA: Optional

.. _hl7-v2_8_1-ADT_A05:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A05.ADT_A05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_8_1-ADT_A05_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_8_1-ADT_A05_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_8_1-ADT_A06:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A06.ADT_A06
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``MRG``
     -
     - Optional[:ref:`MRG <hl7-v2_8_1-MRG>`]
     - optional
     -
     - MRG: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_8_1-ADT_A06_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_8_1-ADT_A06_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``UB1``
     -
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     -
     - UB1: Optional
   * - ``UB2``
     -
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     -
     - UB2: Optional

.. _hl7-v2_8_1-ADT_A09:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A09.ADT_A09
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating

.. _hl7-v2_8_1-ADT_A12:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A12.ADT_A12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[:ref:`DG1 <hl7-v2_8_1-DG1>`]
     - optional
     -
     - DG1: Optional

.. _hl7-v2_8_1-ADT_A15:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A15.ADT_A15
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_8_1-ADT_A16:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A16.ADT_A16
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`ADT_A16_PROCEDURE <hl7-v2_8_1-ADT_A16_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`ADT_A16_INSURANCE <hl7-v2_8_1-ADT_A16_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional

.. _hl7-v2_8_1-ADT_A17:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A17.ADT_A17
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_8_1-ADT_A20:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A20.ADT_A20
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``NPU``
     -
     - :ref:`NPU <hl7-v2_8_1-NPU>`
     - required
     -
     - NPU: Required

.. _hl7-v2_8_1-ADT_A21:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A21.ADT_A21
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating

.. _hl7-v2_8_1-ADT_A24:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A24.ADT_A24
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_8_1-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating

.. _hl7-v2_8_1-ADT_A37:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A37.ADT_A37
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - Optional[:ref:`PV1 <hl7-v2_8_1-PV1>`]
     - optional
     -
     - PV1: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating

.. _hl7-v2_8_1-ADT_A38:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A38.ADT_A38
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``OBX``
     -
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     -
     - OBX: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional

.. _hl7-v2_8_1-ADT_A39:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A39.ADT_A39
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_8_1-ADT_A39_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-ADT_A43:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A43.ADT_A43
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_8_1-ADT_A43_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-ADT_A44:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A44.ADT_A44
   :noindex:

   HL7 v2 ADT_A44 message.

ADT_A44
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`ADT_A44_PATIENT <hl7-v2_8_1-ADT_A44_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-ADT_A45:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A45.ADT_A45
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MERGE_INFO``
     -
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_8_1-ADT_A45_MERGE_INFO>`]
     - required
     -
     - MERGE_INFO: Required, repeating

.. _hl7-v2_8_1-ADT_A50:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A50.ADT_A50
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``MRG``
     -
     - :ref:`MRG <hl7-v2_8_1-MRG>`
     - required
     -
     - MRG: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required

.. _hl7-v2_8_1-ADT_A52:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A52.ADT_A52
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional

.. _hl7-v2_8_1-ADT_A54:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A54.ADT_A54
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional

.. _hl7-v2_8_1-ADT_A60:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A60.ADT_A60
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`ADT_A60_VISIT <hl7-v2_8_1-ADT_A60_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``ADVERSE_REACTION_GROUP``
     -
     - Optional[List[:ref:`ADT_A60_ADVERSE_REACTION_GROUP <hl7-v2_8_1-ADT_A60_ADVERSE_REACTION_GROUP>`]]
     - optional
     -
     - ADVERSE_REACTION_GROUP: Optional, repeating

.. _hl7-v2_8_1-ADT_A61:

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A61.ADT_A61
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional

.. _hl7-v2_8_1-BAR_P01:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P01.BAR_P01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - List[:ref:`BAR_P01_VISIT <hl7-v2_8_1-BAR_P01_VISIT>`]
     - required
     -
     - VISIT: Required, repeating

.. _hl7-v2_8_1-BAR_P02:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P02.BAR_P02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_8_1-BAR_P02_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-BAR_P05:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P05.BAR_P05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - List[:ref:`BAR_P05_VISIT <hl7-v2_8_1-BAR_P05_VISIT>`]
     - required
     -
     - VISIT: Required, repeating

.. _hl7-v2_8_1-BAR_P06:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P06.BAR_P06
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PATIENT``
     -
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_8_1-BAR_P06_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-BAR_P10:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P10.BAR_P10
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``GP1``
     -
     - :ref:`GP1 <hl7-v2_8_1-GP1>`
     - required
     -
     - GP1: Required
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`BAR_P10_PROCEDURE <hl7-v2_8_1-BAR_P10_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating

.. _hl7-v2_8_1-BAR_P12:

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P12.BAR_P12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`BAR_P12_PROCEDURE <hl7-v2_8_1-BAR_P12_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBX``
     -
     - Optional[:ref:`OBX <hl7-v2_8_1-OBX>`]
     - optional
     -
     - OBX: Optional

.. _hl7-v2_8_1-BPS_O29:

.. py:class:: hl7types.hl7.v2_8_1.messages.BPS_O29.BPS_O29
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`BPS_O29_PATIENT <hl7-v2_8_1-BPS_O29_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`BPS_O29_ORDER <hl7-v2_8_1-BPS_O29_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-BRP_O30:

.. py:class:: hl7types.hl7.v2_8_1.messages.BRP_O30.BRP_O30
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`BRP_O30_RESPONSE <hl7-v2_8_1-BRP_O30_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-BRT_O32:

.. py:class:: hl7types.hl7.v2_8_1.messages.BRT_O32.BRT_O32
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`BRT_O32_RESPONSE <hl7-v2_8_1-BRT_O32_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-BTS_O31:

.. py:class:: hl7types.hl7.v2_8_1.messages.BTS_O31.BTS_O31
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`BTS_O31_PATIENT <hl7-v2_8_1-BTS_O31_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`BTS_O31_ORDER <hl7-v2_8_1-BTS_O31_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-CCF_I22:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCF_I22.CCF_I22
   :noindex:

   HL7 v2 CCF_I22 message.

CCF_I22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required

.. _hl7-v2_8_1-CCI_I22:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCI_I22.CCI_I22
   :noindex:

   HL7 v2 CCI_I22 message.

CCI_I22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`CCI_I22_INSURANCE <hl7-v2_8_1-CCI_I22_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``APPOINTMENT_HISTORY``
     -
     - Optional[List[:ref:`CCI_I22_APPOINTMENT_HISTORY <hl7-v2_8_1-CCI_I22_APPOINTMENT_HISTORY>`]]
     - optional
     -
     - APPOINTMENT_HISTORY: Optional, repeating
   * - ``CLINICAL_HISTORY``
     -
     - Optional[List[:ref:`CCI_I22_CLINICAL_HISTORY <hl7-v2_8_1-CCI_I22_CLINICAL_HISTORY>`]]
     - optional
     -
     - CLINICAL_HISTORY: Optional, repeating
   * - ``PATIENT_VISITS``
     -
     - List[:ref:`CCI_I22_PATIENT_VISITS <hl7-v2_8_1-CCI_I22_PATIENT_VISITS>`]
     - required
     -
     - PATIENT_VISITS: Required, repeating
   * - ``MEDICATION_HISTORY``
     -
     - Optional[List[:ref:`CCI_I22_MEDICATION_HISTORY <hl7-v2_8_1-CCI_I22_MEDICATION_HISTORY>`]]
     - optional
     -
     - MEDICATION_HISTORY: Optional, repeating
   * - ``PROBLEM``
     -
     - Optional[List[:ref:`CCI_I22_PROBLEM <hl7-v2_8_1-CCI_I22_PROBLEM>`]]
     - optional
     -
     - PROBLEM: Optional, repeating
   * - ``GOAL``
     -
     - Optional[List[:ref:`CCI_I22_GOAL <hl7-v2_8_1-CCI_I22_GOAL>`]]
     - optional
     -
     - GOAL: Optional, repeating
   * - ``PATHWAY``
     -
     - Optional[List[:ref:`CCI_I22_PATHWAY <hl7-v2_8_1-CCI_I22_PATHWAY>`]]
     - optional
     -
     - PATHWAY: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CCM_I21:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCM_I21.CCM_I21
   :noindex:

   HL7 v2 CCM_I21 message.

CCM_I21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`CCM_I21_INSURANCE <hl7-v2_8_1-CCM_I21_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``APPOINTMENT_HISTORY``
     -
     - Optional[List[:ref:`CCM_I21_APPOINTMENT_HISTORY <hl7-v2_8_1-CCM_I21_APPOINTMENT_HISTORY>`]]
     - optional
     -
     - APPOINTMENT_HISTORY: Optional, repeating
   * - ``CLINICAL_HISTORY``
     -
     - Optional[List[:ref:`CCM_I21_CLINICAL_HISTORY <hl7-v2_8_1-CCM_I21_CLINICAL_HISTORY>`]]
     - optional
     -
     - CLINICAL_HISTORY: Optional, repeating
   * - ``PATIENT_VISITS``
     -
     - List[:ref:`CCM_I21_PATIENT_VISITS <hl7-v2_8_1-CCM_I21_PATIENT_VISITS>`]
     - required
     -
     - PATIENT_VISITS: Required, repeating
   * - ``MEDICATION_HISTORY``
     -
     - Optional[List[:ref:`CCM_I21_MEDICATION_HISTORY <hl7-v2_8_1-CCM_I21_MEDICATION_HISTORY>`]]
     - optional
     -
     - MEDICATION_HISTORY: Optional, repeating
   * - ``PROBLEM``
     -
     - Optional[List[:ref:`CCM_I21_PROBLEM <hl7-v2_8_1-CCM_I21_PROBLEM>`]]
     - optional
     -
     - PROBLEM: Optional, repeating
   * - ``GOAL``
     -
     - Optional[List[:ref:`CCM_I21_GOAL <hl7-v2_8_1-CCM_I21_GOAL>`]]
     - optional
     -
     - GOAL: Optional, repeating
   * - ``PATHWAY``
     -
     - Optional[List[:ref:`CCM_I21_PATHWAY <hl7-v2_8_1-CCM_I21_PATHWAY>`]]
     - optional
     -
     - PATHWAY: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CCQ_I19:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCQ_I19.CCQ_I19
   :noindex:

   HL7 v2 CCQ_I19 message.

CCQ_I19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``RF1``
     -
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     -
     - RF1: Required
   * - ``PROVIDER_CONTACT``
     -
     - Optional[List[:ref:`CCQ_I19_PROVIDER_CONTACT <hl7-v2_8_1-CCQ_I19_PROVIDER_CONTACT>`]]
     - optional
     -
     - PROVIDER_CONTACT: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CCR_I16:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCR_I16.CCR_I16
   :noindex:

   HL7 v2 CCR_I16 message.

CCR_I16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``RF1``
     -
     - List[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - required
     -
     - RF1: Required, repeating
   * - ``PROVIDER_CONTACT``
     -
     - List[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8_1-CCR_I16_PROVIDER_CONTACT>`]
     - required
     -
     - PROVIDER_CONTACT: Required, repeating
   * - ``CLINICAL_ORDER``
     -
     - Optional[List[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8_1-CCR_I16_CLINICAL_ORDER>`]]
     - optional
     -
     - CLINICAL_ORDER: Optional, repeating
   * - ``PATIENT``
     -
     - List[:ref:`CCR_I16_PATIENT <hl7-v2_8_1-CCR_I16_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`CCR_I16_INSURANCE <hl7-v2_8_1-CCR_I16_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``APPOINTMENT_HISTORY``
     -
     - Optional[List[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8_1-CCR_I16_APPOINTMENT_HISTORY>`]]
     - optional
     -
     - APPOINTMENT_HISTORY: Optional, repeating
   * - ``CLINICAL_HISTORY``
     -
     - Optional[List[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8_1-CCR_I16_CLINICAL_HISTORY>`]]
     - optional
     -
     - CLINICAL_HISTORY: Optional, repeating
   * - ``PATIENT_VISITS``
     -
     - List[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8_1-CCR_I16_PATIENT_VISITS>`]
     - required
     -
     - PATIENT_VISITS: Required, repeating
   * - ``MEDICATION_HISTORY``
     -
     - Optional[List[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8_1-CCR_I16_MEDICATION_HISTORY>`]]
     - optional
     -
     - MEDICATION_HISTORY: Optional, repeating
   * - ``PROBLEM``
     -
     - Optional[List[:ref:`CCR_I16_PROBLEM <hl7-v2_8_1-CCR_I16_PROBLEM>`]]
     - optional
     -
     - PROBLEM: Optional, repeating
   * - ``GOAL``
     -
     - Optional[List[:ref:`CCR_I16_GOAL <hl7-v2_8_1-CCR_I16_GOAL>`]]
     - optional
     -
     - GOAL: Optional, repeating
   * - ``PATHWAY``
     -
     - Optional[List[:ref:`CCR_I16_PATHWAY <hl7-v2_8_1-CCR_I16_PATHWAY>`]]
     - optional
     -
     - PATHWAY: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CCU_I20:

.. py:class:: hl7types.hl7.v2_8_1.messages.CCU_I20.CCU_I20
   :noindex:

   HL7 v2 CCU_I20 message.

CCU_I20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``RF1``
     -
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     -
     - RF1: Required
   * - ``PROVIDER_CONTACT``
     -
     - Optional[List[:ref:`CCU_I20_PROVIDER_CONTACT <hl7-v2_8_1-CCU_I20_PROVIDER_CONTACT>`]]
     - optional
     -
     - PROVIDER_CONTACT: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`CCU_I20_PATIENT <hl7-v2_8_1-CCU_I20_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`CCU_I20_INSURANCE <hl7-v2_8_1-CCU_I20_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``APPOINTMENT_HISTORY``
     -
     - Optional[List[:ref:`CCU_I20_APPOINTMENT_HISTORY <hl7-v2_8_1-CCU_I20_APPOINTMENT_HISTORY>`]]
     - optional
     -
     - APPOINTMENT_HISTORY: Optional, repeating
   * - ``CLINICAL_HISTORY``
     -
     - Optional[List[:ref:`CCU_I20_CLINICAL_HISTORY <hl7-v2_8_1-CCU_I20_CLINICAL_HISTORY>`]]
     - optional
     -
     - CLINICAL_HISTORY: Optional, repeating
   * - ``PATIENT_VISITS``
     -
     - List[:ref:`CCU_I20_PATIENT_VISITS <hl7-v2_8_1-CCU_I20_PATIENT_VISITS>`]
     - required
     -
     - PATIENT_VISITS: Required, repeating
   * - ``MEDICATION_HISTORY``
     -
     - Optional[List[:ref:`CCU_I20_MEDICATION_HISTORY <hl7-v2_8_1-CCU_I20_MEDICATION_HISTORY>`]]
     - optional
     -
     - MEDICATION_HISTORY: Optional, repeating
   * - ``PROBLEM``
     -
     - Optional[List[:ref:`CCU_I20_PROBLEM <hl7-v2_8_1-CCU_I20_PROBLEM>`]]
     - optional
     -
     - PROBLEM: Optional, repeating
   * - ``GOAL``
     -
     - Optional[List[:ref:`CCU_I20_GOAL <hl7-v2_8_1-CCU_I20_GOAL>`]]
     - optional
     -
     - GOAL: Optional, repeating
   * - ``PATHWAY``
     -
     - Optional[List[:ref:`CCU_I20_PATHWAY <hl7-v2_8_1-CCU_I20_PATHWAY>`]]
     - optional
     -
     - PATHWAY: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CQU_I19:

.. py:class:: hl7types.hl7.v2_8_1.messages.CQU_I19.CQU_I19
   :noindex:

   HL7 v2 CQU_I19 message.

CQU_I19
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``RF1``
     -
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     -
     - RF1: Required
   * - ``PROVIDER_CONTACT``
     -
     - Optional[List[:ref:`CQU_I19_PROVIDER_CONTACT <hl7-v2_8_1-CQU_I19_PROVIDER_CONTACT>`]]
     - optional
     -
     - PROVIDER_CONTACT: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`CQU_I19_PATIENT <hl7-v2_8_1-CQU_I19_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`CQU_I19_INSURANCE <hl7-v2_8_1-CQU_I19_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``APPOINTMENT_HISTORY``
     -
     - Optional[List[:ref:`CQU_I19_APPOINTMENT_HISTORY <hl7-v2_8_1-CQU_I19_APPOINTMENT_HISTORY>`]]
     - optional
     -
     - APPOINTMENT_HISTORY: Optional, repeating
   * - ``CLINICAL_HISTORY``
     -
     - Optional[List[:ref:`CQU_I19_CLINICAL_HISTORY <hl7-v2_8_1-CQU_I19_CLINICAL_HISTORY>`]]
     - optional
     -
     - CLINICAL_HISTORY: Optional, repeating
   * - ``PATIENT_VISITS``
     -
     - List[:ref:`CQU_I19_PATIENT_VISITS <hl7-v2_8_1-CQU_I19_PATIENT_VISITS>`]
     - required
     -
     - PATIENT_VISITS: Required, repeating
   * - ``MEDICATION_HISTORY``
     -
     - Optional[List[:ref:`CQU_I19_MEDICATION_HISTORY <hl7-v2_8_1-CQU_I19_MEDICATION_HISTORY>`]]
     - optional
     -
     - MEDICATION_HISTORY: Optional, repeating
   * - ``PROBLEM``
     -
     - Optional[List[:ref:`CQU_I19_PROBLEM <hl7-v2_8_1-CQU_I19_PROBLEM>`]]
     - optional
     -
     - PROBLEM: Optional, repeating
   * - ``GOAL``
     -
     - Optional[List[:ref:`CQU_I19_GOAL <hl7-v2_8_1-CQU_I19_GOAL>`]]
     - optional
     -
     - GOAL: Optional, repeating
   * - ``PATHWAY``
     -
     - Optional[List[:ref:`CQU_I19_PATHWAY <hl7-v2_8_1-CQU_I19_PATHWAY>`]]
     - optional
     -
     - PATHWAY: Optional, repeating
   * - ``REL``
     -
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     -
     - REL: Optional, repeating

.. _hl7-v2_8_1-CRM_C01:

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C01.CRM_C01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PATIENT``
     -
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-CSU_C09:

.. py:class:: hl7types.hl7.v2_8_1.messages.CSU_C09.CSU_C09
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PATIENT``
     -
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_8_1-CSU_C09_PATIENT>`]
     - required
     -
     - PATIENT: Required, repeating

.. _hl7-v2_8_1-DBC_O41:

.. py:class:: hl7types.hl7.v2_8_1.messages.DBC_O41.DBC_O41
   :noindex:

   HL7 v2 DBC_O41 message.

DBC_O41
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DBC_O41_DONOR <hl7-v2_8_1-DBC_O41_DONOR>`]
     - optional
     -
     - DONOR: Optional

.. _hl7-v2_8_1-DBC_O42:

.. py:class:: hl7types.hl7.v2_8_1.messages.DBC_O42.DBC_O42
   :noindex:

   HL7 v2 DBC_O42 message.

DBC_O42
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DBC_O42_DONOR <hl7-v2_8_1-DBC_O42_DONOR>`]
     - optional
     -
     - DONOR: Optional

.. _hl7-v2_8_1-DEL_O46:

.. py:class:: hl7types.hl7.v2_8_1.messages.DEL_O46.DEL_O46
   :noindex:

   HL7 v2 DEL_O46 message.

DEL_O46
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DEL_O46_DONOR <hl7-v2_8_1-DEL_O46_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DON``
     -
     - :ref:`DON <hl7-v2_8_1-DON>`
     - required
     -
     - DON: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-DEO_O45:

.. py:class:: hl7types.hl7.v2_8_1.messages.DEO_O45.DEO_O45
   :noindex:

   HL7 v2 DEO_O45 message.

DEO_O45
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DEO_O45_DONOR <hl7-v2_8_1-DEO_O45_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DONATION_ORDER``
     -
     - List[:ref:`DEO_O45_DONATION_ORDER <hl7-v2_8_1-DEO_O45_DONATION_ORDER>`]
     - required
     -
     - DONATION_ORDER: Required, repeating

.. _hl7-v2_8_1-DER_O44:

.. py:class:: hl7types.hl7.v2_8_1.messages.DER_O44.DER_O44
   :noindex:

   HL7 v2 DER_O44 message.

DER_O44
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DER_O44_DONOR <hl7-v2_8_1-DER_O44_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DONATION_ORDER``
     -
     - List[:ref:`DER_O44_DONATION_ORDER <hl7-v2_8_1-DER_O44_DONATION_ORDER>`]
     - required
     -
     - DONATION_ORDER: Required, repeating

.. _hl7-v2_8_1-DFT_P03:

.. py:class:: hl7types.hl7.v2_8_1.messages.DFT_P03.DFT_P03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`DFT_P03_VISIT <hl7-v2_8_1-DFT_P03_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_8_1-DFT_P03_COMMON_ORDER>`]]
     - optional
     -
     - COMMON_ORDER: Optional, repeating
   * - ``FINANCIAL``
     -
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_8_1-DFT_P03_FINANCIAL>`]
     - required
     -
     - FINANCIAL: Required, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_8_1-DFT_P03_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional

.. _hl7-v2_8_1-DFT_P11:

.. py:class:: hl7types.hl7.v2_8_1.messages.DFT_P11.DFT_P11
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`DFT_P11_VISIT <hl7-v2_8_1-DFT_P11_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``DB1``
     -
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     -
     - DB1: Optional, repeating
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_8_1-DFT_P11_COMMON_ORDER>`]]
     - optional
     -
     - COMMON_ORDER: Optional, repeating
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     -
     - DRG: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`DFT_P11_INSURANCE <hl7-v2_8_1-DFT_P11_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``FINANCIAL``
     -
     - List[:ref:`DFT_P11_FINANCIAL <hl7-v2_8_1-DFT_P11_FINANCIAL>`]
     - required
     -
     - FINANCIAL: Required, repeating

.. _hl7-v2_8_1-DPR_O48:

.. py:class:: hl7types.hl7.v2_8_1.messages.DPR_O48.DPR_O48
   :noindex:

   HL7 v2 DPR_O48 message.

DPR_O48
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DPR_O48_DONOR <hl7-v2_8_1-DPR_O48_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DONATION_ORDER``
     -
     - List[:ref:`DPR_O48_DONATION_ORDER <hl7-v2_8_1-DPR_O48_DONATION_ORDER>`]
     - required
     -
     - DONATION_ORDER: Required, repeating
   * - ``DONATION``
     -
     - Optional[:ref:`DPR_O48_DONATION <hl7-v2_8_1-DPR_O48_DONATION>`]
     - optional
     -
     - DONATION: Optional

.. _hl7-v2_8_1-DRC_O47:

.. py:class:: hl7types.hl7.v2_8_1.messages.DRC_O47.DRC_O47
   :noindex:

   HL7 v2 DRC_O47 message.

DRC_O47
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DRC_O47_DONOR <hl7-v2_8_1-DRC_O47_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DONATION_ORDER``
     -
     - List[:ref:`DRC_O47_DONATION_ORDER <hl7-v2_8_1-DRC_O47_DONATION_ORDER>`]
     - required
     -
     - DONATION_ORDER: Required, repeating

.. _hl7-v2_8_1-DRG_O43:

.. py:class:: hl7types.hl7.v2_8_1.messages.DRG_O43.DRG_O43
   :noindex:

   HL7 v2 DRG_O43 message.

DRG_O43
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DONOR``
     -
     - Optional[:ref:`DRG_O43_DONOR <hl7-v2_8_1-DRG_O43_DONOR>`]
     - optional
     -
     - DONOR: Optional

.. _hl7-v2_8_1-EAC_U07:

.. py:class:: hl7types.hl7.v2_8_1.messages.EAC_U07.EAC_U07
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``COMMAND``
     -
     - List[:ref:`EAC_U07_COMMAND <hl7-v2_8_1-EAC_U07_COMMAND>`]
     - required
     -
     - COMMAND: Required, repeating

.. _hl7-v2_8_1-EAN_U09:

.. py:class:: hl7types.hl7.v2_8_1.messages.EAN_U09.EAN_U09
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``NOTIFICATION``
     -
     - List[:ref:`EAN_U09_NOTIFICATION <hl7-v2_8_1-EAN_U09_NOTIFICATION>`]
     - required
     -
     - NOTIFICATION: Required, repeating

.. _hl7-v2_8_1-EAR_U08:

.. py:class:: hl7types.hl7.v2_8_1.messages.EAR_U08.EAR_U08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``COMMAND_RESPONSE``
     -
     - List[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_8_1-EAR_U08_COMMAND_RESPONSE>`]
     - required
     -
     - COMMAND_RESPONSE: Required, repeating

.. _hl7-v2_8_1-EHC_E01:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E01.EHC_E01
   :noindex:

   HL7 v2 EHC_E01 message.

EHC_E01
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``INVOICE_INFORMATION_SUBMIT``
     -
     - :ref:`EHC_E01_INVOICE_INFORMATION_SUBMIT <hl7-v2_8_1-EHC_E01_INVOICE_INFORMATION_SUBMIT>`
     - required
     -
     - INVOICE_INFORMATION_SUBMIT: Required

.. _hl7-v2_8_1-EHC_E02:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E02.EHC_E02
   :noindex:

   HL7 v2 EHC_E02 message.

EHC_E02
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``INVOICE_INFORMATION_CANCEL``
     -
     - :ref:`EHC_E02_INVOICE_INFORMATION_CANCEL <hl7-v2_8_1-EHC_E02_INVOICE_INFORMATION_CANCEL>`
     - required
     -
     - INVOICE_INFORMATION_CANCEL: Required

.. _hl7-v2_8_1-EHC_E04:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E04.EHC_E04
   :noindex:

   HL7 v2 EHC_E04 message.

EHC_E04
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``REASSESSMENT_REQUEST_INFO``
     -
     - :ref:`EHC_E04_REASSESSMENT_REQUEST_INFO <hl7-v2_8_1-EHC_E04_REASSESSMENT_REQUEST_INFO>`
     - required
     -
     - REASSESSMENT_REQUEST_INFO: Required

.. _hl7-v2_8_1-EHC_E10:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E10.EHC_E10
   :noindex:

   HL7 v2 EHC_E10 message.

EHC_E10
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``INVOICE_PROCESSING_RESULTS_INFO``
     -
     - List[:ref:`EHC_E10_INVOICE_PROCESSING_RESULTS_INFO <hl7-v2_8_1-EHC_E10_INVOICE_PROCESSING_RESULTS_INFO>`]
     - required
     -
     - INVOICE_PROCESSING_RESULTS_INFO: Required, repeating

.. _hl7-v2_8_1-EHC_E12:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E12.EHC_E12
   :noindex:

   HL7 v2 EHC_E12 message.

EHC_E12
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``RFI``
     -
     - :ref:`RFI <hl7-v2_8_1-RFI>`
     - required
     -
     - RFI: Required
   * - ``CTD``
     -
     - Optional[List[:ref:`CTD <hl7-v2_8_1-CTD>`]]
     - optional
     -
     - CTD: Optional, repeating
   * - ``IVC``
     -
     - :ref:`IVC <hl7-v2_8_1-IVC>`
     - required
     -
     - IVC: Required
   * - ``PSS``
     -
     - :ref:`PSS <hl7-v2_8_1-PSS>`
     - required
     -
     - PSS: Required
   * - ``PSG``
     -
     - :ref:`PSG <hl7-v2_8_1-PSG>`
     - required
     -
     - PSG: Required
   * - ``PID``
     -
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     -
     - PID: Optional
   * - ``PSL``
     -
     - Optional[List[:ref:`PSL <hl7-v2_8_1-PSL>`]]
     - optional
     -
     - PSL: Optional, repeating
   * - ``REQUEST``
     -
     - List[:ref:`EHC_E12_REQUEST <hl7-v2_8_1-EHC_E12_REQUEST>`]
     - required
     -
     - REQUEST: Required, repeating

.. _hl7-v2_8_1-EHC_E13:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E13.EHC_E13
   :noindex:

   HL7 v2 EHC_E13 message.

EHC_E13
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``RFI``
     -
     - :ref:`RFI <hl7-v2_8_1-RFI>`
     - required
     -
     - RFI: Required
   * - ``CTD``
     -
     - Optional[List[:ref:`CTD <hl7-v2_8_1-CTD>`]]
     - optional
     -
     - CTD: Optional, repeating
   * - ``IVC``
     -
     - :ref:`IVC <hl7-v2_8_1-IVC>`
     - required
     -
     - IVC: Required
   * - ``PSS``
     -
     - :ref:`PSS <hl7-v2_8_1-PSS>`
     - required
     -
     - PSS: Required
   * - ``PSG``
     -
     - :ref:`PSG <hl7-v2_8_1-PSG>`
     - required
     -
     - PSG: Required
   * - ``PID``
     -
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     -
     - PID: Optional
   * - ``PSL``
     -
     - Optional[:ref:`PSL <hl7-v2_8_1-PSL>`]
     - optional
     -
     - PSL: Optional
   * - ``REQUEST``
     -
     - List[:ref:`EHC_E13_REQUEST <hl7-v2_8_1-EHC_E13_REQUEST>`]
     - required
     -
     - REQUEST: Required, repeating

.. _hl7-v2_8_1-EHC_E15:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E15.EHC_E15
   :noindex:

   HL7 v2 EHC_E15 message.

EHC_E15
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``PAYMENT_REMITTANCE_HEADER_INFO``
     -
     - :ref:`EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO <hl7-v2_8_1-EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO>`
     - required
     -
     - PAYMENT_REMITTANCE_HEADER_INFO: Required
   * - ``PAYMENT_REMITTANCE_DETAIL_INFO``
     -
     - Optional[List[:ref:`EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO <hl7-v2_8_1-EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO>`]]
     - optional
     -
     - PAYMENT_REMITTANCE_DETAIL_INFO: Optional, repeating
   * - ``ADJUSTMENT_PAYEE``
     -
     - Optional[List[:ref:`EHC_E15_ADJUSTMENT_PAYEE <hl7-v2_8_1-EHC_E15_ADJUSTMENT_PAYEE>`]]
     - optional
     -
     - ADJUSTMENT_PAYEE: Optional, repeating

.. _hl7-v2_8_1-EHC_E20:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E20.EHC_E20
   :noindex:

   HL7 v2 EHC_E20 message.

EHC_E20
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``AUTHORIZATION_REQUEST``
     -
     - :ref:`EHC_E20_AUTHORIZATION_REQUEST <hl7-v2_8_1-EHC_E20_AUTHORIZATION_REQUEST>`
     - required
     -
     - AUTHORIZATION_REQUEST: Required

.. _hl7-v2_8_1-EHC_E21:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E21.EHC_E21
   :noindex:

   HL7 v2 EHC_E21 message.

EHC_E21
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``AUTHORIZATION_REQUEST``
     -
     - :ref:`EHC_E21_AUTHORIZATION_REQUEST <hl7-v2_8_1-EHC_E21_AUTHORIZATION_REQUEST>`
     - required
     -
     - AUTHORIZATION_REQUEST: Required

.. _hl7-v2_8_1-EHC_E24:

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E24.EHC_E24
   :noindex:

   HL7 v2 EHC_E24 message.

EHC_E24
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``AUTHORIZATION_RESPONSE_INFO``
     -
     - :ref:`EHC_E24_AUTHORIZATION_RESPONSE_INFO <hl7-v2_8_1-EHC_E24_AUTHORIZATION_RESPONSE_INFO>`
     - required
     -
     - AUTHORIZATION_RESPONSE_INFO: Required

.. _hl7-v2_8_1-ESR_U02:

.. py:class:: hl7types.hl7.v2_8_1.messages.ESR_U02.ESR_U02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required

.. _hl7-v2_8_1-ESU_U01:

.. py:class:: hl7types.hl7.v2_8_1.messages.ESU_U01.ESU_U01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``ISD``
     -
     - Optional[List[:ref:`ISD <hl7-v2_8_1-ISD>`]]
     - optional
     -
     - ISD: Optional, repeating

.. _hl7-v2_8_1-INR_U06:

.. py:class:: hl7types.hl7.v2_8_1.messages.INR_U06.INR_U06
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``INV``
     -
     - List[:ref:`INV <hl7-v2_8_1-INV>`]
     - required
     -
     - INV: Required, repeating

.. _hl7-v2_8_1-INU_U05:

.. py:class:: hl7types.hl7.v2_8_1.messages.INU_U05.INU_U05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``INV``
     -
     - List[:ref:`INV <hl7-v2_8_1-INV>`]
     - required
     -
     - INV: Required, repeating

.. _hl7-v2_8_1-LSU_U12:

.. py:class:: hl7types.hl7.v2_8_1.messages.LSU_U12.LSU_U12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``EQP``
     -
     - List[:ref:`EQP <hl7-v2_8_1-EQP>`]
     - required
     -
     - EQP: Required, repeating

.. _hl7-v2_8_1-MDM_T01:

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T01.MDM_T01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     -
     - COMMON_ORDER: Optional, repeating
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     -
     - TXA: Required
   * - ``CON``
     -
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     -
     - CON: Optional, repeating

.. _hl7-v2_8_1-MDM_T02:

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T02.MDM_T02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``COMMON_ORDER``
     -
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     -
     - COMMON_ORDER: Optional, repeating
   * - ``TXA``
     -
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     -
     - TXA: Required
   * - ``CON``
     -
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     -
     - CON: Optional, repeating
   * - ``OBSERVATION``
     -
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     -
     - OBSERVATION: Required, repeating

.. _hl7-v2_8_1-MFK_M01:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFK_M01.MFK_M01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFA``
     -
     - Optional[List[:ref:`MFA <hl7-v2_8_1-MFA>`]]
     - optional
     -
     - MFA: Optional, repeating

.. _hl7-v2_8_1-MFN_M02:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M02.MFN_M02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_STAFF``
     -
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_8_1-MFN_M02_MF_STAFF>`]
     - required
     -
     - MF_STAFF: Required, repeating

.. _hl7-v2_8_1-MFN_M04:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M04.MFN_M04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``MF_CDM``
     -
     - List[:ref:`MFN_M04_MF_CDM <hl7-v2_8_1-MFN_M04_MF_CDM>`]
     - required
     -
     - MF_CDM: Required, repeating

.. _hl7-v2_8_1-MFN_M05:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M05.MFN_M05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_LOCATION``
     -
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_8_1-MFN_M05_MF_LOCATION>`]
     - required
     -
     - MF_LOCATION: Required, repeating

.. _hl7-v2_8_1-MFN_M06:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M06.MFN_M06
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_CLIN_STUDY``
     -
     - List[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_8_1-MFN_M06_MF_CLIN_STUDY>`]
     - required
     -
     - MF_CLIN_STUDY: Required, repeating

.. _hl7-v2_8_1-MFN_M07:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M07.MFN_M07
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_CLIN_STUDY_SCHED``
     -
     - List[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_8_1-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - required
     -
     - MF_CLIN_STUDY_SCHED: Required, repeating

.. _hl7-v2_8_1-MFN_M08:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M08.MFN_M08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_NUMERIC``
     -
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_8_1-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     -
     - MF_TEST_NUMERIC: Required, repeating

.. _hl7-v2_8_1-MFN_M09:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M09.MFN_M09
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_CATEGORICAL``
     -
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_8_1-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     -
     - MF_TEST_CATEGORICAL: Required, repeating

.. _hl7-v2_8_1-MFN_M10:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M10.MFN_M10
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_BATTERIES``
     -
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_8_1-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     -
     - MF_TEST_BATTERIES: Required, repeating

.. _hl7-v2_8_1-MFN_M11:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M11.MFN_M11
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_TEST_CALCULATED``
     -
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_8_1-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     -
     - MF_TEST_CALCULATED: Required, repeating

.. _hl7-v2_8_1-MFN_M12:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M12.MFN_M12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_OBS_ATTRIBUTES``
     -
     - List[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_8_1-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - required
     -
     - MF_OBS_ATTRIBUTES: Required, repeating

.. _hl7-v2_8_1-MFN_M13:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M13.MFN_M13
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MFE``
     -
     - List[:ref:`MFE <hl7-v2_8_1-MFE>`]
     - required
     -
     - MFE: Required, repeating

.. _hl7-v2_8_1-MFN_M15:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M15.MFN_M15
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_INV_ITEM``
     -
     - List[:ref:`MFN_M15_MF_INV_ITEM <hl7-v2_8_1-MFN_M15_MF_INV_ITEM>`]
     - required
     -
     - MF_INV_ITEM: Required, repeating

.. _hl7-v2_8_1-MFN_M16:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M16.MFN_M16
   :noindex:

   HL7 v2 MFN_M16 message.

MFN_M16
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MATERIAL_ITEM_RECORD``
     -
     - List[:ref:`MFN_M16_MATERIAL_ITEM_RECORD <hl7-v2_8_1-MFN_M16_MATERIAL_ITEM_RECORD>`]
     - required
     -
     - MATERIAL_ITEM_RECORD: Required, repeating

.. _hl7-v2_8_1-MFN_M17:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M17.MFN_M17
   :noindex:

   HL7 v2 MFN_M17 message.

MFN_M17
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_DRG``
     -
     - List[:ref:`MFN_M17_MF_DRG <hl7-v2_8_1-MFN_M17_MF_DRG>`]
     - required
     -
     - MF_DRG: Required, repeating

.. _hl7-v2_8_1-MFN_Znn:

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_Znn.MFN_Znn
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MFI``
     -
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     -
     - MFI: Required
   * - ``MF_SITE_DEFINED``
     -
     - List[MFN_ZnnMF_SITE_DEFINED]
     - required
     -
     - MF_SITE_DEFINED: Required, repeating

.. _hl7-v2_8_1-NMD_N02:

.. py:class:: hl7types.hl7.v2_8_1.messages.NMD_N02.NMD_N02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     -
     - List[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_8_1-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     -
     - CLOCK_AND_STATS_WITH_NOTES: Required, repeating

.. _hl7-v2_8_1-OMB_O27:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMB_O27.OMB_O27
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMB_O27_PATIENT <hl7-v2_8_1-OMB_O27_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMB_O27_ORDER <hl7-v2_8_1-OMB_O27_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMD_O03:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMD_O03.OMD_O03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMD_O03_PATIENT <hl7-v2_8_1-OMD_O03_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER_DIET``
     -
     - List[:ref:`OMD_O03_ORDER_DIET <hl7-v2_8_1-OMD_O03_ORDER_DIET>`]
     - required
     -
     - ORDER_DIET: Required, repeating
   * - ``ORDER_TRAY``
     -
     - Optional[List[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_8_1-OMD_O03_ORDER_TRAY>`]]
     - optional
     -
     - ORDER_TRAY: Optional, repeating

.. _hl7-v2_8_1-OMG_O19:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMG_O19.OMG_O19
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMG_O19_PATIENT <hl7-v2_8_1-OMG_O19_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMG_O19_ORDER <hl7-v2_8_1-OMG_O19_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMI_O23:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMI_O23.OMI_O23
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMI_O23_PATIENT <hl7-v2_8_1-OMI_O23_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMI_O23_ORDER <hl7-v2_8_1-OMI_O23_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OML_O21:

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O21.OML_O21
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O21_PATIENT <hl7-v2_8_1-OML_O21_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OML_O21_ORDER <hl7-v2_8_1-OML_O21_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OML_O33:

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O33.OML_O33
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O33_PATIENT <hl7-v2_8_1-OML_O33_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OML_O33_SPECIMEN <hl7-v2_8_1-OML_O33_SPECIMEN>`]
     - required
     -
     - SPECIMEN: Required, repeating

.. _hl7-v2_8_1-OML_O35:

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O35.OML_O35
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O35_PATIENT <hl7-v2_8_1-OML_O35_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``SPECIMEN``
     -
     - List[:ref:`OML_O35_SPECIMEN <hl7-v2_8_1-OML_O35_SPECIMEN>`]
     - required
     -
     - SPECIMEN: Required, repeating

.. _hl7-v2_8_1-OML_O39:

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O39.OML_O39
   :noindex:

   HL7 v2 OML_O39 message.

OML_O39
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OML_O39_PATIENT <hl7-v2_8_1-OML_O39_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OML_O39_ORDER <hl7-v2_8_1-OML_O39_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMN_O07:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMN_O07.OMN_O07
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMN_O07_PATIENT <hl7-v2_8_1-OMN_O07_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMN_O07_ORDER <hl7-v2_8_1-OMN_O07_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMP_O09:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMP_O09.OMP_O09
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMP_O09_PATIENT <hl7-v2_8_1-OMP_O09_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMP_O09_ORDER <hl7-v2_8_1-OMP_O09_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMQ_O57:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMQ_O57.OMQ_O57
   :noindex:

   HL7 v2 OMQ_O57 message.

OMQ_O57
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMQ_O57_PATIENT <hl7-v2_8_1-OMQ_O57_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMQ_O57_ORDER <hl7-v2_8_1-OMQ_O57_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OMS_O05:

.. py:class:: hl7types.hl7.v2_8_1.messages.OMS_O05.OMS_O05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`OMS_O05_PATIENT <hl7-v2_8_1-OMS_O05_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`OMS_O05_ORDER <hl7-v2_8_1-OMS_O05_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OPL_O37:

.. py:class:: hl7types.hl7.v2_8_1.messages.OPL_O37.OPL_O37
   :noindex:

   HL7 v2 OPL_O37 message.

OPL_O37
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PRT``
     -
     - List[:ref:`PRT <hl7-v2_8_1-PRT>`]
     - required
     -
     - PRT: Required, repeating
   * - ``GUARANTOR``
     -
     - Optional[:ref:`OPL_O37_GUARANTOR <hl7-v2_8_1-OPL_O37_GUARANTOR>`]
     - optional
     -
     - GUARANTOR: Optional
   * - ``ORDER``
     -
     - List[:ref:`OPL_O37_ORDER <hl7-v2_8_1-OPL_O37_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-OPR_O38:

.. py:class:: hl7types.hl7.v2_8_1.messages.OPR_O38.OPR_O38
   :noindex:

   HL7 v2 OPR_O38 message.

OPR_O38
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`OPR_O38_RESPONSE <hl7-v2_8_1-OPR_O38_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-OPU_R25:

.. py:class:: hl7types.hl7.v2_8_1.messages.OPU_R25.OPU_R25
   :noindex:

   HL7 v2 OPU_R25 message.

OPU_R25
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     -
     - NTE: Optional
   * - ``PV1``
     -
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     -
     - PV1: Required
   * - ``PV2``
     -
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     -
     - PV2: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``PATIENT_VISIT_OBSERVATION``
     -
     - Optional[List[:ref:`OPU_R25_PATIENT_VISIT_OBSERVATION <hl7-v2_8_1-OPU_R25_PATIENT_VISIT_OBSERVATION>`]]
     - optional
     -
     - PATIENT_VISIT_OBSERVATION: Optional, repeating
   * - ``ACCESSION_DETAIL``
     -
     - List[:ref:`OPU_R25_ACCESSION_DETAIL <hl7-v2_8_1-OPU_R25_ACCESSION_DETAIL>`]
     - required
     -
     - ACCESSION_DETAIL: Required, repeating

.. _hl7-v2_8_1-ORA_R33:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORA_R33.ORA_R33
   :noindex:

   HL7 v2 ORA_R33 message.

ORA_R33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``ORC``
     -
     - Optional[:ref:`ORC <hl7-v2_8_1-ORC>`]
     - optional
     -
     - ORC: Optional

.. _hl7-v2_8_1-ORA_R41:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORA_R41.ORA_R41
   :noindex:

   HL7 v2 ORA_R41 message.

ORA_R41
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating

.. _hl7-v2_8_1-ORB_O28:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORB_O28.ORB_O28
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORB_O28_RESPONSE <hl7-v2_8_1-ORB_O28_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORD_O04:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORD_O04.ORD_O04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORD_O04_RESPONSE <hl7-v2_8_1-ORD_O04_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORG_O20:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORG_O20.ORG_O20
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORG_O20_RESPONSE <hl7-v2_8_1-ORG_O20_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORI_O24:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORI_O24.ORI_O24
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORI_O24_RESPONSE <hl7-v2_8_1-ORI_O24_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O22:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O22.ORL_O22
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O22_RESPONSE <hl7-v2_8_1-ORL_O22_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O34:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O34.ORL_O34
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O34_RESPONSE <hl7-v2_8_1-ORL_O34_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O36:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O36.ORL_O36
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O36_RESPONSE <hl7-v2_8_1-ORL_O36_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O40:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O40.ORL_O40
   :noindex:

   HL7 v2 ORL_O40 message.

ORL_O40
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O40_RESPONSE <hl7-v2_8_1-ORL_O40_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O41:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O41.ORL_O41
   :noindex:

   HL7 v2 ORL_O41 message.

ORL_O41
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O41_RESPONSE <hl7-v2_8_1-ORL_O41_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O42:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O42.ORL_O42
   :noindex:

   HL7 v2 ORL_O42 message.

ORL_O42
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O42_RESPONSE <hl7-v2_8_1-ORL_O42_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O43:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O43.ORL_O43
   :noindex:

   HL7 v2 ORL_O43 message.

ORL_O43
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O43_RESPONSE <hl7-v2_8_1-ORL_O43_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORL_O44:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O44.ORL_O44
   :noindex:

   HL7 v2 ORL_O44 message.

ORL_O44
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORL_O44_RESPONSE <hl7-v2_8_1-ORL_O44_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORN_O08:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORN_O08.ORN_O08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORN_O08_RESPONSE <hl7-v2_8_1-ORN_O08_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORP_O10:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORP_O10.ORP_O10
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORP_O10_RESPONSE <hl7-v2_8_1-ORP_O10_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORS_O06:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORS_O06.ORS_O06
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORS_O06_RESPONSE <hl7-v2_8_1-ORS_O06_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-ORU_R01:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R01.ORU_R01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PATIENT_RESULT``
     -
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_8_1-ORU_R01_PATIENT_RESULT>`]
     - required
     -
     - PATIENT_RESULT: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-ORU_R30:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R30.ORU_R30
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``PATIENT_OBSERVATION``
     -
     - Optional[List[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8_1-ORU_R30_PATIENT_OBSERVATION>`]]
     - optional
     -
     - PATIENT_OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_8_1-ORU_R30_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``ORC``
     -
     - :ref:`ORC <hl7-v2_8_1-ORC>`
     - required
     -
     - ORC: Required
   * - ``OBR``
     -
     - :ref:`OBR <hl7-v2_8_1-OBR>`
     - required
     -
     - OBR: Required
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``TIMING_QTY``
     -
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8_1-ORU_R30_TIMING_QTY>`]]
     - optional
     -
     - TIMING_QTY: Optional, repeating
   * - ``OBSERVATION``
     -
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_8_1-ORU_R30_OBSERVATION>`]
     - required
     -
     - OBSERVATION: Required, repeating

.. _hl7-v2_8_1-ORX_O58:

.. py:class:: hl7types.hl7.v2_8_1.messages.ORX_O58.ORX_O58
   :noindex:

   HL7 v2 ORX_O58 message.

ORX_O58
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`ORX_O58_RESPONSE <hl7-v2_8_1-ORX_O58_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-OSM_R26:

.. py:class:: hl7types.hl7.v2_8_1.messages.OSM_R26.OSM_R26
   :noindex:

   HL7 v2 OSM_R26 message.

OSM_R26
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``SHIPMENT``
     -
     - List[:ref:`OSM_R26_SHIPMENT <hl7-v2_8_1-OSM_R26_SHIPMENT>`]
     - required
     -
     - SHIPMENT: Required, repeating

.. _hl7-v2_8_1-OSU_O51:

.. py:class:: hl7types.hl7.v2_8_1.messages.OSU_O51.OSU_O51
   :noindex:

   HL7 v2 OSU_O51 message.

OSU_O51
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PID``
     -
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     -
     - PID: Optional
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``ORDER_STATUS``
     -
     - List[:ref:`OSU_O51_ORDER_STATUS <hl7-v2_8_1-OSU_O51_ORDER_STATUS>`]
     - required
     -
     - ORDER_STATUS: Required, repeating

.. _hl7-v2_8_1-OUL_R22:

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R22.OUL_R22
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     -
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R22_PATIENT <hl7-v2_8_1-OUL_R22_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``SPECIMEN``
     -
     - List[:ref:`OUL_R22_SPECIMEN <hl7-v2_8_1-OUL_R22_SPECIMEN>`]
     - required
     -
     - SPECIMEN: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-OUL_R23:

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R23.OUL_R23
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     -
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R23_PATIENT <hl7-v2_8_1-OUL_R23_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``SPECIMEN``
     -
     - List[:ref:`OUL_R23_SPECIMEN <hl7-v2_8_1-OUL_R23_SPECIMEN>`]
     - required
     -
     - SPECIMEN: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-OUL_R24:

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R24.OUL_R24
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     -
     - NTE: Optional
   * - ``PATIENT``
     -
     - Optional[:ref:`OUL_R24_PATIENT <hl7-v2_8_1-OUL_R24_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``ORDER``
     -
     - List[:ref:`OUL_R24_ORDER <hl7-v2_8_1-OUL_R24_ORDER>`]
     - required
     -
     - ORDER: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-PEX_P07:

.. py:class:: hl7types.hl7.v2_8_1.messages.PEX_P07.PEX_P07
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_8_1-PEX_P07_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``EXPERIENCE``
     -
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_8_1-PEX_P07_EXPERIENCE>`]
     - required
     -
     - EXPERIENCE: Required, repeating

.. _hl7-v2_8_1-PGL_PC6:

.. py:class:: hl7types.hl7.v2_8_1.messages.PGL_PC6.PGL_PC6
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``GOAL``
     -
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_8_1-PGL_PC6_GOAL>`]
     - required
     -
     - GOAL: Required, repeating

.. _hl7-v2_8_1-PMU_B01:

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B01.PMU_B01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     -
     - STF: Required
   * - ``PRA``
     -
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     -
     - PRA: Optional, repeating
   * - ``ORG``
     -
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     -
     - ORG: Optional, repeating
   * - ``AFF``
     -
     - Optional[List[:ref:`AFF <hl7-v2_8_1-AFF>`]]
     - optional
     -
     - AFF: Optional, repeating
   * - ``LAN``
     -
     - Optional[List[:ref:`LAN <hl7-v2_8_1-LAN>`]]
     - optional
     -
     - LAN: Optional, repeating
   * - ``EDU``
     -
     - Optional[List[:ref:`EDU <hl7-v2_8_1-EDU>`]]
     - optional
     -
     - EDU: Optional, repeating
   * - ``CER``
     -
     - Optional[List[:ref:`CER <hl7-v2_8_1-CER>`]]
     - optional
     -
     - CER: Optional, repeating
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``PRT``
     -
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     -
     - PRT: Optional, repeating
   * - ``ROL``
     -
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     -
     - ROL: Optional, repeating

.. _hl7-v2_8_1-PMU_B03:

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B03.PMU_B03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     -
     - STF: Required

.. _hl7-v2_8_1-PMU_B04:

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B04.PMU_B04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     -
     - STF: Required
   * - ``PRA``
     -
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     -
     - PRA: Optional, repeating
   * - ``ORG``
     -
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     -
     - ORG: Optional, repeating

.. _hl7-v2_8_1-PMU_B07:

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B07.PMU_B07
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     -
     - STF: Required
   * - ``PRA``
     -
     - Optional[:ref:`PRA <hl7-v2_8_1-PRA>`]
     - optional
     -
     - PRA: Optional
   * - ``CERTIFICATE``
     -
     - Optional[List[:ref:`PMU_B07_CERTIFICATE <hl7-v2_8_1-PMU_B07_CERTIFICATE>`]]
     - optional
     -
     - CERTIFICATE: Optional, repeating

.. _hl7-v2_8_1-PMU_B08:

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B08.PMU_B08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EVN``
     -
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     -
     - EVN: Required
   * - ``STF``
     -
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     -
     - STF: Required
   * - ``PRA``
     -
     - Optional[:ref:`PRA <hl7-v2_8_1-PRA>`]
     - optional
     -
     - PRA: Optional
   * - ``CER``
     -
     - Optional[List[:ref:`CER <hl7-v2_8_1-CER>`]]
     - optional
     -
     - CER: Optional, repeating

.. _hl7-v2_8_1-PPG_PCG:

.. py:class:: hl7types.hl7.v2_8_1.messages.PPG_PCG.PPG_PCG
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_8_1-PPG_PCG_PATHWAY>`]
     - required
     -
     - PATHWAY: Required, repeating

.. _hl7-v2_8_1-PPP_PCB:

.. py:class:: hl7types.hl7.v2_8_1.messages.PPP_PCB.PPP_PCB
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PATHWAY``
     -
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_8_1-PPP_PCB_PATHWAY>`]
     - required
     -
     - PATHWAY: Required, repeating

.. _hl7-v2_8_1-PPR_PC1:

.. py:class:: hl7types.hl7.v2_8_1.messages.PPR_PC1.PPR_PC1
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``PROBLEM``
     -
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_8_1-PPR_PC1_PROBLEM>`]
     - required
     -
     - PROBLEM: Required, repeating

.. _hl7-v2_8_1-QBP_E03:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_E03.QBP_E03
   :noindex:

   HL7 v2 QBP_E03 message.

QBP_E03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``QUERY_INFORMATION``
     -
     - :ref:`QBP_E03_QUERY_INFORMATION <hl7-v2_8_1-QBP_E03_QUERY_INFORMATION>`
     - required
     -
     - QUERY_INFORMATION: Required

.. _hl7-v2_8_1-QBP_E22:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_E22.QBP_E22
   :noindex:

   HL7 v2 QBP_E22 message.

QBP_E22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``QUERY``
     -
     - :ref:`QBP_E22_QUERY <hl7-v2_8_1-QBP_E22_QUERY>`
     - required
     -
     - QUERY: Required

.. _hl7-v2_8_1-QBP_O33:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_O33.QBP_O33
   :noindex:

   HL7 v2 QBP_O33 message.

QBP_O33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required

.. _hl7-v2_8_1-QBP_O34:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_O34.QBP_O34
   :noindex:

   HL7 v2 QBP_O34 message.

QBP_O34
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required

.. _hl7-v2_8_1-QBP_Q11:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q11.QBP_Q11
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QBP``
     -
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     -
     - QBP: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QBP_Q13:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q13.QBP_Q13
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``PID``
     -
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     -
     - PID: Optional
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_8_1-RDF>`]
     - optional
     -
     - RDF: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QBP_Q15:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q15.QBP_Q15
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QBP_Q21:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q21.QBP_Q21
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QBP_Qnn:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Qnn.QBP_Qnn
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RDF``
     -
     - Optional[:ref:`RDF <hl7-v2_8_1-RDF>`]
     - optional
     -
     - RDF: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QBP_Z73:

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Z73.QBP_Z73
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required

.. _hl7-v2_8_1-QCN_J01:

.. py:class:: hl7types.hl7.v2_8_1.messages.QCN_J01.QCN_J01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QID``
     -
     - :ref:`QID <hl7-v2_8_1-QID>`
     - required
     -
     - QID: Required

.. _hl7-v2_8_1-QSB_Q16:

.. py:class:: hl7types.hl7.v2_8_1.messages.QSB_Q16.QSB_Q16
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-QVR_Q17:

.. py:class:: hl7types.hl7.v2_8_1.messages.QVR_Q17.QVR_Q17
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QBP``
     -
     - Optional[:ref:`QVR_Q17_QBP <hl7-v2_8_1-QVR_Q17_QBP>`]
     - optional
     -
     - QBP: Optional
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RAS_O17:

.. py:class:: hl7types.hl7.v2_8_1.messages.RAS_O17.RAS_O17
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RAS_O17_PATIENT <hl7-v2_8_1-RAS_O17_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RAS_O17_ORDER <hl7-v2_8_1-RAS_O17_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-RDE_O11:

.. py:class:: hl7types.hl7.v2_8_1.messages.RDE_O11.RDE_O11
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_8_1-RDE_O11_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDE_O11_ORDER <hl7-v2_8_1-RDE_O11_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-RDR_RDR:

.. py:class:: hl7types.hl7.v2_8_1.messages.RDR_RDR.RDR_RDR
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[:ref:`SFT <hl7-v2_8_1-SFT>`]
     - optional
     -
     - SFT: Optional
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``DEFINITION``
     -
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_8_1-RDR_RDR_DEFINITION>`]
     - required
     -
     - DEFINITION: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RDS_O13:

.. py:class:: hl7types.hl7.v2_8_1.messages.RDS_O13.RDS_O13
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RDS_O13_PATIENT <hl7-v2_8_1-RDS_O13_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RDS_O13_ORDER <hl7-v2_8_1-RDS_O13_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-RDY_K15:

.. py:class:: hl7types.hl7.v2_8_1.messages.RDY_K15.RDY_K15
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     -
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RDY_Z80:

.. py:class:: hl7types.hl7.v2_8_1.messages.RDY_Z80.RDY_Z80
   :noindex:

   HL7 v2 RDY_Z80 message.

RDY_Z80
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     -
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-REF_I12:

.. py:class:: hl7types.hl7.v2_8_1.messages.REF_I12.REF_I12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION_CONTACT2``
     -
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-REF_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     -
     - AUTHORIZATION_CONTACT2: Optional
   * - ``PROVIDER_CONTACT``
     -
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     -
     - PROVIDER_CONTACT: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_8_1-REF_I12_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_8_1-REF_I12_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_8_1-REF_I12_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_8_1-REF_I12_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RGV_O15:

.. py:class:: hl7types.hl7.v2_8_1.messages.RGV_O15.RGV_O15
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[:ref:`RGV_O15_PATIENT <hl7-v2_8_1-RGV_O15_PATIENT>`]
     - optional
     -
     - PATIENT: Optional
   * - ``ORDER``
     -
     - List[:ref:`RGV_O15_ORDER <hl7-v2_8_1-RGV_O15_ORDER>`]
     - required
     -
     - ORDER: Required, repeating

.. _hl7-v2_8_1-RPA_I08:

.. py:class:: hl7types.hl7.v2_8_1.messages.RPA_I08.RPA_I08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RPA_I08_AUTHORIZATION <hl7-v2_8_1-RPA_I08_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_8_1-RPA_I08_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_8_1-RPA_I08_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_8_1-RPA_I08_PROCEDURE>`]
     - required
     -
     - PROCEDURE: Required, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_8_1-RPA_I08_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_8_1-RPA_I08_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RPI_I01:

.. py:class:: hl7types.hl7.v2_8_1.messages.RPI_I01.RPI_I01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_8_1-RPI_I01_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RPI_I04:

.. py:class:: hl7types.hl7.v2_8_1.messages.RPI_I04.RPI_I04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPI_I04_PROVIDER <hl7-v2_8_1-RPI_I04_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_8_1-RPI_I04_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RPL_I02:

.. py:class:: hl7types.hl7.v2_8_1.messages.RPL_I02.RPL_I02
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_8_1-RPL_I02_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``DSP``
     -
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     -
     - DSP: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RPR_I03:

.. py:class:: hl7types.hl7.v2_8_1.messages.RPR_I03.RPR_I03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``PROVIDER``
     -
     - List[:ref:`RPR_I03_PROVIDER <hl7-v2_8_1-RPR_I03_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - Optional[List[:ref:`PID <hl7-v2_8_1-PID>`]]
     - optional
     -
     - PID: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RQA_I08:

.. py:class:: hl7types.hl7.v2_8_1.messages.RQA_I08.RQA_I08
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION``
     -
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_8_1-RQA_I08_AUTHORIZATION>`]
     - optional
     -
     - AUTHORIZATION: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_8_1-RQA_I08_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_8_1-RQA_I08_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_8_1-RQA_I08_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``VISIT``
     -
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_8_1-RQA_I08_VISIT>`]
     - optional
     -
     - VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RQI_I01:

.. py:class:: hl7types.hl7.v2_8_1.messages.RQI_I01.RQI_I01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_8_1-RQI_I01_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GUARANTOR_INSURANCE``
     -
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     -
     - GUARANTOR_INSURANCE: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RQP_I04:

.. py:class:: hl7types.hl7.v2_8_1.messages.RQP_I04.RQP_I04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PROVIDER``
     -
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_8_1-RQP_I04_PROVIDER>`]
     - required
     -
     - PROVIDER: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RRA_O18:

.. py:class:: hl7types.hl7.v2_8_1.messages.RRA_O18.RRA_O18
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRA_O18_RESPONSE <hl7-v2_8_1-RRA_O18_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-RRD_O14:

.. py:class:: hl7types.hl7.v2_8_1.messages.RRD_O14.RRD_O14
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRD_O14_RESPONSE <hl7-v2_8_1-RRD_O14_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-RRE_O12:

.. py:class:: hl7types.hl7.v2_8_1.messages.RRE_O12.RRE_O12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_8_1-RRE_O12_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-RRG_O16:

.. py:class:: hl7types.hl7.v2_8_1.messages.RRG_O16.RRG_O16
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``RESPONSE``
     -
     - Optional[:ref:`RRG_O16_RESPONSE <hl7-v2_8_1-RRG_O16_RESPONSE>`]
     - optional
     -
     - RESPONSE: Optional

.. _hl7-v2_8_1-RRI_I12:

.. py:class:: hl7types.hl7.v2_8_1.messages.RRI_I12.RRI_I12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - Optional[:ref:`MSA <hl7-v2_8_1-MSA>`]
     - optional
     -
     - MSA: Optional
   * - ``RF1``
     -
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     -
     - RF1: Optional
   * - ``AUTHORIZATION_CONTACT2``
     -
     - Optional[:ref:`RRI_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-RRI_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     -
     - AUTHORIZATION_CONTACT2: Optional
   * - ``PROVIDER_CONTACT``
     -
     - List[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_8_1-RRI_I12_PROVIDER_CONTACT>`]
     - required
     -
     - PROVIDER_CONTACT: Required, repeating
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``ACC``
     -
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     -
     - ACC: Optional
   * - ``DG1``
     -
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     -
     - DG1: Optional, repeating
   * - ``DRG``
     -
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     -
     - DRG: Optional, repeating
   * - ``AL1``
     -
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     -
     - AL1: Optional, repeating
   * - ``PROCEDURE``
     -
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_8_1-RRI_I12_PROCEDURE>`]]
     - optional
     -
     - PROCEDURE: Optional, repeating
   * - ``OBSERVATION``
     -
     - Optional[List[:ref:`RRI_I12_OBSERVATION <hl7-v2_8_1-RRI_I12_OBSERVATION>`]]
     - optional
     -
     - OBSERVATION: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`RRI_I12_PATIENT_VISIT <hl7-v2_8_1-RRI_I12_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating

.. _hl7-v2_8_1-RSP_E03:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_E03.RSP_E03
   :noindex:

   HL7 v2 RSP_E03 message.

RSP_E03
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``QUERY_ACK_IPR``
     -
     - :ref:`RSP_E03_QUERY_ACK_IPR <hl7-v2_8_1-RSP_E03_QUERY_ACK_IPR>`
     - required
     -
     - QUERY_ACK_IPR: Required

.. _hl7-v2_8_1-RSP_E22:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_E22.RSP_E22
   :noindex:

   HL7 v2 RSP_E22 message.

RSP_E22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     -
     - UAC: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``QUERY_ACK``
     -
     - :ref:`RSP_E22_QUERY_ACK <hl7-v2_8_1-RSP_E22_QUERY_ACK>`
     - required
     -
     - QUERY_ACK: Required

.. _hl7-v2_8_1-RSP_K11:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K11.RSP_K11
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``SEGMENT_PATTERN``
     -
     - Optional[:ref:`RSP_K11_SEGMENT_PATTERN <hl7-v2_8_1-RSP_K11_SEGMENT_PATTERN>`]
     - optional
     -
     - SEGMENT_PATTERN: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K21:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K21.RSP_K21
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[:ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_8_1-RSP_K21_QUERY_RESPONSE>`]
     - optional
     -
     - QUERY_RESPONSE: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K22:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K22.RSP_K22
   :noindex:

   HL7 v2 RSP_K22 message.

RSP_K22
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[List[:ref:`RSP_K22_QUERY_RESPONSE <hl7-v2_8_1-RSP_K22_QUERY_RESPONSE>`]]
     - optional
     -
     - QUERY_RESPONSE: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K23:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K23.RSP_K23
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_8_1-RSP_K23_QUERY_RESPONSE>`]
     - optional
     -
     - QUERY_RESPONSE: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K25:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K25.RSP_K25
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``STAFF``
     -
     - List[:ref:`RSP_K25_STAFF <hl7-v2_8_1-RSP_K25_STAFF>`]
     - required
     -
     - STAFF: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K31:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K31.RSP_K31
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``RESPONSE``
     -
     - List[:ref:`RSP_K31_RESPONSE <hl7-v2_8_1-RSP_K31_RESPONSE>`]
     - required
     -
     - RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_K32:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K32.RSP_K32
   :noindex:

   HL7 v2 RSP_K32 message.

RSP_K32
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - Optional[List[:ref:`RSP_K32_QUERY_RESPONSE <hl7-v2_8_1-RSP_K32_QUERY_RESPONSE>`]]
     - optional
     -
     - QUERY_RESPONSE: Optional, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_O33:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_O33.RSP_O33
   :noindex:

   HL7 v2 RSP_O33 message.

RSP_O33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DONOR``
     -
     - Optional[:ref:`RSP_O33_DONOR <hl7-v2_8_1-RSP_O33_DONOR>`]
     - optional
     -
     - DONOR: Optional

.. _hl7-v2_8_1-RSP_O34:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_O34.RSP_O34
   :noindex:

   HL7 v2 RSP_O34 message.

RSP_O34
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DONOR``
     -
     - Optional[:ref:`RSP_O34_DONOR <hl7-v2_8_1-RSP_O34_DONOR>`]
     - optional
     -
     - DONOR: Optional
   * - ``DONATION``
     -
     - Optional[:ref:`RSP_O34_DONATION <hl7-v2_8_1-RSP_O34_DONATION>`]
     - optional
     -
     - DONATION: Optional

.. _hl7-v2_8_1-RSP_Z82:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z82.RSP_Z82
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z82_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_Z84:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z84.RSP_Z84
   :noindex:

   HL7 v2 RSP_Z84 message.

RSP_Z84
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RSP_Z84_ROW_DEFINITION <hl7-v2_8_1-RSP_Z84_ROW_DEFINITION>`]
     - optional
     -
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_Z86:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z86.RSP_Z86
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z86_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RSP_Z88:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z88.RSP_Z88
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z88_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_8_1-DSC>`
     - required
     -
     - DSC: Required

.. _hl7-v2_8_1-RSP_Z90:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z90.RSP_Z90
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``RCP``
     -
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     -
     - RCP: Required
   * - ``QUERY_RESPONSE``
     -
     - List[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z90_QUERY_RESPONSE>`]
     - required
     -
     - QUERY_RESPONSE: Required, repeating
   * - ``DSC``
     -
     - :ref:`DSC <hl7-v2_8_1-DSC>`
     - required
     -
     - DSC: Required

.. _hl7-v2_8_1-RSP_Znn:

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Znn.RSP_Znn
   :noindex:

   HL7 v2 RSP_Znn message.

RSP_Znn
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RTB_K13:

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_K13.RTB_K13
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     -
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RTB_Knn:

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Knn.RTB_Knn
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     -
     - ERR: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-RTB_Z74:

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z74.RTB_Z74
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``QAK``
     -
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     -
     - QAK: Required
   * - ``QPD``
     -
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     -
     - QPD: Required
   * - ``ROW_DEFINITION``
     -
     - Optional[:ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_8_1-RTB_Z74_ROW_DEFINITION>`]
     - optional
     -
     - ROW_DEFINITION: Optional
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-SDR_S31:

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S31.SDR_S31
   :noindex:

   HL7 v2 SDR_S31 message.

SDR_S31
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``ANTI_MICROBIAL_DEVICE_DATA``
     -
     - :ref:`SDR_S31_ANTI_MICROBIAL_DEVICE_DATA <hl7-v2_8_1-SDR_S31_ANTI_MICROBIAL_DEVICE_DATA>`
     - required
     -
     - ANTI_MICROBIAL_DEVICE_DATA: Required

.. _hl7-v2_8_1-SDR_S32:

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S32.SDR_S32
   :noindex:

   HL7 v2 SDR_S32 message.

SDR_S32
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``ANTI_MICROBIAL_DEVICE_CYCLE_DATA``
     -
     - :ref:`SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA <hl7-v2_8_1-SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA>`
     - required
     -
     - ANTI_MICROBIAL_DEVICE_CYCLE_DATA: Required

.. _hl7-v2_8_1-SIU_S12:

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S12.SIU_S12
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SCH``
     -
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     -
     - SCH: Required
   * - ``TQ1``
     -
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     -
     - TQ1: Optional, repeating
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     -
     - RESOURCES: Required, repeating

.. _hl7-v2_8_1-SLR_S28:

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S28.SLR_S28
   :noindex:

   HL7 v2 SLR_S28 message.

SLR_S28
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``SLT``
     -
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     -
     - SLT: Required, repeating

.. _hl7-v2_8_1-SRM_S01:

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S01.SRM_S01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``ARQ``
     -
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     -
     - ARQ: Required
   * - ``APR``
     -
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     -
     - APR: Optional
   * - ``NTE``
     -
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     -
     - NTE: Optional, repeating
   * - ``PATIENT``
     -
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     -
     - PATIENT: Optional, repeating
   * - ``RESOURCES``
     -
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     -
     - RESOURCES: Required, repeating

.. _hl7-v2_8_1-SRR_S01:

.. py:class:: hl7types.hl7.v2_8_1.messages.SRR_S01.SRR_S01
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``MSA``
     -
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     -
     - MSA: Required
   * - ``ERR``
     -
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     -
     - ERR: Optional, repeating
   * - ``SCHEDULE``
     -
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_8_1-SRR_S01_SCHEDULE>`]
     - optional
     -
     - SCHEDULE: Optional

.. _hl7-v2_8_1-SSR_U04:

.. py:class:: hl7types.hl7.v2_8_1.messages.SSR_U04.SSR_U04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``SPECIMEN_CONTAINER``
     -
     - List[:ref:`SSR_U04_SPECIMEN_CONTAINER <hl7-v2_8_1-SSR_U04_SPECIMEN_CONTAINER>`]
     - required
     -
     - SPECIMEN_CONTAINER: Required, repeating

.. _hl7-v2_8_1-SSU_U03:

.. py:class:: hl7types.hl7.v2_8_1.messages.SSU_U03.SSU_U03
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``SPECIMEN_CONTAINER``
     -
     - List[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_8_1-SSU_U03_SPECIMEN_CONTAINER>`]
     - required
     -
     - SPECIMEN_CONTAINER: Required, repeating

.. _hl7-v2_8_1-STC_S33:

.. py:class:: hl7types.hl7.v2_8_1.messages.STC_S33.STC_S33
   :noindex:

   HL7 v2 STC_S33 message.

STC_S33
~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``SCP``
     -
     - List[:ref:`SCP <hl7-v2_8_1-SCP>`]
     - required
     -
     - SCP: Required, repeating

.. _hl7-v2_8_1-TCU_U10:

.. py:class:: hl7types.hl7.v2_8_1.messages.TCU_U10.TCU_U10
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``EQU``
     -
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     -
     - EQU: Required
   * - ``TEST_CONFIGURATION``
     -
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_8_1-TCU_U10_TEST_CONFIGURATION>`]
     - required
     -
     - TEST_CONFIGURATION: Required, repeating

.. _hl7-v2_8_1-UDM_Q05:

.. py:class:: hl7types.hl7.v2_8_1.messages.UDM_Q05.UDM_Q05
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``URD``
     -
     - :ref:`URD <hl7-v2_8_1-URD>`
     - required
     -
     - URD: Required
   * - ``URS``
     -
     - Optional[:ref:`URS <hl7-v2_8_1-URS>`]
     - optional
     -
     - URS: Optional
   * - ``DSP``
     -
     - List[:ref:`DSP <hl7-v2_8_1-DSP>`]
     - required
     -
     - DSP: Required, repeating
   * - ``DSC``
     -
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     -
     - DSC: Optional

.. _hl7-v2_8_1-VXU_V04:

.. py:class:: hl7types.hl7.v2_8_1.messages.VXU_V04.VXU_V04
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
     - Max Length
     - Description
   * - ``MSH``
     -
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     -
     - MSH: Required
   * - ``SFT``
     -
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     -
     - SFT: Optional, repeating
   * - ``UAC``
     -
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     -
     - UAC: Optional
   * - ``PID``
     -
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     -
     - PID: Required
   * - ``PD1``
     -
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     -
     - PD1: Optional
   * - ``NK1``
     -
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     -
     - NK1: Optional, repeating
   * - ``ARV``
     -
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     -
     - ARV: Optional, repeating
   * - ``PATIENT_VISIT``
     -
     - Optional[:ref:`VXU_V04_PATIENT_VISIT <hl7-v2_8_1-VXU_V04_PATIENT_VISIT>`]
     - optional
     -
     - PATIENT_VISIT: Optional
   * - ``GT1``
     -
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     -
     - GT1: Optional, repeating
   * - ``INSURANCE``
     -
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_8_1-VXU_V04_INSURANCE>`]]
     - optional
     -
     - INSURANCE: Optional, repeating
   * - ``PERSON_OBSERVATION``
     -
     - Optional[List[:ref:`VXU_V04_PERSON_OBSERVATION <hl7-v2_8_1-VXU_V04_PERSON_OBSERVATION>`]]
     - optional
     -
     - PERSON_OBSERVATION: Optional, repeating
   * - ``ORDER``
     -
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_8_1-VXU_V04_ORDER>`]]
     - optional
     -
     - ORDER: Optional, repeating
