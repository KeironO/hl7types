v2.5.1 Messages
===============

.. _hl7-v2_5_1-ACK:

ACK General acknowledgment message (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error

.. _hl7-v2_5_1-ADR_A19:

ADR_A19 QRY/ADR -  Patient query (S3.3.19).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADR_A19.ADR_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``QUERY_RESPONSE``
     - List[:ref:`ADR_A19_QUERY_RESPONSE <hl7-v2_5_1-ADR_A19_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-ADT_A01:

ADT_A01 ADT/ACK - Admit/visit notification (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_5_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_5_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A02:

ADT_A02 ADT/ACK - Transfer a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A03:

ADT_A03 ADT/ACK -  Discharge/end visit (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_5_1-ADT_A03_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A03_INSURANCE <hl7-v2_5_1-ADT_A03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A04:

ADT_A04 ADT/ACK -  Register a patient (S3.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_5_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_5_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A05:

ADT_A05 ADT/ACK -  Pre-admit a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_5_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_5_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A06:

ADT_A06 ADT/ACK -  Change an outpatient to an inpatient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_5_1-MRG>`]
     - optional
     - Merge Patient Information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_5_1-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_5_1-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A07:

ADT_A07 ADT/ACK -  Change an inpatient to an outpatient (S3.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_5_1-MRG>`]
     - optional
     - Merge Patient Information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_5_1-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_5_1-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A08:

ADT_A08 ADT/ACK -  Update patient information (S3.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_5_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_5_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A09:

ADT_A09 ADT/ACK -  Patient departing - tracking (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_5_1-ADT_A10:

ADT_A10 ADT/ACK -  Patient arriving - tracking (S3.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_5_1-ADT_A11:

ADT_A11 ADT/ACK -  Cancel admit/visit notification (S3.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_5_1-ADT_A12:

ADT_A12 ADT/ACK -  Cancel transfer (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_5_1-DG1>`]
     - optional
     - Diagnosis

.. _hl7-v2_5_1-ADT_A13:

ADT_A13 ADT/ACK -  Cancel discharge/end visit (S3.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_5_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_5_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_5_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_5_1-ADT_A14:

ADT_A14 ADT/ACK -  Pending admit (S3.3.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_5_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_5_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A15:

ADT_A15 ADT/ACK -  Pending transfer (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_5_1-ADT_A16:

ADT_A16 ADT/ACK -  Pending discharge (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A16_PROCEDURE <hl7-v2_5_1-ADT_A16_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A16_INSURANCE <hl7-v2_5_1-ADT_A16_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident

.. _hl7-v2_5_1-ADT_A17:

ADT_A17 ADT/ACK -  Swap patients (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_5_1-ADT_A18:

ADT_A18 ADT/ACK -  Merge patient information (for backward compatibility only) (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A18.ADT_A18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit

.. _hl7-v2_5_1-ADT_A20:

ADT_A20 ADT/ACK -  Bed status update (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``NPU``
     - :ref:`NPU <hl7-v2_5_1-NPU>`
     - required
     - Bed Status Update

.. _hl7-v2_5_1-ADT_A21:

ADT_A21 HL7 v2 ADT_A21 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A21.ADT_A21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_5_1-ADT_A24:

ADT_A24 ADT/ACK -  Link patient information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_5_1-PV1>`]
     - optional
     - Patient Visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability

.. _hl7-v2_5_1-ADT_A28:

ADT_A28 ADT/ACK -  Add person information (S3.3.28).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_5_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_5_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A30:

ADT_A30 ADT/ACK -  Merge person information (for backward compatibility only) (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A30.ADT_A30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A31:

ADT_A31 ADT/ACK -  Update person information (S3.3.31).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_5_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_5_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_5_1-UB1>`]
     - optional
     - UB82
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_5_1-UB2>`]
     - optional
     - UB92 Data

.. _hl7-v2_5_1-ADT_A34:

ADT_A34 ADT/ACK -  Merge patient information - patient ID only (for backward compatibili (S3.3.34).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A34.ADT_A34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A35:

ADT_A35 ADT/ACK -  Merge patient information - account number only (for backward compati (S3.3.35).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A35.ADT_A35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A36:

ADT_A36 ADT/ACK -  Merge patient information - patient ID and account number (for backwa (S3.3.36).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A36.ADT_A36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A37:

ADT_A37 ADT/ACK -  Unlink patient information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_5_1-PV1>`]
     - optional
     - Patient Visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability

.. _hl7-v2_5_1-ADT_A38:

ADT_A38 ADT/ACK - Cancel pre-admit (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_5_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group

.. _hl7-v2_5_1-ADT_A39:

ADT_A39 ADT/ACK - Merge person - patient ID (for backward compatibility only) (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_5_1-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A40:

ADT_A40 ADT/ACK - Merge patient - patient identifier list (S3.3.40).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A40.ADT_A40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_5_1-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A41:

ADT_A41 ADT/ACK - Merge account - patient account number (S3.3.41).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A41.ADT_A41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_5_1-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A42:

ADT_A42 ADT/ACK - Merge visit - visit number (S3.3.42).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A42.ADT_A42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_5_1-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A43:

ADT_A43 ADT/ACK - Move patient information - patient identifier list (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_5_1-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A44:

ADT_A44 ADT/ACK - Move account information - patient account number (S3.3.44).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_5_1-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-ADT_A45:

ADT_A45 ADT/ACK - Move visit information - visit number (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MERGE_INFO``
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_5_1-ADT_A45_MERGE_INFO>`]
     - required
     - MERGE_INFO

.. _hl7-v2_5_1-ADT_A46:

ADT_A46 ADT/ACK - Change patient ID (for backward compatibility only) (S3.3.46).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A46.ADT_A46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A47:

ADT_A47 ADT/ACK - Change patient identifier list (S3.3.47).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A48:

ADT_A48 ADT/ACK - Change alternate patient ID (for backward compatibility only) (S3.3.48).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A48.ADT_A48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A49:

ADT_A49 ADT/ACK - Change patient account number (S3.3.49).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information

.. _hl7-v2_5_1-ADT_A50:

ADT_A50 ADT/ACK - Change visit number (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit

.. _hl7-v2_5_1-ADT_A51:

ADT_A51 ADT/ACK - Change alternate visit ID (S3.3.51).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_5_1-MRG>`
     - required
     - Merge Patient Information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit

.. _hl7-v2_5_1-ADT_A52:

ADT_A52 ADT/ACK - Cancel leave of absence for a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A52.ADT_A52
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-ADT_A53:

ADT_A53 ADT/ACK - Cancel patient returns from a leave of absence (S3.3.53).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A53.ADT_A53
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-ADT_A54:

ADT_A54 ADT/ACK - Change attending doctor (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A54.ADT_A54
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-ADT_A55:

ADT_A55 ADT/ACK - Cancel change attending doctor (S3.3.55).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A55.ADT_A55
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-ADT_A60:

ADT_A60 ADT/ACK - Update allergy information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A60.ADT_A60
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_5_1-PV1>`]
     - optional
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``IAM``
     - Optional[List[:ref:`IAM <hl7-v2_5_1-IAM>`]]
     - optional
     - Patient Adverse Reaction Information

.. _hl7-v2_5_1-ADT_A61:

ADT_A61 ADT/ACK - Change consulting doctor (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A61.ADT_A61
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-ADT_A62:

ADT_A62 ADT/ACK - Cancel change consulting doctor (S3.3.62).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ADT_A62.ADT_A62
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_5_1-BAR_P01:

BAR_P01 BAR/ACK - Add patient accounts (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_5_1-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_5_1-BAR_P02:

BAR_P02 BAR/ACK - Purge patient accounts (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_5_1-BAR_P02_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-BAR_P05:

BAR_P05 BAR/ACK - Update account (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - List[:ref:`BAR_P05_VISIT <hl7-v2_5_1-BAR_P05_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_5_1-BAR_P06:

BAR_P06 BAR/ACK - End account (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_5_1-BAR_P06_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-BAR_P10:

BAR_P10 BAR/ACK -Transmit Ambulatory Payment  Classification(APC) (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P10.BAR_P10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``GP1``
     - :ref:`GP1 <hl7-v2_5_1-GP1>`
     - required
     - Grouping/Reimbursement - Visit
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P10_PROCEDURE <hl7-v2_5_1-BAR_P10_PROCEDURE>`]]
     - optional
     - PROCEDURE

.. _hl7-v2_5_1-BAR_P12:

BAR_P12 BAR/ACK - Update Diagnosis/Procedure (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BAR_P12.BAR_P12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P12_PROCEDURE <hl7-v2_5_1-BAR_P12_PROCEDURE>`]]
     - optional
     - PROCEDURE

.. _hl7-v2_5_1-BPS_O29:

BPS_O29 BPS - Blood product dispense status (S4.20.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BPS_O29.BPS_O29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`BPS_O29_PATIENT <hl7-v2_5_1-BPS_O29_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`BPS_O29_ORDER <hl7-v2_5_1-BPS_O29_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-BRP_O30:

BRP_O30 BRP - Blood product dispense status acknowledgment (S4.20.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BRP_O30.BRP_O30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`BRP_O30_RESPONSE <hl7-v2_5_1-BRP_O30_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-BRT_O32:

BRT_O32 BRT - Blood product transfusion/disposition acknowledgment (S4.20.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BRT_O32.BRT_O32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`BRT_O32_RESPONSE <hl7-v2_5_1-BRT_O32_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-BTS_O31:

BTS_O31 BTS - Blood product transfusion/disposition (S4.20.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.BTS_O31.BTS_O31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`BTS_O31_PATIENT <hl7-v2_5_1-BTS_O31_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`BTS_O31_ORDER <hl7-v2_5_1-BTS_O31_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-CRM_C01:

CRM_C01 CRM - Register a patient on a clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C02:

CRM_C02 CRM - Cancel a patient registration on clinical trial (for clerical mistakes onl (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C03:

CRM_C03 CRM - Correct/update registration information (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C04:

CRM_C04 CRM - Patient has gone off a clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C05:

CRM_C05 CRM - Patient enters phase of clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C06:

CRM_C06 CRM - Cancel patient entering a phase (clerical mistake) (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C07:

CRM_C07 CRM - Correct/update phase information (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CRM_C08:

CRM_C08 CRM - Patient has gone off phase of clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_5_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CSU_C09:

CSU_C09 CSU - Automated time intervals for reporting, like monthly (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_5_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CSU_C10:

CSU_C10 CSU - Patient completes the clinical trial (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_5_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CSU_C11:

CSU_C11 CSU - Patient completes a phase of the clinical trial (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_5_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-CSU_C12:

CSU_C12 CSU - Update/correction of patient order/result information (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_5_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-DFT_P03:

DFT_P03 DFT/ACK - Post detail financial transaction (S6.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_5_1-PV1>`]
     - optional
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_5_1-DFT_P03_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``FINANCIAL``
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_5_1-DFT_P03_FINANCIAL>`]
     - required
     - FINANCIAL
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_5_1-DFT_P03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident

.. _hl7-v2_5_1-DFT_P11:

DFT_P11 DFT/ACK - Post Detail Financial Transactions - New (S6.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.DFT_P11.DFT_P11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_5_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_5_1-PV1>`]
     - optional
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_5_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_5_1-DB1>`]]
     - optional
     - Disability
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_5_1-DFT_P11_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_5_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`DFT_P11_INSURANCE <hl7-v2_5_1-DFT_P11_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``FINANCIAL``
     - List[:ref:`DFT_P11_FINANCIAL <hl7-v2_5_1-DFT_P11_FINANCIAL>`]
     - required
     - FINANCIAL

.. _hl7-v2_5_1-DOC_T12:

DOC_T12 QRY/DOC - Document query (S9.8.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.DOC_T12.DOC_T12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``EVNPIDPV1TXAOBX_SUPPGRP``
     - List[:ref:`DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP <hl7-v2_5_1-DOC_T12_EVNPIDPV1TXAOBX_SUPPGRP>`]
     - required
     - EVNPIDPV1TXAOBX_SUPPGRP
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-DSR_Q01:

DSR_Q01 HL7 v2 DSR_Q01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.DSR_Q01.DSR_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_5_1-DSP>`]
     - required
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-DSR_Q03:

DSR_Q03 HL7 v2 DSR_Q03 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.DSR_Q03.DSR_Q03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_5_1-MSA>`]
     - optional
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_5_1-DSP>`]
     - required
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-EAC_U07:

EAC_U07 EAC/ACK - Automated equipment command (S13.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.EAC_U07.EAC_U07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``COMMAND``
     - List[:ref:`EAC_U07_COMMAND <hl7-v2_5_1-EAC_U07_COMMAND>`]
     - required
     - COMMAND
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-EAN_U09:

EAN_U09 EAN/ACK - Automated equipment notification (S13.3.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.EAN_U09.EAN_U09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``NOTIFICATION``
     - List[:ref:`EAN_U09_NOTIFICATION <hl7-v2_5_1-EAN_U09_NOTIFICATION>`]
     - required
     - NOTIFICATION
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-EAR_U08:

EAR_U08 EAR/ACK - Automated equipment response (S13.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.EAR_U08.EAR_U08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``COMMAND_RESPONSE``
     - List[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_5_1-EAR_U08_COMMAND_RESPONSE>`]
     - required
     - COMMAND_RESPONSE
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-EDR_R07:

EDR_R07 HL7 v2 EDR_R07 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.EDR_R07.EDR_R07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_5_1-DSP>`]
     - required
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-EQQ_Q04:

EQQ_Q04 HL7 v2 EQQ_Q04 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.EQQ_Q04.EQQ_Q04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQL``
     - :ref:`EQL <hl7-v2_5_1-EQL>`
     - required
     - Embedded Query Language
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-ERP_R09:

ERP_R09 HL7 v2 ERP_R09 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ERP_R09.ERP_R09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_5_1-ERQ>`
     - required
     - Event replay query
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-ESR_U02:

ESR_U02 ESR/ACK - Automated equipment status request (S13.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ESR_U02.ESR_U02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-ESU_U01:

ESU_U01 ESU/ACK - Automated equipment status update (S13.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ESU_U01.ESU_U01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``ISD``
     - Optional[List[:ref:`ISD <hl7-v2_5_1-ISD>`]]
     - optional
     - Interaction Status Detail
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-INR_U06:

INR_U06 INR/ACK - Automated equipment inventory request (S13.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.INR_U06.INR_U06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``INV``
     - List[:ref:`INV <hl7-v2_5_1-INV>`]
     - required
     - Inventory Detail
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-INU_U05:

INU_U05 INU/ACK  - Automated equipment inventory update (S13.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.INU_U05.INU_U05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``INV``
     - List[:ref:`INV <hl7-v2_5_1-INV>`]
     - required
     - Inventory Detail
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-LSU_U12:

LSU_U12 LSU/ACK - Automated equipment log/service update (S13.3.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.LSU_U12.LSU_U12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``EQP``
     - List[:ref:`EQP <hl7-v2_5_1-EQP>`]
     - required
     - Equipment/log Service
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-LSU_U13:

LSU_U13 LSR/ACK - Automated equipment log/service request (S13.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.LSU_U13.LSU_U13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``EQP``
     - List[:ref:`EQP <hl7-v2_5_1-EQP>`]
     - required
     - Equipment/log Service
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-MDM_T01:

MDM_T01 MDM/ACK - Original document notification (S9.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MDM_T02:

MDM_T02 MDM/ACK - Original document notification and content (S9.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header
   * - ``OBXNTE_SUPPGRP``
     - List[:ref:`MDM_T02_OBXNTE_SUPPGRP <hl7-v2_5_1-MDM_T02_OBXNTE_SUPPGRP>`]
     - required
     - OBXNTE_SUPPGRP

.. _hl7-v2_5_1-MDM_T03:

MDM_T03 MDM/ACK - Document status change notification (S9.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MDM_T04:

MDM_T04 MDM/ACK - Document status change notification and content (S9.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header
   * - ``OBXNTE_SUPPGRP``
     - List[:ref:`MDM_T02_OBXNTE_SUPPGRP <hl7-v2_5_1-MDM_T02_OBXNTE_SUPPGRP>`]
     - required
     - OBXNTE_SUPPGRP

.. _hl7-v2_5_1-MDM_T05:

MDM_T05 MDM/ACK - Document addendum notification (S9.5.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MDM_T06:

MDM_T06 MDM/ACK - Document addendum notification and content (S9.5.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header
   * - ``OBXNTE_SUPPGRP``
     - List[:ref:`MDM_T02_OBXNTE_SUPPGRP <hl7-v2_5_1-MDM_T02_OBXNTE_SUPPGRP>`]
     - required
     - OBXNTE_SUPPGRP

.. _hl7-v2_5_1-MDM_T07:

MDM_T07 MDM/ACK - Document edit notification (S9.5.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MDM_T08:

MDM_T08 MDM/ACK - Document edit notification and content (S9.5.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header
   * - ``OBXNTE_SUPPGRP``
     - List[:ref:`MDM_T02_OBXNTE_SUPPGRP <hl7-v2_5_1-MDM_T02_OBXNTE_SUPPGRP>`]
     - required
     - OBXNTE_SUPPGRP

.. _hl7-v2_5_1-MDM_T09:

MDM_T09 MDM/ACK - Document replacement notification (S9.5.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MDM_T10:

MDM_T10 MDM/ACK - Document replacement notification and content (S9.5.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_5_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header
   * - ``OBXNTE_SUPPGRP``
     - List[:ref:`MDM_T02_OBXNTE_SUPPGRP <hl7-v2_5_1-MDM_T02_OBXNTE_SUPPGRP>`]
     - required
     - OBXNTE_SUPPGRP

.. _hl7-v2_5_1-MDM_T11:

MDM_T11 MDM/ACK - Document cancel notification (S9.5.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_5_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_5_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_5_1-TXA>`
     - required
     - Transcription Document Header

.. _hl7-v2_5_1-MFK_M01:

MFK_M01 MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_5_1-MFA>`]]
     - optional
     - Master File Acknowledgment

.. _hl7-v2_5_1-MFN_M01:

MFN_M01 MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M01.MFN_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF``
     - List[:ref:`MFN_M01_MF <hl7-v2_5_1-MFN_M01_MF>`]
     - required
     - MF

.. _hl7-v2_5_1-MFN_M02:

MFN_M02 MFN/MFK - Master file - staff practitioner (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_STAFF``
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_5_1-MFN_M02_MF_STAFF>`]
     - required
     - MF_STAFF

.. _hl7-v2_5_1-MFN_M03:

MFN_M03 MFN/MFK - Master file - test/observation (for backward compatibility only) (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M03.MFN_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST``
     - List[:ref:`MFN_M03_MF_TEST <hl7-v2_5_1-MFN_M03_MF_TEST>`]
     - required
     - MF_TEST

.. _hl7-v2_5_1-MFN_M04:

MFN_M04 MFN/MFK - Master files charge description (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_CDM``
     - List[:ref:`MFN_M04_MF_CDM <hl7-v2_5_1-MFN_M04_MF_CDM>`]
     - required
     - MF_CDM

.. _hl7-v2_5_1-MFN_M05:

MFN_M05 MFN/MFK - Patient location master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_LOCATION``
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_5_1-MFN_M05_MF_LOCATION>`]
     - required
     - MF_LOCATION

.. _hl7-v2_5_1-MFN_M06:

MFN_M06 MFN/MFK - Clinical study with phases and schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_CLIN_STUDY``
     - List[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_5_1-MFN_M06_MF_CLIN_STUDY>`]
     - required
     - MF_CLIN_STUDY

.. _hl7-v2_5_1-MFN_M07:

MFN_M07 MFN/MFK - Clinical study without phases but with schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_CLIN_STUDY_SCHED``
     - List[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_5_1-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - required
     - MF_CLIN_STUDY_SCHED

.. _hl7-v2_5_1-MFN_M08:

MFN_M08 MFN/MFK - Test/observation (numeric) master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_NUMERIC``
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_5_1-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     - MF_TEST_NUMERIC

.. _hl7-v2_5_1-MFN_M09:

MFN_M09 MFN/MFK - Test/observation (categorical) master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_CATEGORICAL``
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_5_1-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     - MF_TEST_CATEGORICAL

.. _hl7-v2_5_1-MFN_M10:

MFN_M10 MFN/MFK - Test /observation batteries master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_BATTERIES``
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_5_1-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     - MF_TEST_BATTERIES

.. _hl7-v2_5_1-MFN_M11:

MFN_M11 MFN/MFK - Test/calculated observations master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_CALCULATED``
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_5_1-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     - MF_TEST_CALCULATED

.. _hl7-v2_5_1-MFN_M12:

MFN_M12 MFN/MFK - Master file notification message (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M12.MFN_M12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_OBS_ATTRIBUTES``
     - List[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_5_1-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - required
     - MF_OBS_ATTRIBUTES

.. _hl7-v2_5_1-MFN_M13:

MFN_M13 MFN/MFK - Master file notification - general (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M13.MFN_M13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MFE``
     - List[:ref:`MFE <hl7-v2_5_1-MFE>`]
     - required
     - Master File Entry

.. _hl7-v2_5_1-MFN_M15:

MFN_M15 MFN/MFK - Inventory item master file notification (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_M15.MFN_M15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_INV_ITEM``
     - List[:ref:`MFN_M15_MF_INV_ITEM <hl7-v2_5_1-MFN_M15_MF_INV_ITEM>`]
     - required
     - MF_INV_ITEM

.. _hl7-v2_5_1-MFN_Znn:

MFN_Znn HL7 v2 MFN_Znn message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFN_Znn.MFN_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_SITE_DEFINED``
     - List[MFN_ZnnMF_SITE_DEFINED]
     - required
     - MF_SITE_DEFINED

.. _hl7-v2_5_1-MFQ_M01:

MFQ_M01 MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M01.MFQ_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M02:

MFQ_M02 MFN/MFK - Master file - staff practitioner (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M02.MFQ_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M03:

MFQ_M03 MFN/MFK - Master file - test/observation (for backward compatibility only) (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M03.MFQ_M03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M04:

MFQ_M04 MFN/MFK - Master files charge description (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M04.MFQ_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M05:

MFQ_M05 MFN/MFK - Patient location master file (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M05.MFQ_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M06:

MFQ_M06 MFN/MFK - Clinical study with phases and schedules master file (S8.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M06.MFQ_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M07:

MFQ_M07 MFN/MFK - Clinical study without phases but with schedules master file (S8.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M07.MFQ_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M08:

MFQ_M08 MFN/MFK - Test/observation (numeric) master file (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M08.MFQ_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M09:

MFQ_M09 MFN/MFK - Test/observation (categorical) master file (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M09.MFQ_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M10:

MFQ_M10 MFN/MFK - Test /observation batteries master file (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M10.MFQ_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M11:

MFQ_M11 MFN/MFK - Test/calculated observations master file (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M11.MFQ_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M12:

MFQ_M12 MFN/MFK - Master file notification message (S8.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M12.MFQ_M12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M13:

MFQ_M13 MFN/MFK - Master file notification - general (S8.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M13.MFQ_M13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFQ_M14:

MFQ_M14 MFN/MFK - Master file notification - site defined (S8.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFQ_M14.MFQ_M14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFR_M01:

MFR_M01 MFN/MFK - Master file not otherwise specified (for backward compatibility only) (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFR_M01.MFR_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_QUERY``
     - List[:ref:`MFR_M01_MF_QUERY <hl7-v2_5_1-MFR_M01_MF_QUERY>`]
     - required
     - MF_QUERY
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFR_M04:

MFR_M04 MFN/MFK - Master files charge description (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFR_M04.MFR_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_QUERY``
     - List[:ref:`MFR_M04_MF_QUERY <hl7-v2_5_1-MFR_M04_MF_QUERY>`]
     - required
     - MF_QUERY
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFR_M05:

MFR_M05 MFN/MFK - Patient location master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFR_M05.MFR_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_QUERY``
     - List[:ref:`MFR_M05_MF_QUERY <hl7-v2_5_1-MFR_M05_MF_QUERY>`]
     - required
     - MF_QUERY
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFR_M06:

MFR_M06 MFN/MFK - Clinical study with phases and schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFR_M06.MFR_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_QUERY``
     - List[:ref:`MFR_M06_MF_QUERY <hl7-v2_5_1-MFR_M06_MF_QUERY>`]
     - required
     - MF_QUERY
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-MFR_M07:

MFR_M07 MFN/MFK - Clinical study without phases but with schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.MFR_M07.MFR_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``MFI``
     - :ref:`MFI <hl7-v2_5_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_QUERY``
     - List[:ref:`MFR_M07_MF_QUERY <hl7-v2_5_1-MFR_M07_MF_QUERY>`]
     - required
     - MF_QUERY
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-NMD_N02:

NMD_N02 NMD/ACK - Application management data message (unsolicited) (S14.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.NMD_N02.NMD_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - List[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_5_1-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_5_1-NMQ_N01:

NMQ_N01 NMQ/NMR - Application management query message (S14.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.NMQ_N01.NMQ_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRY_WITH_DETAIL``
     - Optional[:ref:`NMQ_N01_QRY_WITH_DETAIL <hl7-v2_5_1-NMQ_N01_QRY_WITH_DETAIL>`]
     - optional
     - QRY_WITH_DETAIL
   * - ``CLOCK_AND_STATISTICS``
     - List[:ref:`NMQ_N01_CLOCK_AND_STATISTICS <hl7-v2_5_1-NMQ_N01_CLOCK_AND_STATISTICS>`]
     - required
     - CLOCK_AND_STATISTICS

.. _hl7-v2_5_1-NMR_N01:

NMR_N01 NMQ/NMR - Application management query message (S14.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.NMR_N01.NMR_N01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QRD``
     - Optional[:ref:`QRD <hl7-v2_5_1-QRD>`]
     - optional
     - Original-Style Query Definition
   * - ``CLOCK_AND_STATS_WITH_NOTES_ALT``
     - List[:ref:`NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT <hl7-v2_5_1-NMR_N01_CLOCK_AND_STATS_WITH_NOTES_ALT>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES_ALT

.. _hl7-v2_5_1-OMB_O27:

OMB_O27 OMB - Blood product order (S4.20.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMB_O27.OMB_O27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMB_O27_PATIENT <hl7-v2_5_1-OMB_O27_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMB_O27_ORDER <hl7-v2_5_1-OMB_O27_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OMD_O03:

OMD_O03 OMD - Diet order (S4.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMD_O03.OMD_O03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMD_O03_PATIENT <hl7-v2_5_1-OMD_O03_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_DIET``
     - List[:ref:`OMD_O03_ORDER_DIET <hl7-v2_5_1-OMD_O03_ORDER_DIET>`]
     - required
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - Optional[List[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_5_1-OMD_O03_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY

.. _hl7-v2_5_1-OMG_O19:

OMG_O19 OMG - General clinical order (S4.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMG_O19.OMG_O19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMG_O19_PATIENT <hl7-v2_5_1-OMG_O19_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMG_O19_ORDER <hl7-v2_5_1-OMG_O19_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OMI_O23:

OMI_O23 OMI - Imaging order (S4.4.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMI_O23.OMI_O23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMI_O23_PATIENT <hl7-v2_5_1-OMI_O23_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMI_O23_ORDER <hl7-v2_5_1-OMI_O23_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OML_O21:

OML_O21 OML - Laboratory order (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OML_O21.OML_O21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O21_PATIENT <hl7-v2_5_1-OML_O21_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OML_O21_ORDER <hl7-v2_5_1-OML_O21_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OML_O33:

OML_O33 OML - Laboratory order for multiple orders related to a single specimen (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OML_O33.OML_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O33_PATIENT <hl7-v2_5_1-OML_O33_PATIENT>`]
     - optional
     - PATIENT
   * - ``SPECIMEN``
     - List[:ref:`OML_O33_SPECIMEN <hl7-v2_5_1-OML_O33_SPECIMEN>`]
     - required
     - SPECIMEN

.. _hl7-v2_5_1-OML_O35:

OML_O35 OML - Laboratory order for multiple orders related to a single container of a sp (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OML_O35.OML_O35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O35_PATIENT <hl7-v2_5_1-OML_O35_PATIENT>`]
     - optional
     - PATIENT
   * - ``SPECIMEN``
     - List[:ref:`OML_O35_SPECIMEN <hl7-v2_5_1-OML_O35_SPECIMEN>`]
     - required
     - SPECIMEN

.. _hl7-v2_5_1-OMN_O07:

OMN_O07 OMN - Non-stock requisition order (S4.10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMN_O07.OMN_O07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMN_O07_PATIENT <hl7-v2_5_1-OMN_O07_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMN_O07_ORDER <hl7-v2_5_1-OMN_O07_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OMP_O09:

OMP_O09 OMP - Pharmacy/treatment order (S4.13.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMP_O09.OMP_O09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMP_O09_PATIENT <hl7-v2_5_1-OMP_O09_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMP_O09_ORDER <hl7-v2_5_1-OMP_O09_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-OMS_O05:

OMS_O05 OMS - Stock requisition order (S4.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OMS_O05.OMS_O05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMS_O05_PATIENT <hl7-v2_5_1-OMS_O05_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMS_O05_ORDER <hl7-v2_5_1-OMS_O05_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-ORB_O28:

ORB_O28 ORB - Blood product order acknowledgment (S4.20.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORB_O28.ORB_O28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORB_O28_RESPONSE <hl7-v2_5_1-ORB_O28_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORD_O04:

ORD_O04 ORD - Diet order acknowledgment (S4.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORD_O04.ORD_O04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORD_O04_RESPONSE <hl7-v2_5_1-ORD_O04_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORF_R04:

ORF_R04 ORF - Response to query; transmission of requested observation (S7.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORF_R04.ORF_R04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP``
     - List[:ref:`ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP <hl7-v2_5_1-ORF_R04_PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP>`]
     - required
     - PIDNTEORCOBRNTETQ1TQ2CTDOBXNTECTI_SUPPGRP
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-ORG_O20:

ORG_O20 ORG/ORL - General clinical order response (S4.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORG_O20.ORG_O20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORG_O20_RESPONSE <hl7-v2_5_1-ORG_O20_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORI_O24:

ORI_O24 ORI - Imaging order response message to any OMI (S4.4.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORI_O24.ORI_O24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORI_O24_RESPONSE <hl7-v2_5_1-ORI_O24_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORL_O22:

ORL_O22 ORL - General laboratory order response message to any OML (S4.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORL_O22.ORL_O22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O22_RESPONSE <hl7-v2_5_1-ORL_O22_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORL_O34:

ORL_O34 ORL - Laboratory order response message to a multiple order related to single sp (S4.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORL_O34.ORL_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O34_RESPONSE <hl7-v2_5_1-ORL_O34_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORL_O36:

ORL_O36 ORL - Laboratory order response message to a single container of a specimen OML (S4.4.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORL_O36.ORL_O36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O36_RESPONSE <hl7-v2_5_1-ORL_O36_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORM_O01:

ORM_O01 ORM - Order message (also RDE, RDS, RGV, RAS) (S4.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORM_O01.ORM_O01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`ORM_O01_PATIENT <hl7-v2_5_1-ORM_O01_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`ORM_O01_ORDER <hl7-v2_5_1-ORM_O01_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-ORN_O08:

ORN_O08 ORN - Non-stock requisition acknowledgment (S4.10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORN_O08.ORN_O08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORN_O08_RESPONSE <hl7-v2_5_1-ORN_O08_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORP_O10:

ORP_O10 ORP - Pharmacy/treatment order acknowledgment (S4.13.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORP_O10.ORP_O10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORP_O10_RESPONSE <hl7-v2_5_1-ORP_O10_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORR_O02:

ORR_O02 ORR - Order response (also RRE, RRD, RRG, RRA) (S4.4.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORR_O02.ORR_O02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORR_O02_RESPONSE <hl7-v2_5_1-ORR_O02_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORS_O06:

ORS_O06 ORS - Stock requisition acknowledgment (S4.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORS_O06.ORS_O06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORS_O06_RESPONSE <hl7-v2_5_1-ORS_O06_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-ORU_R01:

ORU_R01 ORU/ACK - Unsolicited transmission of an observation message (S5.7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_5_1-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-ORU_R30:

ORU_R30 ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Pla (S5.7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORU_R30.ORU_R30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_5_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_5_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_5_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_5_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_5_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_5_1-ORU_R31:

ORU_R31 ORU - Unsolicited New Point-Of-Care Observation Message - Search For An Order (S7.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORU_R31.ORU_R31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_5_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_5_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_5_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_5_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_5_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_5_1-ORU_R32:

ORU_R32 ORU - Unsolicited Pre-Ordered Point-Of-Care Observation (S7.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ORU_R32.ORU_R32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_5_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_5_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_5_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_5_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_5_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_5_1-OSQ_Q06:

OSQ_Q06 OSQ/OSR - Query for order status (S4.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OSQ_Q06.OSQ_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-OSR_Q06:

OSR_Q06 OSQ/OSR - Query for order status (S4.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OSR_Q06.OSR_Q06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``RESPONSE``
     - Optional[:ref:`OSR_Q06_RESPONSE <hl7-v2_5_1-OSR_Q06_RESPONSE>`]
     - optional
     - RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-OUL_R21:

OUL_R21 OUL - Unsolicited laboratory observation (S7.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OUL_R21.OUL_R21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_5_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OUL_R21_PATIENT <hl7-v2_5_1-OUL_R21_PATIENT>`]
     - optional
     - PATIENT
   * - ``VISIT``
     - Optional[:ref:`OUL_R21_VISIT <hl7-v2_5_1-OUL_R21_VISIT>`]
     - optional
     - VISIT
   * - ``ORDER_OBSERVATION``
     - List[:ref:`OUL_R21_ORDER_OBSERVATION <hl7-v2_5_1-OUL_R21_ORDER_OBSERVATION>`]
     - required
     - ORDER_OBSERVATION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-OUL_R22:

OUL_R22 OUL - Unsolicited Specimen Oriented Observation Message (S7.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OUL_R22.OUL_R22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_5_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OUL_R22_PATIENT <hl7-v2_5_1-OUL_R22_PATIENT>`]
     - optional
     - PATIENT
   * - ``VISIT``
     - Optional[:ref:`OUL_R22_VISIT <hl7-v2_5_1-OUL_R22_VISIT>`]
     - optional
     - VISIT
   * - ``SPECIMEN``
     - List[:ref:`OUL_R22_SPECIMEN <hl7-v2_5_1-OUL_R22_SPECIMEN>`]
     - required
     - SPECIMEN
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-OUL_R23:

OUL_R23 OUL - Unsolicited Specimen Container Oriented Observation Message (S7.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OUL_R23.OUL_R23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_5_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PIDPD1NTE_SUPPGRP``
     - Optional[:ref:`OUL_R23_PIDPD1NTE_SUPPGRP <hl7-v2_5_1-OUL_R23_PIDPD1NTE_SUPPGRP>`]
     - optional
     - PIDPD1NTE_SUPPGRP
   * - ``PV1PV2_SUPPGRP``
     - Optional[:ref:`OUL_R23_PV1PV2_SUPPGRP <hl7-v2_5_1-OUL_R23_PV1PV2_SUPPGRP>`]
     - optional
     - PV1PV2_SUPPGRP
   * - ``SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP``
     - List[:ref:`OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP <hl7-v2_5_1-OUL_R23_SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP>`]
     - required
     - SPMOBXSACINVOBRORCNTETQ1TQ2OBXTCDSIDNTECTI_SUPPGRP
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-OUL_R24:

OUL_R24 OUL - Unsolicited Order Oriented Observation Message (S7.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.OUL_R24.OUL_R24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_5_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PIDPD1NTE_SUPPGRP``
     - Optional[:ref:`OUL_R24_PIDPD1NTE_SUPPGRP <hl7-v2_5_1-OUL_R24_PIDPD1NTE_SUPPGRP>`]
     - optional
     - PIDPD1NTE_SUPPGRP
   * - ``PV1PV2_SUPPGRP``
     - Optional[:ref:`OUL_R24_PV1PV2_SUPPGRP <hl7-v2_5_1-OUL_R24_PV1PV2_SUPPGRP>`]
     - optional
     - PV1PV2_SUPPGRP
   * - ``ORDER``
     - List[:ref:`OUL_R24_ORDER <hl7-v2_5_1-OUL_R24_ORDER>`]
     - required
     - ORDER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-PEX_P07:

PEX_P07 PEX - Unsolicited initial individual product experience report (S7.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_5_1-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_5_1-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_5_1-PEX_P08:

PEX_P08 PEX - Unsolicited update individual product experience report (S7.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_5_1-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_5_1-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_5_1-PGL_PC6:

PGL_PC6 PGL - PC/ goal add (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_5_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_5_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_5_1-PGL_PC7:

PGL_PC7 PGL - PC/ goal update (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_5_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_5_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_5_1-PGL_PC8:

PGL_PC8 PGL - PC/ goal delete (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_5_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_5_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_5_1-PMU_B01:

PMU_B01 PMU/ACK - Add personnel record (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B01.PMU_B01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_5_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_5_1-ORG>`]]
     - optional
     - Practitioner Organization Unit
   * - ``AFF``
     - Optional[List[:ref:`AFF <hl7-v2_5_1-AFF>`]]
     - optional
     - Professional Affiliation
   * - ``LAN``
     - Optional[List[:ref:`LAN <hl7-v2_5_1-LAN>`]]
     - optional
     - Language Detail
   * - ``EDU``
     - Optional[List[:ref:`EDU <hl7-v2_5_1-EDU>`]]
     - optional
     - Educational Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_5_1-CER>`]]
     - optional
     - Certificate Detail

.. _hl7-v2_5_1-PMU_B02:

PMU_B02 PMU/ACK - Update personnel record (S15.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B02.PMU_B02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_5_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_5_1-ORG>`]]
     - optional
     - Practitioner Organization Unit
   * - ``AFF``
     - Optional[List[:ref:`AFF <hl7-v2_5_1-AFF>`]]
     - optional
     - Professional Affiliation
   * - ``LAN``
     - Optional[List[:ref:`LAN <hl7-v2_5_1-LAN>`]]
     - optional
     - Language Detail
   * - ``EDU``
     - Optional[List[:ref:`EDU <hl7-v2_5_1-EDU>`]]
     - optional
     - Educational Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_5_1-CER>`]]
     - optional
     - Certificate Detail

.. _hl7-v2_5_1-PMU_B03:

PMU_B03 PMU/ACK - Delete personnel re cord (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B03.PMU_B03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification

.. _hl7-v2_5_1-PMU_B04:

PMU_B04 PMU/ACK - Active practicing person (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B04.PMU_B04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_5_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_5_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_5_1-PMU_B05:

PMU_B05 PMU/ACK - Deactivate practicing person (S15.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B05.PMU_B05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_5_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_5_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_5_1-PMU_B06:

PMU_B06 PMU/ACK - Terminate practicing person (S15.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B06.PMU_B06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_5_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_5_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_5_1-PMU_B07:

PMU_B07 PMU/ACK - Grant Certificate/Permission (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B07.PMU_B07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_5_1-PRA>`]
     - optional
     - Practitioner Detail
   * - ``CERTIFICATE``
     - Optional[List[:ref:`PMU_B07_CERTIFICATE <hl7-v2_5_1-PMU_B07_CERTIFICATE>`]]
     - optional
     - CERTIFICATE

.. _hl7-v2_5_1-PMU_B08:

PMU_B08 PMU/ACK - Revoke Certificate/Permission (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PMU_B08.PMU_B08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_5_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_5_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_5_1-PRA>`]
     - optional
     - Practitioner Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_5_1-CER>`]]
     - optional
     - Certificate Detail

.. _hl7-v2_5_1-PPG_PCG:

PPG_PCG PPG - PC/ pathway (goal-oriented) add (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_5_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_5_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPG_PCH:

PPG_PCH PPG - PC/ pathway (goal-oriented) update (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_5_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_5_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPG_PCJ:

PPG_PCJ PPG - PC/ pathway (goal-oriented) delete (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_5_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_5_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPP_PCB:

PPP_PCB PPP - PC/ pathway (problem-oriented) add (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_5_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_5_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPP_PCC:

PPP_PCC PPP - PC/ pathway (problem-oriented) update (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_5_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_5_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPP_PCD:

PPP_PCD PPP - PC/ pathway (problem-oriented) delete (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_5_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_5_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_5_1-PPR_PC1:

PPR_PC1 PPR - PC/ problem add (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_5_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_5_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_5_1-PPR_PC2:

PPR_PC2 PPR - PC/ problem update (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_5_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_5_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_5_1-PPR_PC3:

PPR_PC3 PPR - PC/ problem delete (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_5_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_5_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_5_1-PPT_PCL:

PPT_PCL PPT - PC/ pathway (goal-oriented) query response (S12.3.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPT_PCL.PPT_PCL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``PATIENT``
     - List[:ref:`PPT_PCL_PATIENT <hl7-v2_5_1-PPT_PCL_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-PPV_PCA:

PPV_PCA PPV - PC/ goal response (S12.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PPV_PCA.PPV_PCA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``PATIENT``
     - List[:ref:`PPV_PCA_PATIENT <hl7-v2_5_1-PPV_PCA_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-PRR_PC5:

PRR_PC5 PRR - PC/ problem response (S12.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PRR_PC5.PRR_PC5
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``PATIENT``
     - List[:ref:`PRR_PC5_PATIENT <hl7-v2_5_1-PRR_PC5_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-PTR_PCF:

PTR_PCF PTR - PC/ pathway (problem-oriented) query response (S12.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.PTR_PCF.PTR_PCF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``PATIENT``
     - List[:ref:`PTR_PCF_PATIENT <hl7-v2_5_1-PTR_PCF_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_5_1-QBP_Q11:

QBP_Q11 QBP - Query by parameter requesting an RSP segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q11.QBP_Q11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q13:

QBP_Q13 QBP - Query by parameter requesting an  RTB - tabular response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q13.QBP_Q13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q15:

QBP_Q15 QBP - Query by parameter requesting an RDY display response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q15.QBP_Q15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q21:

QBP_Q21 QBP - Get person demographics (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q21.QBP_Q21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q22:

QBP_Q22 QBP - Find candidates (S3.3.57).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q22.QBP_Q22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q23:

QBP_Q23 QBP - Get corresponding identifiers (S3.3.58).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q23.QBP_Q23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q24:

QBP_Q24 QBP - Allocate identifiers (S3.3.59).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q24.QBP_Q24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q25:

QBP_Q25 QBP - Personnel Information by Segment Query (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q25.QBP_Q25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Q31:

QBP_Q31 DBP - Dispense History (S4.13.20).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Q31.QBP_Q31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Qnn:

QBP_Qnn HL7 v2 QBP_Qnn message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Qnn.QBP_Qnn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z73:

QBP_Z73 Information about Phone Calls (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z73.QBP_Z73
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_5_1-QBP_Z75:

QBP_Z75 Tabular Patient List (S5.9.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z75.QBP_Z75
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z77:

QBP_Z77 Tabular Patient List (S5.9.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z77.QBP_Z77
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z79:

QBP_Z79 Dispense Information (S5.9.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z79.QBP_Z79
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z81:

QBP_Z81 Dispense History (S5.9.1.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z81.QBP_Z81
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z85:

QBP_Z85 Pharmacy Information Comprehensive (S5.9.1.2.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z85.QBP_Z85
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z87:

QBP_Z87 Dispense Information (S5.9.2.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z87.QBP_Z87
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z89:

QBP_Z89 Lab Results History (S5.9.2.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z89.QBP_Z89
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z91:

QBP_Z91 Who Am I (S5.9.3.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z91.QBP_Z91
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z93:

QBP_Z93 Tabular Dispense History (S5.9.3.2.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z93.QBP_Z93
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z95:

QBP_Z95 Tabular Dispense History (S5.9.4.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z95.QBP_Z95
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z97:

QBP_Z97 Dispense History (S5.9.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z97.QBP_Z97
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QBP_Z99:

QBP_Z99 Who Am I (S5.3.1.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QBP_Z99.QBP_Z99
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QCK_Q02:

QCK_Q02 HL7 v2 QCK_Q02 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QCK_Q02.QCK_Q02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - Optional[:ref:`QAK <hl7-v2_5_1-QAK>`]
     - optional
     - Query Acknowledgment

.. _hl7-v2_5_1-QCN_J01:

QCN_J01 QCN/ACK - Cancel query/acknowledge message (S5.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QCN_J01.QCN_J01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QID``
     - :ref:`QID <hl7-v2_5_1-QID>`
     - required
     - Query Identification

.. _hl7-v2_5_1-QCN_J02:

QCN_J02 QSX/ACK - Cancel subscription/acknowledge message (S5.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QCN_J02.QCN_J02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QID``
     - :ref:`QID <hl7-v2_5_1-QID>`
     - required
     - Query Identification

.. _hl7-v2_5_1-QRY:

QRY HL7 v2 QRY message.
~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY.QRY
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_A19:

QRY_A19 QRY/ADR -  Patient query (S12.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_A19.QRY_A19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_PC4:

QRY_PC4 QRY - PC/ problem query (S12.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_PC4.QRY_PC4
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_PC9:

QRY_PC9 QRY - PC/ goal query (S12.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_PC9.QRY_PC9
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_PCE:

QRY_PCE QRY - PC/ pathway (problem-oriented) query (S12.3.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_PCE.QRY_PCE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_PCK:

QRY_PCK QRY - PC/ pathway (goal-oriented) query (S12.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_PCK.QRY_PCK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-QRY_Q01:

QRY_Q01 QRY/DSR - Query sent for immediate response (S12.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q01.QRY_Q01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_Q26:

QRY_Q26 ROR - Pharmacy/treatment order response (S4.13.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q26.QRY_Q26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_Q27:

QRY_Q27 RAR - Pharmacy/treatment administration information (S4.13.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q27.QRY_Q27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_Q28:

QRY_Q28 RDR - Pharmacy/treatment dispense information (S4.13.17).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q28.QRY_Q28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_Q29:

QRY_Q29 RER - Pharmacy/treatment encoded order information (S4.13.18).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q29.QRY_Q29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_Q30:

QRY_Q30 RGR - Pharmacy/treatment dose information (S4.13.19).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_Q30.QRY_Q30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QRY_R02:

QRY_R02 QRY - Query for results of observation (S12.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QRY_R02.QRY_R02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - :ref:`QRF <hl7-v2_5_1-QRF>`
     - required
     - Original style query filter

.. _hl7-v2_5_1-QSB_Q16:

QSB_Q16 QSB - Create subscription (S5.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QSB_Q16.QSB_Q16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QSB_Z83:

QSB_Z83 ORU Subscription (S5.7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QSB_Z83.QSB_Z83
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-QVR_Q17:

QVR_Q17 QVR - Query for previous events (S5.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.QVR_Q17.QVR_Q17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QVR_Q17_QBP <hl7-v2_5_1-QVR_Q17_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RAR_RAR:

RAR_RAR Pharmacy/Treatment Administration Information (S4.13.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RAR_RAR.RAR_RAR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``DEFINITION``
     - List[:ref:`RAR_RAR_DEFINITION <hl7-v2_5_1-RAR_RAR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RAS_O17:

RAS_O17 RAS - Pharmacy/treatment administration (S4.13.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RAS_O17.RAS_O17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RAS_O17_PATIENT <hl7-v2_5_1-RAS_O17_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RAS_O17_ORDER <hl7-v2_5_1-RAS_O17_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-RCI_I05:

RCI_I05 RQC/RCI - Request for patient clinical information (S11.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RCI_I05.RCI_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PROVIDER``
     - List[:ref:`RCI_I05_PROVIDER <hl7-v2_5_1-RCI_I05_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``OBSERVATION``
     - Optional[List[:ref:`RCI_I05_OBSERVATION <hl7-v2_5_1-RCI_I05_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RCL_I06:

RCL_I06 RQC/RCL - Request/receipt of clinical data listing (S11.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RCL_I06.RCL_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PROVIDER``
     - List[:ref:`RCL_I06_PROVIDER <hl7-v2_5_1-RCL_I06_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_5_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RDE_O11:

RDE_O11 RDE - Pharmacy/treatment encoded order (S4.13.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDE_O11.RDE_O11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_5_1-RDE_O11_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDE_O11_ORDER <hl7-v2_5_1-RDE_O11_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-RDE_O25:

RDE_O25 RDE - Pharmacy/treatment refill authorization request (S4.13.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDE_O25.RDE_O25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_5_1-RDE_O11_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDE_O11_ORDER <hl7-v2_5_1-RDE_O11_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-RDR_RDR:

RDR_RDR Pharmacy/treatment Dispense Information (S4.13.17).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``DEFINITION``
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_5_1-RDR_RDR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RDS_O13:

RDS_O13 RDS - Pharmacy/treatment dispense (S4.13.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDS_O13.RDS_O13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDS_O13_PATIENT <hl7-v2_5_1-RDS_O13_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDS_O13_ORDER <hl7-v2_5_1-RDS_O13_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-RDY_K15:

RDY_K15 RDY - Display response in response to QBP^Q15 (S5.3.2.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDY_K15.RDY_K15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_5_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RDY_Z98:

RDY_Z98 Dispense History (Response) (S5.9.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RDY_Z98.RDY_Z98
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_5_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-REF_I12:

REF_I12 REF/RRI - Patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_5_1-REF_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_5_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_5_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_5_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_5_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_5_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-REF_I13:

REF_I13 REF/RRI - Modify patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_5_1-REF_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_5_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_5_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_5_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_5_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_5_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-REF_I14:

REF_I14 REF/RRI - Cancel patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_5_1-REF_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_5_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_5_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_5_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_5_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_5_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-REF_I15:

REF_I15 REF/RRI - Request patient referral status (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT <hl7-v2_5_1-REF_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_5_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_5_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_5_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_5_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_5_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RER_RER:

RER_RER Pharmacy/Treatment Encoded Order Information (S4.13.18).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RER_RER.RER_RER
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``DEFINITION``
     - List[:ref:`RER_RER_DEFINITION <hl7-v2_5_1-RER_RER_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RGR_RGR:

RGR_RGR Pharmacy/Treatment Dose Information (S4.13.19).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RGR_RGR.RGR_RGR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``DEFINITION``
     - List[:ref:`RGR_RGR_DEFINITION <hl7-v2_5_1-RGR_RGR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RGV_O15:

RGV_O15 RGV - Pharmacy/treatment give (S4.13.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RGV_O15.RGV_O15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RGV_O15_PATIENT <hl7-v2_5_1-RGV_O15_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RGV_O15_ORDER <hl7-v2_5_1-RGV_O15_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_5_1-ROR_ROR:

ROR_ROR ROR - Pharmacy prescription order query response (S4.13.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.ROR_ROR.ROR_ROR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``DEFINITION``
     - List[:ref:`ROR_ROR_DEFINITION <hl7-v2_5_1-ROR_ROR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RPA_I08:

RPA_I08 RQA/RPA - Request for treatment authorization information (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RPA_I08_AUTHORIZATION <hl7-v2_5_1-RPA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_5_1-RPA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_5_1-RPA_I08_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_5_1-RPA_I08_PROCEDURE>`]
     - required
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_5_1-RPA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_5_1-RPA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RPI_I01:

RPI_I01 RQI/RPI - Request for insurance information (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_5_1-RPI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_5_1-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RPI_I04:

RPI_I04 RQD/RPI - Request for patient demographic data (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RPI_I04.RPI_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPI_I04_PROVIDER <hl7-v2_5_1-RPI_I04_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_5_1-RPI_I04_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RPL_I02:

RPL_I02 RQI/RPL - Request/receipt of patient selection display list (S11.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_5_1-RPL_I02_PROVIDER>`]
     - required
     - PROVIDER
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_5_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RPR_I03:

RPR_I03 RQI/RPR - Request/receipt of patient selection list (S11.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RPR_I03.RPR_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPR_I03_PROVIDER <hl7-v2_5_1-RPR_I03_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - Optional[List[:ref:`PID <hl7-v2_5_1-PID>`]]
     - optional
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQA_I08:

RQA_I08 RQA/RPA - Request for treatment authorization information (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_5_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_5_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_5_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_5_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_5_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_5_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQA_I09:

RQA_I09 RQA/RPA - Request for modification to an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_5_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_5_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_5_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_5_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_5_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_5_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQA_I10:

RQA_I10 RQA/RPA - Request for resubmission of an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_5_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_5_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_5_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_5_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_5_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_5_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQA_I11:

RQA_I11 RQA/RPA - Request for cancellation of an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_5_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_5_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_5_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_5_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_5_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_5_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQC_I05:

RQC_I05 RQC/RCI - Request for patient clinical information (S11.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQC_I05.RQC_I05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PROVIDER``
     - List[:ref:`RQC_I05_PROVIDER <hl7-v2_5_1-RQC_I05_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQC_I06:

RQC_I06 RQC/RCL - Request/receipt of clinical data listing (S11.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQC_I06.RQC_I06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PROVIDER``
     - List[:ref:`RQC_I05_PROVIDER <hl7-v2_5_1-RQC_I05_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQI_I01:

RQI_I01 RQI/RPI - Request for insurance information (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_5_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_5_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQI_I02:

RQI_I02 RQI/RPL - Request/receipt of patient selection display list (S11.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_5_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_5_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQI_I03:

RQI_I03 RQI/RPR - Request/receipt of patient selection list (S11.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_5_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_5_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQI_I07:

RQI_I07 PIN/ACK - Unsolicited insurance information (S11.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQI_I07.RQI_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_5_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_5_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQP_I04:

RQP_I04 RQD/RPI - Request for patient demographic data (S11.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PROVIDER``
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_5_1-RQP_I04_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RQQ_Q09:

RQQ_Q09 HL7 v2 RQQ_Q09 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RQQ_Q09.RQQ_Q09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``ERQ``
     - :ref:`ERQ <hl7-v2_5_1-ERQ>`
     - required
     - Event replay query
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RRA_O18:

RRA_O18 RRA - Pharmacy/treatment administration acknowledgment (S4.13.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRA_O18.RRA_O18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRA_O18_RESPONSE <hl7-v2_5_1-RRA_O18_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-RRD_O14:

RRD_O14 RRD - Pharmacy/treatment dispense acknowledgment (S4.13.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRD_O14.RRD_O14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRD_O14_RESPONSE <hl7-v2_5_1-RRD_O14_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-RRE_O12:

RRE_O12 RRE - Pharmacy/treatment encoded order acknowledgment (S4.13.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRE_O12.RRE_O12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_5_1-RRE_O12_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-RRE_O26:

RRE_O26 RRE - Pharmacy/Treatment Refill Authorization Acknowledgement (S4.13.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRE_O26.RRE_O26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_5_1-RRE_O12_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-RRG_O16:

RRG_O16 RRG - Pharmacy/treatment give acknowledgment (S4.13.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRG_O16.RRG_O16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRG_O16_RESPONSE <hl7-v2_5_1-RRG_O16_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_5_1-RRI_I12:

RRI_I12 REF/RRI - Patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_5_1-MSA>`]
     - optional
     - Message Acknowledgment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_5_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT``
     - Optional[:ref:`RRI_I12_AUTHORIZATION_CONTACT <hl7-v2_5_1-RRI_I12_AUTHORIZATION_CONTACT>`]
     - optional
     - AUTHORIZATION_CONTACT
   * - ``PROVIDER_CONTACT``
     - List[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_5_1-RRI_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_5_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_5_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_5_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_5_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_5_1-RRI_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RRI_I12_OBSERVATION <hl7-v2_5_1-RRI_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RRI_I12_PATIENT_VISIT <hl7-v2_5_1-RRI_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_5_1-RSP_K11:

RSP_K11 RSP - Segment pattern response in response to QBP^Q11 (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K11.RSP_K11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RSP_K11_ROW_DEFINITION <hl7-v2_5_1-RSP_K11_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K21:

RSP_K21 RSP - Get person demographics response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K21.RSP_K21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_5_1-RSP_K21_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K22:

RSP_K22 RSP - Find candidates response (S3.3.57).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K22.RSP_K22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_5_1-RSP_K21_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K23:

RSP_K23 RSP - Get corresponding identifiers response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K23.RSP_K23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_5_1-RSP_K23_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K24:

RSP_K24 RSP - Allocate identifiers response (S3.3.59).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K24.RSP_K24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_5_1-RSP_K23_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K25:

RSP_K25 RSP - Personnel Information by Segment Response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K25.RSP_K25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``STAFF``
     - List[:ref:`RSP_K25_STAFF <hl7-v2_5_1-RSP_K25_STAFF>`]
     - required
     - STAFF
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_K31:

RSP_K31 RSP - Dispense History (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_K31.RSP_K31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``RESPONSE``
     - List[:ref:`RSP_K31_RESPONSE <hl7-v2_5_1-RSP_K31_RESPONSE>`]
     - required
     - RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Q11:

RSP_Q11 QBP - Query by parameter requesting an RSP segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Q11.RSP_Q11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESULT_CLUSTER``
     - Optional[:ref:`RSP_Q11_QUERY_RESULT_CLUSTER <hl7-v2_5_1-RSP_Q11_QUERY_RESULT_CLUSTER>`]
     - optional
     - QUERY_RESULT_CLUSTER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z80:

RSP_Z80 Dispense Information (Response) (S5.9.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z80.RSP_Z80
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RSP_K11_ROW_DEFINITION <hl7-v2_5_1-RSP_K11_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z82:

RSP_Z82 Dispense History (Response) (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z82.RSP_Z82
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_5_1-RSP_Z82_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z84:

RSP_Z84 Who Am I (Response) (S5.3.1.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z84.RSP_Z84
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RSP_K11_ROW_DEFINITION <hl7-v2_5_1-RSP_K11_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z86:

RSP_Z86 Pharmacy Information Comprehensive (Response) (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z86.RSP_Z86
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_5_1-RSP_Z86_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z88:

RSP_Z88 Dispense Information (Response) (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z88.RSP_Z88
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_5_1-RSP_Z88_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_5_1-DSC>`
     - required
     - Continuation Pointer

.. _hl7-v2_5_1-RSP_Z90:

RSP_Z90 Lab Results History (Response) (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RSP_Z90.RSP_Z90
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_5_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_5_1-RSP_Z90_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_5_1-DSC>`
     - required
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_K13:

RTB_K13 RTB - Tabular response in response to QBP^Q13 (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_K13.RTB_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Knn:

RTB_Knn HL7 v2 RTB_Knn message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Knn.RTB_Knn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z74:

RTB_Z74 Information about Phone Calls (Response) (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z74.RTB_Z74
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_5_1-RTB_Z74_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z76:

RTB_Z76 Tabular Patient List (Response) (S5.9.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z76.RTB_Z76
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z78:

RTB_Z78 Tabular Patient List (Response) (S5.9.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z78.RTB_Z78
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z92:

RTB_Z92 Who Am I (Response) (S5.9.3.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z92.RTB_Z92
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z94:

RTB_Z94 Tabular Dispense History (Response) (S5.9.3.2.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z94.RTB_Z94
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-RTB_Z96:

RTB_Z96 Tabular Dispense History (Response) (S5.9.4.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.RTB_Z96.RTB_Z96
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_5_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_5_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-SIU_S12:

SIU_S12 SIU/ACK - Notification of new appointment booking (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S13:

SIU_S13 SIU/ACK - Notification of appointment rescheduling (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S14:

SIU_S14 SIU/ACK - Notification of appointment modification (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S15:

SIU_S15 SIU/ACK - Notification of appointment cancellation (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S16:

SIU_S16 SIU/ACK - Notification of appointment discontinuation (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S17:

SIU_S17 SIU/ACK - Notification of appointment deletion (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S18:

SIU_S18 SIU/ACK - Notification of addition of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S19:

SIU_S19 SIU/ACK - Notification of modification of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S20:

SIU_S20 SIU/ACK - Notification of cancellation of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S21:

SIU_S21 SIU/ACK - Notification of discontinuation of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S22:

SIU_S22 SIU/ACK - Notification of deletion of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S23:

SIU_S23 SIU/ACK - Notification of blocked schedule time slot(s) (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S24:

SIU_S24 Alias for SIU_S12.
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SIU_S26:

SIU_S26 SIU/ACK Notification that patient did not show up for schedule appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_5_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_5_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_5_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_5_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SPQ_Q08:

SPQ_Q08 HL7 v2 SPQ_Q08 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SPQ_Q08.SPQ_Q08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``SPR``
     - :ref:`SPR <hl7-v2_5_1-SPR>`
     - required
     - Stored Procedure Request Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-SQM_S25:

SQM_S25 SQM/SQR - Schedule query message and response (S10.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SQM_S25.SQM_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``REQUEST``
     - Optional[:ref:`SQM_S25_REQUEST <hl7-v2_5_1-SQM_S25_REQUEST>`]
     - optional
     - REQUEST
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-SQR_S25:

SQR_S25 SQM/SQR - Schedule query message and response (S10.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SQR_S25.SQR_S25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``SCHEDULE``
     - Optional[List[:ref:`SQR_S25_SCHEDULE <hl7-v2_5_1-SQR_S25_SCHEDULE>`]]
     - optional
     - SCHEDULE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-SRM_S01:

SRM_S01 SRM/SRR - Request new appointment booking (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S02:

SRM_S02 SRM/SRR - Request appointment rescheduling (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S03:

SRM_S03 SRM/SRR - Request appointment modification (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S04:

SRM_S04 SRM/SRR - Request appointment cancellation (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S05:

SRM_S05 SRM/SRR - Request appointment discontinuation (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S06:

SRM_S06 SRM/SRR - Request appointment deletion (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S07:

SRM_S07 SRM/SRR - Request addition of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S08:

SRM_S08 SRM/SRR - Request modification of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S09:

SRM_S09 SRM/SRR - Request cancellation of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S10:

SRM_S10 SRM/SRR - Request discontinuation of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRM_S11:

SRM_S11 SRM/SRR - Request deletion of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_5_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_5_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_5_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_5_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_5_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_5_1-SRR_S01:

SRR_S01 SRM/SRR - Request new appointment booking (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_5_1-ERR>`]]
     - optional
     - Error
   * - ``SCHEDULE``
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_5_1-SRR_S01_SCHEDULE>`]
     - optional
     - SCHEDULE

.. _hl7-v2_5_1-SSR_U04:

SSR_U04 SSR/ACK - specimen status request (S13.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SSR_U04.SSR_U04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``SPECIMEN_CONTAINER``
     - List[:ref:`SSR_U04_SPECIMEN_CONTAINER <hl7-v2_5_1-SSR_U04_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-SSU_U03:

SSU_U03 SSU/ACK - Specimen status update (S13.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SSU_U03.SSU_U03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``SPECIMEN_CONTAINER``
     - List[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_5_1-SSU_U03_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-SUR_P09:

SUR_P09 SUR - Summary product experience report (S7.11.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.SUR_P09.SUR_P09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``FACPSHPDCPSHFACPDCNTEED_SUPPGRP``
     - List[:ref:`SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP <hl7-v2_5_1-SUR_P09_FACPSHPDCPSHFACPDCNTEED_SUPPGRP>`]
     - required
     - FACPSHPDCPSHFACPDCNTEED_SUPPGRP

.. _hl7-v2_5_1-TBR_R08:

TBR_R08 HL7 v2 TBR_R08 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.TBR_R08.TBR_R08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_5_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_5_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``RDF``
     - :ref:`RDF <hl7-v2_5_1-RDF>`
     - required
     - Table Row Definition
   * - ``RDT``
     - List[:ref:`RDT <hl7-v2_5_1-RDT>`]
     - required
     - Table Row Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-TCU_U10:

TCU_U10 TCU/ACK - Automated equipment test code settings update (S13.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.TCU_U10.TCU_U10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``TEST_CONFIGURATION``
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_5_1-TCU_U10_TEST_CONFIGURATION>`]
     - required
     - TEST_CONFIGURATION
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-TCU_U11:

TCU_U11 TCR/ACK - Automated equipment test code settings request (S13.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.TCU_U11.TCU_U11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_5_1-EQU>`
     - required
     - Equipment Detail
   * - ``TEST_CONFIGURATION``
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_5_1-TCU_U10_TEST_CONFIGURATION>`]
     - required
     - TEST_CONFIGURATION
   * - ``ROL``
     - Optional[:ref:`ROL <hl7-v2_5_1-ROL>`]
     - optional
     - Role

.. _hl7-v2_5_1-UDM_Q05:

UDM_Q05 HL7 v2 UDM_Q05 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``URD``
     - :ref:`URD <hl7-v2_5_1-URD>`
     - required
     - Results/update Definition
   * - ``URS``
     - Optional[:ref:`URS <hl7-v2_5_1-URS>`]
     - optional
     - Unsolicited Selection
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_5_1-DSP>`]
     - required
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-VQQ_Q07:

VQQ_Q07 HL7 v2 VQQ_Q07 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.VQQ_Q07.VQQ_Q07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``VTQ``
     - :ref:`VTQ <hl7-v2_5_1-VTQ>`
     - required
     - Virtual Table Query Request
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_5_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_5_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_5_1-VXQ_V01:

VXQ_V01 VXQ - Query for vaccination record (S4.17.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.VXQ_V01.VXQ_V01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter

.. _hl7-v2_5_1-VXR_V03:

VXR_V03 VXR - Vaccination record response (S4.17.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.VXR_V03.VXR_V03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PATIENT_VISIT``
     - Optional[:ref:`VXR_V03_PATIENT_VISIT <hl7-v2_5_1-VXR_V03_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`VXR_V03_INSURANCE <hl7-v2_5_1-VXR_V03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ORDER``
     - Optional[List[:ref:`VXR_V03_ORDER <hl7-v2_5_1-VXR_V03_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_5_1-VXU_V04:

VXU_V04 VXU - Unsolicited vaccination record update (S4.17.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_5_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_5_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_5_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PATIENT``
     - Optional[:ref:`VXU_V04_PATIENT <hl7-v2_5_1-VXU_V04_PATIENT>`]
     - optional
     - PATIENT
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_5_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_5_1-VXU_V04_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ORDER``
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_5_1-VXU_V04_ORDER>`]]
     - optional
     - ORDER

.. _hl7-v2_5_1-VXX_V02:

VXX_V02 VXX - Response to vaccination query returning multiple PID matches (S4.17.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_5_1.messages.VXX_V02.VXX_V02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_5_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_5_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_5_1-SFT>`]]
     - optional
     - Software Segment
   * - ``QRD``
     - :ref:`QRD <hl7-v2_5_1-QRD>`
     - required
     - Original-Style Query Definition
   * - ``QRF``
     - Optional[:ref:`QRF <hl7-v2_5_1-QRF>`]
     - optional
     - Original style query filter
   * - ``PATIENT``
     - List[:ref:`VXX_V02_PATIENT <hl7-v2_5_1-VXX_V02_PATIENT>`]
     - required
     - PATIENT
