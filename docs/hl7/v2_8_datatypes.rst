v2.8 Data Types
===============

.. _hl7-v2_8-AD:

AD: Address
~~~~~~~~~~~

Section 2.A.1

.. py:class:: hl7types.hl7.v2_8.datatypes.AD.AD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ad_1``
     - AD.1
     - str
     - O
     - Street Address
   * - ``ad_2``
     - AD.2
     - str
     - O
     - Other Designation
   * - ``ad_3``
     - AD.3
     - str
     - O
     - City
   * - ``ad_4``
     - AD.4
     - str
     - O
     - State or Province
   * - ``ad_5``
     - AD.5
     - str
     - O
     - Zip or Postal Code
   * - ``ad_6``
     - AD.6
     - str
     - O
     - Country
   * - ``ad_7``
     - AD.7
     - str
     - O
     - Address Type
   * - ``ad_8``
     - AD.8
     - str
     - O
     - Other Geographic Designation

.. _hl7-v2_8-AUI:

AUI: Authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.2

.. py:class:: hl7types.hl7.v2_8.datatypes.AUI.AUI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``aui_1``
     - AUI.1
     - str
     - O
     - Authorization Number
   * - ``aui_2``
     - AUI.2
     - str
     - O
     - Date
   * - ``aui_3``
     - AUI.3
     - str
     - O
     - Source

.. _hl7-v2_8-CCD:

CCD: Charge code and date
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.3

.. py:class:: hl7types.hl7.v2_8.datatypes.CCD.CCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ccd_1``
     - CCD.1
     - str
     - R
     - Invocation Event
   * - ``ccd_2``
     - CCD.2
     - str
     - O
     - Date/time

.. _hl7-v2_8-CCP:

CCP: Channel calibration parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.4

.. py:class:: hl7types.hl7.v2_8.datatypes.CCP.CCP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ccp_1``
     - CCP.1
     - str
     - O
     - Channel Calibration Sensitivity Correction Factor
   * - ``ccp_2``
     - CCP.2
     - str
     - O
     - Channel Calibration Baseline
   * - ``ccp_3``
     - CCP.3
     - str
     - O
     - Channel Calibration Time Skew

.. _hl7-v2_8-CD:

CD: Channel definition
~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.5

.. py:class:: hl7types.hl7.v2_8.datatypes.CD.CD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cd_1``
     - CD.1
     - :ref:`WVI <hl7-v2_8-WVI>`
     - O
     - Channel Identifier
   * - ``cd_2``
     - CD.2
     - :ref:`WVS <hl7-v2_8-WVS>`
     - O
     - Waveform Source
   * - ``cd_3``
     - CD.3
     - :ref:`CSU <hl7-v2_8-CSU>`
     - O
     - Channel Sensitivity and Units
   * - ``cd_4``
     - CD.4
     - :ref:`CCP <hl7-v2_8-CCP>`
     - O
     - Channel Calibration Parameters
   * - ``cd_5``
     - CD.5
     - str
     - O
     - Channel Sampling Frequency
   * - ``cd_6``
     - CD.6
     - :ref:`NR <hl7-v2_8-NR>`
     - O
     - Minimum and Maximum Data Values

.. _hl7-v2_8-CF:

CF: Coded element with formatted values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.7

.. py:class:: hl7types.hl7.v2_8.datatypes.CF.CF
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cf_1``
     - CF.1
     - str
     - O
     - Identifier
   * - ``cf_2``
     - CF.2
     - str
     - O
     - Formatted Text
   * - ``cf_3``
     - CF.3
     - str
     - O
     - Name of Coding System
   * - ``cf_4``
     - CF.4
     - str
     - O
     - Alternate Identifier
   * - ``cf_5``
     - CF.5
     - str
     - O
     - Alternate Formatted Text
   * - ``cf_6``
     - CF.6
     - str
     - O
     - Name of Alternate Coding System
   * - ``cf_7``
     - CF.7
     - str
     - O
     - Coding System Version ID
   * - ``cf_8``
     - CF.8
     - str
     - O
     - Alternate Coding System Version ID
   * - ``cf_9``
     - CF.9
     - str
     - O
     - Original Text
   * - ``cf_10``
     - CF.10
     - str
     - O
     - Second Alternate Identifier
   * - ``cf_11``
     - CF.11
     - str
     - O
     - Second Alternate Formatted Text
   * - ``cf_12``
     - CF.12
     - str
     - O
     - Name of Second Alternate Coding System
   * - ``cf_13``
     - CF.13
     - str
     - O
     - Second Alternate Coding System Version ID
   * - ``cf_14``
     - CF.14
     - str
     - O
     - Coding System OID
   * - ``cf_15``
     - CF.15
     - str
     - O
     - Value Set OID
   * - ``cf_16``
     - CF.16
     - str
     - O
     - Value Set Version ID
   * - ``cf_17``
     - CF.17
     - str
     - O
     - Alternate Coding System OID
   * - ``cf_18``
     - CF.18
     - str
     - O
     - Alternate Value Set OID
   * - ``cf_19``
     - CF.19
     - str
     - O
     - Alternate Value Set Version ID
   * - ``cf_20``
     - CF.20
     - str
     - O
     - Second Alternate Coding System OID
   * - ``cf_21``
     - CF.21
     - str
     - O
     - Second Alternate Value Set OID
   * - ``cf_22``
     - CF.22
     - str
     - O
     - Second Alternate Value Set Version ID

.. _hl7-v2_8-CNE:

CNE: Coded with no exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.8

.. py:class:: hl7types.hl7.v2_8.datatypes.CNE.CNE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cne_1``
     - CNE.1
     - str
     - R
     - Identifier
   * - ``cne_2``
     - CNE.2
     - str
     - O
     - Text
   * - ``cne_3``
     - CNE.3
     - str
     - O
     - Name of Coding System
   * - ``cne_4``
     - CNE.4
     - str
     - O
     - Alternate Identifier
   * - ``cne_5``
     - CNE.5
     - str
     - O
     - Alternate Text
   * - ``cne_6``
     - CNE.6
     - str
     - O
     - Name of Alternate Coding System
   * - ``cne_7``
     - CNE.7
     - str
     - O
     - Coding System Version ID
   * - ``cne_8``
     - CNE.8
     - str
     - O
     - Alternate Coding System Version ID
   * - ``cne_9``
     - CNE.9
     - str
     - O
     - Original Text
   * - ``cne_10``
     - CNE.10
     - str
     - O
     - Second Alternate Identifier
   * - ``cne_11``
     - CNE.11
     - str
     - O
     - Second Alternate Text
   * - ``cne_12``
     - CNE.12
     - str
     - O
     - Name of Second Alternate Coding System
   * - ``cne_13``
     - CNE.13
     - str
     - O
     - Second Alternate Coding System Version ID
   * - ``cne_14``
     - CNE.14
     - str
     - O
     - Coding System OID
   * - ``cne_15``
     - CNE.15
     - str
     - O
     - Value Set OID
   * - ``cne_16``
     - CNE.16
     - str
     - O
     - Value Set Version ID
   * - ``cne_17``
     - CNE.17
     - str
     - O
     - Alternate Coding System OID
   * - ``cne_18``
     - CNE.18
     - str
     - O
     - Alternate Value Set OID
   * - ``cne_19``
     - CNE.19
     - str
     - O
     - Alternate Value Set Version ID
   * - ``cne_20``
     - CNE.20
     - str
     - O
     - Second Alternate Coding System OID
   * - ``cne_21``
     - CNE.21
     - str
     - O
     - Second Alternate Value Set OID
   * - ``cne_22``
     - CNE.22
     - str
     - O
     - Second Alternate Value Set Version ID

.. _hl7-v2_8-CNN:

CNN: Composite id number and name simplified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.9

.. py:class:: hl7types.hl7.v2_8.datatypes.CNN.CNN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cnn_1``
     - CNN.1
     - str
     - O
     - ID Number
   * - ``cnn_2``
     - CNN.2
     - str
     - O
     - Family Name
   * - ``cnn_3``
     - CNN.3
     - str
     - O
     - Given Name
   * - ``cnn_4``
     - CNN.4
     - str
     - O
     - Second and Further Given Names or Initials Thereof
   * - ``cnn_5``
     - CNN.5
     - str
     - O
     - Suffix (e.g., JR or III)
   * - ``cnn_6``
     - CNN.6
     - str
     - O
     - Prefix (e.g., DR)
   * - ``cnn_7``
     - CNN.7
     - str
     - O
     - Degree (e.g., MD)
   * - ``cnn_8``
     - CNN.8
     - str
     - O
     - Source Table
   * - ``cnn_9``
     - CNN.9
     - str
     - O
     - Assigning Authority   - Namespace ID
   * - ``cnn_10``
     - CNN.10
     - str
     - O
     - Assigning Authority  - Universal ID
   * - ``cnn_11``
     - CNN.11
     - str
     - O
     - Assigning Authority  - Universal ID Type

.. _hl7-v2_8-CP:

CP: Composite price
~~~~~~~~~~~~~~~~~~~

Section 2.A.10

.. py:class:: hl7types.hl7.v2_8.datatypes.CP.CP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cp_1``
     - CP.1
     - :ref:`MO <hl7-v2_8-MO>`
     - R
     - Price
   * - ``cp_2``
     - CP.2
     - str
     - O
     - Price Type
   * - ``cp_3``
     - CP.3
     - str
     - O
     - From Value
   * - ``cp_4``
     - CP.4
     - str
     - O
     - To Value
   * - ``cp_5``
     - CP.5
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Range Units
   * - ``cp_6``
     - CP.6
     - str
     - O
     - Range Type

.. _hl7-v2_8-CQ:

CQ: Composite quantity with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.11

.. py:class:: hl7types.hl7.v2_8.datatypes.CQ.CQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cq_1``
     - CQ.1
     - str
     - O
     - Quantity
   * - ``cq_2``
     - CQ.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Units

.. _hl7-v2_8-CSU:

CSU: Channel sensitivity and units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.12

.. py:class:: hl7types.hl7.v2_8.datatypes.CSU.CSU
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``csu_1``
     - CSU.1
     - str
     - R
     - Channel Sensitivity
   * - ``csu_2``
     - CSU.2
     - str
     - O
     - Unit of Measure Identifier
   * - ``csu_3``
     - CSU.3
     - str
     - O
     - Unit of Measure Description
   * - ``csu_4``
     - CSU.4
     - str
     - O
     - Unit of Measure Coding System
   * - ``csu_5``
     - CSU.5
     - str
     - O
     - Alternate Unit of Measure Identifier
   * - ``csu_6``
     - CSU.6
     - str
     - O
     - Alternate Unit of Measure Description
   * - ``csu_7``
     - CSU.7
     - str
     - O
     - Alternate Unit of Measure Coding System
   * - ``csu_8``
     - CSU.8
     - str
     - O
     - Unit of Measure Coding System Version ID
   * - ``csu_9``
     - CSU.9
     - str
     - O
     - Alternate Unit of Measure Coding System Version ID
   * - ``csu_10``
     - CSU.10
     - str
     - O
     - Original Text
   * - ``csu_11``
     - CSU.11
     - str
     - O
     - Second Alternate Unit of Measure Identifier
   * - ``csu_12``
     - CSU.12
     - str
     - O
     - Second Alternate Unit of Measure Text
   * - ``csu_13``
     - CSU.13
     - str
     - O
     - Name of Second Alternate Unit of Measure Coding Sy
   * - ``csu_14``
     - CSU.14
     - str
     - O
     - Second Alternate Unit of Measure Coding System Ver
   * - ``csu_15``
     - CSU.15
     - str
     - O
     - Unit of Measure Coding System OID
   * - ``csu_16``
     - CSU.16
     - str
     - O
     - Unit of Measure Value Set OID
   * - ``csu_17``
     - CSU.17
     - str
     - O
     - Unit of Measure Value Set Version ID
   * - ``csu_18``
     - CSU.18
     - str
     - O
     - Alternate Unit of Measure Coding System OID
   * - ``csu_19``
     - CSU.19
     - str
     - O
     - Alternate Unit of Measure Value Set OID
   * - ``csu_20``
     - CSU.20
     - str
     - O
     - Alternate Unit of Measure Value Set Version ID
   * - ``csu_21``
     - CSU.21
     - str
     - O
     - Alternate Unit of Measure Coding System OID
   * - ``csu_22``
     - CSU.22
     - str
     - O
     - Alternate Unit of Measure Value Set OID
   * - ``csu_23``
     - CSU.23
     - str
     - O
     - Alternate Unit of Measure Value Set Version ID

.. _hl7-v2_8-CWE:

CWE: Coded with exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.13

.. py:class:: hl7types.hl7.v2_8.datatypes.CWE.CWE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cwe_1``
     - CWE.1
     - str
     - O
     - Identifier
   * - ``cwe_2``
     - CWE.2
     - str
     - O
     - Text
   * - ``cwe_3``
     - CWE.3
     - str
     - O
     - Name of Coding System
   * - ``cwe_4``
     - CWE.4
     - str
     - O
     - Alternate Identifier
   * - ``cwe_5``
     - CWE.5
     - str
     - O
     - Alternate Text
   * - ``cwe_6``
     - CWE.6
     - str
     - O
     - Name of Alternate Coding System
   * - ``cwe_7``
     - CWE.7
     - str
     - O
     - Coding System Version ID
   * - ``cwe_8``
     - CWE.8
     - str
     - O
     - Alternate Coding System Version ID
   * - ``cwe_9``
     - CWE.9
     - str
     - O
     - Original Text
   * - ``cwe_10``
     - CWE.10
     - str
     - O
     - Second Alternate Identifier
   * - ``cwe_11``
     - CWE.11
     - str
     - O
     - Second Alternate Text
   * - ``cwe_12``
     - CWE.12
     - str
     - O
     - Name of Second Alternate Coding System
   * - ``cwe_13``
     - CWE.13
     - str
     - O
     - Second Alternate Coding System Version ID
   * - ``cwe_14``
     - CWE.14
     - str
     - O
     - Coding System OID
   * - ``cwe_15``
     - CWE.15
     - str
     - O
     - Value Set OID
   * - ``cwe_16``
     - CWE.16
     - str
     - O
     - Value Set Version ID
   * - ``cwe_17``
     - CWE.17
     - str
     - O
     - Alternate Coding System OID
   * - ``cwe_18``
     - CWE.18
     - str
     - O
     - Alternate Value Set OID
   * - ``cwe_19``
     - CWE.19
     - str
     - O
     - Alternate Value Set Version ID
   * - ``cwe_20``
     - CWE.20
     - str
     - O
     - Second Alternate Coding System OID
   * - ``cwe_21``
     - CWE.21
     - str
     - O
     - Second Alternate Value Set OID
   * - ``cwe_22``
     - CWE.22
     - str
     - O
     - Second Alternate Value Set Version ID

.. _hl7-v2_8-CX:

CX: Extended composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.14

.. py:class:: hl7types.hl7.v2_8.datatypes.CX.CX
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``cx_1``
     - CX.1
     - str
     - R
     - ID Number
   * - ``cx_2``
     - CX.2
     - str
     - O
     - Identifier Check Digit
   * - ``cx_3``
     - CX.3
     - str
     - O
     - Check Digit Scheme
   * - ``cx_4``
     - CX.4
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Authority
   * - ``cx_5``
     - CX.5
     - str
     - R
     - Identifier Type Code
   * - ``cx_6``
     - CX.6
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Facility
   * - ``cx_7``
     - CX.7
     - str
     - O
     - Effective Date
   * - ``cx_8``
     - CX.8
     - str
     - O
     - Expiration Date
   * - ``cx_9``
     - CX.9
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``cx_10``
     - CX.10
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Agency or Department
   * - ``cx_11``
     - CX.11
     - str
     - O
     - Security Check
   * - ``cx_12``
     - CX.12
     - str
     - O
     - Security Check Scheme

.. _hl7-v2_8-DDI:

DDI: Daily deductible information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.15

.. py:class:: hl7types.hl7.v2_8.datatypes.DDI.DDI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ddi_1``
     - DDI.1
     - str
     - O
     - Delay Days
   * - ``ddi_2``
     - DDI.2
     - :ref:`MO <hl7-v2_8-MO>`
     - R
     - Monetary Amount
   * - ``ddi_3``
     - DDI.3
     - str
     - O
     - Number of Days

.. _hl7-v2_8-DIN:

DIN: Date and institution name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.16

.. py:class:: hl7types.hl7.v2_8.datatypes.DIN.DIN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``din_1``
     - DIN.1
     - str
     - R
     - Date
   * - ``din_2``
     - DIN.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Institution Name

.. _hl7-v2_8-DLD:

DLD: Discharge to location and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.17

.. py:class:: hl7types.hl7.v2_8.datatypes.DLD.DLD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dld_1``
     - DLD.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Discharge to Location
   * - ``dld_2``
     - DLD.2
     - str
     - O
     - Effective Date

.. _hl7-v2_8-DLN:

DLN: Driver's license number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.18

.. py:class:: hl7types.hl7.v2_8.datatypes.DLN.DLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dln_1``
     - DLN.1
     - str
     - R
     - License Number
   * - ``dln_2``
     - DLN.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Issuing State, Province, Country
   * - ``dln_3``
     - DLN.3
     - str
     - O
     - Expiration Date

.. _hl7-v2_8-DLT:

DLT: Delta
~~~~~~~~~~

Section 2.A.19

.. py:class:: hl7types.hl7.v2_8.datatypes.DLT.DLT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dlt_1``
     - DLT.1
     - :ref:`NR <hl7-v2_8-NR>`
     - O
     - Normal Range
   * - ``dlt_2``
     - DLT.2
     - str
     - O
     - Numeric Threshold
   * - ``dlt_3``
     - DLT.3
     - str
     - O
     - Change Computation
   * - ``dlt_4``
     - DLT.4
     - str
     - O
     - Days Retained

.. _hl7-v2_8-DR:

DR: Date/time range
~~~~~~~~~~~~~~~~~~~

Section 2.A.20

.. py:class:: hl7types.hl7.v2_8.datatypes.DR.DR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dr_1``
     - DR.1
     - str
     - O
     - Range Start Date/Time
   * - ``dr_2``
     - DR.2
     - str
     - O
     - Range End Date/Time

.. _hl7-v2_8-DTN:

DTN: Day type and number
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.23

.. py:class:: hl7types.hl7.v2_8.datatypes.DTN.DTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``dtn_1``
     - DTN.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Day Type
   * - ``dtn_2``
     - DTN.2
     - str
     - R
     - Number of Days

.. _hl7-v2_8-ED:

ED: Encapsulated data
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.24

.. py:class:: hl7types.hl7.v2_8.datatypes.ED.ED
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ed_1``
     - ED.1
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Source Application
   * - ``ed_2``
     - ED.2
     - str
     - R
     - Type of Data
   * - ``ed_3``
     - ED.3
     - str
     - O
     - Data Subtype
   * - ``ed_4``
     - ED.4
     - str
     - R
     - Encoding
   * - ``ed_5``
     - ED.5
     - str
     - R
     - Data

.. _hl7-v2_8-EI:

EI: Entity identifier
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.25

.. py:class:: hl7types.hl7.v2_8.datatypes.EI.EI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ei_1``
     - EI.1
     - str
     - O
     - Entity Identifier
   * - ``ei_2``
     - EI.2
     - str
     - O
     - Namespace ID
   * - ``ei_3``
     - EI.3
     - str
     - O
     - Universal ID
   * - ``ei_4``
     - EI.4
     - str
     - O
     - Universal ID Type

.. _hl7-v2_8-EIP:

EIP: Entity identifier pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.26

.. py:class:: hl7types.hl7.v2_8.datatypes.EIP.EIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``eip_1``
     - EIP.1
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Placer Assigned Identifier
   * - ``eip_2``
     - EIP.2
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Filler Assigned Identifier

.. _hl7-v2_8-ERL:

ERL: Error location
~~~~~~~~~~~~~~~~~~~

Section 2.A.28

.. py:class:: hl7types.hl7.v2_8.datatypes.ERL.ERL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``erl_1``
     - ERL.1
     - str
     - R
     - Segment ID
   * - ``erl_2``
     - ERL.2
     - str
     - R
     - Segment Sequence
   * - ``erl_3``
     - ERL.3
     - str
     - O
     - Field Position
   * - ``erl_4``
     - ERL.4
     - str
     - O
     - Field Repetition
   * - ``erl_5``
     - ERL.5
     - str
     - O
     - Component Number
   * - ``erl_6``
     - ERL.6
     - str
     - O
     - Sub-Component Number

.. _hl7-v2_8-FC:

FC: Financial class
~~~~~~~~~~~~~~~~~~~

Section 2.A.29

.. py:class:: hl7types.hl7.v2_8.datatypes.FC.FC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``fc_1``
     - FC.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Financial Class Code
   * - ``fc_2``
     - FC.2
     - str
     - O
     - Effective Date

.. _hl7-v2_8-FN:

FN: Family name
~~~~~~~~~~~~~~~

Section 2.A.30

.. py:class:: hl7types.hl7.v2_8.datatypes.FN.FN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``fn_1``
     - FN.1
     - str
     - R
     - Surname
   * - ``fn_2``
     - FN.2
     - str
     - O
     - Own Surname Prefix
   * - ``fn_3``
     - FN.3
     - str
     - O
     - Own Surname
   * - ``fn_4``
     - FN.4
     - str
     - O
     - Surname Prefix from Partner/Spouse
   * - ``fn_5``
     - FN.5
     - str
     - O
     - Surname from Partner/Spouse

.. _hl7-v2_8-HD:

HD: Hierarchic designator
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.33

.. py:class:: hl7types.hl7.v2_8.datatypes.HD.HD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``hd_1``
     - HD.1
     - str
     - O
     - Namespace ID
   * - ``hd_2``
     - HD.2
     - str
     - O
     - Universal ID
   * - ``hd_3``
     - HD.3
     - str
     - O
     - Universal ID Type

.. _hl7-v2_8-ICD:

ICD: Insurance certification definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.34

.. py:class:: hl7types.hl7.v2_8.datatypes.ICD.ICD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``icd_1``
     - ICD.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Certification Patient Type
   * - ``icd_2``
     - ICD.2
     - str
     - R
     - Certification Required
   * - ``icd_3``
     - ICD.3
     - str
     - O
     - Date/Time Certification Required

.. _hl7-v2_8-JCC:

JCC: Job code/class
~~~~~~~~~~~~~~~~~~~

Section 2.A.37

.. py:class:: hl7types.hl7.v2_8.datatypes.JCC.JCC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``jcc_1``
     - JCC.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Job Code
   * - ``jcc_2``
     - JCC.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Job Class
   * - ``jcc_3``
     - JCC.3
     - str
     - O
     - Job Description Text

.. _hl7-v2_8-MA:

MA: Multiplexed array
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.40

.. py:class:: hl7types.hl7.v2_8.datatypes.MA.MA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ma_1``
     - MA.1
     - str
     - O
     - Sample Y From Channel 1
   * - ``ma_2``
     - MA.2
     - str
     - O
     - Sample Y From Channel 2
   * - ``ma_3``
     - MA.3
     - str
     - O
     - Sample Y From Channel 3
   * - ``ma_4``
     - MA.4
     - str
     - O
     - Sample Y From Channel 4

.. _hl7-v2_8-MO:

MO: Money
~~~~~~~~~

Section 2.A.41

.. py:class:: hl7types.hl7.v2_8.datatypes.MO.MO
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``mo_1``
     - MO.1
     - str
     - O
     - Quantity
   * - ``mo_2``
     - MO.2
     - str
     - O
     - Denomination

.. _hl7-v2_8-MOC:

MOC: Money and code
~~~~~~~~~~~~~~~~~~~

Section 2.A.42

.. py:class:: hl7types.hl7.v2_8.datatypes.MOC.MOC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``moc_1``
     - MOC.1
     - :ref:`MO <hl7-v2_8-MO>`
     - O
     - Monetary Amount
   * - ``moc_2``
     - MOC.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Charge Code

.. _hl7-v2_8-MOP:

MOP: Money or percentage
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.43

.. py:class:: hl7types.hl7.v2_8.datatypes.MOP.MOP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``mop_1``
     - MOP.1
     - str
     - R
     - Money or Percentage Indicator
   * - ``mop_2``
     - MOP.2
     - str
     - R
     - Money or Percentage Quantity
   * - ``mop_3``
     - MOP.3
     - str
     - O
     - Monetary  Denomination

.. _hl7-v2_8-MSG:

MSG: Message type
~~~~~~~~~~~~~~~~~

Section 2.A.44

.. py:class:: hl7types.hl7.v2_8.datatypes.MSG.MSG
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``msg_1``
     - MSG.1
     - str
     - R
     - Message Code
   * - ``msg_2``
     - MSG.2
     - str
     - R
     - Trigger Event
   * - ``msg_3``
     - MSG.3
     - str
     - R
     - Message Structure

.. _hl7-v2_8-NA:

NA: Numeric array
~~~~~~~~~~~~~~~~~

Section 2.A.45

.. py:class:: hl7types.hl7.v2_8.datatypes.NA.NA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``na_1``
     - NA.1
     - str
     - O
     - Value1
   * - ``na_2``
     - NA.2
     - str
     - O
     - Value2
   * - ``na_3``
     - NA.3
     - str
     - O
     - Value3
   * - ``na_4``
     - NA.4
     - str
     - O
     - Value4

.. _hl7-v2_8-NDL:

NDL: Name with date and location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.46

.. py:class:: hl7types.hl7.v2_8.datatypes.NDL.NDL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ndl_1``
     - NDL.1
     - :ref:`CNN <hl7-v2_8-CNN>`
     - O
     - Name
   * - ``ndl_2``
     - NDL.2
     - str
     - O
     - Start Date/time
   * - ``ndl_3``
     - NDL.3
     - str
     - O
     - End Date/time
   * - ``ndl_4``
     - NDL.4
     - str
     - O
     - Point of Care
   * - ``ndl_5``
     - NDL.5
     - str
     - O
     - Room
   * - ``ndl_6``
     - NDL.6
     - str
     - O
     - Bed
   * - ``ndl_7``
     - NDL.7
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Facility
   * - ``ndl_8``
     - NDL.8
     - str
     - O
     - Location Status
   * - ``ndl_9``
     - NDL.9
     - str
     - O
     - Patient Location Type
   * - ``ndl_10``
     - NDL.10
     - str
     - O
     - Building
   * - ``ndl_11``
     - NDL.11
     - str
     - O
     - Floor

.. _hl7-v2_8-NR:

NR: Numeric range
~~~~~~~~~~~~~~~~~

Section 2.A.48

.. py:class:: hl7types.hl7.v2_8.datatypes.NR.NR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``nr_1``
     - NR.1
     - str
     - O
     - Low Value
   * - ``nr_2``
     - NR.2
     - str
     - O
     - High Value

.. _hl7-v2_8-OCD:

OCD: Occurrence code and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.49

.. py:class:: hl7types.hl7.v2_8.datatypes.OCD.OCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ocd_1``
     - OCD.1
     - :ref:`CNE <hl7-v2_8-CNE>`
     - R
     - Occurrence Code
   * - ``ocd_2``
     - OCD.2
     - str
     - R
     - Occurrence Date

.. _hl7-v2_8-OSP:

OSP: Occurrence span code and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.51

.. py:class:: hl7types.hl7.v2_8.datatypes.OSP.OSP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``osp_1``
     - OSP.1
     - :ref:`CNE <hl7-v2_8-CNE>`
     - R
     - Occurrence Span Code
   * - ``osp_2``
     - OSP.2
     - str
     - O
     - Occurrence Span Start Date
   * - ``osp_3``
     - OSP.3
     - str
     - O
     - Occurrence Span Stop Date

.. _hl7-v2_8-PIP:

PIP: Practitioner institutional privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.52

.. py:class:: hl7types.hl7.v2_8.datatypes.PIP.PIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pip_1``
     - PIP.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Privilege
   * - ``pip_2``
     - PIP.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Privilege Class
   * - ``pip_3``
     - PIP.3
     - str
     - O
     - Expiration Date
   * - ``pip_4``
     - PIP.4
     - str
     - O
     - Activation Date
   * - ``pip_5``
     - PIP.5
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Facility

.. _hl7-v2_8-PL:

PL: Person location
~~~~~~~~~~~~~~~~~~~

Section 2.A.53

.. py:class:: hl7types.hl7.v2_8.datatypes.PL.PL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pl_1``
     - PL.1
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Point of Care
   * - ``pl_2``
     - PL.2
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Room
   * - ``pl_3``
     - PL.3
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Bed
   * - ``pl_4``
     - PL.4
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Facility
   * - ``pl_5``
     - PL.5
     - str
     - O
     - Location Status
   * - ``pl_6``
     - PL.6
     - str
     - O
     - Person Location Type
   * - ``pl_7``
     - PL.7
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Building
   * - ``pl_8``
     - PL.8
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Floor
   * - ``pl_9``
     - PL.9
     - str
     - O
     - Location Description
   * - ``pl_10``
     - PL.10
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Comprehensive Location Identifier
   * - ``pl_11``
     - PL.11
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Authority for Location

.. _hl7-v2_8-PLN:

PLN: Practitioner license or other id number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.54

.. py:class:: hl7types.hl7.v2_8.datatypes.PLN.PLN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pln_1``
     - PLN.1
     - str
     - R
     - ID Number
   * - ``pln_2``
     - PLN.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Type of ID Number
   * - ``pln_3``
     - PLN.3
     - str
     - O
     - State/other Qualifying Information
   * - ``pln_4``
     - PLN.4
     - str
     - O
     - Expiration Date

.. _hl7-v2_8-PPN:

PPN: Performing person time stamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.55

.. py:class:: hl7types.hl7.v2_8.datatypes.PPN.PPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ppn_1``
     - PPN.1
     - str
     - O
     - Person Identifier
   * - ``ppn_2``
     - PPN.2
     - :ref:`FN <hl7-v2_8-FN>`
     - O
     - Family Name
   * - ``ppn_3``
     - PPN.3
     - str
     - O
     - Given Name
   * - ``ppn_4``
     - PPN.4
     - str
     - O
     - Second and Further Given Names or Initials Thereof
   * - ``ppn_5``
     - PPN.5
     - str
     - O
     - Suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - str
     - O
     - Prefix (e.g., DR)
   * - ``ppn_8``
     - PPN.8
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Source Table
   * - ``ppn_9``
     - PPN.9
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Authority
   * - ``ppn_10``
     - PPN.10
     - str
     - O
     - Name Type Code
   * - ``ppn_11``
     - PPN.11
     - str
     - O
     - Identifier Check Digit
   * - ``ppn_12``
     - PPN.12
     - str
     - O
     - Check Digit Scheme
   * - ``ppn_13``
     - PPN.13
     - str
     - O
     - Identifier Type Code
   * - ``ppn_14``
     - PPN.14
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Facility
   * - ``ppn_15``
     - PPN.15
     - str
     - O
     - Date/Time Action Performed
   * - ``ppn_16``
     - PPN.16
     - str
     - O
     - Name Representation Code
   * - ``ppn_17``
     - PPN.17
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Name Context
   * - ``ppn_19``
     - PPN.19
     - str
     - O
     - Name Assembly Order
   * - ``ppn_20``
     - PPN.20
     - str
     - O
     - Effective Date
   * - ``ppn_21``
     - PPN.21
     - str
     - O
     - Expiration Date
   * - ``ppn_22``
     - PPN.22
     - str
     - O
     - Professional Suffix
   * - ``ppn_23``
     - PPN.23
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``ppn_24``
     - PPN.24
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Agency or Department
   * - ``ppn_25``
     - PPN.25
     - str
     - O
     - Security Check
   * - ``ppn_26``
     - PPN.26
     - str
     - O
     - Security Check Scheme

.. _hl7-v2_8-PRL:

PRL: Parent result link
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.56

.. py:class:: hl7types.hl7.v2_8.datatypes.PRL.PRL
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``prl_1``
     - PRL.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Parent Observation Identifier
   * - ``prl_2``
     - PRL.2
     - str
     - O
     - Parent Observation Sub-identifier
   * - ``prl_3``
     - PRL.3
     - str
     - O
     - Parent Observation Value Descriptor

.. _hl7-v2_8-PT:

PT: Processing type
~~~~~~~~~~~~~~~~~~~

Section 2.A.57

.. py:class:: hl7types.hl7.v2_8.datatypes.PT.PT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pt_1``
     - PT.1
     - str
     - R
     - Processing ID
   * - ``pt_2``
     - PT.2
     - str
     - O
     - Processing Mode

.. _hl7-v2_8-PTA:

PTA: Policy type and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.58

.. py:class:: hl7types.hl7.v2_8.datatypes.PTA.PTA
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``pta_1``
     - PTA.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Policy Type
   * - ``pta_2``
     - PTA.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Amount Class
   * - ``pta_4``
     - PTA.4
     - :ref:`MOP <hl7-v2_8-MOP>`
     - R
     - Money or Percentage

.. _hl7-v2_8-QIP:

QIP: Query input parameter list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.59

.. py:class:: hl7types.hl7.v2_8.datatypes.QIP.QIP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qip_1``
     - QIP.1
     - str
     - R
     - Segment Field Name
   * - ``qip_2``
     - QIP.2
     - str
     - R
     - Values

.. _hl7-v2_8-QSC:

QSC: Query selection criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.60

.. py:class:: hl7types.hl7.v2_8.datatypes.QSC.QSC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``qsc_1``
     - QSC.1
     - str
     - R
     - Segment Field Name
   * - ``qsc_2``
     - QSC.2
     - str
     - O
     - Relational Operator
   * - ``qsc_3``
     - QSC.3
     - str
     - O
     - Value
   * - ``qsc_4``
     - QSC.4
     - str
     - O
     - Relational Conjunction

.. _hl7-v2_8-RCD:

RCD: Row column definition
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.61

.. py:class:: hl7types.hl7.v2_8.datatypes.RCD.RCD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rcd_1``
     - RCD.1
     - str
     - O
     - Segment Field Name
   * - ``rcd_2``
     - RCD.2
     - str
     - O
     - HL7 Data Type
   * - ``rcd_3``
     - RCD.3
     - str
     - O
     - Maximum Column Width

.. _hl7-v2_8-RFR:

RFR: Reference range
~~~~~~~~~~~~~~~~~~~~

Section 2.A.62

.. py:class:: hl7types.hl7.v2_8.datatypes.RFR.RFR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rfr_1``
     - RFR.1
     - :ref:`NR <hl7-v2_8-NR>`
     - R
     - Numeric Range
   * - ``rfr_2``
     - RFR.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Administrative Sex
   * - ``rfr_3``
     - RFR.3
     - :ref:`NR <hl7-v2_8-NR>`
     - O
     - Age Range
   * - ``rfr_4``
     - RFR.4
     - :ref:`NR <hl7-v2_8-NR>`
     - O
     - Gestational Age Range
   * - ``rfr_5``
     - RFR.5
     - str
     - O
     - Species
   * - ``rfr_6``
     - RFR.6
     - str
     - O
     - Race/subspecies
   * - ``rfr_7``
     - RFR.7
     - str
     - O
     - Conditions

.. _hl7-v2_8-RI:

RI: Repeat interval
~~~~~~~~~~~~~~~~~~~

Section 2.A.63

.. py:class:: hl7types.hl7.v2_8.datatypes.RI.RI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ri_1``
     - RI.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Repeat Pattern
   * - ``ri_2``
     - RI.2
     - str
     - O
     - Explicit Time Interval

.. _hl7-v2_8-RMC:

RMC: Room coverage
~~~~~~~~~~~~~~~~~~

Section 2.A.64

.. py:class:: hl7types.hl7.v2_8.datatypes.RMC.RMC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rmc_1``
     - RMC.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Room Type
   * - ``rmc_2``
     - RMC.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Amount Type
   * - ``rmc_4``
     - RMC.4
     - :ref:`MOP <hl7-v2_8-MOP>`
     - R
     - Money or Percentage

.. _hl7-v2_8-RP:

RP: Reference pointer
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.65

.. py:class:: hl7types.hl7.v2_8.datatypes.RP.RP
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rp_1``
     - RP.1
     - str
     - O
     - Pointer
   * - ``rp_2``
     - RP.2
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Application ID
   * - ``rp_3``
     - RP.3
     - str
     - O
     - Type of Data
   * - ``rp_4``
     - RP.4
     - str
     - O
     - Subtype

.. _hl7-v2_8-RPT:

RPT: Repeat pattern
~~~~~~~~~~~~~~~~~~~

Section 2.A.66

.. py:class:: hl7types.hl7.v2_8.datatypes.RPT.RPT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``rpt_1``
     - RPT.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Repeat Pattern Code
   * - ``rpt_2``
     - RPT.2
     - str
     - O
     - Calendar Alignment
   * - ``rpt_3``
     - RPT.3
     - str
     - O
     - Phase Range Begin Value
   * - ``rpt_4``
     - RPT.4
     - str
     - O
     - Phase Range End Value
   * - ``rpt_5``
     - RPT.5
     - str
     - O
     - Period Quantity
   * - ``rpt_6``
     - RPT.6
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Period Units
   * - ``rpt_7``
     - RPT.7
     - str
     - O
     - Institution Specified Time
   * - ``rpt_8``
     - RPT.8
     - str
     - O
     - Event
   * - ``rpt_9``
     - RPT.9
     - str
     - O
     - Event Offset Quantity
   * - ``rpt_10``
     - RPT.10
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Event Offset Units
   * - ``rpt_11``
     - RPT.11
     - str
     - O
     - General Timing Specification

.. _hl7-v2_8-SAD:

SAD: Street address
~~~~~~~~~~~~~~~~~~~

Section 2.A.67

.. py:class:: hl7types.hl7.v2_8.datatypes.SAD.SAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sad_1``
     - SAD.1
     - str
     - O
     - Street or Mailing Address
   * - ``sad_2``
     - SAD.2
     - str
     - O
     - Street Name
   * - ``sad_3``
     - SAD.3
     - str
     - O
     - Dwelling Number

.. _hl7-v2_8-SCV:

SCV: Scheduling class value pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.68

.. py:class:: hl7types.hl7.v2_8.datatypes.SCV.SCV
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``scv_1``
     - SCV.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Parameter Class
   * - ``scv_2``
     - SCV.2
     - str
     - O
     - Parameter Value

.. _hl7-v2_8-SN:

SN: Structured numeric
~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.70

.. py:class:: hl7types.hl7.v2_8.datatypes.SN.SN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sn_1``
     - SN.1
     - str
     - O
     - Comparator
   * - ``sn_2``
     - SN.2
     - str
     - O
     - Num1
   * - ``sn_3``
     - SN.3
     - str
     - O
     - Separator/Suffix
   * - ``sn_4``
     - SN.4
     - str
     - O
     - Num2

.. _hl7-v2_8-SPD:

SPD: Specialty description
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.72

.. py:class:: hl7types.hl7.v2_8.datatypes.SPD.SPD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``spd_1``
     - SPD.1
     - str
     - R
     - Specialty Name
   * - ``spd_2``
     - SPD.2
     - str
     - O
     - Governing Board
   * - ``spd_3``
     - SPD.3
     - str
     - O
     - Eligible or Certified
   * - ``spd_4``
     - SPD.4
     - str
     - O
     - Date of Certification

.. _hl7-v2_8-SRT:

SRT: Sort order
~~~~~~~~~~~~~~~

Section 2.A.74

.. py:class:: hl7types.hl7.v2_8.datatypes.SRT.SRT
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``srt_1``
     - SRT.1
     - str
     - R
     - Sort-by Field
   * - ``srt_2``
     - SRT.2
     - str
     - O
     - Sequencing

.. _hl7-v2_8-UVC:

UVC: Ub value code and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.80

.. py:class:: hl7types.hl7.v2_8.datatypes.UVC.UVC
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``uvc_1``
     - UVC.1
     - :ref:`CWE <hl7-v2_8-CWE>`
     - R
     - Value Code
   * - ``uvc_2``
     - UVC.2
     - :ref:`MO <hl7-v2_8-MO>`
     - O
     - Value Amount
   * - ``uvc_3``
     - UVC.3
     - str
     - O
     - Non-Monetary Value Amount / Quantity
   * - ``uvc_4``
     - UVC.4
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Non-Monetary Value Amount / Units

.. _hl7-v2_8-VH:

VH: Visiting hours
~~~~~~~~~~~~~~~~~~

Section 2.A.81

.. py:class:: hl7types.hl7.v2_8.datatypes.VH.VH
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vh_1``
     - VH.1
     - str
     - O
     - Start Day Range
   * - ``vh_2``
     - VH.2
     - str
     - O
     - End Day Range
   * - ``vh_3``
     - VH.3
     - str
     - O
     - Start Hour Range
   * - ``vh_4``
     - VH.4
     - str
     - O
     - End Hour Range

.. _hl7-v2_8-VID:

VID: Version identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.82

.. py:class:: hl7types.hl7.v2_8.datatypes.VID.VID
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vid_1``
     - VID.1
     - str
     - R
     - Version ID
   * - ``vid_2``
     - VID.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Internationalization Code
   * - ``vid_3``
     - VID.3
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - International Version ID

.. _hl7-v2_8-VR:

VR: Value range
~~~~~~~~~~~~~~~

Section 2.A.83

.. py:class:: hl7types.hl7.v2_8.datatypes.VR.VR
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``vr_1``
     - VR.1
     - str
     - O
     - First Data Code Value
   * - ``vr_2``
     - VR.2
     - str
     - O
     - Last Data Code Value

.. _hl7-v2_8-WVI:

WVI: Channel identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.84

.. py:class:: hl7types.hl7.v2_8.datatypes.WVI.WVI
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``wvi_1``
     - WVI.1
     - str
     - R
     - Channel Number
   * - ``wvi_2``
     - WVI.2
     - str
     - O
     - Channel Name

.. _hl7-v2_8-WVS:

WVS: Waveform source
~~~~~~~~~~~~~~~~~~~~

Section 2.A.85

.. py:class:: hl7types.hl7.v2_8.datatypes.WVS.WVS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``wvs_1``
     - WVS.1
     - str
     - R
     - Source One Name
   * - ``wvs_2``
     - WVS.2
     - str
     - O
     - Source Two Name

.. _hl7-v2_8-XAD:

XAD: Extended address
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.86

.. py:class:: hl7types.hl7.v2_8.datatypes.XAD.XAD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xad_1``
     - XAD.1
     - :ref:`SAD <hl7-v2_8-SAD>`
     - O
     - Street Address
   * - ``xad_2``
     - XAD.2
     - str
     - O
     - Other Designation
   * - ``xad_3``
     - XAD.3
     - str
     - O
     - City
   * - ``xad_4``
     - XAD.4
     - str
     - O
     - State or Province
   * - ``xad_5``
     - XAD.5
     - str
     - O
     - Zip or Postal Code
   * - ``xad_6``
     - XAD.6
     - str
     - O
     - Country
   * - ``xad_7``
     - XAD.7
     - str
     - O
     - Address Type
   * - ``xad_8``
     - XAD.8
     - str
     - O
     - Other Geographic Designation
   * - ``xad_9``
     - XAD.9
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - County/Parish Code
   * - ``xad_10``
     - XAD.10
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Census Tract
   * - ``xad_11``
     - XAD.11
     - str
     - O
     - Address Representation Code
   * - ``xad_13``
     - XAD.13
     - str
     - O
     - Effective Date
   * - ``xad_14``
     - XAD.14
     - str
     - O
     - Expiration Date
   * - ``xad_15``
     - XAD.15
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Expiration Reason
   * - ``xad_16``
     - XAD.16
     - str
     - O
     - Temporary Indicator
   * - ``xad_17``
     - XAD.17
     - str
     - O
     - Bad Address Indicator
   * - ``xad_18``
     - XAD.18
     - str
     - O
     - Address Usage
   * - ``xad_19``
     - XAD.19
     - str
     - O
     - Addressee
   * - ``xad_20``
     - XAD.20
     - str
     - O
     - Comment
   * - ``xad_21``
     - XAD.21
     - str
     - O
     - Preference Order
   * - ``xad_22``
     - XAD.22
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Protection Code
   * - ``xad_23``
     - XAD.23
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Address Identifier

.. _hl7-v2_8-XCN:

XCN: Extended composite id number and name for persons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.87

.. py:class:: hl7types.hl7.v2_8.datatypes.XCN.XCN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xcn_1``
     - XCN.1
     - str
     - O
     - Person Identifier
   * - ``xcn_2``
     - XCN.2
     - :ref:`FN <hl7-v2_8-FN>`
     - O
     - Family Name
   * - ``xcn_3``
     - XCN.3
     - str
     - O
     - Given Name
   * - ``xcn_4``
     - XCN.4
     - str
     - O
     - Second and Further Given Names or Initials Thereof
   * - ``xcn_5``
     - XCN.5
     - str
     - O
     - Suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - str
     - O
     - Prefix (e.g., DR)
   * - ``xcn_8``
     - XCN.8
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Source Table
   * - ``xcn_9``
     - XCN.9
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Authority
   * - ``xcn_10``
     - XCN.10
     - str
     - O
     - Name Type Code
   * - ``xcn_11``
     - XCN.11
     - str
     - O
     - Identifier Check Digit
   * - ``xcn_12``
     - XCN.12
     - str
     - O
     - Check Digit Scheme
   * - ``xcn_13``
     - XCN.13
     - str
     - O
     - Identifier Type Code
   * - ``xcn_14``
     - XCN.14
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Facility
   * - ``xcn_15``
     - XCN.15
     - str
     - O
     - Name Representation Code
   * - ``xcn_16``
     - XCN.16
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Name Context
   * - ``xcn_18``
     - XCN.18
     - str
     - O
     - Name Assembly Order
   * - ``xcn_19``
     - XCN.19
     - str
     - O
     - Effective Date
   * - ``xcn_20``
     - XCN.20
     - str
     - O
     - Expiration Date
   * - ``xcn_21``
     - XCN.21
     - str
     - O
     - Professional Suffix
   * - ``xcn_22``
     - XCN.22
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``xcn_23``
     - XCN.23
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Assigning Agency or Department
   * - ``xcn_24``
     - XCN.24
     - str
     - O
     - Security Check
   * - ``xcn_25``
     - XCN.25
     - str
     - O
     - Security Check Scheme

.. _hl7-v2_8-XON:

XON: Extended composite name and identification number for organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.88

.. py:class:: hl7types.hl7.v2_8.datatypes.XON.XON
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xon_1``
     - XON.1
     - str
     - O
     - Organization Name
   * - ``xon_2``
     - XON.2
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Organization Name Type Code
   * - ``xon_6``
     - XON.6
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Authority
   * - ``xon_7``
     - XON.7
     - str
     - O
     - Identifier Type Code
   * - ``xon_8``
     - XON.8
     - :ref:`HD <hl7-v2_8-HD>`
     - O
     - Assigning Facility
   * - ``xon_9``
     - XON.9
     - str
     - O
     - Name Representation Code
   * - ``xon_10``
     - XON.10
     - str
     - O
     - Organization Identifier

.. _hl7-v2_8-XPN:

XPN: Extended person name
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.89

.. py:class:: hl7types.hl7.v2_8.datatypes.XPN.XPN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xpn_1``
     - XPN.1
     - :ref:`FN <hl7-v2_8-FN>`
     - O
     - Family Name
   * - ``xpn_2``
     - XPN.2
     - str
     - O
     - Given Name
   * - ``xpn_3``
     - XPN.3
     - str
     - O
     - Second and Further Given Names or Initials Thereof
   * - ``xpn_4``
     - XPN.4
     - str
     - O
     - Suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - str
     - O
     - Prefix (e.g., DR)
   * - ``xpn_7``
     - XPN.7
     - str
     - O
     - Name Type Code
   * - ``xpn_8``
     - XPN.8
     - str
     - O
     - Name Representation Code
   * - ``xpn_9``
     - XPN.9
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Name Context
   * - ``xpn_11``
     - XPN.11
     - str
     - O
     - Name Assembly Order
   * - ``xpn_12``
     - XPN.12
     - str
     - O
     - Effective Date
   * - ``xpn_13``
     - XPN.13
     - str
     - O
     - Expiration Date
   * - ``xpn_14``
     - XPN.14
     - str
     - O
     - Professional Suffix
   * - ``xpn_15``
     - XPN.15
     - str
     - O
     - Called By

.. _hl7-v2_8-XTN:

XTN: Extended telecommunication number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.90

.. py:class:: hl7types.hl7.v2_8.datatypes.XTN.XTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xtn_2``
     - XTN.2
     - str
     - O
     - Telecommunication Use Code
   * - ``xtn_3``
     - XTN.3
     - str
     - R
     - Telecommunication Equipment Type
   * - ``xtn_4``
     - XTN.4
     - str
     - O
     - Communication Address
   * - ``xtn_5``
     - XTN.5
     - str
     - O
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - str
     - O
     - Area/City Code
   * - ``xtn_7``
     - XTN.7
     - str
     - O
     - Local Number
   * - ``xtn_8``
     - XTN.8
     - str
     - O
     - Extension
   * - ``xtn_9``
     - XTN.9
     - str
     - O
     - Any Text
   * - ``xtn_10``
     - XTN.10
     - str
     - O
     - Extension Prefix
   * - ``xtn_11``
     - XTN.11
     - str
     - O
     - Speed Dial Code
   * - ``xtn_12``
     - XTN.12
     - str
     - O
     - Unformatted Telephone number
   * - ``xtn_13``
     - XTN.13
     - str
     - O
     - Effective Start Date
   * - ``xtn_14``
     - XTN.14
     - str
     - O
     - Expiration Date
   * - ``xtn_15``
     - XTN.15
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Expiration Reason
   * - ``xtn_16``
     - XTN.16
     - :ref:`CWE <hl7-v2_8-CWE>`
     - O
     - Protection Code
   * - ``xtn_17``
     - XTN.17
     - :ref:`EI <hl7-v2_8-EI>`
     - O
     - Shared Telecommunication Identifier
   * - ``xtn_18``
     - XTN.18
     - str
     - O
     - Preference Order
