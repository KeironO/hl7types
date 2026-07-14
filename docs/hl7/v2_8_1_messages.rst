v2.8.1 Messages
===============

.. _hl7-v2_8_1-ACK:

ACK General acknowledgment message (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ACK.ACK
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error

.. _hl7-v2_8_1-ADT_A01:

ADT_A01 ADT/ACK - Admit/visit notification (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A01.ADT_A01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_8_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_8_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A02:

ADT_A02 ADT/ACK - Transfer a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A02.ADT_A02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A03:

ADT_A03 ADT/ACK -  Discharge/end visit (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A03.ADT_A03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A03_PROCEDURE <hl7-v2_8_1-ADT_A03_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A03_INSURANCE <hl7-v2_8_1-ADT_A03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A04:

ADT_A04 ADT/ACK -  Register a patient (S3.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A04.ADT_A04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_8_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_8_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A05:

ADT_A05 ADT/ACK -  Pre-admit a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A05.ADT_A05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_8_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_8_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A06:

ADT_A06 ADT/ACK -  Change an outpatient to an inpatient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A06.ADT_A06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_8_1-MRG>`]
     - optional
     - Merge Patient Information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_8_1-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_8_1-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A07:

ADT_A07 ADT/ACK -  Change an inpatient to an outpatient (S3.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A07.ADT_A07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``MRG``
     - Optional[:ref:`MRG <hl7-v2_8_1-MRG>`]
     - optional
     - Merge Patient Information
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A06_PROCEDURE <hl7-v2_8_1-ADT_A06_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A06_INSURANCE <hl7-v2_8_1-ADT_A06_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A08:

ADT_A08 ADT/ACK -  Update patient information (S3.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A08.ADT_A08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_8_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_8_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A09:

ADT_A09 ADT/ACK -  Patient departing - tracking (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A09.ADT_A09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_8_1-ADT_A10:

ADT_A10 ADT/ACK -  Patient arriving - tracking (S3.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A10.ADT_A10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_8_1-ADT_A11:

ADT_A11 ADT/ACK -  Cancel admit/visit notification (S3.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A11.ADT_A11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis

.. _hl7-v2_8_1-ADT_A12:

ADT_A12 ADT/ACK -  Cancel transfer (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A12.ADT_A12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[:ref:`DG1 <hl7-v2_8_1-DG1>`]
     - optional
     - Diagnosis

.. _hl7-v2_8_1-ADT_A13:

ADT_A13 ADT/ACK -  Cancel discharge/end visit (S3.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A13.ADT_A13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A01_PROCEDURE <hl7-v2_8_1-ADT_A01_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A01_INSURANCE <hl7-v2_8_1-ADT_A01_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data
   * - ``PDA``
     - Optional[:ref:`PDA <hl7-v2_8_1-PDA>`]
     - optional
     - Patient Death and Autopsy

.. _hl7-v2_8_1-ADT_A14:

ADT_A14 ADT/ACK -  Pending admit (S3.3.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A14.ADT_A14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_8_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_8_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A15:

ADT_A15 ADT/ACK -  Pending transfer (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A15.ADT_A15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_8_1-ADT_A16:

ADT_A16 ADT/ACK -  Pending discharge (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A16.ADT_A16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A16_PROCEDURE <hl7-v2_8_1-ADT_A16_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A16_INSURANCE <hl7-v2_8_1-ADT_A16_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident

.. _hl7-v2_8_1-ADT_A17:

ADT_A17 ADT/ACK -  Swap patients (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A17.ADT_A17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result

.. _hl7-v2_8_1-ADT_A20:

ADT_A20 ADT/ACK -  Bed status update (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A20.ADT_A20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``NPU``
     - :ref:`NPU <hl7-v2_8_1-NPU>`
     - required
     - Bed Status Update

.. _hl7-v2_8_1-ADT_A24:

ADT_A24 ADT/ACK -  Link patient information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A24.ADT_A24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_8_1-PV1>`]
     - optional
     - Patient Visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability

.. _hl7-v2_8_1-ADT_A28:

ADT_A28 ADT/ACK -  Add person information (S3.3.28).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A28.ADT_A28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_8_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_8_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A31:

ADT_A31 ADT/ACK -  Update person information (S3.3.31).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A31.ADT_A31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`ADT_A05_PROCEDURE <hl7-v2_8_1-ADT_A05_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`ADT_A05_INSURANCE <hl7-v2_8_1-ADT_A05_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``UB1``
     - Optional[:ref:`UB1 <hl7-v2_8_1-UB1>`]
     - optional
     - UB1
   * - ``UB2``
     - Optional[:ref:`UB2 <hl7-v2_8_1-UB2>`]
     - optional
     - Uniform Billing Data

.. _hl7-v2_8_1-ADT_A37:

ADT_A37 ADT/ACK -  Unlink patient information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A37.ADT_A37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - Optional[:ref:`PV1 <hl7-v2_8_1-PV1>`]
     - optional
     - Patient Visit
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability

.. _hl7-v2_8_1-ADT_A38:

ADT_A38 ADT/ACK - Cancel pre-admit (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A38.ADT_A38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``OBX``
     - Optional[List[:ref:`OBX <hl7-v2_8_1-OBX>`]]
     - optional
     - Observation/Result
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group

.. _hl7-v2_8_1-ADT_A39:

ADT_A39 HL7 v2 ADT_A39 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A39.ADT_A39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A39_PATIENT <hl7-v2_8_1-ADT_A39_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-ADT_A43:

ADT_A43 ADT/ACK - Move patient information - patient identifier list (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A43.ADT_A43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_8_1-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-ADT_A44:

ADT_A44 ADT/ACK - Move account information - patient account number (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A44.ADT_A44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A44_PATIENT <hl7-v2_8_1-ADT_A44_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-ADT_A45:

ADT_A45 ADT/ACK - Move visit information - visit number (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A45.ADT_A45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MERGE_INFO``
     - List[:ref:`ADT_A45_MERGE_INFO <hl7-v2_8_1-ADT_A45_MERGE_INFO>`]
     - required
     - MERGE_INFO

.. _hl7-v2_8_1-ADT_A47:

ADT_A47 ADT/ACK - Change patient identifier list (S3.3.47).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A47.ADT_A47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A44_PATIENT <hl7-v2_8_1-ADT_A44_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-ADT_A49:

ADT_A49 ADT/ACK - Change patient account number (S3.3.49).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A49.ADT_A49
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`ADT_A43_PATIENT <hl7-v2_8_1-ADT_A43_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-ADT_A50:

ADT_A50 ADT/ACK - Change visit number (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A50.ADT_A50
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8_1-MRG>`
     - required
     - Merge Patient Information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit

.. _hl7-v2_8_1-ADT_A51:

ADT_A51 ADT/ACK - Change alternate visit ID (S3.3.51).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A51.ADT_A51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``MRG``
     - :ref:`MRG <hl7-v2_8_1-MRG>`
     - required
     - Merge Patient Information
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit

.. _hl7-v2_8_1-ADT_A52:

ADT_A52 ADT/ACK - Cancel leave of absence for a patient (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A52.ADT_A52
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-ADT_A53:

ADT_A53 ADT/ACK - Cancel patient returns from a leave of absence (S3.3.53).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A53.ADT_A53
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-ADT_A54:

ADT_A54 ADT/ACK - Change attending doctor (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A54.ADT_A54
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-ADT_A55:

ADT_A55 ADT/ACK - Cancel change attending doctor (S3.3.55).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A55.ADT_A55
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-ADT_A60:

ADT_A60 ADT/ACK - Update allergy information (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A60.ADT_A60
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``VISIT``
     - Optional[:ref:`ADT_A60_VISIT <hl7-v2_8_1-ADT_A60_VISIT>`]
     - optional
     - VISIT
   * - ``ADVERSE_REACTION_GROUP``
     - Optional[List[:ref:`ADT_A60_ADVERSE_REACTION_GROUP <hl7-v2_8_1-ADT_A60_ADVERSE_REACTION_GROUP>`]]
     - optional
     - ADVERSE_REACTION_GROUP

.. _hl7-v2_8_1-ADT_A61:

ADT_A61 ADT/ACK - Change consulting doctor (S3.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A61.ADT_A61
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-ADT_A62:

ADT_A62 ADT/ACK - Cancel change consulting doctor (S3.3.62).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ADT_A62.ADT_A62
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information

.. _hl7-v2_8_1-BAR_P01:

BAR_P01 BAR/ACK - Add patient accounts (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P01.BAR_P01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - List[:ref:`BAR_P01_VISIT <hl7-v2_8_1-BAR_P01_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_8_1-BAR_P02:

BAR_P02 BAR/ACK - Purge patient accounts (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P02.BAR_P02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`BAR_P02_PATIENT <hl7-v2_8_1-BAR_P02_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-BAR_P05:

BAR_P05 BAR/ACK - Update account (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P05.BAR_P05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - List[:ref:`BAR_P05_VISIT <hl7-v2_8_1-BAR_P05_VISIT>`]
     - required
     - VISIT

.. _hl7-v2_8_1-BAR_P06:

BAR_P06 BAR/ACK - End account (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P06.BAR_P06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PATIENT``
     - List[:ref:`BAR_P06_PATIENT <hl7-v2_8_1-BAR_P06_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-BAR_P10:

BAR_P10 BAR/ACK -Transmit Ambulatory Payment  Classification(APC) (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P10.BAR_P10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``GP1``
     - :ref:`GP1 <hl7-v2_8_1-GP1>`
     - required
     - Grouping/Reimbursement - Visit
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P10_PROCEDURE <hl7-v2_8_1-BAR_P10_PROCEDURE>`]]
     - optional
     - PROCEDURE

.. _hl7-v2_8_1-BAR_P12:

BAR_P12 BAR/ACK - Update Diagnosis/Procedure (S6.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BAR_P12.BAR_P12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``PROCEDURE``
     - Optional[List[:ref:`BAR_P12_PROCEDURE <hl7-v2_8_1-BAR_P12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBX``
     - Optional[:ref:`OBX <hl7-v2_8_1-OBX>`]
     - optional
     - Observation/Result

.. _hl7-v2_8_1-BPS_O29:

BPS_O29 BPS - Blood product dispense status (S4.13.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BPS_O29.BPS_O29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`BPS_O29_PATIENT <hl7-v2_8_1-BPS_O29_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`BPS_O29_ORDER <hl7-v2_8_1-BPS_O29_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-BRP_O30:

BRP_O30 BRP - Blood product dispense status acknowledgment (S4.13.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BRP_O30.BRP_O30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`BRP_O30_RESPONSE <hl7-v2_8_1-BRP_O30_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-BRT_O32:

BRT_O32 BRT - Blood product transfusion/disposition acknowledgment (S4.13.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BRT_O32.BRT_O32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`BRT_O32_RESPONSE <hl7-v2_8_1-BRT_O32_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-BTS_O31:

BTS_O31 BTS - Blood product transfusion/disposition (S4.13.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.BTS_O31.BTS_O31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`BTS_O31_PATIENT <hl7-v2_8_1-BTS_O31_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`BTS_O31_ORDER <hl7-v2_8_1-BTS_O31_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-CCF_I22:

CCF_I22 Collaborative Care Fetch / Collaborative Care Information (S11.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCF_I22.CCF_I22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification

.. _hl7-v2_8_1-CCI_I22:

CCI_I22 Collaborative Care Fetch / Collaborative Care Information (S11.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCI_I22.CCI_I22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCI_I22_INSURANCE <hl7-v2_8_1-CCI_I22_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCI_I22_APPOINTMENT_HISTORY <hl7-v2_8_1-CCI_I22_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCI_I22_CLINICAL_HISTORY <hl7-v2_8_1-CCI_I22_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCI_I22_PATIENT_VISITS <hl7-v2_8_1-CCI_I22_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCI_I22_MEDICATION_HISTORY <hl7-v2_8_1-CCI_I22_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCI_I22_PROBLEM <hl7-v2_8_1-CCI_I22_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCI_I22_GOAL <hl7-v2_8_1-CCI_I22_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCI_I22_PATHWAY <hl7-v2_8_1-CCI_I22_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCM_I21:

CCM_I21 Collaborative Care Message (S11.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCM_I21.CCM_I21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCM_I21_INSURANCE <hl7-v2_8_1-CCM_I21_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCM_I21_APPOINTMENT_HISTORY <hl7-v2_8_1-CCM_I21_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCM_I21_CLINICAL_HISTORY <hl7-v2_8_1-CCM_I21_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCM_I21_PATIENT_VISITS <hl7-v2_8_1-CCM_I21_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCM_I21_MEDICATION_HISTORY <hl7-v2_8_1-CCM_I21_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCM_I21_PROBLEM <hl7-v2_8_1-CCM_I21_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCM_I21_GOAL <hl7-v2_8_1-CCM_I21_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCM_I21_PATHWAY <hl7-v2_8_1-CCM_I21_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCQ_I19:

CCQ_I19 Collaborative Care Query/Collaborative Care Query Update (S11.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCQ_I19.CCQ_I19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - Optional[List[:ref:`CCQ_I19_PROVIDER_CONTACT <hl7-v2_8_1-CCQ_I19_PROVIDER_CONTACT>`]]
     - optional
     - PROVIDER_CONTACT
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCR_I16:

CCR_I16 Collaborative Care Referral (S11.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCR_I16.CCR_I16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - List[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - List[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8_1-CCR_I16_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - Optional[List[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8_1-CCR_I16_CLINICAL_ORDER>`]]
     - optional
     - CLINICAL_ORDER
   * - ``PATIENT``
     - List[:ref:`CCR_I16_PATIENT <hl7-v2_8_1-CCR_I16_PATIENT>`]
     - required
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCR_I16_INSURANCE <hl7-v2_8_1-CCR_I16_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8_1-CCR_I16_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8_1-CCR_I16_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8_1-CCR_I16_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8_1-CCR_I16_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCR_I16_PROBLEM <hl7-v2_8_1-CCR_I16_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCR_I16_GOAL <hl7-v2_8_1-CCR_I16_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCR_I16_PATHWAY <hl7-v2_8_1-CCR_I16_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCR_I17:

CCR_I17 Modify Collaborative Care Referral (S11.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCR_I17.CCR_I17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - List[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - List[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8_1-CCR_I16_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - Optional[List[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8_1-CCR_I16_CLINICAL_ORDER>`]]
     - optional
     - CLINICAL_ORDER
   * - ``PATIENT``
     - List[:ref:`CCR_I16_PATIENT <hl7-v2_8_1-CCR_I16_PATIENT>`]
     - required
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCR_I16_INSURANCE <hl7-v2_8_1-CCR_I16_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8_1-CCR_I16_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8_1-CCR_I16_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8_1-CCR_I16_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8_1-CCR_I16_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCR_I16_PROBLEM <hl7-v2_8_1-CCR_I16_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCR_I16_GOAL <hl7-v2_8_1-CCR_I16_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCR_I16_PATHWAY <hl7-v2_8_1-CCR_I16_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCR_I18:

CCR_I18 Cancel Collaborative Care Referral (S11.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCR_I18.CCR_I18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - List[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - List[:ref:`CCR_I16_PROVIDER_CONTACT <hl7-v2_8_1-CCR_I16_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``CLINICAL_ORDER``
     - Optional[List[:ref:`CCR_I16_CLINICAL_ORDER <hl7-v2_8_1-CCR_I16_CLINICAL_ORDER>`]]
     - optional
     - CLINICAL_ORDER
   * - ``PATIENT``
     - List[:ref:`CCR_I16_PATIENT <hl7-v2_8_1-CCR_I16_PATIENT>`]
     - required
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCR_I16_INSURANCE <hl7-v2_8_1-CCR_I16_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCR_I16_APPOINTMENT_HISTORY <hl7-v2_8_1-CCR_I16_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCR_I16_CLINICAL_HISTORY <hl7-v2_8_1-CCR_I16_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCR_I16_PATIENT_VISITS <hl7-v2_8_1-CCR_I16_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCR_I16_MEDICATION_HISTORY <hl7-v2_8_1-CCR_I16_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCR_I16_PROBLEM <hl7-v2_8_1-CCR_I16_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCR_I16_GOAL <hl7-v2_8_1-CCR_I16_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCR_I16_PATHWAY <hl7-v2_8_1-CCR_I16_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CCU_I20:

CCU_I20 Asynchronous Collaborative Care Update (S11.6.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CCU_I20.CCU_I20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - Optional[List[:ref:`CCU_I20_PROVIDER_CONTACT <hl7-v2_8_1-CCU_I20_PROVIDER_CONTACT>`]]
     - optional
     - PROVIDER_CONTACT
   * - ``PATIENT``
     - Optional[List[:ref:`CCU_I20_PATIENT <hl7-v2_8_1-CCU_I20_PATIENT>`]]
     - optional
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CCU_I20_INSURANCE <hl7-v2_8_1-CCU_I20_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CCU_I20_APPOINTMENT_HISTORY <hl7-v2_8_1-CCU_I20_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CCU_I20_CLINICAL_HISTORY <hl7-v2_8_1-CCU_I20_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CCU_I20_PATIENT_VISITS <hl7-v2_8_1-CCU_I20_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CCU_I20_MEDICATION_HISTORY <hl7-v2_8_1-CCU_I20_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CCU_I20_PROBLEM <hl7-v2_8_1-CCU_I20_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CCU_I20_GOAL <hl7-v2_8_1-CCU_I20_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CCU_I20_PATHWAY <hl7-v2_8_1-CCU_I20_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CQU_I19:

CQU_I19 Collaborative Care Query/Collaborative Care Query Update (S11.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CQU_I19.CQU_I19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``RF1``
     - :ref:`RF1 <hl7-v2_8_1-RF1>`
     - required
     - Referral Information
   * - ``PROVIDER_CONTACT``
     - Optional[List[:ref:`CQU_I19_PROVIDER_CONTACT <hl7-v2_8_1-CQU_I19_PROVIDER_CONTACT>`]]
     - optional
     - PROVIDER_CONTACT
   * - ``PATIENT``
     - Optional[List[:ref:`CQU_I19_PATIENT <hl7-v2_8_1-CQU_I19_PATIENT>`]]
     - optional
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``INSURANCE``
     - Optional[List[:ref:`CQU_I19_INSURANCE <hl7-v2_8_1-CQU_I19_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``APPOINTMENT_HISTORY``
     - Optional[List[:ref:`CQU_I19_APPOINTMENT_HISTORY <hl7-v2_8_1-CQU_I19_APPOINTMENT_HISTORY>`]]
     - optional
     - APPOINTMENT_HISTORY
   * - ``CLINICAL_HISTORY``
     - Optional[List[:ref:`CQU_I19_CLINICAL_HISTORY <hl7-v2_8_1-CQU_I19_CLINICAL_HISTORY>`]]
     - optional
     - CLINICAL_HISTORY
   * - ``PATIENT_VISITS``
     - List[:ref:`CQU_I19_PATIENT_VISITS <hl7-v2_8_1-CQU_I19_PATIENT_VISITS>`]
     - required
     - PATIENT_VISITS
   * - ``MEDICATION_HISTORY``
     - Optional[List[:ref:`CQU_I19_MEDICATION_HISTORY <hl7-v2_8_1-CQU_I19_MEDICATION_HISTORY>`]]
     - optional
     - MEDICATION_HISTORY
   * - ``PROBLEM``
     - Optional[List[:ref:`CQU_I19_PROBLEM <hl7-v2_8_1-CQU_I19_PROBLEM>`]]
     - optional
     - PROBLEM
   * - ``GOAL``
     - Optional[List[:ref:`CQU_I19_GOAL <hl7-v2_8_1-CQU_I19_GOAL>`]]
     - optional
     - GOAL
   * - ``PATHWAY``
     - Optional[List[:ref:`CQU_I19_PATHWAY <hl7-v2_8_1-CQU_I19_PATHWAY>`]]
     - optional
     - PATHWAY
   * - ``REL``
     - Optional[List[:ref:`REL <hl7-v2_8_1-REL>`]]
     - optional
     - Clinical Relationship Segment

.. _hl7-v2_8_1-CRM_C01:

CRM_C01 CRM - Register a patient on a clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C01.CRM_C01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C02:

CRM_C02 CRM - Cancel a patient registration on clinical trial (for clerical mistakes onl (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C02.CRM_C02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C03:

CRM_C03 CRM - Correct/update registration information (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C03.CRM_C03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C04:

CRM_C04 CRM - Patient has gone off a clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C04.CRM_C04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C05:

CRM_C05 CRM - Patient enters phase of clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C05.CRM_C05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C06:

CRM_C06 CRM - Cancel patient entering a phase (clerical mistake) (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C06.CRM_C06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C07:

CRM_C07 CRM - Correct/update phase information (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C07.CRM_C07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CRM_C08:

CRM_C08 CRM - Patient has gone off phase of clinical trial (S7.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CRM_C08.CRM_C08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CRM_C01_PATIENT <hl7-v2_8_1-CRM_C01_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CSU_C09:

CSU_C09 CSU - Automated time intervals for reporting, like monthly (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CSU_C09.CSU_C09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_8_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CSU_C10:

CSU_C10 CSU - Patient completes the clinical trial (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CSU_C10.CSU_C10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_8_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CSU_C11:

CSU_C11 CSU - Patient completes a phase of the clinical trial (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CSU_C11.CSU_C11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_8_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-CSU_C12:

CSU_C12 CSU - Update/correction of patient order/result information (S7.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.CSU_C12.CSU_C12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT``
     - List[:ref:`CSU_C09_PATIENT <hl7-v2_8_1-CSU_C09_PATIENT>`]
     - required
     - PATIENT

.. _hl7-v2_8_1-DBC_O41:

DBC_O41 DBC - Create Donor Record Message (S4.16.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DBC_O41.DBC_O41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DBC_O41_DONOR <hl7-v2_8_1-DBC_O41_DONOR>`]
     - optional
     - DONOR

.. _hl7-v2_8_1-DBC_O42:

DBC_O42 DBU - Update Donor Record Message (S4.16.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DBC_O42.DBC_O42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DBC_O42_DONOR <hl7-v2_8_1-DBC_O42_DONOR>`]
     - optional
     - DONOR

.. _hl7-v2_8_1-DEL_O46:

DEL_O46 Donor Eligiblity Message (S4.16.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DEL_O46.DEL_O46
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DEL_O46_DONOR <hl7-v2_8_1-DEL_O46_DONOR>`]
     - optional
     - DONOR
   * - ``DON``
     - :ref:`DON <hl7-v2_8_1-DON>`
     - required
     - Donation
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-DEO_O45:

DEO_O45 Donor Eligibility Observations Message (S4.16.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DEO_O45.DEO_O45
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DEO_O45_DONOR <hl7-v2_8_1-DEO_O45_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION_ORDER``
     - List[:ref:`DEO_O45_DONATION_ORDER <hl7-v2_8_1-DEO_O45_DONATION_ORDER>`]
     - required
     - DONATION_ORDER

.. _hl7-v2_8_1-DER_O44:

DER_O44 Donor Registration - Minimal Message (S4.16.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DER_O44.DER_O44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DER_O44_DONOR <hl7-v2_8_1-DER_O44_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION_ORDER``
     - List[:ref:`DER_O44_DONATION_ORDER <hl7-v2_8_1-DER_O44_DONATION_ORDER>`]
     - required
     - DONATION_ORDER

.. _hl7-v2_8_1-DFT_P03:

DFT_P03 DFT/ACK - Post detail financial transaction (S6.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DFT_P03.DFT_P03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - Optional[:ref:`DFT_P03_VISIT <hl7-v2_8_1-DFT_P03_VISIT>`]
     - optional
     - VISIT
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`DFT_P03_COMMON_ORDER <hl7-v2_8_1-DFT_P03_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``FINANCIAL``
     - List[:ref:`DFT_P03_FINANCIAL <hl7-v2_8_1-DFT_P03_FINANCIAL>`]
     - required
     - FINANCIAL
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`DFT_P03_INSURANCE <hl7-v2_8_1-DFT_P03_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident

.. _hl7-v2_8_1-DFT_P11:

DFT_P11 DFT/ACK - Post Detail Financial Transactions - New (S6.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DFT_P11.DFT_P11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role
   * - ``VISIT``
     - Optional[:ref:`DFT_P11_VISIT <hl7-v2_8_1-DFT_P11_VISIT>`]
     - optional
     - VISIT
   * - ``DB1``
     - Optional[List[:ref:`DB1 <hl7-v2_8_1-DB1>`]]
     - optional
     - Disability
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`DFT_P11_COMMON_ORDER <hl7-v2_8_1-DFT_P11_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[:ref:`DRG <hl7-v2_8_1-DRG>`]
     - optional
     - Diagnosis Related Group
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`DFT_P11_INSURANCE <hl7-v2_8_1-DFT_P11_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``FINANCIAL``
     - List[:ref:`DFT_P11_FINANCIAL <hl7-v2_8_1-DFT_P11_FINANCIAL>`]
     - required
     - FINANCIAL

.. _hl7-v2_8_1-DPR_O48:

DPR_O48 Donation Procedure Message (S4.16.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DPR_O48.DPR_O48
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DPR_O48_DONOR <hl7-v2_8_1-DPR_O48_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION_ORDER``
     - List[:ref:`DPR_O48_DONATION_ORDER <hl7-v2_8_1-DPR_O48_DONATION_ORDER>`]
     - required
     - DONATION_ORDER
   * - ``DONATION``
     - Optional[:ref:`DPR_O48_DONATION <hl7-v2_8_1-DPR_O48_DONATION>`]
     - optional
     - DONATION

.. _hl7-v2_8_1-DRC_O47:

DRC_O47 Donor Request to Collect Message (S4.16.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DRC_O47.DRC_O47
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DRC_O47_DONOR <hl7-v2_8_1-DRC_O47_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION_ORDER``
     - List[:ref:`DRC_O47_DONATION_ORDER <hl7-v2_8_1-DRC_O47_DONATION_ORDER>`]
     - required
     - DONATION_ORDER

.. _hl7-v2_8_1-DRG_O43:

DRG_O43 General Order Message with Document Payload Acknowledgement Message (S4.16.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.DRG_O43.DRG_O43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DONOR``
     - Optional[:ref:`DRG_O43_DONOR <hl7-v2_8_1-DRG_O43_DONOR>`]
     - optional
     - DONOR

.. _hl7-v2_8_1-EAC_U07:

EAC_U07 EAC/ACK - Automated equipment command (S13.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EAC_U07.EAC_U07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``COMMAND``
     - List[:ref:`EAC_U07_COMMAND <hl7-v2_8_1-EAC_U07_COMMAND>`]
     - required
     - COMMAND

.. _hl7-v2_8_1-EAN_U09:

EAN_U09 EAN/ACK - Automated equipment notification (S13.3.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EAN_U09.EAN_U09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``NOTIFICATION``
     - List[:ref:`EAN_U09_NOTIFICATION <hl7-v2_8_1-EAN_U09_NOTIFICATION>`]
     - required
     - NOTIFICATION

.. _hl7-v2_8_1-EAR_U08:

EAR_U08 EAR/ACK - Automated equipment response (S13.3.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EAR_U08.EAR_U08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``COMMAND_RESPONSE``
     - List[:ref:`EAR_U08_COMMAND_RESPONSE <hl7-v2_8_1-EAR_U08_COMMAND_RESPONSE>`]
     - required
     - COMMAND_RESPONSE

.. _hl7-v2_8_1-EHC_E01:

EHC_E01 Submit HealthCare Services Invoice (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E01.EHC_E01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``INVOICE_INFORMATION_SUBMIT``
     - :ref:`EHC_E01_INVOICE_INFORMATION_SUBMIT <hl7-v2_8_1-EHC_E01_INVOICE_INFORMATION_SUBMIT>`
     - required
     - INVOICE_INFORMATION_SUBMIT

.. _hl7-v2_8_1-EHC_E02:

EHC_E02 Cancel HealthCare Services Invoice (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E02.EHC_E02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``INVOICE_INFORMATION_CANCEL``
     - :ref:`EHC_E02_INVOICE_INFORMATION_CANCEL <hl7-v2_8_1-EHC_E02_INVOICE_INFORMATION_CANCEL>`
     - required
     - INVOICE_INFORMATION_CANCEL

.. _hl7-v2_8_1-EHC_E04:

EHC_E04 Re-Assess HealthCare Services Invoice Request (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E04.EHC_E04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``REASSESSMENT_REQUEST_INFO``
     - :ref:`EHC_E04_REASSESSMENT_REQUEST_INFO <hl7-v2_8_1-EHC_E04_REASSESSMENT_REQUEST_INFO>`
     - required
     - REASSESSMENT_REQUEST_INFO

.. _hl7-v2_8_1-EHC_E10:

EHC_E10 Edit/Adjudication Results (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E10.EHC_E10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``INVOICE_PROCESSING_RESULTS_INFO``
     - List[:ref:`EHC_E10_INVOICE_PROCESSING_RESULTS_INFO <hl7-v2_8_1-EHC_E10_INVOICE_PROCESSING_RESULTS_INFO>`]
     - required
     - INVOICE_PROCESSING_RESULTS_INFO

.. _hl7-v2_8_1-EHC_E12:

EHC_E12 Request Additional Information (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E12.EHC_E12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``RFI``
     - :ref:`RFI <hl7-v2_8_1-RFI>`
     - required
     - Request for Information
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_8_1-CTD>`]]
     - optional
     - Contact Data
   * - ``IVC``
     - :ref:`IVC <hl7-v2_8_1-IVC>`
     - required
     - Invoice Segment
   * - ``PSS``
     - :ref:`PSS <hl7-v2_8_1-PSS>`
     - required
     - Product/Service Section
   * - ``PSG``
     - :ref:`PSG <hl7-v2_8_1-PSG>`
     - required
     - Product/Service Group
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     - Patient Identification
   * - ``PSL``
     - Optional[List[:ref:`PSL <hl7-v2_8_1-PSL>`]]
     - optional
     - Product/Service Line Item
   * - ``REQUEST``
     - List[:ref:`EHC_E12_REQUEST <hl7-v2_8_1-EHC_E12_REQUEST>`]
     - required
     - REQUEST

.. _hl7-v2_8_1-EHC_E13:

EHC_E13 Additional Information Response (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E13.EHC_E13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``RFI``
     - :ref:`RFI <hl7-v2_8_1-RFI>`
     - required
     - Request for Information
   * - ``CTD``
     - Optional[List[:ref:`CTD <hl7-v2_8_1-CTD>`]]
     - optional
     - Contact Data
   * - ``IVC``
     - :ref:`IVC <hl7-v2_8_1-IVC>`
     - required
     - Invoice Segment
   * - ``PSS``
     - :ref:`PSS <hl7-v2_8_1-PSS>`
     - required
     - Product/Service Section
   * - ``PSG``
     - :ref:`PSG <hl7-v2_8_1-PSG>`
     - required
     - Product/Service Group
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     - Patient Identification
   * - ``PSL``
     - Optional[:ref:`PSL <hl7-v2_8_1-PSL>`]
     - optional
     - Product/Service Line Item
   * - ``REQUEST``
     - List[:ref:`EHC_E13_REQUEST <hl7-v2_8_1-EHC_E13_REQUEST>`]
     - required
     - REQUEST

.. _hl7-v2_8_1-EHC_E15:

EHC_E15 Payment/Remittance Advice (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E15.EHC_E15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``PAYMENT_REMITTANCE_HEADER_INFO``
     - :ref:`EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO <hl7-v2_8_1-EHC_E15_PAYMENT_REMITTANCE_HEADER_INFO>`
     - required
     - PAYMENT_REMITTANCE_HEADER_INFO
   * - ``PAYMENT_REMITTANCE_DETAIL_INFO``
     - Optional[List[:ref:`EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO <hl7-v2_8_1-EHC_E15_PAYMENT_REMITTANCE_DETAIL_INFO>`]]
     - optional
     - PAYMENT_REMITTANCE_DETAIL_INFO
   * - ``ADJUSTMENT_PAYEE``
     - Optional[List[:ref:`EHC_E15_ADJUSTMENT_PAYEE <hl7-v2_8_1-EHC_E15_ADJUSTMENT_PAYEE>`]]
     - optional
     - ADJUSTMENT_PAYEE

.. _hl7-v2_8_1-EHC_E20:

EHC_E20 Submit Authorization Request (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E20.EHC_E20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``AUTHORIZATION_REQUEST``
     - :ref:`EHC_E20_AUTHORIZATION_REQUEST <hl7-v2_8_1-EHC_E20_AUTHORIZATION_REQUEST>`
     - required
     - AUTHORIZATION_REQUEST

.. _hl7-v2_8_1-EHC_E21:

EHC_E21 Cancel Authorization Request (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E21.EHC_E21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``AUTHORIZATION_REQUEST``
     - :ref:`EHC_E21_AUTHORIZATION_REQUEST <hl7-v2_8_1-EHC_E21_AUTHORIZATION_REQUEST>`
     - required
     - AUTHORIZATION_REQUEST

.. _hl7-v2_8_1-EHC_E24:

EHC_E24 Authorization Response (S16.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.EHC_E24.EHC_E24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``AUTHORIZATION_RESPONSE_INFO``
     - :ref:`EHC_E24_AUTHORIZATION_RESPONSE_INFO <hl7-v2_8_1-EHC_E24_AUTHORIZATION_RESPONSE_INFO>`
     - required
     - AUTHORIZATION_RESPONSE_INFO

.. _hl7-v2_8_1-ESR_U02:

ESR_U02 ESR/ACK - Automated equipment status request (S13.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ESR_U02.ESR_U02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail

.. _hl7-v2_8_1-ESU_U01:

ESU_U01 ESU/ACK - Automated equipment status update (S13.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ESU_U01.ESU_U01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``ISD``
     - Optional[List[:ref:`ISD <hl7-v2_8_1-ISD>`]]
     - optional
     - Interaction Status Detail

.. _hl7-v2_8_1-INR_U06:

INR_U06 INR/ACK - Automated equipment inventory request (S13.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.INR_U06.INR_U06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``INV``
     - List[:ref:`INV <hl7-v2_8_1-INV>`]
     - required
     - Inventory Detail

.. _hl7-v2_8_1-INU_U05:

INU_U05 INU/ACK  - Automated equipment inventory update (S13.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.INU_U05.INU_U05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``INV``
     - List[:ref:`INV <hl7-v2_8_1-INV>`]
     - required
     - Inventory Detail

.. _hl7-v2_8_1-LSU_U12:

LSU_U12 LSU/ACK - Automated equipment log/service update (S13.3.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.LSU_U12.LSU_U12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``EQP``
     - List[:ref:`EQP <hl7-v2_8_1-EQP>`]
     - required
     - Equipment/log Service

.. _hl7-v2_8_1-LSU_U13:

LSU_U13 LSR/ACK - Automated equipment log/service request (S13.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.LSU_U13.LSU_U13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``EQP``
     - List[:ref:`EQP <hl7-v2_8_1-EQP>`]
     - required
     - Equipment/log Service

.. _hl7-v2_8_1-MDM_T01:

MDM_T01 MDM/ACK - Original document notification (S9.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T01.MDM_T01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MDM_T02:

MDM_T02 MDM/ACK - Original document notification and content (S9.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T02.MDM_T02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment
   * - ``OBSERVATION``
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-MDM_T03:

MDM_T03 MDM/ACK - Document status change notification (S9.6.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T03.MDM_T03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MDM_T04:

MDM_T04 MDM/ACK - Document status change notification and content (S9.6.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T04.MDM_T04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment
   * - ``OBSERVATION``
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-MDM_T05:

MDM_T05 MDM/ACK - Document addendum notification (S9.6.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T05.MDM_T05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MDM_T06:

MDM_T06 MDM/ACK - Document addendum notification and content (S9.6.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T06.MDM_T06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment
   * - ``OBSERVATION``
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-MDM_T07:

MDM_T07 MDM/ACK - Document edit notification (S9.6.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T07.MDM_T07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MDM_T08:

MDM_T08 MDM/ACK - Document edit notification and content (S9.6.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T08.MDM_T08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment
   * - ``OBSERVATION``
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-MDM_T09:

MDM_T09 MDM/ACK - Document replacement notification (S9.6.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T09.MDM_T09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MDM_T10:

MDM_T10 MDM/ACK - Document replacement notification and content (S9.6.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T10.MDM_T10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T02_COMMON_ORDER <hl7-v2_8_1-MDM_T02_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment
   * - ``OBSERVATION``
     - List[:ref:`MDM_T02_OBSERVATION <hl7-v2_8_1-MDM_T02_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-MDM_T11:

MDM_T11 MDM/ACK - Document cancel notification (S9.6.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MDM_T11.MDM_T11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``COMMON_ORDER``
     - Optional[List[:ref:`MDM_T01_COMMON_ORDER <hl7-v2_8_1-MDM_T01_COMMON_ORDER>`]]
     - optional
     - COMMON_ORDER
   * - ``TXA``
     - :ref:`TXA <hl7-v2_8_1-TXA>`
     - required
     - Transcription Document Header
   * - ``CON``
     - Optional[List[:ref:`CON <hl7-v2_8_1-CON>`]]
     - optional
     - Consent Segment

.. _hl7-v2_8_1-MFK_M01:

MFK_M01 HL7 v2 MFK_M01 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFK_M01.MFK_M01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MFA``
     - Optional[List[:ref:`MFA <hl7-v2_8_1-MFA>`]]
     - optional
     - Master File Acknowledgment

.. _hl7-v2_8_1-MFN_M02:

MFN_M02 MFN/MFK - Master file - staff practitioner (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M02.MFN_M02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_STAFF``
     - List[:ref:`MFN_M02_MF_STAFF <hl7-v2_8_1-MFN_M02_MF_STAFF>`]
     - required
     - MF_STAFF

.. _hl7-v2_8_1-MFN_M04:

MFN_M04 MFN/MFK - Master files charge description (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M04.MFN_M04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``MF_CDM``
     - List[:ref:`MFN_M04_MF_CDM <hl7-v2_8_1-MFN_M04_MF_CDM>`]
     - required
     - MF_CDM

.. _hl7-v2_8_1-MFN_M05:

MFN_M05 MFN/MFK - Patient location master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M05.MFN_M05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_LOCATION``
     - List[:ref:`MFN_M05_MF_LOCATION <hl7-v2_8_1-MFN_M05_MF_LOCATION>`]
     - required
     - MF_LOCATION

.. _hl7-v2_8_1-MFN_M06:

MFN_M06 MFN/MFK - Clinical study with phases and schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M06.MFN_M06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_CLIN_STUDY``
     - List[:ref:`MFN_M06_MF_CLIN_STUDY <hl7-v2_8_1-MFN_M06_MF_CLIN_STUDY>`]
     - required
     - MF_CLIN_STUDY

.. _hl7-v2_8_1-MFN_M07:

MFN_M07 MFN/MFK - Clinical study without phases but with schedules master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M07.MFN_M07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_CLIN_STUDY_SCHED``
     - List[:ref:`MFN_M07_MF_CLIN_STUDY_SCHED <hl7-v2_8_1-MFN_M07_MF_CLIN_STUDY_SCHED>`]
     - required
     - MF_CLIN_STUDY_SCHED

.. _hl7-v2_8_1-MFN_M08:

MFN_M08 MFN/MFK - Test/observation (numeric) master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M08.MFN_M08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_NUMERIC``
     - List[:ref:`MFN_M08_MF_TEST_NUMERIC <hl7-v2_8_1-MFN_M08_MF_TEST_NUMERIC>`]
     - required
     - MF_TEST_NUMERIC

.. _hl7-v2_8_1-MFN_M09:

MFN_M09 MFN/MFK - Test/observation (categorical) master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M09.MFN_M09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_CATEGORICAL``
     - List[:ref:`MFN_M09_MF_TEST_CATEGORICAL <hl7-v2_8_1-MFN_M09_MF_TEST_CATEGORICAL>`]
     - required
     - MF_TEST_CATEGORICAL

.. _hl7-v2_8_1-MFN_M10:

MFN_M10 MFN/MFK - Test /observation batteries master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M10.MFN_M10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_BATTERIES``
     - List[:ref:`MFN_M10_MF_TEST_BATTERIES <hl7-v2_8_1-MFN_M10_MF_TEST_BATTERIES>`]
     - required
     - MF_TEST_BATTERIES

.. _hl7-v2_8_1-MFN_M11:

MFN_M11 MFN/MFK - Test/calculated observations master file (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M11.MFN_M11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_TEST_CALCULATED``
     - List[:ref:`MFN_M11_MF_TEST_CALCULATED <hl7-v2_8_1-MFN_M11_MF_TEST_CALCULATED>`]
     - required
     - MF_TEST_CALCULATED

.. _hl7-v2_8_1-MFN_M12:

MFN_M12 MFN/MFK - Master file notification message (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M12.MFN_M12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_OBS_ATTRIBUTES``
     - List[:ref:`MFN_M12_MF_OBS_ATTRIBUTES <hl7-v2_8_1-MFN_M12_MF_OBS_ATTRIBUTES>`]
     - required
     - MF_OBS_ATTRIBUTES

.. _hl7-v2_8_1-MFN_M13:

MFN_M13 MFN/MFK - Master file notification - general (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M13.MFN_M13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MFE``
     - List[:ref:`MFE <hl7-v2_8_1-MFE>`]
     - required
     - Master File Entry

.. _hl7-v2_8_1-MFN_M14:

MFN_M14 MFN/MFK - Master file notification - site defined (S8.4.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M14.MFN_M14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_SITE_DEFINED``
     - List[MFN_ZnnMF_SITE_DEFINED]
     - required
     - MF_SITE_DEFINED

.. _hl7-v2_8_1-MFN_M15:

MFN_M15 MFN/MFK - Inventory item master file notification (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M15.MFN_M15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_INV_ITEM``
     - List[:ref:`MFN_M15_MF_INV_ITEM <hl7-v2_8_1-MFN_M15_MF_INV_ITEM>`]
     - required
     - MF_INV_ITEM

.. _hl7-v2_8_1-MFN_M16:

MFN_M16 MFN/MFK - Master File Notification Inventory Item Enhanced (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M16.MFN_M16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MATERIAL_ITEM_RECORD``
     - List[:ref:`MFN_M16_MATERIAL_ITEM_RECORD <hl7-v2_8_1-MFN_M16_MATERIAL_ITEM_RECORD>`]
     - required
     - MATERIAL_ITEM_RECORD

.. _hl7-v2_8_1-MFN_M17:

MFN_M17 DRG Master File Message (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_M17.MFN_M17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_DRG``
     - List[:ref:`MFN_M17_MF_DRG <hl7-v2_8_1-MFN_M17_MF_DRG>`]
     - required
     - MF_DRG

.. _hl7-v2_8_1-MFN_Znn:

MFN_Znn Master files notification (S8.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.MFN_Znn.MFN_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MFI``
     - :ref:`MFI <hl7-v2_8_1-MFI>`
     - required
     - Master File Identification
   * - ``MF_SITE_DEFINED``
     - List[MFN_ZnnMF_SITE_DEFINED]
     - required
     - MF_SITE_DEFINED

.. _hl7-v2_8_1-NMD_N02:

NMD_N02 NMD/ACK - Application management data message (unsolicited) (S14.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.NMD_N02.NMD_N02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``CLOCK_AND_STATS_WITH_NOTES``
     - List[:ref:`NMD_N02_CLOCK_AND_STATS_WITH_NOTES <hl7-v2_8_1-NMD_N02_CLOCK_AND_STATS_WITH_NOTES>`]
     - required
     - CLOCK_AND_STATS_WITH_NOTES

.. _hl7-v2_8_1-OMB_O27:

OMB_O27 OMB - Blood product order (S4.13.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMB_O27.OMB_O27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMB_O27_PATIENT <hl7-v2_8_1-OMB_O27_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMB_O27_ORDER <hl7-v2_8_1-OMB_O27_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMD_O03:

OMD_O03 OMD - Diet order (S4.7.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMD_O03.OMD_O03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMD_O03_PATIENT <hl7-v2_8_1-OMD_O03_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER_DIET``
     - List[:ref:`OMD_O03_ORDER_DIET <hl7-v2_8_1-OMD_O03_ORDER_DIET>`]
     - required
     - ORDER_DIET
   * - ``ORDER_TRAY``
     - Optional[List[:ref:`OMD_O03_ORDER_TRAY <hl7-v2_8_1-OMD_O03_ORDER_TRAY>`]]
     - optional
     - ORDER_TRAY

.. _hl7-v2_8_1-OMG_O19:

OMG_O19 OMG - General clinical order (S4.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMG_O19.OMG_O19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMG_O19_PATIENT <hl7-v2_8_1-OMG_O19_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMG_O19_ORDER <hl7-v2_8_1-OMG_O19_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMI_O23:

OMI_O23 OMI - Imaging order (S4.4.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMI_O23.OMI_O23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMI_O23_PATIENT <hl7-v2_8_1-OMI_O23_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMI_O23_ORDER <hl7-v2_8_1-OMI_O23_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OML_O21:

OML_O21 OML - Laboratory order (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O21.OML_O21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O21_PATIENT <hl7-v2_8_1-OML_O21_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OML_O21_ORDER <hl7-v2_8_1-OML_O21_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OML_O33:

OML_O33 OML - Laboratory order for multiple orders related to a single specimen (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O33.OML_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O33_PATIENT <hl7-v2_8_1-OML_O33_PATIENT>`]
     - optional
     - PATIENT
   * - ``SPECIMEN``
     - List[:ref:`OML_O33_SPECIMEN <hl7-v2_8_1-OML_O33_SPECIMEN>`]
     - required
     - SPECIMEN

.. _hl7-v2_8_1-OML_O35:

OML_O35 OML - Laboratory order for multiple orders related to a single container of a sp (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O35.OML_O35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O35_PATIENT <hl7-v2_8_1-OML_O35_PATIENT>`]
     - optional
     - PATIENT
   * - ``SPECIMEN``
     - List[:ref:`OML_O35_SPECIMEN <hl7-v2_8_1-OML_O35_SPECIMEN>`]
     - required
     - SPECIMEN

.. _hl7-v2_8_1-OML_O39:

OML_O39 Specimen shipment centric laboratory order (S4.4.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OML_O39.OML_O39
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OML_O39_PATIENT <hl7-v2_8_1-OML_O39_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OML_O39_ORDER <hl7-v2_8_1-OML_O39_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMN_O07:

OMN_O07 OMN - Non-stock requisition order (S4.10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMN_O07.OMN_O07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMN_O07_PATIENT <hl7-v2_8_1-OMN_O07_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMN_O07_ORDER <hl7-v2_8_1-OMN_O07_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMP_O09:

OMP_O09 OMP - Pharmacy/treatment order (S4.A.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMP_O09.OMP_O09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMP_O09_PATIENT <hl7-v2_8_1-OMP_O09_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMP_O09_ORDER <hl7-v2_8_1-OMP_O09_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMQ_O57:

OMQ_O57 HL7 v2 OMQ_O57 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMQ_O57.OMQ_O57
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMQ_O57_PATIENT <hl7-v2_8_1-OMQ_O57_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMQ_O57_ORDER <hl7-v2_8_1-OMQ_O57_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OMS_O05:

OMS_O05 OMS - Stock requisition order (S4.10.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OMS_O05.OMS_O05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OMS_O05_PATIENT <hl7-v2_8_1-OMS_O05_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`OMS_O05_ORDER <hl7-v2_8_1-OMS_O05_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OPL_O37:

OPL_O37 OPL - Population/Location-Based Laboratory Order Message (S4.4.16).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OPL_O37.OPL_O37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PRT``
     - List[:ref:`PRT <hl7-v2_8_1-PRT>`]
     - required
     - Participation Information
   * - ``GUARANTOR``
     - Optional[:ref:`OPL_O37_GUARANTOR <hl7-v2_8_1-OPL_O37_GUARANTOR>`]
     - optional
     - GUARANTOR
   * - ``ORDER``
     - List[:ref:`OPL_O37_ORDER <hl7-v2_8_1-OPL_O37_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-OPR_O38:

OPR_O38 OPR - Population/Location-Based Laboratory Order Acknowledgment Message (S4.4.17).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OPR_O38.OPR_O38
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`OPR_O38_RESPONSE <hl7-v2_8_1-OPR_O38_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-OPU_R25:

OPU_R25 OPU - Unsolicited Population/Location-Based Laboratory Observation Message (S7.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OPU_R25.OPU_R25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PV1``
     - :ref:`PV1 <hl7-v2_8_1-PV1>`
     - required
     - Patient Visit
   * - ``PV2``
     - Optional[:ref:`PV2 <hl7-v2_8_1-PV2>`]
     - optional
     - Patient Visit - Additional Information
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``PATIENT_VISIT_OBSERVATION``
     - Optional[List[:ref:`OPU_R25_PATIENT_VISIT_OBSERVATION <hl7-v2_8_1-OPU_R25_PATIENT_VISIT_OBSERVATION>`]]
     - optional
     - PATIENT_VISIT_OBSERVATION
   * - ``ACCESSION_DETAIL``
     - List[:ref:`OPU_R25_ACCESSION_DETAIL <hl7-v2_8_1-OPU_R25_ACCESSION_DETAIL>`]
     - required
     - ACCESSION_DETAIL

.. _hl7-v2_8_1-ORA_R33:

ORA_R33 ORA - Observation Report Acknowledgement (S7.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORA_R33.ORA_R33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``ORC``
     - Optional[:ref:`ORC <hl7-v2_8_1-ORC>`]
     - optional
     - Common Order

.. _hl7-v2_8_1-ORA_R41:

ORA_R41 Observation Report Alert Acknowledgement (S7.3.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORA_R41.ORA_R41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information

.. _hl7-v2_8_1-ORB_O28:

ORB_O28 ORB - Blood product order acknowledgment (S4.13.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORB_O28.ORB_O28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORB_O28_RESPONSE <hl7-v2_8_1-ORB_O28_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORD_O04:

ORD_O04 ORD - Diet order acknowledgment (S4.7.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORD_O04.ORD_O04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORD_O04_RESPONSE <hl7-v2_8_1-ORD_O04_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORG_O20:

ORG_O20 ORG/ORL - General clinical order response (S4.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORG_O20.ORG_O20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORG_O20_RESPONSE <hl7-v2_8_1-ORG_O20_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORI_O24:

ORI_O24 ORI - Imaging order response message to any OMI (S4.4.15).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORI_O24.ORI_O24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORI_O24_RESPONSE <hl7-v2_8_1-ORI_O24_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O22:

ORL_O22 ORL - General laboratory order response message to any OML (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O22.ORL_O22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O22_RESPONSE <hl7-v2_8_1-ORL_O22_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O34:

ORL_O34 ORL - Laboratory order response message to a multiple order related to single sp (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O34.ORL_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O34_RESPONSE <hl7-v2_8_1-ORL_O34_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O36:

ORL_O36 ORL - Laboratory order response message to a single container of a specimen OML (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O36.ORL_O36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O36_RESPONSE <hl7-v2_8_1-ORL_O36_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O40:

ORL_O40 Specimen Shipment Centric Laboratory Order Acknowledgment Message (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O40.ORL_O40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O40_RESPONSE <hl7-v2_8_1-ORL_O40_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O41:

ORL_O41 DBC - Create Donor Record Message (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O41.ORL_O41
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O41_RESPONSE <hl7-v2_8_1-ORL_O41_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O42:

ORL_O42 DBU - Update Donor Record Message (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O42.ORL_O42
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O42_RESPONSE <hl7-v2_8_1-ORL_O42_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O43:

ORL_O43 General Order Message with Document Payload Acknowledgement Message (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O43.ORL_O43
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O43_RESPONSE <hl7-v2_8_1-ORL_O43_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORL_O44:

ORL_O44 Donor Registration - Minimal Message (S4.4.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORL_O44.ORL_O44
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORL_O44_RESPONSE <hl7-v2_8_1-ORL_O44_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORN_O08:

ORN_O08 ORN - Non-stock requisition acknowledgment (S4.10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORN_O08.ORN_O08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORN_O08_RESPONSE <hl7-v2_8_1-ORN_O08_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORP_O10:

ORP_O10 ORP - Pharmacy/treatment order acknowledgment (S4.A.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORP_O10.ORP_O10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORP_O10_RESPONSE <hl7-v2_8_1-ORP_O10_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORS_O06:

ORS_O06 ORS - Stock requisition acknowledgment (S4.10.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORS_O06.ORS_O06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORS_O06_RESPONSE <hl7-v2_8_1-ORS_O06_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-ORU_R01:

ORU_R01 ORU/ACK - Unsolicited transmission of an observation message (S7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R01.ORU_R01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_8_1-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-ORU_R30:

ORU_R30 ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Pla (S7.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R30.ORU_R30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``PATIENT_OBSERVATION``
     - Optional[List[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8_1-ORU_R30_PATIENT_OBSERVATION>`]]
     - optional
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_8_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_8_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-ORU_R31:

ORU_R31 ORU - Unsolicited New Point-Of-Care Observation Message - Search For An Order (S7.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R31.ORU_R31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``PATIENT_OBSERVATION``
     - Optional[List[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8_1-ORU_R30_PATIENT_OBSERVATION>`]]
     - optional
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_8_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_8_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-ORU_R32:

ORU_R32 ORU - Unsolicited Pre-Ordered Point-Of-Care Observation (S7.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R32.ORU_R32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``PATIENT_OBSERVATION``
     - Optional[List[:ref:`ORU_R30_PATIENT_OBSERVATION <hl7-v2_8_1-ORU_R30_PATIENT_OBSERVATION>`]]
     - optional
     - PATIENT_OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`ORU_R30_VISIT <hl7-v2_8_1-ORU_R30_VISIT>`]
     - optional
     - VISIT
   * - ``ORC``
     - :ref:`ORC <hl7-v2_8_1-ORC>`
     - required
     - Common Order
   * - ``OBR``
     - :ref:`OBR <hl7-v2_8_1-OBR>`
     - required
     - Observation Request
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``TIMING_QTY``
     - Optional[List[:ref:`ORU_R30_TIMING_QTY <hl7-v2_8_1-ORU_R30_TIMING_QTY>`]]
     - optional
     - TIMING_QTY
   * - ``OBSERVATION``
     - List[:ref:`ORU_R30_OBSERVATION <hl7-v2_8_1-ORU_R30_OBSERVATION>`]
     - required
     - OBSERVATION

.. _hl7-v2_8_1-ORU_R40:

ORU_R40 ORU - Unsolicited Report Alarm (S7.3.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORU_R40.ORU_R40
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PATIENT_RESULT``
     - List[:ref:`ORU_R01_PATIENT_RESULT <hl7-v2_8_1-ORU_R01_PATIENT_RESULT>`]
     - required
     - PATIENT_RESULT
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-ORX_O58:

ORX_O58 HL7 v2 ORX_O58 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.ORX_O58.ORX_O58
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`ORX_O58_RESPONSE <hl7-v2_8_1-ORX_O58_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-OSM_R26:

OSM_R26 OSM - Unsolicited Specimen Shipment Manifest Message (S7.18.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OSM_R26.OSM_R26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SHIPMENT``
     - List[:ref:`OSM_R26_SHIPMENT <hl7-v2_8_1-OSM_R26_SHIPMENT>`]
     - required
     - SHIPMENT

.. _hl7-v2_8_1-OSU_O51:

OSU_O51 HL7 v2 OSU_O51 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OSU_O51.OSU_O51
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     - Patient Identification
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``ORDER_STATUS``
     - List[:ref:`OSU_O51_ORDER_STATUS <hl7-v2_8_1-OSU_O51_ORDER_STATUS>`]
     - required
     - ORDER_STATUS

.. _hl7-v2_8_1-OUL_R22:

OUL_R22 OUL - Unsolicited Specimen Oriented Observation Message (S7.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R22.OUL_R22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OUL_R22_PATIENT <hl7-v2_8_1-OUL_R22_PATIENT>`]
     - optional
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``SPECIMEN``
     - List[:ref:`OUL_R22_SPECIMEN <hl7-v2_8_1-OUL_R22_SPECIMEN>`]
     - required
     - SPECIMEN
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-OUL_R23:

OUL_R23 OUL - Unsolicited Specimen Container Oriented Observation Message (S7.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R23.OUL_R23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OUL_R23_PATIENT <hl7-v2_8_1-OUL_R23_PATIENT>`]
     - optional
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``SPECIMEN``
     - List[:ref:`OUL_R23_SPECIMEN <hl7-v2_8_1-OUL_R23_SPECIMEN>`]
     - required
     - SPECIMEN
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-OUL_R24:

OUL_R24 OUL - Unsolicited Order Oriented Observation Message (S7.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.OUL_R24.OUL_R24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[:ref:`NTE <hl7-v2_8_1-NTE>`]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`OUL_R24_PATIENT <hl7-v2_8_1-OUL_R24_PATIENT>`]
     - optional
     - PATIENT
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``ORDER``
     - List[:ref:`OUL_R24_ORDER <hl7-v2_8_1-OUL_R24_ORDER>`]
     - required
     - ORDER
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-PEX_P07:

PEX_P07 PEX - Unsolicited initial individual product experience report (S7.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PEX_P07.PEX_P07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_8_1-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_8_1-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_8_1-PEX_P08:

PEX_P08 PEX - Unsolicited update individual product experience report (S7.11.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PEX_P08.PEX_P08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``VISIT``
     - Optional[:ref:`PEX_P07_VISIT <hl7-v2_8_1-PEX_P07_VISIT>`]
     - optional
     - VISIT
   * - ``EXPERIENCE``
     - List[:ref:`PEX_P07_EXPERIENCE <hl7-v2_8_1-PEX_P07_EXPERIENCE>`]
     - required
     - EXPERIENCE

.. _hl7-v2_8_1-PGL_PC6:

PGL_PC6 PGL - PC/ goal add (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PGL_PC6.PGL_PC6
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_8_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_8_1-PGL_PC7:

PGL_PC7 PGL - PC/ goal update (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PGL_PC7.PGL_PC7
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_8_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_8_1-PGL_PC8:

PGL_PC8 PGL - PC/ goal delete (S12.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PGL_PC8.PGL_PC8
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PGL_PC6_PATIENT_VISIT <hl7-v2_8_1-PGL_PC6_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GOAL``
     - List[:ref:`PGL_PC6_GOAL <hl7-v2_8_1-PGL_PC6_GOAL>`]
     - required
     - GOAL

.. _hl7-v2_8_1-PMU_B01:

PMU_B01 PMU/ACK - Add personnel record (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B01.PMU_B01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     - Practitioner Organization Unit
   * - ``AFF``
     - Optional[List[:ref:`AFF <hl7-v2_8_1-AFF>`]]
     - optional
     - Professional Affiliation
   * - ``LAN``
     - Optional[List[:ref:`LAN <hl7-v2_8_1-LAN>`]]
     - optional
     - Language Detail
   * - ``EDU``
     - Optional[List[:ref:`EDU <hl7-v2_8_1-EDU>`]]
     - optional
     - Educational Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_8_1-CER>`]]
     - optional
     - Certificate Detail
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role

.. _hl7-v2_8_1-PMU_B02:

PMU_B02 PMU/ACK - Update personnel record (S15.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B02.PMU_B02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     - Practitioner Organization Unit
   * - ``AFF``
     - Optional[List[:ref:`AFF <hl7-v2_8_1-AFF>`]]
     - optional
     - Professional Affiliation
   * - ``LAN``
     - Optional[List[:ref:`LAN <hl7-v2_8_1-LAN>`]]
     - optional
     - Language Detail
   * - ``EDU``
     - Optional[List[:ref:`EDU <hl7-v2_8_1-EDU>`]]
     - optional
     - Educational Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_8_1-CER>`]]
     - optional
     - Certificate Detail
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``PRT``
     - Optional[List[:ref:`PRT <hl7-v2_8_1-PRT>`]]
     - optional
     - Participation Information
   * - ``ROL``
     - Optional[List[:ref:`ROL <hl7-v2_8_1-ROL>`]]
     - optional
     - Role

.. _hl7-v2_8_1-PMU_B03:

PMU_B03 PMU/ACK - Delete personnel re cord (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B03.PMU_B03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification

.. _hl7-v2_8_1-PMU_B04:

PMU_B04 PMU/ACK - Active practicing person (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B04.PMU_B04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_8_1-PMU_B05:

PMU_B05 PMU/ACK - Deactivate practicing person (S15.3.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B05.PMU_B05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_8_1-PMU_B06:

PMU_B06 PMU/ACK - Terminate practicing person (S15.3.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B06.PMU_B06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[List[:ref:`PRA <hl7-v2_8_1-PRA>`]]
     - optional
     - Practitioner Detail
   * - ``ORG``
     - Optional[List[:ref:`ORG <hl7-v2_8_1-ORG>`]]
     - optional
     - Practitioner Organization Unit

.. _hl7-v2_8_1-PMU_B07:

PMU_B07 PMU/ACK - Grant Certificate/Permission (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B07.PMU_B07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_8_1-PRA>`]
     - optional
     - Practitioner Detail
   * - ``CERTIFICATE``
     - Optional[List[:ref:`PMU_B07_CERTIFICATE <hl7-v2_8_1-PMU_B07_CERTIFICATE>`]]
     - optional
     - CERTIFICATE

.. _hl7-v2_8_1-PMU_B08:

PMU_B08 PMU/ACK - Revoke Certificate/Permission (S15.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PMU_B08.PMU_B08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EVN``
     - :ref:`EVN <hl7-v2_8_1-EVN>`
     - required
     - Event Type
   * - ``STF``
     - :ref:`STF <hl7-v2_8_1-STF>`
     - required
     - Staff Identification
   * - ``PRA``
     - Optional[:ref:`PRA <hl7-v2_8_1-PRA>`]
     - optional
     - Practitioner Detail
   * - ``CER``
     - Optional[List[:ref:`CER <hl7-v2_8_1-CER>`]]
     - optional
     - Certificate Detail

.. _hl7-v2_8_1-PPG_PCG:

PPG_PCG PPG - PC/ pathway (goal-oriented) add (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPG_PCG.PPG_PCG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_8_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPG_PCH:

PPG_PCH PPG - PC/ pathway (goal-oriented) update (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPG_PCH.PPG_PCH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_8_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPG_PCJ:

PPG_PCJ PPG - PC/ pathway (goal-oriented) delete (S12.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPG_PCJ.PPG_PCJ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPG_PCG_PATIENT_VISIT <hl7-v2_8_1-PPG_PCG_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPG_PCG_PATHWAY <hl7-v2_8_1-PPG_PCG_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPP_PCB:

PPP_PCB PPP - PC/ pathway (problem-oriented) add (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPP_PCB.PPP_PCB
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_8_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPP_PCC:

PPP_PCC PPP - PC/ pathway (problem-oriented) update (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPP_PCC.PPP_PCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_8_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPP_PCD:

PPP_PCD PPP - PC/ pathway (problem-oriented) delete (S12.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPP_PCD.PPP_PCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPP_PCB_PATIENT_VISIT <hl7-v2_8_1-PPP_PCB_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PATHWAY``
     - List[:ref:`PPP_PCB_PATHWAY <hl7-v2_8_1-PPP_PCB_PATHWAY>`]
     - required
     - PATHWAY

.. _hl7-v2_8_1-PPR_PC1:

PPR_PC1 PPR - PC/ problem add (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPR_PC1.PPR_PC1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_8_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_8_1-PPR_PC2:

PPR_PC2 PPR - PC/ problem update (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPR_PC2.PPR_PC2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_8_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_8_1-PPR_PC3:

PPR_PC3 PPR - PC/ problem delete (S12.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.PPR_PC3.PPR_PC3
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PATIENT_VISIT``
     - Optional[:ref:`PPR_PC1_PATIENT_VISIT <hl7-v2_8_1-PPR_PC1_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``PROBLEM``
     - List[:ref:`PPR_PC1_PROBLEM <hl7-v2_8_1-PPR_PC1_PROBLEM>`]
     - required
     - PROBLEM

.. _hl7-v2_8_1-QBP_E03:

QBP_E03 HealthCare Services Invoice Status (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_E03.QBP_E03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``QUERY_INFORMATION``
     - :ref:`QBP_E03_QUERY_INFORMATION <hl7-v2_8_1-QBP_E03_QUERY_INFORMATION>`
     - required
     - QUERY_INFORMATION

.. _hl7-v2_8_1-QBP_E22:

QBP_E22 Authorization Request Status (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_E22.QBP_E22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``QUERY``
     - :ref:`QBP_E22_QUERY <hl7-v2_8_1-QBP_E22_QUERY>`
     - required
     - QUERY

.. _hl7-v2_8_1-QBP_O33:

QBP_O33 OML - Laboratory order for multiple orders related to a single specimen (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_O33.QBP_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_8_1-QBP_O34:

QBP_O34 ORL - Laboratory order response message to a multiple order related to single sp (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_O34.QBP_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_8_1-QBP_Q11:

QBP_Q11 QBP - Query by parameter requesting an RSP segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q11.QBP_Q11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q13:

QBP_Q13 HL7 v2 QBP_Q13 message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q13.QBP_Q13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``PID``
     - Optional[:ref:`PID <hl7-v2_8_1-PID>`]
     - optional
     - Patient Identification
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_8_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q15:

QBP_Q15 QBP - Query by parameter requesting an RDY display response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q15.QBP_Q15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q21:

QBP_Q21 QBP - Get person demographics (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q21.QBP_Q21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q22:

QBP_Q22 QBP - Find candidates (S3.3.57).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q22.QBP_Q22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q23:

QBP_Q23 QBP - Get corresponding identifiers (S3.3.58).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q23.QBP_Q23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q24:

QBP_Q24 QBP - Allocate identifiers (S3.3.59).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q24.QBP_Q24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q25:

QBP_Q25 QBP - Personnel Information by Segment Query (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q25.QBP_Q25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q31:

QBP_Q31 QBP Query Dispense history (S4.A.20).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q31.QBP_Q31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q32:

QBP_Q32 Find Candidates including Visit Information (S3.3.63).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q32.QBP_Q32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Q33:

QBP_Q33 (S4.16.6).
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q33.QBP_Q33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_8_1-QBP_Q34:

QBP_Q34 (S4.16.8).
~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Q34.QBP_Q34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_8_1-QBP_Qnn:

QBP_Qnn HL7 v2 QBP_Qnn message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Qnn.QBP_Qnn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RDF``
     - Optional[:ref:`RDF <hl7-v2_8_1-RDF>`]
     - optional
     - Table Row Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Z73:

QBP_Z73 Query by parameter (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Z73.QBP_Z73
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter

.. _hl7-v2_8_1-QBP_Z87:

QBP_Z87 (S5.9.2.1.1).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Z87.QBP_Z87
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Z89:

QBP_Z89 (S5.9.2.4).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Z89.QBP_Z89
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QBP_Znn:

QBP_Znn (S5.3.2.3).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QBP_Znn.QBP_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QBP_Q11_QBP <hl7-v2_8_1-QBP_Q11_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QCN_J01:

QCN_J01 QCN/ACK - Cancel query/acknowledge message (S5.4.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QCN_J01.QCN_J01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QID``
     - :ref:`QID <hl7-v2_8_1-QID>`
     - required
     - Query Identification

.. _hl7-v2_8_1-QCN_J02:

QCN_J02 QSX/ACK - Cancel subscription/acknowledge message (S5.4.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QCN_J02.QCN_J02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QID``
     - :ref:`QID <hl7-v2_8_1-QID>`
     - required
     - Query Identification

.. _hl7-v2_8_1-QSB_Q16:

QSB_Q16 QSB - Create subscription (S5.4.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QSB_Q16.QSB_Q16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QSB_Z83:

QSB_Z83 (S5.7.3.1).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QSB_Z83.QSB_Z83
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-QVR_Q17:

QVR_Q17 QVR - Query for previous events (S5.4.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.QVR_Q17.QVR_Q17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QBP``
     - Optional[:ref:`QVR_Q17_QBP <hl7-v2_8_1-QVR_Q17_QBP>`]
     - optional
     - QBP
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RAS_O17:

RAS_O17 RAS - Pharmacy/treatment administration (S4.A.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RAS_O17.RAS_O17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RAS_O17_PATIENT <hl7-v2_8_1-RAS_O17_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RAS_O17_ORDER <hl7-v2_8_1-RAS_O17_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-RDE_O11:

RDE_O11 RDE - Pharmacy/treatment encoded order (S4.A.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDE_O11.RDE_O11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_8_1-RDE_O11_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDE_O11_ORDER <hl7-v2_8_1-RDE_O11_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-RDE_O25:

RDE_O25 RDE - Pharmacy/treatment refill authorization request (S4.A.13).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDE_O25.RDE_O25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDE_O11_PATIENT <hl7-v2_8_1-RDE_O11_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDE_O11_ORDER <hl7-v2_8_1-RDE_O11_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-RDR_RDR:

RDR_RDR Pharmacy/treatment dispense information (S5.9.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDR_RDR.RDR_RDR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[:ref:`SFT <hl7-v2_8_1-SFT>`]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``DEFINITION``
     - List[:ref:`RDR_RDR_DEFINITION <hl7-v2_8_1-RDR_RDR_DEFINITION>`]
     - required
     - DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RDS_O13:

RDS_O13 RDS - Pharmacy/treatment dispense (S4.A.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDS_O13.RDS_O13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RDS_O13_PATIENT <hl7-v2_8_1-RDS_O13_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RDS_O13_ORDER <hl7-v2_8_1-RDS_O13_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-RDY_K15:

RDY_K15 RDY - Display response in response to QBP^Q15 (S5.3.2.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDY_K15.RDY_K15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RDY_Z80:

RDY_Z80 Display based response (S5.3.2.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDY_Z80.RDY_Z80
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RDY_Z98:

RDY_Z98 (S5.9.5.1).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RDY_Z98.RDY_Z98
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-REF_I12:

REF_I12 REF/RRI - Patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.REF_I12.REF_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT2``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-REF_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_8_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_8_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_8_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_8_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-REF_I13:

REF_I13 REF/RRI - Modify patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.REF_I13.REF_I13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT2``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-REF_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_8_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_8_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_8_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_8_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-REF_I14:

REF_I14 REF/RRI - Cancel patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.REF_I14.REF_I14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT2``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-REF_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_8_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_8_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_8_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_8_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-REF_I15:

REF_I15 REF/RRI - Request patient referral status (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.REF_I15.REF_I15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT2``
     - Optional[:ref:`REF_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-REF_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - List[:ref:`REF_I12_PROVIDER_CONTACT <hl7-v2_8_1-REF_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`REF_I12_INSURANCE <hl7-v2_8_1-REF_I12_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`REF_I12_PROCEDURE <hl7-v2_8_1-REF_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`REF_I12_OBSERVATION <hl7-v2_8_1-REF_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`REF_I12_PATIENT_VISIT <hl7-v2_8_1-REF_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RGV_O15:

RGV_O15 RGV - Pharmacy/treatment give (S4.A.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RGV_O15.RGV_O15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[:ref:`RGV_O15_PATIENT <hl7-v2_8_1-RGV_O15_PATIENT>`]
     - optional
     - PATIENT
   * - ``ORDER``
     - List[:ref:`RGV_O15_ORDER <hl7-v2_8_1-RGV_O15_ORDER>`]
     - required
     - ORDER

.. _hl7-v2_8_1-RPA_I08:

RPA_I08 RQA/RPA - Request for treatment authorization information (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RPA_I08.RPA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RPA_I08_AUTHORIZATION <hl7-v2_8_1-RPA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RPA_I08_PROVIDER <hl7-v2_8_1-RPA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`RPA_I08_INSURANCE <hl7-v2_8_1-RPA_I08_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - List[:ref:`RPA_I08_PROCEDURE <hl7-v2_8_1-RPA_I08_PROCEDURE>`]
     - required
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RPA_I08_OBSERVATION <hl7-v2_8_1-RPA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RPA_I08_VISIT <hl7-v2_8_1-RPA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RPI_I01:

RPI_I01 RQI/RPI - Request for insurance information (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RPI_I01.RPI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPI_I01_PROVIDER <hl7-v2_8_1-RPI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RPI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RPI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RPI_I04:

RPI_I04 RQD/RPI - Request for patient demographic data (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RPI_I04.RPI_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPI_I04_PROVIDER <hl7-v2_8_1-RPI_I04_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RPI_I04_GUARANTOR_INSURANCE <hl7-v2_8_1-RPI_I04_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RPL_I02:

RPL_I02 RQI/RPL - Request/receipt of patient selection display list (S11.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RPL_I02.RPL_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPL_I02_PROVIDER <hl7-v2_8_1-RPL_I02_PROVIDER>`]
     - required
     - PROVIDER
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``DSP``
     - Optional[List[:ref:`DSP <hl7-v2_8_1-DSP>`]]
     - optional
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RPR_I03:

RPR_I03 RQI/RPR - Request/receipt of patient selection list (S11.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RPR_I03.RPR_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``PROVIDER``
     - List[:ref:`RPR_I03_PROVIDER <hl7-v2_8_1-RPR_I03_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - Optional[List[:ref:`PID <hl7-v2_8_1-PID>`]]
     - optional
     - Patient Identification
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQA_I08:

RQA_I08 RQA/RPA - Request for treatment authorization information (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQA_I08.RQA_I08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_8_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_8_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_8_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_8_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_8_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQA_I09:

RQA_I09 RQA/RPA - Request for modification to an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQA_I09.RQA_I09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_8_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_8_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_8_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_8_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_8_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQA_I10:

RQA_I10 RQA/RPA - Request for resubmission of an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQA_I10.RQA_I10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_8_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_8_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_8_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_8_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_8_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQA_I11:

RQA_I11 RQA/RPA - Request for cancellation of an authorization (S11.4.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQA_I11.RQA_I11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION``
     - Optional[:ref:`RQA_I08_AUTHORIZATION <hl7-v2_8_1-RQA_I08_AUTHORIZATION>`]
     - optional
     - AUTHORIZATION
   * - ``PROVIDER``
     - List[:ref:`RQA_I08_PROVIDER <hl7-v2_8_1-RQA_I08_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQA_I08_GUARANTOR_INSURANCE <hl7-v2_8_1-RQA_I08_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RQA_I08_PROCEDURE <hl7-v2_8_1-RQA_I08_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RQA_I08_OBSERVATION <hl7-v2_8_1-RQA_I08_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``VISIT``
     - Optional[:ref:`RQA_I08_VISIT <hl7-v2_8_1-RQA_I08_VISIT>`]
     - optional
     - VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQI_I01:

RQI_I01 RQI/RPI - Request for insurance information (S11.3.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQI_I01.RQI_I01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_8_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQI_I02:

RQI_I02 RQI/RPL - Request/receipt of patient selection display list (S11.3.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQI_I02.RQI_I02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_8_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQI_I03:

RQI_I03 RQI/RPR - Request/receipt of patient selection list (S11.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQI_I03.RQI_I03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_8_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQI_I07:

RQI_I07 PIN/ACK - Unsolicited insurance information (S11.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQI_I07.RQI_I07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PROVIDER``
     - List[:ref:`RQI_I01_PROVIDER <hl7-v2_8_1-RQI_I01_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GUARANTOR_INSURANCE``
     - Optional[:ref:`RQI_I01_GUARANTOR_INSURANCE <hl7-v2_8_1-RQI_I01_GUARANTOR_INSURANCE>`]
     - optional
     - GUARANTOR_INSURANCE
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RQP_I04:

RQP_I04 RQD/RPI - Request for patient demographic data (S11.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RQP_I04.RQP_I04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PROVIDER``
     - List[:ref:`RQP_I04_PROVIDER <hl7-v2_8_1-RQP_I04_PROVIDER>`]
     - required
     - PROVIDER
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RRA_O18:

RRA_O18 RRA - Pharmacy/treatment administration acknowledgment (S4.A.12).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRA_O18.RRA_O18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRA_O18_RESPONSE <hl7-v2_8_1-RRA_O18_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-RRD_O14:

RRD_O14 RRD - Pharmacy/treatment dispense acknowledgment (S4.A.8).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRD_O14.RRD_O14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRD_O14_RESPONSE <hl7-v2_8_1-RRD_O14_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-RRE_O12:

RRE_O12 RRE - Pharmacy/treatment encoded order acknowledgment (S4.A.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRE_O12.RRE_O12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_8_1-RRE_O12_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-RRE_O26:

RRE_O26 RRE - Pharmacy/Treatment Refill Authorization Acknowledgement (S4.A.14).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRE_O26.RRE_O26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRE_O12_RESPONSE <hl7-v2_8_1-RRE_O12_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-RRG_O16:

RRG_O16 RRG - Pharmacy/treatment give acknowledgment (S4.A.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRG_O16.RRG_O16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``RESPONSE``
     - Optional[:ref:`RRG_O16_RESPONSE <hl7-v2_8_1-RRG_O16_RESPONSE>`]
     - optional
     - RESPONSE

.. _hl7-v2_8_1-RRI_I12:

RRI_I12 REF/RRI - Patient referral (S11.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RRI_I12.RRI_I12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - Optional[:ref:`MSA <hl7-v2_8_1-MSA>`]
     - optional
     - Message Acknowledgment
   * - ``RF1``
     - Optional[:ref:`RF1 <hl7-v2_8_1-RF1>`]
     - optional
     - Referral Information
   * - ``AUTHORIZATION_CONTACT2``
     - Optional[:ref:`RRI_I12_AUTHORIZATION_CONTACT2 <hl7-v2_8_1-RRI_I12_AUTHORIZATION_CONTACT2>`]
     - optional
     - AUTHORIZATION_CONTACT2
   * - ``PROVIDER_CONTACT``
     - List[:ref:`RRI_I12_PROVIDER_CONTACT <hl7-v2_8_1-RRI_I12_PROVIDER_CONTACT>`]
     - required
     - PROVIDER_CONTACT
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``ACC``
     - Optional[:ref:`ACC <hl7-v2_8_1-ACC>`]
     - optional
     - Accident
   * - ``DG1``
     - Optional[List[:ref:`DG1 <hl7-v2_8_1-DG1>`]]
     - optional
     - Diagnosis
   * - ``DRG``
     - Optional[List[:ref:`DRG <hl7-v2_8_1-DRG>`]]
     - optional
     - Diagnosis Related Group
   * - ``AL1``
     - Optional[List[:ref:`AL1 <hl7-v2_8_1-AL1>`]]
     - optional
     - Patient Allergy Information
   * - ``PROCEDURE``
     - Optional[List[:ref:`RRI_I12_PROCEDURE <hl7-v2_8_1-RRI_I12_PROCEDURE>`]]
     - optional
     - PROCEDURE
   * - ``OBSERVATION``
     - Optional[List[:ref:`RRI_I12_OBSERVATION <hl7-v2_8_1-RRI_I12_OBSERVATION>`]]
     - optional
     - OBSERVATION
   * - ``PATIENT_VISIT``
     - Optional[:ref:`RRI_I12_PATIENT_VISIT <hl7-v2_8_1-RRI_I12_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments

.. _hl7-v2_8_1-RSP_E03:

RSP_E03 HealthCare Services Invoice Status (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_E03.RSP_E03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``QUERY_ACK_IPR``
     - :ref:`RSP_E03_QUERY_ACK_IPR <hl7-v2_8_1-RSP_E03_QUERY_ACK_IPR>`
     - required
     - QUERY_ACK_IPR

.. _hl7-v2_8_1-RSP_E22:

RSP_E22 Authorization Request Status (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_E22.RSP_E22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[List[:ref:`UAC <hl7-v2_8_1-UAC>`]]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``QUERY_ACK``
     - :ref:`RSP_E22_QUERY_ACK <hl7-v2_8_1-RSP_E22_QUERY_ACK>`
     - required
     - QUERY_ACK

.. _hl7-v2_8_1-RSP_K11:

RSP_K11 RSP - Segment pattern response in response to QBP^Q11 (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K11.RSP_K11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``SEGMENT_PATTERN``
     - Optional[:ref:`RSP_K11_SEGMENT_PATTERN <hl7-v2_8_1-RSP_K11_SEGMENT_PATTERN>`]
     - optional
     - SEGMENT_PATTERN
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K21:

RSP_K21 RSP - Get person demographics response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K21.RSP_K21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K21_QUERY_RESPONSE <hl7-v2_8_1-RSP_K21_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K22:

RSP_K22 RSP - Find candidates response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K22.RSP_K22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[List[:ref:`RSP_K22_QUERY_RESPONSE <hl7-v2_8_1-RSP_K22_QUERY_RESPONSE>`]]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K23:

RSP_K23 RSP - Get corresponding identifiers response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K23.RSP_K23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_8_1-RSP_K23_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K24:

RSP_K24 RSP - Allocate identifiers response (S3.3.59).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K24.RSP_K24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[:ref:`RSP_K23_QUERY_RESPONSE <hl7-v2_8_1-RSP_K23_QUERY_RESPONSE>`]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K25:

RSP_K25 RSP - Personnel Information by Segment Response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K25.RSP_K25
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``STAFF``
     - List[:ref:`RSP_K25_STAFF <hl7-v2_8_1-RSP_K25_STAFF>`]
     - required
     - STAFF
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K31:

RSP_K31 RSP -Dispense History Response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K31.RSP_K31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``RESPONSE``
     - List[:ref:`RSP_K31_RESPONSE <hl7-v2_8_1-RSP_K31_RESPONSE>`]
     - required
     - RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K32:

RSP_K32 Find Candidates including Visit Information Response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K32.RSP_K32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - Optional[List[:ref:`RSP_K32_QUERY_RESPONSE <hl7-v2_8_1-RSP_K32_QUERY_RESPONSE>`]]
     - optional
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_K33:

RSP_K33 Get Donor Record Candidates Response Message (S4.16.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K33.RSP_K33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DONOR``
     - Optional[:ref:`RSP_O33_DONOR <hl7-v2_8_1-RSP_O33_DONOR>`]
     - optional
     - DONOR

.. _hl7-v2_8_1-RSP_K34:

RSP_K34 Segment Pattern Response Message (S4.16.9).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_K34.RSP_K34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DONOR``
     - Optional[:ref:`RSP_O34_DONOR <hl7-v2_8_1-RSP_O34_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION``
     - Optional[:ref:`RSP_O34_DONATION <hl7-v2_8_1-RSP_O34_DONATION>`]
     - optional
     - DONATION

.. _hl7-v2_8_1-RSP_O33:

RSP_O33 OML - Laboratory order for multiple orders related to a single specimen (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_O33.RSP_O33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DONOR``
     - Optional[:ref:`RSP_O33_DONOR <hl7-v2_8_1-RSP_O33_DONOR>`]
     - optional
     - DONOR

.. _hl7-v2_8_1-RSP_O34:

RSP_O34 ORL - Laboratory order response message to a multiple order related to single sp (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_O34.RSP_O34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DONOR``
     - Optional[:ref:`RSP_O34_DONOR <hl7-v2_8_1-RSP_O34_DONOR>`]
     - optional
     - DONOR
   * - ``DONATION``
     - Optional[:ref:`RSP_O34_DONATION <hl7-v2_8_1-RSP_O34_DONATION>`]
     - optional
     - DONATION

.. _hl7-v2_8_1-RSP_Z82:

RSP_Z82 Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z82.RSP_Z82
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z82_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z82_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_Z84:

RSP_Z84 Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z84.RSP_Z84
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RSP_Z84_ROW_DEFINITION <hl7-v2_8_1-RSP_Z84_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_Z86:

RSP_Z86 Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z86.RSP_Z86
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z86_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z86_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_Z88:

RSP_Z88 Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z88.RSP_Z88
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z88_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z88_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8_1-DSC>`
     - required
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_Z90:

RSP_Z90 Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Z90.RSP_Z90
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``RCP``
     - :ref:`RCP <hl7-v2_8_1-RCP>`
     - required
     - Response Control Parameter
   * - ``QUERY_RESPONSE``
     - List[:ref:`RSP_Z90_QUERY_RESPONSE <hl7-v2_8_1-RSP_Z90_QUERY_RESPONSE>`]
     - required
     - QUERY_RESPONSE
   * - ``DSC``
     - :ref:`DSC <hl7-v2_8_1-DSC>`
     - required
     - Continuation Pointer

.. _hl7-v2_8_1-RSP_Znn:

RSP_Znn Segment pattern response (S15.3.7).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RSP_Znn.RSP_Znn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_K13:

RTB_K13 RTB - Tabular response in response to QBP^Q13 (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_K13.RTB_K13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Knn:

RTB_Knn HL7 v2 RTB_Knn message.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Knn.RTB_Knn
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z74:

RTB_Z74 Tabular response (S4.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z74.RTB_Z74
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_Z74_ROW_DEFINITION <hl7-v2_8_1-RTB_Z74_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z76:

RTB_Z76 (S5.9.7.2).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z76.RTB_Z76
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z78:

RTB_Z78 (S5.9.7.1).
~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z78.RTB_Z78
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z92:

RTB_Z92 (S5.9.3.1.1).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z92.RTB_Z92
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z94:

RTB_Z94 (S5.9.3.2.1).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z94.RTB_Z94
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-RTB_Z96:

RTB_Z96 (S5.9.4.1.1).
~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.RTB_Z96.RTB_Z96
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[:ref:`ERR <hl7-v2_8_1-ERR>`]
     - optional
     - Error
   * - ``QAK``
     - :ref:`QAK <hl7-v2_8_1-QAK>`
     - required
     - Query Acknowledgment
   * - ``QPD``
     - :ref:`QPD <hl7-v2_8_1-QPD>`
     - required
     - Query Parameter Definition
   * - ``ROW_DEFINITION``
     - Optional[:ref:`RTB_K13_ROW_DEFINITION <hl7-v2_8_1-RTB_K13_ROW_DEFINITION>`]
     - optional
     - ROW_DEFINITION
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-SDR_S31:

SDR_S31 SDR/SDS - Request anti-microbial device data (S17.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S31.SDR_S31
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``ANTI_MICROBIAL_DEVICE_DATA``
     - :ref:`SDR_S31_ANTI_MICROBIAL_DEVICE_DATA <hl7-v2_8_1-SDR_S31_ANTI_MICROBIAL_DEVICE_DATA>`
     - required
     - ANTI_MICROBIAL_DEVICE_DATA

.. _hl7-v2_8_1-SDR_S32:

SDR_S32 SMD/SMS - Request anti-microbial device cycle data (S17.5.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S32.SDR_S32
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``ANTI_MICROBIAL_DEVICE_CYCLE_DATA``
     - :ref:`SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA <hl7-v2_8_1-SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA>`
     - required
     - ANTI_MICROBIAL_DEVICE_CYCLE_DATA

.. _hl7-v2_8_1-SDR_S36:

SDR_S36 SDN/ACK - Notification of anti-microbial device data (S17.6.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S36.SDR_S36
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``ANTI_MICROBIAL_DEVICE_DATA``
     - :ref:`SDR_S31_ANTI_MICROBIAL_DEVICE_DATA <hl7-v2_8_1-SDR_S31_ANTI_MICROBIAL_DEVICE_DATA>`
     - required
     - ANTI_MICROBIAL_DEVICE_DATA

.. _hl7-v2_8_1-SDR_S37:

SDR_S37 SCN/ACK - Notification of anti-microbial device cycle data (S17.6.5).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SDR_S37.SDR_S37
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``ANTI_MICROBIAL_DEVICE_CYCLE_DATA``
     - :ref:`SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA <hl7-v2_8_1-SDR_S32_ANTI_MICROBIAL_DEVICE_CYCLE_DATA>`
     - required
     - ANTI_MICROBIAL_DEVICE_CYCLE_DATA

.. _hl7-v2_8_1-SIU_S12:

SIU_S12 SIU/ACK - Notification of new appointment booking (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S12.SIU_S12
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S13:

SIU_S13 SIU/ACK - Notification of appointment rescheduling (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S13.SIU_S13
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S14:

SIU_S14 SIU/ACK - Notification of appointment modification (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S14.SIU_S14
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S15:

SIU_S15 SIU/ACK - Notification of appointment cancellation (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S15.SIU_S15
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S16:

SIU_S16 SIU/ACK - Notification of appointment discontinuation (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S16.SIU_S16
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S17:

SIU_S17 SIU/ACK - Notification of appointment deletion (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S17.SIU_S17
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S18:

SIU_S18 SIU/ACK - Notification of addition of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S18.SIU_S18
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S19:

SIU_S19 SIU/ACK - Notification of modification of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S19.SIU_S19
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S20:

SIU_S20 SIU/ACK - Notification of cancellation of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S20.SIU_S20
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S21:

SIU_S21 SIU/ACK - Notification of discontinuation of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S21.SIU_S21
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S22:

SIU_S22 SIU/ACK - Notification of deletion of service/resource on appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S22.SIU_S22
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S23:

SIU_S23 SIU/ACK - Notification of blocked schedule time slot(s) (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S23.SIU_S23
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S24:

SIU_S24 SIU/ACK - Notification of opened ("unblocked"") schedule time slot(s)" (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S24.SIU_S24
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S26:

SIU_S26 SIU/ACK Notification that patient did not show up for schedule appointment (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S26.SIU_S26
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SIU_S27:

SIU_S27 SIU/ACK - Broadcast Notification of Scheduled Appointments (S10.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SIU_S27.SIU_S27
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SCH``
     - :ref:`SCH <hl7-v2_8_1-SCH>`
     - required
     - Scheduling Activity Information
   * - ``TQ1``
     - Optional[List[:ref:`TQ1 <hl7-v2_8_1-TQ1>`]]
     - optional
     - Timing/Quantity
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SIU_S12_PATIENT <hl7-v2_8_1-SIU_S12_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SIU_S12_RESOURCES <hl7-v2_8_1-SIU_S12_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SLR_S28:

SLR_S28 SLR/SLS - Request new sterilization lot (S17.5.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S28.SLR_S28
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SLT``
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     - Sterilization Lot

.. _hl7-v2_8_1-SLR_S29:

SLR_S29 SLR/SLS - Request Sterilization lot deletion (S17.5.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S29.SLR_S29
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SLT``
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     - Sterilization Lot

.. _hl7-v2_8_1-SLR_S30:

SLR_S30 STI/STS - Request item (S17.5.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S30.SLR_S30
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SLT``
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     - Sterilization Lot

.. _hl7-v2_8_1-SLR_S34:

SLR_S34 SLN/ACK - Notification of sterilization lot (S17.6.2).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S34.SLR_S34
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SLT``
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     - Sterilization Lot

.. _hl7-v2_8_1-SLR_S35:

SLR_S35 SLN/ACK - Notification of sterilization lot deletion (S17.6.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SLR_S35.SLR_S35
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SLT``
     - List[:ref:`SLT <hl7-v2_8_1-SLT>`]
     - required
     - Sterilization Lot

.. _hl7-v2_8_1-SRM_S01:

SRM_S01 SRM/SRR - Request new appointment booking (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S01.SRM_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S02:

SRM_S02 SRM/SRR - Request appointment rescheduling (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S02.SRM_S02
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S03:

SRM_S03 SRM/SRR - Request appointment modification (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S03.SRM_S03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S04:

SRM_S04 SRM/SRR - Request appointment cancellation (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S04.SRM_S04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S05:

SRM_S05 SRM/SRR - Request appointment discontinuation (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S05.SRM_S05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S06:

SRM_S06 SRM/SRR - Request appointment deletion (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S06.SRM_S06
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S07:

SRM_S07 SRM/SRR - Request addition of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S07.SRM_S07
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S08:

SRM_S08 SRM/SRR - Request modification of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S08.SRM_S08
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S09:

SRM_S09 SRM/SRR - Request cancellation of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S09.SRM_S09
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S10:

SRM_S10 SRM/SRR - Request discontinuation of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S10.SRM_S10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRM_S11:

SRM_S11 SRM/SRR - Request deletion of service/resource on appointment (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRM_S11.SRM_S11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``ARQ``
     - :ref:`ARQ <hl7-v2_8_1-ARQ>`
     - required
     - Appointment Request
   * - ``APR``
     - Optional[:ref:`APR <hl7-v2_8_1-APR>`]
     - optional
     - Appointment Preferences
   * - ``NTE``
     - Optional[List[:ref:`NTE <hl7-v2_8_1-NTE>`]]
     - optional
     - Notes and Comments
   * - ``PATIENT``
     - Optional[List[:ref:`SRM_S01_PATIENT <hl7-v2_8_1-SRM_S01_PATIENT>`]]
     - optional
     - PATIENT
   * - ``RESOURCES``
     - List[:ref:`SRM_S01_RESOURCES <hl7-v2_8_1-SRM_S01_RESOURCES>`]
     - required
     - RESOURCES

.. _hl7-v2_8_1-SRR_S01:

SRR_S01 SRM/SRR - Request new appointment booking (S10.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SRR_S01.SRR_S01
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``MSA``
     - :ref:`MSA <hl7-v2_8_1-MSA>`
     - required
     - Message Acknowledgment
   * - ``ERR``
     - Optional[List[:ref:`ERR <hl7-v2_8_1-ERR>`]]
     - optional
     - Error
   * - ``SCHEDULE``
     - Optional[:ref:`SRR_S01_SCHEDULE <hl7-v2_8_1-SRR_S01_SCHEDULE>`]
     - optional
     - SCHEDULE

.. _hl7-v2_8_1-SSR_U04:

SSR_U04 SSR/ACK - specimen status request (S13.3.4).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SSR_U04.SSR_U04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``SPECIMEN_CONTAINER``
     - List[:ref:`SSR_U04_SPECIMEN_CONTAINER <hl7-v2_8_1-SSR_U04_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER

.. _hl7-v2_8_1-SSU_U03:

SSU_U03 SSU/ACK - Specimen status update (S13.3.3).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.SSU_U03.SSU_U03
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``SPECIMEN_CONTAINER``
     - List[:ref:`SSU_U03_SPECIMEN_CONTAINER <hl7-v2_8_1-SSU_U03_SPECIMEN_CONTAINER>`]
     - required
     - SPECIMEN_CONTAINER

.. _hl7-v2_8_1-STC_S33:

STC_S33 STC/ACK - Notification of sterilization configuration (S17.6.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.STC_S33.STC_S33
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``SCP``
     - List[:ref:`SCP <hl7-v2_8_1-SCP>`]
     - required
     - Sterilizer Configuration (Anti-Microbial Devices)

.. _hl7-v2_8_1-TCU_U10:

TCU_U10 TCU/ACK - Automated equipment test code settings update (S13.3.10).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.TCU_U10.TCU_U10
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``TEST_CONFIGURATION``
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_8_1-TCU_U10_TEST_CONFIGURATION>`]
     - required
     - TEST_CONFIGURATION

.. _hl7-v2_8_1-TCU_U11:

TCU_U11 TCR/ACK - Automated equipment test code settings request (S13.3.11).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.TCU_U11.TCU_U11
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``EQU``
     - :ref:`EQU <hl7-v2_8_1-EQU>`
     - required
     - Equipment Detail
   * - ``TEST_CONFIGURATION``
     - List[:ref:`TCU_U10_TEST_CONFIGURATION <hl7-v2_8_1-TCU_U10_TEST_CONFIGURATION>`]
     - required
     - TEST_CONFIGURATION

.. _hl7-v2_8_1-UDM_Q05:

UDM_Q05 UDM/ACK - Unsolicited display update message (S5.10.1.1).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.UDM_Q05.UDM_Q05
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``URD``
     - :ref:`URD <hl7-v2_8_1-URD>`
     - required
     - deprecated
   * - ``URS``
     - Optional[:ref:`URS <hl7-v2_8_1-URS>`]
     - optional
     - deprecated
   * - ``DSP``
     - List[:ref:`DSP <hl7-v2_8_1-DSP>`]
     - required
     - Display Data
   * - ``DSC``
     - Optional[:ref:`DSC <hl7-v2_8_1-DSC>`]
     - optional
     - Continuation Pointer

.. _hl7-v2_8_1-VXU_V04:

VXU_V04 VXU - Unsolicited vaccination record update (S4.A.6).
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:class:: hl7types.hl7.v2_8_1.messages.VXU_V04.VXU_V04
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - Type
     - Required
     - Description
   * - ``MSH``
     - :ref:`MSH <hl7-v2_8_1-MSH>`
     - required
     - Message Header
   * - ``SFT``
     - Optional[List[:ref:`SFT <hl7-v2_8_1-SFT>`]]
     - optional
     - Software Segment
   * - ``UAC``
     - Optional[:ref:`UAC <hl7-v2_8_1-UAC>`]
     - optional
     - User Authentication Credential Segment
   * - ``PID``
     - :ref:`PID <hl7-v2_8_1-PID>`
     - required
     - Patient Identification
   * - ``PD1``
     - Optional[:ref:`PD1 <hl7-v2_8_1-PD1>`]
     - optional
     - Patient Additional Demographic
   * - ``NK1``
     - Optional[List[:ref:`NK1 <hl7-v2_8_1-NK1>`]]
     - optional
     - Next of Kin / Associated Parties
   * - ``ARV``
     - Optional[List[:ref:`ARV <hl7-v2_8_1-ARV>`]]
     - optional
     - Access Restriction
   * - ``PATIENT_VISIT``
     - Optional[:ref:`VXU_V04_PATIENT_VISIT <hl7-v2_8_1-VXU_V04_PATIENT_VISIT>`]
     - optional
     - PATIENT_VISIT
   * - ``GT1``
     - Optional[List[:ref:`GT1 <hl7-v2_8_1-GT1>`]]
     - optional
     - Guarantor
   * - ``INSURANCE``
     - Optional[List[:ref:`VXU_V04_INSURANCE <hl7-v2_8_1-VXU_V04_INSURANCE>`]]
     - optional
     - INSURANCE
   * - ``PERSON_OBSERVATION``
     - Optional[List[:ref:`VXU_V04_PERSON_OBSERVATION <hl7-v2_8_1-VXU_V04_PERSON_OBSERVATION>`]]
     - optional
     - PERSON_OBSERVATION
   * - ``ORDER``
     - Optional[List[:ref:`VXU_V04_ORDER <hl7-v2_8_1-VXU_V04_ORDER>`]]
     - optional
     - ORDER
