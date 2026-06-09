v2.5.1 Data Types
=================

.. _hl7-v2_5_1-AD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.AD.AD
   :noindex:

   HL7 v2 AD data type.

AD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ad_1``
     - AD.1
     - Optional[str]
     - optional
     -
     - Street Address
   * - ``ad_2``
     - AD.2
     - Optional[str]
     - optional
     -
     - Other Designation
   * - ``ad_3``
     - AD.3
     - Optional[str]
     - optional
     -
     - City
   * - ``ad_4``
     - AD.4
     - Optional[str]
     - optional
     -
     - State or Province
   * - ``ad_5``
     - AD.5
     - Optional[str]
     - optional
     -
     - Zip or Postal Code
   * - ``ad_6``
     - AD.6
     - Optional[str]
     - optional
     -
     - Country
   * - ``ad_7``
     - AD.7
     - Optional[str]
     - optional
     -
     - Address Type
   * - ``ad_8``
     - AD.8
     - Optional[str]
     - optional
     -
     - Other Geographic Designation

.. _hl7-v2_5_1-AUI:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.AUI.AUI
   :noindex:

   HL7 v2 AUI data type.

AUI
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
   * - ``aui_1``
     - AUI.1
     - Optional[str]
     - optional
     -
     - Authorization Number
   * - ``aui_2``
     - AUI.2
     - Optional[str]
     - optional
     -
     - Date
   * - ``aui_3``
     - AUI.3
     - Optional[str]
     - optional
     -
     - Source

.. _hl7-v2_5_1-CCD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CCD.CCD
   :noindex:

   HL7 v2 CCD data type.

CCD
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
   * - ``ccd_1``
     - CCD.1
     - Optional[str]
     - optional
     -
     - Invocation Event
   * - ``ccd_2``
     - CCD.2
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Date/time

.. _hl7-v2_5_1-CCP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CCP.CCP
   :noindex:

   HL7 v2 CCP data type.

CCP
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
   * - ``ccp_1``
     - CCP.1
     - Optional[str]
     - optional
     -
     - Channel Calibration Sensitivity Correction Factor
   * - ``ccp_2``
     - CCP.2
     - Optional[str]
     - optional
     -
     - Channel Calibration Baseline
   * - ``ccp_3``
     - CCP.3
     - Optional[str]
     - optional
     -
     - Channel Calibration Time Skew

.. _hl7-v2_5_1-CD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CD.CD
   :noindex:

   HL7 v2 CD data type.

CD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cd_1``
     - CD.1
     - Optional[:ref:`WVI <hl7-v2_5_1-WVI>`]
     - optional
     -
     - Channel Identifier
   * - ``cd_2``
     - CD.2
     - Optional[:ref:`WVS <hl7-v2_5_1-WVS>`]
     - optional
     -
     - Waveform Source
   * - ``cd_3``
     - CD.3
     - Optional[:ref:`CSU <hl7-v2_5_1-CSU>`]
     - optional
     -
     - Channel Sensitivity/Units
   * - ``cd_4``
     - CD.4
     - Optional[:ref:`CCP <hl7-v2_5_1-CCP>`]
     - optional
     -
     - Channel Calibration Parameters
   * - ``cd_5``
     - CD.5
     - Optional[str]
     - optional
     -
     - Channel Sampling Frequency
   * - ``cd_6``
     - CD.6
     - Optional[:ref:`NR <hl7-v2_5_1-NR>`]
     - optional
     -
     - Minimum/Maximum Data Values

.. _hl7-v2_5_1-CE:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CE.CE
   :noindex:

   HL7 v2 CE data type.

CE
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ce_1``
     - CE.1
     - Optional[str]
     - optional
     -
     - Identifier
   * - ``ce_2``
     - CE.2
     - Optional[str]
     - optional
     -
     - Text
   * - ``ce_3``
     - CE.3
     - Optional[str]
     - optional
     -
     - Name of Coding System
   * - ``ce_4``
     - CE.4
     - Optional[str]
     - optional
     -
     - Alternate Identifier
   * - ``ce_5``
     - CE.5
     - Optional[str]
     - optional
     -
     - Alternate Text
   * - ``ce_6``
     - CE.6
     - Optional[str]
     - optional
     -
     - Name of Alternate Coding System

.. _hl7-v2_5_1-CF:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CF.CF
   :noindex:

   HL7 v2 CF data type.

CF
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cf_1``
     - CF.1
     - Optional[str]
     - optional
     -
     - Identifier
   * - ``cf_2``
     - CF.2
     - Optional[str]
     - optional
     -
     - Formatted Text
   * - ``cf_3``
     - CF.3
     - Optional[str]
     - optional
     -
     - Name of Coding System
   * - ``cf_4``
     - CF.4
     - Optional[str]
     - optional
     -
     - Alternate Identifier
   * - ``cf_5``
     - CF.5
     - Optional[str]
     - optional
     -
     - Alternate Formatted Text
   * - ``cf_6``
     - CF.6
     - Optional[str]
     - optional
     -
     - Name of Alternate Coding System

.. _hl7-v2_5_1-CNE:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CNE.CNE
   :noindex:

   HL7 v2 CNE data type.

CNE
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
   * - ``cne_1``
     - CNE.1
     - Optional[str]
     - optional
     -
     - Identifier
   * - ``cne_2``
     - CNE.2
     - Optional[str]
     - optional
     -
     - Text
   * - ``cne_3``
     - CNE.3
     - Optional[str]
     - optional
     -
     - Name of Coding System
   * - ``cne_4``
     - CNE.4
     - Optional[str]
     - optional
     -
     - Alternate Identifier
   * - ``cne_5``
     - CNE.5
     - Optional[str]
     - optional
     -
     - Alternate Text
   * - ``cne_6``
     - CNE.6
     - Optional[str]
     - optional
     -
     - Name of Alternate Coding System
   * - ``cne_7``
     - CNE.7
     - Optional[str]
     - optional
     -
     - Coding System Version ID
   * - ``cne_8``
     - CNE.8
     - Optional[str]
     - optional
     -
     - Alternate Coding System Version ID
   * - ``cne_9``
     - CNE.9
     - Optional[str]
     - optional
     -
     - Original Text

.. _hl7-v2_5_1-CNN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CNN.CNN
   :noindex:

   HL7 v2 CNN data type.

CNN
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
   * - ``cnn_1``
     - CNN.1
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``cnn_2``
     - CNN.2
     - Optional[str]
     - optional
     -
     - Family Name
   * - ``cnn_3``
     - CNN.3
     - Optional[str]
     - optional
     -
     - Given Name
   * - ``cnn_4``
     - CNN.4
     - Optional[str]
     - optional
     -
     - Second and Further Given Names or Initials Thereof
   * - ``cnn_5``
     - CNN.5
     - Optional[str]
     - optional
     -
     - Suffix (e.g., JR or III)
   * - ``cnn_6``
     - CNN.6
     - Optional[str]
     - optional
     -
     - Prefix (e.g., DR)
   * - ``cnn_7``
     - CNN.7
     - Optional[str]
     - optional
     -
     - Degree (e.g., MD
   * - ``cnn_8``
     - CNN.8
     - Optional[str]
     - optional
     -
     - Source Table
   * - ``cnn_9``
     - CNN.9
     - Optional[str]
     - optional
     -
     - Assigning Authority   - Namespace ID
   * - ``cnn_10``
     - CNN.10
     - Optional[str]
     - optional
     -
     - Assigning Authority  - Universal ID
   * - ``cnn_11``
     - CNN.11
     - Optional[str]
     - optional
     -
     - Assigning Authority  - Universal ID Type

.. _hl7-v2_5_1-CP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CP.CP
   :noindex:

   HL7 v2 CP data type.

CP
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cp_1``
     - CP.1
     - Optional[:ref:`MO <hl7-v2_5_1-MO>`]
     - optional
     -
     - Price
   * - ``cp_2``
     - CP.2
     - Optional[str]
     - optional
     -
     - Price Type
   * - ``cp_3``
     - CP.3
     - Optional[str]
     - optional
     -
     - From Value
   * - ``cp_4``
     - CP.4
     - Optional[str]
     - optional
     -
     - To Value
   * - ``cp_5``
     - CP.5
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Range Units
   * - ``cp_6``
     - CP.6
     - Optional[str]
     - optional
     -
     - Range Type

.. _hl7-v2_5_1-CQ:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CQ.CQ
   :noindex:

   HL7 v2 CQ data type.

CQ
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cq_1``
     - CQ.1
     - Optional[str]
     - optional
     -
     - Quantity
   * - ``cq_2``
     - CQ.2
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Units

.. _hl7-v2_5_1-CSU:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CSU.CSU
   :noindex:

   HL7 v2 CSU data type.

CSU
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
   * - ``csu_1``
     - CSU.1
     - Optional[str]
     - optional
     -
     - Channel Sensitivity
   * - ``csu_2``
     - CSU.2
     - Optional[str]
     - optional
     -
     - Unit of Measure Identifier
   * - ``csu_3``
     - CSU.3
     - Optional[str]
     - optional
     -
     - Unit of Measure Description
   * - ``csu_4``
     - CSU.4
     - Optional[str]
     - optional
     -
     - Unit of Measure Coding System
   * - ``csu_5``
     - CSU.5
     - Optional[str]
     - optional
     -
     - Alternate Unit of Measure Identifier
   * - ``csu_6``
     - CSU.6
     - Optional[str]
     - optional
     -
     - Alternate Unit of Measure Description
   * - ``csu_7``
     - CSU.7
     - Optional[str]
     - optional
     -
     - Alternate Unit of Measure Coding System

.. _hl7-v2_5_1-CWE:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CWE.CWE
   :noindex:

   HL7 v2 CWE data type.

CWE
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
   * - ``cwe_1``
     - CWE.1
     - Optional[str]
     - optional
     -
     - Identifier
   * - ``cwe_2``
     - CWE.2
     - Optional[str]
     - optional
     -
     - Text
   * - ``cwe_3``
     - CWE.3
     - Optional[str]
     - optional
     -
     - Name of Coding System
   * - ``cwe_4``
     - CWE.4
     - Optional[str]
     - optional
     -
     - Alternate Identifier
   * - ``cwe_5``
     - CWE.5
     - Optional[str]
     - optional
     -
     - Alternate Text
   * - ``cwe_6``
     - CWE.6
     - Optional[str]
     - optional
     -
     - Name of Alternate Coding System
   * - ``cwe_7``
     - CWE.7
     - Optional[str]
     - optional
     -
     - Coding System Version ID
   * - ``cwe_8``
     - CWE.8
     - Optional[str]
     - optional
     -
     - Alternate Coding System Version ID
   * - ``cwe_9``
     - CWE.9
     - Optional[str]
     - optional
     -
     - Original Text

.. _hl7-v2_5_1-CX:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.CX.CX
   :noindex:

   HL7 v2 CX data type.

CX
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``cx_1``
     - CX.1
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``cx_2``
     - CX.2
     - Optional[str]
     - optional
     -
     - Check Digit
   * - ``cx_3``
     - CX.3
     - Optional[str]
     - optional
     -
     - Check Digit Scheme
   * - ``cx_4``
     - CX.4
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Authority
   * - ``cx_5``
     - CX.5
     - Optional[str]
     - optional
     -
     - Identifier Type Code
   * - ``cx_6``
     - CX.6
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Facility
   * - ``cx_7``
     - CX.7
     - Optional[str]
     - optional
     -
     - Effective Date
   * - ``cx_8``
     - CX.8
     - Optional[str]
     - optional
     -
     - Expiration Date
   * - ``cx_9``
     - CX.9
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Jurisdiction
   * - ``cx_10``
     - CX.10
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Agency or Department

.. _hl7-v2_5_1-DDI:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DDI.DDI
   :noindex:

   HL7 v2 DDI data type.

DDI
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
   * - ``ddi_1``
     - DDI.1
     - Optional[str]
     - optional
     -
     - Delay Days
   * - ``ddi_2``
     - DDI.2
     - Optional[:ref:`MO <hl7-v2_5_1-MO>`]
     - optional
     -
     - Monetary Amount
   * - ``ddi_3``
     - DDI.3
     - Optional[str]
     - optional
     -
     - Number of Days

.. _hl7-v2_5_1-DIN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DIN.DIN
   :noindex:

   HL7 v2 DIN data type.

DIN
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
   * - ``din_1``
     - DIN.1
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Date
   * - ``din_2``
     - DIN.2
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Institution Name

.. _hl7-v2_5_1-DLD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLD.DLD
   :noindex:

   HL7 v2 DLD data type.

DLD
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
   * - ``dld_1``
     - DLD.1
     - Optional[str]
     - optional
     -
     - Discharge Location
   * - ``dld_2``
     - DLD.2
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date

.. _hl7-v2_5_1-DLN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLN.DLN
   :noindex:

   HL7 v2 DLN data type.

DLN
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
   * - ``dln_1``
     - DLN.1
     - Optional[str]
     - optional
     -
     - License Number
   * - ``dln_2``
     - DLN.2
     - Optional[str]
     - optional
     -
     - Issuing State, Province, Country
   * - ``dln_3``
     - DLN.3
     - Optional[str]
     - optional
     -
     - Expiration Date

.. _hl7-v2_5_1-DLT:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DLT.DLT
   :noindex:

   HL7 v2 DLT data type.

DLT
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
   * - ``dlt_1``
     - DLT.1
     - Optional[:ref:`NR <hl7-v2_5_1-NR>`]
     - optional
     -
     - Normal Range
   * - ``dlt_2``
     - DLT.2
     - Optional[str]
     - optional
     -
     - Numeric Threshold
   * - ``dlt_3``
     - DLT.3
     - Optional[str]
     - optional
     -
     - Change Computation
   * - ``dlt_4``
     - DLT.4
     - Optional[str]
     - optional
     -
     - Days Retained

.. _hl7-v2_5_1-DR:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DR.DR
   :noindex:

   HL7 v2 DR data type.

DR
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``dr_1``
     - DR.1
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Range Start Date/Time
   * - ``dr_2``
     - DR.2
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Range End Date/Time

.. _hl7-v2_5_1-DTN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.DTN.DTN
   :noindex:

   HL7 v2 DTN data type.

DTN
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
   * - ``dtn_1``
     - DTN.1
     - Optional[str]
     - optional
     -
     - Day Type
   * - ``dtn_2``
     - DTN.2
     - Optional[str]
     - optional
     -
     - Number of Days

.. _hl7-v2_5_1-ED:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ED.ED
   :noindex:

   HL7 v2 ED data type.

ED
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ed_1``
     - ED.1
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Source Application
   * - ``ed_2``
     - ED.2
     - Optional[str]
     - optional
     -
     - Type of Data
   * - ``ed_3``
     - ED.3
     - Optional[str]
     - optional
     -
     - Data Subtype
   * - ``ed_4``
     - ED.4
     - Optional[str]
     - optional
     -
     - Encoding
   * - ``ed_5``
     - ED.5
     - Optional[str]
     - optional
     -
     - Data

.. _hl7-v2_5_1-EI:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.EI.EI
   :noindex:

   HL7 v2 EI data type.

EI
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ei_1``
     - EI.1
     - Optional[str]
     - optional
     -
     - Entity Identifier
   * - ``ei_2``
     - EI.2
     - Optional[str]
     - optional
     -
     - Namespace ID
   * - ``ei_3``
     - EI.3
     - Optional[str]
     - optional
     -
     - Universal ID
   * - ``ei_4``
     - EI.4
     - Optional[str]
     - optional
     -
     - Universal ID Type

.. _hl7-v2_5_1-EIP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.EIP.EIP
   :noindex:

   HL7 v2 EIP data type.

EIP
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
   * - ``eip_1``
     - EIP.1
     - Optional[:ref:`EI <hl7-v2_5_1-EI>`]
     - optional
     -
     - Placer Assigned Identifier
   * - ``eip_2``
     - EIP.2
     - Optional[:ref:`EI <hl7-v2_5_1-EI>`]
     - optional
     -
     - Filler Assigned Identifier

.. _hl7-v2_5_1-ELD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ELD.ELD
   :noindex:

   HL7 v2 ELD data type.

ELD
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
   * - ``eld_1``
     - ELD.1
     - Optional[str]
     - optional
     -
     - Segment ID
   * - ``eld_2``
     - ELD.2
     - Optional[str]
     - optional
     -
     - Segment Sequence
   * - ``eld_3``
     - ELD.3
     - Optional[str]
     - optional
     -
     - Field Position
   * - ``eld_4``
     - ELD.4
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Code Identifying Error

.. _hl7-v2_5_1-ERL:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ERL.ERL
   :noindex:

   HL7 v2 ERL data type.

ERL
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
   * - ``erl_1``
     - ERL.1
     - Optional[str]
     - optional
     -
     - Segment ID
   * - ``erl_2``
     - ERL.2
     - Optional[str]
     - optional
     -
     - Segment Sequence
   * - ``erl_3``
     - ERL.3
     - Optional[str]
     - optional
     -
     - Field Position
   * - ``erl_4``
     - ERL.4
     - Optional[str]
     - optional
     -
     - Field Repetition
   * - ``erl_5``
     - ERL.5
     - Optional[str]
     - optional
     -
     - Component Number
   * - ``erl_6``
     - ERL.6
     - Optional[str]
     - optional
     -
     - Sub-Component Number

.. _hl7-v2_5_1-FC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.FC.FC
   :noindex:

   HL7 v2 FC data type.

FC
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``fc_1``
     - FC.1
     - Optional[str]
     - optional
     -
     - Financial Class Code
   * - ``fc_2``
     - FC.2
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date

.. _hl7-v2_5_1-FN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.FN.FN
   :noindex:

   HL7 v2 FN data type.

FN
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``fn_1``
     - FN.1
     - Optional[str]
     - optional
     -
     - Surname
   * - ``fn_2``
     - FN.2
     - Optional[str]
     - optional
     -
     - Own Surname Prefix
   * - ``fn_3``
     - FN.3
     - Optional[str]
     - optional
     -
     - Own Surname
   * - ``fn_4``
     - FN.4
     - Optional[str]
     - optional
     -
     - Surname Prefix From Partner/Spouse
   * - ``fn_5``
     - FN.5
     - Optional[str]
     - optional
     -
     - Surname From Partner/Spouse

.. _hl7-v2_5_1-HD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.HD.HD
   :noindex:

   HL7 v2 HD data type.

HD
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``hd_1``
     - HD.1
     - Optional[str]
     - optional
     -
     - Namespace ID
   * - ``hd_2``
     - HD.2
     - Optional[str]
     - optional
     -
     - Universal ID
   * - ``hd_3``
     - HD.3
     - Optional[str]
     - optional
     -
     - Universal ID Type

.. _hl7-v2_5_1-ICD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.ICD.ICD
   :noindex:

   HL7 v2 ICD data type.

ICD
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
   * - ``icd_1``
     - ICD.1
     - Optional[str]
     - optional
     -
     - Certification Patient Type
   * - ``icd_2``
     - ICD.2
     - Optional[str]
     - optional
     -
     - Certification Required
   * - ``icd_3``
     - ICD.3
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Date/Time Certification Required

.. _hl7-v2_5_1-JCC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.JCC.JCC
   :noindex:

   HL7 v2 JCC data type.

JCC
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
   * - ``jcc_1``
     - JCC.1
     - Optional[str]
     - optional
     -
     - Job Code
   * - ``jcc_2``
     - JCC.2
     - Optional[str]
     - optional
     -
     - Job Class
   * - ``jcc_3``
     - JCC.3
     - Optional[str]
     - optional
     -
     - Job Description Text

.. _hl7-v2_5_1-LA1:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.LA1.LA1
   :noindex:

   HL7 v2 LA1 data type.

LA1
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
   * - ``la1_1``
     - LA1.1
     - Optional[str]
     - optional
     -
     - Point of Care
   * - ``la1_2``
     - LA1.2
     - Optional[str]
     - optional
     -
     - Room
   * - ``la1_3``
     - LA1.3
     - Optional[str]
     - optional
     -
     - Bed
   * - ``la1_4``
     - LA1.4
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Facility
   * - ``la1_5``
     - LA1.5
     - Optional[str]
     - optional
     -
     - Location Status
   * - ``la1_6``
     - LA1.6
     - Optional[str]
     - optional
     -
     - Patient Location Type
   * - ``la1_7``
     - LA1.7
     - Optional[str]
     - optional
     -
     - Building
   * - ``la1_8``
     - LA1.8
     - Optional[str]
     - optional
     -
     - Floor
   * - ``la1_9``
     - LA1.9
     - Optional[:ref:`AD <hl7-v2_5_1-AD>`]
     - optional
     -
     - Address

.. _hl7-v2_5_1-LA2:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.LA2.LA2
   :noindex:

   HL7 v2 LA2 data type.

LA2
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
   * - ``la2_1``
     - LA2.1
     - Optional[str]
     - optional
     -
     - Point of Care
   * - ``la2_2``
     - LA2.2
     - Optional[str]
     - optional
     -
     - Room
   * - ``la2_3``
     - LA2.3
     - Optional[str]
     - optional
     -
     - Bed
   * - ``la2_4``
     - LA2.4
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Facility
   * - ``la2_5``
     - LA2.5
     - Optional[str]
     - optional
     -
     - Location Status
   * - ``la2_6``
     - LA2.6
     - Optional[str]
     - optional
     -
     - Patient Location Type
   * - ``la2_7``
     - LA2.7
     - Optional[str]
     - optional
     -
     - Building
   * - ``la2_8``
     - LA2.8
     - Optional[str]
     - optional
     -
     - Floor
   * - ``la2_9``
     - LA2.9
     - Optional[str]
     - optional
     -
     - Street Address
   * - ``la2_10``
     - LA2.10
     - Optional[str]
     - optional
     -
     - Other Designation
   * - ``la2_11``
     - LA2.11
     - Optional[str]
     - optional
     -
     - City
   * - ``la2_12``
     - LA2.12
     - Optional[str]
     - optional
     -
     - State or Province
   * - ``la2_13``
     - LA2.13
     - Optional[str]
     - optional
     -
     - Zip or Postal Code
   * - ``la2_14``
     - LA2.14
     - Optional[str]
     - optional
     -
     - Country
   * - ``la2_15``
     - LA2.15
     - Optional[str]
     - optional
     -
     - Address Type
   * - ``la2_16``
     - LA2.16
     - Optional[str]
     - optional
     -
     - Other Geographic Designation

.. _hl7-v2_5_1-MA:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MA.MA
   :noindex:

   HL7 v2 MA data type.

MA
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ma_1``
     - MA.1
     - Optional[str]
     - optional
     -
     - Sample 1 From Channel 1
   * - ``ma_2``
     - MA.2
     - Optional[str]
     - optional
     -
     - Sample 1 From Channel 2
   * - ``ma_3``
     - MA.3
     - Optional[str]
     - optional
     -
     - Sample 1 From Channel N
   * - ``ma_4``
     - MA.4
     - Optional[str]
     - optional
     -
     - Sample 2 From Channel 1
   * - ``ma_5``
     - MA.5
     - Optional[str]
     - optional
     -
     - Sample 2 From Channel N
   * - ``ma_6``
     - MA.6
     - Optional[str]
     - optional
     -
     - Sample N From Channel N

.. _hl7-v2_5_1-MO:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MO.MO
   :noindex:

   HL7 v2 MO data type.

MO
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``mo_1``
     - MO.1
     - Optional[str]
     - optional
     -
     - Quantity
   * - ``mo_2``
     - MO.2
     - Optional[str]
     - optional
     -
     - Denomination

.. _hl7-v2_5_1-MOC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MOC.MOC
   :noindex:

   HL7 v2 MOC data type.

MOC
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
   * - ``moc_1``
     - MOC.1
     - Optional[:ref:`MO <hl7-v2_5_1-MO>`]
     - optional
     -
     - Monetary Amount
   * - ``moc_2``
     - MOC.2
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Charge Code

.. _hl7-v2_5_1-MOP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MOP.MOP
   :noindex:

   HL7 v2 MOP data type.

MOP
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
   * - ``mop_1``
     - MOP.1
     - Optional[str]
     - optional
     -
     - Money or Percentage Indicator
   * - ``mop_2``
     - MOP.2
     - Optional[str]
     - optional
     -
     - Money or Percentage Quantity
   * - ``mop_3``
     - MOP.3
     - Optional[str]
     - optional
     -
     - Currency Denomination

.. _hl7-v2_5_1-MSG:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.MSG.MSG
   :noindex:

   HL7 v2 MSG data type.

MSG
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
   * - ``msg_1``
     - MSG.1
     - Optional[str]
     - optional
     -
     - Message Code
   * - ``msg_2``
     - MSG.2
     - Optional[str]
     - optional
     -
     - Trigger Event
   * - ``msg_3``
     - MSG.3
     - Optional[str]
     - optional
     -
     - Message Structure

.. _hl7-v2_5_1-NA:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NA.NA
   :noindex:

   HL7 v2 NA data type.

NA
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``na_1``
     - NA.1
     - Optional[str]
     - optional
     -
     - Value1
   * - ``na_2``
     - NA.2
     - Optional[str]
     - optional
     -
     - Value2
   * - ``na_3``
     - NA.3
     - Optional[str]
     - optional
     -
     - Value3
   * - ``na_4``
     - NA.4
     - Optional[str]
     - optional
     -
     - Value4

.. _hl7-v2_5_1-NDL:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NDL.NDL
   :noindex:

   HL7 v2 NDL data type.

NDL
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
   * - ``ndl_1``
     - NDL.1
     - Optional[:ref:`CNN <hl7-v2_5_1-CNN>`]
     - optional
     -
     - Name
   * - ``ndl_2``
     - NDL.2
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Start Date/time
   * - ``ndl_3``
     - NDL.3
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - End Date/time
   * - ``ndl_4``
     - NDL.4
     - Optional[str]
     - optional
     -
     - Point of Care
   * - ``ndl_5``
     - NDL.5
     - Optional[str]
     - optional
     -
     - Room
   * - ``ndl_6``
     - NDL.6
     - Optional[str]
     - optional
     -
     - Bed
   * - ``ndl_7``
     - NDL.7
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Facility
   * - ``ndl_8``
     - NDL.8
     - Optional[str]
     - optional
     -
     - Location Status
   * - ``ndl_9``
     - NDL.9
     - Optional[str]
     - optional
     -
     - Patient Location Type
   * - ``ndl_10``
     - NDL.10
     - Optional[str]
     - optional
     -
     - Building
   * - ``ndl_11``
     - NDL.11
     - Optional[str]
     - optional
     -
     - Floor

.. _hl7-v2_5_1-NR:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.NR.NR
   :noindex:

   HL7 v2 NR data type.

NR
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``nr_1``
     - NR.1
     - Optional[str]
     - optional
     -
     - Low Value
   * - ``nr_2``
     - NR.2
     - Optional[str]
     - optional
     -
     - High Value

.. _hl7-v2_5_1-OCD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OCD.OCD
   :noindex:

   HL7 v2 OCD data type.

OCD
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
   * - ``ocd_1``
     - OCD.1
     - Optional[:ref:`CNE <hl7-v2_5_1-CNE>`]
     - optional
     -
     - Occurrence Code
   * - ``ocd_2``
     - OCD.2
     - Optional[str]
     - optional
     -
     - Occurrence Date

.. _hl7-v2_5_1-OSD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OSD.OSD
   :noindex:

   HL7 v2 OSD data type.

OSD
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
   * - ``osd_1``
     - OSD.1
     - Optional[str]
     - optional
     -
     - Sequence/Results Flag
   * - ``osd_2``
     - OSD.2
     - Optional[str]
     - optional
     -
     - Placer Order Number: Entity Identifier
   * - ``osd_3``
     - OSD.3
     - Optional[str]
     - optional
     -
     - Placer Order Number: Namespace ID
   * - ``osd_4``
     - OSD.4
     - Optional[str]
     - optional
     -
     - Filler Order Number: Entity Identifier
   * - ``osd_5``
     - OSD.5
     - Optional[str]
     - optional
     -
     - Filler Order Number: Namespace ID
   * - ``osd_6``
     - OSD.6
     - Optional[str]
     - optional
     -
     - Sequence Condition Value
   * - ``osd_7``
     - OSD.7
     - Optional[str]
     - optional
     -
     - Maximum Number of Repeats
   * - ``osd_8``
     - OSD.8
     - Optional[str]
     - optional
     -
     - Placer Order Number: Universal ID
   * - ``osd_9``
     - OSD.9
     - Optional[str]
     - optional
     -
     - Placer Order Number: Universal ID Type
   * - ``osd_10``
     - OSD.10
     - Optional[str]
     - optional
     -
     - Filler Order Number: Universal ID
   * - ``osd_11``
     - OSD.11
     - Optional[str]
     - optional
     -
     - Filler Order Number: Universal ID Type

.. _hl7-v2_5_1-OSP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.OSP.OSP
   :noindex:

   HL7 v2 OSP data type.

OSP
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
   * - ``osp_1``
     - OSP.1
     - Optional[:ref:`CNE <hl7-v2_5_1-CNE>`]
     - optional
     -
     - Occurrence Span Code
   * - ``osp_2``
     - OSP.2
     - Optional[str]
     - optional
     -
     - Occurrence Span Start Date
   * - ``osp_3``
     - OSP.3
     - Optional[str]
     - optional
     -
     - Occurrence Span Stop Date

.. _hl7-v2_5_1-PIP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PIP.PIP
   :noindex:

   HL7 v2 PIP data type.

PIP
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
   * - ``pip_1``
     - PIP.1
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Privilege
   * - ``pip_2``
     - PIP.2
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Privilege Class
   * - ``pip_3``
     - PIP.3
     - Optional[str]
     - optional
     -
     - Expiration Date
   * - ``pip_4``
     - PIP.4
     - Optional[str]
     - optional
     -
     - Activation Date
   * - ``pip_5``
     - PIP.5
     - Optional[:ref:`EI <hl7-v2_5_1-EI>`]
     - optional
     -
     - Facility

.. _hl7-v2_5_1-PL:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PL.PL
   :noindex:

   HL7 v2 PL data type.

PL
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pl_1``
     - PL.1
     - Optional[str]
     - optional
     -
     - Point of Care
   * - ``pl_2``
     - PL.2
     - Optional[str]
     - optional
     -
     - Room
   * - ``pl_3``
     - PL.3
     - Optional[str]
     - optional
     -
     - Bed
   * - ``pl_4``
     - PL.4
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Facility
   * - ``pl_5``
     - PL.5
     - Optional[str]
     - optional
     -
     - Location Status
   * - ``pl_6``
     - PL.6
     - Optional[str]
     - optional
     -
     - Person Location Type
   * - ``pl_7``
     - PL.7
     - Optional[str]
     - optional
     -
     - Building
   * - ``pl_8``
     - PL.8
     - Optional[str]
     - optional
     -
     - Floor
   * - ``pl_9``
     - PL.9
     - Optional[str]
     - optional
     -
     - Location Description
   * - ``pl_10``
     - PL.10
     - Optional[:ref:`EI <hl7-v2_5_1-EI>`]
     - optional
     -
     - Comprehensive Location Identifier
   * - ``pl_11``
     - PL.11
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Authority for Location

.. _hl7-v2_5_1-PLN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PLN.PLN
   :noindex:

   HL7 v2 PLN data type.

PLN
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
   * - ``pln_1``
     - PLN.1
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``pln_2``
     - PLN.2
     - Optional[str]
     - optional
     -
     - Type of ID Number
   * - ``pln_3``
     - PLN.3
     - Optional[str]
     - optional
     -
     - State/other Qualifying Information
   * - ``pln_4``
     - PLN.4
     - Optional[str]
     - optional
     -
     - Expiration Date

.. _hl7-v2_5_1-PPN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PPN.PPN
   :noindex:

   HL7 v2 PPN data type.

PPN
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
   * - ``ppn_1``
     - PPN.1
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``ppn_2``
     - PPN.2
     - Optional[:ref:`FN <hl7-v2_5_1-FN>`]
     - optional
     -
     - Family Name
   * - ``ppn_3``
     - PPN.3
     - Optional[str]
     - optional
     -
     - Given Name
   * - ``ppn_4``
     - PPN.4
     - Optional[str]
     - optional
     -
     - Second and Further Given Names or Initials Thereof
   * - ``ppn_5``
     - PPN.5
     - Optional[str]
     - optional
     -
     - Suffix (e.g., JR or III)
   * - ``ppn_6``
     - PPN.6
     - Optional[str]
     - optional
     -
     - Prefix (e.g., DR)
   * - ``ppn_7``
     - PPN.7
     - Optional[str]
     - optional
     -
     - Degree (e.g., MD)
   * - ``ppn_8``
     - PPN.8
     - Optional[str]
     - optional
     -
     - Source Table
   * - ``ppn_9``
     - PPN.9
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Authority
   * - ``ppn_10``
     - PPN.10
     - Optional[str]
     - optional
     -
     - Name Type Code
   * - ``ppn_11``
     - PPN.11
     - Optional[str]
     - optional
     -
     - Identifier Check Digit
   * - ``ppn_12``
     - PPN.12
     - Optional[str]
     - optional
     -
     - Check Digit Scheme
   * - ``ppn_13``
     - PPN.13
     - Optional[str]
     - optional
     -
     - Identifier Type Code
   * - ``ppn_14``
     - PPN.14
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Facility
   * - ``ppn_15``
     - PPN.15
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Date/Time Action Performed
   * - ``ppn_16``
     - PPN.16
     - Optional[str]
     - optional
     -
     - Name Representation Code
   * - ``ppn_17``
     - PPN.17
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Name Context
   * - ``ppn_18``
     - PPN.18
     - Optional[:ref:`DR <hl7-v2_5_1-DR>`]
     - optional
     -
     - Name Validity Range
   * - ``ppn_19``
     - PPN.19
     - Optional[str]
     - optional
     -
     - Name Assembly Order
   * - ``ppn_20``
     - PPN.20
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date
   * - ``ppn_21``
     - PPN.21
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Expiration Date
   * - ``ppn_22``
     - PPN.22
     - Optional[str]
     - optional
     -
     - Professional Suffix
   * - ``ppn_23``
     - PPN.23
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Jurisdiction
   * - ``ppn_24``
     - PPN.24
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Agency or Department

.. _hl7-v2_5_1-PRL:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PRL.PRL
   :noindex:

   HL7 v2 PRL data type.

PRL
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
   * - ``prl_1``
     - PRL.1
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Parent Observation Identifier
   * - ``prl_2``
     - PRL.2
     - Optional[str]
     - optional
     -
     - Parent Observation Sub-identifier
   * - ``prl_3``
     - PRL.3
     - Optional[str]
     - optional
     -
     - Parent Observation Value Descriptor

.. _hl7-v2_5_1-PT:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PT.PT
   :noindex:

   HL7 v2 PT data type.

PT
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``pt_1``
     - PT.1
     - Optional[str]
     - optional
     -
     - Processing ID
   * - ``pt_2``
     - PT.2
     - Optional[str]
     - optional
     -
     - Processing Mode

.. _hl7-v2_5_1-PTA:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.PTA.PTA
   :noindex:

   HL7 v2 PTA data type.

PTA
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
   * - ``pta_1``
     - PTA.1
     - Optional[str]
     - optional
     -
     - Policy Type
   * - ``pta_2``
     - PTA.2
     - Optional[str]
     - optional
     -
     - Amount Class
   * - ``pta_3``
     - PTA.3
     - Optional[str]
     - optional
     -
     - Money or Percentage Quantity
   * - ``pta_4``
     - PTA.4
     - Optional[:ref:`MOP <hl7-v2_5_1-MOP>`]
     - optional
     -
     - Money or Percentage

.. _hl7-v2_5_1-QIP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.QIP.QIP
   :noindex:

   HL7 v2 QIP data type.

QIP
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
   * - ``qip_1``
     - QIP.1
     - Optional[str]
     - optional
     -
     - Segment Field Name
   * - ``qip_2``
     - QIP.2
     - Optional[str]
     - optional
     -
     - Values

.. _hl7-v2_5_1-QSC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.QSC.QSC
   :noindex:

   HL7 v2 QSC data type.

QSC
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
   * - ``qsc_1``
     - QSC.1
     - Optional[str]
     - optional
     -
     - Segment Field Name
   * - ``qsc_2``
     - QSC.2
     - Optional[str]
     - optional
     -
     - Relational Operator
   * - ``qsc_3``
     - QSC.3
     - Optional[str]
     - optional
     -
     - Value
   * - ``qsc_4``
     - QSC.4
     - Optional[str]
     - optional
     -
     - Relational Conjunction

.. _hl7-v2_5_1-RCD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RCD.RCD
   :noindex:

   HL7 v2 RCD data type.

RCD
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
   * - ``rcd_1``
     - RCD.1
     - Optional[str]
     - optional
     -
     - Segment Field Name
   * - ``rcd_2``
     - RCD.2
     - Optional[str]
     - optional
     -
     - HL7 Data Type
   * - ``rcd_3``
     - RCD.3
     - Optional[str]
     - optional
     -
     - Maximum Column Width

.. _hl7-v2_5_1-RFR:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RFR.RFR
   :noindex:

   HL7 v2 RFR data type.

RFR
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
   * - ``rfr_1``
     - RFR.1
     - Optional[:ref:`NR <hl7-v2_5_1-NR>`]
     - optional
     -
     - Numeric Range
   * - ``rfr_2``
     - RFR.2
     - Optional[str]
     - optional
     -
     - Administrative Sex
   * - ``rfr_3``
     - RFR.3
     - Optional[:ref:`NR <hl7-v2_5_1-NR>`]
     - optional
     -
     - Age Range
   * - ``rfr_4``
     - RFR.4
     - Optional[:ref:`NR <hl7-v2_5_1-NR>`]
     - optional
     -
     - Gestational Age Range
   * - ``rfr_5``
     - RFR.5
     - Optional[str]
     - optional
     -
     - Species
   * - ``rfr_6``
     - RFR.6
     - Optional[str]
     - optional
     -
     - Race/subspecies
   * - ``rfr_7``
     - RFR.7
     - Optional[str]
     - optional
     -
     - Conditions

.. _hl7-v2_5_1-RI:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RI.RI
   :noindex:

   HL7 v2 RI data type.

RI
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ri_1``
     - RI.1
     - Optional[str]
     - optional
     -
     - Repeat Pattern
   * - ``ri_2``
     - RI.2
     - Optional[str]
     - optional
     -
     - Explicit Time Interval

.. _hl7-v2_5_1-RMC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RMC.RMC
   :noindex:

   HL7 v2 RMC data type.

RMC
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
   * - ``rmc_1``
     - RMC.1
     - Optional[str]
     - optional
     -
     - Room Type
   * - ``rmc_2``
     - RMC.2
     - Optional[str]
     - optional
     -
     - Amount Type
   * - ``rmc_3``
     - RMC.3
     - Optional[str]
     - optional
     -
     - Coverage Amount
   * - ``rmc_4``
     - RMC.4
     - Optional[:ref:`MOP <hl7-v2_5_1-MOP>`]
     - optional
     -
     - Money or Percentage

.. _hl7-v2_5_1-RP:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RP.RP
   :noindex:

   HL7 v2 RP data type.

RP
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``rp_1``
     - RP.1
     - Optional[str]
     - optional
     -
     - Pointer
   * - ``rp_2``
     - RP.2
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Application ID
   * - ``rp_3``
     - RP.3
     - Optional[str]
     - optional
     -
     - Type of Data
   * - ``rp_4``
     - RP.4
     - Optional[str]
     - optional
     -
     - Subtype

.. _hl7-v2_5_1-RPT:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.RPT.RPT
   :noindex:

   HL7 v2 RPT data type.

RPT
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
   * - ``rpt_1``
     - RPT.1
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Repeat Pattern Code
   * - ``rpt_2``
     - RPT.2
     - Optional[str]
     - optional
     -
     - Calendar Alignment
   * - ``rpt_3``
     - RPT.3
     - Optional[str]
     - optional
     -
     - Phase Range Begin Value
   * - ``rpt_4``
     - RPT.4
     - Optional[str]
     - optional
     -
     - Phase Range End Value
   * - ``rpt_5``
     - RPT.5
     - Optional[str]
     - optional
     -
     - Period Quantity
   * - ``rpt_6``
     - RPT.6
     - Optional[str]
     - optional
     -
     - Period Units
   * - ``rpt_7``
     - RPT.7
     - Optional[str]
     - optional
     -
     - Institution Specified Time
   * - ``rpt_8``
     - RPT.8
     - Optional[str]
     - optional
     -
     - Event
   * - ``rpt_9``
     - RPT.9
     - Optional[str]
     - optional
     -
     - Event Offset Quantity
   * - ``rpt_10``
     - RPT.10
     - Optional[str]
     - optional
     -
     - Event Offset Units
   * - ``rpt_11``
     - RPT.11
     - Optional[str]
     - optional
     -
     - General Timing Specification

.. _hl7-v2_5_1-SAD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SAD.SAD
   :noindex:

   HL7 v2 SAD data type.

SAD
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
   * - ``sad_1``
     - SAD.1
     - Optional[str]
     - optional
     -
     - Street or Mailing Address
   * - ``sad_2``
     - SAD.2
     - Optional[str]
     - optional
     -
     - Street Name
   * - ``sad_3``
     - SAD.3
     - Optional[str]
     - optional
     -
     - Dwelling Number

.. _hl7-v2_5_1-SCV:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SCV.SCV
   :noindex:

   HL7 v2 SCV data type.

SCV
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
   * - ``scv_1``
     - SCV.1
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Parameter Class
   * - ``scv_2``
     - SCV.2
     - Optional[str]
     - optional
     -
     - Parameter Value

.. _hl7-v2_5_1-SN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SN.SN
   :noindex:

   HL7 v2 SN data type.

SN
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``sn_1``
     - SN.1
     - Optional[str]
     - optional
     -
     - Comparator
   * - ``sn_2``
     - SN.2
     - Optional[str]
     - optional
     -
     - Num1
   * - ``sn_3``
     - SN.3
     - Optional[str]
     - optional
     -
     - Separator/Suffix
   * - ``sn_4``
     - SN.4
     - Optional[str]
     - optional
     -
     - Num2

.. _hl7-v2_5_1-SPD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SPD.SPD
   :noindex:

   HL7 v2 SPD data type.

SPD
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
   * - ``spd_1``
     - SPD.1
     - Optional[str]
     - optional
     -
     - Specialty Name
   * - ``spd_2``
     - SPD.2
     - Optional[str]
     - optional
     -
     - Governing Board
   * - ``spd_3``
     - SPD.3
     - Optional[str]
     - optional
     -
     - Eligible or Certified
   * - ``spd_4``
     - SPD.4
     - Optional[str]
     - optional
     -
     - Date of Certification

.. _hl7-v2_5_1-SPS:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SPS.SPS
   :noindex:

   HL7 v2 SPS data type.

SPS
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
   * - ``sps_1``
     - SPS.1
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Specimen Source Name or Code
   * - ``sps_2``
     - SPS.2
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Additives
   * - ``sps_3``
     - SPS.3
     - Optional[str]
     - optional
     -
     - Specimen Collection Method
   * - ``sps_4``
     - SPS.4
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Body Site
   * - ``sps_5``
     - SPS.5
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Site Modifier
   * - ``sps_6``
     - SPS.6
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Collection Method Modifier Code
   * - ``sps_7``
     - SPS.7
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Specimen Role

.. _hl7-v2_5_1-SRT:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.SRT.SRT
   :noindex:

   HL7 v2 SRT data type.

SRT
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
   * - ``srt_1``
     - SRT.1
     - Optional[str]
     - optional
     -
     - Sort-by Field
   * - ``srt_2``
     - SRT.2
     - Optional[str]
     - optional
     -
     - Sequencing

.. _hl7-v2_5_1-TQ:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.TQ.TQ
   :noindex:

   HL7 v2 TQ data type.

TQ
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``tq_1``
     - TQ.1
     - Optional[:ref:`CQ <hl7-v2_5_1-CQ>`]
     - optional
     -
     - Quantity
   * - ``tq_2``
     - TQ.2
     - Optional[:ref:`RI <hl7-v2_5_1-RI>`]
     - optional
     -
     - Interval
   * - ``tq_3``
     - TQ.3
     - Optional[str]
     - optional
     -
     - Duration
   * - ``tq_4``
     - TQ.4
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Start Date/Time
   * - ``tq_5``
     - TQ.5
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - End Date/Time
   * - ``tq_6``
     - TQ.6
     - Optional[str]
     - optional
     -
     - Priority
   * - ``tq_7``
     - TQ.7
     - Optional[str]
     - optional
     -
     - Condition
   * - ``tq_8``
     - TQ.8
     - Optional[str]
     - optional
     -
     - Text
   * - ``tq_9``
     - TQ.9
     - Optional[str]
     - optional
     -
     - Conjunction
   * - ``tq_10``
     - TQ.10
     - Optional[:ref:`OSD <hl7-v2_5_1-OSD>`]
     - optional
     -
     - Order Sequencing
   * - ``tq_11``
     - TQ.11
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Occurrence Duration
   * - ``tq_12``
     - TQ.12
     - Optional[str]
     - optional
     -
     - Total Occurrences

.. _hl7-v2_5_1-TS:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.TS.TS
   :noindex:

   HL7 v2 TS data type.

TS
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``ts_1``
     - TS.1
     - Optional[str]
     - optional
     -
     - Time
   * - ``ts_2``
     - TS.2
     - Optional[str]
     - optional
     -
     - Degree of Precision

.. _hl7-v2_5_1-UVC:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.UVC.UVC
   :noindex:

   HL7 v2 UVC data type.

UVC
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
   * - ``uvc_1``
     - UVC.1
     - Optional[:ref:`CNE <hl7-v2_5_1-CNE>`]
     - optional
     -
     - Value Code
   * - ``uvc_2``
     - UVC.2
     - Optional[:ref:`MO <hl7-v2_5_1-MO>`]
     - optional
     -
     - Value Amount

.. _hl7-v2_5_1-VH:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VH.VH
   :noindex:

   HL7 v2 VH data type.

VH
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``vh_1``
     - VH.1
     - Optional[str]
     - optional
     -
     - Start Day Range
   * - ``vh_2``
     - VH.2
     - Optional[str]
     - optional
     -
     - End Day Range
   * - ``vh_3``
     - VH.3
     - Optional[str]
     - optional
     -
     - Start Hour Range
   * - ``vh_4``
     - VH.4
     - Optional[str]
     - optional
     -
     - End Hour Range

.. _hl7-v2_5_1-VID:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VID.VID
   :noindex:

   HL7 v2 VID data type.

VID
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
   * - ``vid_1``
     - VID.1
     - Optional[str]
     - optional
     -
     - Version ID
   * - ``vid_2``
     - VID.2
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Internationalization Code
   * - ``vid_3``
     - VID.3
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - International Version ID

.. _hl7-v2_5_1-VR:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.VR.VR
   :noindex:

   HL7 v2 VR data type.

VR
~~

.. list-table::
   :header-rows: 1
   :widths: auto

   * - Field
     - HL7
     - Type
     - Required
     - Max Length
     - Description
   * - ``vr_1``
     - VR.1
     - Optional[str]
     - optional
     -
     - First Data Code Value
   * - ``vr_2``
     - VR.2
     - Optional[str]
     - optional
     -
     - Last Data Code Value

.. _hl7-v2_5_1-WVI:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.WVI.WVI
   :noindex:

   HL7 v2 WVI data type.

WVI
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
   * - ``wvi_1``
     - WVI.1
     - Optional[str]
     - optional
     -
     - Channel Number
   * - ``wvi_2``
     - WVI.2
     - Optional[str]
     - optional
     -
     - Channel Name

.. _hl7-v2_5_1-WVS:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.WVS.WVS
   :noindex:

   HL7 v2 WVS data type.

WVS
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
   * - ``wvs_1``
     - WVS.1
     - Optional[str]
     - optional
     -
     - Source One Name
   * - ``wvs_2``
     - WVS.2
     - Optional[str]
     - optional
     -
     - Source Two Name

.. _hl7-v2_5_1-XAD:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XAD.XAD
   :noindex:

   HL7 v2 XAD data type.

XAD
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
   * - ``xad_1``
     - XAD.1
     - Optional[:ref:`SAD <hl7-v2_5_1-SAD>`]
     - optional
     -
     - Street Address
   * - ``xad_2``
     - XAD.2
     - Optional[str]
     - optional
     -
     - Other Designation
   * - ``xad_3``
     - XAD.3
     - Optional[str]
     - optional
     -
     - City
   * - ``xad_4``
     - XAD.4
     - Optional[str]
     - optional
     -
     - State or Province
   * - ``xad_5``
     - XAD.5
     - Optional[str]
     - optional
     -
     - Zip or Postal Code
   * - ``xad_6``
     - XAD.6
     - Optional[str]
     - optional
     -
     - Country
   * - ``xad_7``
     - XAD.7
     - Optional[str]
     - optional
     -
     - Address Type
   * - ``xad_8``
     - XAD.8
     - Optional[str]
     - optional
     -
     - Other Geographic Designation
   * - ``xad_9``
     - XAD.9
     - Optional[str]
     - optional
     -
     - County/Parish Code
   * - ``xad_10``
     - XAD.10
     - Optional[str]
     - optional
     -
     - Census Tract
   * - ``xad_11``
     - XAD.11
     - Optional[str]
     - optional
     -
     - Address Representation Code
   * - ``xad_12``
     - XAD.12
     - Optional[:ref:`DR <hl7-v2_5_1-DR>`]
     - optional
     -
     - Address Validity Range
   * - ``xad_13``
     - XAD.13
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date
   * - ``xad_14``
     - XAD.14
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Expiration Date

.. _hl7-v2_5_1-XCN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XCN.XCN
   :noindex:

   HL7 v2 XCN data type.

XCN
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
   * - ``xcn_1``
     - XCN.1
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``xcn_2``
     - XCN.2
     - Optional[:ref:`FN <hl7-v2_5_1-FN>`]
     - optional
     -
     - Family Name
   * - ``xcn_3``
     - XCN.3
     - Optional[str]
     - optional
     -
     - Given Name
   * - ``xcn_4``
     - XCN.4
     - Optional[str]
     - optional
     -
     - Second and Further Given Names or Initials Thereof
   * - ``xcn_5``
     - XCN.5
     - Optional[str]
     - optional
     -
     - Suffix (e.g., JR or III)
   * - ``xcn_6``
     - XCN.6
     - Optional[str]
     - optional
     -
     - Prefix (e.g., DR)
   * - ``xcn_7``
     - XCN.7
     - Optional[str]
     - optional
     -
     - Degree (e.g., MD)
   * - ``xcn_8``
     - XCN.8
     - Optional[str]
     - optional
     -
     - Source Table
   * - ``xcn_9``
     - XCN.9
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Authority
   * - ``xcn_10``
     - XCN.10
     - Optional[str]
     - optional
     -
     - Name Type Code
   * - ``xcn_11``
     - XCN.11
     - Optional[str]
     - optional
     -
     - Identifier Check Digit
   * - ``xcn_12``
     - XCN.12
     - Optional[str]
     - optional
     -
     - Check Digit Scheme
   * - ``xcn_13``
     - XCN.13
     - Optional[str]
     - optional
     -
     - Identifier Type Code
   * - ``xcn_14``
     - XCN.14
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Facility
   * - ``xcn_15``
     - XCN.15
     - Optional[str]
     - optional
     -
     - Name Representation Code
   * - ``xcn_16``
     - XCN.16
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Name Context
   * - ``xcn_17``
     - XCN.17
     - Optional[:ref:`DR <hl7-v2_5_1-DR>`]
     - optional
     -
     - Name Validity Range
   * - ``xcn_18``
     - XCN.18
     - Optional[str]
     - optional
     -
     - Name Assembly Order
   * - ``xcn_19``
     - XCN.19
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date
   * - ``xcn_20``
     - XCN.20
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Expiration Date
   * - ``xcn_21``
     - XCN.21
     - Optional[str]
     - optional
     -
     - Professional Suffix
   * - ``xcn_22``
     - XCN.22
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Jurisdiction
   * - ``xcn_23``
     - XCN.23
     - Optional[:ref:`CWE <hl7-v2_5_1-CWE>`]
     - optional
     -
     - Assigning Agency or Department

.. _hl7-v2_5_1-XON:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XON.XON
   :noindex:

   HL7 v2 XON data type.

XON
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
   * - ``xon_1``
     - XON.1
     - Optional[str]
     - optional
     -
     - Organization Name
   * - ``xon_2``
     - XON.2
     - Optional[str]
     - optional
     -
     - Organization Name Type Code
   * - ``xon_3``
     - XON.3
     - Optional[str]
     - optional
     -
     - ID Number
   * - ``xon_4``
     - XON.4
     - Optional[str]
     - optional
     -
     - Check Digit
   * - ``xon_5``
     - XON.5
     - Optional[str]
     - optional
     -
     - Check Digit Scheme
   * - ``xon_6``
     - XON.6
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Authority
   * - ``xon_7``
     - XON.7
     - Optional[str]
     - optional
     -
     - Identifier Type Code
   * - ``xon_8``
     - XON.8
     - Optional[:ref:`HD <hl7-v2_5_1-HD>`]
     - optional
     -
     - Assigning Facility
   * - ``xon_9``
     - XON.9
     - Optional[str]
     - optional
     -
     - Name Representation Code
   * - ``xon_10``
     - XON.10
     - Optional[str]
     - optional
     -
     - Organization Identifier

.. _hl7-v2_5_1-XPN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XPN.XPN
   :noindex:

   HL7 v2 XPN data type.

XPN
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
   * - ``xpn_1``
     - XPN.1
     - Optional[:ref:`FN <hl7-v2_5_1-FN>`]
     - optional
     -
     - Family Name
   * - ``xpn_2``
     - XPN.2
     - Optional[str]
     - optional
     -
     - Given Name
   * - ``xpn_3``
     - XPN.3
     - Optional[str]
     - optional
     -
     - Second and Further Given Names or Initials Thereof
   * - ``xpn_4``
     - XPN.4
     - Optional[str]
     - optional
     -
     - Suffix (e.g., JR or III)
   * - ``xpn_5``
     - XPN.5
     - Optional[str]
     - optional
     -
     - Prefix (e.g., DR)
   * - ``xpn_6``
     - XPN.6
     - Optional[str]
     - optional
     -
     - Degree (e.g., MD)
   * - ``xpn_7``
     - XPN.7
     - Optional[str]
     - optional
     -
     - Name Type Code
   * - ``xpn_8``
     - XPN.8
     - Optional[str]
     - optional
     -
     - Name Representation Code
   * - ``xpn_9``
     - XPN.9
     - Optional[:ref:`CE <hl7-v2_5_1-CE>`]
     - optional
     -
     - Name Context
   * - ``xpn_10``
     - XPN.10
     - Optional[:ref:`DR <hl7-v2_5_1-DR>`]
     - optional
     -
     - Name Validity Range
   * - ``xpn_11``
     - XPN.11
     - Optional[str]
     - optional
     -
     - Name Assembly Order
   * - ``xpn_12``
     - XPN.12
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Effective Date
   * - ``xpn_13``
     - XPN.13
     - Optional[:ref:`TS <hl7-v2_5_1-TS>`]
     - optional
     -
     - Expiration Date
   * - ``xpn_14``
     - XPN.14
     - Optional[str]
     - optional
     -
     - Professional Suffix

.. _hl7-v2_5_1-XTN:

.. py:class:: hl7types.hl7.v2_5_1.datatypes.XTN.XTN
   :noindex:

   HL7 v2 XTN data type.

XTN
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
   * - ``xtn_1``
     - XTN.1
     - Optional[str]
     - optional
     -
     - Telephone Number
   * - ``xtn_2``
     - XTN.2
     - Optional[str]
     - optional
     -
     - Telecommunication Use Code
   * - ``xtn_3``
     - XTN.3
     - Optional[str]
     - optional
     -
     - Telecommunication Equipment Type
   * - ``xtn_4``
     - XTN.4
     - Optional[str]
     - optional
     -
     - Email Address
   * - ``xtn_5``
     - XTN.5
     - Optional[str]
     - optional
     -
     - Country Code
   * - ``xtn_6``
     - XTN.6
     - Optional[str]
     - optional
     -
     - Area/City Code
   * - ``xtn_7``
     - XTN.7
     - Optional[str]
     - optional
     -
     - Local Number
   * - ``xtn_8``
     - XTN.8
     - Optional[str]
     - optional
     -
     - Extension
   * - ``xtn_9``
     - XTN.9
     - Optional[str]
     - optional
     -
     - Any Text
   * - ``xtn_10``
     - XTN.10
     - Optional[str]
     - optional
     -
     - Extension Prefix
   * - ``xtn_11``
     - XTN.11
     - Optional[str]
     - optional
     -
     - Speed Dial Code
   * - ``xtn_12``
     - XTN.12
     - Optional[str]
     - optional
     -
     - Unformatted Telephone number
