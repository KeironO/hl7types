v2.5.1 Data Types
=================

.. _hl7-v2_5_1-AD:

AD: Address
~~~~~~~~~~~

Section 2.A.1.1

.. py:class:: hl7types.hl7.v2_5_1.datatypes.AD.AD
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

.. _hl7-v2_5_1-AUI:

AUI: Authorization information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.2

.. py:class:: hl7types.hl7.v2_5_1.datatypes.AUI.AUI
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

.. _hl7-v2_5_1-CCD:

CCD: Charge code and date
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.3

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CCD.CCD
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
     - O
     - Invocation Event
   * - ``ccd_2``
     - CCD.2
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Date/time

.. _hl7-v2_5_1-CCP:

CCP: Channel calibration parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.4

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CCP.CCP
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

.. _hl7-v2_5_1-CD:

CD: Channel definition
~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.5

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CD.CD
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
     - :ref:`WVI <hl7-v2_5_1-WVI>`
     - O
     - Channel Identifier
   * - ``cd_2``
     - CD.2
     - :ref:`WVS <hl7-v2_5_1-WVS>`
     - O
     - Waveform Source
   * - ``cd_3``
     - CD.3
     - :ref:`CSU <hl7-v2_5_1-CSU>`
     - O
     - Channel Sensitivity/Units
   * - ``cd_4``
     - CD.4
     - :ref:`CCP <hl7-v2_5_1-CCP>`
     - O
     - Channel Calibration Parameters
   * - ``cd_5``
     - CD.5
     - str
     - O
     - Channel Sampling Frequency
   * - ``cd_6``
     - CD.6
     - :ref:`NR <hl7-v2_5_1-NR>`
     - O
     - Minimum/Maximum Data Values

.. _hl7-v2_5_1-CE:

CE: Coded element
~~~~~~~~~~~~~~~~~

Section 2.A.1.6

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CE.CE
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ce_1``
     - CE.1
     - str
     - O
     - Identifier
   * - ``ce_2``
     - CE.2
     - str
     - O
     - Text
   * - ``ce_3``
     - CE.3
     - str
     - O
     - Name of Coding System
   * - ``ce_4``
     - CE.4
     - str
     - O
     - Alternate Identifier
   * - ``ce_5``
     - CE.5
     - str
     - O
     - Alternate Text
   * - ``ce_6``
     - CE.6
     - str
     - O
     - Name of Alternate Coding System

.. _hl7-v2_5_1-CF:

CF: Coded element with formatted values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.7

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CF.CF
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

.. _hl7-v2_5_1-CNE:

CNE: Coded with no exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.8

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CNE.CNE
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
     - O
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

.. _hl7-v2_5_1-CNN:

CNN: Composite id number and name simplified
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.9

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CNN.CNN
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
     - Degree (e.g., MD
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

.. _hl7-v2_5_1-CP:

CP: Composite price
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.10

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CP.CP
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
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Range Units
   * - ``cp_6``
     - CP.6
     - str
     - O
     - Range Type

.. _hl7-v2_5_1-CQ:

CQ: Composite quantity with units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.11

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CQ.CQ
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Units

.. _hl7-v2_5_1-CSU:

CSU: Channel sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.12

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CSU.CSU
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
     - O
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

.. _hl7-v2_5_1-CWE:

CWE: Coded with exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.13

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CWE.CWE
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

.. _hl7-v2_5_1-CX:

CX: Extended composite id with check digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.14

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CX.CX
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
     - O
     - ID Number
   * - ``cx_2``
     - CX.2
     - str
     - O
     - Check Digit
   * - ``cx_3``
     - CX.3
     - str
     - O
     - Check Digit Scheme
   * - ``cx_4``
     - CX.4
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Assigning Authority
   * - ``cx_5``
     - CX.5
     - str
     - O
     - Identifier Type Code
   * - ``cx_6``
     - CX.6
     - :ref:`HD <hl7-v2_5_1-HD>`
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
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``cx_10``
     - CX.10
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Agency or Department

.. _hl7-v2_5_1-DDI:

DDI: Daily deductible information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.15

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DDI.DDI
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
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     - Monetary Amount
   * - ``ddi_3``
     - DDI.3
     - str
     - O
     - Number of Days

.. _hl7-v2_5_1-DIN:

DIN: Date and institution name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.16

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DIN.DIN
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Date
   * - ``din_2``
     - DIN.2
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Institution Name

.. _hl7-v2_5_1-DLD:

DLD: Discharge location and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.17

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLD.DLD
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
     - str
     - O
     - Discharge Location
   * - ``dld_2``
     - DLD.2
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date

.. _hl7-v2_5_1-DLN:

DLN: Driver's license number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.18

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLN.DLN
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
     - O
     - License Number
   * - ``dln_2``
     - DLN.2
     - str
     - O
     - Issuing State, Province, Country
   * - ``dln_3``
     - DLN.3
     - str
     - O
     - Expiration Date

.. _hl7-v2_5_1-DLT:

DLT: Delta
~~~~~~~~~~

Section 2.A.1.19

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLT.DLT
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
     - :ref:`NR <hl7-v2_5_1-NR>`
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

.. _hl7-v2_5_1-DR:

DR: Date/time range
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.20

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DR.DR
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
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Range Start Date/Time
   * - ``dr_2``
     - DR.2
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Range End Date/Time

.. _hl7-v2_5_1-DTN:

DTN: Day type and number
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.23

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DTN.DTN
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
     - str
     - O
     - Day Type
   * - ``dtn_2``
     - DTN.2
     - str
     - O
     - Number of Days

.. _hl7-v2_5_1-ED:

ED: Encapsulated data
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.24

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ED.ED
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
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Source Application
   * - ``ed_2``
     - ED.2
     - str
     - O
     - Type of Data
   * - ``ed_3``
     - ED.3
     - str
     - O
     - Data Subtype
   * - ``ed_4``
     - ED.4
     - str
     - O
     - Encoding
   * - ``ed_5``
     - ED.5
     - str
     - O
     - Data

.. _hl7-v2_5_1-EI:

EI: Entity identifier
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.25

.. py:class:: hl7types.hl7.v2_5_1.datatypes.EI.EI
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

.. _hl7-v2_5_1-EIP:

EIP: Entity identifier pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.26

.. py:class:: hl7types.hl7.v2_5_1.datatypes.EIP.EIP
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
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     - Placer Assigned Identifier
   * - ``eip_2``
     - EIP.2
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     - Filler Assigned Identifier

.. _hl7-v2_5_1-ELD:

ELD: Error location and description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.27

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ELD.ELD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``eld_1``
     - ELD.1
     - str
     - O
     - Segment ID
   * - ``eld_2``
     - ELD.2
     - str
     - O
     - Segment Sequence
   * - ``eld_3``
     - ELD.3
     - str
     - O
     - Field Position
   * - ``eld_4``
     - ELD.4
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Code Identifying Error

.. _hl7-v2_5_1-ERL:

ERL: Error location
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.28

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ERL.ERL
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
     - O
     - Segment ID
   * - ``erl_2``
     - ERL.2
     - str
     - O
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

.. _hl7-v2_5_1-FC:

FC: Financial class
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.29

.. py:class:: hl7types.hl7.v2_5_1.datatypes.FC.FC
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
     - str
     - O
     - Financial Class Code
   * - ``fc_2``
     - FC.2
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date

.. _hl7-v2_5_1-FN:

FN: Family name
~~~~~~~~~~~~~~~

Section 2.A.1.30

.. py:class:: hl7types.hl7.v2_5_1.datatypes.FN.FN
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
     - O
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
     - Surname Prefix From Partner/Spouse
   * - ``fn_5``
     - FN.5
     - str
     - O
     - Surname From Partner/Spouse

.. _hl7-v2_5_1-HD:

HD: Hierarchic designator
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.33

.. py:class:: hl7types.hl7.v2_5_1.datatypes.HD.HD
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

.. _hl7-v2_5_1-ICD:

ICD: Insurance certification definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.34

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ICD.ICD
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
     - str
     - O
     - Certification Patient Type
   * - ``icd_2``
     - ICD.2
     - str
     - O
     - Certification Required
   * - ``icd_3``
     - ICD.3
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Date/Time Certification Required

.. _hl7-v2_5_1-JCC:

JCC: Job code/class
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.37

.. py:class:: hl7types.hl7.v2_5_1.datatypes.JCC.JCC
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
     - str
     - O
     - Job Code
   * - ``jcc_2``
     - JCC.2
     - str
     - O
     - Job Class
   * - ``jcc_3``
     - JCC.3
     - str
     - O
     - Job Description Text

.. _hl7-v2_5_1-LA1:

LA1: Location with address variation 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.38

.. py:class:: hl7types.hl7.v2_5_1.datatypes.LA1.LA1
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``la1_1``
     - LA1.1
     - str
     - O
     - Point of Care
   * - ``la1_2``
     - LA1.2
     - str
     - O
     - Room
   * - ``la1_3``
     - LA1.3
     - str
     - O
     - Bed
   * - ``la1_4``
     - LA1.4
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Facility
   * - ``la1_5``
     - LA1.5
     - str
     - O
     - Location Status
   * - ``la1_6``
     - LA1.6
     - str
     - O
     - Patient Location Type
   * - ``la1_7``
     - LA1.7
     - str
     - O
     - Building
   * - ``la1_8``
     - LA1.8
     - str
     - O
     - Floor
   * - ``la1_9``
     - LA1.9
     - :ref:`AD <hl7-v2_5_1-AD>`
     - O
     - Address

.. _hl7-v2_5_1-LA2:

LA2: Location with address variation 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.39

.. py:class:: hl7types.hl7.v2_5_1.datatypes.LA2.LA2
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``la2_1``
     - LA2.1
     - str
     - O
     - Point of Care
   * - ``la2_2``
     - LA2.2
     - str
     - O
     - Room
   * - ``la2_3``
     - LA2.3
     - str
     - O
     - Bed
   * - ``la2_4``
     - LA2.4
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Facility
   * - ``la2_5``
     - LA2.5
     - str
     - O
     - Location Status
   * - ``la2_6``
     - LA2.6
     - str
     - O
     - Patient Location Type
   * - ``la2_7``
     - LA2.7
     - str
     - O
     - Building
   * - ``la2_8``
     - LA2.8
     - str
     - O
     - Floor
   * - ``la2_9``
     - LA2.9
     - str
     - O
     - Street Address
   * - ``la2_10``
     - LA2.10
     - str
     - O
     - Other Designation
   * - ``la2_11``
     - LA2.11
     - str
     - O
     - City
   * - ``la2_12``
     - LA2.12
     - str
     - O
     - State or Province
   * - ``la2_13``
     - LA2.13
     - str
     - O
     - Zip or Postal Code
   * - ``la2_14``
     - LA2.14
     - str
     - O
     - Country
   * - ``la2_15``
     - LA2.15
     - str
     - O
     - Address Type
   * - ``la2_16``
     - LA2.16
     - str
     - O
     - Other Geographic Designation

.. _hl7-v2_5_1-MA:

MA: Multiplexed array
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.40

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MA.MA
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
     - Sample 1 From Channel 1
   * - ``ma_2``
     - MA.2
     - str
     - O
     - Sample 1 From Channel 2
   * - ``ma_3``
     - MA.3
     - str
     - O
     - Sample 1 From Channel N
   * - ``ma_4``
     - MA.4
     - str
     - O
     - Sample 2 From Channel 1
   * - ``ma_5``
     - MA.5
     - str
     - O
     - Sample 2 From Channel N
   * - ``ma_6``
     - MA.6
     - str
     - O
     - Sample N From Channel N

.. _hl7-v2_5_1-MO:

MO: Money
~~~~~~~~~

Section 2.A.1.41

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MO.MO
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

.. _hl7-v2_5_1-MOC:

MOC: Money and code
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.42

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MOC.MOC
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
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     - Monetary Amount
   * - ``moc_2``
     - MOC.2
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Charge Code

.. _hl7-v2_5_1-MOP:

MOP: Money or percentage
~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.43

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MOP.MOP
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
     - O
     - Money or Percentage Indicator
   * - ``mop_2``
     - MOP.2
     - str
     - O
     - Money or Percentage Quantity
   * - ``mop_3``
     - MOP.3
     - str
     - O
     - Currency Denomination

.. _hl7-v2_5_1-MSG:

MSG: Message type
~~~~~~~~~~~~~~~~~

Section 2.A.1.44

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MSG.MSG
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
     - O
     - Message Code
   * - ``msg_2``
     - MSG.2
     - str
     - O
     - Trigger Event
   * - ``msg_3``
     - MSG.3
     - str
     - O
     - Message Structure

.. _hl7-v2_5_1-NA:

NA: Numeric array
~~~~~~~~~~~~~~~~~

Section 2.A.1.45

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NA.NA
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

.. _hl7-v2_5_1-NDL:

NDL: Name with date and location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.46

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NDL.NDL
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
     - :ref:`CNN <hl7-v2_5_1-CNN>`
     - O
     - Name
   * - ``ndl_2``
     - NDL.2
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Start Date/time
   * - ``ndl_3``
     - NDL.3
     - :ref:`TS <hl7-v2_5_1-TS>`
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
     - :ref:`HD <hl7-v2_5_1-HD>`
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

.. _hl7-v2_5_1-NR:

NR: Numeric range
~~~~~~~~~~~~~~~~~

Section 2.A.1.48

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NR.NR
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

.. _hl7-v2_5_1-OCD:

OCD: Occurrence code and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.49

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OCD.OCD
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
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     - Occurrence Code
   * - ``ocd_2``
     - OCD.2
     - str
     - O
     - Occurrence Date

.. _hl7-v2_5_1-OSD:

OSD: Order sequence definition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.50

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OSD.OSD
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``osd_1``
     - OSD.1
     - str
     - O
     - Sequence/Results Flag
   * - ``osd_2``
     - OSD.2
     - str
     - O
     - Placer Order Number: Entity Identifier
   * - ``osd_3``
     - OSD.3
     - str
     - O
     - Placer Order Number: Namespace ID
   * - ``osd_4``
     - OSD.4
     - str
     - O
     - Filler Order Number: Entity Identifier
   * - ``osd_5``
     - OSD.5
     - str
     - O
     - Filler Order Number: Namespace ID
   * - ``osd_6``
     - OSD.6
     - str
     - O
     - Sequence Condition Value
   * - ``osd_7``
     - OSD.7
     - str
     - O
     - Maximum Number of Repeats
   * - ``osd_8``
     - OSD.8
     - str
     - O
     - Placer Order Number: Universal ID
   * - ``osd_9``
     - OSD.9
     - str
     - O
     - Placer Order Number: Universal ID Type
   * - ``osd_10``
     - OSD.10
     - str
     - O
     - Filler Order Number: Universal ID
   * - ``osd_11``
     - OSD.11
     - str
     - O
     - Filler Order Number: Universal ID Type

.. _hl7-v2_5_1-OSP:

OSP: Occurrence span code and date
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.51

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OSP.OSP
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
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
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

.. _hl7-v2_5_1-PIP:

PIP: Practitioner institutional privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.52

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PIP.PIP
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Privilege
   * - ``pip_2``
     - PIP.2
     - :ref:`CE <hl7-v2_5_1-CE>`
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
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     - Facility

.. _hl7-v2_5_1-PL:

PL: Person location
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.53

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PL.PL
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
     - str
     - O
     - Point of Care
   * - ``pl_2``
     - PL.2
     - str
     - O
     - Room
   * - ``pl_3``
     - PL.3
     - str
     - O
     - Bed
   * - ``pl_4``
     - PL.4
     - :ref:`HD <hl7-v2_5_1-HD>`
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
     - str
     - O
     - Building
   * - ``pl_8``
     - PL.8
     - str
     - O
     - Floor
   * - ``pl_9``
     - PL.9
     - str
     - O
     - Location Description
   * - ``pl_10``
     - PL.10
     - :ref:`EI <hl7-v2_5_1-EI>`
     - O
     - Comprehensive Location Identifier
   * - ``pl_11``
     - PL.11
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Assigning Authority for Location

.. _hl7-v2_5_1-PLN:

PLN: Practitioner license or other id number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.54

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PLN.PLN
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
     - O
     - ID Number
   * - ``pln_2``
     - PLN.2
     - str
     - O
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

.. _hl7-v2_5_1-PPN:

PPN: Performing person time stamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.55

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PPN.PPN
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
     - ID Number
   * - ``ppn_2``
     - PPN.2
     - :ref:`FN <hl7-v2_5_1-FN>`
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
   * - ``ppn_7``
     - PPN.7
     - str
     - O
     - Degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - str
     - O
     - Source Table
   * - ``ppn_9``
     - PPN.9
     - :ref:`HD <hl7-v2_5_1-HD>`
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
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Assigning Facility
   * - ``ppn_15``
     - PPN.15
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Date/Time Action Performed
   * - ``ppn_16``
     - PPN.16
     - str
     - O
     - Name Representation Code
   * - ``ppn_17``
     - PPN.17
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Name Context
   * - ``ppn_18``
     - PPN.18
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     - Name Validity Range
   * - ``ppn_19``
     - PPN.19
     - str
     - O
     - Name Assembly Order
   * - ``ppn_20``
     - PPN.20
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date
   * - ``ppn_21``
     - PPN.21
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Expiration Date
   * - ``ppn_22``
     - PPN.22
     - str
     - O
     - Professional Suffix
   * - ``ppn_23``
     - PPN.23
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``ppn_24``
     - PPN.24
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Agency or Department

.. _hl7-v2_5_1-PRL:

PRL: Parent result link
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.56

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PRL.PRL
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
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

.. _hl7-v2_5_1-PT:

PT: Processing type
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.57

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PT.PT
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
     - O
     - Processing ID
   * - ``pt_2``
     - PT.2
     - str
     - O
     - Processing Mode

.. _hl7-v2_5_1-PTA:

PTA: Policy type and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.58

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PTA.PTA
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
     - str
     - O
     - Policy Type
   * - ``pta_2``
     - PTA.2
     - str
     - O
     - Amount Class
   * - ``pta_3``
     - PTA.3
     - str
     - O
     - Money or Percentage Quantity
   * - ``pta_4``
     - PTA.4
     - :ref:`MOP <hl7-v2_5_1-MOP>`
     - O
     - Money or Percentage

.. _hl7-v2_5_1-QIP:

QIP: Query input parameter list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.59

.. py:class:: hl7types.hl7.v2_5_1.datatypes.QIP.QIP
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
     - O
     - Segment Field Name
   * - ``qip_2``
     - QIP.2
     - str
     - O
     - Values

.. _hl7-v2_5_1-QSC:

QSC: Query selection criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.60

.. py:class:: hl7types.hl7.v2_5_1.datatypes.QSC.QSC
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
     - O
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

.. _hl7-v2_5_1-RCD:

RCD: Row column definition
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.61

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RCD.RCD
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

.. _hl7-v2_5_1-RFR:

RFR: Reference range
~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.62

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RFR.RFR
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
     - :ref:`NR <hl7-v2_5_1-NR>`
     - O
     - Numeric Range
   * - ``rfr_2``
     - RFR.2
     - str
     - O
     - Administrative Sex
   * - ``rfr_3``
     - RFR.3
     - :ref:`NR <hl7-v2_5_1-NR>`
     - O
     - Age Range
   * - ``rfr_4``
     - RFR.4
     - :ref:`NR <hl7-v2_5_1-NR>`
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

.. _hl7-v2_5_1-RI:

RI: Repeat interval
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.63

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RI.RI
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
     - str
     - O
     - Repeat Pattern
   * - ``ri_2``
     - RI.2
     - str
     - O
     - Explicit Time Interval

.. _hl7-v2_5_1-RMC:

RMC: Room coverage
~~~~~~~~~~~~~~~~~~

Section 2.A.1.64

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RMC.RMC
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
     - str
     - O
     - Room Type
   * - ``rmc_2``
     - RMC.2
     - str
     - O
     - Amount Type
   * - ``rmc_3``
     - RMC.3
     - str
     - O
     - Coverage Amount
   * - ``rmc_4``
     - RMC.4
     - :ref:`MOP <hl7-v2_5_1-MOP>`
     - O
     - Money or Percentage

.. _hl7-v2_5_1-RP:

RP: Reference pointer
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.65

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RP.RP
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
     - :ref:`HD <hl7-v2_5_1-HD>`
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

.. _hl7-v2_5_1-RPT:

RPT: Repeat pattern
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.66

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RPT.RPT
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
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
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
     - str
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
     - str
     - O
     - Event Offset Units
   * - ``rpt_11``
     - RPT.11
     - str
     - O
     - General Timing Specification

.. _hl7-v2_5_1-SAD:

SAD: Street address
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.67

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SAD.SAD
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

.. _hl7-v2_5_1-SCV:

SCV: Scheduling class value pair
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.68

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SCV.SCV
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
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Parameter Class
   * - ``scv_2``
     - SCV.2
     - str
     - O
     - Parameter Value

.. _hl7-v2_5_1-SN:

SN: Structured numeric
~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.70

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SN.SN
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

.. _hl7-v2_5_1-SPD:

SPD: Specialty description
~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.71

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SPD.SPD
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
     - O
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

.. _hl7-v2_5_1-SPS:

SPS: Specimen source
~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.72

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SPS.SPS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``sps_1``
     - SPS.1
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Specimen Source Name or Code
   * - ``sps_2``
     - SPS.2
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Additives
   * - ``sps_3``
     - SPS.3
     - str
     - O
     - Specimen Collection Method
   * - ``sps_4``
     - SPS.4
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Body Site
   * - ``sps_5``
     - SPS.5
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Site Modifier
   * - ``sps_6``
     - SPS.6
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Collection Method Modifier Code
   * - ``sps_7``
     - SPS.7
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Specimen Role

.. _hl7-v2_5_1-SRT:

SRT: Sort order
~~~~~~~~~~~~~~~

Section 2.A.1.73

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SRT.SRT
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
     - O
     - Sort-by Field
   * - ``srt_2``
     - SRT.2
     - str
     - O
     - Sequencing

.. _hl7-v2_5_1-TQ:

TQ: Timing quantity
~~~~~~~~~~~~~~~~~~~

Section 2.A.1.76

.. py:class:: hl7types.hl7.v2_5_1.datatypes.TQ.TQ
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``tq_1``
     - TQ.1
     - :ref:`CQ <hl7-v2_5_1-CQ>`
     - O
     - Quantity
   * - ``tq_2``
     - TQ.2
     - :ref:`RI <hl7-v2_5_1-RI>`
     - O
     - Interval
   * - ``tq_3``
     - TQ.3
     - str
     - O
     - Duration
   * - ``tq_4``
     - TQ.4
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Start Date/Time
   * - ``tq_5``
     - TQ.5
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - End Date/Time
   * - ``tq_6``
     - TQ.6
     - str
     - O
     - Priority
   * - ``tq_7``
     - TQ.7
     - str
     - O
     - Condition
   * - ``tq_8``
     - TQ.8
     - str
     - O
     - Text
   * - ``tq_9``
     - TQ.9
     - str
     - O
     - Conjunction
   * - ``tq_10``
     - TQ.10
     - :ref:`OSD <hl7-v2_5_1-OSD>`
     - O
     - Order Sequencing
   * - ``tq_11``
     - TQ.11
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Occurrence Duration
   * - ``tq_12``
     - TQ.12
     - str
     - O
     - Total Occurrences

.. _hl7-v2_5_1-TS:

TS: Time stamp
~~~~~~~~~~~~~~

Section 2.A.1.77

.. py:class:: hl7types.hl7.v2_5_1.datatypes.TS.TS
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``ts_1``
     - TS.1
     - str
     - O
     - Time
   * - ``ts_2``
     - TS.2
     - str
     - O
     - Degree of Precision

.. _hl7-v2_5_1-UVC:

UVC: Ub value code and amount
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.79

.. py:class:: hl7types.hl7.v2_5_1.datatypes.UVC.UVC
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
     - :ref:`CNE <hl7-v2_5_1-CNE>`
     - O
     - Value Code
   * - ``uvc_2``
     - UVC.2
     - :ref:`MO <hl7-v2_5_1-MO>`
     - O
     - Value Amount

.. _hl7-v2_5_1-VH:

VH: Visiting hours
~~~~~~~~~~~~~~~~~~

Section 2.A.1.80

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VH.VH
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

.. _hl7-v2_5_1-VID:

VID: Version identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.81

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VID.VID
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
     - O
     - Version ID
   * - ``vid_2``
     - VID.2
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Internationalization Code
   * - ``vid_3``
     - VID.3
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - International Version ID

.. _hl7-v2_5_1-VR:

VR: Value range
~~~~~~~~~~~~~~~

Section 2.A.1.82

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VR.VR
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

.. _hl7-v2_5_1-WVI:

WVI: Channel identifier
~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.83

.. py:class:: hl7types.hl7.v2_5_1.datatypes.WVI.WVI
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
     - O
     - Channel Number
   * - ``wvi_2``
     - WVI.2
     - str
     - O
     - Channel Name

.. _hl7-v2_5_1-WVS:

WVS: Waveform source
~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.84

.. py:class:: hl7types.hl7.v2_5_1.datatypes.WVS.WVS
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
     - O
     - Source One Name
   * - ``wvs_2``
     - WVS.2
     - str
     - O
     - Source Two Name

.. _hl7-v2_5_1-XAD:

XAD: Extended address
~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.85

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XAD.XAD
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
     - :ref:`SAD <hl7-v2_5_1-SAD>`
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
     - str
     - O
     - County/Parish Code
   * - ``xad_10``
     - XAD.10
     - str
     - O
     - Census Tract
   * - ``xad_11``
     - XAD.11
     - str
     - O
     - Address Representation Code
   * - ``xad_12``
     - XAD.12
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     - Address Validity Range
   * - ``xad_13``
     - XAD.13
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date
   * - ``xad_14``
     - XAD.14
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Expiration Date

.. _hl7-v2_5_1-XCN:

XCN: Extended composite id number and name for persons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.86

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XCN.XCN
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
     - ID Number
   * - ``xcn_2``
     - XCN.2
     - :ref:`FN <hl7-v2_5_1-FN>`
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
   * - ``xcn_7``
     - XCN.7
     - str
     - O
     - Degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - str
     - O
     - Source Table
   * - ``xcn_9``
     - XCN.9
     - :ref:`HD <hl7-v2_5_1-HD>`
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
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Assigning Facility
   * - ``xcn_15``
     - XCN.15
     - str
     - O
     - Name Representation Code
   * - ``xcn_16``
     - XCN.16
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Name Context
   * - ``xcn_17``
     - XCN.17
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     - Name Validity Range
   * - ``xcn_18``
     - XCN.18
     - str
     - O
     - Name Assembly Order
   * - ``xcn_19``
     - XCN.19
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date
   * - ``xcn_20``
     - XCN.20
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Expiration Date
   * - ``xcn_21``
     - XCN.21
     - str
     - O
     - Professional Suffix
   * - ``xcn_22``
     - XCN.22
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Jurisdiction
   * - ``xcn_23``
     - XCN.23
     - :ref:`CWE <hl7-v2_5_1-CWE>`
     - O
     - Assigning Agency or Department

.. _hl7-v2_5_1-XON:

XON: Extended composite name and identification number for organizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.87

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XON.XON
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
     - str
     - O
     - Organization Name Type Code
   * - ``xon_3``
     - XON.3
     - str
     - O
     - ID Number
   * - ``xon_4``
     - XON.4
     - str
     - O
     - Check Digit
   * - ``xon_5``
     - XON.5
     - str
     - O
     - Check Digit Scheme
   * - ``xon_6``
     - XON.6
     - :ref:`HD <hl7-v2_5_1-HD>`
     - O
     - Assigning Authority
   * - ``xon_7``
     - XON.7
     - str
     - O
     - Identifier Type Code
   * - ``xon_8``
     - XON.8
     - :ref:`HD <hl7-v2_5_1-HD>`
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

.. _hl7-v2_5_1-XPN:

XPN: Extended person name
~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.88

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XPN.XPN
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
     - :ref:`FN <hl7-v2_5_1-FN>`
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
   * - ``xpn_6``
     - XPN.6
     - str
     - O
     - Degree (e.g., MD)
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
     - :ref:`CE <hl7-v2_5_1-CE>`
     - O
     - Name Context
   * - ``xpn_10``
     - XPN.10
     - :ref:`DR <hl7-v2_5_1-DR>`
     - O
     - Name Validity Range
   * - ``xpn_11``
     - XPN.11
     - str
     - O
     - Name Assembly Order
   * - ``xpn_12``
     - XPN.12
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Effective Date
   * - ``xpn_13``
     - XPN.13
     - :ref:`TS <hl7-v2_5_1-TS>`
     - O
     - Expiration Date
   * - ``xpn_14``
     - XPN.14
     - str
     - O
     - Professional Suffix

.. _hl7-v2_5_1-XTN:

XTN: Extended telecommunication number
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Section 2.A.1.89

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XTN.XTN
   :noindex:

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - OPT
     - Description
   * - ``xtn_1``
     - XTN.1
     - str
     - O
     - Telephone Number
   * - ``xtn_2``
     - XTN.2
     - str
     - O
     - Telecommunication Use Code
   * - ``xtn_3``
     - XTN.3
     - str
     - O
     - Telecommunication Equipment Type
   * - ``xtn_4``
     - XTN.4
     - str
     - O
     - Email Address
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
