import pyreadstat
import pandas as pd
import numpy as np
from mappings import *
from collections import Counter
from functools import reduce


# clean missing values

def clean_missing(value):
    if value in ["7701001", "7701003"]:
        return np.nan
    return value

# get unique values from value lists

def get_unique(value):
    return list(set(value))

# get count for unique values in value lists

def get_count(value):
    return Counter(value)

# get epi counts

def get_epi_count(value):
    return int(value.get("Epinephrine", 0))

# get total meds/procedures

def total_count(value):
    return len(value)

# get ROSC status

def ROSC_status(value):
    return int(any("Yes" in item for item in value))

def simplify_rhythm(r):
    if pd.isna(r):
        return "Unknown"
    r = str(r)

    if "Asystole" in r:
        return "Asystole"
    elif "PEA" in r:
        return "PEA"
    elif "Non-Shockable" in r:
        return "Non-Shockable"
    elif "Shockable" in r:
        return "Shockable"
    elif "Unknown" in r:
        return "Unknown"

def build_final_dataset():

    # read files and create tables

    df_main, meta_main = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_1to1.sas7bdat"
    )

    df_meds, meta_meds = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_emedications.sas7bdat"
    )

    df_proc, meta_proc = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_eprocedures.sas7bdat"
    )

    df_arrest_resus, meta_arrest_03 = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_earrest03.sas7bdat"
    )

    df_arrest_ROSC, meta_arrest_12 = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_earrest12.sas7bdat"
    )

    df_symptoms, meta_situation_09 = pyreadstat.read_sas7bdat(
        "data/CardiacArrestPUD2023/cardiacarrestpud_esituation09.sas7bdat"
    )

    # get columns

    df = df_main[["PcrKey", "eResponse_07", "eArrest_01", "eArrest_02", "eArrest_07", "eArrest_11",
                  "eArrest_18", "eSituation_13", "eDisposition_19"]]

    df_medications = df_meds[["PcrKey", "eMedications_03"]]

    df_procedures = df_proc[["PcrKey", "eProcedures_03"]]

    # rename columns

    df.rename(columns={"eResponse_07": "Response_Type", "eArrest_01": "Arrest", "eArrest_02": "Arrest_Etiology",
                       "eArrest_07": "AED_Prior_to_EMS", "eArrest_11": "Initial_Rhythm", "eArrest_18": "End_of_EMS_Cardiac_Event",
                       "eSituation_13": "Initial_Acuity", "eDisposition_19": "Final_Acuity"}, inplace=True)

    df_medications.rename(columns={"eMedications_03": "Medications"}, inplace=True)

    df_procedures.rename(columns={"eProcedures_03": "Procedures"}, inplace=True)

    df_arrest_resus.rename(columns={"eArrest_03": "Resuscitation"}, inplace=True)

    df_arrest_ROSC.rename(columns={"eArrest_12": "ROSC"}, inplace=True)

    df_symptoms.rename(columns={"eSituation_09": "Symptoms"}, inplace=True)

    # clean missing values

    df_clean = df.map(clean_missing)
    df_medications = df_medications.map(clean_missing).dropna()
    df_procedures = df_procedures.map(clean_missing).dropna()
    df_arrest_resus = df_arrest_resus.map(clean_missing).dropna()
    df_arrest_ROSC = df_arrest_ROSC.map(clean_missing).dropna()
    df_symptoms = df_symptoms.map(clean_missing)

    # apply maps to columns

    df_clean["Response_Type"] = df_clean["Response_Type"].map(RESPONSE_TYPE)
    df_clean["Arrest"] = df_clean["Arrest"].map(ARREST)
    df_clean["Arrest_Etiology"] = df_clean["Arrest_Etiology"].map(ARREST_ETIOLOGY)
    df_clean["AED_Prior_to_EMS"] = df_clean["AED_Prior_to_EMS"].map(ARREST_AED_USE_PRIOR_TO_EMS_ARRIVAL)
    df_clean["Initial_Rhythm"] = df_clean["Initial_Rhythm"].map(ARREST_FIRST_MONITORED_RHYTHM)
    df_clean["End_of_EMS_Cardiac_Event"] = df_clean["End_of_EMS_Cardiac_Event"].map(ARREST_END_OF_EMS_CARDIAC_EVENT)
    df_clean["Initial_Acuity"] = df_clean["Initial_Acuity"].map(INITIAL_PATIENT_ACUITY)
    df_clean["Final_Acuity"] = df_clean["Final_Acuity"].map(FINAL_PATIENT_ACUITY)

    df_medications["Medications"] = df_medications["Medications"].map(MEDICATIONS)

    df_procedures["Procedures"] = df_procedures["Procedures"].map(PROCEDURES)

    df_arrest_resus["Resuscitation"] = df_arrest_resus["Resuscitation"].map(ARREST_RESUSCITATION)

    df_arrest_ROSC["ROSC"] = df_arrest_ROSC["ROSC"].map(ARREST_ROSC)

    df_symptoms["ICD_Group"] = df_symptoms["Symptoms"].str[0]
    df_symptoms["Symptoms"] = df_symptoms["ICD_Group"].map(ICD_CHAPTER_MAP).fillna("Other")
    df_symptoms = df_symptoms.drop(columns=["ICD_Group"])

    # group by PcrKey for non-unique PcrKey

    df_medications_lists = df_medications.groupby("PcrKey")["Medications"].apply(list).reset_index(name="Medications")
    df_procedures_lists = df_procedures.groupby("PcrKey")["Procedures"].apply(list).reset_index(name="Procedures")
    df_arrest_resus_lists = df_arrest_resus.groupby("PcrKey")["Resuscitation"].apply(list).reset_index(name="Resuscitation")
    df_arrest_ROSC_lists = df_arrest_ROSC.groupby("PcrKey")["ROSC"].apply(list).reset_index(name="ROSC")

    # create medications features
    df_medications_lists["meds_unique"] = df_medications_lists["Medications"].apply(get_unique)
    df_medications_lists["meds_count"] = df_medications_lists["Medications"].apply(get_count)

    df_medications_lists["epi_count"] = df_medications_lists["meds_count"].apply(get_epi_count)
    df_medications_lists["epi_count"] = df_medications_lists["epi_count"].fillna(0).astype(int)

    df_medications_lists["epi_given"] = df_medications_lists["Medications"].apply(
        lambda x: 1 if isinstance(x, list) and "Epinephrine" in x else 0
    ).astype(int)

    df_medications_lists["total_medications"] = df_medications_lists["Medications"].apply(total_count)
    df_medications_lists["unique_medications"] = df_medications_lists["meds_unique"].apply(total_count)

    # create procedures features
    df_procedures_lists["procedures_unique"] = df_procedures_lists["Procedures"].apply(get_unique)
    df_procedures_lists["procedures_count"] = df_procedures_lists["Procedures"].apply(get_count)
    df_procedures_lists["defibrillation_status"] = df_procedures_lists["Procedures"].apply(
        lambda x: 1 if isinstance(x, list) and "Defibrillation" in x else 0
    ).astype(int)
    df_procedures_lists["CPR_status"] = df_procedures_lists["Procedures"].apply(
        lambda x: 1 if isinstance(x, list) and "CPR" in x else 0
    ).astype(int)

    df_procedures_lists["total_procedures"] = df_procedures_lists["Procedures"].apply(total_count)
    df_procedures_lists["unique_procedures"] = df_procedures_lists["procedures_unique"].apply(total_count)

    # get unique lists for arrest and ROSC
    df_arrest_resus_lists["Resuscitation"] = df_arrest_resus_lists["Resuscitation"].map(get_unique)
    df_arrest_ROSC_lists["ROSC"] = df_arrest_ROSC_lists["ROSC"].map(get_unique)

    # get ROSC status
    df_arrest_ROSC_lists["ROSC"] = df_arrest_ROSC_lists["ROSC"].apply(ROSC_status)

    # join tables on keys

    dfs = [df_clean, df_medications_lists, df_procedures_lists, df_arrest_resus_lists,
           df_arrest_ROSC_lists, df_symptoms]

    df_final = reduce(lambda left, right: pd.merge(left, right, on="PcrKey", how="left"), dfs)

    # create intensity score

    df_final["intervention_intensity"] = df_final["total_medications"] + df_final["total_procedures"]

    # drop redundant columns

    df_final.drop(columns=["Medications", "Procedures", "meds_count", "procedures_count",
                           "meds_unique", "procedures_unique", "Resuscitation"], inplace=True)

    # clean up the rest of the NaN values

    binary_cols = [
        "ROSC",
        "CPR_status",
        "epi_given",
        "intervention_intensity",
        "epi_count",
        "defibrillation_status",
        "total_procedures",
        "unique_procedures",
        "total_medications",
        "unique_medications"
    ]

    for col in binary_cols:
        df_final[col] = pd.to_numeric(df_final[col], errors='coerce').fillna(0).astype(int)

    df_final.to_csv("outputs/cleaned_data.csv", index=False)

    return df_final

if __name__ == "__main__":
    build_final_dataset()