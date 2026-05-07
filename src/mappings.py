
NOT_VALUES = {
    "7701001": "Not Applicable",
    "7701003": "Not Recorded"
}

# main file, eResponse_07

RESPONSE_TYPE = {
    "2207003": "Ground",
    "2207009": "Ground",
    "2207007": "Ground",
    "2207005": "Ground",
    "2207011": "Air: Helicopter",
    "2207013": "Air: Fixed Wing"
}

# main file, eArrest_01

ARREST = {
    "3001001": "No",
    "3001003": "Yes, Prior to Any EMS Arrival",
    "3001005": "Yes, After Any EMS Arrival"
}

# main file, eArrest_02

ARREST_ETIOLOGY = {
    "3002001": "Cardiac Etiology (presumed)"
}

# main file, eArrest_07

ARREST_AED_USE_PRIOR_TO_EMS_ARRIVAL = {
    "3007001": "No",
    "3007003": "Yes, Applied without Defibrillation",
    "3007005": "Yes, with Defibrillation",
}

# main file, eArrest_11

ARREST_FIRST_MONITORED_RHYTHM = {
    "3011001": "Asystole",
    "3011005": "PEA",
    "3011007": "Unknown AED Non-Shockable Rhythm",
    "3011009": "Unknown AED Shockable Rhythm",
    "3001011": "Ventricular Fibrillation",
    "3001013": "Ventricular Tachycardia - Pulseless"
}

# main file, eArrest_18

ARREST_END_OF_EMS_CARDIAC_EVENT = {
    "3018001": "Expired in ED",
    "3018003": "Expired in the Field",
    "3018005": "Ongoing Resuscitation in ED",
    "3018007": "ROSC in the Field",
    "3018009": "ROSC in the ED",
    "3018011": "Ongoing Resuscitation by Other EMS"
}

# eArrest_03

ARREST_RESUSCITATION = {
    "3003001": "Attempted Defibrillation",
    "3003003": "Attempted Ventilation",
    "3003005": "Initiated Chest Compressions",
    "3003007": "Not Attempted- Considered Futile",
    "3003009": "Not Attempted- DNR Orders",
    "3003011": "Not Attempted- Signs of Circulation"
}

# eArrest_12

ARREST_ROSC = {
    "3012001": "No",
    "3012003": "Yes, At Arrival at the ED",
    "3012005": "Yes, Prior to Arrival at the ED",
    "3012007": "Yes, Sustained for 20 consecutive minutes"
}

# main file, eSituation_13

INITIAL_PATIENT_ACUITY = {
    "2813001": "Critical (Red)",
    "2813003": "Emergent (Yellow)",
    "2813005": "Lower Acuity (Green)",
    "2813007": "Dead without Resuscitation Efforts (Black)",
    "2813009": "Non-Acute/Routine"
}

# main file, eDisposition_19

FINAL_PATIENT_ACUITY = {
    "4219001": "Critical (Red)",
    "4219003": "Emergent (Yellow)",
    "4219005": "Lower Acuity (Green)",
    "4219007": "Dead without Resuscitation Efforts (Black)",
    "4219009": "Dead with Resuscitation Efforts (Black)",
    "4219011": "Non-Acute/Routine"
}

# emedications file, eMedications_03

MEDICATIONS = {
    "317361": "Epinephrine",
    "7806": "Oxygen",
    "7701003": "Unknown",
    "313002": "Sodium Chloride",
    "36676": "Sodium Bicarbonate",
    "1375913": "Epinephrine",
    "328316": "Epinephrine",
    "703": "Amiodarone",
    "7242": "Naloxone",
    "125464": "Unknown",
    "3992": "Epinephrine",
    "1901": "Calcium Chloride",
    "330545": "Epinephrine",
    "6387": "Lidocaine",
    "1223": "Atropine",
    "6960": "Midazolam",
    "9863": "Sodium Chloride",
    "1008377": "Lactated Ringer's",
    "310132": "Epinephrine",
    "237653": "Glucose",
    "35629": "Lactated Ringer's",
    "7512": "Norepinephrine",
    "237648": "Glucose",
    "6130": "Ketamine",
    "4337": "Fentanyl",
    "727373": "Epinephrine",
    "6585": "Magnesium Sulfate",
    "373902": "Sodium Chloride Irrigation Solution",
    "1191": "Aspirin",
    "727374": "Epinephrine",
    "1908": "Calcium Gluconate",
    "68139": "Rocuronium",
    "4177": "Etomidate",
    "1154985": "Atropine/Pralidoxime",
    "3628": "Dopamine",
    "4917": "Nitroglycerin",
    "643187": "Sodium Chloride",
    "727347": "Epinephrine",
    "10154": "Succinylcholine",
    "26225": "Ondansetron",
    "237363": "Sodium Bicarbonate",
    "203192": "Naloxone Hydrochloride",
    "352975": "Sodium Chloride",
    "203588": "Amiodarone",
    "317630": "Glucose",
    "8782": "Propofol",
    "197117": "Narcan",
    "362": "Epinephrine",
    "260258": "Glucose"
}

# eprocedures file, eProcedures_03

PROCEDURES = {
    "89666000": "CPR",
    "426220008": "Defibrillation",
    "430824005": "IO Insertion",
    "392230005": "IV Insertion",
    "429283006": "CPR",
    "425447009": "BVM Ventilation",
    "268400002": "12-Lead ECG",
    "428803005": "Cardiac Monitoring",
    "232674004": "Orotracheal Intubation",
    "425543005": "ETCO2",
    "46825001": "Cardiac Monitoring",
    "386053000": "Assessment",
    "230040009": "Airway Suction",
    "7443007": "OPA Insertion",
    "424979004": "Supraglottic Airway",
    "422618004": "Assessment",
    "304562007": "Healthcare Information Exchange",
    "23852006": "Cardiac Monitoring",
    "33747003": "BGL Check",
    "427753009": "Supraglottic Airway",
    "243140006": "BVM Ventilation",
    "673005": "Indirect Laryngoscopy",
    "284029005": "ETCO",
    "386509000": "Airway Management Unspecified",
    "182692007": "NPA Insertion",
    "440009003": "Not Available",
    "302789003": "BGL Check",
    "18590009": "Cardiac Pacing",
    "441893003": "CPR",
    "58715004": "Moving Patient to Stretcher",
    "225718003": "ET Tube Verify",
    "232664002": "Manual Airway",
    "112798008": "Awake Intubation",
    "252465000": "Pulse Oximetry",
    "182777000": "Monitoring",
    "233169004": "Defibrillation",
    "385857005": "Ventilator Care and Adjustment",
    "81375008": "Assessment",
    "398041008": "Cervical Spine Immobilization",
    "235425002": "Orogastric Tube Insertion",
    "61746007": "Vital Signs",
    "408994004": "Assessment",
    "315639002": "Assessment",
    "78121007": "Direct Laryngoscopy",
    "103744005": "Administration of IV Fluids",
    "166888009": "BGL Check",
    "386518003": "Airway Management Unspecified",
    "232679009": "Nasotracheal Intubation"
}

# esituation09 file, eSituation09 column

ICD_CHAPTER_MAP = {
    "I": "Cardiovascular",
    "J": "Respiratory",
    "S": "Injury/Trauma",
    "T": "Injury/Poisoning",
    "R": "Symptoms/Unknown",
    "E": "Endocrine/Metabolic",
    "F": "Behavioral/Mental Health",
    "O": "Pregnancy/Childbirth",
    "G": "CNS/Neuro",
    "K": "Digestive"
}