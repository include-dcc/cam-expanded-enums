# Auto generated from cam_expanded_enums.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-08T13:54:59
# Schema: cam-expanded-enums
#
# id: https://includedcc.org/cam-expanded-enums
# description: LinkML Schema for the Common Access Model Expanded Enums
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.11.0"
version = None

# Namespaces
DUO = CurieNamespace('DUO', 'http://purl.obolibrary.org/obo/DUO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
CAM = CurieNamespace('cam', 'https://includedcc.org/common-access-model/')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238/')
EDAM = CurieNamespace('edam', 'http://edamontology.org/')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/')
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace('ig2_biospecimen_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/')
IG2DAC = CurieNamespace('ig2dac', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
IG2DAT = CurieNamespace('ig2dat', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/')
IG_DOB_METHOD = CurieNamespace('ig_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/')
IGCONDTYPE = CurieNamespace('igcondtype', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MESH = CurieNamespace('mesh', 'http://id.nlm.nih.gov/mesh/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SNOMEDCT = CurieNamespace('snomedct', 'http://snomed.info/id/')
DEFAULT_ = CAM


# Types

# Class references



@dataclass(repr=False)
class RequiredClass(YAMLRoot):
    """
    This is a placeholder class to satisfy the LinkML requirement of at least one class and is not otherwise used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["RequiredClass"]
    class_class_curie: ClassVar[str] = "cam:RequiredClass"
    class_name: ClassVar[str] = "RequiredClass"
    class_model_uri: ClassVar[URIRef] = CAM.RequiredClass

    id: Optional[str] = None
    full_name: Optional[str] = None
    aliases: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.aliases is not None and not isinstance(self.aliases, str):
            self.aliases = str(self.aliases)

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataUsePermission(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    _defn = EnumDefinition(
        name="EnumDataUsePermission",
        description="Data Use Ontology (DUO) terms for data use permissions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DUO:0000004",
            PermissibleValue(
                text="DUO:0000004",
                title="no restriction",
                description="This data use permission indicates there is no restriction on use.",
                meaning=DUO["0000004"]))
        setattr(cls, "DUO:0000006",
            PermissibleValue(
                text="DUO:0000006",
                title="health or medical or biomedical research",
                description="""This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.""",
                meaning=DUO["0000006"]))
        setattr(cls, "DUO:0000007",
            PermissibleValue(
                text="DUO:0000007",
                title="disease specific research",
                description="""This data use permission indicates that use is allowed provided it is related to the specified disease.
This term should be coupled with a term describing a disease from an ontology to specify the disease the restriction applies to.

DUO recommends MONDO be used, to provide the basis for automated evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md

Other resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can also be used. When those other resources are being used, this may require an extra mapping step to leverage automated matching algorithms.""",
                meaning=DUO["0000007"]))
        setattr(cls, "DUO:0000011",
            PermissibleValue(
                text="DUO:0000011",
                title="population origins or ancestry research only",
                description="""This data use permission indicates that use of the data is limited to the study of population origins or ancestry.""",
                meaning=DUO["0000011"]))
        setattr(cls, "DUO:0000042",
            PermissibleValue(
                text="DUO:0000042",
                title="general research use",
                description="""This data use permission indicates that use is allowed for general research use for any research purpose.
This includes but is not limited to: health/medical/biomedical purposes, fundamental biology research, the study of population origins or ancestry, statistical methods and algorithms development, and social-sciences research.""",
                meaning=DUO["0000042"]))

class EnumDataUseModifier(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    _defn = EnumDefinition(
        name="EnumDataUseModifier",
        description="Data Use Ontology (DUO) terms for data use modifiers.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DUO:00000044",
            PermissibleValue(
                text="DUO:00000044",
                title="population origins or ancestry research prohibited",
                description="""This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.""",
                meaning=DUO["00000044"]))
        setattr(cls, "DUO:0000012",
            PermissibleValue(
                text="DUO:0000012",
                title="research specific restrictions",
                description="""This data use modifier indicates that use is limited to studies of a certain research type.""",
                meaning=DUO["0000012"]))
        setattr(cls, "DUO:0000015",
            PermissibleValue(
                text="DUO:0000015",
                title="no general methods research",
                description="""This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).""",
                meaning=DUO["0000015"]))
        setattr(cls, "DUO:0000016",
            PermissibleValue(
                text="DUO:0000016",
                title="genetic studies only",
                description="""This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)""",
                meaning=DUO["0000016"]))
        setattr(cls, "DUO:0000018",
            PermissibleValue(
                text="DUO:0000018",
                title="not for profit, non commercial use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.""",
                meaning=DUO["0000018"]))
        setattr(cls, "DUO:0000019",
            PermissibleValue(
                text="DUO:0000019",
                title="publication required",
                description="""This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.""",
                meaning=DUO["0000019"]))
        setattr(cls, "DUO:0000020",
            PermissibleValue(
                text="DUO:0000020",
                title="collaboration required",
                description="""This could be coupled with a string describing the primary study investigator(s).
This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s).""",
                meaning=DUO["0000020"]))
        setattr(cls, "DUO:0000021",
            PermissibleValue(
                text="DUO:0000021",
                title="ethics approval required",
                description="""This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.""",
                meaning=DUO["0000021"]))
        setattr(cls, "DUO:0000022",
            PermissibleValue(
                text="DUO:0000022",
                title="geographical restriction",
                description="""This data use modifier indicates that use is limited to within a specific geographic region.
This should be coupled with an ontology term describing the geographical location the restriction applies to.""",
                meaning=DUO["0000022"]))
        setattr(cls, "DUO:0000024",
            PermissibleValue(
                text="DUO:0000024",
                title="publication moratorium",
                description="""This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.
This should be coupled with a date specified as ISO8601""",
                meaning=DUO["0000024"]))
        setattr(cls, "DUO:0000025",
            PermissibleValue(
                text="DUO:0000025",
                title="time limit on use",
                description="""This data use modifier indicates that use is approved for a specific number of months.
This should be coupled with an integer value indicating the number of months.""",
                meaning=DUO["0000025"]))
        setattr(cls, "DUO:0000026",
            PermissibleValue(
                text="DUO:0000026",
                title="user specific restriction",
                description="This data use modifier indicates that use is limited to use by approved users.",
                meaning=DUO["0000026"]))
        setattr(cls, "DUO:0000027",
            PermissibleValue(
                text="DUO:0000027",
                title="project specific restriction",
                description="""This data use modifier indicates that use is limited to use within an approved project.""",
                meaning=DUO["0000027"]))
        setattr(cls, "DUO:0000028",
            PermissibleValue(
                text="DUO:0000028",
                title="institution specific restriction",
                description="""This data use modifier indicates that use is limited to use within an approved institution.""",
                meaning=DUO["0000028"]))
        setattr(cls, "DUO:0000029",
            PermissibleValue(
                text="DUO:0000029",
                title="return to database or resource",
                description="""This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.""",
                meaning=DUO["0000029"]))
        setattr(cls, "DUO:0000043",
            PermissibleValue(
                text="DUO:0000043",
                title="clinical care use",
                description="""Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making.
This data use modifier indicates that use is allowed for clinical use and care.""",
                meaning=DUO["0000043"]))
        setattr(cls, "DUO:0000045",
            PermissibleValue(
                text="DUO:0000045",
                title="not for profit organisation use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations.""",
                meaning=DUO["0000045"]))
        setattr(cls, "DUO:0000046",
            PermissibleValue(
                text="DUO:0000046",
                title="non-commercial use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit use.
This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes.""",
                meaning=DUO["0000046"]))

class EnumProgram(EnumDefinitionImpl):
    """
    Funding programs relevant to inform operations.
    """
    include = PermissibleValue(
        text="include",
        title="INCLUDE")
    kf = PermissibleValue(
        text="kf",
        title="KF")
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumProgram",
        description="Funding programs relevant to inform operations.",
    )

class EnumResearchDomain(EnumDefinitionImpl):
    """
    Domains of Research used to find studies.
    """
    behavior_and_behavior_mechanisms = PermissibleValue(
        text="behavior_and_behavior_mechanisms",
        title="Behavior and Behavior Mechanisms",
        meaning=MESH["D001520"])
    congenital_heart_defects = PermissibleValue(
        text="congenital_heart_defects",
        title="Congenital Heart Defects",
        meaning=MESH["D006330"])
    immune_system_diseases = PermissibleValue(
        text="immune_system_diseases",
        title="Immune System Diseases",
        meaning=MESH["D007154"])
    hematologic_diseases = PermissibleValue(
        text="hematologic_diseases",
        title="Hematologic Diseases",
        meaning=MESH["D006402"])
    neurodevelopment = PermissibleValue(
        text="neurodevelopment",
        title="Neurodevelopment",
        meaning=MESH["D065886"])
    sleep_wake_disorders = PermissibleValue(
        text="sleep_wake_disorders",
        title="Sleep Wake Disorders",
        meaning=MESH["D012893"])
    all_co_occurring_conditions = PermissibleValue(
        text="all_co_occurring_conditions",
        title="All Co-occurring Conditions",
        meaning=MESH["D013568"])
    physical_fitness = PermissibleValue(
        text="physical_fitness",
        title="Physical Fitness",
        meaning=MESH["D010809"])
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumResearchDomain",
        description="Domains of Research used to find studies.",
    )

class EnumParticipantLifespanStage(EnumDefinitionImpl):
    """
    Stages of life during which participants may be recruited.
    """
    fetal = PermissibleValue(
        text="fetal",
        title="Fetal",
        description="Before birth")
    neonatal = PermissibleValue(
        text="neonatal",
        title="Neonatal",
        description="0-28 days old")
    pediatric = PermissibleValue(
        text="pediatric",
        title="Pediatric",
        description="Birth-17 years old")
    adult = PermissibleValue(
        text="adult",
        title="Adult",
        description="18+ years old")

    _defn = EnumDefinition(
        name="EnumParticipantLifespanStage",
        description="Stages of life during which participants may be recruited.",
    )

class EnumStudyDesign(EnumDefinitionImpl):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    case_control = PermissibleValue(
        text="case_control",
        title="Case-Control")
    case_set = PermissibleValue(
        text="case_set",
        title="Case Set")
    control_set = PermissibleValue(
        text="control_set",
        title="Control Set")
    clinical_trial = PermissibleValue(
        text="clinical_trial",
        title="Clinical Trial")
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        title="Cross-Sectional")
    family_twins_trios = PermissibleValue(
        text="family_twins_trios",
        title="Family/Twins/Trios")
    interventional = PermissibleValue(
        text="interventional",
        title="Interventional")
    longitudinal = PermissibleValue(
        text="longitudinal",
        title="Longitudinal")
    trial_readiness_study = PermissibleValue(
        text="trial_readiness_study",
        title="Trial Readiness Study")
    tumor_vs_matched_normal = PermissibleValue(
        text="tumor_vs_matched_normal",
        title="Tumor vs Matched Normal")

    _defn = EnumDefinition(
        name="EnumStudyDesign",
        description="Approaches for collecting data, investigating interventions, and/or analyzing data.",
    )

class EnumClinicalDataSourceType(EnumDefinitionImpl):
    """
    Approaches to ascertain clinical information about a participant.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained directly from medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown")

    _defn = EnumDefinition(
        name="EnumClinicalDataSourceType",
        description="Approaches to ascertain clinical information about a participant.",
    )

class EnumDataCategory(EnumDefinitionImpl):
    """
    Categories of data which may be collected about participants.
    """
    unharmonized_demographic_clinical_data = PermissibleValue(
        text="unharmonized_demographic_clinical_data",
        title="Unharmonized Demographic/Clinical Data")
    harmonized_demographic_clinical_data = PermissibleValue(
        text="harmonized_demographic_clinical_data",
        title="Harmonized Demographic/Clinical Data")
    genomics = PermissibleValue(
        text="genomics",
        title="Genomics")
    transcriptomics = PermissibleValue(
        text="transcriptomics",
        title="Transcriptomics")
    epigenomics = PermissibleValue(
        text="epigenomics",
        title="Epigenomics")
    proteomics = PermissibleValue(
        text="proteomics",
        title="Proteomics")
    metabolomics = PermissibleValue(
        text="metabolomics",
        title="Metabolomics")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral",
        title="Cognitive/Behavioral")
    immune_profiling = PermissibleValue(
        text="immune_profiling",
        title="Immune Profiling")
    imaging = PermissibleValue(
        text="imaging",
        title="Imaging")
    microbiome = PermissibleValue(
        text="microbiome",
        title="Microbiome")
    fitness = PermissibleValue(
        text="fitness",
        title="Fitness")
    physical_activity = PermissibleValue(
        text="physical_activity",
        title="Physical Activity")
    other = PermissibleValue(
        text="other",
        title="Other")
    sleep_study = PermissibleValue(
        text="sleep_study",
        title="Sleep Study")

    _defn = EnumDefinition(
        name="EnumDataCategory",
        description="Categories of data which may be collected about participants.",
    )

class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of Subject entities
    """
    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.")
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.""")
    cell_line = PermissibleValue(
        text="cell_line",
        description="Cell Line")
    animal_model = PermissibleValue(
        text="animal_model",
        description="Animal model")
    group = PermissibleValue(
        text="group",
        description="A group of individuals or entities.")
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!")

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of Subject entities",
    )

class EnumSex(EnumDefinitionImpl):
    """
    Subject Sex
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        meaning=NCIT["C16576"])
    male = PermissibleValue(
        text="male",
        title="Male",
        meaning=NCIT["C20197"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumSex",
        description="Subject Sex",
    )

class EnumRace(EnumDefinitionImpl):
    """
    Participant Race
    """
    american_indian_or_alaska_native = PermissibleValue(
        text="american_indian_or_alaska_native",
        title="American Indian or Alaska Native",
        meaning=NCIT["C41259"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=NCIT["C41260"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=NCIT["C16352"])
    more_than_one_race = PermissibleValue(
        text="more_than_one_race",
        title="More than one race",
        meaning=NCIT["C67109"])
    native_hawaiian_or_other_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_other_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=NCIT["C41219"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=NCIT["C41261"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])
    east_asian = PermissibleValue(
        text="east_asian",
        title="East Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C161419"])
    latin_american = PermissibleValue(
        text="latin_american",
        title="Latin American",
        description="UK only; do not use for US data",
        meaning=NCIT["C126531"])
    middle_eastern_or_north_african = PermissibleValue(
        text="middle_eastern_or_north_african",
        title="Middle Eastern or North African",
        description="UK only; do not use for US data",
        meaning=NCIT["C43866"])
    south_asian = PermissibleValue(
        text="south_asian",
        title="South Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C41263"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="Participant Race",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        title="Hispanic or Latino",
        meaning=NCIT["C17459"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        title="Not Hispanic or Latino",
        meaning=NCIT["C41222"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="Participant ethnicity, specific to Hispanic or Latino.",
    )

class EnumVitalStatus(EnumDefinitionImpl):
    """
    Descriptions of a Subject's vital status
    """
    dead = PermissibleValue(
        text="dead",
        title="Dead",
        meaning=NCIT["C28554"])
    alive = PermissibleValue(
        text="alive",
        title="Alive",
        meaning=NCIT["C37987"])

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Descriptions of a Subject's vital status",
    )

class EnumNull(EnumDefinitionImpl):
    """
    Base enumeration providing null options.
    """
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumNull",
        description="Base enumeration providing null options.",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """
    control_only = PermissibleValue(
        text="control_only",
        title="Control-only",
        description="Control Only")
    duo = PermissibleValue(
        text="duo",
        title="Duo",
        description="Duo")
    proband_only = PermissibleValue(
        text="proband_only",
        title="Proband-only",
        description="Proband Only")
    trio = PermissibleValue(
        text="trio",
        title="Trio",
        description="Trio (2 parents and affected child)")
    trio_plus = PermissibleValue(
        text="trio_plus",
        title="Trio+",
        description="2 Parents and 2 or more children")

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Enumerations describing research family type",
    )

class EnumConsanguinityAssertion(EnumDefinitionImpl):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = PermissibleValue(
        text="not_suspected",
        title="not-suspected",
        description="Not suspected",
        meaning=SNOMEDCT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        title="suspected",
        description="Suspected",
        meaning=SNOMEDCT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        title="known-present",
        description="Known Present",
        meaning=SNOMEDCT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        description="Unknown",
        meaning=SNOMEDCT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
    )

class EnumAssertionProvenance(EnumDefinitionImpl):
    """
    Possible data sources for assertions.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained from a medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")

    _defn = EnumDefinition(
        name="EnumAssertionProvenance",
        description="Possible data sources for assertions.",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the biospecimen available for use?
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the biospecimen available for use?",
    )

class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.",
    )

class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is
    recommended.
    """
    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.""",
    )

class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """
    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="Any spatial/location qualifiers.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "snomedct:106233006",
            PermissibleValue(
                text="snomedct:106233006",
                title="Topographical modifier (qualifier value)",
                description="Topographical modifier (qualifier value)",
                meaning=SNOMEDCT["106233006"]))
        setattr(cls, "snomedct:103339001",
            PermissibleValue(
                text="snomedct:103339001",
                title="Long axis",
                meaning=SNOMEDCT["103339001"]))
        setattr(cls, "snomedct:103340004",
            PermissibleValue(
                text="snomedct:103340004",
                title="Short axis",
                meaning=SNOMEDCT["103340004"]))
        setattr(cls, "snomedct:103341000",
            PermissibleValue(
                text="snomedct:103341000",
                title="Off axis",
                meaning=SNOMEDCT["103341000"]))
        setattr(cls, "snomedct:103342007",
            PermissibleValue(
                text="snomedct:103342007",
                title="Mid-longitudinal",
                meaning=SNOMEDCT["103342007"]))
        setattr(cls, "snomedct:103343002",
            PermissibleValue(
                text="snomedct:103343002",
                title="Parasagittal",
                meaning=SNOMEDCT["103343002"]))
        setattr(cls, "snomedct:103344008",
            PermissibleValue(
                text="snomedct:103344008",
                title="Transvesical",
                meaning=SNOMEDCT["103344008"]))
        setattr(cls, "snomedct:103345009",
            PermissibleValue(
                text="snomedct:103345009",
                title="Transthecal",
                meaning=SNOMEDCT["103345009"]))
        setattr(cls, "snomedct:103346005",
            PermissibleValue(
                text="snomedct:103346005",
                title="Transsplenic",
                meaning=SNOMEDCT["103346005"]))
        setattr(cls, "snomedct:103347001",
            PermissibleValue(
                text="snomedct:103347001",
                title="Transrenal",
                meaning=SNOMEDCT["103347001"]))
        setattr(cls, "snomedct:103348006",
            PermissibleValue(
                text="snomedct:103348006",
                title="Transpleural",
                meaning=SNOMEDCT["103348006"]))
        setattr(cls, "snomedct:103349003",
            PermissibleValue(
                text="snomedct:103349003",
                title="Transpancreatic",
                meaning=SNOMEDCT["103349003"]))
        setattr(cls, "snomedct:103353001",
            PermissibleValue(
                text="snomedct:103353001",
                title="Transgastric",
                meaning=SNOMEDCT["103353001"]))
        setattr(cls, "snomedct:103354007",
            PermissibleValue(
                text="snomedct:103354007",
                title="Transmural",
                meaning=SNOMEDCT["103354007"]))
        setattr(cls, "snomedct:11070000",
            PermissibleValue(
                text="snomedct:11070000",
                title="Capsular",
                meaning=SNOMEDCT["11070000"]))
        setattr(cls, "snomedct:1146002",
            PermissibleValue(
                text="snomedct:1146002",
                title="Arcuate",
                meaning=SNOMEDCT["1146002"]))
        setattr(cls, "snomedct:11896004",
            PermissibleValue(
                text="snomedct:11896004",
                title="Intermediate",
                meaning=SNOMEDCT["11896004"]))
        setattr(cls, "snomedct:1217011006",
            PermissibleValue(
                text="snomedct:1217011006",
                title="Non-adjacent",
                meaning=SNOMEDCT["1217011006"]))
        setattr(cls, "snomedct:131183008",
            PermissibleValue(
                text="snomedct:131183008",
                title="Intra-articular",
                meaning=SNOMEDCT["131183008"]))
        setattr(cls, "snomedct:131184002",
            PermissibleValue(
                text="snomedct:131184002",
                title="Area of defined region",
                meaning=SNOMEDCT["131184002"]))
        setattr(cls, "snomedct:131185001",
            PermissibleValue(
                text="snomedct:131185001",
                title="Vertical long axis",
                meaning=SNOMEDCT["131185001"]))
        setattr(cls, "snomedct:131186000",
            PermissibleValue(
                text="snomedct:131186000",
                title="Horizontal long axis",
                meaning=SNOMEDCT["131186000"]))
        setattr(cls, "snomedct:131187009",
            PermissibleValue(
                text="snomedct:131187009",
                title="Major Axis",
                meaning=SNOMEDCT["131187009"]))
        setattr(cls, "snomedct:131188004",
            PermissibleValue(
                text="snomedct:131188004",
                title="Minor Axis",
                meaning=SNOMEDCT["131188004"]))
        setattr(cls, "snomedct:131189007",
            PermissibleValue(
                text="snomedct:131189007",
                title="Perpendicular axis",
                meaning=SNOMEDCT["131189007"]))
        setattr(cls, "snomedct:131190003",
            PermissibleValue(
                text="snomedct:131190003",
                title="Radius",
                meaning=SNOMEDCT["131190003"]))
        setattr(cls, "snomedct:131191004",
            PermissibleValue(
                text="snomedct:131191004",
                title="Perimeter",
                meaning=SNOMEDCT["131191004"]))
        setattr(cls, "snomedct:14414005",
            PermissibleValue(
                text="snomedct:14414005",
                title="Peripheral",
                meaning=SNOMEDCT["14414005"]))
        setattr(cls, "snomedct:1483009",
            PermissibleValue(
                text="snomedct:1483009",
                title="Angular",
                meaning=SNOMEDCT["1483009"]))
        setattr(cls, "snomedct:18769003",
            PermissibleValue(
                text="snomedct:18769003",
                title="Juxta-posed",
                meaning=SNOMEDCT["18769003"]))
        setattr(cls, "snomedct:21006006",
            PermissibleValue(
                text="snomedct:21006006",
                title="Hemispheric",
                meaning=SNOMEDCT["21006006"]))
        setattr(cls, "snomedct:21481007",
            PermissibleValue(
                text="snomedct:21481007",
                title="Over",
                meaning=SNOMEDCT["21481007"]))
        setattr(cls, "snomedct:24020000",
            PermissibleValue(
                text="snomedct:24020000",
                title="Horizontal",
                meaning=SNOMEDCT["24020000"]))
        setattr(cls, "snomedct:24028007",
            PermissibleValue(
                text="snomedct:24028007",
                title="Right (qualifier value)",
                description="Right (qualifier value)",
                meaning=SNOMEDCT["24028007"]))
        setattr(cls, "snomedct:24422004",
            PermissibleValue(
                text="snomedct:24422004",
                title="Axial",
                meaning=SNOMEDCT["24422004"]))
        setattr(cls, "snomedct:255527003",
            PermissibleValue(
                text="snomedct:255527003",
                title="Horizontal - 3 and 9",
                meaning=SNOMEDCT["255527003"]))
        setattr(cls, "snomedct:255528008",
            PermissibleValue(
                text="snomedct:255528008",
                title="Horizontal and vertical",
                meaning=SNOMEDCT["255528008"]))
        setattr(cls, "snomedct:261129000",
            PermissibleValue(
                text="snomedct:261129000",
                title="Mediolateral",
                meaning=SNOMEDCT["261129000"]))
        setattr(cls, "snomedct:26216008",
            PermissibleValue(
                text="snomedct:26216008",
                title="Central",
                meaning=SNOMEDCT["26216008"]))
        setattr(cls, "snomedct:26283006",
            PermissibleValue(
                text="snomedct:26283006",
                title="Superficial",
                meaning=SNOMEDCT["26283006"]))
        setattr(cls, "snomedct:263687007",
            PermissibleValue(
                text="snomedct:263687007",
                title="Bony extra-articular",
                meaning=SNOMEDCT["263687007"]))
        setattr(cls, "snomedct:263688002",
            PermissibleValue(
                text="snomedct:263688002",
                title="Bony intra-articular",
                meaning=SNOMEDCT["263688002"]))
        setattr(cls, "snomedct:264731004",
            PermissibleValue(
                text="snomedct:264731004",
                title="Lateral to the left",
                meaning=SNOMEDCT["264731004"]))
        setattr(cls, "snomedct:264732006",
            PermissibleValue(
                text="snomedct:264732006",
                title="Lateral to the right",
                meaning=SNOMEDCT["264732006"]))
        setattr(cls, "snomedct:264733001",
            PermissibleValue(
                text="snomedct:264733001",
                title="Linear longitudinal",
                meaning=SNOMEDCT["264733001"]))
        setattr(cls, "snomedct:264737000",
            PermissibleValue(
                text="snomedct:264737000",
                title="Linear transverse",
                meaning=SNOMEDCT["264737000"]))
        setattr(cls, "snomedct:264741001",
            PermissibleValue(
                text="snomedct:264741001",
                title="Posterolateral to the left",
                meaning=SNOMEDCT["264741001"]))
        setattr(cls, "snomedct:264742008",
            PermissibleValue(
                text="snomedct:264742008",
                title="Posterolateral to the right",
                meaning=SNOMEDCT["264742008"]))
        setattr(cls, "snomedct:264839005",
            PermissibleValue(
                text="snomedct:264839005",
                title="Horizontal cleavage",
                meaning=SNOMEDCT["264839005"]))
        setattr(cls, "snomedct:27237009",
            PermissibleValue(
                text="snomedct:27237009",
                title="Triangular",
                meaning=SNOMEDCT["27237009"]))
        setattr(cls, "snomedct:28241006",
            PermissibleValue(
                text="snomedct:28241006",
                title="Rhomboid",
                meaning=SNOMEDCT["28241006"]))
        setattr(cls, "snomedct:28947002",
            PermissibleValue(
                text="snomedct:28947002",
                title="Right curve",
                meaning=SNOMEDCT["28947002"]))
        setattr(cls, "snomedct:30730003",
            PermissibleValue(
                text="snomedct:30730003",
                title="Sagittal",
                meaning=SNOMEDCT["30730003"]))
        setattr(cls, "snomedct:30899007",
            PermissibleValue(
                text="snomedct:30899007",
                title="Quadrangular",
                meaning=SNOMEDCT["30899007"]))
        setattr(cls, "snomedct:32381004",
            PermissibleValue(
                text="snomedct:32381004",
                title="Portal",
                meaning=SNOMEDCT["32381004"]))
        setattr(cls, "snomedct:32400000",
            PermissibleValue(
                text="snomedct:32400000",
                title="Preaxial",
                meaning=SNOMEDCT["32400000"]))
        setattr(cls, "snomedct:33096000",
            PermissibleValue(
                text="snomedct:33096000",
                title="Vertical",
                meaning=SNOMEDCT["33096000"]))
        setattr(cls, "snomedct:33843005",
            PermissibleValue(
                text="snomedct:33843005",
                title="Efferent",
                meaning=SNOMEDCT["33843005"]))
        setattr(cls, "snomedct:350722008",
            PermissibleValue(
                text="snomedct:350722008",
                title="Behind",
                meaning=SNOMEDCT["350722008"]))
        setattr(cls, "snomedct:351726001",
            PermissibleValue(
                text="snomedct:351726001",
                title="Below",
                meaning=SNOMEDCT["351726001"]))
        setattr(cls, "snomedct:352730000",
            PermissibleValue(
                text="snomedct:352730000",
                title="Supra-",
                meaning=SNOMEDCT["352730000"]))
        setattr(cls, "snomedct:353734004",
            PermissibleValue(
                text="snomedct:353734004",
                title="Upward",
                meaning=SNOMEDCT["353734004"]))
        setattr(cls, "snomedct:354652004",
            PermissibleValue(
                text="snomedct:354652004",
                title="Circular",
                meaning=SNOMEDCT["354652004"]))
        setattr(cls, "snomedct:355648006",
            PermissibleValue(
                text="snomedct:355648006",
                title="Surrounding",
                meaning=SNOMEDCT["355648006"]))
        setattr(cls, "snomedct:37197008",
            PermissibleValue(
                text="snomedct:37197008",
                title="Anterolateral",
                meaning=SNOMEDCT["37197008"]))
        setattr(cls, "snomedct:38717003",
            PermissibleValue(
                text="snomedct:38717003",
                title="Longitudinal",
                meaning=SNOMEDCT["38717003"]))
        setattr(cls, "snomedct:39187007",
            PermissibleValue(
                text="snomedct:39187007",
                title="Bent",
                meaning=SNOMEDCT["39187007"]))
        setattr(cls, "snomedct:40415009",
            PermissibleValue(
                text="snomedct:40415009",
                title="Proximal",
                meaning=SNOMEDCT["40415009"]))
        setattr(cls, "snomedct:410674003",
            PermissibleValue(
                text="snomedct:410674003",
                title="Regional",
                meaning=SNOMEDCT["410674003"]))
        setattr(cls, "snomedct:410679008",
            PermissibleValue(
                text="snomedct:410679008",
                title="Surface",
                meaning=SNOMEDCT["410679008"]))
        setattr(cls, "snomedct:42798000",
            PermissibleValue(
                text="snomedct:42798000",
                title="Area",
                meaning=SNOMEDCT["42798000"]))
        setattr(cls, "snomedct:43674008",
            PermissibleValue(
                text="snomedct:43674008",
                title="Apical",
                meaning=SNOMEDCT["43674008"]))
        setattr(cls, "snomedct:45226003",
            PermissibleValue(
                text="snomedct:45226003",
                title="Cylindrical",
                meaning=SNOMEDCT["45226003"]))
        setattr(cls, "snomedct:46053002",
            PermissibleValue(
                text="snomedct:46053002",
                title="Distal",
                meaning=SNOMEDCT["46053002"]))
        setattr(cls, "snomedct:47021000",
            PermissibleValue(
                text="snomedct:47021000",
                title="Left curve",
                meaning=SNOMEDCT["47021000"]))
        setattr(cls, "snomedct:49370004",
            PermissibleValue(
                text="snomedct:49370004",
                title="Lateral",
                meaning=SNOMEDCT["49370004"]))
        setattr(cls, "snomedct:49530007",
            PermissibleValue(
                text="snomedct:49530007",
                title="Afferent",
                meaning=SNOMEDCT["49530007"]))
        setattr(cls, "snomedct:50009006",
            PermissibleValue(
                text="snomedct:50009006",
                title="Linear",
                meaning=SNOMEDCT["50009006"]))
        setattr(cls, "snomedct:50362007",
            PermissibleValue(
                text="snomedct:50362007",
                title="Stellate",
                meaning=SNOMEDCT["50362007"]))
        setattr(cls, "snomedct:50974003",
            PermissibleValue(
                text="snomedct:50974003",
                title="Junctional",
                meaning=SNOMEDCT["50974003"]))
        setattr(cls, "snomedct:51440002",
            PermissibleValue(
                text="snomedct:51440002",
                title="Right and left",
                meaning=SNOMEDCT["51440002"]))
        setattr(cls, "snomedct:5686001",
            PermissibleValue(
                text="snomedct:5686001",
                title="Remote",
                meaning=SNOMEDCT["5686001"]))
        setattr(cls, "snomedct:56924007",
            PermissibleValue(
                text="snomedct:56924007",
                title="Square",
                meaning=SNOMEDCT["56924007"]))
        setattr(cls, "snomedct:57183005",
            PermissibleValue(
                text="snomedct:57183005",
                title="Along edge",
                meaning=SNOMEDCT["57183005"]))
        setattr(cls, "snomedct:57195005",
            PermissibleValue(
                text="snomedct:57195005",
                title="Basal",
                meaning=SNOMEDCT["57195005"]))
        setattr(cls, "snomedct:59410002",
            PermissibleValue(
                text="snomedct:59410002",
                title="Rectangular",
                meaning=SNOMEDCT["59410002"]))
        setattr(cls, "snomedct:60301000",
            PermissibleValue(
                text="snomedct:60301000",
                title="Curved",
                meaning=SNOMEDCT["60301000"]))
        setattr(cls, "snomedct:60583000",
            PermissibleValue(
                text="snomedct:60583000",
                title="Postaxial",
                meaning=SNOMEDCT["60583000"]))
        setattr(cls, "snomedct:61397002",
            PermissibleValue(
                text="snomedct:61397002",
                title="Subcapsular",
                meaning=SNOMEDCT["61397002"]))
        setattr(cls, "snomedct:62083003",
            PermissibleValue(
                text="snomedct:62083003",
                title="Sectional",
                meaning=SNOMEDCT["62083003"]))
        setattr(cls, "snomedct:62372003",
            PermissibleValue(
                text="snomedct:62372003",
                title="Segmental",
                meaning=SNOMEDCT["62372003"]))
        setattr(cls, "snomedct:62824007",
            PermissibleValue(
                text="snomedct:62824007",
                title="Transverse",
                meaning=SNOMEDCT["62824007"]))
        setattr(cls, "snomedct:66787007",
            PermissibleValue(
                text="snomedct:66787007",
                title="Cephalic",
                meaning=SNOMEDCT["66787007"]))
        setattr(cls, "snomedct:68493006",
            PermissibleValue(
                text="snomedct:68493006",
                title="Gutter",
                meaning=SNOMEDCT["68493006"]))
        setattr(cls, "snomedct:69320009",
            PermissibleValue(
                text="snomedct:69320009",
                title="Extracellular",
                meaning=SNOMEDCT["69320009"]))
        setattr(cls, "snomedct:69389007",
            PermissibleValue(
                text="snomedct:69389007",
                title="Saccular",
                meaning=SNOMEDCT["69389007"]))
        setattr(cls, "snomedct:710097009",
            PermissibleValue(
                text="snomedct:710097009",
                title="Incisal",
                meaning=SNOMEDCT["710097009"]))
        setattr(cls, "snomedct:710098004",
            PermissibleValue(
                text="snomedct:710098004",
                title="Occlusal",
                meaning=SNOMEDCT["710098004"]))
        setattr(cls, "snomedct:710099007",
            PermissibleValue(
                text="snomedct:710099007",
                title="Mesial",
                meaning=SNOMEDCT["710099007"]))
        setattr(cls, "snomedct:7771000",
            PermissibleValue(
                text="snomedct:7771000",
                title="Left (qualifier value)",
                description="Left (qualifier value)",
                meaning=SNOMEDCT["7771000"]))
        setattr(cls, "snomedct:795002",
            PermissibleValue(
                text="snomedct:795002",
                title="Deep",
                meaning=SNOMEDCT["795002"]))
        setattr(cls, "snomedct:81654009",
            PermissibleValue(
                text="snomedct:81654009",
                title="Coronal",
                meaning=SNOMEDCT["81654009"]))
        setattr(cls, "snomedct:83167003",
            PermissibleValue(
                text="snomedct:83167003",
                title="Intracellular",
                meaning=SNOMEDCT["83167003"]))
        setattr(cls, "snomedct:84177009",
            PermissibleValue(
                text="snomedct:84177009",
                title="Straddling",
                meaning=SNOMEDCT["84177009"]))
        setattr(cls, "snomedct:87687004",
            PermissibleValue(
                text="snomedct:87687004",
                title="Extra-articular",
                meaning=SNOMEDCT["87687004"]))
        setattr(cls, "snomedct:90069004",
            PermissibleValue(
                text="snomedct:90069004",
                title="Posterolateral",
                meaning=SNOMEDCT["90069004"]))
        setattr(cls, "snomedct:272424004",
            PermissibleValue(
                text="snomedct:272424004",
                title="Relative sites (qualifier value)",
                description="Relative sites (qualifier value)",
                meaning=SNOMEDCT["272424004"]))
        setattr(cls, "snomedct:112233002",
            PermissibleValue(
                text="snomedct:112233002",
                title="Marginal",
                meaning=SNOMEDCT["112233002"]))
        setattr(cls, "snomedct:1197041002",
            PermissibleValue(
                text="snomedct:1197041002",
                title="Intercostal",
                meaning=SNOMEDCT["1197041002"]))
        setattr(cls, "snomedct:1285325005",
            PermissibleValue(
                text="snomedct:1285325005",
                title="Intralobular",
                meaning=SNOMEDCT["1285325005"]))
        setattr(cls, "snomedct:128590009",
            PermissibleValue(
                text="snomedct:128590009",
                title="Anatomical reference point of right atrium",
                meaning=SNOMEDCT["128590009"]))
        setattr(cls, "snomedct:1362012009",
            PermissibleValue(
                text="snomedct:1362012009",
                title="Inlet projection",
                meaning=SNOMEDCT["1362012009"]))
        setattr(cls, "snomedct:1363295008",
            PermissibleValue(
                text="snomedct:1363295008",
                title="Unilobar",
                meaning=SNOMEDCT["1363295008"]))
        setattr(cls, "snomedct:1363296009",
            PermissibleValue(
                text="snomedct:1363296009",
                title="Ipsilateral multilobar",
                meaning=SNOMEDCT["1363296009"]))
        setattr(cls, "snomedct:182353008",
            PermissibleValue(
                text="snomedct:182353008",
                title="Side",
                meaning=SNOMEDCT["182353008"]))
        setattr(cls, "snomedct:225780003",
            PermissibleValue(
                text="snomedct:225780003",
                title="Sublingual",
                meaning=SNOMEDCT["225780003"]))
        setattr(cls, "snomedct:229801003",
            PermissibleValue(
                text="snomedct:229801003",
                title="Intra-arterial",
                meaning=SNOMEDCT["229801003"]))
        setattr(cls, "snomedct:255208005",
            PermissibleValue(
                text="snomedct:255208005",
                title="Ipsilateral",
                meaning=SNOMEDCT["255208005"]))
        setattr(cls, "snomedct:255209002",
            PermissibleValue(
                text="snomedct:255209002",
                title="Contralateral",
                meaning=SNOMEDCT["255209002"]))
        setattr(cls, "snomedct:255348000",
            PermissibleValue(
                text="snomedct:255348000",
                title="Inframammary",
                meaning=SNOMEDCT["255348000"]))
        setattr(cls, "snomedct:255472009",
            PermissibleValue(
                text="snomedct:255472009",
                title="Panretinal",
                meaning=SNOMEDCT["255472009"]))
        setattr(cls, "snomedct:255482005",
            PermissibleValue(
                text="snomedct:255482005",
                title="Left upper segment",
                meaning=SNOMEDCT["255482005"]))
        setattr(cls, "snomedct:255486008",
            PermissibleValue(
                text="snomedct:255486008",
                title="Lower segment",
                meaning=SNOMEDCT["255486008"]))
        setattr(cls, "snomedct:255496004",
            PermissibleValue(
                text="snomedct:255496004",
                title="Right lower segment",
                meaning=SNOMEDCT["255496004"]))
        setattr(cls, "snomedct:255499006",
            PermissibleValue(
                text="snomedct:255499006",
                title="Right upper segment",
                meaning=SNOMEDCT["255499006"]))
        setattr(cls, "snomedct:255501003",
            PermissibleValue(
                text="snomedct:255501003",
                title="Upper segment",
                meaning=SNOMEDCT["255501003"]))
        setattr(cls, "snomedct:255546002",
            PermissibleValue(
                text="snomedct:255546002",
                title="Underlay",
                meaning=SNOMEDCT["255546002"]))
        setattr(cls, "snomedct:255547006",
            PermissibleValue(
                text="snomedct:255547006",
                title="Overlay",
                meaning=SNOMEDCT["255547006"]))
        setattr(cls, "snomedct:255548001",
            PermissibleValue(
                text="snomedct:255548001",
                title="Sandwich graft",
                meaning=SNOMEDCT["255548001"]))
        setattr(cls, "snomedct:255549009",
            PermissibleValue(
                text="snomedct:255549009",
                title="Anterior",
                meaning=SNOMEDCT["255549009"]))
        setattr(cls, "snomedct:255550009",
            PermissibleValue(
                text="snomedct:255550009",
                title="Anterior to epiglottis",
                meaning=SNOMEDCT["255550009"]))
        setattr(cls, "snomedct:255551008",
            PermissibleValue(
                text="snomedct:255551008",
                title="Posterior",
                meaning=SNOMEDCT["255551008"]))
        setattr(cls, "snomedct:255552001",
            PermissibleValue(
                text="snomedct:255552001",
                title="Posterior to epiglottis",
                meaning=SNOMEDCT["255552001"]))
        setattr(cls, "snomedct:255554000",
            PermissibleValue(
                text="snomedct:255554000",
                title="Dorsal",
                meaning=SNOMEDCT["255554000"]))
        setattr(cls, "snomedct:255557007",
            PermissibleValue(
                text="snomedct:255557007",
                title="Intracerebral",
                meaning=SNOMEDCT["255557007"]))
        setattr(cls, "snomedct:255558002",
            PermissibleValue(
                text="snomedct:255558002",
                title="Intragastric",
                meaning=SNOMEDCT["255558002"]))
        setattr(cls, "snomedct:255559005",
            PermissibleValue(
                text="snomedct:255559005",
                title="Intramuscular",
                meaning=SNOMEDCT["255559005"]))
        setattr(cls, "snomedct:255560000",
            PermissibleValue(
                text="snomedct:255560000",
                title="Intravenous",
                meaning=SNOMEDCT["255560000"]))
        setattr(cls, "snomedct:255561001",
            PermissibleValue(
                text="snomedct:255561001",
                title="Medial",
                meaning=SNOMEDCT["255561001"]))
        setattr(cls, "snomedct:255562008",
            PermissibleValue(
                text="snomedct:255562008",
                title="Mid",
                meaning=SNOMEDCT["255562008"]))
        setattr(cls, "snomedct:255563003",
            PermissibleValue(
                text="snomedct:255563003",
                title="Mid-zone",
                meaning=SNOMEDCT["255563003"]))
        setattr(cls, "snomedct:255564009",
            PermissibleValue(
                text="snomedct:255564009",
                title="Perivascular",
                meaning=SNOMEDCT["255564009"]))
        setattr(cls, "snomedct:255565005",
            PermissibleValue(
                text="snomedct:255565005",
                title="Peripapillary",
                meaning=SNOMEDCT["255565005"]))
        setattr(cls, "snomedct:255567002",
            PermissibleValue(
                text="snomedct:255567002",
                title="Postauricular",
                meaning=SNOMEDCT["255567002"]))
        setattr(cls, "snomedct:255568007",
            PermissibleValue(
                text="snomedct:255568007",
                title="Retrosternal",
                meaning=SNOMEDCT["255568007"]))
        setattr(cls, "snomedct:255569004",
            PermissibleValue(
                text="snomedct:255569004",
                title="Suprasternal",
                meaning=SNOMEDCT["255569004"]))
        setattr(cls, "snomedct:255579002",
            PermissibleValue(
                text="snomedct:255579002",
                title="Palatal-lingual",
                meaning=SNOMEDCT["255579002"]))
        setattr(cls, "snomedct:255584008",
            PermissibleValue(
                text="snomedct:255584008",
                title="Septal",
                meaning=SNOMEDCT["255584008"]))
        setattr(cls, "snomedct:255690001",
            PermissibleValue(
                text="snomedct:255690001",
                title="Drug in contact with skin",
                meaning=SNOMEDCT["255690001"]))
        setattr(cls, "snomedct:258186003",
            PermissibleValue(
                text="snomedct:258186003",
                title="Via collaterals",
                meaning=SNOMEDCT["258186003"]))
        setattr(cls, "snomedct:258187007",
            PermissibleValue(
                text="snomedct:258187007",
                title="Via native vessel - graft impaired",
                meaning=SNOMEDCT["258187007"]))
        setattr(cls, "snomedct:258188002",
            PermissibleValue(
                text="snomedct:258188002",
                title="Via native vessel - graft occluded",
                meaning=SNOMEDCT["258188002"]))
        setattr(cls, "snomedct:258189005",
            PermissibleValue(
                text="snomedct:258189005",
                title="Via skip graft",
                meaning=SNOMEDCT["258189005"]))
        setattr(cls, "snomedct:258329003",
            PermissibleValue(
                text="snomedct:258329003",
                title="Supratentorial",
                meaning=SNOMEDCT["258329003"]))
        setattr(cls, "snomedct:258330008",
            PermissibleValue(
                text="snomedct:258330008",
                title="Infratentorial",
                meaning=SNOMEDCT["258330008"]))
        setattr(cls, "snomedct:260240005",
            PermissibleValue(
                text="snomedct:260240005",
                title="Interdental",
                meaning=SNOMEDCT["260240005"]))
        setattr(cls, "snomedct:260318004",
            PermissibleValue(
                text="snomedct:260318004",
                title="1 o'clock position",
                meaning=SNOMEDCT["260318004"]))
        setattr(cls, "snomedct:260319007",
            PermissibleValue(
                text="snomedct:260319007",
                title="1.30 o'clock position",
                meaning=SNOMEDCT["260319007"]))
        setattr(cls, "snomedct:260322009",
            PermissibleValue(
                text="snomedct:260322009",
                title="10 o'clock position",
                meaning=SNOMEDCT["260322009"]))
        setattr(cls, "snomedct:260323004",
            PermissibleValue(
                text="snomedct:260323004",
                title="10.30 o'clock position",
                meaning=SNOMEDCT["260323004"]))
        setattr(cls, "snomedct:260324005",
            PermissibleValue(
                text="snomedct:260324005",
                title="11 o'clock position",
                meaning=SNOMEDCT["260324005"]))
        setattr(cls, "snomedct:260325006",
            PermissibleValue(
                text="snomedct:260325006",
                title="11.30 o'clock position",
                meaning=SNOMEDCT["260325006"]))
        setattr(cls, "snomedct:260326007",
            PermissibleValue(
                text="snomedct:260326007",
                title="12 o'clock position",
                meaning=SNOMEDCT["260326007"]))
        setattr(cls, "snomedct:260327003",
            PermissibleValue(
                text="snomedct:260327003",
                title="12.30 o'clock position",
                meaning=SNOMEDCT["260327003"]))
        setattr(cls, "snomedct:260328008",
            PermissibleValue(
                text="snomedct:260328008",
                title="2 o'clock position",
                meaning=SNOMEDCT["260328008"]))
        setattr(cls, "snomedct:260329000",
            PermissibleValue(
                text="snomedct:260329000",
                title="2.30 o'clock position",
                meaning=SNOMEDCT["260329000"]))
        setattr(cls, "snomedct:260330005",
            PermissibleValue(
                text="snomedct:260330005",
                title="3 o'clock position",
                meaning=SNOMEDCT["260330005"]))
        setattr(cls, "snomedct:260331009",
            PermissibleValue(
                text="snomedct:260331009",
                title="3.30 o'clock position",
                meaning=SNOMEDCT["260331009"]))
        setattr(cls, "snomedct:260333007",
            PermissibleValue(
                text="snomedct:260333007",
                title="4 o'clock position",
                meaning=SNOMEDCT["260333007"]))
        setattr(cls, "snomedct:260334001",
            PermissibleValue(
                text="snomedct:260334001",
                title="4.30 o'clock position",
                meaning=SNOMEDCT["260334001"]))
        setattr(cls, "snomedct:260335000",
            PermissibleValue(
                text="snomedct:260335000",
                title="5 o'clock position",
                meaning=SNOMEDCT["260335000"]))
        setattr(cls, "snomedct:260336004",
            PermissibleValue(
                text="snomedct:260336004",
                title="5.30 o'clock position",
                meaning=SNOMEDCT["260336004"]))
        setattr(cls, "snomedct:260337008",
            PermissibleValue(
                text="snomedct:260337008",
                title="6 o'clock position",
                meaning=SNOMEDCT["260337008"]))
        setattr(cls, "snomedct:260338003",
            PermissibleValue(
                text="snomedct:260338003",
                title="6.30 o'clock position",
                meaning=SNOMEDCT["260338003"]))
        setattr(cls, "snomedct:260339006",
            PermissibleValue(
                text="snomedct:260339006",
                title="7 o'clock position",
                meaning=SNOMEDCT["260339006"]))
        setattr(cls, "snomedct:260340008",
            PermissibleValue(
                text="snomedct:260340008",
                title="7.30 o'clock position",
                meaning=SNOMEDCT["260340008"]))
        setattr(cls, "snomedct:260341007",
            PermissibleValue(
                text="snomedct:260341007",
                title="8 o'clock position",
                meaning=SNOMEDCT["260341007"]))
        setattr(cls, "snomedct:260342000",
            PermissibleValue(
                text="snomedct:260342000",
                title="8.30 o'clock position",
                meaning=SNOMEDCT["260342000"]))
        setattr(cls, "snomedct:260343005",
            PermissibleValue(
                text="snomedct:260343005",
                title="9 o'clock position",
                meaning=SNOMEDCT["260343005"]))
        setattr(cls, "snomedct:260344004",
            PermissibleValue(
                text="snomedct:260344004",
                title="9.30 o'clock position",
                meaning=SNOMEDCT["260344004"]))
        setattr(cls, "snomedct:260419006",
            PermissibleValue(
                text="snomedct:260419006",
                title="Projection",
                meaning=SNOMEDCT["260419006"]))
        setattr(cls, "snomedct:260421001",
            PermissibleValue(
                text="snomedct:260421001",
                title="Left lateral oblique",
                meaning=SNOMEDCT["260421001"]))
        setattr(cls, "snomedct:260422008",
            PermissibleValue(
                text="snomedct:260422008",
                title="C1-C2 left oblique",
                meaning=SNOMEDCT["260422008"]))
        setattr(cls, "snomedct:260424009",
            PermissibleValue(
                text="snomedct:260424009",
                title="Right lateral oblique",
                meaning=SNOMEDCT["260424009"]))
        setattr(cls, "snomedct:260425005",
            PermissibleValue(
                text="snomedct:260425005",
                title="C1-C2 right oblique",
                meaning=SNOMEDCT["260425005"]))
        setattr(cls, "snomedct:260426006",
            PermissibleValue(
                text="snomedct:260426006",
                title="Medial oblique",
                meaning=SNOMEDCT["260426006"]))
        setattr(cls, "snomedct:260427002",
            PermissibleValue(
                text="snomedct:260427002",
                title="Oblique lateral",
                meaning=SNOMEDCT["260427002"]))
        setattr(cls, "snomedct:260428007",
            PermissibleValue(
                text="snomedct:260428007",
                title="Mandible X-ray - lateral oblique",
                meaning=SNOMEDCT["260428007"]))
        setattr(cls, "snomedct:260430009",
            PermissibleValue(
                text="snomedct:260430009",
                title="Anteroposterior left lateral decubitus",
                meaning=SNOMEDCT["260430009"]))
        setattr(cls, "snomedct:260431008",
            PermissibleValue(
                text="snomedct:260431008",
                title="C1-C2 left lateral",
                meaning=SNOMEDCT["260431008"]))
        setattr(cls, "snomedct:260432001",
            PermissibleValue(
                text="snomedct:260432001",
                title="Left true lateral",
                meaning=SNOMEDCT["260432001"]))
        setattr(cls, "snomedct:260434000",
            PermissibleValue(
                text="snomedct:260434000",
                title="Anteroposterior right lateral decubitus",
                meaning=SNOMEDCT["260434000"]))
        setattr(cls, "snomedct:260435004",
            PermissibleValue(
                text="snomedct:260435004",
                title="C1-C2 right lateral",
                meaning=SNOMEDCT["260435004"]))
        setattr(cls, "snomedct:260436003",
            PermissibleValue(
                text="snomedct:260436003",
                title="Right true lateral",
                meaning=SNOMEDCT["260436003"]))
        setattr(cls, "snomedct:260437007",
            PermissibleValue(
                text="snomedct:260437007",
                title="Lateral vertical beam",
                meaning=SNOMEDCT["260437007"]))
        setattr(cls, "snomedct:260438002",
            PermissibleValue(
                text="snomedct:260438002",
                title="Lateral horizontal beam",
                meaning=SNOMEDCT["260438002"]))
        setattr(cls, "snomedct:260439005",
            PermissibleValue(
                text="snomedct:260439005",
                title="Lateral inverted",
                meaning=SNOMEDCT["260439005"]))
        setattr(cls, "snomedct:260440007",
            PermissibleValue(
                text="snomedct:260440007",
                title="True lateral of mandible",
                meaning=SNOMEDCT["260440007"]))
        setattr(cls, "snomedct:260441006",
            PermissibleValue(
                text="snomedct:260441006",
                title="Frog lateral",
                meaning=SNOMEDCT["260441006"]))
        setattr(cls, "snomedct:260442004",
            PermissibleValue(
                text="snomedct:260442004",
                title="Erect lateral",
                meaning=SNOMEDCT["260442004"]))
        setattr(cls, "snomedct:260443009",
            PermissibleValue(
                text="snomedct:260443009",
                title="Anteroposterior inverted",
                meaning=SNOMEDCT["260443009"]))
        setattr(cls, "snomedct:260444003",
            PermissibleValue(
                text="snomedct:260444003",
                title="Rotated posteroanterior",
                meaning=SNOMEDCT["260444003"]))
        setattr(cls, "snomedct:260445002",
            PermissibleValue(
                text="snomedct:260445002",
                title="Posteroanterior 20 degree",
                meaning=SNOMEDCT["260445002"]))
        setattr(cls, "snomedct:260446001",
            PermissibleValue(
                text="snomedct:260446001",
                title="Posteroanterior in ulnar deviation",
                meaning=SNOMEDCT["260446001"]))
        setattr(cls, "snomedct:260447005",
            PermissibleValue(
                text="snomedct:260447005",
                title="Penetrated posteroanterior",
                meaning=SNOMEDCT["260447005"]))
        setattr(cls, "snomedct:260450008",
            PermissibleValue(
                text="snomedct:260450008",
                title="Lordotic projection",
                meaning=SNOMEDCT["260450008"]))
        setattr(cls, "snomedct:260451007",
            PermissibleValue(
                text="snomedct:260451007",
                title="Supine decubitus",
                meaning=SNOMEDCT["260451007"]))
        setattr(cls, "snomedct:260452000",
            PermissibleValue(
                text="snomedct:260452000",
                title="Decubitus",
                meaning=SNOMEDCT["260452000"]))
        setattr(cls, "snomedct:260453005",
            PermissibleValue(
                text="snomedct:260453005",
                title="Internal/external rotation",
                meaning=SNOMEDCT["260453005"]))
        setattr(cls, "snomedct:260454004",
            PermissibleValue(
                text="snomedct:260454004",
                title="45 degree projection",
                meaning=SNOMEDCT["260454004"]))
        setattr(cls, "snomedct:260455003",
            PermissibleValue(
                text="snomedct:260455003",
                title="Head and neck projection",
                meaning=SNOMEDCT["260455003"]))
        setattr(cls, "snomedct:260458001",
            PermissibleValue(
                text="snomedct:260458001",
                title="Slit Towne's",
                meaning=SNOMEDCT["260458001"]))
        setattr(cls, "snomedct:260459009",
            PermissibleValue(
                text="snomedct:260459009",
                title="Reverse Towne's",
                meaning=SNOMEDCT["260459009"]))
        setattr(cls, "snomedct:260460004",
            PermissibleValue(
                text="snomedct:260460004",
                title="Slit 35 degree fronto-occipital",
                meaning=SNOMEDCT["260460004"]))
        setattr(cls, "snomedct:260461000",
            PermissibleValue(
                text="snomedct:260461000",
                title="Vertex projection",
                meaning=SNOMEDCT["260461000"]))
        setattr(cls, "snomedct:260463002",
            PermissibleValue(
                text="snomedct:260463002",
                title="Left Stenver's",
                meaning=SNOMEDCT["260463002"]))
        setattr(cls, "snomedct:260464008",
            PermissibleValue(
                text="snomedct:260464008",
                title="Right Stenver's",
                meaning=SNOMEDCT["260464008"]))
        setattr(cls, "snomedct:260465009",
            PermissibleValue(
                text="snomedct:260465009",
                title="Occipitofrontal projection",
                meaning=SNOMEDCT["260465009"]))
        setattr(cls, "snomedct:260466005",
            PermissibleValue(
                text="snomedct:260466005",
                title="Occipitomental projection",
                meaning=SNOMEDCT["260466005"]))
        setattr(cls, "snomedct:260467001",
            PermissibleValue(
                text="snomedct:260467001",
                title="Occipitomental - erect",
                meaning=SNOMEDCT["260467001"]))
        setattr(cls, "snomedct:260468006",
            PermissibleValue(
                text="snomedct:260468006",
                title="Occipitomental - tilted",
                meaning=SNOMEDCT["260468006"]))
        setattr(cls, "snomedct:260469003",
            PermissibleValue(
                text="snomedct:260469003",
                title="Occipitomental - prone",
                meaning=SNOMEDCT["260469003"]))
        setattr(cls, "snomedct:260470002",
            PermissibleValue(
                text="snomedct:260470002",
                title="Occipitomental - 15 degree",
                meaning=SNOMEDCT["260470002"]))
        setattr(cls, "snomedct:260471003",
            PermissibleValue(
                text="snomedct:260471003",
                title="Occipitomental - 30 degree",
                meaning=SNOMEDCT["260471003"]))
        setattr(cls, "snomedct:260472005",
            PermissibleValue(
                text="snomedct:260472005",
                title="Occipitomental - 45 degree",
                meaning=SNOMEDCT["260472005"]))
        setattr(cls, "snomedct:260473000",
            PermissibleValue(
                text="snomedct:260473000",
                title="Waters - 35 degree tilt to radiographic baseline",
                meaning=SNOMEDCT["260473000"]))
        setattr(cls, "snomedct:260475007",
            PermissibleValue(
                text="snomedct:260475007",
                title="Submentovertical reduced exposure for zygomatic arches",
                meaning=SNOMEDCT["260475007"]))
        setattr(cls, "snomedct:260476008",
            PermissibleValue(
                text="snomedct:260476008",
                title="Slit submentovertical",
                meaning=SNOMEDCT["260476008"]))
        setattr(cls, "snomedct:260477004",
            PermissibleValue(
                text="snomedct:260477004",
                title="Dental/oral projection",
                meaning=SNOMEDCT["260477004"]))
        setattr(cls, "snomedct:260478009",
            PermissibleValue(
                text="snomedct:260478009",
                title="Body - molar",
                meaning=SNOMEDCT["260478009"]))
        setattr(cls, "snomedct:260479001",
            PermissibleValue(
                text="snomedct:260479001",
                title="Body - premolar",
                meaning=SNOMEDCT["260479001"]))
        setattr(cls, "snomedct:260481004",
            PermissibleValue(
                text="snomedct:260481004",
                title="Ramus projection",
                meaning=SNOMEDCT["260481004"]))
        setattr(cls, "snomedct:260482006",
            PermissibleValue(
                text="snomedct:260482006",
                title="Bimolar projection",
                meaning=SNOMEDCT["260482006"]))
        setattr(cls, "snomedct:260483001",
            PermissibleValue(
                text="snomedct:260483001",
                title="Transpharyngeal projection",
                meaning=SNOMEDCT["260483001"]))
        setattr(cls, "snomedct:260484007",
            PermissibleValue(
                text="snomedct:260484007",
                title="Transmaxillary projection",
                meaning=SNOMEDCT["260484007"]))
        setattr(cls, "snomedct:260485008",
            PermissibleValue(
                text="snomedct:260485008",
                title="Temporomandibular joint setting",
                meaning=SNOMEDCT["260485008"]))
        setattr(cls, "snomedct:260486009",
            PermissibleValue(
                text="snomedct:260486009",
                title="Maxillary sinus setting",
                meaning=SNOMEDCT["260486009"]))
        setattr(cls, "snomedct:260487000",
            PermissibleValue(
                text="snomedct:260487000",
                title="Dental panoramic",
                meaning=SNOMEDCT["260487000"]))
        setattr(cls, "snomedct:260489002",
            PermissibleValue(
                text="snomedct:260489002",
                title="Implant setting projection",
                meaning=SNOMEDCT["260489002"]))
        setattr(cls, "snomedct:260490006",
            PermissibleValue(
                text="snomedct:260490006",
                title="Segmental setting",
                meaning=SNOMEDCT["260490006"]))
        setattr(cls, "snomedct:260491005",
            PermissibleValue(
                text="snomedct:260491005",
                title="Axial view for sesamoid bones",
                meaning=SNOMEDCT["260491005"]))
        setattr(cls, "snomedct:260492003",
            PermissibleValue(
                text="snomedct:260492003",
                title="Brewerton's projection",
                meaning=SNOMEDCT["260492003"]))
        setattr(cls, "snomedct:260493008",
            PermissibleValue(
                text="snomedct:260493008",
                title="Harris Beath axial projection",
                meaning=SNOMEDCT["260493008"]))
        setattr(cls, "snomedct:260494002",
            PermissibleValue(
                text="snomedct:260494002",
                title="Intercondylar projection",
                meaning=SNOMEDCT["260494002"]))
        setattr(cls, "snomedct:260496000",
            PermissibleValue(
                text="snomedct:260496000",
                title="Judet projection",
                meaning=SNOMEDCT["260496000"]))
        setattr(cls, "snomedct:260497009",
            PermissibleValue(
                text="snomedct:260497009",
                title="Mortice projection",
                meaning=SNOMEDCT["260497009"]))
        setattr(cls, "snomedct:260499007",
            PermissibleValue(
                text="snomedct:260499007",
                title="Occlusal projection",
                meaning=SNOMEDCT["260499007"]))
        setattr(cls, "snomedct:260500003",
            PermissibleValue(
                text="snomedct:260500003",
                title="Projected oblique occlusal",
                meaning=SNOMEDCT["260500003"]))
        setattr(cls, "snomedct:260501004",
            PermissibleValue(
                text="snomedct:260501004",
                title="Lower true occlusal",
                meaning=SNOMEDCT["260501004"]))
        setattr(cls, "snomedct:260502006",
            PermissibleValue(
                text="snomedct:260502006",
                title="Power grip series",
                meaning=SNOMEDCT["260502006"]))
        setattr(cls, "snomedct:260503001",
            PermissibleValue(
                text="snomedct:260503001",
                title="Radial head projection",
                meaning=SNOMEDCT["260503001"]))
        setattr(cls, "snomedct:260504007",
            PermissibleValue(
                text="snomedct:260504007",
                title="Skyline projection",
                meaning=SNOMEDCT["260504007"]))
        setattr(cls, "snomedct:260506009",
            PermissibleValue(
                text="snomedct:260506009",
                title="Van Rosen projection",
                meaning=SNOMEDCT["260506009"]))
        setattr(cls, "snomedct:260514003",
            PermissibleValue(
                text="snomedct:260514003",
                title="Via body reference line",
                meaning=SNOMEDCT["260514003"]))
        setattr(cls, "snomedct:260520002",
            PermissibleValue(
                text="snomedct:260520002",
                title="Extracorporeal",
                meaning=SNOMEDCT["260520002"]))
        setattr(cls, "snomedct:260521003",
            PermissibleValue(
                text="snomedct:260521003",
                title="Internal",
                meaning=SNOMEDCT["260521003"]))
        setattr(cls, "snomedct:260528009",
            PermissibleValue(
                text="snomedct:260528009",
                title="Median",
                meaning=SNOMEDCT["260528009"]))
        setattr(cls, "snomedct:260529001",
            PermissibleValue(
                text="snomedct:260529001",
                title="Vectors",
                meaning=SNOMEDCT["260529001"]))
        setattr(cls, "snomedct:260530006",
            PermissibleValue(
                text="snomedct:260530006",
                title="Via body region",
                meaning=SNOMEDCT["260530006"]))
        setattr(cls, "snomedct:260532003",
            PermissibleValue(
                text="snomedct:260532003",
                title="Thoracoabdominal",
                meaning=SNOMEDCT["260532003"]))
        setattr(cls, "snomedct:260535001",
            PermissibleValue(
                text="snomedct:260535001",
                title="Lateral extrapleural",
                meaning=SNOMEDCT["260535001"]))
        setattr(cls, "snomedct:260541008",
            PermissibleValue(
                text="snomedct:260541008",
                title="Nasopancreatic",
                meaning=SNOMEDCT["260541008"]))
        setattr(cls, "snomedct:260544000",
            PermissibleValue(
                text="snomedct:260544000",
                title="Endobronchial",
                meaning=SNOMEDCT["260544000"]))
        setattr(cls, "snomedct:260549005",
            PermissibleValue(
                text="snomedct:260549005",
                title="Orogastric",
                meaning=SNOMEDCT["260549005"]))
        setattr(cls, "snomedct:260568008",
            PermissibleValue(
                text="snomedct:260568008",
                title="Via cardiovascular system",
                meaning=SNOMEDCT["260568008"]))
        setattr(cls, "snomedct:260602004",
            PermissibleValue(
                text="snomedct:260602004",
                title="Via superficialized vessel (qualifier value)",
                meaning=SNOMEDCT["260602004"]))
        setattr(cls, "snomedct:260620008",
            PermissibleValue(
                text="snomedct:260620008",
                title="Postaural approach",
                meaning=SNOMEDCT["260620008"]))
        setattr(cls, "snomedct:260637001",
            PermissibleValue(
                text="snomedct:260637001",
                title="Sublabial transseptal",
                meaning=SNOMEDCT["260637001"]))
        setattr(cls, "snomedct:260641002",
            PermissibleValue(
                text="snomedct:260641002",
                title="Extraperitoneal",
                meaning=SNOMEDCT["260641002"]))
        setattr(cls, "snomedct:260642009",
            PermissibleValue(
                text="snomedct:260642009",
                title="Retroperitoneal",
                meaning=SNOMEDCT["260642009"]))
        setattr(cls, "snomedct:260668002",
            PermissibleValue(
                text="snomedct:260668002",
                title="Venovenous",
                meaning=SNOMEDCT["260668002"]))
        setattr(cls, "snomedct:261045000",
            PermissibleValue(
                text="snomedct:261045000",
                title="Anterior dorsal",
                meaning=SNOMEDCT["261045000"]))
        setattr(cls, "snomedct:261052003",
            PermissibleValue(
                text="snomedct:261052003",
                title="Aortocoronary",
                meaning=SNOMEDCT["261052003"]))
        setattr(cls, "snomedct:261054002",
            PermissibleValue(
                text="snomedct:261054002",
                title="Arterio-arterial",
                meaning=SNOMEDCT["261054002"]))
        setattr(cls, "snomedct:261055001",
            PermissibleValue(
                text="snomedct:261055001",
                title="Arteriovenous",
                meaning=SNOMEDCT["261055001"]))
        setattr(cls, "snomedct:261057009",
            PermissibleValue(
                text="snomedct:261057009",
                title="Between intestinal loops",
                meaning=SNOMEDCT["261057009"]))
        setattr(cls, "snomedct:261059007",
            PermissibleValue(
                text="snomedct:261059007",
                title="Bicoronal",
                meaning=SNOMEDCT["261059007"]))
        setattr(cls, "snomedct:261065007",
            PermissibleValue(
                text="snomedct:261065007",
                title="Circumareolar",
                meaning=SNOMEDCT["261065007"]))
        setattr(cls, "snomedct:261067004",
            PermissibleValue(
                text="snomedct:261067004",
                title="Dorsal part",
                meaning=SNOMEDCT["261067004"]))
        setattr(cls, "snomedct:261073003",
            PermissibleValue(
                text="snomedct:261073003",
                title="Epicardial",
                meaning=SNOMEDCT["261073003"]))
        setattr(cls, "snomedct:261074009",
            PermissibleValue(
                text="snomedct:261074009",
                title="External",
                meaning=SNOMEDCT["261074009"]))
        setattr(cls, "snomedct:261075005",
            PermissibleValue(
                text="snomedct:261075005",
                title="Extra-amniotic",
                meaning=SNOMEDCT["261075005"]))
        setattr(cls, "snomedct:261076006",
            PermissibleValue(
                text="snomedct:261076006",
                title="Extracoronal",
                meaning=SNOMEDCT["261076006"]))
        setattr(cls, "snomedct:261089000",
            PermissibleValue(
                text="snomedct:261089000",
                title="Inferior",
                meaning=SNOMEDCT["261089000"]))
        setattr(cls, "snomedct:261094000",
            PermissibleValue(
                text="snomedct:261094000",
                title="Into urinary bladder",
                meaning=SNOMEDCT["261094000"]))
        setattr(cls, "snomedct:261095004",
            PermissibleValue(
                text="snomedct:261095004",
                title="Into ureter",
                meaning=SNOMEDCT["261095004"]))
        setattr(cls, "snomedct:261097007",
            PermissibleValue(
                text="snomedct:261097007",
                title="Intracoronal",
                meaning=SNOMEDCT["261097007"]))
        setattr(cls, "snomedct:261100002",
            PermissibleValue(
                text="snomedct:261100002",
                title="Intraperitoneal",
                meaning=SNOMEDCT["261100002"]))
        setattr(cls, "snomedct:261101003",
            PermissibleValue(
                text="snomedct:261101003",
                title="Intravascular",
                meaning=SNOMEDCT["261101003"]))
        setattr(cls, "snomedct:261117009",
            PermissibleValue(
                text="snomedct:261117009",
                title="Laryngotracheal",
                meaning=SNOMEDCT["261117009"]))
        setattr(cls, "snomedct:261119007",
            PermissibleValue(
                text="snomedct:261119007",
                title="Lateral part",
                meaning=SNOMEDCT["261119007"]))
        setattr(cls, "snomedct:261122009",
            PermissibleValue(
                text="snomedct:261122009",
                title="Lower",
                meaning=SNOMEDCT["261122009"]))
        setattr(cls, "snomedct:261123004",
            PermissibleValue(
                text="snomedct:261123004",
                title="Lower anterior",
                meaning=SNOMEDCT["261123004"]))
        setattr(cls, "snomedct:261128008",
            PermissibleValue(
                text="snomedct:261128008",
                title="Medial part",
                meaning=SNOMEDCT["261128008"]))
        setattr(cls, "snomedct:261131009",
            PermissibleValue(
                text="snomedct:261131009",
                title="Midaxillary",
                meaning=SNOMEDCT["261131009"]))
        setattr(cls, "snomedct:261132002",
            PermissibleValue(
                text="snomedct:261132002",
                title="Midclavicular",
                meaning=SNOMEDCT["261132002"]))
        setattr(cls, "snomedct:261133007",
            PermissibleValue(
                text="snomedct:261133007",
                title="Middle third",
                meaning=SNOMEDCT["261133007"]))
        setattr(cls, "snomedct:261136004",
            PermissibleValue(
                text="snomedct:261136004",
                title="Mural",
                meaning=SNOMEDCT["261136004"]))
        setattr(cls, "snomedct:261137008",
            PermissibleValue(
                text="snomedct:261137008",
                title="Musculocutaneous",
                meaning=SNOMEDCT["261137008"]))
        setattr(cls, "snomedct:261146002",
            PermissibleValue(
                text="snomedct:261146002",
                title="Para-aortic",
                meaning=SNOMEDCT["261146002"]))
        setattr(cls, "snomedct:261147006",
            PermissibleValue(
                text="snomedct:261147006",
                title="Paracolic",
                meaning=SNOMEDCT["261147006"]))
        setattr(cls, "snomedct:261148001",
            PermissibleValue(
                text="snomedct:261148001",
                title="Paraspinal",
                meaning=SNOMEDCT["261148001"]))
        setattr(cls, "snomedct:261149009",
            PermissibleValue(
                text="snomedct:261149009",
                title="Parasternal",
                meaning=SNOMEDCT["261149009"]))
        setattr(cls, "snomedct:261154000",
            PermissibleValue(
                text="snomedct:261154000",
                title="Penis and urinary bladder neck",
                meaning=SNOMEDCT["261154000"]))
        setattr(cls, "snomedct:261156003",
            PermissibleValue(
                text="snomedct:261156003",
                title="Periadrenal",
                meaning=SNOMEDCT["261156003"]))
        setattr(cls, "snomedct:261165005",
            PermissibleValue(
                text="snomedct:261165005",
                title="Posterior dorsal",
                meaning=SNOMEDCT["261165005"]))
        setattr(cls, "snomedct:261172006",
            PermissibleValue(
                text="snomedct:261172006",
                title="Proximal third",
                meaning=SNOMEDCT["261172006"]))
        setattr(cls, "snomedct:261174007",
            PermissibleValue(
                text="snomedct:261174007",
                title="Retrocecal (qualifier value)",
                meaning=SNOMEDCT["261174007"]))
        setattr(cls, "snomedct:261175008",
            PermissibleValue(
                text="snomedct:261175008",
                title="Retroduodenal",
                meaning=SNOMEDCT["261175008"]))
        setattr(cls, "snomedct:261181000",
            PermissibleValue(
                text="snomedct:261181000",
                title="Tracheobronchial",
                meaning=SNOMEDCT["261181000"]))
        setattr(cls, "snomedct:261183002",
            PermissibleValue(
                text="snomedct:261183002",
                title="Upper",
                meaning=SNOMEDCT["261183002"]))
        setattr(cls, "snomedct:261184008",
            PermissibleValue(
                text="snomedct:261184008",
                title="Upper anterior",
                meaning=SNOMEDCT["261184008"]))
        setattr(cls, "snomedct:261185009",
            PermissibleValue(
                text="snomedct:261185009",
                title="Venoarterial",
                meaning=SNOMEDCT["261185009"]))
        setattr(cls, "snomedct:261186005",
            PermissibleValue(
                text="snomedct:261186005",
                title="Ventral part",
                meaning=SNOMEDCT["261186005"]))
        setattr(cls, "snomedct:261411001",
            PermissibleValue(
                text="snomedct:261411001",
                title="Distal third",
                meaning=SNOMEDCT["261411001"]))
        setattr(cls, "snomedct:261446009",
            PermissibleValue(
                text="snomedct:261446009",
                title="Transpulmonary annulus",
                meaning=SNOMEDCT["261446009"]))
        setattr(cls, "snomedct:261466000",
            PermissibleValue(
                text="snomedct:261466000",
                title="Via intrapulmonary trunk tunnel",
                meaning=SNOMEDCT["261466000"]))
        setattr(cls, "snomedct:261469007",
            PermissibleValue(
                text="snomedct:261469007",
                title="Via orbitotomy",
                meaning=SNOMEDCT["261469007"]))
        setattr(cls, "snomedct:261760007",
            PermissibleValue(
                text="snomedct:261760007",
                title="Deep to rectus abdominis",
                meaning=SNOMEDCT["261760007"]))
        setattr(cls, "snomedct:261788001",
            PermissibleValue(
                text="snomedct:261788001",
                title="Exteriorized (qualifier value)",
                meaning=SNOMEDCT["261788001"]))
        setattr(cls, "snomedct:261799004",
            PermissibleValue(
                text="snomedct:261799004",
                title="From existing graft to coronary artery",
                meaning=SNOMEDCT["261799004"]))
        setattr(cls, "snomedct:261847009",
            PermissibleValue(
                text="snomedct:261847009",
                title="Intracervical",
                meaning=SNOMEDCT["261847009"]))
        setattr(cls, "snomedct:261851006",
            PermissibleValue(
                text="snomedct:261851006",
                title="Internally to bladder",
                meaning=SNOMEDCT["261851006"]))
        setattr(cls, "snomedct:261945002",
            PermissibleValue(
                text="snomedct:261945002",
                title="Mixed venoarterial and venovenous",
                meaning=SNOMEDCT["261945002"]))
        setattr(cls, "snomedct:261964008",
            PermissibleValue(
                text="snomedct:261964008",
                title="Muscle fibers only (qualifier value)",
                meaning=SNOMEDCT["261964008"]))
        setattr(cls, "snomedct:261980003",
            PermissibleValue(
                text="snomedct:261980003",
                title="Neuromuscular junction only",
                meaning=SNOMEDCT["261980003"]))
        setattr(cls, "snomedct:262379005",
            PermissibleValue(
                text="snomedct:262379005",
                title="Dominant side",
                meaning=SNOMEDCT["262379005"]))
        setattr(cls, "snomedct:262458006",
            PermissibleValue(
                text="snomedct:262458006",
                title="Non-dominant side",
                meaning=SNOMEDCT["262458006"]))
        setattr(cls, "snomedct:263672002",
            PermissibleValue(
                text="snomedct:263672002",
                title="Anocutaneous",
                meaning=SNOMEDCT["263672002"]))
        setattr(cls, "snomedct:263674001",
            PermissibleValue(
                text="snomedct:263674001",
                title="Anovestibular",
                meaning=SNOMEDCT["263674001"]))
        setattr(cls, "snomedct:263759007",
            PermissibleValue(
                text="snomedct:263759007",
                title="Foraminal",
                meaning=SNOMEDCT["263759007"]))
        setattr(cls, "snomedct:263794000",
            PermissibleValue(
                text="snomedct:263794000",
                title="Left side-by-side",
                meaning=SNOMEDCT["263794000"]))
        setattr(cls, "snomedct:263795004",
            PermissibleValue(
                text="snomedct:263795004",
                title="Left sided",
                meaning=SNOMEDCT["263795004"]))
        setattr(cls, "snomedct:263830001",
            PermissibleValue(
                text="snomedct:263830001",
                title="Panacinar",
                meaning=SNOMEDCT["263830001"]))
        setattr(cls, "snomedct:263831002",
            PermissibleValue(
                text="snomedct:263831002",
                title="Panlobular",
                meaning=SNOMEDCT["263831002"]))
        setattr(cls, "snomedct:263838008",
            PermissibleValue(
                text="snomedct:263838008",
                title="Periacinar",
                meaning=SNOMEDCT["263838008"]))
        setattr(cls, "snomedct:263846009",
            PermissibleValue(
                text="snomedct:263846009",
                title="Prevascular",
                meaning=SNOMEDCT["263846009"]))
        setattr(cls, "snomedct:263848005",
            PermissibleValue(
                text="snomedct:263848005",
                title="Proximal acinar",
                meaning=SNOMEDCT["263848005"]))
        setattr(cls, "snomedct:263869007",
            PermissibleValue(
                text="snomedct:263869007",
                title="Separate",
                meaning=SNOMEDCT["263869007"]))
        setattr(cls, "snomedct:263887005",
            PermissibleValue(
                text="snomedct:263887005",
                title="Subcutaneous",
                meaning=SNOMEDCT["263887005"]))
        setattr(cls, "snomedct:263938007",
            PermissibleValue(
                text="snomedct:263938007",
                title="Above middle turbinate",
                meaning=SNOMEDCT["263938007"]))
        setattr(cls, "snomedct:263942005",
            PermissibleValue(
                text="snomedct:263942005",
                title="Anterior segment",
                meaning=SNOMEDCT["263942005"]))
        setattr(cls, "snomedct:263943000",
            PermissibleValue(
                text="snomedct:263943000",
                title="Anterior wall",
                meaning=SNOMEDCT["263943000"]))
        setattr(cls, "snomedct:263952009",
            PermissibleValue(
                text="snomedct:263952009",
                title="Periorbital",
                meaning=SNOMEDCT["263952009"]))
        setattr(cls, "snomedct:263953004",
            PermissibleValue(
                text="snomedct:263953004",
                title="Perioral",
                meaning=SNOMEDCT["263953004"]))
        setattr(cls, "snomedct:263955006",
            PermissibleValue(
                text="snomedct:263955006",
                title="Atlantoaxial",
                meaning=SNOMEDCT["263955006"]))
        setattr(cls, "snomedct:263958008",
            PermissibleValue(
                text="snomedct:263958008",
                title="Between left common carotid and brachiocephalic arteries",
                meaning=SNOMEDCT["263958008"]))
        setattr(cls, "snomedct:263959000",
            PermissibleValue(
                text="snomedct:263959000",
                title="Between left subclavian and common carotid arteries",
                meaning=SNOMEDCT["263959000"]))
        setattr(cls, "snomedct:263965000",
            PermissibleValue(
                text="snomedct:263965000",
                title="Bronchocutaneous",
                meaning=SNOMEDCT["263965000"]))
        setattr(cls, "snomedct:263966004",
            PermissibleValue(
                text="snomedct:263966004",
                title="Bronchopleural",
                meaning=SNOMEDCT["263966004"]))
        setattr(cls, "snomedct:263969006",
            PermissibleValue(
                text="snomedct:263969006",
                title="Centriacinar",
                meaning=SNOMEDCT["263969006"]))
        setattr(cls, "snomedct:263970007",
            PermissibleValue(
                text="snomedct:263970007",
                title="Centrilobular",
                meaning=SNOMEDCT["263970007"]))
        setattr(cls, "snomedct:263974003",
            PermissibleValue(
                text="snomedct:263974003",
                title="Cervicothoracic",
                meaning=SNOMEDCT["263974003"]))
        setattr(cls, "snomedct:263975002",
            PermissibleValue(
                text="snomedct:263975002",
                title="Cervicothoracolumbar",
                meaning=SNOMEDCT["263975002"]))
        setattr(cls, "snomedct:263981005",
            PermissibleValue(
                text="snomedct:263981005",
                title="Distal to left subclavian artery",
                meaning=SNOMEDCT["263981005"]))
        setattr(cls, "snomedct:263990003",
            PermissibleValue(
                text="snomedct:263990003",
                title="Duodenoduodenal",
                meaning=SNOMEDCT["263990003"]))
        setattr(cls, "snomedct:263991004",
            PermissibleValue(
                text="snomedct:263991004",
                title="Duodenojejunal",
                meaning=SNOMEDCT["263991004"]))
        setattr(cls, "snomedct:263996009",
            PermissibleValue(
                text="snomedct:263996009",
                title="Extrafoveal",
                meaning=SNOMEDCT["263996009"]))
        setattr(cls, "snomedct:263997000",
            PermissibleValue(
                text="snomedct:263997000",
                title="Extraureteric",
                meaning=SNOMEDCT["263997000"]))
        setattr(cls, "snomedct:263998005",
            PermissibleValue(
                text="snomedct:263998005",
                title="Extravaginal",
                meaning=SNOMEDCT["263998005"]))
        setattr(cls, "snomedct:263999002",
            PermissibleValue(
                text="snomedct:263999002",
                title="From anterosuperior-superior bridging leaflet commissure",
                meaning=SNOMEDCT["263999002"]))
        setattr(cls, "snomedct:264000000",
            PermissibleValue(
                text="snomedct:264000000",
                title="From left inferior bridging leaflet-lateral commissure",
                meaning=SNOMEDCT["264000000"]))
        setattr(cls, "snomedct:264001001",
            PermissibleValue(
                text="snomedct:264001001",
                title="From left septal commissure",
                meaning=SNOMEDCT["264001001"]))
        setattr(cls, "snomedct:264002008",
            PermissibleValue(
                text="snomedct:264002008",
                title="From left superior bridging leaflet-lateral commissure",
                meaning=SNOMEDCT["264002008"]))
        setattr(cls, "snomedct:264004009",
            PermissibleValue(
                text="snomedct:264004009",
                title="From left ventricular component",
                meaning=SNOMEDCT["264004009"]))
        setattr(cls, "snomedct:264005005",
            PermissibleValue(
                text="snomedct:264005005",
                title="From right anterosuperior-inferior commissure",
                meaning=SNOMEDCT["264005005"]))
        setattr(cls, "snomedct:264006006",
            PermissibleValue(
                text="snomedct:264006006",
                title="From right inferior bridging leaflet-inferior commissure",
                meaning=SNOMEDCT["264006006"]))
        setattr(cls, "snomedct:264007002",
            PermissibleValue(
                text="snomedct:264007002",
                title="From right septal commissure",
                meaning=SNOMEDCT["264007002"]))
        setattr(cls, "snomedct:264008007",
            PermissibleValue(
                text="snomedct:264008007",
                title="From right ventricular component",
                meaning=SNOMEDCT["264008007"]))
        setattr(cls, "snomedct:264011008",
            PermissibleValue(
                text="snomedct:264011008",
                title="Gastroduodenal",
                meaning=SNOMEDCT["264011008"]))
        setattr(cls, "snomedct:264012001",
            PermissibleValue(
                text="snomedct:264012001",
                title="Gastrogastric",
                meaning=SNOMEDCT["264012001"]))
        setattr(cls, "snomedct:264015004",
            PermissibleValue(
                text="snomedct:264015004",
                title="Hepatopleural",
                meaning=SNOMEDCT["264015004"]))
        setattr(cls, "snomedct:264023002",
            PermissibleValue(
                text="snomedct:264023002",
                title="Ileocecal (qualifier value)",
                meaning=SNOMEDCT["264023002"]))
        setattr(cls, "snomedct:264024008",
            PermissibleValue(
                text="snomedct:264024008",
                title="Ileocolic",
                meaning=SNOMEDCT["264024008"]))
        setattr(cls, "snomedct:264025009",
            PermissibleValue(
                text="snomedct:264025009",
                title="Iliofemoral vein zone",
                meaning=SNOMEDCT["264025009"]))
        setattr(cls, "snomedct:264026005",
            PermissibleValue(
                text="snomedct:264026005",
                title="Ileo-ileal",
                meaning=SNOMEDCT["264026005"]))
        setattr(cls, "snomedct:264027001",
            PermissibleValue(
                text="snomedct:264027001",
                title="Ileorectal",
                meaning=SNOMEDCT["264027001"]))
        setattr(cls, "snomedct:264030008",
            PermissibleValue(
                text="snomedct:264030008",
                title="In joint",
                meaning=SNOMEDCT["264030008"]))
        setattr(cls, "snomedct:264031007",
            PermissibleValue(
                text="snomedct:264031007",
                title="In situ",
                meaning=SNOMEDCT["264031007"]))
        setattr(cls, "snomedct:264034004",
            PermissibleValue(
                text="snomedct:264034004",
                title="Infracardiac",
                meaning=SNOMEDCT["264034004"]))
        setattr(cls, "snomedct:264035003",
            PermissibleValue(
                text="snomedct:264035003",
                title="Infravesical",
                meaning=SNOMEDCT["264035003"]))
        setattr(cls, "snomedct:264040006",
            PermissibleValue(
                text="snomedct:264040006",
                title="Interchordal",
                meaning=SNOMEDCT["264040006"]))
        setattr(cls, "snomedct:264041005",
            PermissibleValue(
                text="snomedct:264041005",
                title="Interdigital",
                meaning=SNOMEDCT["264041005"]))
        setattr(cls, "snomedct:264042003",
            PermissibleValue(
                text="snomedct:264042003",
                title="Intervertebral",
                meaning=SNOMEDCT["264042003"]))
        setattr(cls, "snomedct:264043008",
            PermissibleValue(
                text="snomedct:264043008",
                title="Intraligamentous",
                meaning=SNOMEDCT["264043008"]))
        setattr(cls, "snomedct:264044002",
            PermissibleValue(
                text="snomedct:264044002",
                title="Intracardiac",
                meaning=SNOMEDCT["264044002"]))
        setattr(cls, "snomedct:264045001",
            PermissibleValue(
                text="snomedct:264045001",
                title="Intraluminal",
                meaning=SNOMEDCT["264045001"]))
        setattr(cls, "snomedct:264046000",
            PermissibleValue(
                text="snomedct:264046000",
                title="Intramammary",
                meaning=SNOMEDCT["264046000"]))
        setattr(cls, "snomedct:264047009",
            PermissibleValue(
                text="snomedct:264047009",
                title="Intrapulmonary",
                meaning=SNOMEDCT["264047009"]))
        setattr(cls, "snomedct:264049007",
            PermissibleValue(
                text="snomedct:264049007",
                title="Intravaginal",
                meaning=SNOMEDCT["264049007"]))
        setattr(cls, "snomedct:264056001",
            PermissibleValue(
                text="snomedct:264056001",
                title="Lateral column",
                meaning=SNOMEDCT["264056001"]))
        setattr(cls, "snomedct:264060003",
            PermissibleValue(
                text="snomedct:264060003",
                title="Lateral segment",
                meaning=SNOMEDCT["264060003"]))
        setattr(cls, "snomedct:264065008",
            PermissibleValue(
                text="snomedct:264065008",
                title="Left anterior",
                meaning=SNOMEDCT["264065008"]))
        setattr(cls, "snomedct:264067000",
            PermissibleValue(
                text="snomedct:264067000",
                title="Left lateral wall",
                meaning=SNOMEDCT["264067000"]))
        setattr(cls, "snomedct:264068005",
            PermissibleValue(
                text="snomedct:264068005",
                title="Left lower segment",
                meaning=SNOMEDCT["264068005"]))
        setattr(cls, "snomedct:264076007",
            PermissibleValue(
                text="snomedct:264076007",
                title="Lower left parasternal",
                meaning=SNOMEDCT["264076007"]))
        setattr(cls, "snomedct:264081003",
            PermissibleValue(
                text="snomedct:264081003",
                title="Lower third",
                meaning=SNOMEDCT["264081003"]))
        setattr(cls, "snomedct:264083000",
            PermissibleValue(
                text="snomedct:264083000",
                title="Lumbosacral",
                meaning=SNOMEDCT["264083000"]))
        setattr(cls, "snomedct:264096004",
            PermissibleValue(
                text="snomedct:264096004",
                title="Medial segment",
                meaning=SNOMEDCT["264096004"]))
        setattr(cls, "snomedct:264103001",
            PermissibleValue(
                text="snomedct:264103001",
                title="Midtarsal",
                meaning=SNOMEDCT["264103001"]))
        setattr(cls, "snomedct:264107000",
            PermissibleValue(
                text="snomedct:264107000",
                title="Paravertebral",
                meaning=SNOMEDCT["264107000"]))
        setattr(cls, "snomedct:264110007",
            PermissibleValue(
                text="snomedct:264110007",
                title="Esophagocolonic (qualifier value)",
                meaning=SNOMEDCT["264110007"]))
        setattr(cls, "snomedct:264111006",
            PermissibleValue(
                text="snomedct:264111006",
                title="Esophagogastric (qualifier value)",
                meaning=SNOMEDCT["264111006"]))
        setattr(cls, "snomedct:264112004",
            PermissibleValue(
                text="snomedct:264112004",
                title="Esophagojejunal (qualifier value)",
                meaning=SNOMEDCT["264112004"]))
        setattr(cls, "snomedct:264114003",
            PermissibleValue(
                text="snomedct:264114003",
                title="Ostium",
                meaning=SNOMEDCT["264114003"]))
        setattr(cls, "snomedct:264117005",
            PermissibleValue(
                text="snomedct:264117005",
                title="Paraesophageal (qualifier value)",
                meaning=SNOMEDCT["264117005"]))
        setattr(cls, "snomedct:264118000",
            PermissibleValue(
                text="snomedct:264118000",
                title="Paraduodenal",
                meaning=SNOMEDCT["264118000"]))
        setattr(cls, "snomedct:264119008",
            PermissibleValue(
                text="snomedct:264119008",
                title="Parafoveal",
                meaning=SNOMEDCT["264119008"]))
        setattr(cls, "snomedct:264121003",
            PermissibleValue(
                text="snomedct:264121003",
                title="Paramacular",
                meaning=SNOMEDCT["264121003"]))
        setattr(cls, "snomedct:264123000",
            PermissibleValue(
                text="snomedct:264123000",
                title="Paraseptal",
                meaning=SNOMEDCT["264123000"]))
        setattr(cls, "snomedct:264124006",
            PermissibleValue(
                text="snomedct:264124006",
                title="Paraumbilical",
                meaning=SNOMEDCT["264124006"]))
        setattr(cls, "snomedct:264126008",
            PermissibleValue(
                text="snomedct:264126008",
                title="Paravascular",
                meaning=SNOMEDCT["264126008"]))
        setattr(cls, "snomedct:264127004",
            PermissibleValue(
                text="snomedct:264127004",
                title="Paraovarian",
                meaning=SNOMEDCT["264127004"]))
        setattr(cls, "snomedct:264128009",
            PermissibleValue(
                text="snomedct:264128009",
                title="Paratracheal",
                meaning=SNOMEDCT["264128009"]))
        setattr(cls, "snomedct:264131005",
            PermissibleValue(
                text="snomedct:264131005",
                title="Peri-intestinal",
                meaning=SNOMEDCT["264131005"]))
        setattr(cls, "snomedct:264133008",
            PermissibleValue(
                text="snomedct:264133008",
                title="Perianal",
                meaning=SNOMEDCT["264133008"]))
        setattr(cls, "snomedct:264136000",
            PermissibleValue(
                text="snomedct:264136000",
                title="Perihepatic",
                meaning=SNOMEDCT["264136000"]))
        setattr(cls, "snomedct:264137009",
            PermissibleValue(
                text="snomedct:264137009",
                title="Perinephric",
                meaning=SNOMEDCT["264137009"]))
        setattr(cls, "snomedct:264139007",
            PermissibleValue(
                text="snomedct:264139007",
                title="Peripancreatic",
                meaning=SNOMEDCT["264139007"]))
        setattr(cls, "snomedct:264142001",
            PermissibleValue(
                text="snomedct:264142001",
                title="Perisplenic",
                meaning=SNOMEDCT["264142001"]))
        setattr(cls, "snomedct:264153007",
            PermissibleValue(
                text="snomedct:264153007",
                title="Posterior pole",
                meaning=SNOMEDCT["264153007"]))
        setattr(cls, "snomedct:264154001",
            PermissibleValue(
                text="snomedct:264154001",
                title="Posterior segment",
                meaning=SNOMEDCT["264154001"]))
        setattr(cls, "snomedct:264159006",
            PermissibleValue(
                text="snomedct:264159006",
                title="Posterior wall",
                meaning=SNOMEDCT["264159006"]))
        setattr(cls, "snomedct:264168008",
            PermissibleValue(
                text="snomedct:264168008",
                title="Rectocloacal",
                meaning=SNOMEDCT["264168008"]))
        setattr(cls, "snomedct:264169000",
            PermissibleValue(
                text="snomedct:264169000",
                title="Rectocutaneous",
                meaning=SNOMEDCT["264169000"]))
        setattr(cls, "snomedct:264170004",
            PermissibleValue(
                text="snomedct:264170004",
                title="Rectourethral",
                meaning=SNOMEDCT["264170004"]))
        setattr(cls, "snomedct:264171000",
            PermissibleValue(
                text="snomedct:264171000",
                title="Rectovaginal",
                meaning=SNOMEDCT["264171000"]))
        setattr(cls, "snomedct:264172007",
            PermissibleValue(
                text="snomedct:264172007",
                title="Rectovesical",
                meaning=SNOMEDCT["264172007"]))
        setattr(cls, "snomedct:264173002",
            PermissibleValue(
                text="snomedct:264173002",
                title="Rectovulval",
                meaning=SNOMEDCT["264173002"]))
        setattr(cls, "snomedct:264174008",
            PermissibleValue(
                text="snomedct:264174008",
                title="Retromammary",
                meaning=SNOMEDCT["264174008"]))
        setattr(cls, "snomedct:264175009",
            PermissibleValue(
                text="snomedct:264175009",
                title="Retrocolumellar",
                meaning=SNOMEDCT["264175009"]))
        setattr(cls, "snomedct:264176005",
            PermissibleValue(
                text="snomedct:264176005",
                title="Right anterior",
                meaning=SNOMEDCT["264176005"]))
        setattr(cls, "snomedct:264178006",
            PermissibleValue(
                text="snomedct:264178006",
                title="Right lateral wall",
                meaning=SNOMEDCT["264178006"]))
        setattr(cls, "snomedct:264179003",
            PermissibleValue(
                text="snomedct:264179003",
                title="Right side-by-side",
                meaning=SNOMEDCT["264179003"]))
        setattr(cls, "snomedct:264180000",
            PermissibleValue(
                text="snomedct:264180000",
                title="Right sided",
                meaning=SNOMEDCT["264180000"]))
        setattr(cls, "snomedct:264193005",
            PermissibleValue(
                text="snomedct:264193005",
                title="Segment",
                meaning=SNOMEDCT["264193005"]))
        setattr(cls, "snomedct:264201006",
            PermissibleValue(
                text="snomedct:264201006",
                title="Sternocostal",
                meaning=SNOMEDCT["264201006"]))
        setattr(cls, "snomedct:264202004",
            PermissibleValue(
                text="snomedct:264202004",
                title="Subaortic",
                meaning=SNOMEDCT["264202004"]))
        setattr(cls, "snomedct:264205002",
            PermissibleValue(
                text="snomedct:264205002",
                title="Subareolar",
                meaning=SNOMEDCT["264205002"]))
        setattr(cls, "snomedct:264206001",
            PermissibleValue(
                text="snomedct:264206001",
                title="Subconjunctival",
                meaning=SNOMEDCT["264206001"]))
        setattr(cls, "snomedct:264208000",
            PermissibleValue(
                text="snomedct:264208000",
                title="Subcostal",
                meaning=SNOMEDCT["264208000"]))
        setattr(cls, "snomedct:264209008",
            PermissibleValue(
                text="snomedct:264209008",
                title="Subfoveal",
                meaning=SNOMEDCT["264209008"]))
        setattr(cls, "snomedct:264216009",
            PermissibleValue(
                text="snomedct:264216009",
                title="Superficial to rectus abdominis",
                meaning=SNOMEDCT["264216009"]))
        setattr(cls, "snomedct:264217000",
            PermissibleValue(
                text="snomedct:264217000",
                title="Superior",
                meaning=SNOMEDCT["264217000"]))
        setattr(cls, "snomedct:264221007",
            PermissibleValue(
                text="snomedct:264221007",
                title="Supraumbilical",
                meaning=SNOMEDCT["264221007"]))
        setattr(cls, "snomedct:264222000",
            PermissibleValue(
                text="snomedct:264222000",
                title="Supracardiac",
                meaning=SNOMEDCT["264222000"]))
        setattr(cls, "snomedct:264224004",
            PermissibleValue(
                text="snomedct:264224004",
                title="Supraglottic",
                meaning=SNOMEDCT["264224004"]))
        setattr(cls, "snomedct:264225003",
            PermissibleValue(
                text="snomedct:264225003",
                title="Suprahepatic",
                meaning=SNOMEDCT["264225003"]))
        setattr(cls, "snomedct:264227006",
            PermissibleValue(
                text="snomedct:264227006",
                title="Tarsometatarsal",
                meaning=SNOMEDCT["264227006"]))
        setattr(cls, "snomedct:264232007",
            PermissibleValue(
                text="snomedct:264232007",
                title="Thoracolumbar",
                meaning=SNOMEDCT["264232007"]))
        setattr(cls, "snomedct:264245006",
            PermissibleValue(
                text="snomedct:264245006",
                title="Upper left parasternal",
                meaning=SNOMEDCT["264245006"]))
        setattr(cls, "snomedct:264253003",
            PermissibleValue(
                text="snomedct:264253003",
                title="Upper third",
                meaning=SNOMEDCT["264253003"]))
        setattr(cls, "snomedct:264261008",
            PermissibleValue(
                text="snomedct:264261008",
                title="Cholecystoduodenal",
                meaning=SNOMEDCT["264261008"]))
        setattr(cls, "snomedct:264262001",
            PermissibleValue(
                text="snomedct:264262001",
                title="Cholecystenteric (qualifier value)",
                meaning=SNOMEDCT["264262001"]))
        setattr(cls, "snomedct:264263006",
            PermissibleValue(
                text="snomedct:264263006",
                title="Cholecystogastric",
                meaning=SNOMEDCT["264263006"]))
        setattr(cls, "snomedct:264264000",
            PermissibleValue(
                text="snomedct:264264000",
                title="Choledochoduodenal",
                meaning=SNOMEDCT["264264000"]))
        setattr(cls, "snomedct:264266003",
            PermissibleValue(
                text="snomedct:264266003",
                title="Colocolic",
                meaning=SNOMEDCT["264266003"]))
        setattr(cls, "snomedct:264267007",
            PermissibleValue(
                text="snomedct:264267007",
                title="Colorectal",
                meaning=SNOMEDCT["264267007"]))
        setattr(cls, "snomedct:264463009",
            PermissibleValue(
                text="snomedct:264463009",
                title="Epitrochlear",
                meaning=SNOMEDCT["264463009"]))
        setattr(cls, "snomedct:264940008",
            PermissibleValue(
                text="snomedct:264940008",
                title="Under inferior bridging leaflet",
                meaning=SNOMEDCT["264940008"]))
        setattr(cls, "snomedct:264941007",
            PermissibleValue(
                text="snomedct:264941007",
                title="Under superior bridging leaflet",
                meaning=SNOMEDCT["264941007"]))
        setattr(cls, "snomedct:272288000",
            PermissibleValue(
                text="snomedct:272288000",
                title="Onlay",
                meaning=SNOMEDCT["272288000"]))
        setattr(cls, "snomedct:272425003",
            PermissibleValue(
                text="snomedct:272425003",
                title="General site descriptor",
                meaning=SNOMEDCT["272425003"]))
        setattr(cls, "snomedct:272427006",
            PermissibleValue(
                text="snomedct:272427006",
                title="Anatomical part descriptor",
                meaning=SNOMEDCT["272427006"]))
        setattr(cls, "snomedct:272428001",
            PermissibleValue(
                text="snomedct:272428001",
                title="Anatomical third",
                meaning=SNOMEDCT["272428001"]))
        setattr(cls, "snomedct:272429009",
            PermissibleValue(
                text="snomedct:272429009",
                title="Part structure",
                meaning=SNOMEDCT["272429009"]))
        setattr(cls, "snomedct:272430004",
            PermissibleValue(
                text="snomedct:272430004",
                title="Column structure",
                meaning=SNOMEDCT["272430004"]))
        setattr(cls, "snomedct:272431000",
            PermissibleValue(
                text="snomedct:272431000",
                title="Segment structure",
                meaning=SNOMEDCT["272431000"]))
        setattr(cls, "snomedct:272432007",
            PermissibleValue(
                text="snomedct:272432007",
                title="Wall structure",
                meaning=SNOMEDCT["272432007"]))
        setattr(cls, "snomedct:272434008",
            PermissibleValue(
                text="snomedct:272434008",
                title="Anatomical relationship descriptor",
                meaning=SNOMEDCT["272434008"]))
        setattr(cls, "snomedct:272435009",
            PermissibleValue(
                text="snomedct:272435009",
                title="Centri-location",
                meaning=SNOMEDCT["272435009"]))
        setattr(cls, "snomedct:272436005",
            PermissibleValue(
                text="snomedct:272436005",
                title="Circum-location",
                meaning=SNOMEDCT["272436005"]))
        setattr(cls, "snomedct:272437001",
            PermissibleValue(
                text="snomedct:272437001",
                title="Extra-location",
                meaning=SNOMEDCT["272437001"]))
        setattr(cls, "snomedct:272438006",
            PermissibleValue(
                text="snomedct:272438006",
                title="Extrapleural",
                meaning=SNOMEDCT["272438006"]))
        setattr(cls, "snomedct:272439003",
            PermissibleValue(
                text="snomedct:272439003",
                title="Infra-location",
                meaning=SNOMEDCT["272439003"]))
        setattr(cls, "snomedct:272440001",
            PermissibleValue(
                text="snomedct:272440001",
                title="Inter-location",
                meaning=SNOMEDCT["272440001"]))
        setattr(cls, "snomedct:272441002",
            PermissibleValue(
                text="snomedct:272441002",
                title="Intra-location",
                meaning=SNOMEDCT["272441002"]))
        setattr(cls, "snomedct:272442009",
            PermissibleValue(
                text="snomedct:272442009",
                title="Mid-location",
                meaning=SNOMEDCT["272442009"]))
        setattr(cls, "snomedct:272443004",
            PermissibleValue(
                text="snomedct:272443004",
                title="Pan-location",
                meaning=SNOMEDCT["272443004"]))
        setattr(cls, "snomedct:272444005",
            PermissibleValue(
                text="snomedct:272444005",
                title="Para-location",
                meaning=SNOMEDCT["272444005"]))
        setattr(cls, "snomedct:272446007",
            PermissibleValue(
                text="snomedct:272446007",
                title="Per-location",
                meaning=SNOMEDCT["272446007"]))
        setattr(cls, "snomedct:272447003",
            PermissibleValue(
                text="snomedct:272447003",
                title="Peri-location",
                meaning=SNOMEDCT["272447003"]))
        setattr(cls, "snomedct:272448008",
            PermissibleValue(
                text="snomedct:272448008",
                title="Post-location",
                meaning=SNOMEDCT["272448008"]))
        setattr(cls, "snomedct:272449000",
            PermissibleValue(
                text="snomedct:272449000",
                title="Pre-location",
                meaning=SNOMEDCT["272449000"]))
        setattr(cls, "snomedct:272450000",
            PermissibleValue(
                text="snomedct:272450000",
                title="Retro-location",
                meaning=SNOMEDCT["272450000"]))
        setattr(cls, "snomedct:272451001",
            PermissibleValue(
                text="snomedct:272451001",
                title="Sub-location",
                meaning=SNOMEDCT["272451001"]))
        setattr(cls, "snomedct:272452008",
            PermissibleValue(
                text="snomedct:272452008",
                title="Supra-location",
                meaning=SNOMEDCT["272452008"]))
        setattr(cls, "snomedct:272455005",
            PermissibleValue(
                text="snomedct:272455005",
                title="Inferosuperior projection",
                meaning=SNOMEDCT["272455005"]))
        setattr(cls, "snomedct:272456006",
            PermissibleValue(
                text="snomedct:272456006",
                title="Apical projection",
                meaning=SNOMEDCT["272456006"]))
        setattr(cls, "snomedct:272457002",
            PermissibleValue(
                text="snomedct:272457002",
                title="Vertical projection",
                meaning=SNOMEDCT["272457002"]))
        setattr(cls, "snomedct:272458007",
            PermissibleValue(
                text="snomedct:272458007",
                title="Prone projection",
                meaning=SNOMEDCT["272458007"]))
        setattr(cls, "snomedct:272459004",
            PermissibleValue(
                text="snomedct:272459004",
                title="Supine projection",
                meaning=SNOMEDCT["272459004"]))
        setattr(cls, "snomedct:272460009",
            PermissibleValue(
                text="snomedct:272460009",
                title="Anterior projection",
                meaning=SNOMEDCT["272460009"]))
        setattr(cls, "snomedct:272461008",
            PermissibleValue(
                text="snomedct:272461008",
                title="Right posterior projection",
                meaning=SNOMEDCT["272461008"]))
        setattr(cls, "snomedct:272462001",
            PermissibleValue(
                text="snomedct:272462001",
                title="Left posterior projection",
                meaning=SNOMEDCT["272462001"]))
        setattr(cls, "snomedct:272464000",
            PermissibleValue(
                text="snomedct:272464000",
                title="Perorbital projection",
                meaning=SNOMEDCT["272464000"]))
        setattr(cls, "snomedct:272465004",
            PermissibleValue(
                text="snomedct:272465004",
                title="Temporomandibular joint projection",
                meaning=SNOMEDCT["272465004"]))
        setattr(cls, "snomedct:272466003",
            PermissibleValue(
                text="snomedct:272466003",
                title="Optic foramen projection",
                meaning=SNOMEDCT["272466003"]))
        setattr(cls, "snomedct:272467007",
            PermissibleValue(
                text="snomedct:272467007",
                title="Lateral facial skeleton projection",
                meaning=SNOMEDCT["272467007"]))
        setattr(cls, "snomedct:272468002",
            PermissibleValue(
                text="snomedct:272468002",
                title="Ear projection",
                meaning=SNOMEDCT["272468002"]))
        setattr(cls, "snomedct:272469005",
            PermissibleValue(
                text="snomedct:272469005",
                title="Mid face projection",
                meaning=SNOMEDCT["272469005"]))
        setattr(cls, "snomedct:272470006",
            PermissibleValue(
                text="snomedct:272470006",
                title="Cervical spine projection",
                meaning=SNOMEDCT["272470006"]))
        setattr(cls, "snomedct:272472003",
            PermissibleValue(
                text="snomedct:272472003",
                title="Macro projection",
                meaning=SNOMEDCT["272472003"]))
        setattr(cls, "snomedct:272473008",
            PermissibleValue(
                text="snomedct:272473008",
                title="Outlet projection",
                meaning=SNOMEDCT["272473008"]))
        setattr(cls, "snomedct:272474002",
            PermissibleValue(
                text="snomedct:272474002",
                title="Swimmer's projection",
                meaning=SNOMEDCT["272474002"]))
        setattr(cls, "snomedct:272475001",
            PermissibleValue(
                text="snomedct:272475001",
                title="Tibial tuberosity projection",
                meaning=SNOMEDCT["272475001"]))
        setattr(cls, "snomedct:272476000",
            PermissibleValue(
                text="snomedct:272476000",
                title="Transthoracic projection",
                meaning=SNOMEDCT["272476000"]))
        setattr(cls, "snomedct:272478004",
            PermissibleValue(
                text="snomedct:272478004",
                title="Transcranial projection",
                meaning=SNOMEDCT["272478004"]))
        setattr(cls, "snomedct:272479007",
            PermissibleValue(
                text="snomedct:272479007",
                title="Posteroanterior projection",
                meaning=SNOMEDCT["272479007"]))
        setattr(cls, "snomedct:272480005",
            PermissibleValue(
                text="snomedct:272480005",
                title="Horizontal projection",
                meaning=SNOMEDCT["272480005"]))
        setattr(cls, "snomedct:272481009",
            PermissibleValue(
                text="snomedct:272481009",
                title="Erect projection",
                meaning=SNOMEDCT["272481009"]))
        setattr(cls, "snomedct:272482002",
            PermissibleValue(
                text="snomedct:272482002",
                title="Adduction projection",
                meaning=SNOMEDCT["272482002"]))
        setattr(cls, "snomedct:272483007",
            PermissibleValue(
                text="snomedct:272483007",
                title="True projection",
                meaning=SNOMEDCT["272483007"]))
        setattr(cls, "snomedct:272484001",
            PermissibleValue(
                text="snomedct:272484001",
                title="Contralateral projection",
                meaning=SNOMEDCT["272484001"]))
        setattr(cls, "snomedct:272485000",
            PermissibleValue(
                text="snomedct:272485000",
                title="Clockface position",
                meaning=SNOMEDCT["272485000"]))
        setattr(cls, "snomedct:272486004",
            PermissibleValue(
                text="snomedct:272486004",
                title="Trans-direction",
                meaning=SNOMEDCT["272486004"]))
        setattr(cls, "snomedct:272487008",
            PermissibleValue(
                text="snomedct:272487008",
                title="Into-structure",
                meaning=SNOMEDCT["272487008"]))
        setattr(cls, "snomedct:272488003",
            PermissibleValue(
                text="snomedct:272488003",
                title="From-structure",
                meaning=SNOMEDCT["272488003"]))
        setattr(cls, "snomedct:272489006",
            PermissibleValue(
                text="snomedct:272489006",
                title="Via values",
                meaning=SNOMEDCT["272489006"]))
        setattr(cls, "snomedct:272496008",
            PermissibleValue(
                text="snomedct:272496008",
                title="Via incision",
                meaning=SNOMEDCT["272496008"]))
        setattr(cls, "snomedct:276749003",
            PermissibleValue(
                text="snomedct:276749003",
                title="Epi-location",
                meaning=SNOMEDCT["276749003"]))
        setattr(cls, "snomedct:276825009",
            PermissibleValue(
                text="snomedct:276825009",
                title="Overlapping sites",
                meaning=SNOMEDCT["276825009"]))
        setattr(cls, "snomedct:276979001",
            PermissibleValue(
                text="snomedct:276979001",
                title="Aortoiliac",
                meaning=SNOMEDCT["276979001"]))
        setattr(cls, "snomedct:277292000",
            PermissibleValue(
                text="snomedct:277292000",
                title="Endo-location",
                meaning=SNOMEDCT["277292000"]))
        setattr(cls, "snomedct:277407002",
            PermissibleValue(
                text="snomedct:277407002",
                title="Deep locations",
                meaning=SNOMEDCT["277407002"]))
        setattr(cls, "snomedct:277409004",
            PermissibleValue(
                text="snomedct:277409004",
                title="Superficial locations",
                meaning=SNOMEDCT["277409004"]))
        setattr(cls, "snomedct:277410009",
            PermissibleValue(
                text="snomedct:277410009",
                title="Anterior locations",
                meaning=SNOMEDCT["277410009"]))
        setattr(cls, "snomedct:277411008",
            PermissibleValue(
                text="snomedct:277411008",
                title="Posterior locations",
                meaning=SNOMEDCT["277411008"]))
        setattr(cls, "snomedct:277412001",
            PermissibleValue(
                text="snomedct:277412001",
                title="Proximal locations",
                meaning=SNOMEDCT["277412001"]))
        setattr(cls, "snomedct:277413006",
            PermissibleValue(
                text="snomedct:277413006",
                title="Distal locations",
                meaning=SNOMEDCT["277413006"]))
        setattr(cls, "snomedct:277414000",
            PermissibleValue(
                text="snomedct:277414000",
                title="Between locations",
                meaning=SNOMEDCT["277414000"]))
        setattr(cls, "snomedct:277415004",
            PermissibleValue(
                text="snomedct:277415004",
                title="Above locations",
                meaning=SNOMEDCT["277415004"]))
        setattr(cls, "snomedct:277593009",
            PermissibleValue(
                text="snomedct:277593009",
                title="Right posterior",
                meaning=SNOMEDCT["277593009"]))
        setattr(cls, "snomedct:277594003",
            PermissibleValue(
                text="snomedct:277594003",
                title="Left posterior",
                meaning=SNOMEDCT["277594003"]))
        setattr(cls, "snomedct:277681008",
            PermissibleValue(
                text="snomedct:277681008",
                title="Intrastomal",
                meaning=SNOMEDCT["277681008"]))
        setattr(cls, "snomedct:277685004",
            PermissibleValue(
                text="snomedct:277685004",
                title="Tubo-ovarian",
                meaning=SNOMEDCT["277685004"]))
        setattr(cls, "snomedct:277686003",
            PermissibleValue(
                text="snomedct:277686003",
                title="Peritubular",
                meaning=SNOMEDCT["277686003"]))
        setattr(cls, "snomedct:277806003",
            PermissibleValue(
                text="snomedct:277806003",
                title="Sidedness",
                meaning=SNOMEDCT["277806003"]))
        setattr(cls, "snomedct:278227002",
            PermissibleValue(
                text="snomedct:278227002",
                title="Limited structures",
                meaning=SNOMEDCT["278227002"]))
        setattr(cls, "snomedct:278255003",
            PermissibleValue(
                text="snomedct:278255003",
                title="Posterior projection",
                meaning=SNOMEDCT["278255003"]))
        setattr(cls, "snomedct:278267001",
            PermissibleValue(
                text="snomedct:278267001",
                title="Abduction projection",
                meaning=SNOMEDCT["278267001"]))
        setattr(cls, "snomedct:278318001",
            PermissibleValue(
                text="snomedct:278318001",
                title="Transorbital projection",
                meaning=SNOMEDCT["278318001"]))
        setattr(cls, "snomedct:278701003",
            PermissibleValue(
                text="snomedct:278701003",
                title="Periumbilical",
                meaning=SNOMEDCT["278701003"]))
        setattr(cls, "snomedct:278702005",
            PermissibleValue(
                text="snomedct:278702005",
                title="Transumbilical",
                meaning=SNOMEDCT["278702005"]))
        setattr(cls, "snomedct:285418008",
            PermissibleValue(
                text="snomedct:285418008",
                title="Subcuticular",
                meaning=SNOMEDCT["285418008"]))
        setattr(cls, "snomedct:298107004",
            PermissibleValue(
                text="snomedct:298107004",
                title="Orthotopic",
                meaning=SNOMEDCT["298107004"]))
        setattr(cls, "snomedct:298108009",
            PermissibleValue(
                text="snomedct:298108009",
                title="Heterotopic",
                meaning=SNOMEDCT["298108009"]))
        setattr(cls, "snomedct:298109001",
            PermissibleValue(
                text="snomedct:298109001",
                title="Ectopic",
                meaning=SNOMEDCT["298109001"]))
        setattr(cls, "snomedct:303218009",
            PermissibleValue(
                text="snomedct:303218009",
                title="Subfascial",
                meaning=SNOMEDCT["303218009"]))
        setattr(cls, "snomedct:303231004",
            PermissibleValue(
                text="snomedct:303231004",
                title="Intracranial",
                meaning=SNOMEDCT["303231004"]))
        setattr(cls, "snomedct:303232006",
            PermissibleValue(
                text="snomedct:303232006",
                title="Extracranial",
                meaning=SNOMEDCT["303232006"]))
        setattr(cls, "snomedct:303483009",
            PermissibleValue(
                text="snomedct:303483009",
                title="Subcranial",
                meaning=SNOMEDCT["303483009"]))
        setattr(cls, "snomedct:304047000",
            PermissibleValue(
                text="snomedct:304047000",
                title="Transannular",
                meaning=SNOMEDCT["304047000"]))
        setattr(cls, "snomedct:304059001",
            PermissibleValue(
                text="snomedct:304059001",
                title="Endocardial",
                meaning=SNOMEDCT["304059001"]))
        setattr(cls, "snomedct:306766009",
            PermissibleValue(
                text="snomedct:306766009",
                title="Low - site descriptor",
                meaning=SNOMEDCT["306766009"]))
        setattr(cls, "snomedct:306767000",
            PermissibleValue(
                text="snomedct:306767000",
                title="High - site descriptor",
                meaning=SNOMEDCT["306767000"]))
        setattr(cls, "snomedct:312206004",
            PermissibleValue(
                text="snomedct:312206004",
                title="Periapical",
                meaning=SNOMEDCT["312206004"]))
        setattr(cls, "snomedct:3583002",
            PermissibleValue(
                text="snomedct:3583002",
                title="Caudal",
                meaning=SNOMEDCT["3583002"]))
        setattr(cls, "snomedct:373863008",
            PermissibleValue(
                text="snomedct:373863008",
                title="Intracavitary",
                meaning=SNOMEDCT["373863008"]))
        setattr(cls, "snomedct:397406000",
            PermissibleValue(
                text="snomedct:397406000",
                title="Collateral branch of vessel",
                meaning=SNOMEDCT["397406000"]))
        setattr(cls, "snomedct:397421006",
            PermissibleValue(
                text="snomedct:397421006",
                title="Vessel origin",
                meaning=SNOMEDCT["397421006"]))
        setattr(cls, "snomedct:398236008",
            PermissibleValue(
                text="snomedct:398236008",
                title="Intrauterine",
                meaning=SNOMEDCT["398236008"]))
        setattr(cls, "snomedct:398994001",
            PermissibleValue(
                text="snomedct:398994001",
                title="Five chamber view",
                meaning=SNOMEDCT["398994001"]))
        setattr(cls, "snomedct:398996004",
            PermissibleValue(
                text="snomedct:398996004",
                title="Leonard-George projection",
                meaning=SNOMEDCT["398996004"]))
        setattr(cls, "snomedct:398998003",
            PermissibleValue(
                text="snomedct:398998003",
                title="Right ventricular inflow tract view",
                meaning=SNOMEDCT["398998003"]))
        setattr(cls, "snomedct:399000008",
            PermissibleValue(
                text="snomedct:399000008",
                title="Mayer projection",
                meaning=SNOMEDCT["399000008"]))
        setattr(cls, "snomedct:399001007",
            PermissibleValue(
                text="snomedct:399001007",
                title="Posterior emissive projection",
                meaning=SNOMEDCT["399001007"]))
        setattr(cls, "snomedct:399002000",
            PermissibleValue(
                text="snomedct:399002000",
                title="Nolke projection",
                meaning=SNOMEDCT["399002000"]))
        setattr(cls, "snomedct:399003005",
            PermissibleValue(
                text="snomedct:399003005",
                title="Hughston projection",
                meaning=SNOMEDCT["399003005"]))
        setattr(cls, "snomedct:399004004",
            PermissibleValue(
                text="snomedct:399004004",
                title="Oblique axial projection",
                meaning=SNOMEDCT["399004004"]))
        setattr(cls, "snomedct:399005003",
            PermissibleValue(
                text="snomedct:399005003",
                title="Miller projection",
                meaning=SNOMEDCT["399005003"]))
        setattr(cls, "snomedct:399006002",
            PermissibleValue(
                text="snomedct:399006002",
                title="Left posterior oblique projection",
                meaning=SNOMEDCT["399006002"]))
        setattr(cls, "snomedct:399011000",
            PermissibleValue(
                text="snomedct:399011000",
                title="Axillary tail mammography view",
                meaning=SNOMEDCT["399011000"]))
        setattr(cls, "snomedct:399012007",
            PermissibleValue(
                text="snomedct:399012007",
                title="Medial-lateral emissive projection",
                meaning=SNOMEDCT["399012007"]))
        setattr(cls, "snomedct:399013002",
            PermissibleValue(
                text="snomedct:399013002",
                title="Chassard-Lapin projection",
                meaning=SNOMEDCT["399013002"]))
        setattr(cls, "snomedct:399022001",
            PermissibleValue(
                text="snomedct:399022001",
                title="Pirie projection",
                meaning=SNOMEDCT["399022001"]))
        setattr(cls, "snomedct:399024000",
            PermissibleValue(
                text="snomedct:399024000",
                title="May projection",
                meaning=SNOMEDCT["399024000"]))
        setattr(cls, "snomedct:399025004",
            PermissibleValue(
                text="snomedct:399025004",
                title="Ischerwood projection",
                meaning=SNOMEDCT["399025004"]))
        setattr(cls, "snomedct:399026003",
            PermissibleValue(
                text="snomedct:399026003",
                title="Zanelli projection",
                meaning=SNOMEDCT["399026003"]))
        setattr(cls, "snomedct:399028002",
            PermissibleValue(
                text="snomedct:399028002",
                title="Clements projection",
                meaning=SNOMEDCT["399028002"]))
        setattr(cls, "snomedct:399033003",
            PermissibleValue(
                text="snomedct:399033003",
                title="Frontal projection",
                meaning=SNOMEDCT["399033003"]))
        setattr(cls, "snomedct:399036006",
            PermissibleValue(
                text="snomedct:399036006",
                title="Parasternal short axis view at the mitral valve level",
                meaning=SNOMEDCT["399036006"]))
        setattr(cls, "snomedct:399037002",
            PermissibleValue(
                text="snomedct:399037002",
                title="Lewis projection",
                meaning=SNOMEDCT["399037002"]))
        setattr(cls, "snomedct:399038007",
            PermissibleValue(
                text="snomedct:399038007",
                title="Right posterior oblique projection",
                meaning=SNOMEDCT["399038007"]))
        setattr(cls, "snomedct:399043000",
            PermissibleValue(
                text="snomedct:399043000",
                title="Cardiac imaging views",
                meaning=SNOMEDCT["399043000"]))
        setattr(cls, "snomedct:399059000",
            PermissibleValue(
                text="snomedct:399059000",
                title="Postero-anterior oblique projection",
                meaning=SNOMEDCT["399059000"]))
        setattr(cls, "snomedct:399061009",
            PermissibleValue(
                text="snomedct:399061009",
                title="Axial projection",
                meaning=SNOMEDCT["399061009"]))
        setattr(cls, "snomedct:399065000",
            PermissibleValue(
                text="snomedct:399065000",
                title="Causton projection",
                meaning=SNOMEDCT["399065000"]))
        setattr(cls, "snomedct:399067008",
            PermissibleValue(
                text="snomedct:399067008",
                title="Lateral projection",
                meaning=SNOMEDCT["399067008"]))
        setattr(cls, "snomedct:399071006",
            PermissibleValue(
                text="snomedct:399071006",
                title="Plantodorsal projection",
                meaning=SNOMEDCT["399071006"]))
        setattr(cls, "snomedct:399073009",
            PermissibleValue(
                text="snomedct:399073009",
                title="Fuchs projection",
                meaning=SNOMEDCT["399073009"]))
        setattr(cls, "snomedct:399074003",
            PermissibleValue(
                text="snomedct:399074003",
                title="Left anterior oblique emissive projection",
                meaning=SNOMEDCT["399074003"]))
        setattr(cls, "snomedct:399075002",
            PermissibleValue(
                text="snomedct:399075002",
                title="Right posterior oblique emissive projection",
                meaning=SNOMEDCT["399075002"]))
        setattr(cls, "snomedct:399080006",
            PermissibleValue(
                text="snomedct:399080006",
                title="Kuchendorf projection",
                meaning=SNOMEDCT["399080006"]))
        setattr(cls, "snomedct:399082003",
            PermissibleValue(
                text="snomedct:399082003",
                title="Gaynor-Hart projection",
                meaning=SNOMEDCT["399082003"]))
        setattr(cls, "snomedct:399083008",
            PermissibleValue(
                text="snomedct:399083008",
                title="Hsieh projection",
                meaning=SNOMEDCT["399083008"]))
        setattr(cls, "snomedct:399089007",
            PermissibleValue(
                text="snomedct:399089007",
                title="Oblique axial emissive projection",
                meaning=SNOMEDCT["399089007"]))
        setattr(cls, "snomedct:399098005",
            PermissibleValue(
                text="snomedct:399098005",
                title="Staunig projection",
                meaning=SNOMEDCT["399098005"]))
        setattr(cls, "snomedct:399099002",
            PermissibleValue(
                text="snomedct:399099002",
                title="Latero-medial oblique projection",
                meaning=SNOMEDCT["399099002"]))
        setattr(cls, "snomedct:399101009",
            PermissibleValue(
                text="snomedct:399101009",
                title="Cranio-caudal projection exaggerated medially",
                meaning=SNOMEDCT["399101009"]))
        setattr(cls, "snomedct:399103007",
            PermissibleValue(
                text="snomedct:399103007",
                title="Friedman projection",
                meaning=SNOMEDCT["399103007"]))
        setattr(cls, "snomedct:399106004",
            PermissibleValue(
                text="snomedct:399106004",
                title="Suprasternal long axis view",
                meaning=SNOMEDCT["399106004"]))
        setattr(cls, "snomedct:399108003",
            PermissibleValue(
                text="snomedct:399108003",
                title="Right anterior oblique emissive projection",
                meaning=SNOMEDCT["399108003"]))
        setattr(cls, "snomedct:399110001",
            PermissibleValue(
                text="snomedct:399110001",
                title="Tangential projection",
                meaning=SNOMEDCT["399110001"]))
        setattr(cls, "snomedct:399113004",
            PermissibleValue(
                text="snomedct:399113004",
                title="Eponymous projection",
                meaning=SNOMEDCT["399113004"]))
        setattr(cls, "snomedct:399118008",
            PermissibleValue(
                text="snomedct:399118008",
                title="Left lateral emissive projection",
                meaning=SNOMEDCT["399118008"]))
        setattr(cls, "snomedct:399125001",
            PermissibleValue(
                text="snomedct:399125001",
                title="Twining projection",
                meaning=SNOMEDCT["399125001"]))
        setattr(cls, "snomedct:399127009",
            PermissibleValue(
                text="snomedct:399127009",
                title="Teufel projection",
                meaning=SNOMEDCT["399127009"]))
        setattr(cls, "snomedct:399129007",
            PermissibleValue(
                text="snomedct:399129007",
                title="Holly projection",
                meaning=SNOMEDCT["399129007"]))
        setattr(cls, "snomedct:399130002",
            PermissibleValue(
                text="snomedct:399130002",
                title="West Point projection",
                meaning=SNOMEDCT["399130002"]))
        setattr(cls, "snomedct:399132005",
            PermissibleValue(
                text="snomedct:399132005",
                title="Frontal-oblique axial projection",
                meaning=SNOMEDCT["399132005"]))
        setattr(cls, "snomedct:399135007",
            PermissibleValue(
                text="snomedct:399135007",
                title="Left anterior oblique projection",
                meaning=SNOMEDCT["399135007"]))
        setattr(cls, "snomedct:399136008",
            PermissibleValue(
                text="snomedct:399136008",
                title="Left posterior oblique emissive projection",
                meaning=SNOMEDCT["399136008"]))
        setattr(cls, "snomedct:399138009",
            PermissibleValue(
                text="snomedct:399138009",
                title="Penner projection",
                meaning=SNOMEDCT["399138009"]))
        setattr(cls, "snomedct:399139001",
            PermissibleValue(
                text="snomedct:399139001",
                title="Parasternal long axis view",
                meaning=SNOMEDCT["399139001"]))
        setattr(cls, "snomedct:399142007",
            PermissibleValue(
                text="snomedct:399142007",
                title="Albers-Schönberg projection",
                meaning=SNOMEDCT["399142007"]))
        setattr(cls, "snomedct:399145009",
            PermissibleValue(
                text="snomedct:399145009",
                title="Suprasternal short axis view",
                meaning=SNOMEDCT["399145009"]))
        setattr(cls, "snomedct:399146005",
            PermissibleValue(
                text="snomedct:399146005",
                title="Grashey projection",
                meaning=SNOMEDCT["399146005"]))
        setattr(cls, "snomedct:399148006",
            PermissibleValue(
                text="snomedct:399148006",
                title="Chamberlain projection",
                meaning=SNOMEDCT["399148006"]))
        setattr(cls, "snomedct:399152006",
            PermissibleValue(
                text="snomedct:399152006",
                title="Kandel projection",
                meaning=SNOMEDCT["399152006"]))
        setattr(cls, "snomedct:399156009",
            PermissibleValue(
                text="snomedct:399156009",
                title="Laquerriere-Pierquin projection",
                meaning=SNOMEDCT["399156009"]))
        setattr(cls, "snomedct:399157000",
            PermissibleValue(
                text="snomedct:399157000",
                title="Norgaard's projection",
                meaning=SNOMEDCT["399157000"]))
        setattr(cls, "snomedct:399159002",
            PermissibleValue(
                text="snomedct:399159002",
                title="Latero-medial oblique emissive projection",
                meaning=SNOMEDCT["399159002"]))
        setattr(cls, "snomedct:399160007",
            PermissibleValue(
                text="snomedct:399160007",
                title="Frontal oblique projection",
                meaning=SNOMEDCT["399160007"]))
        setattr(cls, "snomedct:399161006",
            PermissibleValue(
                text="snomedct:399161006",
                title="Cleavage mammography view",
                meaning=SNOMEDCT["399161006"]))
        setattr(cls, "snomedct:399162004",
            PermissibleValue(
                text="snomedct:399162004",
                title="Cranio-caudal projection",
                meaning=SNOMEDCT["399162004"]))
        setattr(cls, "snomedct:399163009",
            PermissibleValue(
                text="snomedct:399163009",
                title="Magnified projection",
                meaning=SNOMEDCT["399163009"]))
        setattr(cls, "snomedct:399168000",
            PermissibleValue(
                text="snomedct:399168000",
                title="Hough projection",
                meaning=SNOMEDCT["399168000"]))
        setattr(cls, "snomedct:399169008",
            PermissibleValue(
                text="snomedct:399169008",
                title="Lauenstein projection",
                meaning=SNOMEDCT["399169008"]))
        setattr(cls, "snomedct:399171008",
            PermissibleValue(
                text="snomedct:399171008",
                title="Ottonello projection",
                meaning=SNOMEDCT["399171008"]))
        setattr(cls, "snomedct:399173006",
            PermissibleValue(
                text="snomedct:399173006",
                title="Left lateral projection",
                meaning=SNOMEDCT["399173006"]))
        setattr(cls, "snomedct:399179005",
            PermissibleValue(
                text="snomedct:399179005",
                title="Lawrence projection",
                meaning=SNOMEDCT["399179005"]))
        setattr(cls, "snomedct:399181007",
            PermissibleValue(
                text="snomedct:399181007",
                title="Pawlow projection",
                meaning=SNOMEDCT["399181007"]))
        setattr(cls, "snomedct:399182000",
            PermissibleValue(
                text="snomedct:399182000",
                title="Oblique projection",
                meaning=SNOMEDCT["399182000"]))
        setattr(cls, "snomedct:399184004",
            PermissibleValue(
                text="snomedct:399184004",
                title="Left oblique projection",
                meaning=SNOMEDCT["399184004"]))
        setattr(cls, "snomedct:399188001",
            PermissibleValue(
                text="snomedct:399188001",
                title="Superolateral to inferomedial oblique projection",
                meaning=SNOMEDCT["399188001"]))
        setattr(cls, "snomedct:399192008",
            PermissibleValue(
                text="snomedct:399192008",
                title="Cranio-caudal projection exaggerated laterally",
                meaning=SNOMEDCT["399192008"]))
        setattr(cls, "snomedct:399195005",
            PermissibleValue(
                text="snomedct:399195005",
                title="Right ventricular outflow tract view",
                meaning=SNOMEDCT["399195005"]))
        setattr(cls, "snomedct:399196006",
            PermissibleValue(
                text="snomedct:399196006",
                title="Caudo-cranial projection",
                meaning=SNOMEDCT["399196006"]))
        setattr(cls, "snomedct:399198007",
            PermissibleValue(
                text="snomedct:399198007",
                title="Right lateral projection",
                meaning=SNOMEDCT["399198007"]))
        setattr(cls, "snomedct:399199004",
            PermissibleValue(
                text="snomedct:399199004",
                title="Henschen projection",
                meaning=SNOMEDCT["399199004"]))
        setattr(cls, "snomedct:399200001",
            PermissibleValue(
                text="snomedct:399200001",
                title="Subcostal short axis view",
                meaning=SNOMEDCT["399200001"]))
        setattr(cls, "snomedct:399201002",
            PermissibleValue(
                text="snomedct:399201002",
                title="Judd projection",
                meaning=SNOMEDCT["399201002"]))
        setattr(cls, "snomedct:399206007",
            PermissibleValue(
                text="snomedct:399206007",
                title="Law projection",
                meaning=SNOMEDCT["399206007"]))
        setattr(cls, "snomedct:399212002",
            PermissibleValue(
                text="snomedct:399212002",
                title="Camp-Coventry projection",
                meaning=SNOMEDCT["399212002"]))
        setattr(cls, "snomedct:399214001",
            PermissibleValue(
                text="snomedct:399214001",
                title="Apical four chamber view",
                meaning=SNOMEDCT["399214001"]))
        setattr(cls, "snomedct:399215000",
            PermissibleValue(
                text="snomedct:399215000",
                title="Wigby-Taylor projection",
                meaning=SNOMEDCT["399215000"]))
        setattr(cls, "snomedct:399218003",
            PermissibleValue(
                text="snomedct:399218003",
                title="Arcelin projection",
                meaning=SNOMEDCT["399218003"]))
        setattr(cls, "snomedct:399225005",
            PermissibleValue(
                text="snomedct:399225005",
                title="Oblique caudo-cranial projection",
                meaning=SNOMEDCT["399225005"]))
        setattr(cls, "snomedct:399227002",
            PermissibleValue(
                text="snomedct:399227002",
                title="Kemp Harper projection",
                meaning=SNOMEDCT["399227002"]))
        setattr(cls, "snomedct:399232001",
            PermissibleValue(
                text="snomedct:399232001",
                title="Apical two chamber view",
                meaning=SNOMEDCT["399232001"]))
        setattr(cls, "snomedct:399234000",
            PermissibleValue(
                text="snomedct:399234000",
                title="Rhese projection",
                meaning=SNOMEDCT["399234000"]))
        setattr(cls, "snomedct:399236003",
            PermissibleValue(
                text="snomedct:399236003",
                title="Right oblique projection",
                meaning=SNOMEDCT["399236003"]))
        setattr(cls, "snomedct:399237007",
            PermissibleValue(
                text="snomedct:399237007",
                title="Alexander projection",
                meaning=SNOMEDCT["399237007"]))
        setattr(cls, "snomedct:399239005",
            PermissibleValue(
                text="snomedct:399239005",
                title="Parasternal short axis view at the aortic valve level",
                meaning=SNOMEDCT["399239005"]))
        setattr(cls, "snomedct:399241006",
            PermissibleValue(
                text="snomedct:399241006",
                title="Titterington projection",
                meaning=SNOMEDCT["399241006"]))
        setattr(cls, "snomedct:399242004",
            PermissibleValue(
                text="snomedct:399242004",
                title="Acanthioparietal projection",
                meaning=SNOMEDCT["399242004"]))
        setattr(cls, "snomedct:399243009",
            PermissibleValue(
                text="snomedct:399243009",
                title="Settegast projection",
                meaning=SNOMEDCT["399243009"]))
        setattr(cls, "snomedct:399245002",
            PermissibleValue(
                text="snomedct:399245002",
                title="Cleaves projection",
                meaning=SNOMEDCT["399245002"]))
        setattr(cls, "snomedct:399246001",
            PermissibleValue(
                text="snomedct:399246001",
                title="Blackett-Healy projection",
                meaning=SNOMEDCT["399246001"]))
        setattr(cls, "snomedct:399247005",
            PermissibleValue(
                text="snomedct:399247005",
                title="Tarrant projection",
                meaning=SNOMEDCT["399247005"]))
        setattr(cls, "snomedct:399251007",
            PermissibleValue(
                text="snomedct:399251007",
                title="Lorenz projection",
                meaning=SNOMEDCT["399251007"]))
        setattr(cls, "snomedct:399255003",
            PermissibleValue(
                text="snomedct:399255003",
                title="Submentovertical projection",
                meaning=SNOMEDCT["399255003"]))
        setattr(cls, "snomedct:399260004",
            PermissibleValue(
                text="snomedct:399260004",
                title="Mediolateral projection",
                meaning=SNOMEDCT["399260004"]))
        setattr(cls, "snomedct:399263002",
            PermissibleValue(
                text="snomedct:399263002",
                title="Beclere projection",
                meaning=SNOMEDCT["399263002"]))
        setattr(cls, "snomedct:399265009",
            PermissibleValue(
                text="snomedct:399265009",
                title="Exaggerated cranio-caudal projection",
                meaning=SNOMEDCT["399265009"]))
        setattr(cls, "snomedct:399268006",
            PermissibleValue(
                text="snomedct:399268006",
                title="Medio-lateral oblique emissive projection",
                meaning=SNOMEDCT["399268006"]))
        setattr(cls, "snomedct:399270002",
            PermissibleValue(
                text="snomedct:399270002",
                title="Towne's projection",
                meaning=SNOMEDCT["399270002"]))
        setattr(cls, "snomedct:399271003",
            PermissibleValue(
                text="snomedct:399271003",
                title="Parasternal short axis view at the papillary muscle level",
                meaning=SNOMEDCT["399271003"]))
        setattr(cls, "snomedct:399272005",
            PermissibleValue(
                text="snomedct:399272005",
                title="Parietoacanthial projection",
                meaning=SNOMEDCT["399272005"]))
        setattr(cls, "snomedct:399273000",
            PermissibleValue(
                text="snomedct:399273000",
                title="Sagittal-oblique axial emissive projection",
                meaning=SNOMEDCT["399273000"]))
        setattr(cls, "snomedct:399277004",
            PermissibleValue(
                text="snomedct:399277004",
                title="Hickey projection",
                meaning=SNOMEDCT["399277004"]))
        setattr(cls, "snomedct:399278009",
            PermissibleValue(
                text="snomedct:399278009",
                title="Cahoon projection",
                meaning=SNOMEDCT["399278009"]))
        setattr(cls, "snomedct:399280003",
            PermissibleValue(
                text="snomedct:399280003",
                title="Kasabach projection",
                meaning=SNOMEDCT["399280003"]))
        setattr(cls, "snomedct:399281004",
            PermissibleValue(
                text="snomedct:399281004",
                title="Fleischner projection",
                meaning=SNOMEDCT["399281004"]))
        setattr(cls, "snomedct:399284007",
            PermissibleValue(
                text="snomedct:399284007",
                title="Merchant projection",
                meaning=SNOMEDCT["399284007"]))
        setattr(cls, "snomedct:399285008",
            PermissibleValue(
                text="snomedct:399285008",
                title="Holmblad projection",
                meaning=SNOMEDCT["399285008"]))
        setattr(cls, "snomedct:399288005",
            PermissibleValue(
                text="snomedct:399288005",
                title="Oblique cranio-caudal projection",
                meaning=SNOMEDCT["399288005"]))
        setattr(cls, "snomedct:399290006",
            PermissibleValue(
                text="snomedct:399290006",
                title="Schüller projection",
                meaning=SNOMEDCT["399290006"]))
        setattr(cls, "snomedct:399292003",
            PermissibleValue(
                text="snomedct:399292003",
                title="Stecher projection",
                meaning=SNOMEDCT["399292003"]))
        setattr(cls, "snomedct:399296000",
            PermissibleValue(
                text="snomedct:399296000",
                title="Taylor projection",
                meaning=SNOMEDCT["399296000"]))
        setattr(cls, "snomedct:399297009",
            PermissibleValue(
                text="snomedct:399297009",
                title="Right lateral emissive projection",
                meaning=SNOMEDCT["399297009"]))
        setattr(cls, "snomedct:399300004",
            PermissibleValue(
                text="snomedct:399300004",
                title="Lateral-medial emissive projection",
                meaning=SNOMEDCT["399300004"]))
        setattr(cls, "snomedct:399303002",
            PermissibleValue(
                text="snomedct:399303002",
                title="Dunlap projection",
                meaning=SNOMEDCT["399303002"]))
        setattr(cls, "snomedct:399306005",
            PermissibleValue(
                text="snomedct:399306005",
                title="Parasternal short axis view",
                meaning=SNOMEDCT["399306005"]))
        setattr(cls, "snomedct:399308006",
            PermissibleValue(
                text="snomedct:399308006",
                title="Lindblom projection",
                meaning=SNOMEDCT["399308006"]))
        setattr(cls, "snomedct:399310008",
            PermissibleValue(
                text="snomedct:399310008",
                title="Subcostal long axis view",
                meaning=SNOMEDCT["399310008"]))
        setattr(cls, "snomedct:399311007",
            PermissibleValue(
                text="snomedct:399311007",
                title="Grandy projection",
                meaning=SNOMEDCT["399311007"]))
        setattr(cls, "snomedct:399312000",
            PermissibleValue(
                text="snomedct:399312000",
                title="Antero-posterior oblique projection",
                meaning=SNOMEDCT["399312000"]))
        setattr(cls, "snomedct:399313005",
            PermissibleValue(
                text="snomedct:399313005",
                title="Swanson projection",
                meaning=SNOMEDCT["399313005"]))
        setattr(cls, "snomedct:399316002",
            PermissibleValue(
                text="snomedct:399316002",
                title="Parieto-orbital projection",
                meaning=SNOMEDCT["399316002"]))
        setattr(cls, "snomedct:399318001",
            PermissibleValue(
                text="snomedct:399318001",
                title="Kovacs projection",
                meaning=SNOMEDCT["399318001"]))
        setattr(cls, "snomedct:399320003",
            PermissibleValue(
                text="snomedct:399320003",
                title="Clements-Nakayama projection",
                meaning=SNOMEDCT["399320003"]))
        setattr(cls, "snomedct:399321004",
            PermissibleValue(
                text="snomedct:399321004",
                title="Anterior emissive projection",
                meaning=SNOMEDCT["399321004"]))
        setattr(cls, "snomedct:399325008",
            PermissibleValue(
                text="snomedct:399325008",
                title="Sagittal-oblique axial projection",
                meaning=SNOMEDCT["399325008"]))
        setattr(cls, "snomedct:399327000",
            PermissibleValue(
                text="snomedct:399327000",
                title="Low-Beer projection",
                meaning=SNOMEDCT["399327000"]))
        setattr(cls, "snomedct:399330007",
            PermissibleValue(
                text="snomedct:399330007",
                title="Valdini projection",
                meaning=SNOMEDCT["399330007"]))
        setattr(cls, "snomedct:399332004",
            PermissibleValue(
                text="snomedct:399332004",
                title="Kurzbauer projection",
                meaning=SNOMEDCT["399332004"]))
        setattr(cls, "snomedct:399335002",
            PermissibleValue(
                text="snomedct:399335002",
                title="Dorsoplantar projection",
                meaning=SNOMEDCT["399335002"]))
        setattr(cls, "snomedct:399339008",
            PermissibleValue(
                text="snomedct:399339008",
                title="Apical long axis",
                meaning=SNOMEDCT["399339008"]))
        setattr(cls, "snomedct:399341009",
            PermissibleValue(
                text="snomedct:399341009",
                title="Haas projection",
                meaning=SNOMEDCT["399341009"]))
        setattr(cls, "snomedct:399342002",
            PermissibleValue(
                text="snomedct:399342002",
                title="Lilienfeld projection",
                meaning=SNOMEDCT["399342002"]))
        setattr(cls, "snomedct:399344001",
            PermissibleValue(
                text="snomedct:399344001",
                title="Broden projection",
                meaning=SNOMEDCT["399344001"]))
        setattr(cls, "snomedct:399348003",
            PermissibleValue(
                text="snomedct:399348003",
                title="Antero-posterior projection",
                meaning=SNOMEDCT["399348003"]))
        setattr(cls, "snomedct:399349006",
            PermissibleValue(
                text="snomedct:399349006",
                title="Stenver's projection",
                meaning=SNOMEDCT["399349006"]))
        setattr(cls, "snomedct:399351005",
            PermissibleValue(
                text="snomedct:399351005",
                title="Orbito-parietal projection",
                meaning=SNOMEDCT["399351005"]))
        setattr(cls, "snomedct:399352003",
            PermissibleValue(
                text="snomedct:399352003",
                title="Lateral-medial projection",
                meaning=SNOMEDCT["399352003"]))
        setattr(cls, "snomedct:399355001",
            PermissibleValue(
                text="snomedct:399355001",
                title="Chausse projection",
                meaning=SNOMEDCT["399355001"]))
        setattr(cls, "snomedct:399356000",
            PermissibleValue(
                text="snomedct:399356000",
                title="Right anterior oblique projection",
                meaning=SNOMEDCT["399356000"]))
        setattr(cls, "snomedct:399358004",
            PermissibleValue(
                text="snomedct:399358004",
                title="Caldwell projection",
                meaning=SNOMEDCT["399358004"]))
        setattr(cls, "snomedct:399360002",
            PermissibleValue(
                text="snomedct:399360002",
                title="Verticosubmental projection",
                meaning=SNOMEDCT["399360002"]))
        setattr(cls, "snomedct:399361003",
            PermissibleValue(
                text="snomedct:399361003",
                title="Nuclear medicine projection",
                meaning=SNOMEDCT["399361003"]))
        setattr(cls, "snomedct:399362005",
            PermissibleValue(
                text="snomedct:399362005",
                title="Bertel projection",
                meaning=SNOMEDCT["399362005"]))
        setattr(cls, "snomedct:399365007",
            PermissibleValue(
                text="snomedct:399365007",
                title="Pearson projection",
                meaning=SNOMEDCT["399365007"]))
        setattr(cls, "snomedct:399368009",
            PermissibleValue(
                text="snomedct:399368009",
                title="Medio-lateral oblique projection",
                meaning=SNOMEDCT["399368009"]))
        setattr(cls, "snomedct:399370000",
            PermissibleValue(
                text="snomedct:399370000",
                title="Lysholm projection",
                meaning=SNOMEDCT["399370000"]))
        setattr(cls, "snomedct:399371001",
            PermissibleValue(
                text="snomedct:399371001",
                title="Parasternal short axis view at the level of the mitral chords",
                meaning=SNOMEDCT["399371001"]))
        setattr(cls, "snomedct:399372008",
            PermissibleValue(
                text="snomedct:399372008",
                title="Ferguson projection",
                meaning=SNOMEDCT["399372008"]))
        setattr(cls, "snomedct:399488007",
            PermissibleValue(
                text="snomedct:399488007",
                title="Midline (qualifier value)",
                description="Midline (qualifier value)",
                meaning=SNOMEDCT["399488007"]))
        setattr(cls, "snomedct:408723005",
            PermissibleValue(
                text="snomedct:408723005",
                title="Cranial LAO",
                meaning=SNOMEDCT["408723005"]))
        setattr(cls, "snomedct:408724004",
            PermissibleValue(
                text="snomedct:408724004",
                title="Caudal LAO",
                meaning=SNOMEDCT["408724004"]))
        setattr(cls, "snomedct:408725003",
            PermissibleValue(
                text="snomedct:408725003",
                title="Cranial RAO",
                meaning=SNOMEDCT["408725003"]))
        setattr(cls, "snomedct:408726002",
            PermissibleValue(
                text="snomedct:408726002",
                title="Caudal RAO",
                meaning=SNOMEDCT["408726002"]))
        setattr(cls, "snomedct:421610009",
            PermissibleValue(
                text="snomedct:421610009",
                title="Bottom",
                meaning=SNOMEDCT["421610009"]))
        setattr(cls, "snomedct:421812003",
            PermissibleValue(
                text="snomedct:421812003",
                title="Top",
                meaning=SNOMEDCT["421812003"]))
        setattr(cls, "snomedct:422534007",
            PermissibleValue(
                text="snomedct:422534007",
                title="Rafert-Long projection",
                meaning=SNOMEDCT["422534007"]))
        setattr(cls, "snomedct:422568001",
            PermissibleValue(
                text="snomedct:422568001",
                title="Moore projection",
                meaning=SNOMEDCT["422568001"]))
        setattr(cls, "snomedct:422670003",
            PermissibleValue(
                text="snomedct:422670003",
                title="Apple projection",
                meaning=SNOMEDCT["422670003"]))
        setattr(cls, "snomedct:422795009",
            PermissibleValue(
                text="snomedct:422795009",
                title="Neer projection",
                meaning=SNOMEDCT["422795009"]))
        setattr(cls, "snomedct:422861003",
            PermissibleValue(
                text="snomedct:422861003",
                title="Burman projection",
                meaning=SNOMEDCT["422861003"]))
        setattr(cls, "snomedct:422954003",
            PermissibleValue(
                text="snomedct:422954003",
                title="Stryker projection",
                meaning=SNOMEDCT["422954003"]))
        setattr(cls, "snomedct:422996004",
            PermissibleValue(
                text="snomedct:422996004",
                title="Wolf projection",
                meaning=SNOMEDCT["422996004"]))
        setattr(cls, "snomedct:423091003",
            PermissibleValue(
                text="snomedct:423091003",
                title="Colcher-Sussman projection",
                meaning=SNOMEDCT["423091003"]))
        setattr(cls, "snomedct:423720000",
            PermissibleValue(
                text="snomedct:423720000",
                title="Rafer projection",
                meaning=SNOMEDCT["423720000"]))
        setattr(cls, "snomedct:424086005",
            PermissibleValue(
                text="snomedct:424086005",
                title="Hirtz Modification projection",
                meaning=SNOMEDCT["424086005"]))
        setattr(cls, "snomedct:424655003",
            PermissibleValue(
                text="snomedct:424655003",
                title="Eraso Modification projection",
                meaning=SNOMEDCT["424655003"]))
        setattr(cls, "snomedct:424811006",
            PermissibleValue(
                text="snomedct:424811006",
                title="Danelius-Miller projection",
                meaning=SNOMEDCT["424811006"]))
        setattr(cls, "snomedct:424962005",
            PermissibleValue(
                text="snomedct:424962005",
                title="Fisk projection",
                meaning=SNOMEDCT["424962005"]))
        setattr(cls, "snomedct:425030002",
            PermissibleValue(
                text="snomedct:425030002",
                title="Kite projection",
                meaning=SNOMEDCT["425030002"]))
        setattr(cls, "snomedct:425035007",
            PermissibleValue(
                text="snomedct:425035007",
                title="Robert projection",
                meaning=SNOMEDCT["425035007"]))
        setattr(cls, "snomedct:425042007",
            PermissibleValue(
                text="snomedct:425042007",
                title="Rosenberg projection",
                meaning=SNOMEDCT["425042007"]))
        setattr(cls, "snomedct:425157002",
            PermissibleValue(
                text="snomedct:425157002",
                title="Folio projection",
                meaning=SNOMEDCT["425157002"]))
        setattr(cls, "snomedct:425188003",
            PermissibleValue(
                text="snomedct:425188003",
                title="Garth projection",
                meaning=SNOMEDCT["425188003"]))
        setattr(cls, "snomedct:441505008",
            PermissibleValue(
                text="snomedct:441505008",
                title="Dorsopalmar projection",
                meaning=SNOMEDCT["441505008"]))
        setattr(cls, "snomedct:441555000",
            PermissibleValue(
                text="snomedct:441555000",
                title="Inferomedial to superolateral oblique view",
                meaning=SNOMEDCT["441555000"]))
        setattr(cls, "snomedct:441672003",
            PermissibleValue(
                text="snomedct:441672003",
                title="Dorso-ventral projection",
                meaning=SNOMEDCT["441672003"]))
        setattr(cls, "snomedct:441753009",
            PermissibleValue(
                text="snomedct:441753009",
                title="Mammography view",
                meaning=SNOMEDCT["441753009"]))
        setattr(cls, "snomedct:442361004",
            PermissibleValue(
                text="snomedct:442361004",
                title="Stereoscopic view",
                meaning=SNOMEDCT["442361004"]))
        setattr(cls, "snomedct:442441009",
            PermissibleValue(
                text="snomedct:442441009",
                title="Ventro-dorsal projection",
                meaning=SNOMEDCT["442441009"]))
        setattr(cls, "snomedct:442580003",
            PermissibleValue(
                text="snomedct:442580003",
                title="Axillary tissue mammography view",
                meaning=SNOMEDCT["442580003"]))
        setattr(cls, "snomedct:442581004",
            PermissibleValue(
                text="snomedct:442581004",
                title="Nipple in profile mammography view",
                meaning=SNOMEDCT["442581004"]))
        setattr(cls, "snomedct:442593008",
            PermissibleValue(
                text="snomedct:442593008",
                title="Infra-mammary fold mammography view",
                meaning=SNOMEDCT["442593008"]))
        setattr(cls, "snomedct:442594002",
            PermissibleValue(
                text="snomedct:442594002",
                title="Right stereoscopic view",
                meaning=SNOMEDCT["442594002"]))
        setattr(cls, "snomedct:442640004",
            PermissibleValue(
                text="snomedct:442640004",
                title="Left stereoscopic view",
                meaning=SNOMEDCT["442640004"]))
        setattr(cls, "snomedct:442653001",
            PermissibleValue(
                text="snomedct:442653001",
                title="Stereoscopic view incremented from baseline",
                meaning=SNOMEDCT["442653001"]))
        setattr(cls, "snomedct:442667005",
            PermissibleValue(
                text="snomedct:442667005",
                title="Stereoscopic view decremented from baseline",
                meaning=SNOMEDCT["442667005"]))
        setattr(cls, "snomedct:443082005",
            PermissibleValue(
                text="snomedct:443082005",
                title="Parasternal long axis view of right ventricular inflow tract",
                meaning=SNOMEDCT["443082005"]))
        setattr(cls, "snomedct:443083000",
            PermissibleValue(
                text="snomedct:443083000",
                title="Parasternal long axis view of right ventricular outflow tract",
                meaning=SNOMEDCT["443083000"]))
        setattr(cls, "snomedct:443100003",
            PermissibleValue(
                text="snomedct:443100003",
                title="Subcostal view of cardiac outlets directed anteriorly",
                meaning=SNOMEDCT["443100003"]))
        setattr(cls, "snomedct:443160001",
            PermissibleValue(
                text="snomedct:443160001",
                title="Subcostal short axis view at papillary muscle level",
                meaning=SNOMEDCT["443160001"]))
        setattr(cls, "snomedct:443162009",
            PermissibleValue(
                text="snomedct:443162009",
                title="Suprasternal coronal view",
                meaning=SNOMEDCT["443162009"]))
        setattr(cls, "snomedct:443163004",
            PermissibleValue(
                text="snomedct:443163004",
                title="Suprasternal sagittal view",
                meaning=SNOMEDCT["443163004"]))
        setattr(cls, "snomedct:443293000",
            PermissibleValue(
                text="snomedct:443293000",
                title="Transgastric short axis view",
                meaning=SNOMEDCT["443293000"]))
        setattr(cls, "snomedct:443459002",
            PermissibleValue(
                text="snomedct:443459002",
                title="Intramedullary",
                meaning=SNOMEDCT["443459002"]))
        setattr(cls, "snomedct:443499004",
            PermissibleValue(
                text="snomedct:443499004",
                title="Subcostal short axis view at mitral valve level",
                meaning=SNOMEDCT["443499004"]))
        setattr(cls, "snomedct:443500008",
            PermissibleValue(
                text="snomedct:443500008",
                title="Subcostal short axis view at venous inflow level",
                meaning=SNOMEDCT["443500008"]))
        setattr(cls, "snomedct:443562002",
            PermissibleValue(
                text="snomedct:443562002",
                title="Suprasternal long axis view of aortic arch",
                meaning=SNOMEDCT["443562002"]))
        setattr(cls, "snomedct:443609003",
            PermissibleValue(
                text="snomedct:443609003",
                title="Subcostal short axis view at aortic valve level",
                meaning=SNOMEDCT["443609003"]))
        setattr(cls, "snomedct:443640005",
            PermissibleValue(
                text="snomedct:443640005",
                title="Subcostal oblique coronal view",
                meaning=SNOMEDCT["443640005"]))
        setattr(cls, "snomedct:443662005",
            PermissibleValue(
                text="snomedct:443662005",
                title="Transesophageal four chamber view (qualifier value)",
                meaning=SNOMEDCT["443662005"]))
        setattr(cls, "snomedct:443698002",
            PermissibleValue(
                text="snomedct:443698002",
                title="Transesophageal short axis view (qualifier value)",
                meaning=SNOMEDCT["443698002"]))
        setattr(cls, "snomedct:65424008",
            PermissibleValue(
                text="snomedct:65424008",
                title="Contiguous",
                meaning=SNOMEDCT["65424008"]))
        setattr(cls, "snomedct:66459002",
            PermissibleValue(
                text="snomedct:66459002",
                title="Unilateral",
                meaning=SNOMEDCT["66459002"]))
        setattr(cls, "snomedct:72906007",
            PermissibleValue(
                text="snomedct:72906007",
                title="Common",
                meaning=SNOMEDCT["72906007"]))
        setattr(cls, "snomedct:741000124103",
            PermissibleValue(
                text="snomedct:741000124103",
                title="Dorsoventral",
                meaning=SNOMEDCT["741000124103"]))
        setattr(cls, "snomedct:761000124104",
            PermissibleValue(
                text="snomedct:761000124104",
                title="Dorsolateral",
                meaning=SNOMEDCT["761000124104"]))
        setattr(cls, "snomedct:771000124106",
            PermissibleValue(
                text="snomedct:771000124106",
                title="Ventrolateral",
                meaning=SNOMEDCT["771000124106"]))
        setattr(cls, "snomedct:781000124109",
            PermissibleValue(
                text="snomedct:781000124109",
                title="Palmar",
                meaning=SNOMEDCT["781000124109"]))

class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """
    _defn = EnumDefinition(
        name="EnumLaterality",
        description="Laterality information for the site",
    )

class EnumEDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMFormats",
        description="Data formats from the EDAM ontology.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "edam:format_1915",
            PermissibleValue(
                text="edam:format_1915",
                title="Format",
                description="Format",
                meaning=EDAM["format_1915"]))
        setattr(cls, "edam:format_1196",
            PermissibleValue(
                text="edam:format_1196",
                title="SMILES",
                description="""Chemical structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation.""",
                meaning=EDAM["format_1196"]))
        setattr(cls, "edam:format_1197",
            PermissibleValue(
                text="edam:format_1197",
                title="InChI",
                description="""Chemical structure specified in IUPAC International Chemical Identifier (InChI) line notation.""",
                meaning=EDAM["format_1197"]))
        setattr(cls, "edam:format_1198",
            PermissibleValue(
                text="edam:format_1198",
                title="mf",
                description="""Chemical structure specified by Molecular Formula (MF), including a count of each element in a compound.
The general MF query format consists of a series of valid atomic symbols, with an optional number or range.""",
                meaning=EDAM["format_1198"]))
        setattr(cls, "edam:format_1199",
            PermissibleValue(
                text="edam:format_1199",
                title="InChIKey",
                description="""An InChIKey identifier is not human- nor machine-readable but is more suitable for web searches than an InChI chemical structure specification.
The InChIKey (hashed InChI) is a fixed length (25 character) condensed digital representation of an InChI chemical structure specification. It uniquely identifies a chemical compound.""",
                meaning=EDAM["format_1199"]))
        setattr(cls, "edam:format_1200",
            PermissibleValue(
                text="edam:format_1200",
                title="smarts",
                description="""SMILES ARbitrary Target Specification (SMARTS) format for chemical structure specification, which is a subset of the SMILES line notation.""",
                meaning=EDAM["format_1200"]))
        setattr(cls, "edam:format_1206",
            PermissibleValue(
                text="edam:format_1206",
                title="unambiguous pure",
                description="""Alphabet for a molecular sequence with possible unknown positions but without ambiguity or non-sequence characters.""",
                meaning=EDAM["format_1206"]))
        setattr(cls, "edam:format_1207",
            PermissibleValue(
                text="edam:format_1207",
                title="nucleotide",
                description="""Alphabet for a nucleotide sequence with possible ambiguity, unknown positions and non-sequence characters.
Non-sequence characters may be used for example for gaps.""",
                meaning=EDAM["format_1207"]))
        setattr(cls, "edam:format_1208",
            PermissibleValue(
                text="edam:format_1208",
                title="protein",
                description="""Alphabet for a protein sequence with possible ambiguity, unknown positions and non-sequence characters.
Non-sequence characters may be used for gaps and translation stop.""",
                meaning=EDAM["format_1208"]))
        setattr(cls, "edam:format_1209",
            PermissibleValue(
                text="edam:format_1209",
                title="consensus",
                description="Alphabet for the consensus of two or more molecular sequences.",
                meaning=EDAM["format_1209"]))
        setattr(cls, "edam:format_1210",
            PermissibleValue(
                text="edam:format_1210",
                title="pure nucleotide",
                description="""Alphabet for a nucleotide sequence with possible ambiguity and unknown positions but without non-sequence characters.""",
                meaning=EDAM["format_1210"]))
        setattr(cls, "edam:format_1211",
            PermissibleValue(
                text="edam:format_1211",
                title="unambiguous pure nucleotide",
                description="""Alphabet for a nucleotide sequence (characters ACGTU only) with possible unknown positions but without ambiguity or non-sequence characters .""",
                meaning=EDAM["format_1211"]))
        setattr(cls, "edam:format_1212",
            PermissibleValue(
                text="edam:format_1212",
                title="dna",
                description="""Alphabet for a DNA sequence with possible ambiguity, unknown positions and non-sequence characters.""",
                meaning=EDAM["format_1212"]))
        setattr(cls, "edam:format_1213",
            PermissibleValue(
                text="edam:format_1213",
                title="rna",
                description="""Alphabet for an RNA sequence with possible ambiguity, unknown positions and non-sequence characters.""",
                meaning=EDAM["format_1213"]))
        setattr(cls, "edam:format_1214",
            PermissibleValue(
                text="edam:format_1214",
                title="unambiguous pure dna",
                description="""Alphabet for a DNA sequence (characters ACGT only) with possible unknown positions but without ambiguity or non-sequence characters.""",
                meaning=EDAM["format_1214"]))
        setattr(cls, "edam:format_1215",
            PermissibleValue(
                text="edam:format_1215",
                title="pure dna",
                description="""Alphabet for a DNA sequence with possible ambiguity and unknown positions but without non-sequence characters.""",
                meaning=EDAM["format_1215"]))
        setattr(cls, "edam:format_1216",
            PermissibleValue(
                text="edam:format_1216",
                title="unambiguous pure rna sequence",
                description="""Alphabet for an RNA sequence (characters ACGU only) with possible unknown positions but without ambiguity or non-sequence characters.""",
                meaning=EDAM["format_1216"]))
        setattr(cls, "edam:format_1217",
            PermissibleValue(
                text="edam:format_1217",
                title="pure rna",
                description="""Alphabet for an RNA sequence with possible ambiguity and unknown positions but without non-sequence characters.""",
                meaning=EDAM["format_1217"]))
        setattr(cls, "edam:format_1218",
            PermissibleValue(
                text="edam:format_1218",
                title="unambiguous pure protein",
                description="""Alphabet for any protein sequence with possible unknown positions but without ambiguity or non-sequence characters.""",
                meaning=EDAM["format_1218"]))
        setattr(cls, "edam:format_1219",
            PermissibleValue(
                text="edam:format_1219",
                title="pure protein",
                description="""Alphabet for any protein sequence with possible ambiguity and unknown positions but without non-sequence characters.""",
                meaning=EDAM["format_1219"]))
        setattr(cls, "edam:format_1248",
            PermissibleValue(
                text="edam:format_1248",
                title="EMBL feature location",
                description="""Format for sequence positions (feature location) as used in DDBJ/EMBL/GenBank database.""",
                meaning=EDAM["format_1248"]))
        setattr(cls, "edam:format_1295",
            PermissibleValue(
                text="edam:format_1295",
                title="quicktandem",
                description="""Report format for tandem repeats in a nucleotide sequence (format generated by the Sanger Centre quicktandem program).""",
                meaning=EDAM["format_1295"]))
        setattr(cls, "edam:format_1296",
            PermissibleValue(
                text="edam:format_1296",
                title="Sanger inverted repeats",
                description="""Report format for inverted repeats in a nucleotide sequence (format generated by the Sanger Centre inverted program).""",
                meaning=EDAM["format_1296"]))
        setattr(cls, "edam:format_1297",
            PermissibleValue(
                text="edam:format_1297",
                title="EMBOSS repeat",
                description="Report format for tandem repeats in a sequence (an EMBOSS report format).",
                meaning=EDAM["format_1297"]))
        setattr(cls, "edam:format_1316",
            PermissibleValue(
                text="edam:format_1316",
                title="est2genome format",
                description="Format of a report on exon-intron structure generated by EMBOSS est2genome.",
                meaning=EDAM["format_1316"]))
        setattr(cls, "edam:format_1318",
            PermissibleValue(
                text="edam:format_1318",
                title="restrict format",
                description="""Report format for restriction enzyme recognition sites used by EMBOSS restrict program.""",
                meaning=EDAM["format_1318"]))
        setattr(cls, "edam:format_1319",
            PermissibleValue(
                text="edam:format_1319",
                title="restover format",
                description="""Report format for restriction enzyme recognition sites used by EMBOSS restover program.""",
                meaning=EDAM["format_1319"]))
        setattr(cls, "edam:format_1320",
            PermissibleValue(
                text="edam:format_1320",
                title="REBASE restriction sites",
                description="Report format for restriction enzyme recognition sites used by REBASE database.",
                meaning=EDAM["format_1320"]))
        setattr(cls, "edam:format_1332",
            PermissibleValue(
                text="edam:format_1332",
                title="FASTA search results format",
                description="""Format of results of a sequence database search using FASTA.
This includes (typically) score data, alignment data and a histogram (of observed and expected distribution of E values.)""",
                meaning=EDAM["format_1332"]))
        setattr(cls, "edam:format_1333",
            PermissibleValue(
                text="edam:format_1333",
                title="BLAST results",
                description="""Format of results of a sequence database search using some variant of BLAST.
This includes score data, alignment data and summary table.""",
                meaning=EDAM["format_1333"]))
        setattr(cls, "edam:format_1334",
            PermissibleValue(
                text="edam:format_1334",
                title="mspcrunch",
                description="Format of results of a sequence database search using some variant of MSPCrunch.",
                meaning=EDAM["format_1334"]))
        setattr(cls, "edam:format_1335",
            PermissibleValue(
                text="edam:format_1335",
                title="Smith-Waterman format",
                description="Format of results of a sequence database search using some variant of Smith Waterman.",
                meaning=EDAM["format_1335"]))
        setattr(cls, "edam:format_1336",
            PermissibleValue(
                text="edam:format_1336",
                title="dhf",
                description="""Format of EMBASSY domain hits file (DHF) of hits (sequences) with domain classification information.
The hits are relatives to a SCOP or CATH family and are found from a search of a sequence database.""",
                meaning=EDAM["format_1336"]))
        setattr(cls, "edam:format_1337",
            PermissibleValue(
                text="edam:format_1337",
                title="lhf",
                description="""Format of EMBASSY ligand hits file (LHF) of database hits (sequences) with ligand classification information.
The hits are putative ligand-binding sequences and are found from a search of a sequence database.""",
                meaning=EDAM["format_1337"]))
        setattr(cls, "edam:format_1341",
            PermissibleValue(
                text="edam:format_1341",
                title="InterPro hits format",
                description="Results format for searches of the InterPro database.",
                meaning=EDAM["format_1341"]))
        setattr(cls, "edam:format_1342",
            PermissibleValue(
                text="edam:format_1342",
                title="InterPro protein view report format",
                description="""Format of results of a search of the InterPro database showing matches of query protein sequence(s) to InterPro entries.
The report includes a classification of regions in a query protein sequence which are assigned to a known InterPro protein family or group.""",
                meaning=EDAM["format_1342"]))
        setattr(cls, "edam:format_1343",
            PermissibleValue(
                text="edam:format_1343",
                title="InterPro match table format",
                description="""Format of results of a search of the InterPro database showing matches between protein sequence(s) and signatures for an InterPro entry.
The table presents matches between query proteins (rows) and signature methods (columns) for this entry. Alternatively the sequence(s) might be from from the InterPro entry itself. The match position in the protein sequence and match status (true positive, false positive etc) are indicated.""",
                meaning=EDAM["format_1343"]))
        setattr(cls, "edam:format_1349",
            PermissibleValue(
                text="edam:format_1349",
                title="HMMER Dirichlet prior",
                description="Dirichlet distribution HMMER format.",
                meaning=EDAM["format_1349"]))
        setattr(cls, "edam:format_1350",
            PermissibleValue(
                text="edam:format_1350",
                title="MEME Dirichlet prior",
                description="Dirichlet distribution MEME format.",
                meaning=EDAM["format_1350"]))
        setattr(cls, "edam:format_1351",
            PermissibleValue(
                text="edam:format_1351",
                title="HMMER emission and transition",
                description="""Format of a report from the HMMER package on the emission and transition counts of a hidden Markov model.""",
                meaning=EDAM["format_1351"]))
        setattr(cls, "edam:format_1356",
            PermissibleValue(
                text="edam:format_1356",
                title="prosite-pattern",
                description="Format of a regular expression pattern from the Prosite database.",
                meaning=EDAM["format_1356"]))
        setattr(cls, "edam:format_1357",
            PermissibleValue(
                text="edam:format_1357",
                title="EMBOSS sequence pattern",
                description="Format of an EMBOSS sequence pattern.",
                meaning=EDAM["format_1357"]))
        setattr(cls, "edam:format_1360",
            PermissibleValue(
                text="edam:format_1360",
                title="meme-motif",
                description="A motif in the format generated by the MEME program.",
                meaning=EDAM["format_1360"]))
        setattr(cls, "edam:format_1366",
            PermissibleValue(
                text="edam:format_1366",
                title="prosite-profile",
                description="Sequence profile (sequence classifier) format used in the PROSITE database.",
                meaning=EDAM["format_1366"]))
        setattr(cls, "edam:format_1367",
            PermissibleValue(
                text="edam:format_1367",
                title="JASPAR format",
                description="A profile (sequence classifier) in the format used in the JASPAR database.",
                meaning=EDAM["format_1367"]))
        setattr(cls, "edam:format_1369",
            PermissibleValue(
                text="edam:format_1369",
                title="MEME background Markov model",
                description="Format of the model of random sequences used by MEME.",
                meaning=EDAM["format_1369"]))
        setattr(cls, "edam:format_1370",
            PermissibleValue(
                text="edam:format_1370",
                title="HMMER format",
                description="Format of a hidden Markov model representation used by the HMMER package.",
                meaning=EDAM["format_1370"]))
        setattr(cls, "edam:format_1391",
            PermissibleValue(
                text="edam:format_1391",
                title="HMMER-aln",
                description="FASTA-style format for multiple sequences aligned by HMMER package to an HMM.",
                meaning=EDAM["format_1391"]))
        setattr(cls, "edam:format_1392",
            PermissibleValue(
                text="edam:format_1392",
                title="DIALIGN format",
                description="Format of multiple sequences aligned by DIALIGN package.",
                meaning=EDAM["format_1392"]))
        setattr(cls, "edam:format_1393",
            PermissibleValue(
                text="edam:format_1393",
                title="daf",
                description="""EMBASSY 'domain alignment file' (DAF) format, containing a sequence alignment of protein domains belonging to the same SCOP or CATH family.
The format is clustal-like and includes annotation of domain family classification information.""",
                meaning=EDAM["format_1393"]))
        setattr(cls, "edam:format_1419",
            PermissibleValue(
                text="edam:format_1419",
                title="Sequence-MEME profile alignment",
                description="""Format for alignment of molecular sequences to MEME profiles (position-dependent scoring matrices) as generated by the MAST tool from the MEME package.""",
                meaning=EDAM["format_1419"]))
        setattr(cls, "edam:format_1421",
            PermissibleValue(
                text="edam:format_1421",
                title="HMMER profile alignment (sequences versus HMMs)",
                description="""Format used by the HMMER package for an alignment of a sequence against a hidden Markov model database.""",
                meaning=EDAM["format_1421"]))
        setattr(cls, "edam:format_1422",
            PermissibleValue(
                text="edam:format_1422",
                title="HMMER profile alignment (HMM versus sequences)",
                description="""Format used by the HMMER package for of an alignment of a hidden Markov model against a sequence database.""",
                meaning=EDAM["format_1422"]))
        setattr(cls, "edam:format_1423",
            PermissibleValue(
                text="edam:format_1423",
                title="Phylip distance matrix",
                description="""Data Type must include the distance matrix, probably as pairs of sequence identifiers with a distance (integer or float).
Format of PHYLIP phylogenetic distance matrix data.""",
                meaning=EDAM["format_1423"]))
        setattr(cls, "edam:format_1424",
            PermissibleValue(
                text="edam:format_1424",
                title="ClustalW dendrogram",
                description="Dendrogram (tree file) format generated by ClustalW.",
                meaning=EDAM["format_1424"]))
        setattr(cls, "edam:format_1425",
            PermissibleValue(
                text="edam:format_1425",
                title="Phylip tree raw",
                description="""Raw data file format used by Phylip from which a phylogenetic tree is directly generated or plotted.""",
                meaning=EDAM["format_1425"]))
        setattr(cls, "edam:format_1430",
            PermissibleValue(
                text="edam:format_1430",
                title="Phylip continuous quantitative characters",
                description="PHYLIP file format for continuous quantitative character data.",
                meaning=EDAM["format_1430"]))
        setattr(cls, "edam:format_1432",
            PermissibleValue(
                text="edam:format_1432",
                title="Phylip character frequencies format",
                description="PHYLIP file format for phylogenetics character frequency data.",
                meaning=EDAM["format_1432"]))
        setattr(cls, "edam:format_1433",
            PermissibleValue(
                text="edam:format_1433",
                title="Phylip discrete states format",
                description="Format of PHYLIP discrete states data.",
                meaning=EDAM["format_1433"]))
        setattr(cls, "edam:format_1434",
            PermissibleValue(
                text="edam:format_1434",
                title="Phylip cliques format",
                description="Format of PHYLIP cliques data.",
                meaning=EDAM["format_1434"]))
        setattr(cls, "edam:format_1435",
            PermissibleValue(
                text="edam:format_1435",
                title="Phylip tree format",
                description="Phylogenetic tree data format used by the PHYLIP program.",
                meaning=EDAM["format_1435"]))
        setattr(cls, "edam:format_1436",
            PermissibleValue(
                text="edam:format_1436",
                title="TreeBASE format",
                description="The format of an entry from the TreeBASE database of phylogenetic data.",
                meaning=EDAM["format_1436"]))
        setattr(cls, "edam:format_1437",
            PermissibleValue(
                text="edam:format_1437",
                title="TreeFam format",
                description="The format of an entry from the TreeFam database of phylogenetic data.",
                meaning=EDAM["format_1437"]))
        setattr(cls, "edam:format_1445",
            PermissibleValue(
                text="edam:format_1445",
                title="Phylip tree distance format",
                description="""Format for distances, such as Branch Score distance, between two or more phylogenetic trees as used by the Phylip package.""",
                meaning=EDAM["format_1445"]))
        setattr(cls, "edam:format_1454",
            PermissibleValue(
                text="edam:format_1454",
                title="dssp",
                description="""Format of an entry from the DSSP database (Dictionary of Secondary Structure in Proteins).
The DSSP database is built using the DSSP application which defines secondary structure, geometrical features and solvent exposure of proteins, given atomic coordinates in PDB format.""",
                meaning=EDAM["format_1454"]))
        setattr(cls, "edam:format_1455",
            PermissibleValue(
                text="edam:format_1455",
                title="hssp",
                description="Entry format of the HSSP database (Homology-derived Secondary Structure in Proteins).",
                meaning=EDAM["format_1455"]))
        setattr(cls, "edam:format_1457",
            PermissibleValue(
                text="edam:format_1457",
                title="Dot-bracket format",
                description="""Format of RNA secondary structure in dot-bracket notation, originally generated by the Vienna RNA package/server.""",
                meaning=EDAM["format_1457"]))
        setattr(cls, "edam:format_1458",
            PermissibleValue(
                text="edam:format_1458",
                title="Vienna local RNA secondary structure format",
                description="""Format of local RNA secondary structure components with free energy values, generated by the Vienna RNA package/server.""",
                meaning=EDAM["format_1458"]))
        setattr(cls, "edam:format_1475",
            PermissibleValue(
                text="edam:format_1475",
                title="PDB database entry format",
                description="Format of an entry (or part of an entry) from the PDB database.",
                meaning=EDAM["format_1475"]))
        setattr(cls, "edam:format_1476",
            PermissibleValue(
                text="edam:format_1476",
                title="PDB",
                description="Entry format of PDB database in PDB format.",
                meaning=EDAM["format_1476"]))
        setattr(cls, "edam:format_1477",
            PermissibleValue(
                text="edam:format_1477",
                title="mmCIF",
                description="Entry format of PDB database in mmCIF format.",
                meaning=EDAM["format_1477"]))
        setattr(cls, "edam:format_1478",
            PermissibleValue(
                text="edam:format_1478",
                title="PDBML",
                description="Entry format of PDB database in PDBML (XML) format.",
                meaning=EDAM["format_1478"]))
        setattr(cls, "edam:format_1504",
            PermissibleValue(
                text="edam:format_1504",
                title="aaindex",
                description="Amino acid index format used by the AAindex database.",
                meaning=EDAM["format_1504"]))
        setattr(cls, "edam:format_1551",
            PermissibleValue(
                text="edam:format_1551",
                title="Pcons report format",
                description="""Format of output of the Pcons Model Quality Assessment Program (MQAP).
Pcons ranks protein models by assessing their quality based on the occurrence of recurring common three-dimensional structural patterns. Pcons returns a score reflecting the overall global quality and a score for each individual residue in the protein reflecting the local residue quality.""",
                meaning=EDAM["format_1551"]))
        setattr(cls, "edam:format_1552",
            PermissibleValue(
                text="edam:format_1552",
                title="ProQ report format",
                description="""Format of output of the ProQ protein model quality predictor.
ProQ is a neural network-based predictor that predicts the quality of a protein model based on the number of structural features.""",
                meaning=EDAM["format_1552"]))
        setattr(cls, "edam:format_1582",
            PermissibleValue(
                text="edam:format_1582",
                title="findkm",
                description="""A report format for the kinetics of enzyme-catalysed reaction(s) in a format generated by EMBOSS findkm. This includes Michaelis Menten plot, Hanes Woolf plot, Michaelis Menten constant (Km) and maximum velocity (Vmax).""",
                meaning=EDAM["format_1582"]))
        setattr(cls, "edam:format_1627",
            PermissibleValue(
                text="edam:format_1627",
                title="Primer3 primer",
                description="""Report format on PCR primers and hybridisation oligos as generated by Whitehead primer3 program.""",
                meaning=EDAM["format_1627"]))
        setattr(cls, "edam:format_1628",
            PermissibleValue(
                text="edam:format_1628",
                title="ABI",
                description="A format of raw sequence read data from an Applied Biosystems sequencing machine.",
                meaning=EDAM["format_1628"]))
        setattr(cls, "edam:format_1629",
            PermissibleValue(
                text="edam:format_1629",
                title="mira",
                description="Format of MIRA sequence trace information file.",
                meaning=EDAM["format_1629"]))
        setattr(cls, "edam:format_1630",
            PermissibleValue(
                text="edam:format_1630",
                title="CAF",
                description="""Common Assembly Format (CAF). A sequence assembly format including contigs, base-call qualities, and other metadata.""",
                meaning=EDAM["format_1630"]))
        setattr(cls, "edam:format_1631",
            PermissibleValue(
                text="edam:format_1631",
                title="EXP",
                description="Sequence assembly project file EXP format.",
                meaning=EDAM["format_1631"]))
        setattr(cls, "edam:format_1632",
            PermissibleValue(
                text="edam:format_1632",
                title="SCF",
                description="""Staden Chromatogram Files format (SCF) of base-called sequence reads, qualities, and other metadata.""",
                meaning=EDAM["format_1632"]))
        setattr(cls, "edam:format_1633",
            PermissibleValue(
                text="edam:format_1633",
                title="PHD",
                description="PHD sequence trace format to store serialised chromatogram data (reads).",
                meaning=EDAM["format_1633"]))
        setattr(cls, "edam:format_1637",
            PermissibleValue(
                text="edam:format_1637",
                title="dat",
                description="Format of Affymetrix data file of raw image data.",
                meaning=EDAM["format_1637"]))
        setattr(cls, "edam:format_1638",
            PermissibleValue(
                text="edam:format_1638",
                title="cel",
                description="""Format of Affymetrix data file of information about (raw) expression levels of the individual probes.""",
                meaning=EDAM["format_1638"]))
        setattr(cls, "edam:format_1639",
            PermissibleValue(
                text="edam:format_1639",
                title="affymetrix",
                description="""Format of affymetrix gene cluster files (hc-genes.txt, hc-chips.txt) from hierarchical clustering.""",
                meaning=EDAM["format_1639"]))
        setattr(cls, "edam:format_1641",
            PermissibleValue(
                text="edam:format_1641",
                title="affymetrix-exp",
                description="""Affymetrix data file format for information about experimental conditions and protocols.""",
                meaning=EDAM["format_1641"]))
        setattr(cls, "edam:format_1644",
            PermissibleValue(
                text="edam:format_1644",
                title="CHP",
                description="""Format of Affymetrix data file of information about (normalised) expression levels of the individual probes.""",
                meaning=EDAM["format_1644"]))
        setattr(cls, "edam:format_1665",
            PermissibleValue(
                text="edam:format_1665",
                title="Taverna workflow format",
                description="Format of Taverna workflows.",
                meaning=EDAM["format_1665"]))
        setattr(cls, "edam:format_1705",
            PermissibleValue(
                text="edam:format_1705",
                title="HET group dictionary entry format",
                description="The format of an entry from the HET group dictionary (HET groups from PDB files).",
                meaning=EDAM["format_1705"]))
        setattr(cls, "edam:format_1734",
            PermissibleValue(
                text="edam:format_1734",
                title="PubMed citation",
                description="Format of bibliographic reference as used by the PubMed database.",
                meaning=EDAM["format_1734"]))
        setattr(cls, "edam:format_1735",
            PermissibleValue(
                text="edam:format_1735",
                title="Medline Display Format",
                description="""Bibliographic reference information including citation information is included
Format for abstracts of scientific articles from the Medline database.""",
                meaning=EDAM["format_1735"]))
        setattr(cls, "edam:format_1736",
            PermissibleValue(
                text="edam:format_1736",
                title="CiteXplore-core",
                description="CiteXplore 'core' citation format including title, journal, authors and abstract.",
                meaning=EDAM["format_1736"]))
        setattr(cls, "edam:format_1737",
            PermissibleValue(
                text="edam:format_1737",
                title="CiteXplore-all",
                description="""CiteXplore 'all' citation format includes all known details such as Mesh terms and cross-references.""",
                meaning=EDAM["format_1737"]))
        setattr(cls, "edam:format_1739",
            PermissibleValue(
                text="edam:format_1739",
                title="pmc",
                description="Article format of the PubMed Central database.",
                meaning=EDAM["format_1739"]))
        setattr(cls, "edam:format_1740",
            PermissibleValue(
                text="edam:format_1740",
                title="iHOP format",
                description="The format of iHOP (Information Hyperlinked over Proteins) text-mining result.",
                meaning=EDAM["format_1740"]))
        setattr(cls, "edam:format_1741",
            PermissibleValue(
                text="edam:format_1741",
                title="OSCAR format",
                description="""OSCAR (Open-Source Chemistry Analysis Routines) software performs chemistry-specific parsing of chemical documents. It attempts to identify chemical names, ontology concepts, and chemical data from a document.
OSCAR format of annotated chemical text.""",
                meaning=EDAM["format_1741"]))
        setattr(cls, "edam:format_1861",
            PermissibleValue(
                text="edam:format_1861",
                title="PlasMapper TextMap",
                description="Map of a plasmid (circular DNA) in PlasMapper TextMap format.",
                meaning=EDAM["format_1861"]))
        setattr(cls, "edam:format_1910",
            PermissibleValue(
                text="edam:format_1910",
                title="newick",
                description="Phylogenetic tree Newick (text) format.",
                meaning=EDAM["format_1910"]))
        setattr(cls, "edam:format_1911",
            PermissibleValue(
                text="edam:format_1911",
                title="TreeCon format",
                description="Phylogenetic tree TreeCon (text) format.",
                meaning=EDAM["format_1911"]))
        setattr(cls, "edam:format_1912",
            PermissibleValue(
                text="edam:format_1912",
                title="Nexus format",
                description="Phylogenetic tree Nexus (text) format.",
                meaning=EDAM["format_1912"]))
        setattr(cls, "edam:format_1919",
            PermissibleValue(
                text="edam:format_1919",
                title="Sequence record format",
                description="Data format for a molecular sequence record.",
                meaning=EDAM["format_1919"]))
        setattr(cls, "edam:format_1920",
            PermissibleValue(
                text="edam:format_1920",
                title="Sequence feature annotation format",
                description="Data format for molecular sequence feature information.",
                meaning=EDAM["format_1920"]))
        setattr(cls, "edam:format_1921",
            PermissibleValue(
                text="edam:format_1921",
                title="Alignment format",
                description="Data format for molecular sequence alignment information.",
                meaning=EDAM["format_1921"]))
        setattr(cls, "edam:format_1923",
            PermissibleValue(
                text="edam:format_1923",
                title="acedb",
                description="ACEDB sequence format.",
                meaning=EDAM["format_1923"]))
        setattr(cls, "edam:format_1925",
            PermissibleValue(
                text="edam:format_1925",
                title="codata",
                description="Codata entry format.",
                meaning=EDAM["format_1925"]))
        setattr(cls, "edam:format_1926",
            PermissibleValue(
                text="edam:format_1926",
                title="dbid",
                description="Fasta format variant with database name before ID.",
                meaning=EDAM["format_1926"]))
        setattr(cls, "edam:format_1927",
            PermissibleValue(
                text="edam:format_1927",
                title="EMBL format",
                description="EMBL entry format.",
                meaning=EDAM["format_1927"]))
        setattr(cls, "edam:format_1928",
            PermissibleValue(
                text="edam:format_1928",
                title="Staden experiment format",
                description="Staden experiment file format.",
                meaning=EDAM["format_1928"]))
        setattr(cls, "edam:format_1929",
            PermissibleValue(
                text="edam:format_1929",
                title="FASTA",
                description="FASTA format including NCBI-style IDs.",
                meaning=EDAM["format_1929"]))
        setattr(cls, "edam:format_1930",
            PermissibleValue(
                text="edam:format_1930",
                title="FASTQ",
                description="FASTQ short read format ignoring quality scores.",
                meaning=EDAM["format_1930"]))
        setattr(cls, "edam:format_1931",
            PermissibleValue(
                text="edam:format_1931",
                title="FASTQ-illumina",
                description="FASTQ Illumina 1.3 short read format.",
                meaning=EDAM["format_1931"]))
        setattr(cls, "edam:format_1932",
            PermissibleValue(
                text="edam:format_1932",
                title="FASTQ-sanger",
                description="FASTQ short read format with phred quality.",
                meaning=EDAM["format_1932"]))
        setattr(cls, "edam:format_1933",
            PermissibleValue(
                text="edam:format_1933",
                title="FASTQ-solexa",
                description="FASTQ Solexa/Illumina 1.0 short read format.",
                meaning=EDAM["format_1933"]))
        setattr(cls, "edam:format_1934",
            PermissibleValue(
                text="edam:format_1934",
                title="fitch program",
                description="Fitch program format.",
                meaning=EDAM["format_1934"]))
        setattr(cls, "edam:format_1935",
            PermissibleValue(
                text="edam:format_1935",
                title="GCG",
                description="""GCG SSF (single sequence file) file format.
GCG sequence file format.""",
                meaning=EDAM["format_1935"]))
        setattr(cls, "edam:format_1936",
            PermissibleValue(
                text="edam:format_1936",
                title="GenBank format",
                description="Genbank entry format.",
                meaning=EDAM["format_1936"]))
        setattr(cls, "edam:format_1937",
            PermissibleValue(
                text="edam:format_1937",
                title="genpept",
                description="""Currently identical to refseqp format
Genpept protein entry format.""",
                meaning=EDAM["format_1937"]))
        setattr(cls, "edam:format_1938",
            PermissibleValue(
                text="edam:format_1938",
                title="GFF2-seq",
                description="GFF feature file format with sequence in the header.",
                meaning=EDAM["format_1938"]))
        setattr(cls, "edam:format_1939",
            PermissibleValue(
                text="edam:format_1939",
                title="GFF3-seq",
                description="GFF3 feature file format with sequence.",
                meaning=EDAM["format_1939"]))
        setattr(cls, "edam:format_1940",
            PermissibleValue(
                text="edam:format_1940",
                title="giFASTA format",
                description="FASTA sequence format including NCBI-style GIs.",
                meaning=EDAM["format_1940"]))
        setattr(cls, "edam:format_1941",
            PermissibleValue(
                text="edam:format_1941",
                title="hennig86",
                description="Hennig86 output sequence format.",
                meaning=EDAM["format_1941"]))
        setattr(cls, "edam:format_1942",
            PermissibleValue(
                text="edam:format_1942",
                title="ig",
                description="Intelligenetics sequence format.",
                meaning=EDAM["format_1942"]))
        setattr(cls, "edam:format_1943",
            PermissibleValue(
                text="edam:format_1943",
                title="igstrict",
                description="Intelligenetics sequence format (strict version).",
                meaning=EDAM["format_1943"]))
        setattr(cls, "edam:format_1944",
            PermissibleValue(
                text="edam:format_1944",
                title="jackknifer",
                description="Jackknifer interleaved and non-interleaved sequence format.",
                meaning=EDAM["format_1944"]))
        setattr(cls, "edam:format_1945",
            PermissibleValue(
                text="edam:format_1945",
                title="mase format",
                description="Mase program sequence format.",
                meaning=EDAM["format_1945"]))
        setattr(cls, "edam:format_1946",
            PermissibleValue(
                text="edam:format_1946",
                title="mega-seq",
                description="Mega interleaved and non-interleaved sequence format.",
                meaning=EDAM["format_1946"]))
        setattr(cls, "edam:format_1947",
            PermissibleValue(
                text="edam:format_1947",
                title="GCG MSF",
                description="GCG MSF (multiple sequence file) file format.",
                meaning=EDAM["format_1947"]))
        setattr(cls, "edam:format_1948",
            PermissibleValue(
                text="edam:format_1948",
                title="nbrf/pir",
                description="NBRF/PIR entry sequence format.",
                meaning=EDAM["format_1948"]))
        setattr(cls, "edam:format_1949",
            PermissibleValue(
                text="edam:format_1949",
                title="nexus-seq",
                description="Nexus/paup interleaved sequence format.",
                meaning=EDAM["format_1949"]))
        setattr(cls, "edam:format_1950",
            PermissibleValue(
                text="edam:format_1950",
                title="pdbatom",
                description="""PDB sequence format (ATOM lines).
pdb format in EMBOSS.""",
                meaning=EDAM["format_1950"]))
        setattr(cls, "edam:format_1951",
            PermissibleValue(
                text="edam:format_1951",
                title="pdbatomnuc",
                description="""PDB nucleotide sequence format (ATOM lines).
pdbnuc format in EMBOSS.""",
                meaning=EDAM["format_1951"]))
        setattr(cls, "edam:format_1952",
            PermissibleValue(
                text="edam:format_1952",
                title="pdbseqresnuc",
                description="""PDB nucleotide sequence format (SEQRES lines).
pdbnucseq format in EMBOSS.""",
                meaning=EDAM["format_1952"]))
        setattr(cls, "edam:format_1953",
            PermissibleValue(
                text="edam:format_1953",
                title="pdbseqres",
                description="""PDB sequence format (SEQRES lines).
pdbseq format in EMBOSS.""",
                meaning=EDAM["format_1953"]))
        setattr(cls, "edam:format_1954",
            PermissibleValue(
                text="edam:format_1954",
                title="Pearson format",
                description="Plain old FASTA sequence format (unspecified format for IDs).",
                meaning=EDAM["format_1954"]))
        setattr(cls, "edam:format_1957",
            PermissibleValue(
                text="edam:format_1957",
                title="raw",
                description="Raw sequence format with no non-sequence characters.",
                meaning=EDAM["format_1957"]))
        setattr(cls, "edam:format_1958",
            PermissibleValue(
                text="edam:format_1958",
                title="refseqp",
                description="""Currently identical to genpept format
Refseq protein entry sequence format.""",
                meaning=EDAM["format_1958"]))
        setattr(cls, "edam:format_1960",
            PermissibleValue(
                text="edam:format_1960",
                title="Staden format",
                description="Staden suite sequence format.",
                meaning=EDAM["format_1960"]))
        setattr(cls, "edam:format_1961",
            PermissibleValue(
                text="edam:format_1961",
                title="Stockholm format",
                description="Stockholm multiple sequence alignment format (used by Pfam and Rfam).",
                meaning=EDAM["format_1961"]))
        setattr(cls, "edam:format_1962",
            PermissibleValue(
                text="edam:format_1962",
                title="strider format",
                description="DNA strider output sequence format.",
                meaning=EDAM["format_1962"]))
        setattr(cls, "edam:format_1963",
            PermissibleValue(
                text="edam:format_1963",
                title="UniProtKB format",
                description="UniProtKB entry sequence format.",
                meaning=EDAM["format_1963"]))
        setattr(cls, "edam:format_1964",
            PermissibleValue(
                text="edam:format_1964",
                title="plain text format (unformatted)",
                description="Plain text sequence format (essentially unformatted).",
                meaning=EDAM["format_1964"]))
        setattr(cls, "edam:format_1966",
            PermissibleValue(
                text="edam:format_1966",
                title="ASN.1 sequence format",
                description="NCBI ASN.1-based sequence format.",
                meaning=EDAM["format_1966"]))
        setattr(cls, "edam:format_1967",
            PermissibleValue(
                text="edam:format_1967",
                title="DAS format",
                description="DAS sequence (XML) format (any type).",
                meaning=EDAM["format_1967"]))
        setattr(cls, "edam:format_1968",
            PermissibleValue(
                text="edam:format_1968",
                title="dasdna",
                description="""DAS sequence (XML) format (nucleotide-only).
The use of this format is deprecated.""",
                meaning=EDAM["format_1968"]))
        setattr(cls, "edam:format_1969",
            PermissibleValue(
                text="edam:format_1969",
                title="debug-seq",
                description="EMBOSS debugging trace sequence format of full internal data content.",
                meaning=EDAM["format_1969"]))
        setattr(cls, "edam:format_1970",
            PermissibleValue(
                text="edam:format_1970",
                title="jackknifernon",
                description="Jackknifer output sequence non-interleaved format.",
                meaning=EDAM["format_1970"]))
        setattr(cls, "edam:format_1972",
            PermissibleValue(
                text="edam:format_1972",
                title="NCBI format",
                description="""NCBI FASTA sequence format with NCBI-style IDs.
There are several variants of this.""",
                meaning=EDAM["format_1972"]))
        setattr(cls, "edam:format_1973",
            PermissibleValue(
                text="edam:format_1973",
                title="nexusnon",
                description="Nexus/paup non-interleaved sequence format.",
                meaning=EDAM["format_1973"]))
        setattr(cls, "edam:format_1974",
            PermissibleValue(
                text="edam:format_1974",
                title="GFF2",
                description="General Feature Format (GFF) of sequence features.",
                meaning=EDAM["format_1974"]))
        setattr(cls, "edam:format_1975",
            PermissibleValue(
                text="edam:format_1975",
                title="GFF3",
                description="Generic Feature Format version 3 (GFF3) of sequence features.",
                meaning=EDAM["format_1975"]))
        setattr(cls, "edam:format_1978",
            PermissibleValue(
                text="edam:format_1978",
                title="DASGFF",
                description="DAS GFF (XML) feature format.",
                meaning=EDAM["format_1978"]))
        setattr(cls, "edam:format_1979",
            PermissibleValue(
                text="edam:format_1979",
                title="debug-feat",
                description="EMBOSS debugging trace feature format of full internal data content.",
                meaning=EDAM["format_1979"]))
        setattr(cls, "edam:format_1982",
            PermissibleValue(
                text="edam:format_1982",
                title="ClustalW format",
                description="ClustalW format for (aligned) sequences.",
                meaning=EDAM["format_1982"]))
        setattr(cls, "edam:format_1983",
            PermissibleValue(
                text="edam:format_1983",
                title="debug",
                description="EMBOSS alignment format for debugging trace of full internal data content.",
                meaning=EDAM["format_1983"]))
        setattr(cls, "edam:format_1984",
            PermissibleValue(
                text="edam:format_1984",
                title="FASTA-aln",
                description="Fasta format for (aligned) sequences.",
                meaning=EDAM["format_1984"]))
        setattr(cls, "edam:format_1985",
            PermissibleValue(
                text="edam:format_1985",
                title="markx0",
                description="Pearson MARKX0 alignment format.",
                meaning=EDAM["format_1985"]))
        setattr(cls, "edam:format_1986",
            PermissibleValue(
                text="edam:format_1986",
                title="markx1",
                description="Pearson MARKX1 alignment format.",
                meaning=EDAM["format_1986"]))
        setattr(cls, "edam:format_1987",
            PermissibleValue(
                text="edam:format_1987",
                title="markx10",
                description="Pearson MARKX10 alignment format.",
                meaning=EDAM["format_1987"]))
        setattr(cls, "edam:format_1988",
            PermissibleValue(
                text="edam:format_1988",
                title="markx2",
                description="Pearson MARKX2 alignment format.",
                meaning=EDAM["format_1988"]))
        setattr(cls, "edam:format_1989",
            PermissibleValue(
                text="edam:format_1989",
                title="markx3",
                description="Pearson MARKX3 alignment format.",
                meaning=EDAM["format_1989"]))
        setattr(cls, "edam:format_1990",
            PermissibleValue(
                text="edam:format_1990",
                title="match",
                description="Alignment format for start and end of matches between sequence pairs.",
                meaning=EDAM["format_1990"]))
        setattr(cls, "edam:format_1991",
            PermissibleValue(
                text="edam:format_1991",
                title="mega",
                description="Mega format for (typically aligned) sequences.",
                meaning=EDAM["format_1991"]))
        setattr(cls, "edam:format_1992",
            PermissibleValue(
                text="edam:format_1992",
                title="meganon",
                description="Mega non-interleaved format for (typically aligned) sequences.",
                meaning=EDAM["format_1992"]))
        setattr(cls, "edam:format_1996",
            PermissibleValue(
                text="edam:format_1996",
                title="pair",
                description="EMBOSS simple sequence pairwise alignment format.",
                meaning=EDAM["format_1996"]))
        setattr(cls, "edam:format_1997",
            PermissibleValue(
                text="edam:format_1997",
                title="PHYLIP format",
                description="Phylip format for (aligned) sequences.",
                meaning=EDAM["format_1997"]))
        setattr(cls, "edam:format_1998",
            PermissibleValue(
                text="edam:format_1998",
                title="PHYLIP sequential",
                description="Phylip non-interleaved format for (aligned) sequences.",
                meaning=EDAM["format_1998"]))
        setattr(cls, "edam:format_1999",
            PermissibleValue(
                text="edam:format_1999",
                title="scores format",
                description="Alignment format for score values for pairs of sequences.",
                meaning=EDAM["format_1999"]))
        setattr(cls, "edam:format_2000",
            PermissibleValue(
                text="edam:format_2000",
                title="selex",
                description="SELEX format for (aligned) sequences.",
                meaning=EDAM["format_2000"]))
        setattr(cls, "edam:format_2001",
            PermissibleValue(
                text="edam:format_2001",
                title="EMBOSS simple format",
                description="EMBOSS simple multiple alignment format.",
                meaning=EDAM["format_2001"]))
        setattr(cls, "edam:format_2002",
            PermissibleValue(
                text="edam:format_2002",
                title="srs format",
                description="Simple multiple sequence (alignment) format for SRS.",
                meaning=EDAM["format_2002"]))
        setattr(cls, "edam:format_2003",
            PermissibleValue(
                text="edam:format_2003",
                title="srspair",
                description="Simple sequence pair (alignment) format for SRS.",
                meaning=EDAM["format_2003"]))
        setattr(cls, "edam:format_2004",
            PermissibleValue(
                text="edam:format_2004",
                title="T-Coffee format",
                description="T-Coffee program alignment format.",
                meaning=EDAM["format_2004"]))
        setattr(cls, "edam:format_2005",
            PermissibleValue(
                text="edam:format_2005",
                title="TreeCon-seq",
                description="Treecon format for (aligned) sequences.",
                meaning=EDAM["format_2005"]))
        setattr(cls, "edam:format_2006",
            PermissibleValue(
                text="edam:format_2006",
                title="Phylogenetic tree format",
                description="Data format for a phylogenetic tree.",
                meaning=EDAM["format_2006"]))
        setattr(cls, "edam:format_2013",
            PermissibleValue(
                text="edam:format_2013",
                title="Biological pathway or network format",
                description="Data format for a biological pathway or network.",
                meaning=EDAM["format_2013"]))
        setattr(cls, "edam:format_2014",
            PermissibleValue(
                text="edam:format_2014",
                title="Sequence-profile alignment format",
                description="Data format for a sequence-profile alignment.",
                meaning=EDAM["format_2014"]))
        setattr(cls, "edam:format_2017",
            PermissibleValue(
                text="edam:format_2017",
                title="Amino acid index format",
                description="Data format for an amino acid index.",
                meaning=EDAM["format_2017"]))
        setattr(cls, "edam:format_2020",
            PermissibleValue(
                text="edam:format_2020",
                title="Article format",
                description="Data format for a full-text scientific article.",
                meaning=EDAM["format_2020"]))
        setattr(cls, "edam:format_2021",
            PermissibleValue(
                text="edam:format_2021",
                title="Text mining report format",
                description="Data format of a report from text mining.",
                meaning=EDAM["format_2021"]))
        setattr(cls, "edam:format_2027",
            PermissibleValue(
                text="edam:format_2027",
                title="Enzyme kinetics report format",
                description="Data format for reports on enzyme kinetics.",
                meaning=EDAM["format_2027"]))
        setattr(cls, "edam:format_2030",
            PermissibleValue(
                text="edam:format_2030",
                title="Chemical data format",
                description="Format of a report on a chemical compound.",
                meaning=EDAM["format_2030"]))
        setattr(cls, "edam:format_2031",
            PermissibleValue(
                text="edam:format_2031",
                title="Gene annotation format",
                description="Format of a report on a particular locus, gene, gene system or groups of genes.",
                meaning=EDAM["format_2031"]))
        setattr(cls, "edam:format_2032",
            PermissibleValue(
                text="edam:format_2032",
                title="Workflow format",
                description="Format of a workflow.",
                meaning=EDAM["format_2032"]))
        setattr(cls, "edam:format_2033",
            PermissibleValue(
                text="edam:format_2033",
                title="Tertiary structure format",
                description="Data format for a molecular tertiary structure.",
                meaning=EDAM["format_2033"]))
        setattr(cls, "edam:format_2035",
            PermissibleValue(
                text="edam:format_2035",
                title="Chemical formula format",
                description="Text format of a chemical formula.",
                meaning=EDAM["format_2035"]))
        setattr(cls, "edam:format_2036",
            PermissibleValue(
                text="edam:format_2036",
                title="Phylogenetic character data format",
                description="Format of raw (unplotted) phylogenetic data.",
                meaning=EDAM["format_2036"]))
        setattr(cls, "edam:format_2037",
            PermissibleValue(
                text="edam:format_2037",
                title="Phylogenetic continuous quantitative character format",
                description="Format of phylogenetic continuous quantitative character data.",
                meaning=EDAM["format_2037"]))
        setattr(cls, "edam:format_2038",
            PermissibleValue(
                text="edam:format_2038",
                title="Phylogenetic discrete states format",
                description="Format of phylogenetic discrete states data.",
                meaning=EDAM["format_2038"]))
        setattr(cls, "edam:format_2039",
            PermissibleValue(
                text="edam:format_2039",
                title="Phylogenetic tree report (cliques) format",
                description="Format of phylogenetic cliques data.",
                meaning=EDAM["format_2039"]))
        setattr(cls, "edam:format_2040",
            PermissibleValue(
                text="edam:format_2040",
                title="Phylogenetic tree report (invariants) format",
                description="Format of phylogenetic invariants data.",
                meaning=EDAM["format_2040"]))
        setattr(cls, "edam:format_2049",
            PermissibleValue(
                text="edam:format_2049",
                title="Phylogenetic tree report (tree distances) format",
                description="Format for phylogenetic tree distance data.",
                meaning=EDAM["format_2049"]))
        setattr(cls, "edam:format_2052",
            PermissibleValue(
                text="edam:format_2052",
                title="Protein family report format",
                description="Format for reports on a protein family.",
                meaning=EDAM["format_2052"]))
        setattr(cls, "edam:format_2054",
            PermissibleValue(
                text="edam:format_2054",
                title="Protein interaction format",
                description="Format for molecular interaction data.",
                meaning=EDAM["format_2054"]))
        setattr(cls, "edam:format_2055",
            PermissibleValue(
                text="edam:format_2055",
                title="Sequence assembly format",
                description="Format for sequence assembly data.",
                meaning=EDAM["format_2055"]))
        setattr(cls, "edam:format_2056",
            PermissibleValue(
                text="edam:format_2056",
                title="Microarray experiment data format",
                description="""Format for information about a microarray experimental per se (not the data generated from that experiment).""",
                meaning=EDAM["format_2056"]))
        setattr(cls, "edam:format_2057",
            PermissibleValue(
                text="edam:format_2057",
                title="Sequence trace format",
                description="Format for sequence trace data (i.e. including base call information).",
                meaning=EDAM["format_2057"]))
        setattr(cls, "edam:format_2058",
            PermissibleValue(
                text="edam:format_2058",
                title="Gene expression report format",
                description="Format of a file of gene expression data, e.g. a gene expression matrix or profile.",
                meaning=EDAM["format_2058"]))
        setattr(cls, "edam:format_2060",
            PermissibleValue(
                text="edam:format_2060",
                title="Map format",
                description="Format of a map of (typically one) molecular sequence annotated with features.",
                meaning=EDAM["format_2060"]))
        setattr(cls, "edam:format_2061",
            PermissibleValue(
                text="edam:format_2061",
                title="Nucleic acid features (primers) format",
                description="Format of a report on PCR primers or hybridisation oligos in a nucleic acid sequence.",
                meaning=EDAM["format_2061"]))
        setattr(cls, "edam:format_2062",
            PermissibleValue(
                text="edam:format_2062",
                title="Protein report format",
                description="Format of a report of general information about a specific protein.",
                meaning=EDAM["format_2062"]))
        setattr(cls, "edam:format_2064",
            PermissibleValue(
                text="edam:format_2064",
                title="3D-1D scoring matrix format",
                description="Format of a matrix of 3D-1D scores (amino acid environment probabilities).",
                meaning=EDAM["format_2064"]))
        setattr(cls, "edam:format_2065",
            PermissibleValue(
                text="edam:format_2065",
                title="Protein structure report (quality evaluation) format",
                description="Format of a report on the quality of a protein three-dimensional model.",
                meaning=EDAM["format_2065"]))
        setattr(cls, "edam:format_2066",
            PermissibleValue(
                text="edam:format_2066",
                title="Database hits (sequence) format",
                description="""Format of a report on sequence hits and associated data from searching a sequence database.""",
                meaning=EDAM["format_2066"]))
        setattr(cls, "edam:format_2067",
            PermissibleValue(
                text="edam:format_2067",
                title="Sequence distance matrix format",
                description="Format of a matrix of genetic distances between molecular sequences.",
                meaning=EDAM["format_2067"]))
        setattr(cls, "edam:format_2068",
            PermissibleValue(
                text="edam:format_2068",
                title="Sequence motif format",
                description="Format of a sequence motif.",
                meaning=EDAM["format_2068"]))
        setattr(cls, "edam:format_2069",
            PermissibleValue(
                text="edam:format_2069",
                title="Sequence profile format",
                description="Format of a sequence profile.",
                meaning=EDAM["format_2069"]))
        setattr(cls, "edam:format_2072",
            PermissibleValue(
                text="edam:format_2072",
                title="Hidden Markov model format",
                description="Format of a hidden Markov model.",
                meaning=EDAM["format_2072"]))
        setattr(cls, "edam:format_2074",
            PermissibleValue(
                text="edam:format_2074",
                title="Dirichlet distribution format",
                description="Data format of a dirichlet distribution.",
                meaning=EDAM["format_2074"]))
        setattr(cls, "edam:format_2075",
            PermissibleValue(
                text="edam:format_2075",
                title="HMM emission and transition counts format",
                description="Data format for the emission and transition counts of a hidden Markov model.",
                meaning=EDAM["format_2075"]))
        setattr(cls, "edam:format_2076",
            PermissibleValue(
                text="edam:format_2076",
                title="RNA secondary structure format",
                description="Format for secondary structure (predicted or real) of an RNA molecule.",
                meaning=EDAM["format_2076"]))
        setattr(cls, "edam:format_2077",
            PermissibleValue(
                text="edam:format_2077",
                title="Protein secondary structure format",
                description="Format for secondary structure (predicted or real) of a protein molecule.",
                meaning=EDAM["format_2077"]))
        setattr(cls, "edam:format_2078",
            PermissibleValue(
                text="edam:format_2078",
                title="Sequence range format",
                description="Format used to specify range(s) of sequence positions.",
                meaning=EDAM["format_2078"]))
        setattr(cls, "edam:format_2094",
            PermissibleValue(
                text="edam:format_2094",
                title="pure",
                description="""Alphabet for molecular sequence with possible unknown positions but without non-sequence characters.""",
                meaning=EDAM["format_2094"]))
        setattr(cls, "edam:format_2095",
            PermissibleValue(
                text="edam:format_2095",
                title="unpure",
                description="""Alphabet for a molecular sequence with possible unknown positions but possibly with non-sequence characters.""",
                meaning=EDAM["format_2095"]))
        setattr(cls, "edam:format_2096",
            PermissibleValue(
                text="edam:format_2096",
                title="unambiguous sequence",
                description="""Alphabet for a molecular sequence with possible unknown positions but without ambiguity characters.""",
                meaning=EDAM["format_2096"]))
        setattr(cls, "edam:format_2097",
            PermissibleValue(
                text="edam:format_2097",
                title="ambiguous",
                description="""Alphabet for a molecular sequence with possible unknown positions and possible ambiguity characters.""",
                meaning=EDAM["format_2097"]))
        setattr(cls, "edam:format_2155",
            PermissibleValue(
                text="edam:format_2155",
                title="Sequence features (repeats) format",
                description="Format used for map of repeats in molecular (typically nucleotide) sequences.",
                meaning=EDAM["format_2155"]))
        setattr(cls, "edam:format_2158",
            PermissibleValue(
                text="edam:format_2158",
                title="Nucleic acid features (restriction sites) format",
                description="""Format used for report on restriction enzyme recognition sites in nucleotide sequences.""",
                meaning=EDAM["format_2158"]))
        setattr(cls, "edam:format_2170",
            PermissibleValue(
                text="edam:format_2170",
                title="Sequence cluster format",
                description="Format used for clusters of molecular sequences.",
                meaning=EDAM["format_2170"]))
        setattr(cls, "edam:format_2171",
            PermissibleValue(
                text="edam:format_2171",
                title="Sequence cluster format (protein)",
                description="Format used for clusters of protein sequences.",
                meaning=EDAM["format_2171"]))
        setattr(cls, "edam:format_2172",
            PermissibleValue(
                text="edam:format_2172",
                title="Sequence cluster format (nucleic acid)",
                description="Format used for clusters of nucleotide sequences.",
                meaning=EDAM["format_2172"]))
        setattr(cls, "edam:format_2181",
            PermissibleValue(
                text="edam:format_2181",
                title="EMBL-like (text)",
                description="""A text format resembling EMBL entry format.
This concept may be used for the many non-standard EMBL-like text formats.""",
                meaning=EDAM["format_2181"]))
        setattr(cls, "edam:format_2182",
            PermissibleValue(
                text="edam:format_2182",
                title="FASTQ-like format (text)",
                description="""A text format resembling FASTQ short read format.
This concept may be used for non-standard FASTQ short read-like formats.""",
                meaning=EDAM["format_2182"]))
        setattr(cls, "edam:format_2183",
            PermissibleValue(
                text="edam:format_2183",
                title="EMBLXML",
                description="XML format for EMBL entries.",
                meaning=EDAM["format_2183"]))
        setattr(cls, "edam:format_2184",
            PermissibleValue(
                text="edam:format_2184",
                title="cdsxml",
                description="Specific XML format for EMBL entries (only uses certain sections).",
                meaning=EDAM["format_2184"]))
        setattr(cls, "edam:format_2185",
            PermissibleValue(
                text="edam:format_2185",
                title="INSDSeq",
                description="""INSDSeq provides the elements of a sequence as presented in the GenBank/EMBL/DDBJ-style flatfile formats, with a small amount of additional structure.""",
                meaning=EDAM["format_2185"]))
        setattr(cls, "edam:format_2186",
            PermissibleValue(
                text="edam:format_2186",
                title="geneseq",
                description="Geneseq sequence format.",
                meaning=EDAM["format_2186"]))
        setattr(cls, "edam:format_2187",
            PermissibleValue(
                text="edam:format_2187",
                title="UniProt-like (text)",
                description="A text sequence format resembling uniprotkb entry format.",
                meaning=EDAM["format_2187"]))
        setattr(cls, "edam:format_2194",
            PermissibleValue(
                text="edam:format_2194",
                title="medline",
                description="Abstract format used by MedLine database.",
                meaning=EDAM["format_2194"]))
        setattr(cls, "edam:format_2195",
            PermissibleValue(
                text="edam:format_2195",
                title="Ontology format",
                description="Format used for ontologies.",
                meaning=EDAM["format_2195"]))
        setattr(cls, "edam:format_2196",
            PermissibleValue(
                text="edam:format_2196",
                title="OBO format",
                description="A serialisation format conforming to the Open Biomedical Ontologies (OBO) model.",
                meaning=EDAM["format_2196"]))
        setattr(cls, "edam:format_2197",
            PermissibleValue(
                text="edam:format_2197",
                title="OWL format",
                description="A serialisation format conforming to the Web Ontology Language (OWL) model.",
                meaning=EDAM["format_2197"]))
        setattr(cls, "edam:format_2200",
            PermissibleValue(
                text="edam:format_2200",
                title="FASTA-like (text)",
                description="""A text format resembling FASTA format.
This concept may also be used for the many non-standard FASTA-like formats.""",
                meaning=EDAM["format_2200"]))
        setattr(cls, "edam:format_2204",
            PermissibleValue(
                text="edam:format_2204",
                title="EMBL format (XML)",
                description="""An XML format for EMBL entries.
This is a placeholder for other more specific concepts. It should not normally be used for annotation.""",
                meaning=EDAM["format_2204"]))
        setattr(cls, "edam:format_2205",
            PermissibleValue(
                text="edam:format_2205",
                title="GenBank-like format (text)",
                description="""A text format resembling GenBank entry (plain text) format.
This concept may be used for the non-standard GenBank-like text formats.""",
                meaning=EDAM["format_2205"]))
        setattr(cls, "edam:format_2206",
            PermissibleValue(
                text="edam:format_2206",
                title="Sequence feature table format (text)",
                description="Text format for a sequence feature table.",
                meaning=EDAM["format_2206"]))
        setattr(cls, "edam:format_2304",
            PermissibleValue(
                text="edam:format_2304",
                title="STRING entry format (XML)",
                description="Entry format (XML) for the STRING database of protein interaction.",
                meaning=EDAM["format_2304"]))
        setattr(cls, "edam:format_2305",
            PermissibleValue(
                text="edam:format_2305",
                title="GFF",
                description="GFF feature format (of indeterminate version).",
                meaning=EDAM["format_2305"]))
        setattr(cls, "edam:format_2306",
            PermissibleValue(
                text="edam:format_2306",
                title="GTF",
                description="Gene Transfer Format (GTF), a restricted version of GFF.",
                meaning=EDAM["format_2306"]))
        setattr(cls, "edam:format_2310",
            PermissibleValue(
                text="edam:format_2310",
                title="FASTA-HTML",
                description="FASTA format wrapped in HTML elements.",
                meaning=EDAM["format_2310"]))
        setattr(cls, "edam:format_2311",
            PermissibleValue(
                text="edam:format_2311",
                title="EMBL-HTML",
                description="EMBL entry format wrapped in HTML elements.",
                meaning=EDAM["format_2311"]))
        setattr(cls, "edam:format_2330",
            PermissibleValue(
                text="edam:format_2330",
                title="Textual format",
                description="""Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual).
Textual format.""",
                meaning=EDAM["format_2330"]))
        setattr(cls, "edam:format_2331",
            PermissibleValue(
                text="edam:format_2331",
                title="HTML",
                description="HTML format.",
                meaning=EDAM["format_2331"]))
        setattr(cls, "edam:format_2332",
            PermissibleValue(
                text="edam:format_2332",
                title="XML",
                description="""Data in XML format can be serialised into text, or binary format.
eXtensible Markup Language (XML) format.""",
                meaning=EDAM["format_2332"]))
        setattr(cls, "edam:format_2333",
            PermissibleValue(
                text="edam:format_2333",
                title="Binary format",
                description="""Binary format.
Only specific native binary formats are listed under 'Binary format' in EDAM. Generic binary formats - such as any data being zipped, or any XML data being serialised into the Efficient XML Interchange (EXI) format - are not modelled in EDAM. Refer to http://wsio.org/compression_004.""",
                meaning=EDAM["format_2333"]))
        setattr(cls, "edam:format_2350",
            PermissibleValue(
                text="edam:format_2350",
                title="Format (by type of data)",
                description="""A placeholder concept for visual navigation by dividing data formats by the content of the data that is represented.
This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. The concept branch under 'Format (typed)' provides an alternative organisation of the concepts nested under the other top-level branches ('Binary', 'HTML', 'RDF', 'Text' and 'XML'. All concepts under here are already included under those branches.""",
                meaning=EDAM["format_2350"]))
        setattr(cls, "edam:format_2352",
            PermissibleValue(
                text="edam:format_2352",
                title="BioXSD (XML)",
                description="""'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioXSD in XML' is the XML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.
BioXSD-schema-based XML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, Web services, and object-oriented programming.""",
                meaning=EDAM["format_2352"]))
        setattr(cls, "edam:format_2376",
            PermissibleValue(
                text="edam:format_2376",
                title="RDF format",
                description="A serialisation format conforming to the Resource Description Framework (RDF) model.",
                meaning=EDAM["format_2376"]))
        setattr(cls, "edam:format_2532",
            PermissibleValue(
                text="edam:format_2532",
                title="GenBank-HTML",
                description="Genbank entry format wrapped in HTML elements.",
                meaning=EDAM["format_2532"]))
        setattr(cls, "edam:format_2543",
            PermissibleValue(
                text="edam:format_2543",
                title="EMBL-like format",
                description="""A format resembling EMBL entry (plain text) format.
This concept may be used for the many non-standard EMBL-like formats.""",
                meaning=EDAM["format_2543"]))
        setattr(cls, "edam:format_2545",
            PermissibleValue(
                text="edam:format_2545",
                title="FASTQ-like format",
                description="""A format resembling FASTQ short read format.
This concept may be used for non-standard FASTQ short read-like formats.""",
                meaning=EDAM["format_2545"]))
        setattr(cls, "edam:format_2546",
            PermissibleValue(
                text="edam:format_2546",
                title="FASTA-like",
                description="""A format resembling FASTA format.
This concept may be used for the many non-standard FASTA-like formats.""",
                meaning=EDAM["format_2546"]))
        setattr(cls, "edam:format_2547",
            PermissibleValue(
                text="edam:format_2547",
                title="uniprotkb-like format",
                description="A sequence format resembling uniprotkb entry format.",
                meaning=EDAM["format_2547"]))
        setattr(cls, "edam:format_2548",
            PermissibleValue(
                text="edam:format_2548",
                title="Sequence feature table format",
                description="Format for a sequence feature table.",
                meaning=EDAM["format_2548"]))
        setattr(cls, "edam:format_2549",
            PermissibleValue(
                text="edam:format_2549",
                title="OBO",
                description="OBO ontology text format.",
                meaning=EDAM["format_2549"]))
        setattr(cls, "edam:format_2550",
            PermissibleValue(
                text="edam:format_2550",
                title="OBO-XML",
                description="OBO ontology XML format.",
                meaning=EDAM["format_2550"]))
        setattr(cls, "edam:format_2551",
            PermissibleValue(
                text="edam:format_2551",
                title="Sequence record format (text)",
                description="Data format for a molecular sequence record (text).",
                meaning=EDAM["format_2551"]))
        setattr(cls, "edam:format_2552",
            PermissibleValue(
                text="edam:format_2552",
                title="Sequence record format (XML)",
                description="Data format for a molecular sequence record (XML).",
                meaning=EDAM["format_2552"]))
        setattr(cls, "edam:format_2553",
            PermissibleValue(
                text="edam:format_2553",
                title="Sequence feature table format (XML)",
                description="XML format for a sequence feature table.",
                meaning=EDAM["format_2553"]))
        setattr(cls, "edam:format_2554",
            PermissibleValue(
                text="edam:format_2554",
                title="Alignment format (text)",
                description="Text format for molecular sequence alignment information.",
                meaning=EDAM["format_2554"]))
        setattr(cls, "edam:format_2555",
            PermissibleValue(
                text="edam:format_2555",
                title="Alignment format (XML)",
                description="XML format for molecular sequence alignment information.",
                meaning=EDAM["format_2555"]))
        setattr(cls, "edam:format_2556",
            PermissibleValue(
                text="edam:format_2556",
                title="Phylogenetic tree format (text)",
                description="Text format for a phylogenetic tree.",
                meaning=EDAM["format_2556"]))
        setattr(cls, "edam:format_2557",
            PermissibleValue(
                text="edam:format_2557",
                title="Phylogenetic tree format (XML)",
                description="XML format for a phylogenetic tree.",
                meaning=EDAM["format_2557"]))
        setattr(cls, "edam:format_2558",
            PermissibleValue(
                text="edam:format_2558",
                title="EMBL-like (XML)",
                description="""An XML format resembling EMBL entry format.
This concept may be used for the any non-standard EMBL-like XML formats.""",
                meaning=EDAM["format_2558"]))
        setattr(cls, "edam:format_2559",
            PermissibleValue(
                text="edam:format_2559",
                title="GenBank-like format",
                description="""A format resembling GenBank entry (plain text) format.
This concept may be used for the non-standard GenBank-like formats.""",
                meaning=EDAM["format_2559"]))
        setattr(cls, "edam:format_2561",
            PermissibleValue(
                text="edam:format_2561",
                title="Sequence assembly format (text)",
                description="Text format for sequence assembly data.",
                meaning=EDAM["format_2561"]))
        setattr(cls, "edam:format_2566",
            PermissibleValue(
                text="edam:format_2566",
                title="completely unambiguous",
                description="""Alphabet for a molecular sequence without any unknown positions or ambiguity characters.""",
                meaning=EDAM["format_2566"]))
        setattr(cls, "edam:format_2567",
            PermissibleValue(
                text="edam:format_2567",
                title="completely unambiguous pure",
                description="""Alphabet for a molecular sequence without unknown positions, ambiguity or non-sequence characters.""",
                meaning=EDAM["format_2567"]))
        setattr(cls, "edam:format_2568",
            PermissibleValue(
                text="edam:format_2568",
                title="completely unambiguous pure nucleotide",
                description="""Alphabet for a nucleotide sequence (characters ACGTU only) without unknown positions, ambiguity or non-sequence characters .""",
                meaning=EDAM["format_2568"]))
        setattr(cls, "edam:format_2569",
            PermissibleValue(
                text="edam:format_2569",
                title="completely unambiguous pure dna",
                description="""Alphabet for a DNA sequence (characters ACGT only) without unknown positions, ambiguity or non-sequence characters.""",
                meaning=EDAM["format_2569"]))
        setattr(cls, "edam:format_2570",
            PermissibleValue(
                text="edam:format_2570",
                title="completely unambiguous pure rna sequence",
                description="""Alphabet for an RNA sequence (characters ACGU only) without unknown positions, ambiguity or non-sequence characters.""",
                meaning=EDAM["format_2570"]))
        setattr(cls, "edam:format_2571",
            PermissibleValue(
                text="edam:format_2571",
                title="Raw sequence format",
                description="Format of a raw molecular sequence (i.e. the alphabet used).",
                meaning=EDAM["format_2571"]))
        setattr(cls, "edam:format_2572",
            PermissibleValue(
                text="edam:format_2572",
                title="BAM",
                description="""BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.""",
                meaning=EDAM["format_2572"]))
        setattr(cls, "edam:format_2573",
            PermissibleValue(
                text="edam:format_2573",
                title="SAM",
                description="""Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
The format supports short and long reads (up to 128Mbp) produced by different sequencing platforms and is used to hold mapped data within the GATK and across the Broad Institute, the Sanger Centre, and throughout the 1000 Genomes project.""",
                meaning=EDAM["format_2573"]))
        setattr(cls, "edam:format_2585",
            PermissibleValue(
                text="edam:format_2585",
                title="SBML",
                description="""Systems Biology Markup Language (SBML), the standard XML format for models of biological processes such as for example metabolism, cell signaling, and gene regulation.""",
                meaning=EDAM["format_2585"]))
        setattr(cls, "edam:format_2607",
            PermissibleValue(
                text="edam:format_2607",
                title="completely unambiguous pure protein",
                description="""Alphabet for any protein sequence without unknown positions, ambiguity or non-sequence characters.""",
                meaning=EDAM["format_2607"]))
        setattr(cls, "edam:format_2848",
            PermissibleValue(
                text="edam:format_2848",
                title="Bibliographic reference format",
                description="Format of a bibliographic reference.",
                meaning=EDAM["format_2848"]))
        setattr(cls, "edam:format_2919",
            PermissibleValue(
                text="edam:format_2919",
                title="Sequence annotation track format",
                description="Format of a sequence annotation track.",
                meaning=EDAM["format_2919"]))
        setattr(cls, "edam:format_2920",
            PermissibleValue(
                text="edam:format_2920",
                title="Alignment format (pair only)",
                description="""Data format for molecular sequence alignment information that can hold sequence alignment(s) of only 2 sequences.""",
                meaning=EDAM["format_2920"]))
        setattr(cls, "edam:format_2921",
            PermissibleValue(
                text="edam:format_2921",
                title="Sequence variation annotation format",
                description="Format of sequence variation annotation.",
                meaning=EDAM["format_2921"]))
        setattr(cls, "edam:format_2922",
            PermissibleValue(
                text="edam:format_2922",
                title="markx0 variant",
                description="Some variant of Pearson MARKX alignment format.",
                meaning=EDAM["format_2922"]))
        setattr(cls, "edam:format_2923",
            PermissibleValue(
                text="edam:format_2923",
                title="mega variant",
                description="Some variant of Mega format for (typically aligned) sequences.",
                meaning=EDAM["format_2923"]))
        setattr(cls, "edam:format_2924",
            PermissibleValue(
                text="edam:format_2924",
                title="Phylip format variant",
                description="Some variant of Phylip format for (aligned) sequences.",
                meaning=EDAM["format_2924"]))
        setattr(cls, "edam:format_3000",
            PermissibleValue(
                text="edam:format_3000",
                title="AB1",
                description="""AB1 binary format of raw DNA sequence reads (output of Applied Biosystems' sequencing analysis software). Contains an electropherogram and the DNA base sequence.
AB1 uses the generic binary Applied Biosystems, Inc. Format (ABIF).""",
                meaning=EDAM["format_3000"]))
        setattr(cls, "edam:format_3001",
            PermissibleValue(
                text="edam:format_3001",
                title="ACE",
                description="""ACE sequence assembly format including contigs, base-call qualities, and other metadata (version Aug 1998 and onwards).""",
                meaning=EDAM["format_3001"]))
        setattr(cls, "edam:format_3003",
            PermissibleValue(
                text="edam:format_3003",
                title="BED",
                description="""BED detail format includes 2 additional columns (http://genome.ucsc.edu/FAQ/FAQformat#format1.7) and BED 15 includes 3 additional columns for experiment scores (http://genomewiki.ucsc.edu/index.php/Microarray_track).
Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser.""",
                meaning=EDAM["format_3003"]))
        setattr(cls, "edam:format_3004",
            PermissibleValue(
                text="edam:format_3004",
                title="bigBed",
                description="bigBed format for large sequence annotation tracks, similar to textual BED format.",
                meaning=EDAM["format_3004"]))
        setattr(cls, "edam:format_3005",
            PermissibleValue(
                text="edam:format_3005",
                title="WIG",
                description="""Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser.""",
                meaning=EDAM["format_3005"]))
        setattr(cls, "edam:format_3006",
            PermissibleValue(
                text="edam:format_3006",
                title="bigWig",
                description="""bigWig format for large sequence annotation tracks that consist of a value for each sequence position. Similar to textual WIG format.""",
                meaning=EDAM["format_3006"]))
        setattr(cls, "edam:format_3007",
            PermissibleValue(
                text="edam:format_3007",
                title="PSL",
                description="""PSL format of alignments, typically generated by BLAT or psLayout. Can be displayed in a genome browser like a sequence annotation track.""",
                meaning=EDAM["format_3007"]))
        setattr(cls, "edam:format_3008",
            PermissibleValue(
                text="edam:format_3008",
                title="MAF",
                description="""Multiple Alignment Format (MAF) supporting alignments of whole genomes with rearrangements, directions, multiple pieces to the alignment, and so forth.
Typically generated by Multiz and TBA aligners; can be displayed in a genome browser like a sequence annotation track. This should not be confused with MIRA Assembly Format or Mutation Annotation Format.""",
                meaning=EDAM["format_3008"]))
        setattr(cls, "edam:format_3009",
            PermissibleValue(
                text="edam:format_3009",
                title="2bit",
                description="""2bit binary format of nucleotide sequences using 2 bits per nucleotide. In addition encodes unknown nucleotides and lower-case 'masking'.""",
                meaning=EDAM["format_3009"]))
        setattr(cls, "edam:format_3010",
            PermissibleValue(
                text="edam:format_3010",
                title=".nib",
                description=""".nib (nibble) binary format of a nucleotide sequence using 4 bits per nucleotide (including unknown) and its lower-case 'masking'.""",
                meaning=EDAM["format_3010"]))
        setattr(cls, "edam:format_3011",
            PermissibleValue(
                text="edam:format_3011",
                title="genePred",
                description="""genePred format has 3 main variations (http://genome.ucsc.edu/FAQ/FAQformat#format9 http://www.broadinstitute.org/software/igv/genePred). They reflect UCSC Browser DB tables.
genePred table format for gene prediction tracks.""",
                meaning=EDAM["format_3011"]))
        setattr(cls, "edam:format_3012",
            PermissibleValue(
                text="edam:format_3012",
                title="pgSnp",
                description="""Personal Genome SNP (pgSnp) format for sequence variation tracks (indels and polymorphisms), supported by the UCSC Genome Browser.""",
                meaning=EDAM["format_3012"]))
        setattr(cls, "edam:format_3013",
            PermissibleValue(
                text="edam:format_3013",
                title="axt",
                description="axt format of alignments, typically produced from BLASTZ.",
                meaning=EDAM["format_3013"]))
        setattr(cls, "edam:format_3014",
            PermissibleValue(
                text="edam:format_3014",
                title="LAV",
                description="LAV format of alignments generated by BLASTZ and LASTZ.",
                meaning=EDAM["format_3014"]))
        setattr(cls, "edam:format_3015",
            PermissibleValue(
                text="edam:format_3015",
                title="Pileup",
                description="""Pileup format of alignment of sequences (e.g. sequencing reads) to (a) reference sequence(s). Contains aligned bases per base of the reference sequence(s).""",
                meaning=EDAM["format_3015"]))
        setattr(cls, "edam:format_3016",
            PermissibleValue(
                text="edam:format_3016",
                title="VCF",
                description="""1000 Genomes Project has its own specification for encoding structural variations in VCF (https://www.internationalgenome.org/wiki/Analysis/Variant%20Call%20Format/VCF%20(Variant%20Call%20Format)%20version%204.0/encoding-structural-variants). This is based on VCF version 4.0 and not directly compatible with VCF version 4.3.
Variant Call Format (VCF) is tabular format for storing genomic sequence variations.""",
                meaning=EDAM["format_3016"]))
        setattr(cls, "edam:format_3017",
            PermissibleValue(
                text="edam:format_3017",
                title="SRF",
                description="""Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive.""",
                meaning=EDAM["format_3017"]))
        setattr(cls, "edam:format_3018",
            PermissibleValue(
                text="edam:format_3018",
                title="ZTR",
                description="ZTR format for storing chromatogram data from DNA sequencing instruments.",
                meaning=EDAM["format_3018"]))
        setattr(cls, "edam:format_3019",
            PermissibleValue(
                text="edam:format_3019",
                title="GVF",
                description="""Genome Variation Format (GVF). A GFF3-compatible format with defined header and attribute tags for sequence variation.""",
                meaning=EDAM["format_3019"]))
        setattr(cls, "edam:format_3020",
            PermissibleValue(
                text="edam:format_3020",
                title="BCF",
                description="""BCF is the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation).""",
                meaning=EDAM["format_3020"]))
        setattr(cls, "edam:format_3033",
            PermissibleValue(
                text="edam:format_3033",
                title="Matrix format",
                description="Format of a matrix (array) of numerical values.",
                meaning=EDAM["format_3033"]))
        setattr(cls, "edam:format_3097",
            PermissibleValue(
                text="edam:format_3097",
                title="Protein domain classification format",
                description="""Format of data concerning the classification of the sequences and/or structures of protein structural domain(s).""",
                meaning=EDAM["format_3097"]))
        setattr(cls, "edam:format_3098",
            PermissibleValue(
                text="edam:format_3098",
                title="Raw SCOP domain classification format",
                description="""Format of raw SCOP domain classification data files.
These are the parsable data files provided by SCOP.""",
                meaning=EDAM["format_3098"]))
        setattr(cls, "edam:format_3099",
            PermissibleValue(
                text="edam:format_3099",
                title="Raw CATH domain classification format",
                description="""Format of raw CATH domain classification data files.
These are the parsable data files provided by CATH.""",
                meaning=EDAM["format_3099"]))
        setattr(cls, "edam:format_3100",
            PermissibleValue(
                text="edam:format_3100",
                title="CATH domain report format",
                description="""Format of summary of domain classification information for a CATH domain.
The report (for example http://www.cathdb.info/domain/1cukA01) includes CATH codes for levels in the hierarchy for the domain, level descriptions and relevant data and links.""",
                meaning=EDAM["format_3100"]))
        setattr(cls, "edam:format_3155",
            PermissibleValue(
                text="edam:format_3155",
                title="SBRML",
                description="""Systems Biology Result Markup Language (SBRML), the standard XML format for simulated or calculated results (e.g. trajectories) of systems biology models.""",
                meaning=EDAM["format_3155"]))
        setattr(cls, "edam:format_3156",
            PermissibleValue(
                text="edam:format_3156",
                title="BioPAX",
                description="BioPAX is an exchange format for pathway data, with its data model defined in OWL.",
                meaning=EDAM["format_3156"]))
        setattr(cls, "edam:format_3157",
            PermissibleValue(
                text="edam:format_3157",
                title="EBI Application Result XML",
                description="""EBI Application Result XML is a format returned by sequence similarity search Web services at EBI.""",
                meaning=EDAM["format_3157"]))
        setattr(cls, "edam:format_3158",
            PermissibleValue(
                text="edam:format_3158",
                title="PSI MI XML (MIF)",
                description="XML Molecular Interaction Format (MIF), standardised by HUPO PSI MI.",
                meaning=EDAM["format_3158"]))
        setattr(cls, "edam:format_3159",
            PermissibleValue(
                text="edam:format_3159",
                title="phyloXML",
                description="""phyloXML is a standardised XML format for phylogenetic trees, networks, and associated data.""",
                meaning=EDAM["format_3159"]))
        setattr(cls, "edam:format_3160",
            PermissibleValue(
                text="edam:format_3160",
                title="NeXML",
                description="NeXML is a standardised XML format for rich phyloinformatic data.",
                meaning=EDAM["format_3160"]))
        setattr(cls, "edam:format_3161",
            PermissibleValue(
                text="edam:format_3161",
                title="MAGE-ML",
                description="MAGE-ML XML format for microarray expression data, standardised by MGED (now FGED).",
                meaning=EDAM["format_3161"]))
        setattr(cls, "edam:format_3162",
            PermissibleValue(
                text="edam:format_3162",
                title="MAGE-TAB",
                description="""MAGE-TAB textual format for microarray expression data, standardised by MGED (now FGED).""",
                meaning=EDAM["format_3162"]))
        setattr(cls, "edam:format_3163",
            PermissibleValue(
                text="edam:format_3163",
                title="GCDML",
                description="""GCDML XML format for genome and metagenome metadata according to MIGS/MIMS/MIMARKS information standards, standardised by the Genomic Standards Consortium (GSC).""",
                meaning=EDAM["format_3163"]))
        setattr(cls, "edam:format_3164",
            PermissibleValue(
                text="edam:format_3164",
                title="GTrack",
                description="""'GTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GTrack' is the tabular format for representing features of sequences and genomes.
GTrack is a generic and optimised tabular format for genome or sequence feature tracks. GTrack unifies the power of other track formats (e.g. GFF3, BED, WIG), and while optimised in size, adds more flexibility, customisation, and automation (\"machine understandability\").""",
                meaning=EDAM["format_3164"]))
        setattr(cls, "edam:format_3166",
            PermissibleValue(
                text="edam:format_3166",
                title="Biological pathway or network report format",
                description="Data format for a report of information derived from a biological pathway or network.",
                meaning=EDAM["format_3166"]))
        setattr(cls, "edam:format_3167",
            PermissibleValue(
                text="edam:format_3167",
                title="Experiment annotation format",
                description="Data format for annotation on a laboratory experiment.",
                meaning=EDAM["format_3167"]))
        setattr(cls, "edam:format_3235",
            PermissibleValue(
                text="edam:format_3235",
                title="Cytoband format",
                description="""Cytoband format for chromosome cytobands.
Reflects a UCSC Browser DB table.""",
                meaning=EDAM["format_3235"]))
        setattr(cls, "edam:format_3239",
            PermissibleValue(
                text="edam:format_3239",
                title="CopasiML",
                description="CopasiML, the native format of COPASI.",
                meaning=EDAM["format_3239"]))
        setattr(cls, "edam:format_3240",
            PermissibleValue(
                text="edam:format_3240",
                title="CellML",
                description="CellML, the format for mathematical models of biological and other networks.",
                meaning=EDAM["format_3240"]))
        setattr(cls, "edam:format_3242",
            PermissibleValue(
                text="edam:format_3242",
                title="PSI MI TAB (MITAB)",
                description="Tabular Molecular Interaction format (MITAB), standardised by HUPO PSI MI.",
                meaning=EDAM["format_3242"]))
        setattr(cls, "edam:format_3243",
            PermissibleValue(
                text="edam:format_3243",
                title="PSI-PAR",
                description="""Protein affinity format (PSI-PAR), standardised by HUPO PSI MI. It is compatible with PSI MI XML (MIF) and uses the same XML Schema.""",
                meaning=EDAM["format_3243"]))
        setattr(cls, "edam:format_3244",
            PermissibleValue(
                text="edam:format_3244",
                title="mzML",
                description="""mzML format for raw spectrometer output data, standardised by HUPO PSI MSS.
mzML is the successor and unifier of the mzData format developed by PSI and mzXML developed at the Seattle Proteome Center.""",
                meaning=EDAM["format_3244"]))
        setattr(cls, "edam:format_3245",
            PermissibleValue(
                text="edam:format_3245",
                title="Mass spectrometry data format",
                description="Format for mass pectra and derived data, include peptide sequences etc.",
                meaning=EDAM["format_3245"]))
        setattr(cls, "edam:format_3246",
            PermissibleValue(
                text="edam:format_3246",
                title="TraML",
                description="""TraML (Transition Markup Language) is the format for mass spectrometry transitions, standardised by HUPO PSI MSS.""",
                meaning=EDAM["format_3246"]))
        setattr(cls, "edam:format_3247",
            PermissibleValue(
                text="edam:format_3247",
                title="mzIdentML",
                description="""mzIdentML is the exchange format for peptides and proteins identified from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of proteomics search engines.""",
                meaning=EDAM["format_3247"]))
        setattr(cls, "edam:format_3248",
            PermissibleValue(
                text="edam:format_3248",
                title="mzQuantML",
                description="""mzQuantML is the format for quantitation values associated with peptides, proteins and small molecules from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of quantitation software for proteomics.""",
                meaning=EDAM["format_3248"]))
        setattr(cls, "edam:format_3249",
            PermissibleValue(
                text="edam:format_3249",
                title="GelML",
                description="""GelML is the format for describing the process of gel electrophoresis, standardised by HUPO PSI PS.""",
                meaning=EDAM["format_3249"]))
        setattr(cls, "edam:format_3250",
            PermissibleValue(
                text="edam:format_3250",
                title="spML",
                description="""spML is the format for describing proteomics sample processing, other than using gels, prior to mass spectrometric protein identification, standardised by HUPO PSI PS. It may also be applicable for metabolomics.""",
                meaning=EDAM["format_3250"]))
        setattr(cls, "edam:format_3252",
            PermissibleValue(
                text="edam:format_3252",
                title="OWL Functional Syntax",
                description="A human-readable encoding for the Web Ontology Language (OWL).",
                meaning=EDAM["format_3252"]))
        setattr(cls, "edam:format_3253",
            PermissibleValue(
                text="edam:format_3253",
                title="Manchester OWL Syntax",
                description="""A syntax for writing OWL class expressions.
This format was influenced by the OWL Abstract Syntax and the DL style syntax.""",
                meaning=EDAM["format_3253"]))
        setattr(cls, "edam:format_3254",
            PermissibleValue(
                text="edam:format_3254",
                title="KRSS2 Syntax",
                description="""A superset of the \"Description-Logic Knowledge Representation System Specification from the KRSS Group of the ARPA Knowledge Sharing Effort\".
This format is used in Protege 4.""",
                meaning=EDAM["format_3254"]))
        setattr(cls, "edam:format_3255",
            PermissibleValue(
                text="edam:format_3255",
                title="Turtle",
                description="""The SPARQL Query Language incorporates a very similar syntax.
The Terse RDF Triple Language (Turtle) is a human-friendly serialisation format for RDF (Resource Description Framework) graphs.""",
                meaning=EDAM["format_3255"]))
        setattr(cls, "edam:format_3256",
            PermissibleValue(
                text="edam:format_3256",
                title="N-Triples",
                description="""A plain text serialisation format for RDF (Resource Description Framework) graphs, and a subset of the Turtle (Terse RDF Triple Language) format.
N-Triples should not be confused with Notation 3 which is a superset of Turtle.""",
                meaning=EDAM["format_3256"]))
        setattr(cls, "edam:format_3257",
            PermissibleValue(
                text="edam:format_3257",
                title="Notation3",
                description="""A shorthand non-XML serialisation of Resource Description Framework model, designed with human-readability in mind.""",
                meaning=EDAM["format_3257"]))
        setattr(cls, "edam:format_3261",
            PermissibleValue(
                text="edam:format_3261",
                title="RDF/XML",
                description="""RDF/XML can be used as a standard serialisation syntax for OWL DL, but not for OWL Full.
Resource Description Framework (RDF) XML format.""",
                meaning=EDAM["format_3261"]))
        setattr(cls, "edam:format_3262",
            PermissibleValue(
                text="edam:format_3262",
                title="OWL/XML",
                description="OWL ontology XML serialisation format.",
                meaning=EDAM["format_3262"]))
        setattr(cls, "edam:format_3281",
            PermissibleValue(
                text="edam:format_3281",
                title="A2M",
                description="""The A2M format is used as the primary format for multiple alignments of protein or nucleic-acid sequences in the SAM suite of tools. It is a small modification of FASTA format for sequences and is compatible with most tools that read FASTA.""",
                meaning=EDAM["format_3281"]))
        setattr(cls, "edam:format_3284",
            PermissibleValue(
                text="edam:format_3284",
                title="SFF",
                description="""Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing.""",
                meaning=EDAM["format_3284"]))
        setattr(cls, "edam:format_3285",
            PermissibleValue(
                text="edam:format_3285",
                title="MAP",
                description="The MAP file describes SNPs and is used by the Plink package.",
                meaning=EDAM["format_3285"]))
        setattr(cls, "edam:format_3286",
            PermissibleValue(
                text="edam:format_3286",
                title="PED",
                description="The PED file describes individuals and genetic data and is used by the Plink package.",
                meaning=EDAM["format_3286"]))
        setattr(cls, "edam:format_3287",
            PermissibleValue(
                text="edam:format_3287",
                title="Individual genetic data format",
                description="Data format for a metadata on an individual and their genetic data.",
                meaning=EDAM["format_3287"]))
        setattr(cls, "edam:format_3288",
            PermissibleValue(
                text="edam:format_3288",
                title="PED/MAP",
                description="The PED/MAP file describes data used by the Plink package.",
                meaning=EDAM["format_3288"]))
        setattr(cls, "edam:format_3309",
            PermissibleValue(
                text="edam:format_3309",
                title="CT",
                description="File format of a CT (Connectivity Table) file from the RNAstructure package.",
                meaning=EDAM["format_3309"]))
        setattr(cls, "edam:format_3310",
            PermissibleValue(
                text="edam:format_3310",
                title="SS",
                description="XRNA old input style format.",
                meaning=EDAM["format_3310"]))
        setattr(cls, "edam:format_3311",
            PermissibleValue(
                text="edam:format_3311",
                title="RNAML",
                description="RNA Markup Language.",
                meaning=EDAM["format_3311"]))
        setattr(cls, "edam:format_3312",
            PermissibleValue(
                text="edam:format_3312",
                title="GDE",
                description="Format for the Genetic Data Environment (GDE).",
                meaning=EDAM["format_3312"]))
        setattr(cls, "edam:format_3313",
            PermissibleValue(
                text="edam:format_3313",
                title="BLC",
                description="""A multiple alignment in vertical format, as used in the AMPS (Alignment of Multiple Protein Sequences) package.""",
                meaning=EDAM["format_3313"]))
        setattr(cls, "edam:format_3326",
            PermissibleValue(
                text="edam:format_3326",
                title="Data index format",
                description="Format of a data index of some type.",
                meaning=EDAM["format_3326"]))
        setattr(cls, "edam:format_3327",
            PermissibleValue(
                text="edam:format_3327",
                title="BAI",
                description="BAM indexing format.",
                meaning=EDAM["format_3327"]))
        setattr(cls, "edam:format_3328",
            PermissibleValue(
                text="edam:format_3328",
                title="HMMER2",
                description="HMMER profile HMM file for HMMER versions 2.x.",
                meaning=EDAM["format_3328"]))
        setattr(cls, "edam:format_3329",
            PermissibleValue(
                text="edam:format_3329",
                title="HMMER3",
                description="HMMER profile HMM file for HMMER versions 3.x.",
                meaning=EDAM["format_3329"]))
        setattr(cls, "edam:format_3330",
            PermissibleValue(
                text="edam:format_3330",
                title="PO",
                description="""PO is the output format of Partial Order Alignment program (POA) performing Multiple Sequence Alignment (MSA).""",
                meaning=EDAM["format_3330"]))
        setattr(cls, "edam:format_3331",
            PermissibleValue(
                text="edam:format_3331",
                title="BLAST XML results format",
                description="XML format as produced by the NCBI Blast package.",
                meaning=EDAM["format_3331"]))
        setattr(cls, "edam:format_3462",
            PermissibleValue(
                text="edam:format_3462",
                title="CRAM",
                description="Reference-based compression of alignment format.",
                meaning=EDAM["format_3462"]))
        setattr(cls, "edam:format_3464",
            PermissibleValue(
                text="edam:format_3464",
                title="JSON",
                description="""JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.""",
                meaning=EDAM["format_3464"]))
        setattr(cls, "edam:format_3466",
            PermissibleValue(
                text="edam:format_3466",
                title="EPS",
                description="Encapsulated PostScript format.",
                meaning=EDAM["format_3466"]))
        setattr(cls, "edam:format_3467",
            PermissibleValue(
                text="edam:format_3467",
                title="GIF",
                description="Graphics Interchange Format.",
                meaning=EDAM["format_3467"]))
        setattr(cls, "edam:format_3468",
            PermissibleValue(
                text="edam:format_3468",
                title="xls",
                description="Microsoft Excel spreadsheet format.",
                meaning=EDAM["format_3468"]))
        setattr(cls, "edam:format_3475",
            PermissibleValue(
                text="edam:format_3475",
                title="TSV",
                description="Tabular data represented as tab-separated values in a text file.",
                meaning=EDAM["format_3475"]))
        setattr(cls, "edam:format_3477",
            PermissibleValue(
                text="edam:format_3477",
                title="Cytoscape input file format",
                description="""Format of the cytoscape input file of gene expression ratios or values are specified over one or more experiments.""",
                meaning=EDAM["format_3477"]))
        setattr(cls, "edam:format_3484",
            PermissibleValue(
                text="edam:format_3484",
                title="ebwt",
                description="Bowtie format for indexed reference genome for \"small\" genomes.",
                meaning=EDAM["format_3484"]))
        setattr(cls, "edam:format_3485",
            PermissibleValue(
                text="edam:format_3485",
                title="RSF",
                description="""RSF-format files contain one or more sequences that may or may not be related. In addition to the sequence data, each sequence can be annotated with descriptive sequence information (from the GCG manual).
Rich sequence format.""",
                meaning=EDAM["format_3485"]))
        setattr(cls, "edam:format_3486",
            PermissibleValue(
                text="edam:format_3486",
                title="GCG format variant",
                description="Some format based on the GCG format.",
                meaning=EDAM["format_3486"]))
        setattr(cls, "edam:format_3487",
            PermissibleValue(
                text="edam:format_3487",
                title="BSML",
                description="Bioinformatics Sequence Markup Language format.",
                meaning=EDAM["format_3487"]))
        setattr(cls, "edam:format_3491",
            PermissibleValue(
                text="edam:format_3491",
                title="ebwtl",
                description="Bowtie format for indexed reference genome for \"large\" genomes.",
                meaning=EDAM["format_3491"]))
        setattr(cls, "edam:format_3499",
            PermissibleValue(
                text="edam:format_3499",
                title="Ensembl variation file format",
                description="Ensembl standard format for variation data.",
                meaning=EDAM["format_3499"]))
        setattr(cls, "edam:format_3506",
            PermissibleValue(
                text="edam:format_3506",
                title="docx",
                description="Microsoft Word format.",
                meaning=EDAM["format_3506"]))
        setattr(cls, "edam:format_3507",
            PermissibleValue(
                text="edam:format_3507",
                title="Document format",
                description="Format of documents including word processor, spreadsheet and presentation.",
                meaning=EDAM["format_3507"]))
        setattr(cls, "edam:format_3508",
            PermissibleValue(
                text="edam:format_3508",
                title="PDF",
                description="Portable Document Format.",
                meaning=EDAM["format_3508"]))
        setattr(cls, "edam:format_3547",
            PermissibleValue(
                text="edam:format_3547",
                title="Image format",
                description="Format used for images and image metadata.",
                meaning=EDAM["format_3547"]))
        setattr(cls, "edam:format_3548",
            PermissibleValue(
                text="edam:format_3548",
                title="DICOM format",
                description="""Medical image format corresponding to the Digital Imaging and Communications in Medicine (DICOM) standard.""",
                meaning=EDAM["format_3548"]))
        setattr(cls, "edam:format_3549",
            PermissibleValue(
                text="edam:format_3549",
                title="nii",
                description="""An open file format from the Neuroimaging Informatics Technology Initiative (NIfTI) commonly used to store brain imaging data obtained using Magnetic Resonance Imaging (MRI) methods.""",
                meaning=EDAM["format_3549"]))
        setattr(cls, "edam:format_3550",
            PermissibleValue(
                text="edam:format_3550",
                title="mhd",
                description="""Text-based tagged file format for medical images generated using the MetaImage software package.""",
                meaning=EDAM["format_3550"]))
        setattr(cls, "edam:format_3551",
            PermissibleValue(
                text="edam:format_3551",
                title="nrrd",
                description="""Nearly Raw Rasta Data format designed to support scientific visualisation and image processing involving N-dimensional raster data.""",
                meaning=EDAM["format_3551"]))
        setattr(cls, "edam:format_3554",
            PermissibleValue(
                text="edam:format_3554",
                title="R file format",
                description="""File format used for scripts written in the R programming language for execution within the R software environment, typically for statistical computation and graphics.""",
                meaning=EDAM["format_3554"]))
        setattr(cls, "edam:format_3555",
            PermissibleValue(
                text="edam:format_3555",
                title="SPSS",
                description="File format used for scripts for the Statistical Package for the Social Sciences.",
                meaning=EDAM["format_3555"]))
        setattr(cls, "edam:format_3556",
            PermissibleValue(
                text="edam:format_3556",
                title="MHTML",
                description="""MHTML is not strictly an HTML format, it is encoded as an HTML email message (although with multipart/related instead of multipart/alternative). It, however, contains the main HTML block as its core, and thus it is for practical reasons included in EDAM as a specialisation of 'HTML'.
MIME HTML format for Web pages, which can include external resources, including images, Flash animations and so on.""",
                meaning=EDAM["format_3556"]))
        setattr(cls, "edam:format_3578",
            PermissibleValue(
                text="edam:format_3578",
                title="IDAT",
                description="""Proprietary file format for (raw) BeadArray data used by genomewide profiling platforms from Illumina Inc. This format is output directly from the scanner and stores summary intensities for each probe-type on an array.""",
                meaning=EDAM["format_3578"]))
        setattr(cls, "edam:format_3579",
            PermissibleValue(
                text="edam:format_3579",
                title="JPG",
                description="""Joint Picture Group file format for lossy graphics file.
Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type.""",
                meaning=EDAM["format_3579"]))
        setattr(cls, "edam:format_3580",
            PermissibleValue(
                text="edam:format_3580",
                title="rcc",
                description="""Reporter Code Count-A data file (.csv) output by the Nanostring nCounter Digital Analyzer, which contains gene sample information, probe information and probe counts.""",
                meaning=EDAM["format_3580"]))
        setattr(cls, "edam:format_3581",
            PermissibleValue(
                text="edam:format_3581",
                title="arff",
                description="""ARFF (Attribute-Relation File Format) is an ASCII text file format that describes a list of instances sharing a set of attributes.
This file format is for machine learning.""",
                meaning=EDAM["format_3581"]))
        setattr(cls, "edam:format_3582",
            PermissibleValue(
                text="edam:format_3582",
                title="afg",
                description="""AFG is a single text-based file assembly format that holds read and consensus information together.""",
                meaning=EDAM["format_3582"]))
        setattr(cls, "edam:format_3583",
            PermissibleValue(
                text="edam:format_3583",
                title="bedgraph",
                description="""Holds a tab-delimited chromosome /start /end / datavalue dataset.
The bedGraph format allows display of continuous-valued data in track format. This display type is useful for probability scores and transcriptome data.""",
                meaning=EDAM["format_3583"]))
        setattr(cls, "edam:format_3584",
            PermissibleValue(
                text="edam:format_3584",
                title="bedstrict",
                description="""Browser Extensible Data (BED) format of sequence annotation track that strictly does not contain non-standard fields beyond the first 3 columns.
Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not.""",
                meaning=EDAM["format_3584"]))
        setattr(cls, "edam:format_3585",
            PermissibleValue(
                text="edam:format_3585",
                title="bed6",
                description="""BED file format where each feature is described by chromosome, start, end, name, score, and strand.
Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 6""",
                meaning=EDAM["format_3585"]))
        setattr(cls, "edam:format_3586",
            PermissibleValue(
                text="edam:format_3586",
                title="bed12",
                description="""A BED file where each feature is described by all twelve columns.
Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 12""",
                meaning=EDAM["format_3586"]))
        setattr(cls, "edam:format_3587",
            PermissibleValue(
                text="edam:format_3587",
                title="chrominfo",
                description="""Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not.
Tabular format of chromosome names and sizes used by Galaxy.""",
                meaning=EDAM["format_3587"]))
        setattr(cls, "edam:format_3588",
            PermissibleValue(
                text="edam:format_3588",
                title="customtrack",
                description="""Custom Sequence annotation track format used by Galaxy.
Used for tracks/track views within galaxy.""",
                meaning=EDAM["format_3588"]))
        setattr(cls, "edam:format_3589",
            PermissibleValue(
                text="edam:format_3589",
                title="csfasta",
                description="""Color space FASTA format sequence variant.
FASTA format extended for color space information.""",
                meaning=EDAM["format_3589"]))
        setattr(cls, "edam:format_3590",
            PermissibleValue(
                text="edam:format_3590",
                title="HDF5",
                description="""An HDF5 file appears to the user as a directed graph. The nodes of this graph are the higher-level HDF5 objects that are exposed by the HDF5 APIs: Groups, Datasets, Named datatypes. Currently supported by the Python MDTraj package.
HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).
HDF5 is the new version, according to the HDF group, a completely different technology (https://support.hdfgroup.org/products/hdf4/ compared to HDF.""",
                meaning=EDAM["format_3590"]))
        setattr(cls, "edam:format_3591",
            PermissibleValue(
                text="edam:format_3591",
                title="TIFF",
                description="""A versatile bitmap format.
The TIFF format is perhaps the most versatile and diverse bitmap format in existence. Its extensible nature and support for numerous data compression schemes allow developers to customize the TIFF format to fit any peculiar data storage needs.""",
                meaning=EDAM["format_3591"]))
        setattr(cls, "edam:format_3592",
            PermissibleValue(
                text="edam:format_3592",
                title="BMP",
                description="""Although it is based on Windows internal bitmap data structures, it is supported by many non-Windows and non-PC applications.
Standard bitmap storage format in the Microsoft Windows environment.""",
                meaning=EDAM["format_3592"]))
        setattr(cls, "edam:format_3593",
            PermissibleValue(
                text="edam:format_3593",
                title="im",
                description="""IFUNC library reads and writes most uncompressed interchange versions of this format.
IM is a format used by LabEye and other applications based on the IFUNC image processing library.""",
                meaning=EDAM["format_3593"]))
        setattr(cls, "edam:format_3594",
            PermissibleValue(
                text="edam:format_3594",
                title="pcd",
                description="""PCD was developed by Kodak. A PCD file contains five different resolution (ranging from low to high) of a slide or film negative. Due to it PCD is often used by many photographers and graphics professionals for high-end printed applications.
Photo CD format, which is the highest resolution format for images on a CD.""",
                meaning=EDAM["format_3594"]))
        setattr(cls, "edam:format_3595",
            PermissibleValue(
                text="edam:format_3595",
                title="pcx",
                description="""PCX is an image file format that uses a simple form of run-length encoding. It is lossless.""",
                meaning=EDAM["format_3595"]))
        setattr(cls, "edam:format_3596",
            PermissibleValue(
                text="edam:format_3596",
                title="ppm",
                description="The PPM format is a lowest common denominator color image file format.",
                meaning=EDAM["format_3596"]))
        setattr(cls, "edam:format_3597",
            PermissibleValue(
                text="edam:format_3597",
                title="psd",
                description="""PSD (Photoshop Document) is a proprietary file that allows the user to work with the images' individual layers even after the file has been saved.""",
                meaning=EDAM["format_3597"]))
        setattr(cls, "edam:format_3598",
            PermissibleValue(
                text="edam:format_3598",
                title="xbm",
                description="""The XBM format was replaced by XPM for X11 in 1989.
X BitMap is a plain text binary image format used by the X Window System used for storing cursor and icon bitmaps used in the X GUI.""",
                meaning=EDAM["format_3598"]))
        setattr(cls, "edam:format_3599",
            PermissibleValue(
                text="edam:format_3599",
                title="xpm",
                description="""Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type.
X PixMap (XPM) is an image file format used by the X Window System, it is intended primarily for creating icon pixmaps, and supports transparent pixels.""",
                meaning=EDAM["format_3599"]))
        setattr(cls, "edam:format_3600",
            PermissibleValue(
                text="edam:format_3600",
                title="rgb",
                description="""RGB file format is the native raster graphics file format for Silicon Graphics workstations.""",
                meaning=EDAM["format_3600"]))
        setattr(cls, "edam:format_3601",
            PermissibleValue(
                text="edam:format_3601",
                title="pbm",
                description="""The PBM format is a lowest common denominator monochrome file format. It serves as the common language of a large family of bitmap image conversion filters.""",
                meaning=EDAM["format_3601"]))
        setattr(cls, "edam:format_3602",
            PermissibleValue(
                text="edam:format_3602",
                title="pgm",
                description="""It is designed to be extremely easy to learn and write programs for.
The PGM format is a lowest common denominator grayscale file format.""",
                meaning=EDAM["format_3602"]))
        setattr(cls, "edam:format_3603",
            PermissibleValue(
                text="edam:format_3603",
                title="PNG",
                description="""It iis expected to replace the Graphics Interchange Format (GIF).
PNG is a file format for image compression.""",
                meaning=EDAM["format_3603"]))
        setattr(cls, "edam:format_3604",
            PermissibleValue(
                text="edam:format_3604",
                title="SVG",
                description="""Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics with support for interactivity and animation.
The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.""",
                meaning=EDAM["format_3604"]))
        setattr(cls, "edam:format_3605",
            PermissibleValue(
                text="edam:format_3605",
                title="rast",
                description="""Sun Raster is a raster graphics file format used on SunOS by Sun Microsystems.
The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.""",
                meaning=EDAM["format_3605"]))
        setattr(cls, "edam:format_3606",
            PermissibleValue(
                text="edam:format_3606",
                title="Sequence quality report format (text)",
                description="Textual report format for sequence quality for reports from sequencing machines.",
                meaning=EDAM["format_3606"]))
        setattr(cls, "edam:format_3607",
            PermissibleValue(
                text="edam:format_3607",
                title="qual",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences).
Phred quality scores are defined as a property which is logarithmically related to the base-calling error probabilities.""",
                meaning=EDAM["format_3607"]))
        setattr(cls, "edam:format_3608",
            PermissibleValue(
                text="edam:format_3608",
                title="qualsolexa",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) for Solexa/Illumina 1.0 format.
Solexa/Illumina 1.0 format can encode a Solexa/Illumina quality score from -5 to 62 using ASCII 59 to 126 (although in raw read data Solexa scores from -5 to 40 only are expected)""",
                meaning=EDAM["format_3608"]))
        setattr(cls, "edam:format_3609",
            PermissibleValue(
                text="edam:format_3609",
                title="qualillumina",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) from Illumina 1.5 and before Illumina 1.8.
Starting in Illumina 1.5 and before Illumina 1.8, the Phred scores 0 to 2 have a slightly different meaning. The values 0 and 1 are no longer used and the value 2, encoded by ASCII 66 \"B\", is used also at the end of reads as a Read Segment Quality Control Indicator.""",
                meaning=EDAM["format_3609"]))
        setattr(cls, "edam:format_3610",
            PermissibleValue(
                text="edam:format_3610",
                title="qualsolid",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) for SOLiD data.
For SOLiD data, the sequence is in color space, except the first position. The quality values are those of the Sanger format.""",
                meaning=EDAM["format_3610"]))
        setattr(cls, "edam:format_3611",
            PermissibleValue(
                text="edam:format_3611",
                title="qual454",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) from 454 sequencers.""",
                meaning=EDAM["format_3611"]))
        setattr(cls, "edam:format_3612",
            PermissibleValue(
                text="edam:format_3612",
                title="ENCODE peak format",
                description="""Format that covers both the broad peak format and narrow peak format from ENCODE.
Human ENCODE peak format.""",
                meaning=EDAM["format_3612"]))
        setattr(cls, "edam:format_3613",
            PermissibleValue(
                text="edam:format_3613",
                title="ENCODE narrow peak format",
                description="""Format that covers both the broad peak format and narrow peak format from ENCODE.
Human ENCODE narrow peak format.""",
                meaning=EDAM["format_3613"]))
        setattr(cls, "edam:format_3614",
            PermissibleValue(
                text="edam:format_3614",
                title="ENCODE broad peak format",
                description="Human ENCODE broad peak format.",
                meaning=EDAM["format_3614"]))
        setattr(cls, "edam:format_3615",
            PermissibleValue(
                text="edam:format_3615",
                title="bgzip",
                description="""BAM files are compressed using a variant of GZIP (GNU ZIP), into a format called BGZF (Blocked GNU Zip Format).
Blocked GNU Zip format.""",
                meaning=EDAM["format_3615"]))
        setattr(cls, "edam:format_3616",
            PermissibleValue(
                text="edam:format_3616",
                title="tabix",
                description="TAB-delimited genome position file index format.",
                meaning=EDAM["format_3616"]))
        setattr(cls, "edam:format_3617",
            PermissibleValue(
                text="edam:format_3617",
                title="Graph format",
                description="Data format for graph data.",
                meaning=EDAM["format_3617"]))
        setattr(cls, "edam:format_3618",
            PermissibleValue(
                text="edam:format_3618",
                title="xgmml",
                description="XML-based format used to store graph descriptions within Galaxy.",
                meaning=EDAM["format_3618"]))
        setattr(cls, "edam:format_3619",
            PermissibleValue(
                text="edam:format_3619",
                title="sif",
                description="""SIF (simple interaction file) Format - a network/pathway format used for instance in cytoscape.""",
                meaning=EDAM["format_3619"]))
        setattr(cls, "edam:format_3620",
            PermissibleValue(
                text="edam:format_3620",
                title="xlsx",
                description="""MS Excel spreadsheet format consisting of a set of XML documents stored in a ZIP-compressed file.""",
                meaning=EDAM["format_3620"]))
        setattr(cls, "edam:format_3621",
            PermissibleValue(
                text="edam:format_3621",
                title="SQLite format",
                description="Data format used by the SQLite database.",
                meaning=EDAM["format_3621"]))
        setattr(cls, "edam:format_3622",
            PermissibleValue(
                text="edam:format_3622",
                title="Gemini SQLite format",
                description="Data format used by the SQLite database conformant to the Gemini schema.",
                meaning=EDAM["format_3622"]))
        setattr(cls, "edam:format_3624",
            PermissibleValue(
                text="edam:format_3624",
                title="snpeffdb",
                description="An index of a genome database, indexed for use by the snpeff tool.",
                meaning=EDAM["format_3624"]))
        setattr(cls, "edam:format_3626",
            PermissibleValue(
                text="edam:format_3626",
                title="MAT",
                description="Binary format used by MATLAB files to store workspace variables.",
                meaning=EDAM["format_3626"]))
        setattr(cls, "edam:format_3650",
            PermissibleValue(
                text="edam:format_3650",
                title="NetCDF",
                description="""Format used by netCDF software library for writing and reading chromatography-MS data files. Also used to store trajectory atom coordinates information, such as the ones obtained by Molecular Dynamics simulations.
Network Common Data Form (NetCDF) library is supported by AMBER MD package from version 9.""",
                meaning=EDAM["format_3650"]))
        setattr(cls, "edam:format_3651",
            PermissibleValue(
                text="edam:format_3651",
                title="MGF",
                description="""Files includes *m*/*z*, intensity pairs separated by headers; headers can contain a bit more information, including search engine instructions.
Mascot Generic Format. Encodes multiple MS/MS spectra in a single file.""",
                meaning=EDAM["format_3651"]))
        setattr(cls, "edam:format_3652",
            PermissibleValue(
                text="edam:format_3652",
                title="dta",
                description="""Each file contains one header line for the known or assumed charge and the mass of the precursor peptide ion, calculated from the measured *m*/*z* and the charge. This one line was then followed by all the *m*/*z*, intensity pairs that represent the spectrum.
Spectral data format file where each spectrum is written to a separate file.""",
                meaning=EDAM["format_3652"]))
        setattr(cls, "edam:format_3653",
            PermissibleValue(
                text="edam:format_3653",
                title="pkl",
                description="""Differ from .dta only in subtleties of the header line format and content and support the added feature of being able to.
Spectral data file similar to dta.""",
                meaning=EDAM["format_3653"]))
        setattr(cls, "edam:format_3654",
            PermissibleValue(
                text="edam:format_3654",
                title="mzXML",
                description="""Common file format for proteomics mass spectrometric data developed at the Seattle Proteome Center/Institute for Systems Biology.""",
                meaning=EDAM["format_3654"]))
        setattr(cls, "edam:format_3655",
            PermissibleValue(
                text="edam:format_3655",
                title="pepXML",
                description="""Open data format for the storage, exchange, and processing of peptide sequence assignments of MS/MS scans, intended to provide a common data output format for many different MS/MS search engines and subsequent peptide-level analyses.""",
                meaning=EDAM["format_3655"]))
        setattr(cls, "edam:format_3657",
            PermissibleValue(
                text="edam:format_3657",
                title="GPML",
                description="""Graphical Pathway Markup Language (GPML) is an XML format used for exchanging biological pathways.""",
                meaning=EDAM["format_3657"]))
        setattr(cls, "edam:format_3665",
            PermissibleValue(
                text="edam:format_3665",
                title="K-mer countgraph",
                description="""A list of k-mers and their occurrences in a dataset. Can also be used as an implicit De Bruijn graph.""",
                meaning=EDAM["format_3665"]))
        setattr(cls, "edam:format_3681",
            PermissibleValue(
                text="edam:format_3681",
                title="mzTab",
                description="""For mass spectrometry-based chemical profiling data (including metabolomics), there is a derived (but incompatible) format mzTab-M (also named mzTab 2.0, http://edamontology.org/format_4058), and its lipidomics version mzTab-L (http://edamontology.org/format_4059).
For more detailed metadata, there are formats such as mzIdentML (http://edamontology.org/format_3247) and mzQuantML (http://edamontology.org/format_3248).
The reference implementation of mzTab in Java is https://github.com/PRIDE-Archive/jmzTab (maintenance stopped in 2022).
mzTab is a light-weight, tab-delimited format for mass spectrometry-based proteomics data.
mzTab is alternatively named mzTab 1.0, as opposed to mzTab 2.0 (and 2.1), which is the incompatible mzTab-M format for chemical profiling e.g. metabolomics.""",
                meaning=EDAM["format_3681"]))
        setattr(cls, "edam:format_3682",
            PermissibleValue(
                text="edam:format_3682",
                title="imzML metadata file",
                description="""imzML data are recorded in 2 files: '.imzXML' (this concept) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (http://edamontology.org/format_3839) is a binary file containing the mass spectra. This entry is for the metadata XML file.
imzML metadata is a data format for mass spectrometry imaging metadata.""",
                meaning=EDAM["format_3682"]))
        setattr(cls, "edam:format_3683",
            PermissibleValue(
                text="edam:format_3683",
                title="qcML",
                description="""The focus of qcML is towards mass spectrometry based proteomics, but the format is suitable for metabolomics and sequencing as well.
qcML is an XML format for quality-related data of mass spectrometry and other high-throughput measurements.""",
                meaning=EDAM["format_3683"]))
        setattr(cls, "edam:format_3684",
            PermissibleValue(
                text="edam:format_3684",
                title="PRIDE XML",
                description="""PRIDE XML is an XML format for mass spectra, peptide and protein identifications, and metadata about a corresponding measurement, sample, experiment.""",
                meaning=EDAM["format_3684"]))
        setattr(cls, "edam:format_3685",
            PermissibleValue(
                text="edam:format_3685",
                title="SED-ML",
                description="""Simulation Experiment Description Markup Language (SED-ML) is an XML format for encoding simulation setups, according to the MIASE (Minimum Information About a Simulation Experiment) requirements.""",
                meaning=EDAM["format_3685"]))
        setattr(cls, "edam:format_3686",
            PermissibleValue(
                text="edam:format_3686",
                title="COMBINE OMEX",
                description="""An OMEX file is a ZIP container that includes a manifest file, listing the content of the archive, an optional metadata file adding information about the archive and its content, and the files describing the model. OMEX is one of the standardised formats within COMBINE (Computational Modeling in Biology Network).
Open Modeling EXchange format (OMEX) is a ZIPped format for encapsulating all information necessary for a modeling and simulation project in systems biology.""",
                meaning=EDAM["format_3686"]))
        setattr(cls, "edam:format_3687",
            PermissibleValue(
                text="edam:format_3687",
                title="ISA-TAB",
                description="""ISA-TAB is based on MAGE-TAB. Other than tabular, the ISA model can also be represented in RDF, and in JSON (compliable with a set of defined JSON Schemata).
The Investigation / Study / Assay (ISA) tab-delimited (TAB) format incorporates metadata from experiments employing a combination of technologies.""",
                meaning=EDAM["format_3687"]))
        setattr(cls, "edam:format_3688",
            PermissibleValue(
                text="edam:format_3688",
                title="SBtab",
                description="SBtab is a tabular format for biochemical network models.",
                meaning=EDAM["format_3688"]))
        setattr(cls, "edam:format_3689",
            PermissibleValue(
                text="edam:format_3689",
                title="BCML",
                description="Biological Connection Markup Language (BCML) is an XML format for biological pathways.",
                meaning=EDAM["format_3689"]))
        setattr(cls, "edam:format_3690",
            PermissibleValue(
                text="edam:format_3690",
                title="BDML",
                description="""Biological Dynamics Markup Language (BDML) is an XML format for quantitative data describing biological dynamics.""",
                meaning=EDAM["format_3690"]))
        setattr(cls, "edam:format_3691",
            PermissibleValue(
                text="edam:format_3691",
                title="BEL",
                description="""Biological Expression Language (BEL) is a textual format for representing scientific findings in life sciences in a computable form.""",
                meaning=EDAM["format_3691"]))
        setattr(cls, "edam:format_3692",
            PermissibleValue(
                text="edam:format_3692",
                title="SBGN-ML",
                description="""SBGN-ML is an XML format for Systems Biology Graphical Notation (SBGN) diagrams of biological pathways or networks.""",
                meaning=EDAM["format_3692"]))
        setattr(cls, "edam:format_3693",
            PermissibleValue(
                text="edam:format_3693",
                title="AGP",
                description="""AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome).""",
                meaning=EDAM["format_3693"]))
        setattr(cls, "edam:format_3696",
            PermissibleValue(
                text="edam:format_3696",
                title="PS",
                description="PostScript format.",
                meaning=EDAM["format_3696"]))
        setattr(cls, "edam:format_3698",
            PermissibleValue(
                text="edam:format_3698",
                title="SRA format",
                description="""SRA archive format (SRA) is the archive format used for input to the NCBI Sequence Read Archive.""",
                meaning=EDAM["format_3698"]))
        setattr(cls, "edam:format_3699",
            PermissibleValue(
                text="edam:format_3699",
                title="VDB",
                description="""VDB ('vertical database') is the native format used for export from the NCBI Sequence Read Archive.""",
                meaning=EDAM["format_3699"]))
        setattr(cls, "edam:format_3701",
            PermissibleValue(
                text="edam:format_3701",
                title="Sequin format",
                description="""A five-column, tab-delimited table of feature locations and qualifiers for importing annotation into an existing Sequin submission (an NCBI tool for submitting and updating GenBank entries).""",
                meaning=EDAM["format_3701"]))
        setattr(cls, "edam:format_3702",
            PermissibleValue(
                text="edam:format_3702",
                title="MSF",
                description="""Proprietary mass-spectrometry format of Thermo Scientific's ProteomeDiscoverer software.
This format corresponds to an SQLite database, and you can look into the files with e.g. SQLiteStudio3. There are also some readers (http://doi.org/10.1021/pr2005154) and converters (http://doi.org/10.1016/j.jprot.2015.06.015) for this format available, which re-engineered the database schema, but there is no official DB schema specification of Thermo Scientific for the format.""",
                meaning=EDAM["format_3702"]))
        setattr(cls, "edam:format_3706",
            PermissibleValue(
                text="edam:format_3706",
                title="Biodiversity data format",
                description="Data format for biodiversity data.",
                meaning=EDAM["format_3706"]))
        setattr(cls, "edam:format_3708",
            PermissibleValue(
                text="edam:format_3708",
                title="ABCD format",
                description="""Exchange format of the Access to Biological Collections Data (ABCD) Schema; a standard for the access to and exchange of data about specimens and observations (primary biodiversity data).""",
                meaning=EDAM["format_3708"]))
        setattr(cls, "edam:format_3709",
            PermissibleValue(
                text="edam:format_3709",
                title="GCT/Res format",
                description="""Tab-delimited text files of GenePattern that contain a column for each sample, a row for each gene, and an expression value for each gene in each sample.""",
                meaning=EDAM["format_3709"]))
        setattr(cls, "edam:format_3710",
            PermissibleValue(
                text="edam:format_3710",
                title="WIFF format",
                description="Mass spectrum file format from QSTAR and QTRAP instruments (ABI/Sciex).",
                meaning=EDAM["format_3710"]))
        setattr(cls, "edam:format_3711",
            PermissibleValue(
                text="edam:format_3711",
                title="X!Tandem XML",
                description="""Output format used by X! series search engines that is based on the XML language BIOML.""",
                meaning=EDAM["format_3711"]))
        setattr(cls, "edam:format_3712",
            PermissibleValue(
                text="edam:format_3712",
                title="Thermo RAW",
                description="""Proprietary file format for mass spectrometry data from Thermo Scientific.
Proprietary format for which documentation is not available.""",
                meaning=EDAM["format_3712"]))
        setattr(cls, "edam:format_3713",
            PermissibleValue(
                text="edam:format_3713",
                title="Mascot .dat file",
                description="\"Raw\" result file from Mascot database search.",
                meaning=EDAM["format_3713"]))
        setattr(cls, "edam:format_3714",
            PermissibleValue(
                text="edam:format_3714",
                title="MaxQuant APL peaklist format",
                description="""Format of peak list files from Andromeda search engine (MaxQuant) that consist of arbitrarily many spectra.""",
                meaning=EDAM["format_3714"]))
        setattr(cls, "edam:format_3725",
            PermissibleValue(
                text="edam:format_3725",
                title="SBOL",
                description="""SBOL introduces a standardised format for the electronic exchange of information on the structural and functional aspects of biological designs.
Synthetic Biology Open Language (SBOL) is an XML format for the specification and exchange of biological design information in synthetic biology.""",
                meaning=EDAM["format_3725"]))
        setattr(cls, "edam:format_3726",
            PermissibleValue(
                text="edam:format_3726",
                title="PMML",
                description="""One or more mining models can be contained in a PMML document.
PMML uses XML to represent mining models. The structure of the models is described by an XML Schema.""",
                meaning=EDAM["format_3726"]))
        setattr(cls, "edam:format_3727",
            PermissibleValue(
                text="edam:format_3727",
                title="OME-TIFF",
                description="""An OME-TIFF dataset consists of one or more files in standard TIFF or BigTIFF format, with the file extension .ome.tif or .ome.tiff, and an identical (or in the case of multiple files, nearly identical) string of OME-XML metadata embedded in the ImageDescription tag of each file's first IFD (Image File Directory). BigTIFF file extensions are also permitted, with the file extension .ome.tf2, .ome.tf8 or .ome.btf, but note these file extensions are an addition to the original specification, and software using an older version of the specification may not be able to handle these file extensions.
Image file format used by the Open Microscopy Environment (OME).
OME develops open-source software and data format standards for the storage and manipulation of biological microscopy data. It is a joint project between universities, research establishments, industry and the software development community.""",
                meaning=EDAM["format_3727"]))
        setattr(cls, "edam:format_3728",
            PermissibleValue(
                text="edam:format_3728",
                title="LocARNA PP",
                description="""Format for multiple aligned or single sequences together with the probabilistic description of the (consensus) RNA secondary structure ensemble by probabilities of base pairs, base pair stackings, and base pairs and unpaired bases in the loop of base pairs.
The LocARNA PP format combines sequence or alignment information and (respectively, single or consensus) ensemble probabilities into an PP 2.0 record.""",
                meaning=EDAM["format_3728"]))
        setattr(cls, "edam:format_3729",
            PermissibleValue(
                text="edam:format_3729",
                title="dbGaP format",
                description="""Input format used by the Database of Genotypes and Phenotypes (dbGaP).
The Database of Genotypes and Phenotypes (dbGaP) is a National Institutes of Health (NIH) sponsored repository charged to archive, curate and distribute information produced by studies investigating the interaction of genotype and phenotype.""",
                meaning=EDAM["format_3729"]))
        setattr(cls, "edam:format_3746",
            PermissibleValue(
                text="edam:format_3746",
                title="BIOM format",
                description="""BIOM is a recognised standard for the Earth Microbiome Project, and is a project supported by Genomics Standards Consortium. Supported in QIIME, Mothur, MEGAN, etc.
The BIological Observation Matrix (BIOM) is a format for representing biological sample by observation contingency tables in broad areas of comparative omics. The primary use of this format is to represent OTU tables and metagenome tables.""",
                meaning=EDAM["format_3746"]))
        setattr(cls, "edam:format_3747",
            PermissibleValue(
                text="edam:format_3747",
                title="protXML",
                description="""A format for storage, exchange, and processing of protein identifications created from ms/ms-derived peptide sequence data.
No human-consumable information about this format is available (see http://tools.proteomecenter.org/wiki/index.php?title=Formats:protXML).""",
                meaning=EDAM["format_3747"]))
        setattr(cls, "edam:format_3748",
            PermissibleValue(
                text="edam:format_3748",
                title="Linked data format",
                description="""A linked data format enables publishing structured data as linked data (Linked Data), so that the data can be interlinked and become more useful through semantic queries.""",
                meaning=EDAM["format_3748"]))
        setattr(cls, "edam:format_3749",
            PermissibleValue(
                text="edam:format_3749",
                title="JSON-LD",
                description="""JSON-LD, or JavaScript Object Notation for Linked Data, is a method of encoding Linked Data using JSON.""",
                meaning=EDAM["format_3749"]))
        setattr(cls, "edam:format_3750",
            PermissibleValue(
                text="edam:format_3750",
                title="YAML",
                description="""Data in YAML format can be serialised into text, or binary format.
YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.
YAML version 1.2 is a superset of JSON; prior versions were \"not strictly compatible\".""",
                meaning=EDAM["format_3750"]))
        setattr(cls, "edam:format_3751",
            PermissibleValue(
                text="edam:format_3751",
                title="DSV",
                description="Tabular data represented as values in a text file delimited by some character.",
                meaning=EDAM["format_3751"]))
        setattr(cls, "edam:format_3752",
            PermissibleValue(
                text="edam:format_3752",
                title="CSV",
                description="Tabular data represented as comma-separated values in a text file.",
                meaning=EDAM["format_3752"]))
        setattr(cls, "edam:format_3758",
            PermissibleValue(
                text="edam:format_3758",
                title="SEQUEST .out file",
                description="\"Raw\" result file from SEQUEST database search.",
                meaning=EDAM["format_3758"]))
        setattr(cls, "edam:format_3764",
            PermissibleValue(
                text="edam:format_3764",
                title="idXML",
                description="""XML file format for files containing information about peptide identifications from mass spectrometry data analysis carried out with OpenMS.""",
                meaning=EDAM["format_3764"]))
        setattr(cls, "edam:format_3765",
            PermissibleValue(
                text="edam:format_3765",
                title="KNIME datatable format",
                description="Data table formatted such that it can be passed/streamed within the KNIME platform.",
                meaning=EDAM["format_3765"]))
        setattr(cls, "edam:format_3770",
            PermissibleValue(
                text="edam:format_3770",
                title="UniProtKB XML",
                description="""UniProtKB XML sequence features format is an XML format available for downloading UniProt entries.""",
                meaning=EDAM["format_3770"]))
        setattr(cls, "edam:format_3771",
            PermissibleValue(
                text="edam:format_3771",
                title="UniProtKB RDF",
                description="""UniProtKB RDF sequence features format is an RDF format available for downloading UniProt entries (in RDF/XML).""",
                meaning=EDAM["format_3771"]))
        setattr(cls, "edam:format_3772",
            PermissibleValue(
                text="edam:format_3772",
                title="BioJSON (BioXSD)",
                description="""BioJSON is a BioXSD-schema-based JSON format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web applications and APIs, and object-oriented programming.
Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioJSON' is the JSON format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.""",
                meaning=EDAM["format_3772"]))
        setattr(cls, "edam:format_3773",
            PermissibleValue(
                text="edam:format_3773",
                title="BioYAML",
                description="""BioYAML is a BioXSD-schema-based YAML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web APIs, human readability and editing, and object-oriented programming.
Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioYAML' is the YAML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.""",
                meaning=EDAM["format_3773"]))
        setattr(cls, "edam:format_3774",
            PermissibleValue(
                text="edam:format_3774",
                title="BioJSON (Jalview)",
                description="""BioJSON is a JSON format of single multiple sequence alignments, with their annotations, features, and custom visualisation and application settings for the Jalview workbench.""",
                meaning=EDAM["format_3774"]))
        setattr(cls, "edam:format_3775",
            PermissibleValue(
                text="edam:format_3775",
                title="GSuite",
                description="""'GSuite' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GSuite' is the tabular format for an annotated collection of individual GTrack files.
GSuite is a tabular format for collections of genome or sequence feature tracks, suitable for integrative multi-track analysis. GSuite contains links to genome/sequence tracks, with additional metadata.""",
                meaning=EDAM["format_3775"]))
        setattr(cls, "edam:format_3776",
            PermissibleValue(
                text="edam:format_3776",
                title="BTrack",
                description="""'BTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'BTrack' is the binary, optionally compressed HDF5-based version of the GTrack and GSuite formats.
BTrack is an HDF5-based binary format for genome or sequence feature tracks and their collections, suitable for integrative multi-track analysis. BTrack is a binary, compressed alternative to the GTrack and GSuite formats.""",
                meaning=EDAM["format_3776"]))
        setattr(cls, "edam:format_3777",
            PermissibleValue(
                text="edam:format_3777",
                title="MCPD",
                description="""Multi-Crop Passport Descriptors is a format available in 2 successive versions, V.1 (FAO/IPGRI 2001) and V.2 (FAO/Bioversity 2012).
The FAO/Bioversity/IPGRI Multi-Crop Passport Descriptors (MCPD) is an international standard format for exchange of germplasm information.""",
                meaning=EDAM["format_3777"]))
        setattr(cls, "edam:format_3780",
            PermissibleValue(
                text="edam:format_3780",
                title="Annotated text format",
                description="""Data format of an annotated text, e.g. with recognised entities, concepts, and relations.""",
                meaning=EDAM["format_3780"]))
        setattr(cls, "edam:format_3781",
            PermissibleValue(
                text="edam:format_3781",
                title="PubAnnotation format",
                description="JSON format of annotated scientific text used by PubAnnotations and other tools.",
                meaning=EDAM["format_3781"]))
        setattr(cls, "edam:format_3782",
            PermissibleValue(
                text="edam:format_3782",
                title="BioC",
                description="""BioC is a standardised XML format for sharing and integrating text data and annotations.""",
                meaning=EDAM["format_3782"]))
        setattr(cls, "edam:format_3783",
            PermissibleValue(
                text="edam:format_3783",
                title="PubTator format",
                description="Native textual export format of annotated scientific text from PubTator.",
                meaning=EDAM["format_3783"]))
        setattr(cls, "edam:format_3784",
            PermissibleValue(
                text="edam:format_3784",
                title="Open Annotation format",
                description="""A format of text annotation using the linked-data Open Annotation Data Model, serialised typically in RDF or JSON-LD.""",
                meaning=EDAM["format_3784"]))
        setattr(cls, "edam:format_3785",
            PermissibleValue(
                text="edam:format_3785",
                title="BioNLP Shared Task format",
                description="""A family of similar formats of text annotation, used by BRAT and other tools, known as BioNLP Shared Task format (BioNLP 2009 Shared Task on Event Extraction, BioNLP Shared Task 2011, BioNLP Shared Task 2013), BRAT format, BRAT standoff format, and similar.""",
                meaning=EDAM["format_3785"]))
        setattr(cls, "edam:format_3787",
            PermissibleValue(
                text="edam:format_3787",
                title="Query language",
                description="A query language (format) for structured database queries.",
                meaning=EDAM["format_3787"]))
        setattr(cls, "edam:format_3788",
            PermissibleValue(
                text="edam:format_3788",
                title="SQL",
                description="""SQL (Structured Query Language) is the de-facto standard query language (format of queries) for querying and manipulating data in relational databases.""",
                meaning=EDAM["format_3788"]))
        setattr(cls, "edam:format_3789",
            PermissibleValue(
                text="edam:format_3789",
                title="XQuery",
                description="""XQuery (XML Query) is a query language (format of queries) for querying and manipulating structured and unstructured data, usually in the form of XML, text, and with vendor-specific extensions for other data formats (JSON, binary, etc.).""",
                meaning=EDAM["format_3789"]))
        setattr(cls, "edam:format_3790",
            PermissibleValue(
                text="edam:format_3790",
                title="SPARQL",
                description="""SPARQL (SPARQL Protocol and RDF Query Language) is a semantic query language for querying and manipulating data stored in Resource Description Framework (RDF) format.""",
                meaning=EDAM["format_3790"]))
        setattr(cls, "edam:format_3804",
            PermissibleValue(
                text="edam:format_3804",
                title="xsd",
                description="XML format for XML Schema.",
                meaning=EDAM["format_3804"]))
        setattr(cls, "edam:format_3811",
            PermissibleValue(
                text="edam:format_3811",
                title="XMFA",
                description="""XMFA format stands for eXtended Multi-FastA format and is used to store collinear sub-alignments that constitute a single genome alignment.""",
                meaning=EDAM["format_3811"]))
        setattr(cls, "edam:format_3812",
            PermissibleValue(
                text="edam:format_3812",
                title="GEN",
                description="The GEN file format contains genetic data and describes SNPs.",
                meaning=EDAM["format_3812"]))
        setattr(cls, "edam:format_3813",
            PermissibleValue(
                text="edam:format_3813",
                title="SAMPLE file format",
                description="""The SAMPLE file format contains information about each individual i.e. individual IDs, covariates, phenotypes and missing data proportions, from a GWAS study.""",
                meaning=EDAM["format_3813"]))
        setattr(cls, "edam:format_3814",
            PermissibleValue(
                text="edam:format_3814",
                title="SDF",
                description="""SDF is one of a family of chemical-data file formats developed by MDL Information Systems; it is intended especially for structural information.""",
                meaning=EDAM["format_3814"]))
        setattr(cls, "edam:format_3815",
            PermissibleValue(
                text="edam:format_3815",
                title="Molfile",
                description="""An MDL Molfile is a file format for holding information about the atoms, bonds, connectivity and coordinates of a molecule.""",
                meaning=EDAM["format_3815"]))
        setattr(cls, "edam:format_3816",
            PermissibleValue(
                text="edam:format_3816",
                title="Mol2",
                description="""Complete, portable representation of a SYBYL molecule. ASCII file which contains all the information needed to reconstruct a SYBYL molecule.""",
                meaning=EDAM["format_3816"]))
        setattr(cls, "edam:format_3817",
            PermissibleValue(
                text="edam:format_3817",
                title="latex",
                description="""format for the LaTeX document preparation system.
uses the TeX typesetting program format""",
                meaning=EDAM["format_3817"]))
        setattr(cls, "edam:format_3818",
            PermissibleValue(
                text="edam:format_3818",
                title="ELAND format",
                description="""Tab-delimited text file format used by Eland - the read-mapping program distributed by Illumina with its sequencing analysis pipeline - which maps short Solexa sequence reads to the human reference genome.""",
                meaning=EDAM["format_3818"]))
        setattr(cls, "edam:format_3819",
            PermissibleValue(
                text="edam:format_3819",
                title="Relaxed PHYLIP Interleaved",
                description="""It differs from Phylip Format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
Phylip multiple alignment sequence format, less stringent than PHYLIP format.""",
                meaning=EDAM["format_3819"]))
        setattr(cls, "edam:format_3820",
            PermissibleValue(
                text="edam:format_3820",
                title="Relaxed PHYLIP Sequential",
                description="""It differs from Phylip sequential format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
Phylip multiple alignment sequence format, less stringent than PHYLIP sequential format (format_1998).""",
                meaning=EDAM["format_3820"]))
        setattr(cls, "edam:format_3821",
            PermissibleValue(
                text="edam:format_3821",
                title="VisML",
                description="Default XML format of VisANT, containing all the network information.",
                meaning=EDAM["format_3821"]))
        setattr(cls, "edam:format_3822",
            PermissibleValue(
                text="edam:format_3822",
                title="GML",
                description="""GML (Graph Modeling Language) is a text file format supporting network data with a very easy syntax. It is used by Graphlet, Pajek, yEd, LEDA and NetworkX.""",
                meaning=EDAM["format_3822"]))
        setattr(cls, "edam:format_3823",
            PermissibleValue(
                text="edam:format_3823",
                title="FASTG",
                description="""FASTG is a format for faithfully representing genome assemblies in the face of allelic polymorphism and assembly uncertainty.
It is called FASTG, like FASTA, but the G stands for \"graph\".""",
                meaning=EDAM["format_3823"]))
        setattr(cls, "edam:format_3824",
            PermissibleValue(
                text="edam:format_3824",
                title="NMR data format",
                description="""Data format for raw data from a nuclear magnetic resonance (NMR) spectroscopy experiment.""",
                meaning=EDAM["format_3824"]))
        setattr(cls, "edam:format_3825",
            PermissibleValue(
                text="edam:format_3825",
                title="nmrML",
                description="""nmrML is an MSI supported XML-based open access format for metabolomics NMR raw and processed spectral data. It is accompanies by an nmrCV (controlled vocabulary) to allow ontology-based annotations.""",
                meaning=EDAM["format_3825"]))
        setattr(cls, "edam:format_3826",
            PermissibleValue(
                text="edam:format_3826",
                title="proBAM",
                description=""". proBAM is an adaptation of BAM (format_2572), which was extended to meet specific requirements entailed by proteomics data.""",
                meaning=EDAM["format_3826"]))
        setattr(cls, "edam:format_3827",
            PermissibleValue(
                text="edam:format_3827",
                title="proBED",
                description=""". proBED is an adaptation of BED (format_3003), which was extended to meet specific requirements entailed by proteomics data.""",
                meaning=EDAM["format_3827"]))
        setattr(cls, "edam:format_3828",
            PermissibleValue(
                text="edam:format_3828",
                title="Raw microarray data format",
                description="Data format for raw microarray data.",
                meaning=EDAM["format_3828"]))
        setattr(cls, "edam:format_3829",
            PermissibleValue(
                text="edam:format_3829",
                title="GPR",
                description="""GenePix Results (GPR) text file format developed by Axon Instruments that is used to save GenePix Results data.""",
                meaning=EDAM["format_3829"]))
        setattr(cls, "edam:format_3830",
            PermissibleValue(
                text="edam:format_3830",
                title="ARB",
                description="Binary format used by the ARB software suite.",
                meaning=EDAM["format_3830"]))
        setattr(cls, "edam:format_3832",
            PermissibleValue(
                text="edam:format_3832",
                title="consensusXML",
                description="OpenMS format for grouping features in one map or across several maps.",
                meaning=EDAM["format_3832"]))
        setattr(cls, "edam:format_3833",
            PermissibleValue(
                text="edam:format_3833",
                title="featureXML",
                description="OpenMS format for quantitation results (LC/MS features).",
                meaning=EDAM["format_3833"]))
        setattr(cls, "edam:format_3834",
            PermissibleValue(
                text="edam:format_3834",
                title="mzData",
                description="""Now deprecated data format of the HUPO Proteomics Standards Initiative. Replaced by mzML (format_3244).""",
                meaning=EDAM["format_3834"]))
        setattr(cls, "edam:format_3835",
            PermissibleValue(
                text="edam:format_3835",
                title="TIDE TXT",
                description="Format supported by the Tide tool for identifying peptides from tandem mass spectra.",
                meaning=EDAM["format_3835"]))
        setattr(cls, "edam:format_3836",
            PermissibleValue(
                text="edam:format_3836",
                title="BLAST XML v2 results format",
                description="XML format as produced by the NCBI Blast package v2.",
                meaning=EDAM["format_3836"]))
        setattr(cls, "edam:format_3838",
            PermissibleValue(
                text="edam:format_3838",
                title="pptx",
                description="Microsoft Powerpoint format.",
                meaning=EDAM["format_3838"]))
        setattr(cls, "edam:format_3839",
            PermissibleValue(
                text="edam:format_3839",
                title="ibd",
                description="""ibd is a data format for mass spectrometry imaging data.
imzML data is recorded in 2 files: '.imzXML' (http://edamontology.org/format_3682) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (this concept) is a binary file containing the mass spectra.""",
                meaning=EDAM["format_3839"]))
        setattr(cls, "edam:format_3841",
            PermissibleValue(
                text="edam:format_3841",
                title="NLP format",
                description="Data format used in Natural Language Processing.",
                meaning=EDAM["format_3841"]))
        setattr(cls, "edam:format_3843",
            PermissibleValue(
                text="edam:format_3843",
                title="BEAST",
                description="""XML input file format for BEAST Software (Bayesian Evolutionary Analysis Sampling Trees).""",
                meaning=EDAM["format_3843"]))
        setattr(cls, "edam:format_3844",
            PermissibleValue(
                text="edam:format_3844",
                title="Chado-XML",
                description="Chado-XML format is a direct mapping of the Chado relational schema into XML.",
                meaning=EDAM["format_3844"]))
        setattr(cls, "edam:format_3845",
            PermissibleValue(
                text="edam:format_3845",
                title="HSAML",
                description="""An alignment format generated by PRANK/PRANKSTER consisting of four elements: newick, nodes, selection and model.""",
                meaning=EDAM["format_3845"]))
        setattr(cls, "edam:format_3846",
            PermissibleValue(
                text="edam:format_3846",
                title="InterProScan XML",
                description="Output xml file from the InterProScan sequence analysis application.",
                meaning=EDAM["format_3846"]))
        setattr(cls, "edam:format_3847",
            PermissibleValue(
                text="edam:format_3847",
                title="KGML",
                description="""The KEGG Markup Language (KGML) is an exchange format of the KEGG pathway maps, which is converted from internally used KGML+ (KGML+SVG) format.""",
                meaning=EDAM["format_3847"]))
        setattr(cls, "edam:format_3848",
            PermissibleValue(
                text="edam:format_3848",
                title="PubMed XML",
                description="XML format for collected entries from bibliographic databases MEDLINE and PubMed.",
                meaning=EDAM["format_3848"]))
        setattr(cls, "edam:format_3849",
            PermissibleValue(
                text="edam:format_3849",
                title="MSAML",
                description="A set of XML compliant markup components for describing multiple sequence alignments.",
                meaning=EDAM["format_3849"]))
        setattr(cls, "edam:format_3850",
            PermissibleValue(
                text="edam:format_3850",
                title="OrthoXML",
                description="""OrthoXML is designed broadly to allow the storage and comparison of orthology data from any ortholog database. It establishes a structure for describing orthology relationships while still allowing flexibility for database-specific information to be encapsulated in the same format.""",
                meaning=EDAM["format_3850"]))
        setattr(cls, "edam:format_3851",
            PermissibleValue(
                text="edam:format_3851",
                title="PSDML",
                description="""Tree structure of Protein Sequence Database Markup Language generated using Matra software.""",
                meaning=EDAM["format_3851"]))
        setattr(cls, "edam:format_3852",
            PermissibleValue(
                text="edam:format_3852",
                title="SeqXML",
                description="""SeqXML is an XML Schema to describe biological sequences, developed by the Stockholm Bioinformatics Centre.""",
                meaning=EDAM["format_3852"]))
        setattr(cls, "edam:format_3853",
            PermissibleValue(
                text="edam:format_3853",
                title="UniParc XML",
                description="XML format for the UniParc database.",
                meaning=EDAM["format_3853"]))
        setattr(cls, "edam:format_3854",
            PermissibleValue(
                text="edam:format_3854",
                title="UniRef XML",
                description="XML format for the UniRef reference clusters.",
                meaning=EDAM["format_3854"]))
        setattr(cls, "edam:format_3857",
            PermissibleValue(
                text="edam:format_3857",
                title="CWL",
                description="""Common Workflow Language (CWL) format for description of command-line tools and workflows.""",
                meaning=EDAM["format_3857"]))
        setattr(cls, "edam:format_3858",
            PermissibleValue(
                text="edam:format_3858",
                title="Waters RAW",
                description="""Proprietary file format for mass spectrometry data from Waters.
Proprietary format for which documentation is not available, but used by multiple tools.""",
                meaning=EDAM["format_3858"]))
        setattr(cls, "edam:format_3859",
            PermissibleValue(
                text="edam:format_3859",
                title="JCAMP-DX",
                description="""A standardized file format for data exchange in mass spectrometry, initially developed for infrared spectrometry.
JCAMP-DX is an ASCII based format and therefore not very compact even though it includes standards for file compression.""",
                meaning=EDAM["format_3859"]))
        setattr(cls, "edam:format_3862",
            PermissibleValue(
                text="edam:format_3862",
                title="NLP annotation format",
                description="An NLP format used for annotated textual documents.",
                meaning=EDAM["format_3862"]))
        setattr(cls, "edam:format_3863",
            PermissibleValue(
                text="edam:format_3863",
                title="NLP corpus format",
                description="NLP format used by a specific type of corpus (collection of texts).",
                meaning=EDAM["format_3863"]))
        setattr(cls, "edam:format_3864",
            PermissibleValue(
                text="edam:format_3864",
                title="mirGFF3",
                description="""mirGFF3 is a common format for microRNA data resulting from small-RNA RNA-Seq workflows.
mirGFF3 is a specialisation of GFF3; produced by small-RNA-Seq analysis workflows, usable and convertible with the miRTop API (https://mirtop.readthedocs.io/en/latest/), and consumable by tools for downstream analysis.""",
                meaning=EDAM["format_3864"]))
        setattr(cls, "edam:format_3865",
            PermissibleValue(
                text="edam:format_3865",
                title="RNA annotation format",
                description="""A \"placeholder\" concept for formats of annotated RNA data, including e.g. microRNA and RNA-Seq data.""",
                meaning=EDAM["format_3865"]))
        setattr(cls, "edam:format_3866",
            PermissibleValue(
                text="edam:format_3866",
                title="Trajectory format",
                description="""File format to store trajectory information for a 3D structure .
Formats differ on what they are able to store (coordinates, velocities, topologies) and how they are storing it (raw, compressed, textual, binary).""",
                meaning=EDAM["format_3866"]))
        setattr(cls, "edam:format_3867",
            PermissibleValue(
                text="edam:format_3867",
                title="Trajectory format (binary)",
                description="Binary file format to store trajectory information for a 3D structure .",
                meaning=EDAM["format_3867"]))
        setattr(cls, "edam:format_3868",
            PermissibleValue(
                text="edam:format_3868",
                title="Trajectory format (text)",
                description="Textual file format to store trajectory information for a 3D structure .",
                meaning=EDAM["format_3868"]))
        setattr(cls, "edam:format_3873",
            PermissibleValue(
                text="edam:format_3873",
                title="HDF",
                description="""HDF is currently supported by many commercial and non-commercial software platforms such as Java, MATLAB/Scilab, Octave, Python and R.
HDF is the name of a set of file formats and libraries designed to store and organize large amounts of numerical data, originally developed at the National Center for Supercomputing Applications at the University of Illinois.""",
                meaning=EDAM["format_3873"]))
        setattr(cls, "edam:format_3874",
            PermissibleValue(
                text="edam:format_3874",
                title="PCAzip",
                description="""PCAZip format is a binary compressed file to store atom coordinates based on Essential Dynamics (ED) and Principal Component Analysis (PCA).
The compression is made projecting the Cartesian snapshots collected along the trajectory into an orthogonal space defined by the most relevant eigenvectors obtained by diagonalization of the covariance matrix (PCA). In the compression/decompression process, part of the original information is lost, depending on the final number of eigenvectors chosen. However, with a reasonable choice of the set of eigenvectors the compression typically reduces the trajectory file to less than one tenth of their original size with very acceptable loss of information. Compression with PCAZip can only be applied to unsolvated structures.""",
                meaning=EDAM["format_3874"]))
        setattr(cls, "edam:format_3875",
            PermissibleValue(
                text="edam:format_3875",
                title="XTC",
                description="""Portable binary format for trajectories produced by GROMACS package.
XTC uses the External Data Representation (xdr) routines for writing and reading data which were created for the Unix Network File System (NFS). XTC files use a reduced precision (lossy) algorithm which works multiplying the coordinates by a scaling factor (typically 1000), so converting them to pm (GROMACS standard distance unit is nm). This allows an integer rounding of the values. Several other tricks are performed, such as making use of atom proximity information: atoms close in sequence are usually close in space (e.g. water molecules). That makes XTC format the most efficient in terms of disk usage, in most cases reducing by a factor of 2 the size of any other binary trajectory format.""",
                meaning=EDAM["format_3875"]))
        setattr(cls, "edam:format_3876",
            PermissibleValue(
                text="edam:format_3876",
                title="TNG",
                description="""Fully architecture-independent format, regarding both endianness and the ability to mix single/double precision trajectories and I/O libraries. Self-sufficient, it should not require any other files for reading, and all the data should be contained in a single file for easy transport. Temporal compression of data, improving the compression rate of the previous XTC format. Possibility to store meta-data with information about the simulation. Direct access to a particular frame. Efficient parallel I/O.
Trajectory Next Generation (TNG) is a format for storage of molecular simulation data. It is designed and implemented by the GROMACS development group, and it is called to be the substitute of the XTC format.""",
                meaning=EDAM["format_3876"]))
        setattr(cls, "edam:format_3877",
            PermissibleValue(
                text="edam:format_3877",
                title="XYZ",
                description="""The XYZ chemical file format is widely supported by many programs, although many slightly different XYZ file formats coexist (Tinker XYZ, UniChem XYZ, etc.). Basic information stored for each atom in the system are x, y and z coordinates and atom element/atomic number.
XYZ files are structured in this way: First line contains the number of atoms in the file. Second line contains a title, comment, or filename. Remaining lines contain atom information. Each line starts with the element symbol, followed by x, y and z coordinates in angstroms separated by whitespace. Multiple molecules or frames can be contained within one file, so it supports trajectory storage. XYZ files can be directly represented by a molecular viewer, as they contain all the basic information needed to build the 3D model.""",
                meaning=EDAM["format_3877"]))
        setattr(cls, "edam:format_3878",
            PermissibleValue(
                text="edam:format_3878",
                title="mdcrd",
                description="""AMBER trajectory (also called mdcrd), with 10 coordinates per line and format F8.3 (fixed point notation with field width 8 and 3 decimal places).""",
                meaning=EDAM["format_3878"]))
        setattr(cls, "edam:format_3879",
            PermissibleValue(
                text="edam:format_3879",
                title="Topology format",
                description="""Format of topology files; containing the static information of a structure molecular system that is needed for a molecular simulation.
Many different file formats exist describing structural molecular topology. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS top, CHARMM psf, AMBER prmtop).""",
                meaning=EDAM["format_3879"]))
        setattr(cls, "edam:format_3880",
            PermissibleValue(
                text="edam:format_3880",
                title="GROMACS top",
                description="""GROMACS MD package top textual files define an entire structure system topology, either directly, or by including itp files.
There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package.""",
                meaning=EDAM["format_3880"]))
        setattr(cls, "edam:format_3881",
            PermissibleValue(
                text="edam:format_3881",
                title="AMBER top",
                description="""AMBER Prmtop file (version 7) is a structure topology text file divided in several sections designed to be parsed easily using simple Fortran code. Each section contains particular topology information, such as atom name, charge, mass, angles, dihedrals, etc.
It can be modified manually, but as the size of the system increases, the hand-editing becomes increasingly complex. AMBER Parameter-Topology file format is used extensively by the AMBER software suite and is referred to as the Prmtop file for short.
version 7 is written to distinguish it from old versions of AMBER Prmtop. Similarly to HDF5, it is a completely different format, according to AMBER group: a drastic change to the file format occurred with the 2004 release of Amber 7 (http://ambermd.org/prmtop.pdf)""",
                meaning=EDAM["format_3881"]))
        setattr(cls, "edam:format_3882",
            PermissibleValue(
                text="edam:format_3882",
                title="PSF",
                description="""The high similarity in the functional form of the two potential energy functions used by AMBER and CHARMM force-fields gives rise to the possible use of one force-field within the other MD engine. Therefore, the conversion of PSF files to AMBER Prmtop format is possible with the use of AMBER chamber (CHARMM - AMBER) program.
X-Plor Protein Structure Files (PSF) are structure topology files used by NAMD and CHARMM molecular simulations programs. PSF files contain six main sections of interest: atoms, bonds, angles, dihedrals, improper dihedrals (force terms used to maintain planarity) and cross-terms.""",
                meaning=EDAM["format_3882"]))
        setattr(cls, "edam:format_3883",
            PermissibleValue(
                text="edam:format_3883",
                title="GROMACS itp",
                description="""GROMACS itp files (include topology) contain structure topology information, and are typically included in GROMACS topology files (GROMACS top). Itp files are used to define individual (or multiple) components of a topology as a separate file. This is particularly useful if there is a molecule that is used frequently, and also reduces the size of the system topology file, splitting it in different parts.
GROMACS itp files are used also to define position restrictions on the molecule, or to define the force field parameters for a particular ligand.""",
                meaning=EDAM["format_3883"]))
        setattr(cls, "edam:format_3884",
            PermissibleValue(
                text="edam:format_3884",
                title="FF parameter format",
                description="""Format of force field parameter files, which store the set of parameters (charges, masses, radii, bond lengths, bond dihedrals, etc.) that are essential for the proper description and simulation of a molecular system.
Many different file formats exist describing force field parameters. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS itp, CHARMM rtf, AMBER off / frcmod).""",
                meaning=EDAM["format_3884"]))
        setattr(cls, "edam:format_3885",
            PermissibleValue(
                text="edam:format_3885",
                title="BinPos",
                description="""It is basically a translation of the ASCII atom coordinate format to binary code. The only additional information stored is a magic number that identifies the BinPos format and the number of atoms per snapshot. The remainder is the chain of coordinates binary encoded. A drawback of this format is its architecture dependency. Integers and floats codification depends on the architecture, thus it needs to be converted if working in different platforms (little endian, big endian).
Scripps Research Institute BinPos format is a binary formatted file to store atom coordinates.""",
                meaning=EDAM["format_3885"]))
        setattr(cls, "edam:format_3886",
            PermissibleValue(
                text="edam:format_3886",
                title="RST",
                description="""AMBER coordinate/restart file with 6 coordinates per line and decimal format F12.7 (fixed point notation with field width 12 and 7 decimal places).""",
                meaning=EDAM["format_3886"]))
        setattr(cls, "edam:format_3887",
            PermissibleValue(
                text="edam:format_3887",
                title="CHARMM rtf",
                description="""Format of CHARMM Residue Topology Files (RTF), which define groups by including the atoms, the properties of the group, and bond and charge information.
There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package.""",
                meaning=EDAM["format_3887"]))
        setattr(cls, "edam:format_3888",
            PermissibleValue(
                text="edam:format_3888",
                title="AMBER frcmod",
                description="""AMBER frcmod (Force field Modification) is a file format to store any modification to the standard force field needed for a particular molecule to be properly represented in the simulation.""",
                meaning=EDAM["format_3888"]))
        setattr(cls, "edam:format_3889",
            PermissibleValue(
                text="edam:format_3889",
                title="AMBER off",
                description="""AMBER Object File Format library files (OFF library files) store residue libraries (forcefield residue parameters).""",
                meaning=EDAM["format_3889"]))
        setattr(cls, "edam:format_3906",
            PermissibleValue(
                text="edam:format_3906",
                title="NMReDATA",
                description="""MReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or \"NMReDATA\") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc.
NMReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or \"NMReDATA\") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc. Find more in the paper at https://doi.org/10.1002/mrc.4527.""",
                meaning=EDAM["format_3906"]))
        setattr(cls, "edam:format_3909",
            PermissibleValue(
                text="edam:format_3909",
                title="BpForms",
                description="""BpForms is a string format for concretely representing the primary structures of biopolymers, including DNA, RNA, and proteins that include non-canonical nucleic and amino acids. See https://www.bpforms.org for more information.""",
                meaning=EDAM["format_3909"]))
        setattr(cls, "edam:format_3910",
            PermissibleValue(
                text="edam:format_3910",
                title="trr",
                description="""Format of trr files that contain the trajectory of a simulation experiment used by GROMACS.
The first 4 bytes of any trr file containing 1993. See https://github.com/galaxyproject/galaxy/pull/6597/files#diff-409951594551183dbf886e24de6cb129R760""",
                meaning=EDAM["format_3910"]))
        setattr(cls, "edam:format_3911",
            PermissibleValue(
                text="edam:format_3911",
                title="msh",
                description="""Mash sketch is a format for sequence / sequence checksum information. To make a sketch, each k-mer in a sequence is hashed, which creates a pseudo-random identifier. By sorting these hashes, a small subset from the top of the sorted list can represent the entire sequence.""",
                meaning=EDAM["format_3911"]))
        setattr(cls, "edam:format_3913",
            PermissibleValue(
                text="edam:format_3913",
                title="Loom",
                description="""The Loom file format is based on HDF5, a standard for storing large numerical datasets. The Loom format is designed to efficiently hold large omics datasets. Typically, such data takes the form of a large matrix of numbers, along with metadata for the rows and columns.""",
                meaning=EDAM["format_3913"]))
        setattr(cls, "edam:format_3915",
            PermissibleValue(
                text="edam:format_3915",
                title="Zarr",
                description="""The Zarr format is an implementation of chunked, compressed, N-dimensional arrays for storing data.""",
                meaning=EDAM["format_3915"]))
        setattr(cls, "edam:format_3916",
            PermissibleValue(
                text="edam:format_3916",
                title="MTX",
                description="""The Matrix Market matrix (MTX) format stores numerical or pattern matrices in a dense (array format) or sparse (coordinate format) representation.""",
                meaning=EDAM["format_3916"]))
        setattr(cls, "edam:format_3951",
            PermissibleValue(
                text="edam:format_3951",
                title="BcForms",
                description="""BcForms is a format for abstractly describing the molecular structure (atoms and bonds) of macromolecular complexes as a collection of subunits and crosslinks. Each subunit can be described with BpForms (http://edamontology.org/format_3909) or SMILES (http://edamontology.org/data_2301). BcForms uses an ontology of crosslinks to abstract the chemical details of crosslinks from the descriptions of complexes (see https://bpforms.org/crosslink.html).
BcForms is related to http://edamontology.org/format_3909. (BcForms uses BpForms to describe subunits which are DNA, RNA, or protein polymers.) However, that format isn't the parent of BcForms. BcForms is similarly related to SMILES (http://edamontology.org/data_2301).""",
                meaning=EDAM["format_3951"]))
        setattr(cls, "edam:format_3956",
            PermissibleValue(
                text="edam:format_3956",
                title="N-Quads",
                description="""N-Quads is a line-based, plain text format for encoding an RDF dataset. It includes information about the graph each triple belongs to.
N-Quads should not be confused with N-Triples which does not contain graph information.""",
                meaning=EDAM["format_3956"]))
        setattr(cls, "edam:format_3969",
            PermissibleValue(
                text="edam:format_3969",
                title="Vega",
                description="""Vega is a visualization grammar, a declarative language for creating, saving, and sharing interactive visualization designs. With Vega, you can describe the visual appearance and interactive behavior of a visualization in a JSON format, and generate web-based views using Canvas or SVG.""",
                meaning=EDAM["format_3969"]))
        setattr(cls, "edam:format_3970",
            PermissibleValue(
                text="edam:format_3970",
                title="Vega-lite",
                description="""Vega-Lite is a high-level grammar of interactive graphics. It provides a concise JSON syntax for rapidly generating visualizations to support analysis. Vega-Lite specifications can be compiled to Vega specifications.""",
                meaning=EDAM["format_3970"]))
        setattr(cls, "edam:format_3971",
            PermissibleValue(
                text="edam:format_3971",
                title="NeuroML",
                description="A model description language for computational neuroscience.",
                meaning=EDAM["format_3971"]))
        setattr(cls, "edam:format_3972",
            PermissibleValue(
                text="edam:format_3972",
                title="BNGL",
                description="""BioNetGen is a format for the specification and simulation of rule-based models of biochemical systems, including signal transduction, metabolic, and genetic regulatory networks.""",
                meaning=EDAM["format_3972"]))
        setattr(cls, "edam:format_3973",
            PermissibleValue(
                text="edam:format_3973",
                title="Docker image",
                description="""A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. An image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel.""",
                meaning=EDAM["format_3973"]))
        setattr(cls, "edam:format_3975",
            PermissibleValue(
                text="edam:format_3975",
                title="GFA 1",
                description="""Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology.""",
                meaning=EDAM["format_3975"]))
        setattr(cls, "edam:format_3976",
            PermissibleValue(
                text="edam:format_3976",
                title="GFA 2",
                description="""Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology. GFA2 is an update of GFA1 which is not compatible with GFA1.""",
                meaning=EDAM["format_3976"]))
        setattr(cls, "edam:format_3977",
            PermissibleValue(
                text="edam:format_3977",
                title="ObjTables",
                description="""ObjTables is a toolkit for creating re-usable datasets that are both human and machine-readable, combining the ease of spreadsheets (e.g., Excel workbooks) with the rigor of schemas (classes, their attributes, the type of each attribute, and the possible relationships between instances of classes). ObjTables consists of a format for describing schemas for spreadsheets, numerous data types for science, a syntax for indicating the class and attribute represented by each table and column in a workbook, and software for using schemas to rigorously validate, merge, split, compare, and revision datasets.""",
                meaning=EDAM["format_3977"]))
        setattr(cls, "edam:format_3978",
            PermissibleValue(
                text="edam:format_3978",
                title="CONTIG",
                description="""The CONTIG format used for output of the SOAPdenovo alignment program. It contains contig sequences generated without using mate pair information.""",
                meaning=EDAM["format_3978"]))
        setattr(cls, "edam:format_3979",
            PermissibleValue(
                text="edam:format_3979",
                title="WEGO",
                description="""WEGO native format used by the Web Gene Ontology Annotation Plot application.   Tab-delimited format with gene names and others GO IDs (columns) with one annotation record per line.""",
                meaning=EDAM["format_3979"]))
        setattr(cls, "edam:format_3980",
            PermissibleValue(
                text="edam:format_3980",
                title="RPKM",
                description="""For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
Tab-delimited format for gene expression levels table, calculated as Reads Per Kilobase per Million (RPKM) mapped reads.""",
                meaning=EDAM["format_3980"]))
        setattr(cls, "edam:format_3981",
            PermissibleValue(
                text="edam:format_3981",
                title="TAR format",
                description="""For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
TAR archive file format generated by the Unix-based utility tar.""",
                meaning=EDAM["format_3981"]))
        setattr(cls, "edam:format_3982",
            PermissibleValue(
                text="edam:format_3982",
                title="CHAIN",
                description="""The CHAIN format describes a pairwise alignment that allow gaps in both sequences simultaneously and is used by the UCSC Genome Browser.""",
                meaning=EDAM["format_3982"]))
        setattr(cls, "edam:format_3983",
            PermissibleValue(
                text="edam:format_3983",
                title="NET",
                description="""The NET file format is used to describe the data that underlie the net alignment annotations in the UCSC Genome Browser.""",
                meaning=EDAM["format_3983"]))
        setattr(cls, "edam:format_3984",
            PermissibleValue(
                text="edam:format_3984",
                title="QMAP",
                description="Format of QMAP files generated for methylation data from an internal BGI pipeline.",
                meaning=EDAM["format_3984"]))
        setattr(cls, "edam:format_3985",
            PermissibleValue(
                text="edam:format_3985",
                title="gxformat2",
                description="An emerging format for high-level Galaxy workflow description.",
                meaning=EDAM["format_3985"]))
        setattr(cls, "edam:format_3986",
            PermissibleValue(
                text="edam:format_3986",
                title="WMV",
                description="""The proprietary native video format of various Microsoft programs such as Windows Media Player.""",
                meaning=EDAM["format_3986"]))
        setattr(cls, "edam:format_3987",
            PermissibleValue(
                text="edam:format_3987",
                title="ZIP format",
                description="""A ZIP file may contain one or more files or directories that may have been compressed.
ZIP is an archive file format that supports lossless data compression.""",
                meaning=EDAM["format_3987"]))
        setattr(cls, "edam:format_3988",
            PermissibleValue(
                text="edam:format_3988",
                title="LSM",
                description="""LSM files are the default data export for the Zeiss LSM series confocal microscopes (e.g. LSM 510, LSM 710). In addition to the image data, LSM files contain most imaging settings.
Zeiss' proprietary image format based on TIFF.""",
                meaning=EDAM["format_3988"]))
        setattr(cls, "edam:format_3989",
            PermissibleValue(
                text="edam:format_3989",
                title="GZIP format",
                description="GNU zip compressed file format common to Unix-based operating systems.",
                meaning=EDAM["format_3989"]))
        setattr(cls, "edam:format_3990",
            PermissibleValue(
                text="edam:format_3990",
                title="AVI",
                description="""Audio Video Interleaved (AVI) format is a multimedia container format for AVI files, that allows synchronous audio-with-video playback.""",
                meaning=EDAM["format_3990"]))
        setattr(cls, "edam:format_3991",
            PermissibleValue(
                text="edam:format_3991",
                title="TrackDB",
                description="A declaration file format for UCSC browsers track dataset display charateristics.",
                meaning=EDAM["format_3991"]))
        setattr(cls, "edam:format_3992",
            PermissibleValue(
                text="edam:format_3992",
                title="CIGAR format",
                description="""Compact Idiosyncratic Gapped Alignment Report format is a compressed (run-length encoded) pairwise alignment format. It is useful for representing long (e.g. genomic) pairwise alignments.""",
                meaning=EDAM["format_3992"]))
        setattr(cls, "edam:format_3993",
            PermissibleValue(
                text="edam:format_3993",
                title="Stereolithography format",
                description="""STL is a file format native to the stereolithography CAD software created by 3D Systems. The format is used to save and share surface-rendered 3D images and also for 3D printing.""",
                meaning=EDAM["format_3993"]))
        setattr(cls, "edam:format_3994",
            PermissibleValue(
                text="edam:format_3994",
                title="U3D",
                description="""U3D (Universal 3D) is a compressed file format and data structure for 3D computer graphics. It contains 3D model information such as triangle meshes, lighting, shading, motion data, lines and points with color and structure.""",
                meaning=EDAM["format_3994"]))
        setattr(cls, "edam:format_3995",
            PermissibleValue(
                text="edam:format_3995",
                title="Texture file format",
                description="""Bitmap image format used for storing textures.
Texture files can create the appearance of different surfaces and can be applied to both 2D and 3D objects. Note the file extension .tex is also used for LaTex documents which are a completely different format and they are NOT interchangeable.""",
                meaning=EDAM["format_3995"]))
        setattr(cls, "edam:format_3996",
            PermissibleValue(
                text="edam:format_3996",
                title="Python script",
                description="""Format for scripts writtenin Python - a widely used high-level programming language for general-purpose programming.""",
                meaning=EDAM["format_3996"]))
        setattr(cls, "edam:format_3997",
            PermissibleValue(
                text="edam:format_3997",
                title="MPEG-4",
                description="A digital multimedia container format most commonly used to store video and audio.",
                meaning=EDAM["format_3997"]))
        setattr(cls, "edam:format_3998",
            PermissibleValue(
                text="edam:format_3998",
                title="Perl script",
                description="""Format for scripts written in Perl - a family of high-level, general-purpose, interpreted, dynamic programming languages.""",
                meaning=EDAM["format_3998"]))
        setattr(cls, "edam:format_3999",
            PermissibleValue(
                text="edam:format_3999",
                title="R script",
                description="""Format for scripts written in the R language - an open source programming language and software environment for statistical computing and graphics that is supported by the R Foundation for Statistical Computing.""",
                meaning=EDAM["format_3999"]))
        setattr(cls, "edam:format_4000",
            PermissibleValue(
                text="edam:format_4000",
                title="R markdown",
                description="A file format for making dynamic documents (R Markdown scripts) with the R language.",
                meaning=EDAM["format_4000"]))
        setattr(cls, "edam:format_4002",
            PermissibleValue(
                text="edam:format_4002",
                title="pickle",
                description="""Format used by Python pickle module for serializing and de-serializing a Python object structure.""",
                meaning=EDAM["format_4002"]))
        setattr(cls, "edam:format_4003",
            PermissibleValue(
                text="edam:format_4003",
                title="NumPy format",
                description="""The standard binary file format used by NumPy - a fundamental package for scientific computing with Python - for persisting a single arbitrary NumPy array on disk. The format stores all of the shape and dtype information necessary to reconstruct the array correctly.""",
                meaning=EDAM["format_4003"]))
        setattr(cls, "edam:format_4004",
            PermissibleValue(
                text="edam:format_4004",
                title="SimTools repertoire file format",
                description="""Format of repertoire (archive) files that can be read by SimToolbox (a MATLAB toolbox for structured illumination fluorescence microscopy) or alternatively extracted with zip file archiver software.""",
                meaning=EDAM["format_4004"]))
        setattr(cls, "edam:format_4005",
            PermissibleValue(
                text="edam:format_4005",
                title="Configuration file format",
                description="""A configuration file used by various programs to store settings that are specific to their respective software.""",
                meaning=EDAM["format_4005"]))
        setattr(cls, "edam:format_4006",
            PermissibleValue(
                text="edam:format_4006",
                title="Zstandard format",
                description="Format used by the Zstandard real-time compression algorithm.",
                meaning=EDAM["format_4006"]))
        setattr(cls, "edam:format_4007",
            PermissibleValue(
                text="edam:format_4007",
                title="MATLAB script",
                description="The file format for MATLAB scripts or functions.",
                meaning=EDAM["format_4007"]))
        setattr(cls, "edam:format_4015",
            PermissibleValue(
                text="edam:format_4015",
                title="PEtab",
                description="A data format for specifying parameter estimation problems in systems biology.",
                meaning=EDAM["format_4015"]))
        setattr(cls, "edam:format_4018",
            PermissibleValue(
                text="edam:format_4018",
                title="gVCF",
                description="""Genomic Variant Call Format (gVCF) is a version of VCF that includes not only the positions that are variant when compared to a reference genome, but also the non-variant positions as ranges, including metrics of confidence that the positions in the range are actually non-variant e.g. minimum read-depth and genotype quality.""",
                meaning=EDAM["format_4018"]))
        setattr(cls, "edam:format_4023",
            PermissibleValue(
                text="edam:format_4023",
                title="cml",
                description="""Chemical Markup Language (CML) is an XML-based format for encoding detailed information about a wide range of chemical concepts.""",
                meaning=EDAM["format_4023"]))
        setattr(cls, "edam:format_4024",
            PermissibleValue(
                text="edam:format_4024",
                title="cif",
                description="""Crystallographic Information File (CIF) is a data exchange standard file format for Crystallographic Information and related Structural Science data.""",
                meaning=EDAM["format_4024"]))
        setattr(cls, "edam:format_4025",
            PermissibleValue(
                text="edam:format_4025",
                title="BioSimulators format for the specifications of biosimulation tools",
                description="""Format for describing the capabilities of a biosimulation tool including the modeling frameworks, simulation algorithms, and modeling formats that it supports, as well as metadata such as a list of the interfaces, programming languages, and operating systems supported by the tool; a link to download the tool; a list of the authors of the tool; and the license to the tool.""",
                meaning=EDAM["format_4025"]))
        setattr(cls, "edam:format_4026",
            PermissibleValue(
                text="edam:format_4026",
                title="BioSimulators standard for command-line interfaces for biosimulation tools",
                description="""Outlines the syntax and semantics of the input and output arguments for command-line interfaces for biosimulation tools.""",
                meaning=EDAM["format_4026"]))
        setattr(cls, "edam:format_4035",
            PermissibleValue(
                text="edam:format_4035",
                title="PQR",
                description="""Data format derived from the standard PDB format, which enables user to incorporate parameters for charge and radius to the existing PDB data file.""",
                meaning=EDAM["format_4035"]))
        setattr(cls, "edam:format_4036",
            PermissibleValue(
                text="edam:format_4036",
                title="PDBQT",
                description="""Data format used in AutoDock 4 for storing atomic coordinates, partial atomic charges and AutoDock atom types for both receptors and ligands.""",
                meaning=EDAM["format_4036"]))
        setattr(cls, "edam:format_4039",
            PermissibleValue(
                text="edam:format_4039",
                title="MSP",
                description="""MSP is a data format for mass spectrometry data.
NIST Text file format for storing MS∕MS spectra (m∕z and intensity of mass peaks) along with additional annotations for each spectrum. A single MSP file can thus contain single or multiple spectra. This format is frequently used to share spectra libraries.""",
                meaning=EDAM["format_4039"]))
        setattr(cls, "edam:format_4041",
            PermissibleValue(
                text="edam:format_4041",
                title="maDMP",
                description="A standard for DMPs developed by the Research Data Alliance",
                meaning=EDAM["format_4041"]))
        setattr(cls, "edam:format_4048",
            PermissibleValue(
                text="edam:format_4048",
                title="Nextflow",
                description="""Nextflow is a workflow system for creating scalable, portable, and reproducible workflows.
This term covers all versions of Nextflow language specifications.""",
                meaning=EDAM["format_4048"]))
        setattr(cls, "edam:format_4049",
            PermissibleValue(
                text="edam:format_4049",
                title="Snakemake",
                description="""The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.""",
                meaning=EDAM["format_4049"]))
        setattr(cls, "edam:format_4050",
            PermissibleValue(
                text="edam:format_4050",
                title="SDRF",
                description="Sample and Data Relationship File for a proteomics experiment.",
                meaning=EDAM["format_4050"]))
        setattr(cls, "edam:format_4058",
            PermissibleValue(
                text="edam:format_4058",
                title="mzTab-M",
                description="""The reference implementation of mzTab-M in Java is https://github.com/lifs-tools/jmzTab-m.
mzTab-M is a light-weight, tab-delimited format for mass spectrometry-based chemical profiling data, including metabolomics.
mzTab-M is alternatively named mzTab 2.0, but in 2025 there is a draft version 2.1 of mzTab-M.
mzTab-M is not compatible with mzTab (also named mzTab 1.0, for proteomics, http://edamontology.org/format_3681). Note: the repository, website, and file extension are the same for both formats.""",
                meaning=EDAM["format_4058"]))
        setattr(cls, "edam:format_4059",
            PermissibleValue(
                text="edam:format_4059",
                title="mzTab-L",
                description="""mzTab-L is a light-weight, tab-delimited format for mass spectrometry-based lipidomics data. It is a compatible version of mzTab-M, with additional rules and information standard (reporting guidelines).""",
                meaning=EDAM["format_4059"]))

class EnumEDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "edam:data_0582",
            PermissibleValue(
                text="edam:data_0582",
                title="Ontology",
                description="""An ontology of biological or bioinformatics concepts and relations, a controlled vocabulary, structured glossary etc.""",
                meaning=EDAM["data_0582"]))
        setattr(cls, "edam:data_0842",
            PermissibleValue(
                text="edam:data_0842",
                title="Identifier",
                description="""A text token, number or something else which identifies an entity, but which may not be persistent (stable) or unique (the same identifier may identify multiple things).""",
                meaning=EDAM["data_0842"]))
        setattr(cls, "edam:data_0844",
            PermissibleValue(
                text="edam:data_0844",
                title="Molecular mass",
                description="Mass of a molecule.",
                meaning=EDAM["data_0844"]))
        setattr(cls, "edam:data_0845",
            PermissibleValue(
                text="edam:data_0845",
                title="Molecular charge",
                description="Net charge of a molecule.",
                meaning=EDAM["data_0845"]))
        setattr(cls, "edam:data_0846",
            PermissibleValue(
                text="edam:data_0846",
                title="Chemical formula",
                description="A specification of a chemical structure.",
                meaning=EDAM["data_0846"]))
        setattr(cls, "edam:data_0847",
            PermissibleValue(
                text="edam:data_0847",
                title="QSAR descriptor",
                description="""A QSAR quantitative descriptor (name-value pair) of chemical structure.
QSAR descriptors have numeric values that quantify chemical information encoded in a symbolic representation of a molecule. They are used in quantitative structure activity relationship (QSAR) applications. Many subtypes of individual descriptors (not included in EDAM) cover various types of protein properties.""",
                meaning=EDAM["data_0847"]))
        setattr(cls, "edam:data_0849",
            PermissibleValue(
                text="edam:data_0849",
                title="Sequence record",
                description="A molecular sequence and associated metadata.",
                meaning=EDAM["data_0849"]))
        setattr(cls, "edam:data_0850",
            PermissibleValue(
                text="edam:data_0850",
                title="Sequence set",
                description="""A collection of one or typically multiple molecular sequences (which can include derived data or metadata) that do not (typically) correspond to molecular sequence database records or entries and which (typically) are derived from some analytical method.
An example is an alignment reference; one or a set of reference molecular sequences, structures, or profiles used for alignment of genomic, transcriptomic, or proteomic experimental data.
This concept may be used for arbitrary sequence sets and associated data arising from processing.""",
                meaning=EDAM["data_0850"]))
        setattr(cls, "edam:data_0856",
            PermissibleValue(
                text="edam:data_0856",
                title="Sequence feature source",
                description="""How the annotation of a sequence feature (for example in EMBL or Swiss-Prot) was derived.
This might be the name and version of a software tool, the name of a database, or 'curated' to indicate a manual annotation (made by a human).""",
                meaning=EDAM["data_0856"]))
        setattr(cls, "edam:data_0857",
            PermissibleValue(
                text="edam:data_0857",
                title="Sequence search results",
                description="""A report of sequence hits and associated data from searching a database of sequences (for example a BLAST search). This will typically include a list of scores (often with statistical evaluation) and a set of alignments for the hits.
The score list includes the alignment score, percentage of the query sequence matched, length of the database sequence entry in this alignment, identifier of the database sequence entry, excerpt of the database sequence entry description etc.""",
                meaning=EDAM["data_0857"]))
        setattr(cls, "edam:data_0858",
            PermissibleValue(
                text="edam:data_0858",
                title="Sequence signature matches",
                description="""A \"profile-profile alignment\" is an alignment of two sequence profiles, each profile typically representing a sequence alignment.
A \"sequence-profile alignment\" is an alignment of one or more molecular sequence(s) to one or more sequence profile(s) (each profile typically representing a sequence alignment).
Report on the location of matches (\"hits\") between sequences, sequence profiles, motifs (conserved or functional patterns) and other types of sequence signatures.
This includes reports of hits from a search of a protein secondary or domain database. Data associated with the search or alignment might also be included, e.g. ranked list of best-scoring sequences, a graphical representation of scores etc.""",
                meaning=EDAM["data_0858"]))
        setattr(cls, "edam:data_0860",
            PermissibleValue(
                text="edam:data_0860",
                title="Sequence signature data",
                description="""Sequence signature data concerns specific or conserved pattern in molecular sequences and the classifiers used for their identification, including sequence motifs, profiles or other diagnostic element.
This can include metadata about a motif or sequence profile such as its name, length, technical details about the profile construction, and so on.""",
                meaning=EDAM["data_0860"]))
        setattr(cls, "edam:data_0862",
            PermissibleValue(
                text="edam:data_0862",
                title="Dotplot",
                description="""A dotplot of sequence similarities identified from word-matching or character comparison.""",
                meaning=EDAM["data_0862"]))
        setattr(cls, "edam:data_0863",
            PermissibleValue(
                text="edam:data_0863",
                title="Sequence alignment",
                description="Alignment of multiple molecular sequences.",
                meaning=EDAM["data_0863"]))
        setattr(cls, "edam:data_0865",
            PermissibleValue(
                text="edam:data_0865",
                title="Sequence similarity score",
                description="A value representing molecular sequence similarity.",
                meaning=EDAM["data_0865"]))
        setattr(cls, "edam:data_0867",
            PermissibleValue(
                text="edam:data_0867",
                title="Sequence alignment report",
                description="""An informative report of molecular sequence alignment-derived data or metadata.
Use this for any computer-generated reports on sequence alignments, and for general information (metadata) on a sequence alignment, such as a description, sequence identifiers and alignment score.""",
                meaning=EDAM["data_0867"]))
        setattr(cls, "edam:data_0870",
            PermissibleValue(
                text="edam:data_0870",
                title="Sequence distance matrix",
                description="""A matrix of estimated evolutionary distance between molecular sequences, such as is suitable for phylogenetic tree calculation.
Methods might perform character compatibility analysis or identify patterns of similarity in an alignment or data matrix.""",
                meaning=EDAM["data_0870"]))
        setattr(cls, "edam:data_0871",
            PermissibleValue(
                text="edam:data_0871",
                title="Phylogenetic character data",
                description="""As defined, this concept would also include molecular sequences, microsatellites, polymorphisms (RAPDs, RFLPs, or AFLPs), restriction sites and fragments
Basic character data from which a phylogenetic tree may be generated.""",
                meaning=EDAM["data_0871"]))
        setattr(cls, "edam:data_0872",
            PermissibleValue(
                text="edam:data_0872",
                title="Phylogenetic tree",
                description="""A phylogenetic tree is usually constructed from a set of sequences from which an alignment (or data matrix) is calculated. See also 'Phylogenetic tree image'.
The raw data (not just an image) from which a phylogenetic tree is directly generated or plotted, such as topology, lengths (in time or in expected amounts of variance) and a confidence interval for each length.""",
                meaning=EDAM["data_0872"]))
        setattr(cls, "edam:data_0874",
            PermissibleValue(
                text="edam:data_0874",
                title="Comparison matrix",
                description="""Matrix of integer or floating point numbers for amino acid or nucleotide sequence comparison.
The comparison matrix might include matrix name, optional comment, height and width (or size) of matrix, an index row/column (of characters) and data rows/columns (of integers or floats).""",
                meaning=EDAM["data_0874"]))
        setattr(cls, "edam:data_0878",
            PermissibleValue(
                text="edam:data_0878",
                title="Protein secondary structure alignment",
                description="Alignment of the (1D representations of) secondary structure of two or more proteins.",
                meaning=EDAM["data_0878"]))
        setattr(cls, "edam:data_0880",
            PermissibleValue(
                text="edam:data_0880",
                title="RNA secondary structure",
                description="""An informative report of secondary structure (predicted or real) of an RNA molecule.
This includes thermodynamically stable or evolutionarily conserved structures such as knots, pseudoknots etc.""",
                meaning=EDAM["data_0880"]))
        setattr(cls, "edam:data_0881",
            PermissibleValue(
                text="edam:data_0881",
                title="RNA secondary structure alignment",
                description="""Alignment of the (1D representations of) secondary structure of two or more RNA molecules.""",
                meaning=EDAM["data_0881"]))
        setattr(cls, "edam:data_0883",
            PermissibleValue(
                text="edam:data_0883",
                title="Structure",
                description="""3D coordinate and associated data for a macromolecular tertiary (3D) structure or part of a structure.
The coordinate data may be predicted or real.""",
                meaning=EDAM["data_0883"]))
        setattr(cls, "edam:data_0886",
            PermissibleValue(
                text="edam:data_0886",
                title="Structure alignment",
                description="""A tertiary structure alignment will include the untransformed coordinates of one macromolecule, followed by the second (or subsequent) structure(s) with all the coordinates transformed (by rotation / translation) to give a superposition.
Alignment (superimposition) of molecular tertiary (3D) structures.""",
                meaning=EDAM["data_0886"]))
        setattr(cls, "edam:data_0887",
            PermissibleValue(
                text="edam:data_0887",
                title="Structure alignment report",
                description="""An informative report of molecular tertiary structure alignment-derived data.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_0887"]))
        setattr(cls, "edam:data_0888",
            PermissibleValue(
                text="edam:data_0888",
                title="Structure similarity score",
                description="""A value representing molecular structure similarity, measured from structure alignment or some other type of structure comparison.""",
                meaning=EDAM["data_0888"]))
        setattr(cls, "edam:data_0889",
            PermissibleValue(
                text="edam:data_0889",
                title="Structural profile",
                description="""Some type of structural (3D) profile or template (representing a structure or structure alignment).""",
                meaning=EDAM["data_0889"]))
        setattr(cls, "edam:data_0890",
            PermissibleValue(
                text="edam:data_0890",
                title="Structural (3D) profile alignment",
                description="""A 3D profile-3D profile alignment (each profile representing structures or a structure alignment).""",
                meaning=EDAM["data_0890"]))
        setattr(cls, "edam:data_0892",
            PermissibleValue(
                text="edam:data_0892",
                title="Protein sequence-structure scoring matrix",
                description="Matrix of values used for scoring sequence-structure compatibility.",
                meaning=EDAM["data_0892"]))
        setattr(cls, "edam:data_0893",
            PermissibleValue(
                text="edam:data_0893",
                title="Sequence-structure alignment",
                description="""An alignment of molecular sequence to structure (from threading sequence(s) through 3D structure or representation of structure(s)).""",
                meaning=EDAM["data_0893"]))
        setattr(cls, "edam:data_0896",
            PermissibleValue(
                text="edam:data_0896",
                title="Protein report",
                description="""An informative human-readable report about one or more specific protein molecules or protein structural domains, derived from analysis of primary (sequence or structural) data.""",
                meaning=EDAM["data_0896"]))
        setattr(cls, "edam:data_0897",
            PermissibleValue(
                text="edam:data_0897",
                title="Protein property",
                description="""A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a protein molecule or model.
This is a broad data type and is used a placeholder for other, more specific types. Data may be based on analysis of nucleic acid sequence or structural data, for example reports on the surface properties (shape, hydropathy, electrostatic patches etc) of a protein structure, protein flexibility or motion, and protein architecture (spatial arrangement of secondary structure).""",
                meaning=EDAM["data_0897"]))
        setattr(cls, "edam:data_0905",
            PermissibleValue(
                text="edam:data_0905",
                title="Protein interaction raw data",
                description="""Protein-protein interaction data from for example yeast two-hybrid analysis, protein microarrays, immunoaffinity chromatography followed by mass spectrometry, phage display etc.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.""",
                meaning=EDAM["data_0905"]))
        setattr(cls, "edam:data_0906",
            PermissibleValue(
                text="edam:data_0906",
                title="Protein interaction data",
                description="""Data concerning the interactions (predicted or known) within or between a protein, structural domain or part of a protein. This includes intra- and inter-residue contacts and distances, as well as interactions with other proteins and non-protein entities such as nucleic acid, metal atoms, water, ions etc.""",
                meaning=EDAM["data_0906"]))
        setattr(cls, "edam:data_0907",
            PermissibleValue(
                text="edam:data_0907",
                title="Protein family report",
                description="""An informative report on a specific protein family or other classification or group of protein sequences or structures.""",
                meaning=EDAM["data_0907"]))
        setattr(cls, "edam:data_0909",
            PermissibleValue(
                text="edam:data_0909",
                title="Vmax",
                description="""The maximum initial velocity or rate of a reaction. It is the limiting velocity as substrate concentrations get very large.""",
                meaning=EDAM["data_0909"]))
        setattr(cls, "edam:data_0910",
            PermissibleValue(
                text="edam:data_0910",
                title="Km",
                description="""Km is the concentration (usually in Molar units) of substrate that leads to half-maximal velocity of an enzyme-catalysed reaction.""",
                meaning=EDAM["data_0910"]))
        setattr(cls, "edam:data_0912",
            PermissibleValue(
                text="edam:data_0912",
                title="Nucleic acid property",
                description="""A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a nucleic acid molecule.
Nucleic acid structural properties stiffness, curvature, twist/roll data or other conformational parameters or properties.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_0912"]))
        setattr(cls, "edam:data_0914",
            PermissibleValue(
                text="edam:data_0914",
                title="Codon usage data",
                description="""Data derived from analysis of codon usage (typically a codon usage table) of DNA sequences.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_0914"]))
        setattr(cls, "edam:data_0916",
            PermissibleValue(
                text="edam:data_0916",
                title="Gene report",
                description="""A report on predicted or actual gene structure, regions which make an RNA product and features such as promoters, coding regions, splice sites etc.
This includes any report on a particular locus or gene. This might include the gene name, description, summary and so on. It can include details about the function of a gene, such as its encoded protein or a functional classification of the gene sequence along according to the encoded protein(s).""",
                meaning=EDAM["data_0916"]))
        setattr(cls, "edam:data_0919",
            PermissibleValue(
                text="edam:data_0919",
                title="Chromosome report",
                description="""A human-readable collection of information about a specific chromosome.
This includes basic information. e.g. chromosome number, length, karyotype features, chromosome sequence etc.""",
                meaning=EDAM["data_0919"]))
        setattr(cls, "edam:data_0920",
            PermissibleValue(
                text="edam:data_0920",
                title="Genotype/phenotype report",
                description="""A human-readable collection of information about the set of genes (or allelic forms) present in an individual, organism or cell and associated with a specific physical characteristic, or a report concerning an organisms traits and phenotypes.""",
                meaning=EDAM["data_0920"]))
        setattr(cls, "edam:data_0924",
            PermissibleValue(
                text="edam:data_0924",
                title="Sequence trace",
                description="""Fluorescence trace data generated by an automated DNA sequencer, which can be interpreted as a molecular sequence (reads), given associated sequencing metadata such as base-call quality scores.
This is the raw data produced by a DNA sequencing machine.""",
                meaning=EDAM["data_0924"]))
        setattr(cls, "edam:data_0925",
            PermissibleValue(
                text="edam:data_0925",
                title="Sequence assembly",
                description="""An assembly of fragments of a (typically genomic) DNA sequence.
Typically, an assembly is a collection of contigs (for example ESTs and genomic DNA fragments) that are ordered, aligned and merged. Annotation of the assembled sequence might be included.""",
                meaning=EDAM["data_0925"]))
        setattr(cls, "edam:data_0926",
            PermissibleValue(
                text="edam:data_0926",
                title="RH scores",
                description="""Radiation Hybrid (RH) scores are used in Radiation Hybrid mapping.
Radiation hybrid scores (RH) scores for one or more markers.""",
                meaning=EDAM["data_0926"]))
        setattr(cls, "edam:data_0927",
            PermissibleValue(
                text="edam:data_0927",
                title="Genetic linkage report",
                description="""A human-readable collection of information about the linkage of alleles.
This includes linkage disequilibrium; the non-random association of alleles or polymorphisms at two or more loci (not necessarily on the same chromosome).""",
                meaning=EDAM["data_0927"]))
        setattr(cls, "edam:data_0928",
            PermissibleValue(
                text="edam:data_0928",
                title="Gene expression profile",
                description="""Data quantifying the level of expression of (typically) multiple genes, derived for example from microarray experiments.""",
                meaning=EDAM["data_0928"]))
        setattr(cls, "edam:data_0937",
            PermissibleValue(
                text="edam:data_0937",
                title="Electron density map",
                description="X-ray crystallography data.",
                meaning=EDAM["data_0937"]))
        setattr(cls, "edam:data_0938",
            PermissibleValue(
                text="edam:data_0938",
                title="Raw NMR data",
                description="Nuclear magnetic resonance (NMR) raw data, typically for a protein.",
                meaning=EDAM["data_0938"]))
        setattr(cls, "edam:data_0939",
            PermissibleValue(
                text="edam:data_0939",
                title="CD spectra",
                description="""Protein secondary structure from protein coordinate or circular dichroism (CD) spectroscopic data.""",
                meaning=EDAM["data_0939"]))
        setattr(cls, "edam:data_0940",
            PermissibleValue(
                text="edam:data_0940",
                title="Volume map",
                description="Volume map data from electron microscopy.",
                meaning=EDAM["data_0940"]))
        setattr(cls, "edam:data_0942",
            PermissibleValue(
                text="edam:data_0942",
                title="2D PAGE image",
                description="Two-dimensional gel electrophoresis image.",
                meaning=EDAM["data_0942"]))
        setattr(cls, "edam:data_0943",
            PermissibleValue(
                text="edam:data_0943",
                title="Mass spectrum",
                description="Spectra from mass spectrometry.",
                meaning=EDAM["data_0943"]))
        setattr(cls, "edam:data_0944",
            PermissibleValue(
                text="edam:data_0944",
                title="Peptide mass fingerprint",
                description="""A molecular weight standard fingerprint is standard protonated molecular masses e.g. from trypsin (modified porcine trypsin, Promega) and keratin peptides.
A set of peptide masses (peptide mass fingerprint) from mass spectrometry.""",
                meaning=EDAM["data_0944"]))
        setattr(cls, "edam:data_0945",
            PermissibleValue(
                text="edam:data_0945",
                title="Peptide identification",
                description="""Protein or peptide identifications with evidence supporting the identifications, for example from comparing a peptide mass fingerprint (from mass spectrometry) to a sequence database, or the set of typical spectra one obtains when running a protein through a mass spectrometer.""",
                meaning=EDAM["data_0945"]))
        setattr(cls, "edam:data_0949",
            PermissibleValue(
                text="edam:data_0949",
                title="Workflow metadata",
                description="""Basic information, annotation or documentation concerning a workflow (but not the workflow itself).""",
                meaning=EDAM["data_0949"]))
        setattr(cls, "edam:data_0950",
            PermissibleValue(
                text="edam:data_0950",
                title="Mathematical model",
                description="A biological model represented in mathematical terms.",
                meaning=EDAM["data_0950"]))
        setattr(cls, "edam:data_0951",
            PermissibleValue(
                text="edam:data_0951",
                title="Statistical estimate score",
                description="""A value representing estimated statistical significance of some observed data; typically sequence database hits.""",
                meaning=EDAM["data_0951"]))
        setattr(cls, "edam:data_0954",
            PermissibleValue(
                text="edam:data_0954",
                title="Database cross-mapping",
                description="""A mapping of the accession numbers (or other database identifier) of entries between (typically) two biological or biomedical databases.
The cross-mapping is typically a table where each row is an accession number and each column is a database being cross-referenced. The cells give the accession number or identifier of the corresponding entry in a database. If a cell in the table is not filled then no mapping could be found for the database. Additional information might be given on version, date etc.""",
                meaning=EDAM["data_0954"]))
        setattr(cls, "edam:data_0955",
            PermissibleValue(
                text="edam:data_0955",
                title="Data index",
                description="An index of data of biological relevance.",
                meaning=EDAM["data_0955"]))
        setattr(cls, "edam:data_0956",
            PermissibleValue(
                text="edam:data_0956",
                title="Data index report",
                description="""A human-readable collection of information concerning an analysis of an index of biological data.""",
                meaning=EDAM["data_0956"]))
        setattr(cls, "edam:data_0957",
            PermissibleValue(
                text="edam:data_0957",
                title="Database metadata",
                description="""Basic information on bioinformatics database(s) or other data sources such as name, type, description, URL etc.""",
                meaning=EDAM["data_0957"]))
        setattr(cls, "edam:data_0958",
            PermissibleValue(
                text="edam:data_0958",
                title="Tool metadata",
                description="""Basic information about one or more bioinformatics applications or packages, such as name, type, description, or other documentation.""",
                meaning=EDAM["data_0958"]))
        setattr(cls, "edam:data_0960",
            PermissibleValue(
                text="edam:data_0960",
                title="User metadata",
                description="""Textual metadata on a software author or end-user, for example a person or other software.""",
                meaning=EDAM["data_0960"]))
        setattr(cls, "edam:data_0962",
            PermissibleValue(
                text="edam:data_0962",
                title="Small molecule report",
                description="A human-readable collection of information about a specific chemical compound.",
                meaning=EDAM["data_0962"]))
        setattr(cls, "edam:data_0963",
            PermissibleValue(
                text="edam:data_0963",
                title="Cell line report",
                description="""A human-readable collection of information about a particular strain of organism cell line including plants, virus, fungi and bacteria. The data typically includes strain number, organism type, growth conditions, source and so on.""",
                meaning=EDAM["data_0963"]))
        setattr(cls, "edam:data_0966",
            PermissibleValue(
                text="edam:data_0966",
                title="Ontology term",
                description="A term (name) from an ontology.",
                meaning=EDAM["data_0966"]))
        setattr(cls, "edam:data_0967",
            PermissibleValue(
                text="edam:data_0967",
                title="Ontology concept data",
                description="Data concerning or derived from a concept from a biological ontology.",
                meaning=EDAM["data_0967"]))
        setattr(cls, "edam:data_0968",
            PermissibleValue(
                text="edam:data_0968",
                title="Keyword",
                description="""Boolean operators (AND, OR and NOT) and wildcard characters may be allowed.
Keyword(s) or phrase(s) used (typically) for text-searching purposes.""",
                meaning=EDAM["data_0968"]))
        setattr(cls, "edam:data_0970",
            PermissibleValue(
                text="edam:data_0970",
                title="Citation",
                description="""A bibliographic reference might include information such as authors, title, journal name, date and (possibly) a link to the abstract or full-text of the article if available.
Bibliographic data that uniquely identifies a scientific article, book or other published material.""",
                meaning=EDAM["data_0970"]))
        setattr(cls, "edam:data_0971",
            PermissibleValue(
                text="edam:data_0971",
                title="Article",
                description="A scientific text, typically a full text article from a scientific journal.",
                meaning=EDAM["data_0971"]))
        setattr(cls, "edam:data_0972",
            PermissibleValue(
                text="edam:data_0972",
                title="Text mining report",
                description="""A human-readable collection of information resulting from text mining.
A text mining abstract will typically include an annotated a list of words or sentences extracted from one or more scientific articles.""",
                meaning=EDAM["data_0972"]))
        setattr(cls, "edam:data_0976",
            PermissibleValue(
                text="edam:data_0976",
                title="Identifier (by type of entity)",
                description="""An identifier that identifies a particular type of data.
This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'.""",
                meaning=EDAM["data_0976"]))
        setattr(cls, "edam:data_0977",
            PermissibleValue(
                text="edam:data_0977",
                title="Tool identifier",
                description="An identifier of a bioinformatics tool, e.g. an application or web service.",
                meaning=EDAM["data_0977"]))
        setattr(cls, "edam:data_0982",
            PermissibleValue(
                text="edam:data_0982",
                title="Molecule identifier",
                description="Name or other identifier of a molecule.",
                meaning=EDAM["data_0982"]))
        setattr(cls, "edam:data_0983",
            PermissibleValue(
                text="edam:data_0983",
                title="Atom ID",
                description="Identifier (e.g. character symbol) of a specific atom.",
                meaning=EDAM["data_0983"]))
        setattr(cls, "edam:data_0984",
            PermissibleValue(
                text="edam:data_0984",
                title="Molecule name",
                description="Name of a specific molecule.",
                meaning=EDAM["data_0984"]))
        setattr(cls, "edam:data_0987",
            PermissibleValue(
                text="edam:data_0987",
                title="Chromosome name",
                description="Name of a chromosome.",
                meaning=EDAM["data_0987"]))
        setattr(cls, "edam:data_0988",
            PermissibleValue(
                text="edam:data_0988",
                title="Peptide identifier",
                description="Identifier of a peptide chain.",
                meaning=EDAM["data_0988"]))
        setattr(cls, "edam:data_0989",
            PermissibleValue(
                text="edam:data_0989",
                title="Protein identifier",
                description="Identifier of a protein.",
                meaning=EDAM["data_0989"]))
        setattr(cls, "edam:data_0990",
            PermissibleValue(
                text="edam:data_0990",
                title="Compound name",
                description="Unique name of a chemical compound.",
                meaning=EDAM["data_0990"]))
        setattr(cls, "edam:data_0991",
            PermissibleValue(
                text="edam:data_0991",
                title="Chemical registry number",
                description="Unique registry number of a chemical compound.",
                meaning=EDAM["data_0991"]))
        setattr(cls, "edam:data_0993",
            PermissibleValue(
                text="edam:data_0993",
                title="Drug identifier",
                description="Identifier of a drug.",
                meaning=EDAM["data_0993"]))
        setattr(cls, "edam:data_0994",
            PermissibleValue(
                text="edam:data_0994",
                title="Amino acid identifier",
                description="Identifier of an amino acid.",
                meaning=EDAM["data_0994"]))
        setattr(cls, "edam:data_0995",
            PermissibleValue(
                text="edam:data_0995",
                title="Nucleotide identifier",
                description="Name or other identifier of a nucleotide.",
                meaning=EDAM["data_0995"]))
        setattr(cls, "edam:data_0996",
            PermissibleValue(
                text="edam:data_0996",
                title="Monosaccharide identifier",
                description="Identifier of a monosaccharide.",
                meaning=EDAM["data_0996"]))
        setattr(cls, "edam:data_0997",
            PermissibleValue(
                text="edam:data_0997",
                title="Chemical name (ChEBI)",
                description="""This is the recommended chemical name for use for example in database annotation.
Unique name from Chemical Entities of Biological Interest (ChEBI) of a chemical compound.""",
                meaning=EDAM["data_0997"]))
        setattr(cls, "edam:data_0998",
            PermissibleValue(
                text="edam:data_0998",
                title="Chemical name (IUPAC)",
                description="IUPAC recommended name of a chemical compound.",
                meaning=EDAM["data_0998"]))
        setattr(cls, "edam:data_0999",
            PermissibleValue(
                text="edam:data_0999",
                title="Chemical name (INN)",
                description="""International Non-proprietary Name (INN or 'generic name') of a chemical compound, assigned by the World Health Organisation (WHO).""",
                meaning=EDAM["data_0999"]))
        setattr(cls, "edam:data_1000",
            PermissibleValue(
                text="edam:data_1000",
                title="Chemical name (brand)",
                description="Brand name of a chemical compound.",
                meaning=EDAM["data_1000"]))
        setattr(cls, "edam:data_1001",
            PermissibleValue(
                text="edam:data_1001",
                title="Chemical name (synonymous)",
                description="Synonymous name of a chemical compound.",
                meaning=EDAM["data_1001"]))
        setattr(cls, "edam:data_1002",
            PermissibleValue(
                text="edam:data_1002",
                title="CAS number",
                description="""CAS registry number of a chemical compound; a unique numerical identifier of chemicals in the scientific literature, as assigned by the Chemical Abstracts Service.""",
                meaning=EDAM["data_1002"]))
        setattr(cls, "edam:data_1003",
            PermissibleValue(
                text="edam:data_1003",
                title="Chemical registry number (Beilstein)",
                description="Beilstein registry number of a chemical compound.",
                meaning=EDAM["data_1003"]))
        setattr(cls, "edam:data_1004",
            PermissibleValue(
                text="edam:data_1004",
                title="Chemical registry number (Gmelin)",
                description="Gmelin registry number of a chemical compound.",
                meaning=EDAM["data_1004"]))
        setattr(cls, "edam:data_1005",
            PermissibleValue(
                text="edam:data_1005",
                title="HET group name",
                description="3-letter code word for a ligand (HET group) from a PDB file, for example ATP.",
                meaning=EDAM["data_1005"]))
        setattr(cls, "edam:data_1006",
            PermissibleValue(
                text="edam:data_1006",
                title="Amino acid name",
                description="String of one or more ASCII characters representing an amino acid.",
                meaning=EDAM["data_1006"]))
        setattr(cls, "edam:data_1007",
            PermissibleValue(
                text="edam:data_1007",
                title="Nucleotide code",
                description="String of one or more ASCII characters representing a nucleotide.",
                meaning=EDAM["data_1007"]))
        setattr(cls, "edam:data_1008",
            PermissibleValue(
                text="edam:data_1008",
                title="Polypeptide chain ID",
                description="""Identifier of a polypeptide chain from a protein.
This is typically a character (for the chain) appended to a PDB identifier, e.g. 1cukA""",
                meaning=EDAM["data_1008"]))
        setattr(cls, "edam:data_1009",
            PermissibleValue(
                text="edam:data_1009",
                title="Protein name",
                description="Name of a protein.",
                meaning=EDAM["data_1009"]))
        setattr(cls, "edam:data_1010",
            PermissibleValue(
                text="edam:data_1010",
                title="Enzyme identifier",
                description="Name or other identifier of an enzyme or record from a database of enzymes.",
                meaning=EDAM["data_1010"]))
        setattr(cls, "edam:data_1011",
            PermissibleValue(
                text="edam:data_1011",
                title="EC number",
                description="An Enzyme Commission (EC) number of an enzyme.",
                meaning=EDAM["data_1011"]))
        setattr(cls, "edam:data_1012",
            PermissibleValue(
                text="edam:data_1012",
                title="Enzyme name",
                description="Name of an enzyme.",
                meaning=EDAM["data_1012"]))
        setattr(cls, "edam:data_1013",
            PermissibleValue(
                text="edam:data_1013",
                title="Restriction enzyme name",
                description="Name of a restriction enzyme.",
                meaning=EDAM["data_1013"]))
        setattr(cls, "edam:data_1015",
            PermissibleValue(
                text="edam:data_1015",
                title="Sequence feature ID",
                description="""A unique identifier of molecular sequence feature, for example an ID of a feature that is unique within the scope of the GFF file.""",
                meaning=EDAM["data_1015"]))
        setattr(cls, "edam:data_1016",
            PermissibleValue(
                text="edam:data_1016",
                title="Sequence position",
                description="""A position of one or more points (base or residue) in a sequence, or part of such a specification.""",
                meaning=EDAM["data_1016"]))
        setattr(cls, "edam:data_1017",
            PermissibleValue(
                text="edam:data_1017",
                title="Sequence range",
                description="Specification of range(s) of sequence positions.",
                meaning=EDAM["data_1017"]))
        setattr(cls, "edam:data_1020",
            PermissibleValue(
                text="edam:data_1020",
                title="Sequence feature key",
                description="""A feature key indicates the biological nature of the feature or information about changes to or versions of the sequence.
The type of a sequence feature, typically a term or accession from the Sequence Ontology, for example an EMBL or Swiss-Prot sequence feature key.""",
                meaning=EDAM["data_1020"]))
        setattr(cls, "edam:data_1021",
            PermissibleValue(
                text="edam:data_1021",
                title="Sequence feature qualifier",
                description="""Feature qualifiers hold information about a feature beyond that provided by the feature key and location.
Typically one of the EMBL or Swiss-Prot feature qualifiers.""",
                meaning=EDAM["data_1021"]))
        setattr(cls, "edam:data_1022",
            PermissibleValue(
                text="edam:data_1022",
                title="Sequence feature label",
                description="""A feature label identifies a feature of a sequence database entry. When used with the database name and the entry's primary accession number, it is a unique identifier of that feature.
A name of a sequence feature, e.g. the name of a feature to be displayed to an end-user. Typically an EMBL or Swiss-Prot feature label.""",
                meaning=EDAM["data_1022"]))
        setattr(cls, "edam:data_1023",
            PermissibleValue(
                text="edam:data_1023",
                title="EMBOSS Uniform Feature Object",
                description="""The name of a sequence feature-containing entity adhering to the standard feature naming scheme used by all EMBOSS applications.""",
                meaning=EDAM["data_1023"]))
        setattr(cls, "edam:data_1025",
            PermissibleValue(
                text="edam:data_1025",
                title="Gene identifier",
                description="""An identifier of a gene, such as a name/symbol or a unique identifier of a gene in a database.""",
                meaning=EDAM["data_1025"]))
        setattr(cls, "edam:data_1026",
            PermissibleValue(
                text="edam:data_1026",
                title="Gene symbol",
                description="""The short name of a gene; a single word that does not contain white space characters. It is typically derived from the gene name.""",
                meaning=EDAM["data_1026"]))
        setattr(cls, "edam:data_1027",
            PermissibleValue(
                text="edam:data_1027",
                title="Gene ID (NCBI)",
                description="An NCBI unique identifier of a gene.",
                meaning=EDAM["data_1027"]))
        setattr(cls, "edam:data_1031",
            PermissibleValue(
                text="edam:data_1031",
                title="Gene ID (CGD)",
                description="Identifier of a gene or feature from the CGD database.",
                meaning=EDAM["data_1031"]))
        setattr(cls, "edam:data_1032",
            PermissibleValue(
                text="edam:data_1032",
                title="Gene ID (DictyBase)",
                description="Identifier of a gene from DictyBase.",
                meaning=EDAM["data_1032"]))
        setattr(cls, "edam:data_1033",
            PermissibleValue(
                text="edam:data_1033",
                title="Ensembl gene ID",
                description="Unique identifier for a gene (or other feature) from the Ensembl database.",
                meaning=EDAM["data_1033"]))
        setattr(cls, "edam:data_1034",
            PermissibleValue(
                text="edam:data_1034",
                title="Gene ID (SGD)",
                description="Identifier of an entry from the SGD database.",
                meaning=EDAM["data_1034"]))
        setattr(cls, "edam:data_1035",
            PermissibleValue(
                text="edam:data_1035",
                title="Gene ID (GeneDB)",
                description="Identifier of a gene from the GeneDB database.",
                meaning=EDAM["data_1035"]))
        setattr(cls, "edam:data_1036",
            PermissibleValue(
                text="edam:data_1036",
                title="TIGR identifier",
                description="Identifier of an entry from the TIGR database.",
                meaning=EDAM["data_1036"]))
        setattr(cls, "edam:data_1037",
            PermissibleValue(
                text="edam:data_1037",
                title="TAIR accession (gene)",
                description="Identifier of an gene from the TAIR database.",
                meaning=EDAM["data_1037"]))
        setattr(cls, "edam:data_1038",
            PermissibleValue(
                text="edam:data_1038",
                title="Protein domain ID",
                description="""Identifier of a protein structural domain.
This is typically a character or string concatenated with a PDB identifier and a chain identifier.""",
                meaning=EDAM["data_1038"]))
        setattr(cls, "edam:data_1039",
            PermissibleValue(
                text="edam:data_1039",
                title="SCOP domain identifier",
                description="Identifier of a protein domain (or other node) from the SCOP database.",
                meaning=EDAM["data_1039"]))
        setattr(cls, "edam:data_1040",
            PermissibleValue(
                text="edam:data_1040",
                title="CATH domain ID",
                description="Identifier of a protein domain from CATH.",
                meaning=EDAM["data_1040"]))
        setattr(cls, "edam:data_1041",
            PermissibleValue(
                text="edam:data_1041",
                title="SCOP concise classification string (sccs)",
                description="""A SCOP concise classification string (sccs) is a compact representation of a SCOP domain classification.
An scss includes the class (alphabetical), fold, superfamily and family (all numerical) to which a given domain belongs.""",
                meaning=EDAM["data_1041"]))
        setattr(cls, "edam:data_1042",
            PermissibleValue(
                text="edam:data_1042",
                title="SCOP sunid",
                description="""A sunid uniquely identifies an entry in the SCOP hierarchy, including leaves (the SCOP domains) and higher level nodes including entries corresponding to the protein level.
Unique identifier (number) of an entry in the SCOP hierarchy, for example 33229.""",
                meaning=EDAM["data_1042"]))
        setattr(cls, "edam:data_1043",
            PermissibleValue(
                text="edam:data_1043",
                title="CATH node ID",
                description="A code number identifying a node from the CATH database.",
                meaning=EDAM["data_1043"]))
        setattr(cls, "edam:data_1044",
            PermissibleValue(
                text="edam:data_1044",
                title="Kingdom name",
                description="The name of a biological kingdom (Bacteria, Archaea, or Eukaryotes).",
                meaning=EDAM["data_1044"]))
        setattr(cls, "edam:data_1045",
            PermissibleValue(
                text="edam:data_1045",
                title="Species name",
                description="The name of a species (typically a taxonomic group) of organism.",
                meaning=EDAM["data_1045"]))
        setattr(cls, "edam:data_1046",
            PermissibleValue(
                text="edam:data_1046",
                title="Strain name",
                description="The name of a strain of an organism variant, typically a plant, virus or bacterium.",
                meaning=EDAM["data_1046"]))
        setattr(cls, "edam:data_1047",
            PermissibleValue(
                text="edam:data_1047",
                title="URI",
                description="A string of characters that name or otherwise identify a resource on the Internet.",
                meaning=EDAM["data_1047"]))
        setattr(cls, "edam:data_1048",
            PermissibleValue(
                text="edam:data_1048",
                title="Database ID",
                description="An identifier of a biological or bioinformatics database.",
                meaning=EDAM["data_1048"]))
        setattr(cls, "edam:data_1049",
            PermissibleValue(
                text="edam:data_1049",
                title="Directory name",
                description="The name of a directory.",
                meaning=EDAM["data_1049"]))
        setattr(cls, "edam:data_1050",
            PermissibleValue(
                text="edam:data_1050",
                title="File name",
                description="The name (or part of a name) of a file (of any type).",
                meaning=EDAM["data_1050"]))
        setattr(cls, "edam:data_1051",
            PermissibleValue(
                text="edam:data_1051",
                title="Ontology name",
                description="Name of an ontology of biological or bioinformatics concepts and relations.",
                meaning=EDAM["data_1051"]))
        setattr(cls, "edam:data_1052",
            PermissibleValue(
                text="edam:data_1052",
                title="URL",
                description="A Uniform Resource Locator (URL).",
                meaning=EDAM["data_1052"]))
        setattr(cls, "edam:data_1053",
            PermissibleValue(
                text="edam:data_1053",
                title="URN",
                description="A Uniform Resource Name (URN).",
                meaning=EDAM["data_1053"]))
        setattr(cls, "edam:data_1055",
            PermissibleValue(
                text="edam:data_1055",
                title="LSID",
                description="""A Life Science Identifier (LSID) - a unique identifier of some data.
LSIDs provide a standard way to locate and describe data. An LSID is represented as a Uniform Resource Name (URN) with the following format: URN:LSID:<Authority>:<Namespace>:<ObjectID>[:<Version>]""",
                meaning=EDAM["data_1055"]))
        setattr(cls, "edam:data_1056",
            PermissibleValue(
                text="edam:data_1056",
                title="Database name",
                description="The name of a biological or bioinformatics database.",
                meaning=EDAM["data_1056"]))
        setattr(cls, "edam:data_1058",
            PermissibleValue(
                text="edam:data_1058",
                title="Enumerated file name",
                description="The name of a file (of any type) with restricted possible values.",
                meaning=EDAM["data_1058"]))
        setattr(cls, "edam:data_1059",
            PermissibleValue(
                text="edam:data_1059",
                title="File name extension",
                description="""A file extension is the characters appearing after the final '.' in the file name.
The extension of a file name.""",
                meaning=EDAM["data_1059"]))
        setattr(cls, "edam:data_1060",
            PermissibleValue(
                text="edam:data_1060",
                title="File base name",
                description="""A file base name is the file name stripped of its directory specification and extension.
The base name of a file.""",
                meaning=EDAM["data_1060"]))
        setattr(cls, "edam:data_1061",
            PermissibleValue(
                text="edam:data_1061",
                title="QSAR descriptor name",
                description="Name of a QSAR descriptor.",
                meaning=EDAM["data_1061"]))
        setattr(cls, "edam:data_1063",
            PermissibleValue(
                text="edam:data_1063",
                title="Sequence identifier",
                description="An identifier of molecular sequence(s) or entries from a molecular sequence database.",
                meaning=EDAM["data_1063"]))
        setattr(cls, "edam:data_1064",
            PermissibleValue(
                text="edam:data_1064",
                title="Sequence set ID",
                description="An identifier of a set of molecular sequence(s).",
                meaning=EDAM["data_1064"]))
        setattr(cls, "edam:data_1066",
            PermissibleValue(
                text="edam:data_1066",
                title="Sequence alignment ID",
                description="""Identifier of a molecular sequence alignment, for example a record from an alignment database.""",
                meaning=EDAM["data_1066"]))
        setattr(cls, "edam:data_1068",
            PermissibleValue(
                text="edam:data_1068",
                title="Phylogenetic tree ID",
                description="Identifier of a phylogenetic tree for example from a phylogenetic tree database.",
                meaning=EDAM["data_1068"]))
        setattr(cls, "edam:data_1069",
            PermissibleValue(
                text="edam:data_1069",
                title="Comparison matrix identifier",
                description="An identifier of a comparison matrix.",
                meaning=EDAM["data_1069"]))
        setattr(cls, "edam:data_1070",
            PermissibleValue(
                text="edam:data_1070",
                title="Structure ID",
                description="""A unique and persistent identifier of a molecular tertiary structure, typically an entry from a structure database.""",
                meaning=EDAM["data_1070"]))
        setattr(cls, "edam:data_1071",
            PermissibleValue(
                text="edam:data_1071",
                title="Structural (3D) profile ID",
                description="""Identifier or name of a structural (3D) profile or template (representing a structure or structure alignment).""",
                meaning=EDAM["data_1071"]))
        setattr(cls, "edam:data_1072",
            PermissibleValue(
                text="edam:data_1072",
                title="Structure alignment ID",
                description="Identifier of an entry from a database of tertiary structure alignments.",
                meaning=EDAM["data_1072"]))
        setattr(cls, "edam:data_1073",
            PermissibleValue(
                text="edam:data_1073",
                title="Amino acid index ID",
                description="Identifier of an index of amino acid physicochemical and biochemical property data.",
                meaning=EDAM["data_1073"]))
        setattr(cls, "edam:data_1074",
            PermissibleValue(
                text="edam:data_1074",
                title="Protein interaction ID",
                description="""Identifier of a report of protein interactions from a protein interaction database (typically).""",
                meaning=EDAM["data_1074"]))
        setattr(cls, "edam:data_1075",
            PermissibleValue(
                text="edam:data_1075",
                title="Protein family identifier",
                description="Identifier of a protein family.",
                meaning=EDAM["data_1075"]))
        setattr(cls, "edam:data_1076",
            PermissibleValue(
                text="edam:data_1076",
                title="Codon usage table name",
                description="Unique name of a codon usage table.",
                meaning=EDAM["data_1076"]))
        setattr(cls, "edam:data_1077",
            PermissibleValue(
                text="edam:data_1077",
                title="Transcription factor identifier",
                description="Identifier of a transcription factor (or a TF binding site).",
                meaning=EDAM["data_1077"]))
        setattr(cls, "edam:data_1078",
            PermissibleValue(
                text="edam:data_1078",
                title="Experiment annotation ID",
                description="Identifier of an entry from a database of microarray data.",
                meaning=EDAM["data_1078"]))
        setattr(cls, "edam:data_1079",
            PermissibleValue(
                text="edam:data_1079",
                title="Electron microscopy model ID",
                description="Identifier of an entry from a database of electron microscopy data.",
                meaning=EDAM["data_1079"]))
        setattr(cls, "edam:data_1080",
            PermissibleValue(
                text="edam:data_1080",
                title="Gene expression report ID",
                description="""Accession of a report of gene expression (e.g. a gene expression profile) from a database.""",
                meaning=EDAM["data_1080"]))
        setattr(cls, "edam:data_1081",
            PermissibleValue(
                text="edam:data_1081",
                title="Genotype and phenotype annotation ID",
                description="Identifier of an entry from a database of genotypes and phenotypes.",
                meaning=EDAM["data_1081"]))
        setattr(cls, "edam:data_1082",
            PermissibleValue(
                text="edam:data_1082",
                title="Pathway or network identifier",
                description="Identifier of an entry from a database of biological pathways or networks.",
                meaning=EDAM["data_1082"]))
        setattr(cls, "edam:data_1083",
            PermissibleValue(
                text="edam:data_1083",
                title="Workflow ID",
                description="""Identifier of a biological or biomedical workflow, typically from a database of workflows.""",
                meaning=EDAM["data_1083"]))
        setattr(cls, "edam:data_1084",
            PermissibleValue(
                text="edam:data_1084",
                title="Data resource definition ID",
                description="Identifier of a data type definition from some provider.",
                meaning=EDAM["data_1084"]))
        setattr(cls, "edam:data_1085",
            PermissibleValue(
                text="edam:data_1085",
                title="Biological model ID",
                description="Identifier of a mathematical model, typically an entry from a database.",
                meaning=EDAM["data_1085"]))
        setattr(cls, "edam:data_1086",
            PermissibleValue(
                text="edam:data_1086",
                title="Compound identifier",
                description="Identifier of an entry from a database of chemicals.",
                meaning=EDAM["data_1086"]))
        setattr(cls, "edam:data_1087",
            PermissibleValue(
                text="edam:data_1087",
                title="Ontology concept ID",
                description="""A unique (typically numerical) identifier of a concept in an ontology of biological or bioinformatics concepts and relations.""",
                meaning=EDAM["data_1087"]))
        setattr(cls, "edam:data_1088",
            PermissibleValue(
                text="edam:data_1088",
                title="Article ID",
                description="Unique identifier of a scientific article.",
                meaning=EDAM["data_1088"]))
        setattr(cls, "edam:data_1089",
            PermissibleValue(
                text="edam:data_1089",
                title="FlyBase ID",
                description="Identifier of an object from the FlyBase database.",
                meaning=EDAM["data_1089"]))
        setattr(cls, "edam:data_1091",
            PermissibleValue(
                text="edam:data_1091",
                title="WormBase name",
                description="Name of an object from the WormBase database, usually a human-readable name.",
                meaning=EDAM["data_1091"]))
        setattr(cls, "edam:data_1092",
            PermissibleValue(
                text="edam:data_1092",
                title="WormBase class",
                description="""A WormBase class describes the type of object such as 'sequence' or 'protein'.
Class of an object from the WormBase database.""",
                meaning=EDAM["data_1092"]))
        setattr(cls, "edam:data_1093",
            PermissibleValue(
                text="edam:data_1093",
                title="Sequence accession",
                description="A persistent, unique identifier of a molecular sequence database entry.",
                meaning=EDAM["data_1093"]))
        setattr(cls, "edam:data_1095",
            PermissibleValue(
                text="edam:data_1095",
                title="EMBOSS Uniform Sequence Address",
                description="""The name of a sequence-based entity adhering to the standard sequence naming scheme used by all EMBOSS applications.""",
                meaning=EDAM["data_1095"]))
        setattr(cls, "edam:data_1096",
            PermissibleValue(
                text="edam:data_1096",
                title="Sequence accession (protein)",
                description="Accession number of a protein sequence database entry.",
                meaning=EDAM["data_1096"]))
        setattr(cls, "edam:data_1097",
            PermissibleValue(
                text="edam:data_1097",
                title="Sequence accession (nucleic acid)",
                description="Accession number of a nucleotide sequence database entry.",
                meaning=EDAM["data_1097"]))
        setattr(cls, "edam:data_1098",
            PermissibleValue(
                text="edam:data_1098",
                title="RefSeq accession",
                description="Accession number of a RefSeq database entry.",
                meaning=EDAM["data_1098"]))
        setattr(cls, "edam:data_1100",
            PermissibleValue(
                text="edam:data_1100",
                title="PIR identifier",
                description="An identifier of PIR sequence database entry.",
                meaning=EDAM["data_1100"]))
        setattr(cls, "edam:data_1102",
            PermissibleValue(
                text="edam:data_1102",
                title="Gramene primary identifier",
                description="Primary identifier of a Gramene database entry.",
                meaning=EDAM["data_1102"]))
        setattr(cls, "edam:data_1103",
            PermissibleValue(
                text="edam:data_1103",
                title="EMBL/GenBank/DDBJ ID",
                description="Identifier of a (nucleic acid) entry from the EMBL/GenBank/DDBJ databases.",
                meaning=EDAM["data_1103"]))
        setattr(cls, "edam:data_1104",
            PermissibleValue(
                text="edam:data_1104",
                title="Sequence cluster ID (UniGene)",
                description="A unique identifier of an entry (gene cluster) from the NCBI UniGene database.",
                meaning=EDAM["data_1104"]))
        setattr(cls, "edam:data_1105",
            PermissibleValue(
                text="edam:data_1105",
                title="dbEST accession",
                description="Identifier of a dbEST database entry.",
                meaning=EDAM["data_1105"]))
        setattr(cls, "edam:data_1106",
            PermissibleValue(
                text="edam:data_1106",
                title="dbSNP ID",
                description="Identifier of a dbSNP database entry.",
                meaning=EDAM["data_1106"]))
        setattr(cls, "edam:data_1112",
            PermissibleValue(
                text="edam:data_1112",
                title="Sequence cluster ID",
                description="An identifier of a cluster of molecular sequence(s).",
                meaning=EDAM["data_1112"]))
        setattr(cls, "edam:data_1113",
            PermissibleValue(
                text="edam:data_1113",
                title="Sequence cluster ID (COG)",
                description="Unique identifier of an entry from the COG database.",
                meaning=EDAM["data_1113"]))
        setattr(cls, "edam:data_1114",
            PermissibleValue(
                text="edam:data_1114",
                title="Sequence motif identifier",
                description="Identifier of a sequence motif, for example an entry from a motif database.",
                meaning=EDAM["data_1114"]))
        setattr(cls, "edam:data_1115",
            PermissibleValue(
                text="edam:data_1115",
                title="Sequence profile ID",
                description="""A sequence profile typically represents a sequence alignment.
Identifier of a sequence profile.""",
                meaning=EDAM["data_1115"]))
        setattr(cls, "edam:data_1116",
            PermissibleValue(
                text="edam:data_1116",
                title="ELM ID",
                description="Identifier of an entry from the ELMdb database of protein functional sites.",
                meaning=EDAM["data_1116"]))
        setattr(cls, "edam:data_1117",
            PermissibleValue(
                text="edam:data_1117",
                title="Prosite accession number",
                description="Accession number of an entry from the Prosite database.",
                meaning=EDAM["data_1117"]))
        setattr(cls, "edam:data_1118",
            PermissibleValue(
                text="edam:data_1118",
                title="HMMER hidden Markov model ID",
                description="Unique identifier or name of a HMMER hidden Markov model.",
                meaning=EDAM["data_1118"]))
        setattr(cls, "edam:data_1119",
            PermissibleValue(
                text="edam:data_1119",
                title="JASPAR profile ID",
                description="Unique identifier or name of a profile from the JASPAR database.",
                meaning=EDAM["data_1119"]))
        setattr(cls, "edam:data_1123",
            PermissibleValue(
                text="edam:data_1123",
                title="TreeBASE study accession number",
                description="Accession number of an entry from the TreeBASE database.",
                meaning=EDAM["data_1123"]))
        setattr(cls, "edam:data_1124",
            PermissibleValue(
                text="edam:data_1124",
                title="TreeFam accession number",
                description="Accession number of an entry from the TreeFam database.",
                meaning=EDAM["data_1124"]))
        setattr(cls, "edam:data_1126",
            PermissibleValue(
                text="edam:data_1126",
                title="Comparison matrix name",
                description="""See for example http://www.ebi.ac.uk/Tools/webservices/help/matrix.
Unique name or identifier of a comparison matrix.""",
                meaning=EDAM["data_1126"]))
        setattr(cls, "edam:data_1127",
            PermissibleValue(
                text="edam:data_1127",
                title="PDB ID",
                description="""A PDB identification code which consists of 4 characters, the first of which is a digit in the range 0 - 9; the remaining 3 are alphanumeric, and letters are upper case only. (source: https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1996.pdf)
An identifier of an entry from the PDB database.""",
                meaning=EDAM["data_1127"]))
        setattr(cls, "edam:data_1128",
            PermissibleValue(
                text="edam:data_1128",
                title="AAindex ID",
                description="Identifier of an entry from the AAindex database.",
                meaning=EDAM["data_1128"]))
        setattr(cls, "edam:data_1129",
            PermissibleValue(
                text="edam:data_1129",
                title="BIND accession number",
                description="Accession number of an entry from the BIND database.",
                meaning=EDAM["data_1129"]))
        setattr(cls, "edam:data_1130",
            PermissibleValue(
                text="edam:data_1130",
                title="IntAct accession number",
                description="Accession number of an entry from the IntAct database.",
                meaning=EDAM["data_1130"]))
        setattr(cls, "edam:data_1131",
            PermissibleValue(
                text="edam:data_1131",
                title="Protein family name",
                description="Name of a protein family.",
                meaning=EDAM["data_1131"]))
        setattr(cls, "edam:data_1132",
            PermissibleValue(
                text="edam:data_1132",
                title="InterPro entry name",
                description="""Name of an InterPro entry, usually indicating the type of protein matches for that entry.""",
                meaning=EDAM["data_1132"]))
        setattr(cls, "edam:data_1133",
            PermissibleValue(
                text="edam:data_1133",
                title="InterPro accession",
                description="""Every InterPro entry has a unique accession number to provide a persistent citation of database records.
Primary accession number of an InterPro entry.""",
                meaning=EDAM["data_1133"]))
        setattr(cls, "edam:data_1134",
            PermissibleValue(
                text="edam:data_1134",
                title="InterPro secondary accession",
                description="Secondary accession number of an InterPro entry.",
                meaning=EDAM["data_1134"]))
        setattr(cls, "edam:data_1135",
            PermissibleValue(
                text="edam:data_1135",
                title="Gene3D ID",
                description="Unique identifier of an entry from the Gene3D database.",
                meaning=EDAM["data_1135"]))
        setattr(cls, "edam:data_1136",
            PermissibleValue(
                text="edam:data_1136",
                title="PIRSF ID",
                description="Unique identifier of an entry from the PIRSF database.",
                meaning=EDAM["data_1136"]))
        setattr(cls, "edam:data_1137",
            PermissibleValue(
                text="edam:data_1137",
                title="PRINTS code",
                description="The unique identifier of an entry in the PRINTS database.",
                meaning=EDAM["data_1137"]))
        setattr(cls, "edam:data_1138",
            PermissibleValue(
                text="edam:data_1138",
                title="Pfam accession number",
                description="Accession number of a Pfam entry.",
                meaning=EDAM["data_1138"]))
        setattr(cls, "edam:data_1139",
            PermissibleValue(
                text="edam:data_1139",
                title="SMART accession number",
                description="Accession number of an entry from the SMART database.",
                meaning=EDAM["data_1139"]))
        setattr(cls, "edam:data_1140",
            PermissibleValue(
                text="edam:data_1140",
                title="Superfamily hidden Markov model number",
                description="Unique identifier (number) of a hidden Markov model from the Superfamily database.",
                meaning=EDAM["data_1140"]))
        setattr(cls, "edam:data_1141",
            PermissibleValue(
                text="edam:data_1141",
                title="TIGRFam ID",
                description="Accession number of an entry (family) from the TIGRFam database.",
                meaning=EDAM["data_1141"]))
        setattr(cls, "edam:data_1142",
            PermissibleValue(
                text="edam:data_1142",
                title="ProDom accession number",
                description="""A ProDom domain family accession number.
ProDom is a protein domain family database.""",
                meaning=EDAM["data_1142"]))
        setattr(cls, "edam:data_1143",
            PermissibleValue(
                text="edam:data_1143",
                title="TRANSFAC accession number",
                description="Identifier of an entry from the TRANSFAC database.",
                meaning=EDAM["data_1143"]))
        setattr(cls, "edam:data_1144",
            PermissibleValue(
                text="edam:data_1144",
                title="ArrayExpress accession number",
                description="Accession number of an entry from the ArrayExpress database.",
                meaning=EDAM["data_1144"]))
        setattr(cls, "edam:data_1145",
            PermissibleValue(
                text="edam:data_1145",
                title="PRIDE experiment accession number",
                description="PRIDE experiment accession number.",
                meaning=EDAM["data_1145"]))
        setattr(cls, "edam:data_1146",
            PermissibleValue(
                text="edam:data_1146",
                title="EMDB ID",
                description="Identifier of an entry from the EMDB electron microscopy database.",
                meaning=EDAM["data_1146"]))
        setattr(cls, "edam:data_1147",
            PermissibleValue(
                text="edam:data_1147",
                title="GEO accession number",
                description="Accession number of an entry from the GEO database.",
                meaning=EDAM["data_1147"]))
        setattr(cls, "edam:data_1148",
            PermissibleValue(
                text="edam:data_1148",
                title="GermOnline ID",
                description="Identifier of an entry from the GermOnline database.",
                meaning=EDAM["data_1148"]))
        setattr(cls, "edam:data_1149",
            PermissibleValue(
                text="edam:data_1149",
                title="EMAGE ID",
                description="Identifier of an entry from the EMAGE database.",
                meaning=EDAM["data_1149"]))
        setattr(cls, "edam:data_1150",
            PermissibleValue(
                text="edam:data_1150",
                title="Disease ID",
                description="Accession number of an entry from a database of disease.",
                meaning=EDAM["data_1150"]))
        setattr(cls, "edam:data_1151",
            PermissibleValue(
                text="edam:data_1151",
                title="HGVbase ID",
                description="Identifier of an entry from the HGVbase database.",
                meaning=EDAM["data_1151"]))
        setattr(cls, "edam:data_1153",
            PermissibleValue(
                text="edam:data_1153",
                title="OMIM ID",
                description="Identifier of an entry from the OMIM database.",
                meaning=EDAM["data_1153"]))
        setattr(cls, "edam:data_1154",
            PermissibleValue(
                text="edam:data_1154",
                title="KEGG object identifier",
                description="""Unique identifier of an object from one of the KEGG databases (excluding the GENES division).""",
                meaning=EDAM["data_1154"]))
        setattr(cls, "edam:data_1155",
            PermissibleValue(
                text="edam:data_1155",
                title="Pathway ID (reactome)",
                description="Identifier of an entry from the Reactome database.",
                meaning=EDAM["data_1155"]))
        setattr(cls, "edam:data_1157",
            PermissibleValue(
                text="edam:data_1157",
                title="Pathway ID (BioCyc)",
                description="Identifier of an pathway from the BioCyc biological pathways database.",
                meaning=EDAM["data_1157"]))
        setattr(cls, "edam:data_1158",
            PermissibleValue(
                text="edam:data_1158",
                title="Pathway ID (INOH)",
                description="Identifier of an entry from the INOH database.",
                meaning=EDAM["data_1158"]))
        setattr(cls, "edam:data_1159",
            PermissibleValue(
                text="edam:data_1159",
                title="Pathway ID (PATIKA)",
                description="Identifier of an entry from the PATIKA database.",
                meaning=EDAM["data_1159"]))
        setattr(cls, "edam:data_1160",
            PermissibleValue(
                text="edam:data_1160",
                title="Pathway ID (CPDB)",
                description="""Identifier of an entry from the CPDB (ConsensusPathDB) biological pathways database, which is an identifier from an external database integrated into CPDB.
This concept refers to identifiers used by the databases collated in CPDB; CPDB identifiers are not independently defined.""",
                meaning=EDAM["data_1160"]))
        setattr(cls, "edam:data_1161",
            PermissibleValue(
                text="edam:data_1161",
                title="Pathway ID (Panther)",
                description="Identifier of a biological pathway from the Panther Pathways database.",
                meaning=EDAM["data_1161"]))
        setattr(cls, "edam:data_1162",
            PermissibleValue(
                text="edam:data_1162",
                title="MIRIAM identifier",
                description="""This is the identifier used internally by MIRIAM for a data type.
Unique identifier of a MIRIAM data resource.""",
                meaning=EDAM["data_1162"]))
        setattr(cls, "edam:data_1163",
            PermissibleValue(
                text="edam:data_1163",
                title="MIRIAM data type name",
                description="The name of a data type from the MIRIAM database.",
                meaning=EDAM["data_1163"]))
        setattr(cls, "edam:data_1164",
            PermissibleValue(
                text="edam:data_1164",
                title="MIRIAM URI",
                description="""A MIRIAM URI consists of the URI of the MIRIAM data type (PubMed, UniProt etc) followed by the identifier of an element of that data type, for example PMID for a publication or an accession number for a GO term.
The URI (URL or URN) of a data entity from the MIRIAM database.""",
                meaning=EDAM["data_1164"]))
        setattr(cls, "edam:data_1165",
            PermissibleValue(
                text="edam:data_1165",
                title="MIRIAM data type primary name",
                description="""The primary name of a MIRIAM data type is taken from a controlled vocabulary.
The primary name of a data type from the MIRIAM database.""",
                meaning=EDAM["data_1165"]))
        setattr(cls, "edam:data_1166",
            PermissibleValue(
                text="edam:data_1166",
                title="MIRIAM data type synonymous name",
                description="""A synonymous name for a MIRIAM data type taken from a controlled vocabulary.
A synonymous name of a data type from the MIRIAM database.""",
                meaning=EDAM["data_1166"]))
        setattr(cls, "edam:data_1167",
            PermissibleValue(
                text="edam:data_1167",
                title="Taverna workflow ID",
                description="Unique identifier of a Taverna workflow.",
                meaning=EDAM["data_1167"]))
        setattr(cls, "edam:data_1170",
            PermissibleValue(
                text="edam:data_1170",
                title="Biological model name",
                description="Name of a biological (mathematical) model.",
                meaning=EDAM["data_1170"]))
        setattr(cls, "edam:data_1171",
            PermissibleValue(
                text="edam:data_1171",
                title="BioModel ID",
                description="Unique identifier of an entry from the BioModel database.",
                meaning=EDAM["data_1171"]))
        setattr(cls, "edam:data_1172",
            PermissibleValue(
                text="edam:data_1172",
                title="PubChem CID",
                description="""Chemical structure specified in PubChem Compound Identification (CID), a non-zero integer identifier for a unique chemical structure.""",
                meaning=EDAM["data_1172"]))
        setattr(cls, "edam:data_1173",
            PermissibleValue(
                text="edam:data_1173",
                title="ChemSpider ID",
                description="Identifier of an entry from the ChemSpider database.",
                meaning=EDAM["data_1173"]))
        setattr(cls, "edam:data_1174",
            PermissibleValue(
                text="edam:data_1174",
                title="ChEBI ID",
                description="Identifier of an entry from the ChEBI database.",
                meaning=EDAM["data_1174"]))
        setattr(cls, "edam:data_1175",
            PermissibleValue(
                text="edam:data_1175",
                title="BioPax concept ID",
                description="An identifier of a concept from the BioPax ontology.",
                meaning=EDAM["data_1175"]))
        setattr(cls, "edam:data_1176",
            PermissibleValue(
                text="edam:data_1176",
                title="GO concept ID",
                description="An identifier of a concept from The Gene Ontology.",
                meaning=EDAM["data_1176"]))
        setattr(cls, "edam:data_1177",
            PermissibleValue(
                text="edam:data_1177",
                title="MeSH concept ID",
                description="An identifier of a concept from the MeSH vocabulary.",
                meaning=EDAM["data_1177"]))
        setattr(cls, "edam:data_1178",
            PermissibleValue(
                text="edam:data_1178",
                title="HGNC concept ID",
                description="An identifier of a concept from the HGNC controlled vocabulary.",
                meaning=EDAM["data_1178"]))
        setattr(cls, "edam:data_1179",
            PermissibleValue(
                text="edam:data_1179",
                title="NCBI taxonomy ID",
                description="""A stable unique identifier for each taxon (for a species, a family, an order, or any other group in the NCBI taxonomy database.""",
                meaning=EDAM["data_1179"]))
        setattr(cls, "edam:data_1180",
            PermissibleValue(
                text="edam:data_1180",
                title="Plant Ontology concept ID",
                description="An identifier of a concept from the Plant Ontology (PO).",
                meaning=EDAM["data_1180"]))
        setattr(cls, "edam:data_1181",
            PermissibleValue(
                text="edam:data_1181",
                title="UMLS concept ID",
                description="An identifier of a concept from the UMLS vocabulary.",
                meaning=EDAM["data_1181"]))
        setattr(cls, "edam:data_1182",
            PermissibleValue(
                text="edam:data_1182",
                title="FMA concept ID",
                description="""An identifier of a concept from Foundational Model of Anatomy.
Classifies anatomical entities according to their shared characteristics (genus) and distinguishing characteristics (differentia). Specifies the part-whole and spatial relationships of the entities, morphological transformation of the entities during prenatal development and the postnatal life cycle and principles, rules and definitions according to which classes and relationships in the other three components of FMA are represented.""",
                meaning=EDAM["data_1182"]))
        setattr(cls, "edam:data_1183",
            PermissibleValue(
                text="edam:data_1183",
                title="EMAP concept ID",
                description="An identifier of a concept from the EMAP mouse ontology.",
                meaning=EDAM["data_1183"]))
        setattr(cls, "edam:data_1184",
            PermissibleValue(
                text="edam:data_1184",
                title="ChEBI concept ID",
                description="An identifier of a concept from the ChEBI ontology.",
                meaning=EDAM["data_1184"]))
        setattr(cls, "edam:data_1185",
            PermissibleValue(
                text="edam:data_1185",
                title="MGED concept ID",
                description="An identifier of a concept from the MGED ontology.",
                meaning=EDAM["data_1185"]))
        setattr(cls, "edam:data_1186",
            PermissibleValue(
                text="edam:data_1186",
                title="myGrid concept ID",
                description="""An identifier of a concept from the myGrid ontology.
The ontology is provided as two components, the service ontology and the domain ontology. The domain ontology acts provides concepts for core bioinformatics data types and their relations. The service ontology describes the physical and operational features of web services.""",
                meaning=EDAM["data_1186"]))
        setattr(cls, "edam:data_1187",
            PermissibleValue(
                text="edam:data_1187",
                title="PubMed ID",
                description="PubMed unique identifier of an article.",
                meaning=EDAM["data_1187"]))
        setattr(cls, "edam:data_1188",
            PermissibleValue(
                text="edam:data_1188",
                title="DOI",
                description="Digital Object Identifier (DOI) of a published article.",
                meaning=EDAM["data_1188"]))
        setattr(cls, "edam:data_1189",
            PermissibleValue(
                text="edam:data_1189",
                title="Medline UI",
                description="""Medline UI (unique identifier) of an article.
The use of Medline UI has been replaced by the PubMed unique identifier.""",
                meaning=EDAM["data_1189"]))
        setattr(cls, "edam:data_1190",
            PermissibleValue(
                text="edam:data_1190",
                title="Tool name",
                description="The name of a computer package, application, method or function.",
                meaning=EDAM["data_1190"]))
        setattr(cls, "edam:data_1191",
            PermissibleValue(
                text="edam:data_1191",
                title="Tool name (signature)",
                description="""Signature methods from http://www.ebi.ac.uk/Tools/InterProScan/help.html#results include BlastProDom, FPrintScan, HMMPIR, HMMPfam, HMMSmart, HMMTigr, ProfileScan, ScanRegExp, SuperFamily and HAMAP.
The unique name of a signature (sequence classifier) method.""",
                meaning=EDAM["data_1191"]))
        setattr(cls, "edam:data_1192",
            PermissibleValue(
                text="edam:data_1192",
                title="Tool name (BLAST)",
                description="""The name of a BLAST tool.
This include 'blastn', 'blastp', 'blastx', 'tblastn' and 'tblastx'.""",
                meaning=EDAM["data_1192"]))
        setattr(cls, "edam:data_1193",
            PermissibleValue(
                text="edam:data_1193",
                title="Tool name (FASTA)",
                description="""The name of a FASTA tool.
This includes 'fasta3', 'fastx3', 'fasty3', 'fastf3', 'fasts3' and 'ssearch'.""",
                meaning=EDAM["data_1193"]))
        setattr(cls, "edam:data_1194",
            PermissibleValue(
                text="edam:data_1194",
                title="Tool name (EMBOSS)",
                description="The name of an EMBOSS application.",
                meaning=EDAM["data_1194"]))
        setattr(cls, "edam:data_1195",
            PermissibleValue(
                text="edam:data_1195",
                title="Tool name (EMBASSY package)",
                description="The name of an EMBASSY package.",
                meaning=EDAM["data_1195"]))
        setattr(cls, "edam:data_1201",
            PermissibleValue(
                text="edam:data_1201",
                title="QSAR descriptor (constitutional)",
                description="A QSAR constitutional descriptor.",
                meaning=EDAM["data_1201"]))
        setattr(cls, "edam:data_1202",
            PermissibleValue(
                text="edam:data_1202",
                title="QSAR descriptor (electronic)",
                description="A QSAR electronic descriptor.",
                meaning=EDAM["data_1202"]))
        setattr(cls, "edam:data_1203",
            PermissibleValue(
                text="edam:data_1203",
                title="QSAR descriptor (geometrical)",
                description="A QSAR geometrical descriptor.",
                meaning=EDAM["data_1203"]))
        setattr(cls, "edam:data_1204",
            PermissibleValue(
                text="edam:data_1204",
                title="QSAR descriptor (topological)",
                description="A QSAR topological descriptor.",
                meaning=EDAM["data_1204"]))
        setattr(cls, "edam:data_1205",
            PermissibleValue(
                text="edam:data_1205",
                title="QSAR descriptor (molecular)",
                description="A QSAR molecular descriptor.",
                meaning=EDAM["data_1205"]))
        setattr(cls, "edam:data_1233",
            PermissibleValue(
                text="edam:data_1233",
                title="Sequence set (protein)",
                description="""Any collection of multiple protein sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.""",
                meaning=EDAM["data_1233"]))
        setattr(cls, "edam:data_1234",
            PermissibleValue(
                text="edam:data_1234",
                title="Sequence set (nucleic acid)",
                description="""Any collection of multiple nucleotide sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.""",
                meaning=EDAM["data_1234"]))
        setattr(cls, "edam:data_1235",
            PermissibleValue(
                text="edam:data_1235",
                title="Sequence cluster",
                description="""A set of sequences that have been clustered or otherwise classified as belonging to a group including (typically) sequence cluster information.
The cluster might include sequences identifiers, short descriptions, alignment and summary information.""",
                meaning=EDAM["data_1235"]))
        setattr(cls, "edam:data_1238",
            PermissibleValue(
                text="edam:data_1238",
                title="Proteolytic digest",
                description="""A protein sequence cleaved into peptide fragments (by enzymatic or chemical cleavage) with fragment masses.""",
                meaning=EDAM["data_1238"]))
        setattr(cls, "edam:data_1239",
            PermissibleValue(
                text="edam:data_1239",
                title="Restriction digest",
                description="""Restriction digest fragments from digesting a nucleotide sequence with restriction sites using a restriction endonuclease.""",
                meaning=EDAM["data_1239"]))
        setattr(cls, "edam:data_1240",
            PermissibleValue(
                text="edam:data_1240",
                title="PCR primers",
                description="""Oligonucleotide primer(s) for PCR and DNA amplification, for example a minimal primer set.""",
                meaning=EDAM["data_1240"]))
        setattr(cls, "edam:data_1245",
            PermissibleValue(
                text="edam:data_1245",
                title="Sequence cluster (protein)",
                description="""A cluster of protein sequences.
The sequences are typically related, for example a family of sequences.""",
                meaning=EDAM["data_1245"]))
        setattr(cls, "edam:data_1246",
            PermissibleValue(
                text="edam:data_1246",
                title="Sequence cluster (nucleic acid)",
                description="""A cluster of nucleotide sequences.
The sequences are typically related, for example a family of sequences.""",
                meaning=EDAM["data_1246"]))
        setattr(cls, "edam:data_1249",
            PermissibleValue(
                text="edam:data_1249",
                title="Sequence length",
                description="""The size (length) of a sequence, subsequence or region in a sequence, or range(s) of lengths.""",
                meaning=EDAM["data_1249"]))
        setattr(cls, "edam:data_1254",
            PermissibleValue(
                text="edam:data_1254",
                title="Sequence property",
                description="""An informative report about non-positional sequence features, typically a report on general molecular sequence properties derived from sequence analysis.""",
                meaning=EDAM["data_1254"]))
        setattr(cls, "edam:data_1255",
            PermissibleValue(
                text="edam:data_1255",
                title="Sequence features",
                description="""Annotation of positional features of molecular sequence(s), i.e. that can be mapped to position(s) in the sequence.
This includes annotation of positional sequence features, organised into a standard feature table, or any other report of sequence features. General feature reports are a source of sequence feature table information although internal conversion would be required.""",
                meaning=EDAM["data_1255"]))
        setattr(cls, "edam:data_1259",
            PermissibleValue(
                text="edam:data_1259",
                title="Sequence complexity report",
                description="""A report on sequence complexity, for example low-complexity or repeat regions in sequences.""",
                meaning=EDAM["data_1259"]))
        setattr(cls, "edam:data_1260",
            PermissibleValue(
                text="edam:data_1260",
                title="Sequence ambiguity report",
                description="A report on ambiguity in molecular sequence(s).",
                meaning=EDAM["data_1260"]))
        setattr(cls, "edam:data_1261",
            PermissibleValue(
                text="edam:data_1261",
                title="Sequence composition report",
                description="""A report (typically a table) on character or word composition / frequency of a molecular sequence(s).""",
                meaning=EDAM["data_1261"]))
        setattr(cls, "edam:data_1262",
            PermissibleValue(
                text="edam:data_1262",
                title="Peptide molecular weight hits",
                description="""A report on peptide fragments of certain molecular weight(s) in one or more protein sequences.""",
                meaning=EDAM["data_1262"]))
        setattr(cls, "edam:data_1263",
            PermissibleValue(
                text="edam:data_1263",
                title="Base position variability plot",
                description="A plot of third base position variability in a nucleotide sequence.",
                meaning=EDAM["data_1263"]))
        setattr(cls, "edam:data_1265",
            PermissibleValue(
                text="edam:data_1265",
                title="Base frequencies table",
                description="A table of base frequencies of a nucleotide sequence.",
                meaning=EDAM["data_1265"]))
        setattr(cls, "edam:data_1266",
            PermissibleValue(
                text="edam:data_1266",
                title="Base word frequencies table",
                description="A table of word composition of a nucleotide sequence.",
                meaning=EDAM["data_1266"]))
        setattr(cls, "edam:data_1267",
            PermissibleValue(
                text="edam:data_1267",
                title="Amino acid frequencies table",
                description="A table of amino acid frequencies of a protein sequence.",
                meaning=EDAM["data_1267"]))
        setattr(cls, "edam:data_1268",
            PermissibleValue(
                text="edam:data_1268",
                title="Amino acid word frequencies table",
                description="A table of amino acid word composition of a protein sequence.",
                meaning=EDAM["data_1268"]))
        setattr(cls, "edam:data_1270",
            PermissibleValue(
                text="edam:data_1270",
                title="Feature table",
                description="Annotation of positional sequence features, organised into a standard feature table.",
                meaning=EDAM["data_1270"]))
        setattr(cls, "edam:data_1274",
            PermissibleValue(
                text="edam:data_1274",
                title="Map",
                description="""A map of (typically one) DNA sequence annotated with positional or non-positional features.""",
                meaning=EDAM["data_1274"]))
        setattr(cls, "edam:data_1276",
            PermissibleValue(
                text="edam:data_1276",
                title="Nucleic acid features",
                description="""An informative report on intrinsic positional features of a nucleotide sequence, formatted to be machine-readable.
This includes nucleotide sequence feature annotation in any known sequence feature table format and any other report of nucleic acid features.""",
                meaning=EDAM["data_1276"]))
        setattr(cls, "edam:data_1277",
            PermissibleValue(
                text="edam:data_1277",
                title="Protein features",
                description="""An informative report on intrinsic positional features of a protein sequence.
This includes protein sequence feature annotation in any known sequence feature table format and any other report of protein features.""",
                meaning=EDAM["data_1277"]))
        setattr(cls, "edam:data_1278",
            PermissibleValue(
                text="edam:data_1278",
                title="Genetic map",
                description="""A genetic (linkage) map indicates the proximity of two genes on a chromosome, whether two genes are linked and the frequency they are transmitted together to an offspring. They are limited to genetic markers of traits observable only in whole organisms.
A map showing the relative positions of genetic markers in a nucleic acid sequence, based on estimation of non-physical distance such as recombination frequencies.""",
                meaning=EDAM["data_1278"]))
        setattr(cls, "edam:data_1279",
            PermissibleValue(
                text="edam:data_1279",
                title="Sequence map",
                description="""A map of genetic markers in a contiguous, assembled genomic sequence, with the sizes and separation of markers measured in base pairs.
A sequence map typically includes annotation on significant subsequences such as contigs, haplotypes and genes. The contigs shown will (typically) be a set of small overlapping clones representing a complete chromosomal segment.""",
                meaning=EDAM["data_1279"]))
        setattr(cls, "edam:data_1280",
            PermissibleValue(
                text="edam:data_1280",
                title="Physical map",
                description="""A map of DNA (linear or circular) annotated with physical features or landmarks such as restriction sites, cloned DNA fragments, genes or genetic markers, along with the physical distances between them.
Distance in a physical map is measured in base pairs. A physical map might be ordered relative to a reference map (typically a genetic map) in the process of genome sequencing.""",
                meaning=EDAM["data_1280"]))
        setattr(cls, "edam:data_1283",
            PermissibleValue(
                text="edam:data_1283",
                title="Cytogenetic map",
                description="""A map showing banding patterns derived from direct observation of a stained chromosome.
This is the lowest-resolution physical map and can provide only rough estimates of physical (base pair) distances. Like a genetic map, they are limited to genetic markers of traits observable only in whole organisms.""",
                meaning=EDAM["data_1283"]))
        setattr(cls, "edam:data_1284",
            PermissibleValue(
                text="edam:data_1284",
                title="DNA transduction map",
                description="""A gene map showing distances between loci based on relative cotransduction frequencies.""",
                meaning=EDAM["data_1284"]))
        setattr(cls, "edam:data_1285",
            PermissibleValue(
                text="edam:data_1285",
                title="Gene map",
                description="""Sequence map of a single gene annotated with genetic features such as introns, exons, untranslated regions, polyA signals, promoters, enhancers and (possibly) mutations defining alleles of a gene.""",
                meaning=EDAM["data_1285"]))
        setattr(cls, "edam:data_1286",
            PermissibleValue(
                text="edam:data_1286",
                title="Plasmid map",
                description="Sequence map of a plasmid (circular DNA).",
                meaning=EDAM["data_1286"]))
        setattr(cls, "edam:data_1288",
            PermissibleValue(
                text="edam:data_1288",
                title="Genome map",
                description="Sequence map of a whole genome.",
                meaning=EDAM["data_1288"]))
        setattr(cls, "edam:data_1289",
            PermissibleValue(
                text="edam:data_1289",
                title="Restriction map",
                description="""Image of the restriction enzyme cleavage sites (restriction sites) in a nucleic acid sequence.""",
                meaning=EDAM["data_1289"]))
        setattr(cls, "edam:data_1347",
            PermissibleValue(
                text="edam:data_1347",
                title="Dirichlet distribution",
                description="Dirichlet distribution used by hidden Markov model analysis programs.",
                meaning=EDAM["data_1347"]))
        setattr(cls, "edam:data_1352",
            PermissibleValue(
                text="edam:data_1352",
                title="Regular expression",
                description="Regular expression pattern.",
                meaning=EDAM["data_1352"]))
        setattr(cls, "edam:data_1353",
            PermissibleValue(
                text="edam:data_1353",
                title="Sequence motif",
                description="""Any specific or conserved pattern (typically expressed as a regular expression) in a molecular sequence.""",
                meaning=EDAM["data_1353"]))
        setattr(cls, "edam:data_1354",
            PermissibleValue(
                text="edam:data_1354",
                title="Sequence profile",
                description="Some type of statistical model representing a (typically multiple) sequence alignment.",
                meaning=EDAM["data_1354"]))
        setattr(cls, "edam:data_1355",
            PermissibleValue(
                text="edam:data_1355",
                title="Protein signature",
                description="An informative report about a specific or conserved protein sequence pattern.",
                meaning=EDAM["data_1355"]))
        setattr(cls, "edam:data_1361",
            PermissibleValue(
                text="edam:data_1361",
                title="Position frequency matrix",
                description="""A profile (typically representing a sequence alignment) that is a simple matrix of nucleotide (or amino acid) counts per position.""",
                meaning=EDAM["data_1361"]))
        setattr(cls, "edam:data_1362",
            PermissibleValue(
                text="edam:data_1362",
                title="Position weight matrix",
                description="""A profile (typically representing a sequence alignment) that is weighted matrix of nucleotide (or amino acid) counts per position.
Contributions of individual sequences to the matrix might be uneven (weighted).""",
                meaning=EDAM["data_1362"]))
        setattr(cls, "edam:data_1363",
            PermissibleValue(
                text="edam:data_1363",
                title="Information content matrix",
                description="""A profile (typically representing a sequence alignment) derived from a matrix of nucleotide (or amino acid) counts per position that reflects information content at each position.""",
                meaning=EDAM["data_1363"]))
        setattr(cls, "edam:data_1364",
            PermissibleValue(
                text="edam:data_1364",
                title="Hidden Markov model",
                description="""A statistical Markov model of a system which is assumed to be a Markov process with unobserved (hidden) states. For example, a hidden Markov model representation of a set or alignment of sequences.""",
                meaning=EDAM["data_1364"]))
        setattr(cls, "edam:data_1365",
            PermissibleValue(
                text="edam:data_1365",
                title="Fingerprint",
                description="One or more fingerprints (sequence classifiers) as used in the PRINTS database.",
                meaning=EDAM["data_1365"]))
        setattr(cls, "edam:data_1381",
            PermissibleValue(
                text="edam:data_1381",
                title="Pair sequence alignment",
                description="Alignment of exactly two molecular sequences.",
                meaning=EDAM["data_1381"]))
        setattr(cls, "edam:data_1383",
            PermissibleValue(
                text="edam:data_1383",
                title="Nucleic acid sequence alignment",
                description="Alignment of multiple nucleotide sequences.",
                meaning=EDAM["data_1383"]))
        setattr(cls, "edam:data_1384",
            PermissibleValue(
                text="edam:data_1384",
                title="Protein sequence alignment",
                description="Alignment of multiple protein sequences.",
                meaning=EDAM["data_1384"]))
        setattr(cls, "edam:data_1385",
            PermissibleValue(
                text="edam:data_1385",
                title="Hybrid sequence alignment",
                description="""Alignment of multiple molecular sequences of different types.
Hybrid sequence alignments include for example genomic DNA to EST, cDNA or mRNA.""",
                meaning=EDAM["data_1385"]))
        setattr(cls, "edam:data_1394",
            PermissibleValue(
                text="edam:data_1394",
                title="Alignment score or penalty",
                description="""A simple floating point number defining the penalty for opening or extending a gap in an alignment.""",
                meaning=EDAM["data_1394"]))
        setattr(cls, "edam:data_1397",
            PermissibleValue(
                text="edam:data_1397",
                title="Gap opening penalty",
                description="A penalty for opening a gap in an alignment.",
                meaning=EDAM["data_1397"]))
        setattr(cls, "edam:data_1398",
            PermissibleValue(
                text="edam:data_1398",
                title="Gap extension penalty",
                description="A penalty for extending a gap in an alignment.",
                meaning=EDAM["data_1398"]))
        setattr(cls, "edam:data_1399",
            PermissibleValue(
                text="edam:data_1399",
                title="Gap separation penalty",
                description="A penalty for gaps that are close together in an alignment.",
                meaning=EDAM["data_1399"]))
        setattr(cls, "edam:data_1401",
            PermissibleValue(
                text="edam:data_1401",
                title="Match reward score",
                description="""The score for a 'match' used in various sequence database search applications with simple scoring schemes.""",
                meaning=EDAM["data_1401"]))
        setattr(cls, "edam:data_1402",
            PermissibleValue(
                text="edam:data_1402",
                title="Mismatch penalty score",
                description="""The score (penalty) for a 'mismatch' used in various alignment and sequence database search applications with simple scoring schemes.""",
                meaning=EDAM["data_1402"]))
        setattr(cls, "edam:data_1403",
            PermissibleValue(
                text="edam:data_1403",
                title="Drop off score",
                description="This is the threshold drop in score at which extension of word alignment is halted.",
                meaning=EDAM["data_1403"]))
        setattr(cls, "edam:data_1410",
            PermissibleValue(
                text="edam:data_1410",
                title="Terminal gap opening penalty",
                description="""A number defining the penalty for opening gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.""",
                meaning=EDAM["data_1410"]))
        setattr(cls, "edam:data_1411",
            PermissibleValue(
                text="edam:data_1411",
                title="Terminal gap extension penalty",
                description="""A number defining the penalty for extending gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.""",
                meaning=EDAM["data_1411"]))
        setattr(cls, "edam:data_1412",
            PermissibleValue(
                text="edam:data_1412",
                title="Sequence identity",
                description="""Sequence identity is the number (%) of matches (identical characters) in positions from an alignment of two molecular sequences.""",
                meaning=EDAM["data_1412"]))
        setattr(cls, "edam:data_1413",
            PermissibleValue(
                text="edam:data_1413",
                title="Sequence similarity",
                description="""Data Type is float probably.
Sequence similarity is the similarity (expressed as a percentage) of two molecular sequences calculated from their alignment, a scoring matrix for scoring characters substitutions and penalties for gap insertion and extension.""",
                meaning=EDAM["data_1413"]))
        setattr(cls, "edam:data_1426",
            PermissibleValue(
                text="edam:data_1426",
                title="Phylogenetic continuous quantitative data",
                description="Continuous quantitative data that may be read during phylogenetic tree calculation.",
                meaning=EDAM["data_1426"]))
        setattr(cls, "edam:data_1427",
            PermissibleValue(
                text="edam:data_1427",
                title="Phylogenetic discrete data",
                description="""Character data with discrete states that may be read during phylogenetic tree calculation.""",
                meaning=EDAM["data_1427"]))
        setattr(cls, "edam:data_1428",
            PermissibleValue(
                text="edam:data_1428",
                title="Phylogenetic character cliques",
                description="""One or more cliques of mutually compatible characters that are generated, for example from analysis of discrete character data, and are used to generate a phylogeny.""",
                meaning=EDAM["data_1428"]))
        setattr(cls, "edam:data_1429",
            PermissibleValue(
                text="edam:data_1429",
                title="Phylogenetic invariants",
                description="Phylogenetic invariants data for testing alternative tree topologies.",
                meaning=EDAM["data_1429"]))
        setattr(cls, "edam:data_1439",
            PermissibleValue(
                text="edam:data_1439",
                title="DNA substitution model",
                description="""A model of DNA substitution that explains a DNA sequence alignment, derived from phylogenetic tree analysis.""",
                meaning=EDAM["data_1439"]))
        setattr(cls, "edam:data_1442",
            PermissibleValue(
                text="edam:data_1442",
                title="Phylogenetic tree distances",
                description="Distances, such as Branch Score distance, between two or more phylogenetic trees.",
                meaning=EDAM["data_1442"]))
        setattr(cls, "edam:data_1444",
            PermissibleValue(
                text="edam:data_1444",
                title="Phylogenetic character contrasts",
                description="""Independent contrasts for characters used in a phylogenetic tree, or covariances, regressions and correlations between characters for those contrasts.""",
                meaning=EDAM["data_1444"]))
        setattr(cls, "edam:data_1448",
            PermissibleValue(
                text="edam:data_1448",
                title="Comparison matrix (nucleotide)",
                description="Matrix of integer or floating point numbers for nucleotide comparison.",
                meaning=EDAM["data_1448"]))
        setattr(cls, "edam:data_1449",
            PermissibleValue(
                text="edam:data_1449",
                title="Comparison matrix (amino acid)",
                description="Matrix of integer or floating point numbers for amino acid comparison.",
                meaning=EDAM["data_1449"]))
        setattr(cls, "edam:data_1459",
            PermissibleValue(
                text="edam:data_1459",
                title="Nucleic acid structure",
                description="3D coordinate and associated data for a nucleic acid tertiary (3D) structure.",
                meaning=EDAM["data_1459"]))
        setattr(cls, "edam:data_1460",
            PermissibleValue(
                text="edam:data_1460",
                title="Protein structure",
                description="""3D coordinate and associated data for a protein tertiary (3D) structure, or part of a structure, possibly in complex with other molecules.""",
                meaning=EDAM["data_1460"]))
        setattr(cls, "edam:data_1461",
            PermissibleValue(
                text="edam:data_1461",
                title="Protein-ligand complex",
                description="""The structure of a protein in complex with a ligand, typically a small molecule such as an enzyme substrate or cofactor, but possibly another macromolecule.
This includes interactions of proteins with atoms, ions and small molecules or macromolecules such as nucleic acids or other polypeptides. For stable inter-polypeptide interactions use 'Protein complex' instead.""",
                meaning=EDAM["data_1461"]))
        setattr(cls, "edam:data_1462",
            PermissibleValue(
                text="edam:data_1462",
                title="Carbohydrate structure",
                description="3D coordinate and associated data for a carbohydrate (3D) structure.",
                meaning=EDAM["data_1462"]))
        setattr(cls, "edam:data_1463",
            PermissibleValue(
                text="edam:data_1463",
                title="Small molecule structure",
                description="""3D coordinate and associated data for the (3D) structure of a small molecule, such as any common chemical compound.""",
                meaning=EDAM["data_1463"]))
        setattr(cls, "edam:data_1464",
            PermissibleValue(
                text="edam:data_1464",
                title="DNA structure",
                description="3D coordinate and associated data for a DNA tertiary (3D) structure.",
                meaning=EDAM["data_1464"]))
        setattr(cls, "edam:data_1465",
            PermissibleValue(
                text="edam:data_1465",
                title="RNA structure",
                description="3D coordinate and associated data for an RNA tertiary (3D) structure.",
                meaning=EDAM["data_1465"]))
        setattr(cls, "edam:data_1466",
            PermissibleValue(
                text="edam:data_1466",
                title="tRNA structure",
                description="""3D coordinate and associated data for a tRNA tertiary (3D) structure, including tmRNA, snoRNAs etc.""",
                meaning=EDAM["data_1466"]))
        setattr(cls, "edam:data_1467",
            PermissibleValue(
                text="edam:data_1467",
                title="Protein chain",
                description="""3D coordinate and associated data for the tertiary (3D) structure of a polypeptide chain.""",
                meaning=EDAM["data_1467"]))
        setattr(cls, "edam:data_1468",
            PermissibleValue(
                text="edam:data_1468",
                title="Protein domain",
                description="3D coordinate and associated data for the tertiary (3D) structure of a protein domain.",
                meaning=EDAM["data_1468"]))
        setattr(cls, "edam:data_1470",
            PermissibleValue(
                text="edam:data_1470",
                title="C-alpha trace",
                description="""3D coordinate and associated data for a protein tertiary (3D) structure (typically C-alpha atoms only).
C-beta atoms from amino acid side-chains may be included.""",
                meaning=EDAM["data_1470"]))
        setattr(cls, "edam:data_1479",
            PermissibleValue(
                text="edam:data_1479",
                title="Structure alignment (pair)",
                description="Alignment (superimposition) of exactly two molecular tertiary (3D) structures.",
                meaning=EDAM["data_1479"]))
        setattr(cls, "edam:data_1481",
            PermissibleValue(
                text="edam:data_1481",
                title="Protein structure alignment",
                description="Alignment (superimposition) of protein tertiary (3D) structures.",
                meaning=EDAM["data_1481"]))
        setattr(cls, "edam:data_1482",
            PermissibleValue(
                text="edam:data_1482",
                title="Nucleic acid structure alignment",
                description="Alignment (superimposition) of nucleic acid tertiary (3D) structures.",
                meaning=EDAM["data_1482"]))
        setattr(cls, "edam:data_1493",
            PermissibleValue(
                text="edam:data_1493",
                title="RNA structure alignment",
                description="Alignment (superimposition) of RNA tertiary (3D) structures.",
                meaning=EDAM["data_1493"]))
        setattr(cls, "edam:data_1494",
            PermissibleValue(
                text="edam:data_1494",
                title="Structural transformation matrix",
                description="""Matrix to transform (rotate/translate) 3D coordinates, typically the transformation necessary to superimpose two molecular structures.""",
                meaning=EDAM["data_1494"]))
        setattr(cls, "edam:data_1497",
            PermissibleValue(
                text="edam:data_1497",
                title="Root-mean-square deviation",
                description="""Root-mean-square deviation (RMSD) is calculated to measure the average distance between superimposed macromolecular coordinates.""",
                meaning=EDAM["data_1497"]))
        setattr(cls, "edam:data_1498",
            PermissibleValue(
                text="edam:data_1498",
                title="Tanimoto similarity score",
                description="""A ligand fingerprint is derived from ligand structural data from a Protein DataBank file. It reflects the elements or groups present or absent, covalent bonds and bond orders and the bonded environment in terms of SATIS codes and BLEEP atom types.
A measure of the similarity between two ligand fingerprints.""",
                meaning=EDAM["data_1498"]))
        setattr(cls, "edam:data_1499",
            PermissibleValue(
                text="edam:data_1499",
                title="3D-1D scoring matrix",
                description="""A matrix of 3D-1D scores reflecting the probability of amino acids to occur in different tertiary structural environments.""",
                meaning=EDAM["data_1499"]))
        setattr(cls, "edam:data_1501",
            PermissibleValue(
                text="edam:data_1501",
                title="Amino acid index",
                description="""A table of 20 numerical values which quantify a property (e.g. physicochemical or biochemical) of the common amino acids.""",
                meaning=EDAM["data_1501"]))
        setattr(cls, "edam:data_1502",
            PermissibleValue(
                text="edam:data_1502",
                title="Amino acid index (chemical classes)",
                description="""Chemical classification (small, aliphatic, aromatic, polar, charged etc) of amino acids.""",
                meaning=EDAM["data_1502"]))
        setattr(cls, "edam:data_1503",
            PermissibleValue(
                text="edam:data_1503",
                title="Amino acid pair-wise contact potentials",
                description="Statistical protein contact potentials.",
                meaning=EDAM["data_1503"]))
        setattr(cls, "edam:data_1505",
            PermissibleValue(
                text="edam:data_1505",
                title="Amino acid index (molecular weight)",
                description="Molecular weights of amino acids.",
                meaning=EDAM["data_1505"]))
        setattr(cls, "edam:data_1506",
            PermissibleValue(
                text="edam:data_1506",
                title="Amino acid index (hydropathy)",
                description="Hydrophobic, hydrophilic or charge properties of amino acids.",
                meaning=EDAM["data_1506"]))
        setattr(cls, "edam:data_1507",
            PermissibleValue(
                text="edam:data_1507",
                title="Amino acid index (White-Wimley data)",
                description="""Experimental free energy values for the water-interface and water-octanol transitions for the amino acids.""",
                meaning=EDAM["data_1507"]))
        setattr(cls, "edam:data_1508",
            PermissibleValue(
                text="edam:data_1508",
                title="Amino acid index (van der Waals radii)",
                description="Van der Waals radii of atoms for different amino acid residues.",
                meaning=EDAM["data_1508"]))
        setattr(cls, "edam:data_1519",
            PermissibleValue(
                text="edam:data_1519",
                title="Peptide molecular weights",
                description="""List of molecular weight(s) of one or more proteins or peptides, for example cut by proteolytic enzymes or reagents.
The report might include associated data such as frequency of peptide fragment molecular weights.""",
                meaning=EDAM["data_1519"]))
        setattr(cls, "edam:data_1520",
            PermissibleValue(
                text="edam:data_1520",
                title="Peptide hydrophobic moment",
                description="""Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation.
Report on the hydrophobic moment of a polypeptide sequence.""",
                meaning=EDAM["data_1520"]))
        setattr(cls, "edam:data_1521",
            PermissibleValue(
                text="edam:data_1521",
                title="Protein aliphatic index",
                description="""The aliphatic index is the relative protein volume occupied by aliphatic side chains.
The aliphatic index of a protein.""",
                meaning=EDAM["data_1521"]))
        setattr(cls, "edam:data_1522",
            PermissibleValue(
                text="edam:data_1522",
                title="Protein sequence hydropathy plot",
                description="""A protein sequence with annotation on hydrophobic or hydrophilic / charged regions, hydrophobicity plot etc.
Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation.""",
                meaning=EDAM["data_1522"]))
        setattr(cls, "edam:data_1523",
            PermissibleValue(
                text="edam:data_1523",
                title="Protein charge plot",
                description="""A plot of the mean charge of the amino acids within a window of specified length as the window is moved along a protein sequence.""",
                meaning=EDAM["data_1523"]))
        setattr(cls, "edam:data_1524",
            PermissibleValue(
                text="edam:data_1524",
                title="Protein solubility",
                description="The solubility or atomic solvation energy of a protein sequence or structure.",
                meaning=EDAM["data_1524"]))
        setattr(cls, "edam:data_1525",
            PermissibleValue(
                text="edam:data_1525",
                title="Protein crystallizability",
                description="Data on the crystallizability of a protein sequence.",
                meaning=EDAM["data_1525"]))
        setattr(cls, "edam:data_1526",
            PermissibleValue(
                text="edam:data_1526",
                title="Protein globularity",
                description="Data on the stability, intrinsic disorder or globularity of a protein sequence.",
                meaning=EDAM["data_1526"]))
        setattr(cls, "edam:data_1527",
            PermissibleValue(
                text="edam:data_1527",
                title="Protein titration curve",
                description="The titration curve of a protein.",
                meaning=EDAM["data_1527"]))
        setattr(cls, "edam:data_1528",
            PermissibleValue(
                text="edam:data_1528",
                title="Protein isoelectric point",
                description="The isoelectric point of one proteins.",
                meaning=EDAM["data_1528"]))
        setattr(cls, "edam:data_1529",
            PermissibleValue(
                text="edam:data_1529",
                title="Protein pKa value",
                description="The pKa value of a protein.",
                meaning=EDAM["data_1529"]))
        setattr(cls, "edam:data_1530",
            PermissibleValue(
                text="edam:data_1530",
                title="Protein hydrogen exchange rate",
                description="The hydrogen exchange rate of a protein.",
                meaning=EDAM["data_1530"]))
        setattr(cls, "edam:data_1531",
            PermissibleValue(
                text="edam:data_1531",
                title="Protein extinction coefficient",
                description="The extinction coefficient of a protein.",
                meaning=EDAM["data_1531"]))
        setattr(cls, "edam:data_1532",
            PermissibleValue(
                text="edam:data_1532",
                title="Protein optical density",
                description="The optical density of a protein.",
                meaning=EDAM["data_1532"]))
        setattr(cls, "edam:data_1534",
            PermissibleValue(
                text="edam:data_1534",
                title="Peptide immunogenicity data",
                description="""An report on allergenicity / immunogenicity of peptides and proteins.
This includes data on peptide ligands that elicit an immune response (immunogens), allergic cross-reactivity, predicted antigenicity (Hopp and Woods plot) etc. These data are useful in the development of peptide-specific antibodies or multi-epitope vaccines. Methods might use sequence data (for example motifs) and / or structural data.""",
                meaning=EDAM["data_1534"]))
        setattr(cls, "edam:data_1537",
            PermissibleValue(
                text="edam:data_1537",
                title="Protein structure report",
                description="""A human-readable collection of information about one or more specific protein 3D structure(s) or structural domains.""",
                meaning=EDAM["data_1537"]))
        setattr(cls, "edam:data_1539",
            PermissibleValue(
                text="edam:data_1539",
                title="Protein structural quality report",
                description="""Model validation might involve checks for atomic packing, steric clashes, agreement with electron density maps etc.
Report on the quality of a protein three-dimensional model.""",
                meaning=EDAM["data_1539"]))
        setattr(cls, "edam:data_1542",
            PermissibleValue(
                text="edam:data_1542",
                title="Protein solvent accessibility",
                description="""Data on the solvent accessible or buried surface area of a protein structure.
This concept covers definitions of the protein surface, interior and interfaces, accessible and buried residues, surface accessible pockets, interior inaccessible cavities etc.""",
                meaning=EDAM["data_1542"]))
        setattr(cls, "edam:data_1544",
            PermissibleValue(
                text="edam:data_1544",
                title="Ramachandran plot",
                description="Phi/psi angle data or a Ramachandran plot of a protein structure.",
                meaning=EDAM["data_1544"]))
        setattr(cls, "edam:data_1545",
            PermissibleValue(
                text="edam:data_1545",
                title="Protein dipole moment",
                description="Data on the net charge distribution (dipole moment) of a protein structure.",
                meaning=EDAM["data_1545"]))
        setattr(cls, "edam:data_1546",
            PermissibleValue(
                text="edam:data_1546",
                title="Protein distance matrix",
                description="""A matrix of distances between amino acid residues (for example the C-alpha atoms) in a protein structure.""",
                meaning=EDAM["data_1546"]))
        setattr(cls, "edam:data_1547",
            PermissibleValue(
                text="edam:data_1547",
                title="Protein contact map",
                description="An amino acid residue contact map for a protein structure.",
                meaning=EDAM["data_1547"]))
        setattr(cls, "edam:data_1548",
            PermissibleValue(
                text="edam:data_1548",
                title="Protein residue 3D cluster",
                description="""Report on clusters of contacting residues in protein structures such as a key structural residue network.""",
                meaning=EDAM["data_1548"]))
        setattr(cls, "edam:data_1549",
            PermissibleValue(
                text="edam:data_1549",
                title="Protein hydrogen bonds",
                description="Patterns of hydrogen bonding in protein structures.",
                meaning=EDAM["data_1549"]))
        setattr(cls, "edam:data_1566",
            PermissibleValue(
                text="edam:data_1566",
                title="Protein-ligand interaction report",
                description="An informative report on protein-ligand (small molecule) interaction(s).",
                meaning=EDAM["data_1566"]))
        setattr(cls, "edam:data_1583",
            PermissibleValue(
                text="edam:data_1583",
                title="Nucleic acid melting profile",
                description="""A melting (stability) profile calculated the free energy required to unwind and separate the nucleic acid strands, plotted for sliding windows over a sequence.
Data on the dissociation characteristics of a double-stranded nucleic acid molecule (DNA or a DNA/RNA hybrid) during heating.
Nucleic acid melting curve: a melting curve of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the proportion of nucleic acid which are double-stranded versus temperature.
Nucleic acid probability profile: a probability profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the probability of a base pair not being melted (i.e. remaining as double-stranded DNA) at a specified temperature
Nucleic acid stitch profile: stitch profile of hybridised or double stranded nucleic acid (DNA or RNA/DNA). A stitch profile diagram shows partly melted DNA conformations (with probabilities) at a range of temperatures. For example, a stitch profile might show possible loop openings with their location, size, probability and fluctuations at a given temperature.
Nucleic acid temperature profile: a temperature profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Plots melting temperature versus base position.""",
                meaning=EDAM["data_1583"]))
        setattr(cls, "edam:data_1584",
            PermissibleValue(
                text="edam:data_1584",
                title="Nucleic acid enthalpy",
                description="Enthalpy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).",
                meaning=EDAM["data_1584"]))
        setattr(cls, "edam:data_1585",
            PermissibleValue(
                text="edam:data_1585",
                title="Nucleic acid entropy",
                description="Entropy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).",
                meaning=EDAM["data_1585"]))
        setattr(cls, "edam:data_1588",
            PermissibleValue(
                text="edam:data_1588",
                title="DNA base pair stacking energies data",
                description="DNA base pair stacking energies data.",
                meaning=EDAM["data_1588"]))
        setattr(cls, "edam:data_1589",
            PermissibleValue(
                text="edam:data_1589",
                title="DNA base pair twist angle data",
                description="DNA base pair twist angle data.",
                meaning=EDAM["data_1589"]))
        setattr(cls, "edam:data_1590",
            PermissibleValue(
                text="edam:data_1590",
                title="DNA base trimer roll angles data",
                description="DNA base trimer roll angles data.",
                meaning=EDAM["data_1590"]))
        setattr(cls, "edam:data_1595",
            PermissibleValue(
                text="edam:data_1595",
                title="Base pairing probability matrix dotplot",
                description="""Dotplot of RNA base pairing probability matrix.
Such as generated by the Vienna package.""",
                meaning=EDAM["data_1595"]))
        setattr(cls, "edam:data_1596",
            PermissibleValue(
                text="edam:data_1596",
                title="Nucleic acid folding report",
                description="""A human-readable collection of information about RNA/DNA folding, minimum folding energies for DNA or RNA sequences, energy landscape of RNA mutants etc.""",
                meaning=EDAM["data_1596"]))
        setattr(cls, "edam:data_1597",
            PermissibleValue(
                text="edam:data_1597",
                title="Codon usage table",
                description="""A codon usage table might include the codon usage table name, optional comments and a table with columns for codons and corresponding codon usage data. A genetic code can be extracted from or represented by a codon usage table.
Table of codon usage data calculated from one or more nucleic acid sequences.""",
                meaning=EDAM["data_1597"]))
        setattr(cls, "edam:data_1598",
            PermissibleValue(
                text="edam:data_1598",
                title="Genetic code",
                description="""A genetic code for an organism.
A genetic code need not include detailed codon usage information.""",
                meaning=EDAM["data_1598"]))
        setattr(cls, "edam:data_1600",
            PermissibleValue(
                text="edam:data_1600",
                title="Codon usage bias plot",
                description="""A plot of the synonymous codon usage calculated for windows over a nucleotide sequence.""",
                meaning=EDAM["data_1600"]))
        setattr(cls, "edam:data_1602",
            PermissibleValue(
                text="edam:data_1602",
                title="Codon usage fraction difference",
                description="The differences in codon usage fractions between two codon usage tables.",
                meaning=EDAM["data_1602"]))
        setattr(cls, "edam:data_1621",
            PermissibleValue(
                text="edam:data_1621",
                title="Pharmacogenomic test report",
                description="""A human-readable collection of information about the influence of genotype on drug response.
The report might correlate gene expression or single-nucleotide polymorphisms with drug efficacy or toxicity.""",
                meaning=EDAM["data_1621"]))
        setattr(cls, "edam:data_1622",
            PermissibleValue(
                text="edam:data_1622",
                title="Disease report",
                description="""A human-readable collection of information about a specific disease.
For example, an informative report on a specific tumor including nature and origin of the sample, anatomic site, organ or tissue, tumor type, including morphology and/or histologic type, and so on.""",
                meaning=EDAM["data_1622"]))
        setattr(cls, "edam:data_1636",
            PermissibleValue(
                text="edam:data_1636",
                title="Heat map",
                description="""A graphical 2D tabular representation of expression data, typically derived from an omics experiment. A heat map is a table where rows and columns correspond to different features and contexts (for example, cells or samples) and the cell colour represents the level of expression of a gene that context.""",
                meaning=EDAM["data_1636"]))
        setattr(cls, "edam:data_1667",
            PermissibleValue(
                text="edam:data_1667",
                title="E-value",
                description="""A simple floating point number defining the lower or upper limit of an expectation value (E-value).
An expectation value (E-Value) is the expected number of observations which are at least as extreme as observations expected to occur by random chance. The E-value describes the number of hits with a given score or better that are expected to occur at random when searching a database of a particular size. It decreases exponentially with the score (S) of a hit. A low E value indicates a more significant score.""",
                meaning=EDAM["data_1667"]))
        setattr(cls, "edam:data_1668",
            PermissibleValue(
                text="edam:data_1668",
                title="Z-value",
                description="""A z-value might be specified as a threshold for reporting hits from database searches.
The z-value is the number of standard deviations a data value is above or below a mean value.""",
                meaning=EDAM["data_1668"]))
        setattr(cls, "edam:data_1669",
            PermissibleValue(
                text="edam:data_1669",
                title="P-value",
                description="""A z-value might be specified as a threshold for reporting hits from database searches.
The P-value is the probability of obtaining by random chance a result that is at least as extreme as an observed result, assuming a NULL hypothesis is true.""",
                meaning=EDAM["data_1669"]))
        setattr(cls, "edam:data_1689",
            PermissibleValue(
                text="edam:data_1689",
                title="Username",
                description="A username on a computer system or a website.",
                meaning=EDAM["data_1689"]))
        setattr(cls, "edam:data_1690",
            PermissibleValue(
                text="edam:data_1690",
                title="Password",
                description="A password on a computer system, or a website.",
                meaning=EDAM["data_1690"]))
        setattr(cls, "edam:data_1691",
            PermissibleValue(
                text="edam:data_1691",
                title="Email address",
                description="A valid email address of an end-user.",
                meaning=EDAM["data_1691"]))
        setattr(cls, "edam:data_1692",
            PermissibleValue(
                text="edam:data_1692",
                title="Person name",
                description="The name of a person.",
                meaning=EDAM["data_1692"]))
        setattr(cls, "edam:data_1696",
            PermissibleValue(
                text="edam:data_1696",
                title="Drug report",
                description="""A drug structure relationship map is report (typically a map diagram) of drug structure relationships.
A human-readable collection of information about a specific drug.""",
                meaning=EDAM["data_1696"]))
        setattr(cls, "edam:data_1707",
            PermissibleValue(
                text="edam:data_1707",
                title="Phylogenetic tree image",
                description="""An image (for viewing or printing) of a phylogenetic tree including (typically) a plot of rooted or unrooted phylogenies, cladograms, circular trees or phenograms and associated information.
See also 'Phylogenetic tree'""",
                meaning=EDAM["data_1707"]))
        setattr(cls, "edam:data_1708",
            PermissibleValue(
                text="edam:data_1708",
                title="RNA secondary structure image",
                description="Image of RNA secondary structure, knots, pseudoknots etc.",
                meaning=EDAM["data_1708"]))
        setattr(cls, "edam:data_1709",
            PermissibleValue(
                text="edam:data_1709",
                title="Protein secondary structure image",
                description="Image of protein secondary structure.",
                meaning=EDAM["data_1709"]))
        setattr(cls, "edam:data_1710",
            PermissibleValue(
                text="edam:data_1710",
                title="Structure image",
                description="Image of one or more molecular tertiary (3D) structures.",
                meaning=EDAM["data_1710"]))
        setattr(cls, "edam:data_1711",
            PermissibleValue(
                text="edam:data_1711",
                title="Sequence alignment image",
                description="""Image of two or more aligned molecular sequences possibly annotated with alignment features.""",
                meaning=EDAM["data_1711"]))
        setattr(cls, "edam:data_1712",
            PermissibleValue(
                text="edam:data_1712",
                title="Chemical structure image",
                description="""An image of the structure of a small chemical compound.
The molecular identifier and formula are typically included.""",
                meaning=EDAM["data_1712"]))
        setattr(cls, "edam:data_1713",
            PermissibleValue(
                text="edam:data_1713",
                title="Fate map",
                description="""A fate map is a plan of early stage of an embryo such as a blastula, showing areas that are significance to development.""",
                meaning=EDAM["data_1713"]))
        setattr(cls, "edam:data_1714",
            PermissibleValue(
                text="edam:data_1714",
                title="Microarray spots image",
                description="An image of spots from a microarray experiment.",
                meaning=EDAM["data_1714"]))
        setattr(cls, "edam:data_1731",
            PermissibleValue(
                text="edam:data_1731",
                title="Ontology concept definition",
                description="The definition of a concept from an ontology.",
                meaning=EDAM["data_1731"]))
        setattr(cls, "edam:data_1742",
            PermissibleValue(
                text="edam:data_1742",
                title="PDB residue number",
                description="A residue identifier (a string) from a PDB file.",
                meaning=EDAM["data_1742"]))
        setattr(cls, "edam:data_1743",
            PermissibleValue(
                text="edam:data_1743",
                title="Atomic coordinate",
                description="Cartesian coordinate of an atom (in a molecular structure).",
                meaning=EDAM["data_1743"]))
        setattr(cls, "edam:data_1748",
            PermissibleValue(
                text="edam:data_1748",
                title="PDB atom name",
                description="Identifier (a string) of a specific atom from a PDB file for a molecular structure.",
                meaning=EDAM["data_1748"]))
        setattr(cls, "edam:data_1755",
            PermissibleValue(
                text="edam:data_1755",
                title="Protein atom",
                description="""Data on a single atom from a protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.""",
                meaning=EDAM["data_1755"]))
        setattr(cls, "edam:data_1756",
            PermissibleValue(
                text="edam:data_1756",
                title="Protein residue",
                description="""Data on a single amino acid residue position in a protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.""",
                meaning=EDAM["data_1756"]))
        setattr(cls, "edam:data_1757",
            PermissibleValue(
                text="edam:data_1757",
                title="Atom name",
                description="Name of an atom.",
                meaning=EDAM["data_1757"]))
        setattr(cls, "edam:data_1758",
            PermissibleValue(
                text="edam:data_1758",
                title="PDB residue name",
                description="Three-letter amino acid residue names as used in PDB files.",
                meaning=EDAM["data_1758"]))
        setattr(cls, "edam:data_1759",
            PermissibleValue(
                text="edam:data_1759",
                title="PDB model number",
                description="Identifier of a model structure from a PDB file.",
                meaning=EDAM["data_1759"]))
        setattr(cls, "edam:data_1771",
            PermissibleValue(
                text="edam:data_1771",
                title="Sequence version",
                description="Information on an molecular sequence version.",
                meaning=EDAM["data_1771"]))
        setattr(cls, "edam:data_1772",
            PermissibleValue(
                text="edam:data_1772",
                title="Score",
                description="""A numerical value, that is some type of scored value arising for example from a prediction method.""",
                meaning=EDAM["data_1772"]))
        setattr(cls, "edam:data_1794",
            PermissibleValue(
                text="edam:data_1794",
                title="Gene ID (PlasmoDB)",
                description="Identifier of a gene from PlasmoDB Plasmodium Genome Resource.",
                meaning=EDAM["data_1794"]))
        setattr(cls, "edam:data_1795",
            PermissibleValue(
                text="edam:data_1795",
                title="Gene ID (EcoGene)",
                description="Identifier of a gene from EcoGene Database.",
                meaning=EDAM["data_1795"]))
        setattr(cls, "edam:data_1796",
            PermissibleValue(
                text="edam:data_1796",
                title="Gene ID (FlyBase)",
                description="Gene identifier from FlyBase database.",
                meaning=EDAM["data_1796"]))
        setattr(cls, "edam:data_1802",
            PermissibleValue(
                text="edam:data_1802",
                title="Gene ID (Gramene)",
                description="Gene identifier from Gramene database.",
                meaning=EDAM["data_1802"]))
        setattr(cls, "edam:data_1803",
            PermissibleValue(
                text="edam:data_1803",
                title="Gene ID (Virginia microbial)",
                description="Gene identifier from Virginia Bioinformatics Institute microbial database.",
                meaning=EDAM["data_1803"]))
        setattr(cls, "edam:data_1804",
            PermissibleValue(
                text="edam:data_1804",
                title="Gene ID (SGN)",
                description="Gene identifier from Sol Genomics Network.",
                meaning=EDAM["data_1804"]))
        setattr(cls, "edam:data_1805",
            PermissibleValue(
                text="edam:data_1805",
                title="Gene ID (WormBase)",
                description="Gene identifier used by WormBase database.",
                meaning=EDAM["data_1805"]))
        setattr(cls, "edam:data_1807",
            PermissibleValue(
                text="edam:data_1807",
                title="ORF name",
                description="The name of an open reading frame attributed by a sequencing project.",
                meaning=EDAM["data_1807"]))
        setattr(cls, "edam:data_1855",
            PermissibleValue(
                text="edam:data_1855",
                title="Clone ID",
                description="An identifier of a clone (cloned molecular sequence) from a database.",
                meaning=EDAM["data_1855"]))
        setattr(cls, "edam:data_1856",
            PermissibleValue(
                text="edam:data_1856",
                title="PDB insertion code",
                description="""An insertion code (part of the residue number) for an amino acid residue from a PDB file.""",
                meaning=EDAM["data_1856"]))
        setattr(cls, "edam:data_1857",
            PermissibleValue(
                text="edam:data_1857",
                title="Atomic occupancy",
                description="""The fraction of an atom type present at a site in a molecular structure.
The sum of the occupancies of all the atom types at a site should not normally significantly exceed 1.0.""",
                meaning=EDAM["data_1857"]))
        setattr(cls, "edam:data_1858",
            PermissibleValue(
                text="edam:data_1858",
                title="Isotropic B factor",
                description="Isotropic B factor (atomic displacement parameter) for an atom from a PDB file.",
                meaning=EDAM["data_1858"]))
        setattr(cls, "edam:data_1859",
            PermissibleValue(
                text="edam:data_1859",
                title="Deletion map",
                description="""A cytogenetic map is built from a set of mutant cell lines with sub-chromosomal deletions and a reference wild-type line ('genome deletion panel'). The panel is used to map markers onto the genome by comparing mutant to wild-type banding patterns. Markers are linked (occur in the same deleted region) if they share the same banding pattern (presence or absence) as the deletion panel.
A cytogenetic map showing chromosome banding patterns in mutant cell lines relative to the wild type.""",
                meaning=EDAM["data_1859"]))
        setattr(cls, "edam:data_1860",
            PermissibleValue(
                text="edam:data_1860",
                title="QTL map",
                description="""A genetic map which shows the approximate location of quantitative trait loci (QTL) between two or more markers.""",
                meaning=EDAM["data_1860"]))
        setattr(cls, "edam:data_1863",
            PermissibleValue(
                text="edam:data_1863",
                title="Haplotype map",
                description="""A map of haplotypes in a genome or other sequence, describing common patterns of genetic variation.""",
                meaning=EDAM["data_1863"]))
        setattr(cls, "edam:data_1867",
            PermissibleValue(
                text="edam:data_1867",
                title="Protein fold name",
                description="The name of a protein fold.",
                meaning=EDAM["data_1867"]))
        setattr(cls, "edam:data_1868",
            PermissibleValue(
                text="edam:data_1868",
                title="Taxon",
                description="""For a complete list of taxonomic ranks see https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary.
The name of a group of organisms belonging to the same taxonomic rank.""",
                meaning=EDAM["data_1868"]))
        setattr(cls, "edam:data_1869",
            PermissibleValue(
                text="edam:data_1869",
                title="Organism identifier",
                description="A unique identifier of a (group of) organisms.",
                meaning=EDAM["data_1869"]))
        setattr(cls, "edam:data_1870",
            PermissibleValue(
                text="edam:data_1870",
                title="Genus name",
                description="The name of a genus of organism.",
                meaning=EDAM["data_1870"]))
        setattr(cls, "edam:data_1872",
            PermissibleValue(
                text="edam:data_1872",
                title="Taxonomic classification",
                description="""Name components correspond to levels in a taxonomic hierarchy (e.g. 'Genus', 'Species', etc.) Meta information such as a reference where the name was defined and a date might be included.
The full name for a group of organisms, reflecting their biological classification and (usually) conforming to a standard nomenclature.""",
                meaning=EDAM["data_1872"]))
        setattr(cls, "edam:data_1873",
            PermissibleValue(
                text="edam:data_1873",
                title="iHOP organism ID",
                description="A unique identifier for an organism used in the iHOP database.",
                meaning=EDAM["data_1873"]))
        setattr(cls, "edam:data_1874",
            PermissibleValue(
                text="edam:data_1874",
                title="Genbank common name",
                description="Common name for an organism as used in the GenBank database.",
                meaning=EDAM["data_1874"]))
        setattr(cls, "edam:data_1875",
            PermissibleValue(
                text="edam:data_1875",
                title="NCBI taxon",
                description="The name of a taxon from the NCBI taxonomy database.",
                meaning=EDAM["data_1875"]))
        setattr(cls, "edam:data_1881",
            PermissibleValue(
                text="edam:data_1881",
                title="Author ID",
                description="Information on the authors of a published work.",
                meaning=EDAM["data_1881"]))
        setattr(cls, "edam:data_1882",
            PermissibleValue(
                text="edam:data_1882",
                title="DragonDB author identifier",
                description="An identifier representing an author in the DragonDB database.",
                meaning=EDAM["data_1882"]))
        setattr(cls, "edam:data_1883",
            PermissibleValue(
                text="edam:data_1883",
                title="Annotated URI",
                description="A URI along with annotation describing the data found at the address.",
                meaning=EDAM["data_1883"]))
        setattr(cls, "edam:data_1885",
            PermissibleValue(
                text="edam:data_1885",
                title="Gene ID (GeneFarm)",
                description="Identifier of a gene from the GeneFarm database.",
                meaning=EDAM["data_1885"]))
        setattr(cls, "edam:data_1886",
            PermissibleValue(
                text="edam:data_1886",
                title="Blattner number",
                description="The blattner identifier for a gene.",
                meaning=EDAM["data_1886"]))
        setattr(cls, "edam:data_1891",
            PermissibleValue(
                text="edam:data_1891",
                title="iHOP symbol",
                description="A unique identifier of a protein or gene used in the iHOP database.",
                meaning=EDAM["data_1891"]))
        setattr(cls, "edam:data_1893",
            PermissibleValue(
                text="edam:data_1893",
                title="Locus ID",
                description="""A unique name or other identifier of a genetic locus, typically conforming to a scheme that names loci (such as predicted genes) depending on their position in a molecular sequence, for example a completely sequenced genome or chromosome.""",
                meaning=EDAM["data_1893"]))
        setattr(cls, "edam:data_1895",
            PermissibleValue(
                text="edam:data_1895",
                title="Locus ID (AGI)",
                description="Locus identifier for Arabidopsis Genome Initiative (TAIR, TIGR and MIPS databases).",
                meaning=EDAM["data_1895"]))
        setattr(cls, "edam:data_1896",
            PermissibleValue(
                text="edam:data_1896",
                title="Locus ID (ASPGD)",
                description="Identifier for loci from ASPGD (Aspergillus Genome Database).",
                meaning=EDAM["data_1896"]))
        setattr(cls, "edam:data_1897",
            PermissibleValue(
                text="edam:data_1897",
                title="Locus ID (MGG)",
                description="Identifier for loci from Magnaporthe grisea Database at the Broad Institute.",
                meaning=EDAM["data_1897"]))
        setattr(cls, "edam:data_1898",
            PermissibleValue(
                text="edam:data_1898",
                title="Locus ID (CGD)",
                description="Identifier for loci from CGD (Candida Genome Database).",
                meaning=EDAM["data_1898"]))
        setattr(cls, "edam:data_1899",
            PermissibleValue(
                text="edam:data_1899",
                title="Locus ID (CMR)",
                description="""Locus identifier for Comprehensive Microbial Resource at the J. Craig Venter Institute.""",
                meaning=EDAM["data_1899"]))
        setattr(cls, "edam:data_1900",
            PermissibleValue(
                text="edam:data_1900",
                title="NCBI locus tag",
                description="Identifier for loci from NCBI database.",
                meaning=EDAM["data_1900"]))
        setattr(cls, "edam:data_1901",
            PermissibleValue(
                text="edam:data_1901",
                title="Locus ID (SGD)",
                description="Identifier for loci from SGD (Saccharomyces Genome Database).",
                meaning=EDAM["data_1901"]))
        setattr(cls, "edam:data_1902",
            PermissibleValue(
                text="edam:data_1902",
                title="Locus ID (MMP)",
                description="Identifier of loci from Maize Mapping Project.",
                meaning=EDAM["data_1902"]))
        setattr(cls, "edam:data_1903",
            PermissibleValue(
                text="edam:data_1903",
                title="Locus ID (DictyBase)",
                description="Identifier of locus from DictyBase (Dictyostelium discoideum).",
                meaning=EDAM["data_1903"]))
        setattr(cls, "edam:data_1904",
            PermissibleValue(
                text="edam:data_1904",
                title="Locus ID (EntrezGene)",
                description="Identifier of a locus from EntrezGene database.",
                meaning=EDAM["data_1904"]))
        setattr(cls, "edam:data_1905",
            PermissibleValue(
                text="edam:data_1905",
                title="Locus ID (MaizeGDB)",
                description="Identifier of locus from MaizeGDB (Maize genome database).",
                meaning=EDAM["data_1905"]))
        setattr(cls, "edam:data_1907",
            PermissibleValue(
                text="edam:data_1907",
                title="Gene ID (KOME)",
                description="Identifier of a gene from the KOME database.",
                meaning=EDAM["data_1907"]))
        setattr(cls, "edam:data_1908",
            PermissibleValue(
                text="edam:data_1908",
                title="Locus ID (Tropgene)",
                description="Identifier of a locus from the Tropgene database.",
                meaning=EDAM["data_1908"]))
        setattr(cls, "edam:data_1916",
            PermissibleValue(
                text="edam:data_1916",
                title="Alignment",
                description="An alignment of molecular sequences, structures or profiles derived from them.",
                meaning=EDAM["data_1916"]))
        setattr(cls, "edam:data_1917",
            PermissibleValue(
                text="edam:data_1917",
                title="Atomic property",
                description="Data for an atom (in a molecular structure).",
                meaning=EDAM["data_1917"]))
        setattr(cls, "edam:data_2007",
            PermissibleValue(
                text="edam:data_2007",
                title="UniProt keyword",
                description="""A word or phrase that can appear in the keywords field (KW line) of entries from the UniProt database.""",
                meaning=EDAM["data_2007"]))
        setattr(cls, "edam:data_2012",
            PermissibleValue(
                text="edam:data_2012",
                title="Sequence coordinates",
                description="""A position in a map (for example a genetic map), either a single position (point) or a region / interval.
This includes positions in genomes based on a reference sequence. A position may be specified for any mappable object, i.e. anything that may have positional information such as a physical position in a chromosome. Data might include sequence region name, strand, coordinate system name, assembly name, start position and end position.""",
                meaning=EDAM["data_2012"]))
        setattr(cls, "edam:data_2016",
            PermissibleValue(
                text="edam:data_2016",
                title="Amino acid property",
                description="""Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all amino acids.""",
                meaning=EDAM["data_2016"]))
        setattr(cls, "edam:data_2019",
            PermissibleValue(
                text="edam:data_2019",
                title="Map data",
                description="""Data describing a molecular map (genetic or physical) or a set of such maps, including various attributes of, data extracted from or derived from the analysis of them, but excluding the map(s) themselves. This includes metadata for map sets that share a common set of features which are mapped.""",
                meaning=EDAM["data_2019"]))
        setattr(cls, "edam:data_2024",
            PermissibleValue(
                text="edam:data_2024",
                title="Enzyme kinetics data",
                description="""Data concerning chemical reaction(s) catalysed by enzyme(s).
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2024"]))
        setattr(cls, "edam:data_2025",
            PermissibleValue(
                text="edam:data_2025",
                title="Michaelis Menten plot",
                description="""A plot giving an approximation of the kinetics of an enzyme-catalysed reaction, assuming simple kinetics (i.e. no intermediate or product inhibition, allostericity or cooperativity). It plots initial reaction rate to the substrate concentration (S) from which the maximum rate (vmax) is apparent.""",
                meaning=EDAM["data_2025"]))
        setattr(cls, "edam:data_2026",
            PermissibleValue(
                text="edam:data_2026",
                title="Hanes Woolf plot",
                description="""A plot based on the Michaelis Menten equation of enzyme kinetics plotting the ratio of the initial substrate concentration (S) against the reaction velocity (v).""",
                meaning=EDAM["data_2026"]))
        setattr(cls, "edam:data_2042",
            PermissibleValue(
                text="edam:data_2042",
                title="Evidence",
                description="""Typically a human-readable summary of body of facts or information indicating why a statement is true or valid. This may include a computational prediction, laboratory experiment, literature reference etc.""",
                meaning=EDAM["data_2042"]))
        setattr(cls, "edam:data_2044",
            PermissibleValue(
                text="edam:data_2044",
                title="Sequence",
                description="""One or more molecular sequences, possibly with associated annotation.
This concept is a placeholder of concepts for primary sequence data including raw sequences and sequence records. It should not normally be used for derivatives such as sequence alignments, motifs or profiles.""",
                meaning=EDAM["data_2044"]))
        setattr(cls, "edam:data_2048",
            PermissibleValue(
                text="edam:data_2048",
                title="Report",
                description="""A human-readable collection of information including annotation on a biological entity or phenomena, computer-generated reports of analysis of primary data (e.g. sequence or structural), and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
You can use this term by default for any textual report, in case you can't find another, more specific term. Reports may be generated automatically or collated by hand and can include metadata on the origin, source, history, ownership or location of some thing.""",
                meaning=EDAM["data_2048"]))
        setattr(cls, "edam:data_2050",
            PermissibleValue(
                text="edam:data_2050",
                title="Molecular property (general)",
                description="General data for a molecule.",
                meaning=EDAM["data_2050"]))
        setattr(cls, "edam:data_2070",
            PermissibleValue(
                text="edam:data_2070",
                title="Sequence motif (nucleic acid)",
                description="A nucleotide sequence motif.",
                meaning=EDAM["data_2070"]))
        setattr(cls, "edam:data_2071",
            PermissibleValue(
                text="edam:data_2071",
                title="Sequence motif (protein)",
                description="An amino acid sequence motif.",
                meaning=EDAM["data_2071"]))
        setattr(cls, "edam:data_2080",
            PermissibleValue(
                text="edam:data_2080",
                title="Database search results",
                description="A report of hits from searching a database of some type.",
                meaning=EDAM["data_2080"]))
        setattr(cls, "edam:data_2082",
            PermissibleValue(
                text="edam:data_2082",
                title="Matrix",
                description="""An array of numerical values.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2082"]))
        setattr(cls, "edam:data_2084",
            PermissibleValue(
                text="edam:data_2084",
                title="Nucleic acid report",
                description="""A human-readable collection of information about one or more specific nucleic acid molecules.""",
                meaning=EDAM["data_2084"]))
        setattr(cls, "edam:data_2085",
            PermissibleValue(
                text="edam:data_2085",
                title="Structure report",
                description="""A human-readable collection of information about one or more molecular tertiary (3D) structures. It might include annotation on the structure, a computer-generated report of analysis of structural data, and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.""",
                meaning=EDAM["data_2085"]))
        setattr(cls, "edam:data_2087",
            PermissibleValue(
                text="edam:data_2087",
                title="Molecular property",
                description="""A report on the physical (e.g. structural) or chemical properties of molecules, or parts of a molecule.""",
                meaning=EDAM["data_2087"]))
        setattr(cls, "edam:data_2088",
            PermissibleValue(
                text="edam:data_2088",
                title="DNA base structural data",
                description="Structural data for DNA base pairs or runs of bases, such as energy or angle data.",
                meaning=EDAM["data_2088"]))
        setattr(cls, "edam:data_2091",
            PermissibleValue(
                text="edam:data_2091",
                title="Accession",
                description="""A persistent (stable) and unique identifier, typically identifying an object (entry) from a database.""",
                meaning=EDAM["data_2091"]))
        setattr(cls, "edam:data_2093",
            PermissibleValue(
                text="edam:data_2093",
                title="Data reference",
                description="""A list of database accessions or identifiers are usually included.
Reference to a dataset (or a cross-reference between two datasets), typically one or more entries in a biological database or ontology.""",
                meaning=EDAM["data_2093"]))
        setattr(cls, "edam:data_2098",
            PermissibleValue(
                text="edam:data_2098",
                title="Job identifier",
                description="An identifier of a submitted job.",
                meaning=EDAM["data_2098"]))
        setattr(cls, "edam:data_2099",
            PermissibleValue(
                text="edam:data_2099",
                title="Name",
                description="A name of a thing, which need not necessarily uniquely identify it.",
                meaning=EDAM["data_2099"]))
        setattr(cls, "edam:data_2101",
            PermissibleValue(
                text="edam:data_2101",
                title="Account authentication",
                description="""Authentication data usually used to log in into an account on an information system such as a web application or a database.""",
                meaning=EDAM["data_2101"]))
        setattr(cls, "edam:data_2102",
            PermissibleValue(
                text="edam:data_2102",
                title="KEGG organism code",
                description="A three-letter code used in the KEGG databases to uniquely identify organisms.",
                meaning=EDAM["data_2102"]))
        setattr(cls, "edam:data_2104",
            PermissibleValue(
                text="edam:data_2104",
                title="BioCyc ID",
                description="Identifier of an object from one of the BioCyc databases.",
                meaning=EDAM["data_2104"]))
        setattr(cls, "edam:data_2105",
            PermissibleValue(
                text="edam:data_2105",
                title="Compound ID (BioCyc)",
                description="Identifier of a compound from the BioCyc chemical compounds database.",
                meaning=EDAM["data_2105"]))
        setattr(cls, "edam:data_2106",
            PermissibleValue(
                text="edam:data_2106",
                title="Reaction ID (BioCyc)",
                description="Identifier of a biological reaction from the BioCyc reactions database.",
                meaning=EDAM["data_2106"]))
        setattr(cls, "edam:data_2107",
            PermissibleValue(
                text="edam:data_2107",
                title="Enzyme ID (BioCyc)",
                description="Identifier of an enzyme from the BioCyc enzymes database.",
                meaning=EDAM["data_2107"]))
        setattr(cls, "edam:data_2108",
            PermissibleValue(
                text="edam:data_2108",
                title="Reaction ID",
                description="Identifier of a biological reaction from a database.",
                meaning=EDAM["data_2108"]))
        setattr(cls, "edam:data_2109",
            PermissibleValue(
                text="edam:data_2109",
                title="Identifier (hybrid)",
                description="""An identifier that is re-used for data objects of fundamentally different types (typically served from a single database).
This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'.""",
                meaning=EDAM["data_2109"]))
        setattr(cls, "edam:data_2110",
            PermissibleValue(
                text="edam:data_2110",
                title="Molecular property identifier",
                description="Identifier of a molecular property.",
                meaning=EDAM["data_2110"]))
        setattr(cls, "edam:data_2111",
            PermissibleValue(
                text="edam:data_2111",
                title="Codon usage table ID",
                description="Identifier of a codon usage table, for example a genetic code.",
                meaning=EDAM["data_2111"]))
        setattr(cls, "edam:data_2112",
            PermissibleValue(
                text="edam:data_2112",
                title="FlyBase primary identifier",
                description="Primary identifier of an object from the FlyBase database.",
                meaning=EDAM["data_2112"]))
        setattr(cls, "edam:data_2113",
            PermissibleValue(
                text="edam:data_2113",
                title="WormBase identifier",
                description="Identifier of an object from the WormBase database.",
                meaning=EDAM["data_2113"]))
        setattr(cls, "edam:data_2114",
            PermissibleValue(
                text="edam:data_2114",
                title="WormBase wormpep ID",
                description="Protein identifier used by WormBase database.",
                meaning=EDAM["data_2114"]))
        setattr(cls, "edam:data_2117",
            PermissibleValue(
                text="edam:data_2117",
                title="Map identifier",
                description="An identifier of a map of a molecular sequence.",
                meaning=EDAM["data_2117"]))
        setattr(cls, "edam:data_2118",
            PermissibleValue(
                text="edam:data_2118",
                title="Person identifier",
                description="""An identifier of a software end-user on a website or a database (typically a person or an entity).""",
                meaning=EDAM["data_2118"]))
        setattr(cls, "edam:data_2119",
            PermissibleValue(
                text="edam:data_2119",
                title="Nucleic acid identifier",
                description="Name or other identifier of a nucleic acid molecule.",
                meaning=EDAM["data_2119"]))
        setattr(cls, "edam:data_2127",
            PermissibleValue(
                text="edam:data_2127",
                title="Genetic code identifier",
                description="An identifier of a genetic code.",
                meaning=EDAM["data_2127"]))
        setattr(cls, "edam:data_2128",
            PermissibleValue(
                text="edam:data_2128",
                title="Genetic code name",
                description="Informal name for a genetic code, typically an organism name.",
                meaning=EDAM["data_2128"]))
        setattr(cls, "edam:data_2129",
            PermissibleValue(
                text="edam:data_2129",
                title="File format name",
                description="Name of a file format such as HTML, PNG, PDF, EMBL, GenBank and so on.",
                meaning=EDAM["data_2129"]))
        setattr(cls, "edam:data_2131",
            PermissibleValue(
                text="edam:data_2131",
                title="Operating system name",
                description="Name of a computer operating system such as Linux, PC or Mac.",
                meaning=EDAM["data_2131"]))
        setattr(cls, "edam:data_2133",
            PermissibleValue(
                text="edam:data_2133",
                title="Logical operator",
                description="A logical operator such as OR, AND, XOR, and NOT.",
                meaning=EDAM["data_2133"]))
        setattr(cls, "edam:data_2137",
            PermissibleValue(
                text="edam:data_2137",
                title="Gap penalty",
                description="A penalty for introducing or extending a gap in an alignment.",
                meaning=EDAM["data_2137"]))
        setattr(cls, "edam:data_2139",
            PermissibleValue(
                text="edam:data_2139",
                title="Nucleic acid melting temperature",
                description="""A temperature concerning nucleic acid denaturation, typically the temperature at which the two strands of a hybridised or double stranded nucleic acid (DNA or RNA/DNA) molecule separate.""",
                meaning=EDAM["data_2139"]))
        setattr(cls, "edam:data_2140",
            PermissibleValue(
                text="edam:data_2140",
                title="Concentration",
                description="The concentration of a chemical compound.",
                meaning=EDAM["data_2140"]))
        setattr(cls, "edam:data_2154",
            PermissibleValue(
                text="edam:data_2154",
                title="Sequence name",
                description="Any arbitrary name of a molecular sequence.",
                meaning=EDAM["data_2154"]))
        setattr(cls, "edam:data_2160",
            PermissibleValue(
                text="edam:data_2160",
                title="Fickett testcode plot",
                description="""A plot of Fickett testcode statistic (identifying protein coding regions) in a nucleotide sequences.""",
                meaning=EDAM["data_2160"]))
        setattr(cls, "edam:data_2161",
            PermissibleValue(
                text="edam:data_2161",
                title="Sequence similarity plot",
                description="""A plot of sequence similarities identified from word-matching or character comparison.
Use this concept for calculated substitution rates, relative site variability, data on sites with biased properties, highly conserved or very poorly conserved sites, regions, blocks etc.""",
                meaning=EDAM["data_2161"]))
        setattr(cls, "edam:data_2162",
            PermissibleValue(
                text="edam:data_2162",
                title="Helical wheel",
                description="""An image of peptide sequence sequence looking down the axis of the helix for highlighting amphipathicity and other properties.""",
                meaning=EDAM["data_2162"]))
        setattr(cls, "edam:data_2163",
            PermissibleValue(
                text="edam:data_2163",
                title="Helical net",
                description="""An image of peptide sequence sequence in a simple 3,4,3,4 repeating pattern that emulates at a simple level the arrangement of residues around an alpha helix.
Useful for highlighting amphipathicity and other properties.""",
                meaning=EDAM["data_2163"]))
        setattr(cls, "edam:data_2165",
            PermissibleValue(
                text="edam:data_2165",
                title="Protein ionisation curve",
                description="A plot of pK versus pH for a protein.",
                meaning=EDAM["data_2165"]))
        setattr(cls, "edam:data_2166",
            PermissibleValue(
                text="edam:data_2166",
                title="Sequence composition plot",
                description="A plot of character or word composition / frequency of a molecular sequence.",
                meaning=EDAM["data_2166"]))
        setattr(cls, "edam:data_2167",
            PermissibleValue(
                text="edam:data_2167",
                title="Nucleic acid density plot",
                description="Density plot (of base composition) for a nucleotide sequence.",
                meaning=EDAM["data_2167"]))
        setattr(cls, "edam:data_2168",
            PermissibleValue(
                text="edam:data_2168",
                title="Sequence trace image",
                description="""Image of a sequence trace (nucleotide sequence versus probabilities of each of the 4 bases).""",
                meaning=EDAM["data_2168"]))
        setattr(cls, "edam:data_2174",
            PermissibleValue(
                text="edam:data_2174",
                title="FlyBase secondary identifier",
                description="""Secondary identifier are used to handle entries that were merged with or split from other entries in the database.
Secondary identifier of an object from the FlyBase database.""",
                meaning=EDAM["data_2174"]))
        setattr(cls, "edam:data_2190",
            PermissibleValue(
                text="edam:data_2190",
                title="Sequence checksum",
                description="""A fixed-size datum calculated (by using a hash function) for a molecular sequence, typically for purposes of error detection or indexing.""",
                meaning=EDAM["data_2190"]))
        setattr(cls, "edam:data_2193",
            PermissibleValue(
                text="edam:data_2193",
                title="Database entry metadata",
                description="Basic information on any arbitrary database entry.",
                meaning=EDAM["data_2193"]))
        setattr(cls, "edam:data_2208",
            PermissibleValue(
                text="edam:data_2208",
                title="Plasmid identifier",
                description="An identifier of a plasmid in a database.",
                meaning=EDAM["data_2208"]))
        setattr(cls, "edam:data_2209",
            PermissibleValue(
                text="edam:data_2209",
                title="Mutation ID",
                description="A unique identifier of a specific mutation catalogued in a database.",
                meaning=EDAM["data_2209"]))
        setattr(cls, "edam:data_2216",
            PermissibleValue(
                text="edam:data_2216",
                title="Codon number",
                description="The number of a codon, for instance, at which a mutation is located.",
                meaning=EDAM["data_2216"]))
        setattr(cls, "edam:data_2219",
            PermissibleValue(
                text="edam:data_2219",
                title="Database field name",
                description="The name of a field in a database.",
                meaning=EDAM["data_2219"]))
        setattr(cls, "edam:data_2220",
            PermissibleValue(
                text="edam:data_2220",
                title="Sequence cluster ID (SYSTERS)",
                description="Unique identifier of a sequence cluster from the SYSTERS database.",
                meaning=EDAM["data_2220"]))
        setattr(cls, "edam:data_2223",
            PermissibleValue(
                text="edam:data_2223",
                title="Ontology metadata",
                description="Data concerning a biological ontology.",
                meaning=EDAM["data_2223"]))
        setattr(cls, "edam:data_2253",
            PermissibleValue(
                text="edam:data_2253",
                title="Data resource definition name",
                description="The name of a data type.",
                meaning=EDAM["data_2253"]))
        setattr(cls, "edam:data_2254",
            PermissibleValue(
                text="edam:data_2254",
                title="OBO file format name",
                description="Name of an OBO file format such as OBO-XML, plain and so on.",
                meaning=EDAM["data_2254"]))
        setattr(cls, "edam:data_2285",
            PermissibleValue(
                text="edam:data_2285",
                title="Gene ID (MIPS)",
                description="Identifier for genetic elements in MIPS database.",
                meaning=EDAM["data_2285"]))
        setattr(cls, "edam:data_2290",
            PermissibleValue(
                text="edam:data_2290",
                title="EMBL accession",
                description="An accession number of an entry from the EMBL sequence database.",
                meaning=EDAM["data_2290"]))
        setattr(cls, "edam:data_2291",
            PermissibleValue(
                text="edam:data_2291",
                title="UniProt ID",
                description="An identifier of a polypeptide in the UniProt database.",
                meaning=EDAM["data_2291"]))
        setattr(cls, "edam:data_2292",
            PermissibleValue(
                text="edam:data_2292",
                title="GenBank accession",
                description="Accession number of an entry from the GenBank sequence database.",
                meaning=EDAM["data_2292"]))
        setattr(cls, "edam:data_2293",
            PermissibleValue(
                text="edam:data_2293",
                title="Gramene secondary identifier",
                description="Secondary (internal) identifier of a Gramene database entry.",
                meaning=EDAM["data_2293"]))
        setattr(cls, "edam:data_2294",
            PermissibleValue(
                text="edam:data_2294",
                title="Sequence variation ID",
                description="An identifier of an entry from a database of molecular sequence variation.",
                meaning=EDAM["data_2294"]))
        setattr(cls, "edam:data_2295",
            PermissibleValue(
                text="edam:data_2295",
                title="Gene ID",
                description="""A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol.""",
                meaning=EDAM["data_2295"]))
        setattr(cls, "edam:data_2297",
            PermissibleValue(
                text="edam:data_2297",
                title="Gene ID (ECK)",
                description="Identifier of an E. coli K-12 gene from EcoGene Database.",
                meaning=EDAM["data_2297"]))
        setattr(cls, "edam:data_2298",
            PermissibleValue(
                text="edam:data_2298",
                title="Gene ID (HGNC)",
                description="Identifier for a gene approved by the HUGO Gene Nomenclature Committee.",
                meaning=EDAM["data_2298"]))
        setattr(cls, "edam:data_2299",
            PermissibleValue(
                text="edam:data_2299",
                title="Gene name",
                description="""The name of a gene, (typically) assigned by a person and/or according to a naming scheme. It may contain white space characters and is typically more intuitive and readable than a gene symbol. It (typically) may be used to identify similar genes in different species and to derive a gene symbol.""",
                meaning=EDAM["data_2299"]))
        setattr(cls, "edam:data_2301",
            PermissibleValue(
                text="edam:data_2301",
                title="SMILES string",
                description="A specification of a chemical structure in SMILES format.",
                meaning=EDAM["data_2301"]))
        setattr(cls, "edam:data_2302",
            PermissibleValue(
                text="edam:data_2302",
                title="STRING ID",
                description="""Unique identifier of an entry from the STRING database of protein-protein interactions.""",
                meaning=EDAM["data_2302"]))
        setattr(cls, "edam:data_2309",
            PermissibleValue(
                text="edam:data_2309",
                title="Reaction ID (SABIO-RK)",
                description="Identifier of a biological reaction from the SABIO-RK reactions database.",
                meaning=EDAM["data_2309"]))
        setattr(cls, "edam:data_2313",
            PermissibleValue(
                text="edam:data_2313",
                title="Carbohydrate report",
                description="""A human-readable collection of information about one or more specific carbohydrate 3D structure(s).""",
                meaning=EDAM["data_2313"]))
        setattr(cls, "edam:data_2314",
            PermissibleValue(
                text="edam:data_2314",
                title="GI number",
                description="""A series of digits that are assigned consecutively to each sequence record processed by NCBI. The GI number bears no resemblance to the Accession number of the sequence record.
Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record.""",
                meaning=EDAM["data_2314"]))
        setattr(cls, "edam:data_2315",
            PermissibleValue(
                text="edam:data_2315",
                title="NCBI version",
                description="""An identifier assigned to sequence records processed by NCBI, made of the accession number of the database record followed by a dot and a version number.
Nucleotide sequence version contains two letters followed by six digits, a dot, and a version number (or for older nucleotide sequence records, the format is one letter followed by five digits, a dot, and a version number). Protein sequence version contains three letters followed by five digits, a dot, and a version number.""",
                meaning=EDAM["data_2315"]))
        setattr(cls, "edam:data_2316",
            PermissibleValue(
                text="edam:data_2316",
                title="Cell line name",
                description="The name of a cell line.",
                meaning=EDAM["data_2316"]))
        setattr(cls, "edam:data_2317",
            PermissibleValue(
                text="edam:data_2317",
                title="Cell line name (exact)",
                description="The exact name of a cell line.",
                meaning=EDAM["data_2317"]))
        setattr(cls, "edam:data_2318",
            PermissibleValue(
                text="edam:data_2318",
                title="Cell line name (truncated)",
                description="The truncated name of a cell line.",
                meaning=EDAM["data_2318"]))
        setattr(cls, "edam:data_2319",
            PermissibleValue(
                text="edam:data_2319",
                title="Cell line name (no punctuation)",
                description="The name of a cell line without any punctuation.",
                meaning=EDAM["data_2319"]))
        setattr(cls, "edam:data_2320",
            PermissibleValue(
                text="edam:data_2320",
                title="Cell line name (assonant)",
                description="The assonant name of a cell line.",
                meaning=EDAM["data_2320"]))
        setattr(cls, "edam:data_2321",
            PermissibleValue(
                text="edam:data_2321",
                title="Enzyme ID",
                description="A unique, persistent identifier of an enzyme.",
                meaning=EDAM["data_2321"]))
        setattr(cls, "edam:data_2325",
            PermissibleValue(
                text="edam:data_2325",
                title="REBASE enzyme number",
                description="Identifier of an enzyme from the REBASE enzymes database.",
                meaning=EDAM["data_2325"]))
        setattr(cls, "edam:data_2326",
            PermissibleValue(
                text="edam:data_2326",
                title="DrugBank ID",
                description="Unique identifier of a drug from the DrugBank database.",
                meaning=EDAM["data_2326"]))
        setattr(cls, "edam:data_2327",
            PermissibleValue(
                text="edam:data_2327",
                title="GI number (protein)",
                description="""A unique identifier assigned to NCBI protein sequence records.
Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record.""",
                meaning=EDAM["data_2327"]))
        setattr(cls, "edam:data_2335",
            PermissibleValue(
                text="edam:data_2335",
                title="Bit score",
                description="""A score derived from the alignment of two sequences, which is then normalised with respect to the scoring system.
Bit scores are normalised with respect to the scoring system and therefore can be used to compare alignment scores from different searches.""",
                meaning=EDAM["data_2335"]))
        setattr(cls, "edam:data_2337",
            PermissibleValue(
                text="edam:data_2337",
                title="Resource metadata",
                description="""Data concerning or describing some core computational resource, as distinct from primary data. This includes metadata on the origin, source, history, ownership or location of some thing.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2337"]))
        setattr(cls, "edam:data_2338",
            PermissibleValue(
                text="edam:data_2338",
                title="Ontology identifier",
                description="Any arbitrary identifier of an ontology.",
                meaning=EDAM["data_2338"]))
        setattr(cls, "edam:data_2339",
            PermissibleValue(
                text="edam:data_2339",
                title="Ontology concept name",
                description="The name of a concept in an ontology.",
                meaning=EDAM["data_2339"]))
        setattr(cls, "edam:data_2340",
            PermissibleValue(
                text="edam:data_2340",
                title="Genome build identifier",
                description="An identifier of a build of a particular genome.",
                meaning=EDAM["data_2340"]))
        setattr(cls, "edam:data_2342",
            PermissibleValue(
                text="edam:data_2342",
                title="Pathway or network name",
                description="The name of a biological pathway or network.",
                meaning=EDAM["data_2342"]))
        setattr(cls, "edam:data_2343",
            PermissibleValue(
                text="edam:data_2343",
                title="Pathway ID (KEGG)",
                description="Identifier of a pathway from the KEGG pathway database.",
                meaning=EDAM["data_2343"]))
        setattr(cls, "edam:data_2344",
            PermissibleValue(
                text="edam:data_2344",
                title="Pathway ID (NCI-Nature)",
                description="Identifier of a pathway from the NCI-Nature pathway database.",
                meaning=EDAM["data_2344"]))
        setattr(cls, "edam:data_2345",
            PermissibleValue(
                text="edam:data_2345",
                title="Pathway ID (ConsensusPathDB)",
                description="Identifier of a pathway from the ConsensusPathDB pathway database.",
                meaning=EDAM["data_2345"]))
        setattr(cls, "edam:data_2346",
            PermissibleValue(
                text="edam:data_2346",
                title="Sequence cluster ID (UniRef)",
                description="Unique identifier of an entry from the UniRef database.",
                meaning=EDAM["data_2346"]))
        setattr(cls, "edam:data_2347",
            PermissibleValue(
                text="edam:data_2347",
                title="Sequence cluster ID (UniRef100)",
                description="Unique identifier of an entry from the UniRef100 database.",
                meaning=EDAM["data_2347"]))
        setattr(cls, "edam:data_2348",
            PermissibleValue(
                text="edam:data_2348",
                title="Sequence cluster ID (UniRef90)",
                description="Unique identifier of an entry from the UniRef90 database.",
                meaning=EDAM["data_2348"]))
        setattr(cls, "edam:data_2349",
            PermissibleValue(
                text="edam:data_2349",
                title="Sequence cluster ID (UniRef50)",
                description="Unique identifier of an entry from the UniRef50 database.",
                meaning=EDAM["data_2349"]))
        setattr(cls, "edam:data_2353",
            PermissibleValue(
                text="edam:data_2353",
                title="Ontology data",
                description="""Data concerning or derived from an ontology.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2353"]))
        setattr(cls, "edam:data_2354",
            PermissibleValue(
                text="edam:data_2354",
                title="RNA family report",
                description="""A human-readable collection of information about a specific RNA family or other group of classified RNA sequences.""",
                meaning=EDAM["data_2354"]))
        setattr(cls, "edam:data_2355",
            PermissibleValue(
                text="edam:data_2355",
                title="RNA family identifier",
                description="""Identifier of an RNA family, typically an entry from a RNA sequence classification database.""",
                meaning=EDAM["data_2355"]))
        setattr(cls, "edam:data_2356",
            PermissibleValue(
                text="edam:data_2356",
                title="RFAM accession",
                description="Stable accession number of an entry (RNA family) from the RFAM database.",
                meaning=EDAM["data_2356"]))
        setattr(cls, "edam:data_2362",
            PermissibleValue(
                text="edam:data_2362",
                title="Sequence accession (hybrid)",
                description="Accession number of a nucleotide or protein sequence database entry.",
                meaning=EDAM["data_2362"]))
        setattr(cls, "edam:data_2365",
            PermissibleValue(
                text="edam:data_2365",
                title="Pathway or network accession",
                description="""A persistent, unique identifier of a biological pathway or network (typically a database entry).""",
                meaning=EDAM["data_2365"]))
        setattr(cls, "edam:data_2366",
            PermissibleValue(
                text="edam:data_2366",
                title="Secondary structure alignment",
                description="Alignment of the (1D representations of) secondary structure of two or more molecules.",
                meaning=EDAM["data_2366"]))
        setattr(cls, "edam:data_2367",
            PermissibleValue(
                text="edam:data_2367",
                title="ASTD ID",
                description="Identifier of an object from the ASTD database.",
                meaning=EDAM["data_2367"]))
        setattr(cls, "edam:data_2368",
            PermissibleValue(
                text="edam:data_2368",
                title="ASTD ID (exon)",
                description="Identifier of an exon from the ASTD database.",
                meaning=EDAM["data_2368"]))
        setattr(cls, "edam:data_2369",
            PermissibleValue(
                text="edam:data_2369",
                title="ASTD ID (intron)",
                description="Identifier of an intron from the ASTD database.",
                meaning=EDAM["data_2369"]))
        setattr(cls, "edam:data_2370",
            PermissibleValue(
                text="edam:data_2370",
                title="ASTD ID (polya)",
                description="Identifier of a polyA signal from the ASTD database.",
                meaning=EDAM["data_2370"]))
        setattr(cls, "edam:data_2371",
            PermissibleValue(
                text="edam:data_2371",
                title="ASTD ID (tss)",
                description="Identifier of a transcription start site from the ASTD database.",
                meaning=EDAM["data_2371"]))
        setattr(cls, "edam:data_2373",
            PermissibleValue(
                text="edam:data_2373",
                title="Spot ID",
                description="Unique identifier of a spot from a two-dimensional (protein) gel.",
                meaning=EDAM["data_2373"]))
        setattr(cls, "edam:data_2374",
            PermissibleValue(
                text="edam:data_2374",
                title="Spot serial number",
                description="""Unique identifier of a spot from a two-dimensional (protein) gel in the SWISS-2DPAGE database.""",
                meaning=EDAM["data_2374"]))
        setattr(cls, "edam:data_2375",
            PermissibleValue(
                text="edam:data_2375",
                title="Spot ID (HSC-2DPAGE)",
                description="""Unique identifier of a spot from a two-dimensional (protein) gel from a HSC-2DPAGE database.""",
                meaning=EDAM["data_2375"]))
        setattr(cls, "edam:data_2379",
            PermissibleValue(
                text="edam:data_2379",
                title="Strain identifier",
                description="Identifier of a strain of an organism variant, typically a plant, virus or bacterium.",
                meaning=EDAM["data_2379"]))
        setattr(cls, "edam:data_2380",
            PermissibleValue(
                text="edam:data_2380",
                title="CABRI accession",
                description="A unique identifier of an item from the CABRI database.",
                meaning=EDAM["data_2380"]))
        setattr(cls, "edam:data_2382",
            PermissibleValue(
                text="edam:data_2382",
                title="Genotype experiment ID",
                description="Identifier of an entry from a database of genotype experiment metadata.",
                meaning=EDAM["data_2382"]))
        setattr(cls, "edam:data_2383",
            PermissibleValue(
                text="edam:data_2383",
                title="EGA accession",
                description="Identifier of an entry from the EGA database.",
                meaning=EDAM["data_2383"]))
        setattr(cls, "edam:data_2384",
            PermissibleValue(
                text="edam:data_2384",
                title="IPI protein ID",
                description="""Identifier of a protein entry catalogued in the International Protein Index (IPI) database.""",
                meaning=EDAM["data_2384"]))
        setattr(cls, "edam:data_2385",
            PermissibleValue(
                text="edam:data_2385",
                title="RefSeq accession (protein)",
                description="Accession number of a protein from the RefSeq database.",
                meaning=EDAM["data_2385"]))
        setattr(cls, "edam:data_2386",
            PermissibleValue(
                text="edam:data_2386",
                title="EPD ID",
                description="Identifier of an entry (promoter) from the EPD database.",
                meaning=EDAM["data_2386"]))
        setattr(cls, "edam:data_2387",
            PermissibleValue(
                text="edam:data_2387",
                title="TAIR accession",
                description="Identifier of an entry from the TAIR database.",
                meaning=EDAM["data_2387"]))
        setattr(cls, "edam:data_2388",
            PermissibleValue(
                text="edam:data_2388",
                title="TAIR accession (At gene)",
                description="Identifier of an Arabidopsis thaliana gene from the TAIR database.",
                meaning=EDAM["data_2388"]))
        setattr(cls, "edam:data_2389",
            PermissibleValue(
                text="edam:data_2389",
                title="UniSTS accession",
                description="Identifier of an entry from the UniSTS database.",
                meaning=EDAM["data_2389"]))
        setattr(cls, "edam:data_2390",
            PermissibleValue(
                text="edam:data_2390",
                title="UNITE accession",
                description="Identifier of an entry from the UNITE database.",
                meaning=EDAM["data_2390"]))
        setattr(cls, "edam:data_2391",
            PermissibleValue(
                text="edam:data_2391",
                title="UTR accession",
                description="Identifier of an entry from the UTR database.",
                meaning=EDAM["data_2391"]))
        setattr(cls, "edam:data_2392",
            PermissibleValue(
                text="edam:data_2392",
                title="UniParc accession",
                description="Accession number of a UniParc (protein sequence) database entry.",
                meaning=EDAM["data_2392"]))
        setattr(cls, "edam:data_2393",
            PermissibleValue(
                text="edam:data_2393",
                title="mFLJ/mKIAA number",
                description="Identifier of an entry from the Rouge or HUGE databases.",
                meaning=EDAM["data_2393"]))
        setattr(cls, "edam:data_2398",
            PermissibleValue(
                text="edam:data_2398",
                title="Ensembl protein ID",
                description="Unique identifier for a protein from the Ensembl database.",
                meaning=EDAM["data_2398"]))
        setattr(cls, "edam:data_2523",
            PermissibleValue(
                text="edam:data_2523",
                title="Phylogenetic data",
                description="""Data concerning phylogeny, typically of molecular sequences, including reports of information concerning or derived from a phylogenetic tree, or from comparing two or more phylogenetic trees.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2523"]))
        setattr(cls, "edam:data_2526",
            PermissibleValue(
                text="edam:data_2526",
                title="Text data",
                description="""Data concerning, extracted from, or derived from the analysis of a scientific text (or texts) such as a full text article from a scientific journal.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation. It includes concepts that are best described as scientific text or closely concerned with or derived from text.""",
                meaning=EDAM["data_2526"]))
        setattr(cls, "edam:data_2530",
            PermissibleValue(
                text="edam:data_2530",
                title="Organism report",
                description="A human-readable collection of information about a specific organism.",
                meaning=EDAM["data_2530"]))
        setattr(cls, "edam:data_2531",
            PermissibleValue(
                text="edam:data_2531",
                title="Protocol",
                description="""A human-readable collection of information about about how a scientific experiment or analysis was carried out that results in a specific set of data or results used for further analysis or to test a specific hypothesis.""",
                meaning=EDAM["data_2531"]))
        setattr(cls, "edam:data_2534",
            PermissibleValue(
                text="edam:data_2534",
                title="Sequence attribute",
                description="An attribute of a molecular sequence, possibly in reference to some other sequence.",
                meaning=EDAM["data_2534"]))
        setattr(cls, "edam:data_2535",
            PermissibleValue(
                text="edam:data_2535",
                title="Sequence tag profile",
                description="""Output from a serial analysis of gene expression (SAGE), massively parallel signature sequencing (MPSS) or sequencing by synthesis (SBS) experiment. In all cases this is a list of short sequence tags and the number of times it is observed.
SAGE, MPSS and SBS experiments are usually performed to study gene expression. The sequence tags are typically subsequently annotated (after a database search) with the mRNA (and therefore gene) the tag was extracted from.
This includes tag to gene assignments (tag mapping) of SAGE, MPSS and SBS data. Typically this is the sequencing-based expression profile annotated with gene identifiers.""",
                meaning=EDAM["data_2535"]))
        setattr(cls, "edam:data_2536",
            PermissibleValue(
                text="edam:data_2536",
                title="Mass spectrometry data",
                description="Data concerning a mass spectrometry measurement.",
                meaning=EDAM["data_2536"]))
        setattr(cls, "edam:data_2537",
            PermissibleValue(
                text="edam:data_2537",
                title="Protein structure raw data",
                description="""Raw data from experimental methods for determining protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.""",
                meaning=EDAM["data_2537"]))
        setattr(cls, "edam:data_2538",
            PermissibleValue(
                text="edam:data_2538",
                title="Mutation identifier",
                description="An identifier of a mutation.",
                meaning=EDAM["data_2538"]))
        setattr(cls, "edam:data_2563",
            PermissibleValue(
                text="edam:data_2563",
                title="Amino acid name (single letter)",
                description="Single letter amino acid identifier, e.g. G.",
                meaning=EDAM["data_2563"]))
        setattr(cls, "edam:data_2564",
            PermissibleValue(
                text="edam:data_2564",
                title="Amino acid name (three letter)",
                description="Three letter amino acid identifier, e.g. GLY.",
                meaning=EDAM["data_2564"]))
        setattr(cls, "edam:data_2565",
            PermissibleValue(
                text="edam:data_2565",
                title="Amino acid name (full name)",
                description="Full name of an amino acid, e.g. Glycine.",
                meaning=EDAM["data_2565"]))
        setattr(cls, "edam:data_2576",
            PermissibleValue(
                text="edam:data_2576",
                title="Toxin identifier",
                description="Identifier of a toxin.",
                meaning=EDAM["data_2576"]))
        setattr(cls, "edam:data_2578",
            PermissibleValue(
                text="edam:data_2578",
                title="ArachnoServer ID",
                description="Unique identifier of a toxin from the ArachnoServer database.",
                meaning=EDAM["data_2578"]))
        setattr(cls, "edam:data_2580",
            PermissibleValue(
                text="edam:data_2580",
                title="BindingDB Monomer ID",
                description="Unique identifier of a monomer from the BindingDB database.",
                meaning=EDAM["data_2580"]))
        setattr(cls, "edam:data_2582",
            PermissibleValue(
                text="edam:data_2582",
                title="GO concept ID (biological process)",
                description="An identifier of a 'biological process' concept from the the Gene Ontology.",
                meaning=EDAM["data_2582"]))
        setattr(cls, "edam:data_2583",
            PermissibleValue(
                text="edam:data_2583",
                title="GO concept ID (molecular function)",
                description="An identifier of a 'molecular function' concept from the the Gene Ontology.",
                meaning=EDAM["data_2583"]))
        setattr(cls, "edam:data_2586",
            PermissibleValue(
                text="edam:data_2586",
                title="Northern blot image",
                description="An image arising from a Northern Blot experiment.",
                meaning=EDAM["data_2586"]))
        setattr(cls, "edam:data_2587",
            PermissibleValue(
                text="edam:data_2587",
                title="Blot ID",
                description="Unique identifier of a blot from a Northern Blot.",
                meaning=EDAM["data_2587"]))
        setattr(cls, "edam:data_2588",
            PermissibleValue(
                text="edam:data_2588",
                title="BlotBase blot ID",
                description="Unique identifier of a blot from a Northern Blot from the BlotBase database.",
                meaning=EDAM["data_2588"]))
        setattr(cls, "edam:data_2589",
            PermissibleValue(
                text="edam:data_2589",
                title="Hierarchy",
                description="""Raw data on a biological hierarchy, describing the hierarchy proper, hierarchy components and possibly associated annotation.""",
                meaning=EDAM["data_2589"]))
        setattr(cls, "edam:data_2591",
            PermissibleValue(
                text="edam:data_2591",
                title="Brite hierarchy ID",
                description="Identifier of an entry from the Brite database of biological hierarchies.",
                meaning=EDAM["data_2591"]))
        setattr(cls, "edam:data_2593",
            PermissibleValue(
                text="edam:data_2593",
                title="BRENDA organism ID",
                description="A unique identifier for an organism used in the BRENDA database.",
                meaning=EDAM["data_2593"]))
        setattr(cls, "edam:data_2594",
            PermissibleValue(
                text="edam:data_2594",
                title="UniGene taxon",
                description="The name of a taxon using the controlled vocabulary of the UniGene database.",
                meaning=EDAM["data_2594"]))
        setattr(cls, "edam:data_2595",
            PermissibleValue(
                text="edam:data_2595",
                title="UTRdb taxon",
                description="The name of a taxon using the controlled vocabulary of the UTRdb database.",
                meaning=EDAM["data_2595"]))
        setattr(cls, "edam:data_2596",
            PermissibleValue(
                text="edam:data_2596",
                title="Catalogue ID",
                description="An identifier of a catalogue of biological resources.",
                meaning=EDAM["data_2596"]))
        setattr(cls, "edam:data_2597",
            PermissibleValue(
                text="edam:data_2597",
                title="CABRI catalogue name",
                description="The name of a catalogue of biological resources from the CABRI database.",
                meaning=EDAM["data_2597"]))
        setattr(cls, "edam:data_2600",
            PermissibleValue(
                text="edam:data_2600",
                title="Pathway or network",
                description="""Primary data about a specific biological pathway or network (the nodes and connections within the pathway or network).""",
                meaning=EDAM["data_2600"]))
        setattr(cls, "edam:data_2603",
            PermissibleValue(
                text="edam:data_2603",
                title="Expression data",
                description="""Image, hybridisation or some other data arising from a study of feature/molecule expression, typically profiling or quantification.""",
                meaning=EDAM["data_2603"]))
        setattr(cls, "edam:data_2605",
            PermissibleValue(
                text="edam:data_2605",
                title="Compound ID (KEGG)",
                description="Unique identifier of a chemical compound from the KEGG database.",
                meaning=EDAM["data_2605"]))
        setattr(cls, "edam:data_2606",
            PermissibleValue(
                text="edam:data_2606",
                title="RFAM name",
                description="Name (not necessarily stable) an entry (RNA family) from the RFAM database.",
                meaning=EDAM["data_2606"]))
        setattr(cls, "edam:data_2608",
            PermissibleValue(
                text="edam:data_2608",
                title="Reaction ID (KEGG)",
                description="Identifier of a biological reaction from the KEGG reactions database.",
                meaning=EDAM["data_2608"]))
        setattr(cls, "edam:data_2609",
            PermissibleValue(
                text="edam:data_2609",
                title="Drug ID (KEGG)",
                description="Unique identifier of a drug from the KEGG Drug database.",
                meaning=EDAM["data_2609"]))
        setattr(cls, "edam:data_2610",
            PermissibleValue(
                text="edam:data_2610",
                title="Ensembl ID",
                description="Identifier of an entry (exon, gene, transcript or protein) from the Ensembl database.",
                meaning=EDAM["data_2610"]))
        setattr(cls, "edam:data_2611",
            PermissibleValue(
                text="edam:data_2611",
                title="ICD identifier",
                description="""An identifier of a disease from the International Classification of Diseases (ICD) database.""",
                meaning=EDAM["data_2611"]))
        setattr(cls, "edam:data_2612",
            PermissibleValue(
                text="edam:data_2612",
                title="Sequence cluster ID (CluSTr)",
                description="Unique identifier of a sequence cluster from the CluSTr database.",
                meaning=EDAM["data_2612"]))
        setattr(cls, "edam:data_2613",
            PermissibleValue(
                text="edam:data_2613",
                title="KEGG Glycan ID",
                description="""Unique identifier of a glycan ligand from the KEGG GLYCAN database (a subset of KEGG LIGAND).""",
                meaning=EDAM["data_2613"]))
        setattr(cls, "edam:data_2614",
            PermissibleValue(
                text="edam:data_2614",
                title="TCDB ID",
                description="""A unique identifier of a family from the transport classification database (TCDB) of membrane transport proteins.
OBO file for regular expression.""",
                meaning=EDAM["data_2614"]))
        setattr(cls, "edam:data_2615",
            PermissibleValue(
                text="edam:data_2615",
                title="MINT ID",
                description="Unique identifier of an entry from the MINT database of protein-protein interactions.",
                meaning=EDAM["data_2615"]))
        setattr(cls, "edam:data_2616",
            PermissibleValue(
                text="edam:data_2616",
                title="DIP ID",
                description="Unique identifier of an entry from the DIP database of protein-protein interactions.",
                meaning=EDAM["data_2616"]))
        setattr(cls, "edam:data_2617",
            PermissibleValue(
                text="edam:data_2617",
                title="Signaling Gateway protein ID",
                description="""Unique identifier of a protein listed in the UCSD-Nature Signaling Gateway Molecule Pages database.""",
                meaning=EDAM["data_2617"]))
        setattr(cls, "edam:data_2618",
            PermissibleValue(
                text="edam:data_2618",
                title="Protein modification ID",
                description="Identifier of a protein modification catalogued in a database.",
                meaning=EDAM["data_2618"]))
        setattr(cls, "edam:data_2619",
            PermissibleValue(
                text="edam:data_2619",
                title="RESID ID",
                description="Identifier of a protein modification catalogued in the RESID database.",
                meaning=EDAM["data_2619"]))
        setattr(cls, "edam:data_2620",
            PermissibleValue(
                text="edam:data_2620",
                title="RGD ID",
                description="Identifier of an entry from the RGD database.",
                meaning=EDAM["data_2620"]))
        setattr(cls, "edam:data_2621",
            PermissibleValue(
                text="edam:data_2621",
                title="TAIR accession (protein)",
                description="Identifier of a protein sequence from the TAIR database.",
                meaning=EDAM["data_2621"]))
        setattr(cls, "edam:data_2622",
            PermissibleValue(
                text="edam:data_2622",
                title="Compound ID (HMDB)",
                description="Identifier of a small molecule metabolite from the Human Metabolome Database (HMDB).",
                meaning=EDAM["data_2622"]))
        setattr(cls, "edam:data_2625",
            PermissibleValue(
                text="edam:data_2625",
                title="LIPID MAPS ID",
                description="Identifier of an entry from the LIPID MAPS database.",
                meaning=EDAM["data_2625"]))
        setattr(cls, "edam:data_2626",
            PermissibleValue(
                text="edam:data_2626",
                title="PeptideAtlas ID",
                description="Identifier of a peptide from the PeptideAtlas peptide databases.",
                meaning=EDAM["data_2626"]))
        setattr(cls, "edam:data_2628",
            PermissibleValue(
                text="edam:data_2628",
                title="BioGRID interaction ID",
                description="A unique identifier of an interaction from the BioGRID database.",
                meaning=EDAM["data_2628"]))
        setattr(cls, "edam:data_2629",
            PermissibleValue(
                text="edam:data_2629",
                title="Enzyme ID (MEROPS)",
                description="Unique identifier of a peptidase enzyme from the MEROPS database.",
                meaning=EDAM["data_2629"]))
        setattr(cls, "edam:data_2630",
            PermissibleValue(
                text="edam:data_2630",
                title="Mobile genetic element ID",
                description="An identifier of a mobile genetic element.",
                meaning=EDAM["data_2630"]))
        setattr(cls, "edam:data_2631",
            PermissibleValue(
                text="edam:data_2631",
                title="ACLAME ID",
                description="An identifier of a mobile genetic element from the Aclame database.",
                meaning=EDAM["data_2631"]))
        setattr(cls, "edam:data_2632",
            PermissibleValue(
                text="edam:data_2632",
                title="SGD ID",
                description="Identifier of an entry from the Saccharomyces genome database (SGD).",
                meaning=EDAM["data_2632"]))
        setattr(cls, "edam:data_2633",
            PermissibleValue(
                text="edam:data_2633",
                title="Book ID",
                description="Unique identifier of a book.",
                meaning=EDAM["data_2633"]))
        setattr(cls, "edam:data_2634",
            PermissibleValue(
                text="edam:data_2634",
                title="ISBN",
                description="The International Standard Book Number (ISBN) is for identifying printed books.",
                meaning=EDAM["data_2634"]))
        setattr(cls, "edam:data_2635",
            PermissibleValue(
                text="edam:data_2635",
                title="Compound ID (3DMET)",
                description="Identifier of a metabolite from the 3DMET database.",
                meaning=EDAM["data_2635"]))
        setattr(cls, "edam:data_2636",
            PermissibleValue(
                text="edam:data_2636",
                title="MatrixDB interaction ID",
                description="A unique identifier of an interaction from the MatrixDB database.",
                meaning=EDAM["data_2636"]))
        setattr(cls, "edam:data_2637",
            PermissibleValue(
                text="edam:data_2637",
                title="cPath ID",
                description="""A unique identifier for pathways, reactions, complexes and small molecules from the cPath (Pathway Commons) database.
These identifiers are unique within the cPath database, however, they are not stable between releases.""",
                meaning=EDAM["data_2637"]))
        setattr(cls, "edam:data_2638",
            PermissibleValue(
                text="edam:data_2638",
                title="PubChem bioassay ID",
                description="Identifier of an assay from the PubChem database.",
                meaning=EDAM["data_2638"]))
        setattr(cls, "edam:data_2639",
            PermissibleValue(
                text="edam:data_2639",
                title="PubChem ID",
                description="Identifier of an entry from the PubChem database.",
                meaning=EDAM["data_2639"]))
        setattr(cls, "edam:data_2641",
            PermissibleValue(
                text="edam:data_2641",
                title="Reaction ID (MACie)",
                description="Identifier of an enzyme reaction mechanism from the MACie database.",
                meaning=EDAM["data_2641"]))
        setattr(cls, "edam:data_2642",
            PermissibleValue(
                text="edam:data_2642",
                title="Gene ID (miRBase)",
                description="Identifier for a gene from the miRBase database.",
                meaning=EDAM["data_2642"]))
        setattr(cls, "edam:data_2643",
            PermissibleValue(
                text="edam:data_2643",
                title="Gene ID (ZFIN)",
                description="Identifier for a gene from the Zebrafish information network genome (ZFIN) database.",
                meaning=EDAM["data_2643"]))
        setattr(cls, "edam:data_2644",
            PermissibleValue(
                text="edam:data_2644",
                title="Reaction ID (Rhea)",
                description="Identifier of an enzyme-catalysed reaction from the Rhea database.",
                meaning=EDAM["data_2644"]))
        setattr(cls, "edam:data_2645",
            PermissibleValue(
                text="edam:data_2645",
                title="Pathway ID (Unipathway)",
                description="Identifier of a biological pathway from the Unipathway database.",
                meaning=EDAM["data_2645"]))
        setattr(cls, "edam:data_2646",
            PermissibleValue(
                text="edam:data_2646",
                title="Compound ID (ChEMBL)",
                description="Identifier of a small molecular from the ChEMBL database.",
                meaning=EDAM["data_2646"]))
        setattr(cls, "edam:data_2647",
            PermissibleValue(
                text="edam:data_2647",
                title="LGICdb identifier",
                description="Unique identifier of an entry from the Ligand-gated ion channel (LGICdb) database.",
                meaning=EDAM["data_2647"]))
        setattr(cls, "edam:data_2648",
            PermissibleValue(
                text="edam:data_2648",
                title="Reaction kinetics ID (SABIO-RK)",
                description="""Identifier of a biological reaction (kinetics entry) from the SABIO-RK reactions database.""",
                meaning=EDAM["data_2648"]))
        setattr(cls, "edam:data_2649",
            PermissibleValue(
                text="edam:data_2649",
                title="PharmGKB ID",
                description="""Identifier of an entry from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).""",
                meaning=EDAM["data_2649"]))
        setattr(cls, "edam:data_2650",
            PermissibleValue(
                text="edam:data_2650",
                title="Pathway ID (PharmGKB)",
                description="""Identifier of a pathway from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).""",
                meaning=EDAM["data_2650"]))
        setattr(cls, "edam:data_2651",
            PermissibleValue(
                text="edam:data_2651",
                title="Disease ID (PharmGKB)",
                description="""Identifier of a disease from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).""",
                meaning=EDAM["data_2651"]))
        setattr(cls, "edam:data_2652",
            PermissibleValue(
                text="edam:data_2652",
                title="Drug ID (PharmGKB)",
                description="""Identifier of a drug from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).""",
                meaning=EDAM["data_2652"]))
        setattr(cls, "edam:data_2653",
            PermissibleValue(
                text="edam:data_2653",
                title="Drug ID (TTD)",
                description="Identifier of a drug from the Therapeutic Target Database (TTD).",
                meaning=EDAM["data_2653"]))
        setattr(cls, "edam:data_2654",
            PermissibleValue(
                text="edam:data_2654",
                title="Target ID (TTD)",
                description="Identifier of a target protein from the Therapeutic Target Database (TTD).",
                meaning=EDAM["data_2654"]))
        setattr(cls, "edam:data_2655",
            PermissibleValue(
                text="edam:data_2655",
                title="Cell type identifier",
                description="A unique identifier of a type or group of cells.",
                meaning=EDAM["data_2655"]))
        setattr(cls, "edam:data_2656",
            PermissibleValue(
                text="edam:data_2656",
                title="NeuronDB ID",
                description="A unique identifier of a neuron from the NeuronDB database.",
                meaning=EDAM["data_2656"]))
        setattr(cls, "edam:data_2657",
            PermissibleValue(
                text="edam:data_2657",
                title="NeuroMorpho ID",
                description="A unique identifier of a neuron from the NeuroMorpho database.",
                meaning=EDAM["data_2657"]))
        setattr(cls, "edam:data_2658",
            PermissibleValue(
                text="edam:data_2658",
                title="Compound ID (ChemIDplus)",
                description="Identifier of a chemical from the ChemIDplus database.",
                meaning=EDAM["data_2658"]))
        setattr(cls, "edam:data_2659",
            PermissibleValue(
                text="edam:data_2659",
                title="Pathway ID (SMPDB)",
                description="Identifier of a pathway from the Small Molecule Pathway Database (SMPDB).",
                meaning=EDAM["data_2659"]))
        setattr(cls, "edam:data_2660",
            PermissibleValue(
                text="edam:data_2660",
                title="BioNumbers ID",
                description="""Identifier of an entry from the BioNumbers database of key numbers and associated data in molecular biology.""",
                meaning=EDAM["data_2660"]))
        setattr(cls, "edam:data_2662",
            PermissibleValue(
                text="edam:data_2662",
                title="T3DB ID",
                description="Unique identifier of a toxin from the Toxin and Toxin Target Database (T3DB) database.",
                meaning=EDAM["data_2662"]))
        setattr(cls, "edam:data_2663",
            PermissibleValue(
                text="edam:data_2663",
                title="Carbohydrate identifier",
                description="Identifier of a carbohydrate.",
                meaning=EDAM["data_2663"]))
        setattr(cls, "edam:data_2664",
            PermissibleValue(
                text="edam:data_2664",
                title="GlycomeDB ID",
                description="Identifier of an entry from the GlycomeDB database.",
                meaning=EDAM["data_2664"]))
        setattr(cls, "edam:data_2665",
            PermissibleValue(
                text="edam:data_2665",
                title="LipidBank ID",
                description="Identifier of an entry from the LipidBank database.",
                meaning=EDAM["data_2665"]))
        setattr(cls, "edam:data_2666",
            PermissibleValue(
                text="edam:data_2666",
                title="CDD ID",
                description="Identifier of a conserved domain from the Conserved Domain Database.",
                meaning=EDAM["data_2666"]))
        setattr(cls, "edam:data_2667",
            PermissibleValue(
                text="edam:data_2667",
                title="MMDB ID",
                description="An identifier of an entry from the MMDB database.",
                meaning=EDAM["data_2667"]))
        setattr(cls, "edam:data_2668",
            PermissibleValue(
                text="edam:data_2668",
                title="iRefIndex ID",
                description="""Unique identifier of an entry from the iRefIndex database of protein-protein interactions.""",
                meaning=EDAM["data_2668"]))
        setattr(cls, "edam:data_2669",
            PermissibleValue(
                text="edam:data_2669",
                title="ModelDB ID",
                description="Unique identifier of an entry from the ModelDB database.",
                meaning=EDAM["data_2669"]))
        setattr(cls, "edam:data_2670",
            PermissibleValue(
                text="edam:data_2670",
                title="Pathway ID (DQCS)",
                description="""Identifier of a signaling pathway from the Database of Quantitative Cellular Signaling (DQCS).""",
                meaning=EDAM["data_2670"]))
        setattr(cls, "edam:data_2700",
            PermissibleValue(
                text="edam:data_2700",
                title="CATH identifier",
                description="Identifier of a protein domain (or other node) from the CATH database.",
                meaning=EDAM["data_2700"]))
        setattr(cls, "edam:data_2701",
            PermissibleValue(
                text="edam:data_2701",
                title="CATH node ID (family)",
                description="A code number identifying a family from the CATH database.",
                meaning=EDAM["data_2701"]))
        setattr(cls, "edam:data_2702",
            PermissibleValue(
                text="edam:data_2702",
                title="Enzyme ID (CAZy)",
                description="Identifier of an enzyme from the CAZy enzymes database.",
                meaning=EDAM["data_2702"]))
        setattr(cls, "edam:data_2704",
            PermissibleValue(
                text="edam:data_2704",
                title="Clone ID (IMAGE)",
                description="""A unique identifier assigned by the I.M.A.G.E. consortium to a clone (cloned molecular sequence).""",
                meaning=EDAM["data_2704"]))
        setattr(cls, "edam:data_2705",
            PermissibleValue(
                text="edam:data_2705",
                title="GO concept ID (cellular component)",
                description="An identifier of a 'cellular component' concept from the Gene Ontology.",
                meaning=EDAM["data_2705"]))
        setattr(cls, "edam:data_2706",
            PermissibleValue(
                text="edam:data_2706",
                title="Chromosome name (BioCyc)",
                description="Name of a chromosome as used in the BioCyc database.",
                meaning=EDAM["data_2706"]))
        setattr(cls, "edam:data_2709",
            PermissibleValue(
                text="edam:data_2709",
                title="CleanEx entry name",
                description="An identifier of a gene expression profile from the CleanEx database.",
                meaning=EDAM["data_2709"]))
        setattr(cls, "edam:data_2710",
            PermissibleValue(
                text="edam:data_2710",
                title="CleanEx dataset code",
                description="""An identifier of (typically a list of) gene expression experiments catalogued in the CleanEx database.""",
                meaning=EDAM["data_2710"]))
        setattr(cls, "edam:data_2711",
            PermissibleValue(
                text="edam:data_2711",
                title="Genome report",
                description="A human-readable collection of information concerning a genome as a whole.",
                meaning=EDAM["data_2711"]))
        setattr(cls, "edam:data_2713",
            PermissibleValue(
                text="edam:data_2713",
                title="Protein ID (CORUM)",
                description="Unique identifier for a protein complex from the CORUM database.",
                meaning=EDAM["data_2713"]))
        setattr(cls, "edam:data_2714",
            PermissibleValue(
                text="edam:data_2714",
                title="CDD PSSM-ID",
                description="Unique identifier of a position-specific scoring matrix from the CDD database.",
                meaning=EDAM["data_2714"]))
        setattr(cls, "edam:data_2715",
            PermissibleValue(
                text="edam:data_2715",
                title="Protein ID (CuticleDB)",
                description="Unique identifier for a protein from the CuticleDB database.",
                meaning=EDAM["data_2715"]))
        setattr(cls, "edam:data_2716",
            PermissibleValue(
                text="edam:data_2716",
                title="DBD ID",
                description="Identifier of a predicted transcription factor from the DBD database.",
                meaning=EDAM["data_2716"]))
        setattr(cls, "edam:data_2717",
            PermissibleValue(
                text="edam:data_2717",
                title="Oligonucleotide probe annotation",
                description="General annotation on an oligonucleotide probe, or a set of probes.",
                meaning=EDAM["data_2717"]))
        setattr(cls, "edam:data_2718",
            PermissibleValue(
                text="edam:data_2718",
                title="Oligonucleotide ID",
                description="Identifier of an oligonucleotide from a database.",
                meaning=EDAM["data_2718"]))
        setattr(cls, "edam:data_2719",
            PermissibleValue(
                text="edam:data_2719",
                title="dbProbe ID",
                description="Identifier of an oligonucleotide probe from the dbProbe database.",
                meaning=EDAM["data_2719"]))
        setattr(cls, "edam:data_2720",
            PermissibleValue(
                text="edam:data_2720",
                title="Dinucleotide property",
                description="Physicochemical property data for one or more dinucleotides.",
                meaning=EDAM["data_2720"]))
        setattr(cls, "edam:data_2721",
            PermissibleValue(
                text="edam:data_2721",
                title="DiProDB ID",
                description="Identifier of an dinucleotide property from the DiProDB database.",
                meaning=EDAM["data_2721"]))
        setattr(cls, "edam:data_2723",
            PermissibleValue(
                text="edam:data_2723",
                title="Protein ID (DisProt)",
                description="Unique identifier for a protein from the DisProt database.",
                meaning=EDAM["data_2723"]))
        setattr(cls, "edam:data_2725",
            PermissibleValue(
                text="edam:data_2725",
                title="Ensembl transcript ID",
                description="Unique identifier for a gene transcript from the Ensembl database.",
                meaning=EDAM["data_2725"]))
        setattr(cls, "edam:data_2727",
            PermissibleValue(
                text="edam:data_2727",
                title="Promoter ID",
                description="An identifier of a promoter of a gene that is catalogued in a database.",
                meaning=EDAM["data_2727"]))
        setattr(cls, "edam:data_2728",
            PermissibleValue(
                text="edam:data_2728",
                title="EST accession",
                description="Identifier of an EST sequence.",
                meaning=EDAM["data_2728"]))
        setattr(cls, "edam:data_2729",
            PermissibleValue(
                text="edam:data_2729",
                title="COGEME EST ID",
                description="Identifier of an EST sequence from the COGEME database.",
                meaning=EDAM["data_2729"]))
        setattr(cls, "edam:data_2730",
            PermissibleValue(
                text="edam:data_2730",
                title="COGEME unisequence ID",
                description="""A unisequence is a single sequence assembled from ESTs.
Identifier of a unisequence from the COGEME database.""",
                meaning=EDAM["data_2730"]))
        setattr(cls, "edam:data_2731",
            PermissibleValue(
                text="edam:data_2731",
                title="Protein family ID (GeneFarm)",
                description="Accession number of an entry (protein family) from the GeneFarm database.",
                meaning=EDAM["data_2731"]))
        setattr(cls, "edam:data_2732",
            PermissibleValue(
                text="edam:data_2732",
                title="Family name",
                description="The name of a family of organism.",
                meaning=EDAM["data_2732"]))
        setattr(cls, "edam:data_2736",
            PermissibleValue(
                text="edam:data_2736",
                title="Sequence feature ID (SwissRegulon)",
                description="""A feature identifier as used in the SwissRegulon database.
This can be name of a gene, the ID of a TFBS, or genomic coordinates in form \"chr:start..end\".""",
                meaning=EDAM["data_2736"]))
        setattr(cls, "edam:data_2737",
            PermissibleValue(
                text="edam:data_2737",
                title="FIG ID",
                description="""A FIG ID consists of four parts: a prefix, genome id, locus type and id number.
A unique identifier of gene in the NMPDR database.""",
                meaning=EDAM["data_2737"]))
        setattr(cls, "edam:data_2738",
            PermissibleValue(
                text="edam:data_2738",
                title="Gene ID (Xenbase)",
                description="A unique identifier of gene in the Xenbase database.",
                meaning=EDAM["data_2738"]))
        setattr(cls, "edam:data_2739",
            PermissibleValue(
                text="edam:data_2739",
                title="Gene ID (Genolist)",
                description="A unique identifier of gene in the Genolist database.",
                meaning=EDAM["data_2739"]))
        setattr(cls, "edam:data_2741",
            PermissibleValue(
                text="edam:data_2741",
                title="ABS ID",
                description="Identifier of an entry (promoter) from the ABS database.",
                meaning=EDAM["data_2741"]))
        setattr(cls, "edam:data_2742",
            PermissibleValue(
                text="edam:data_2742",
                title="AraC-XylS ID",
                description="Identifier of a transcription factor from the AraC-XylS database.",
                meaning=EDAM["data_2742"]))
        setattr(cls, "edam:data_2744",
            PermissibleValue(
                text="edam:data_2744",
                title="Locus ID (PseudoCAP)",
                description="Identifier of a locus from the PseudoCAP database.",
                meaning=EDAM["data_2744"]))
        setattr(cls, "edam:data_2745",
            PermissibleValue(
                text="edam:data_2745",
                title="Locus ID (UTR)",
                description="Identifier of a locus from the UTR database.",
                meaning=EDAM["data_2745"]))
        setattr(cls, "edam:data_2746",
            PermissibleValue(
                text="edam:data_2746",
                title="MonosaccharideDB ID",
                description="Unique identifier of a monosaccharide from the MonosaccharideDB database.",
                meaning=EDAM["data_2746"]))
        setattr(cls, "edam:data_2749",
            PermissibleValue(
                text="edam:data_2749",
                title="Genome identifier",
                description="An identifier of a particular genome.",
                meaning=EDAM["data_2749"]))
        setattr(cls, "edam:data_2752",
            PermissibleValue(
                text="edam:data_2752",
                title="GlycoMap ID",
                description="Identifier of an entry from the GlycoMapsDB (Glycosciences.de) database.",
                meaning=EDAM["data_2752"]))
        setattr(cls, "edam:data_2753",
            PermissibleValue(
                text="edam:data_2753",
                title="Carbohydrate conformational map",
                description="A conformational energy map of the glycosidic linkages in a carbohydrate molecule.",
                meaning=EDAM["data_2753"]))
        setattr(cls, "edam:data_2755",
            PermissibleValue(
                text="edam:data_2755",
                title="Transcription factor name",
                description="The name of a transcription factor.",
                meaning=EDAM["data_2755"]))
        setattr(cls, "edam:data_2756",
            PermissibleValue(
                text="edam:data_2756",
                title="TCID",
                description="""Identifier of a membrane transport proteins from the transport classification database (TCDB).""",
                meaning=EDAM["data_2756"]))
        setattr(cls, "edam:data_2757",
            PermissibleValue(
                text="edam:data_2757",
                title="Pfam domain name",
                description="Name of a domain from the Pfam database.",
                meaning=EDAM["data_2757"]))
        setattr(cls, "edam:data_2758",
            PermissibleValue(
                text="edam:data_2758",
                title="Pfam clan ID",
                description="Accession number of a Pfam clan.",
                meaning=EDAM["data_2758"]))
        setattr(cls, "edam:data_2759",
            PermissibleValue(
                text="edam:data_2759",
                title="Gene ID (VectorBase)",
                description="Identifier for a gene from the VectorBase database.",
                meaning=EDAM["data_2759"]))
        setattr(cls, "edam:data_2761",
            PermissibleValue(
                text="edam:data_2761",
                title="UTRSite ID",
                description="""Identifier of an entry from the UTRSite database of regulatory motifs in eukaryotic UTRs.""",
                meaning=EDAM["data_2761"]))
        setattr(cls, "edam:data_2762",
            PermissibleValue(
                text="edam:data_2762",
                title="Sequence signature report",
                description="""An informative report about a specific or conserved pattern in a molecular sequence, such as its context in genes or proteins, its role, origin or method of construction, etc.""",
                meaning=EDAM["data_2762"]))
        setattr(cls, "edam:data_2764",
            PermissibleValue(
                text="edam:data_2764",
                title="Protein name (UniProt)",
                description="Official name of a protein as used in the UniProt database.",
                meaning=EDAM["data_2764"]))
        setattr(cls, "edam:data_2766",
            PermissibleValue(
                text="edam:data_2766",
                title="HAMAP ID",
                description="Name of a protein family from the HAMAP database.",
                meaning=EDAM["data_2766"]))
        setattr(cls, "edam:data_2769",
            PermissibleValue(
                text="edam:data_2769",
                title="Transcript ID",
                description="Identifier of a RNA transcript.",
                meaning=EDAM["data_2769"]))
        setattr(cls, "edam:data_2770",
            PermissibleValue(
                text="edam:data_2770",
                title="HIT ID",
                description="Identifier of an RNA transcript from the H-InvDB database.",
                meaning=EDAM["data_2770"]))
        setattr(cls, "edam:data_2771",
            PermissibleValue(
                text="edam:data_2771",
                title="HIX ID",
                description="A unique identifier of gene cluster in the H-InvDB database.",
                meaning=EDAM["data_2771"]))
        setattr(cls, "edam:data_2772",
            PermissibleValue(
                text="edam:data_2772",
                title="HPA antibody id",
                description="Identifier of a antibody from the HPA database.",
                meaning=EDAM["data_2772"]))
        setattr(cls, "edam:data_2773",
            PermissibleValue(
                text="edam:data_2773",
                title="IMGT/HLA ID",
                description="""Identifier of a human major histocompatibility complex (HLA) or other protein from the IMGT/HLA database.""",
                meaning=EDAM["data_2773"]))
        setattr(cls, "edam:data_2774",
            PermissibleValue(
                text="edam:data_2774",
                title="Gene ID (JCVI)",
                description="A unique identifier of gene assigned by the J. Craig Venter Institute (JCVI).",
                meaning=EDAM["data_2774"]))
        setattr(cls, "edam:data_2775",
            PermissibleValue(
                text="edam:data_2775",
                title="Kinase name",
                description="The name of a kinase protein.",
                meaning=EDAM["data_2775"]))
        setattr(cls, "edam:data_2776",
            PermissibleValue(
                text="edam:data_2776",
                title="ConsensusPathDB entity ID",
                description="Identifier of a physical entity from the ConsensusPathDB database.",
                meaning=EDAM["data_2776"]))
        setattr(cls, "edam:data_2777",
            PermissibleValue(
                text="edam:data_2777",
                title="ConsensusPathDB entity name",
                description="Name of a physical entity from the ConsensusPathDB database.",
                meaning=EDAM["data_2777"]))
        setattr(cls, "edam:data_2778",
            PermissibleValue(
                text="edam:data_2778",
                title="CCAP strain number",
                description="The number of a strain of algae and protozoa from the CCAP database.",
                meaning=EDAM["data_2778"]))
        setattr(cls, "edam:data_2779",
            PermissibleValue(
                text="edam:data_2779",
                title="Stock number",
                description="An identifier of stock from a catalogue of biological resources.",
                meaning=EDAM["data_2779"]))
        setattr(cls, "edam:data_2780",
            PermissibleValue(
                text="edam:data_2780",
                title="Stock number (TAIR)",
                description="A stock number from The Arabidopsis information resource (TAIR).",
                meaning=EDAM["data_2780"]))
        setattr(cls, "edam:data_2781",
            PermissibleValue(
                text="edam:data_2781",
                title="REDIdb ID",
                description="Identifier of an entry from the RNA editing database (REDIdb).",
                meaning=EDAM["data_2781"]))
        setattr(cls, "edam:data_2782",
            PermissibleValue(
                text="edam:data_2782",
                title="SMART domain name",
                description="Name of a domain from the SMART database.",
                meaning=EDAM["data_2782"]))
        setattr(cls, "edam:data_2783",
            PermissibleValue(
                text="edam:data_2783",
                title="Protein family ID (PANTHER)",
                description="Accession number of an entry (family) from the PANTHER database.",
                meaning=EDAM["data_2783"]))
        setattr(cls, "edam:data_2784",
            PermissibleValue(
                text="edam:data_2784",
                title="RNAVirusDB ID",
                description="""A unique identifier for a virus from the RNAVirusDB database.
Could list (or reference) other taxa here from https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary.""",
                meaning=EDAM["data_2784"]))
        setattr(cls, "edam:data_2785",
            PermissibleValue(
                text="edam:data_2785",
                title="Virus identifier",
                description="An accession of annotation on a (group of) viruses (catalogued in a database).",
                meaning=EDAM["data_2785"]))
        setattr(cls, "edam:data_2786",
            PermissibleValue(
                text="edam:data_2786",
                title="NCBI Genome Project ID",
                description="An identifier of a genome project assigned by NCBI.",
                meaning=EDAM["data_2786"]))
        setattr(cls, "edam:data_2787",
            PermissibleValue(
                text="edam:data_2787",
                title="NCBI genome accession",
                description="A unique identifier of a whole genome assigned by the NCBI.",
                meaning=EDAM["data_2787"]))
        setattr(cls, "edam:data_2789",
            PermissibleValue(
                text="edam:data_2789",
                title="Protein ID (TopDB)",
                description="Unique identifier for a membrane protein from the TopDB database.",
                meaning=EDAM["data_2789"]))
        setattr(cls, "edam:data_2790",
            PermissibleValue(
                text="edam:data_2790",
                title="Gel ID",
                description="Identifier of a two-dimensional (protein) gel.",
                meaning=EDAM["data_2790"]))
        setattr(cls, "edam:data_2791",
            PermissibleValue(
                text="edam:data_2791",
                title="Reference map name (SWISS-2DPAGE)",
                description="Name of a reference map gel from the SWISS-2DPAGE database.",
                meaning=EDAM["data_2791"]))
        setattr(cls, "edam:data_2792",
            PermissibleValue(
                text="edam:data_2792",
                title="Protein ID (PeroxiBase)",
                description="Unique identifier for a peroxidase protein from the PeroxiBase database.",
                meaning=EDAM["data_2792"]))
        setattr(cls, "edam:data_2793",
            PermissibleValue(
                text="edam:data_2793",
                title="SISYPHUS ID",
                description="Identifier of an entry from the SISYPHUS database of tertiary structure alignments.",
                meaning=EDAM["data_2793"]))
        setattr(cls, "edam:data_2794",
            PermissibleValue(
                text="edam:data_2794",
                title="ORF ID",
                description="Accession of an open reading frame (catalogued in a database).",
                meaning=EDAM["data_2794"]))
        setattr(cls, "edam:data_2795",
            PermissibleValue(
                text="edam:data_2795",
                title="ORF identifier",
                description="An identifier of an open reading frame.",
                meaning=EDAM["data_2795"]))
        setattr(cls, "edam:data_2796",
            PermissibleValue(
                text="edam:data_2796",
                title="LINUCS ID",
                description="Identifier of an entry from the GlycosciencesDB database.",
                meaning=EDAM["data_2796"]))
        setattr(cls, "edam:data_2797",
            PermissibleValue(
                text="edam:data_2797",
                title="Protein ID (LGICdb)",
                description="Unique identifier for a ligand-gated ion channel protein from the LGICdb database.",
                meaning=EDAM["data_2797"]))
        setattr(cls, "edam:data_2798",
            PermissibleValue(
                text="edam:data_2798",
                title="MaizeDB ID",
                description="Identifier of an EST sequence from the MaizeDB database.",
                meaning=EDAM["data_2798"]))
        setattr(cls, "edam:data_2799",
            PermissibleValue(
                text="edam:data_2799",
                title="Gene ID (MfunGD)",
                description="A unique identifier of gene in the MfunGD database.",
                meaning=EDAM["data_2799"]))
        setattr(cls, "edam:data_2800",
            PermissibleValue(
                text="edam:data_2800",
                title="Orpha number",
                description="An identifier of a disease from the Orpha database.",
                meaning=EDAM["data_2800"]))
        setattr(cls, "edam:data_2802",
            PermissibleValue(
                text="edam:data_2802",
                title="Protein ID (EcID)",
                description="Unique identifier for a protein from the EcID database.",
                meaning=EDAM["data_2802"]))
        setattr(cls, "edam:data_2803",
            PermissibleValue(
                text="edam:data_2803",
                title="Clone ID (RefSeq)",
                description="A unique identifier of a cDNA molecule catalogued in the RefSeq database.",
                meaning=EDAM["data_2803"]))
        setattr(cls, "edam:data_2804",
            PermissibleValue(
                text="edam:data_2804",
                title="Protein ID (ConoServer)",
                description="Unique identifier for a cone snail toxin protein from the ConoServer database.",
                meaning=EDAM["data_2804"]))
        setattr(cls, "edam:data_2805",
            PermissibleValue(
                text="edam:data_2805",
                title="GeneSNP ID",
                description="Identifier of a GeneSNP database entry.",
                meaning=EDAM["data_2805"]))
        setattr(cls, "edam:data_2812",
            PermissibleValue(
                text="edam:data_2812",
                title="Lipid identifier",
                description="Identifier of a lipid.",
                meaning=EDAM["data_2812"]))
        setattr(cls, "edam:data_2835",
            PermissibleValue(
                text="edam:data_2835",
                title="Gene ID (VBASE2)",
                description="Identifier for a gene from the VBASE2 database.",
                meaning=EDAM["data_2835"]))
        setattr(cls, "edam:data_2836",
            PermissibleValue(
                text="edam:data_2836",
                title="DPVweb ID",
                description="A unique identifier for a virus from the DPVweb database.",
                meaning=EDAM["data_2836"]))
        setattr(cls, "edam:data_2837",
            PermissibleValue(
                text="edam:data_2837",
                title="Pathway ID (BioSystems)",
                description="Identifier of a pathway from the BioSystems pathway database.",
                meaning=EDAM["data_2837"]))
        setattr(cls, "edam:data_2849",
            PermissibleValue(
                text="edam:data_2849",
                title="Abstract",
                description="An abstract of a scientific article.",
                meaning=EDAM["data_2849"]))
        setattr(cls, "edam:data_2850",
            PermissibleValue(
                text="edam:data_2850",
                title="Lipid structure",
                description="3D coordinate and associated data for a lipid structure.",
                meaning=EDAM["data_2850"]))
        setattr(cls, "edam:data_2851",
            PermissibleValue(
                text="edam:data_2851",
                title="Drug structure",
                description="3D coordinate and associated data for the (3D) structure of a drug.",
                meaning=EDAM["data_2851"]))
        setattr(cls, "edam:data_2852",
            PermissibleValue(
                text="edam:data_2852",
                title="Toxin structure",
                description="3D coordinate and associated data for the (3D) structure of a toxin.",
                meaning=EDAM["data_2852"]))
        setattr(cls, "edam:data_2854",
            PermissibleValue(
                text="edam:data_2854",
                title="Position-specific scoring matrix",
                description="""A simple matrix of numbers, where each value (or column of values) is derived derived from analysis of the corresponding position in a sequence alignment.""",
                meaning=EDAM["data_2854"]))
        setattr(cls, "edam:data_2855",
            PermissibleValue(
                text="edam:data_2855",
                title="Distance matrix",
                description="""A matrix of distances between molecular entities, where a value (distance) is (typically) derived from comparison of two entities and reflects their similarity.""",
                meaning=EDAM["data_2855"]))
        setattr(cls, "edam:data_2856",
            PermissibleValue(
                text="edam:data_2856",
                title="Structural distance matrix",
                description="Distances (values representing similarity) between a group of molecular structures.",
                meaning=EDAM["data_2856"]))
        setattr(cls, "edam:data_2858",
            PermissibleValue(
                text="edam:data_2858",
                title="Ontology concept",
                description="""A concept from a biological ontology.
This includes any fields from the concept definition such as concept name, definition, comments and so on.""",
                meaning=EDAM["data_2858"]))
        setattr(cls, "edam:data_2865",
            PermissibleValue(
                text="edam:data_2865",
                title="Codon usage bias",
                description="""A numerical measure of differences in the frequency of occurrence of synonymous codons in DNA sequences.""",
                meaning=EDAM["data_2865"]))
        setattr(cls, "edam:data_2870",
            PermissibleValue(
                text="edam:data_2870",
                title="Radiation hybrid map",
                description="""A map showing distance between genetic markers estimated by radiation-induced breaks in a chromosome.
The radiation method can break very closely linked markers providing a more detailed map. Most genetic markers and subsequences may be located to a defined map position and with a more precise estimates of distance than a linkage map.""",
                meaning=EDAM["data_2870"]))
        setattr(cls, "edam:data_2872",
            PermissibleValue(
                text="edam:data_2872",
                title="ID list",
                description="""A simple list of data identifiers (such as database accessions), possibly with additional basic information on the addressed data.""",
                meaning=EDAM["data_2872"]))
        setattr(cls, "edam:data_2873",
            PermissibleValue(
                text="edam:data_2873",
                title="Phylogenetic gene frequencies data",
                description="Gene frequencies data that may be read during phylogenetic tree calculation.",
                meaning=EDAM["data_2873"]))
        setattr(cls, "edam:data_2877",
            PermissibleValue(
                text="edam:data_2877",
                title="Protein complex",
                description="""3D coordinate and associated data for a multi-protein complex; two or more polypeptides chains in a stable, functional association with one another.""",
                meaning=EDAM["data_2877"]))
        setattr(cls, "edam:data_2878",
            PermissibleValue(
                text="edam:data_2878",
                title="Protein structural motif",
                description="""3D coordinate and associated data for a protein (3D) structural motif; any group of contiguous or non-contiguous amino acid residues but typically those forming a feature with a structural or functional role.""",
                meaning=EDAM["data_2878"]))
        setattr(cls, "edam:data_2879",
            PermissibleValue(
                text="edam:data_2879",
                title="Lipid report",
                description="""A human-readable collection of information about one or more specific lipid 3D structure(s).""",
                meaning=EDAM["data_2879"]))
        setattr(cls, "edam:data_2884",
            PermissibleValue(
                text="edam:data_2884",
                title="Plot",
                description="""Biological data that has been plotted as a graph of some type, or plotting instructions for rendering such a graph.""",
                meaning=EDAM["data_2884"]))
        setattr(cls, "edam:data_2886",
            PermissibleValue(
                text="edam:data_2886",
                title="Protein sequence record",
                description="A protein sequence and associated metadata.",
                meaning=EDAM["data_2886"]))
        setattr(cls, "edam:data_2887",
            PermissibleValue(
                text="edam:data_2887",
                title="Nucleic acid sequence record",
                description="A nucleic acid sequence and associated metadata.",
                meaning=EDAM["data_2887"]))
        setattr(cls, "edam:data_2891",
            PermissibleValue(
                text="edam:data_2891",
                title="Biological model accession",
                description="Accession of a mathematical model, typically an entry from a database.",
                meaning=EDAM["data_2891"]))
        setattr(cls, "edam:data_2892",
            PermissibleValue(
                text="edam:data_2892",
                title="Cell type name",
                description="The name of a type or group of cells.",
                meaning=EDAM["data_2892"]))
        setattr(cls, "edam:data_2893",
            PermissibleValue(
                text="edam:data_2893",
                title="Cell type accession",
                description="Accession of a type or group of cells (catalogued in a database).",
                meaning=EDAM["data_2893"]))
        setattr(cls, "edam:data_2894",
            PermissibleValue(
                text="edam:data_2894",
                title="Compound accession",
                description="Accession of an entry from a database of chemicals.",
                meaning=EDAM["data_2894"]))
        setattr(cls, "edam:data_2895",
            PermissibleValue(
                text="edam:data_2895",
                title="Drug accession",
                description="Accession of a drug.",
                meaning=EDAM["data_2895"]))
        setattr(cls, "edam:data_2896",
            PermissibleValue(
                text="edam:data_2896",
                title="Toxin name",
                description="Name of a toxin.",
                meaning=EDAM["data_2896"]))
        setattr(cls, "edam:data_2897",
            PermissibleValue(
                text="edam:data_2897",
                title="Toxin accession",
                description="Accession of a toxin (catalogued in a database).",
                meaning=EDAM["data_2897"]))
        setattr(cls, "edam:data_2898",
            PermissibleValue(
                text="edam:data_2898",
                title="Monosaccharide accession",
                description="Accession of a monosaccharide (catalogued in a database).",
                meaning=EDAM["data_2898"]))
        setattr(cls, "edam:data_2899",
            PermissibleValue(
                text="edam:data_2899",
                title="Drug name",
                description="Common name of a drug.",
                meaning=EDAM["data_2899"]))
        setattr(cls, "edam:data_2900",
            PermissibleValue(
                text="edam:data_2900",
                title="Carbohydrate accession",
                description="Accession of an entry from a database of carbohydrates.",
                meaning=EDAM["data_2900"]))
        setattr(cls, "edam:data_2901",
            PermissibleValue(
                text="edam:data_2901",
                title="Molecule accession",
                description="Accession of a specific molecule (catalogued in a database).",
                meaning=EDAM["data_2901"]))
        setattr(cls, "edam:data_2902",
            PermissibleValue(
                text="edam:data_2902",
                title="Data resource definition accession",
                description="Accession of a data definition (catalogued in a database).",
                meaning=EDAM["data_2902"]))
        setattr(cls, "edam:data_2903",
            PermissibleValue(
                text="edam:data_2903",
                title="Genome accession",
                description="An accession of a particular genome (in a database).",
                meaning=EDAM["data_2903"]))
        setattr(cls, "edam:data_2904",
            PermissibleValue(
                text="edam:data_2904",
                title="Map accession",
                description="An accession of a map of a molecular sequence (deposited in a database).",
                meaning=EDAM["data_2904"]))
        setattr(cls, "edam:data_2905",
            PermissibleValue(
                text="edam:data_2905",
                title="Lipid accession",
                description="Accession of an entry from a database of lipids.",
                meaning=EDAM["data_2905"]))
        setattr(cls, "edam:data_2906",
            PermissibleValue(
                text="edam:data_2906",
                title="Peptide ID",
                description="Accession of a peptide deposited in a database.",
                meaning=EDAM["data_2906"]))
        setattr(cls, "edam:data_2907",
            PermissibleValue(
                text="edam:data_2907",
                title="Protein accession",
                description="Accession of a protein deposited in a database.",
                meaning=EDAM["data_2907"]))
        setattr(cls, "edam:data_2908",
            PermissibleValue(
                text="edam:data_2908",
                title="Organism accession",
                description="An accession of annotation on a (group of) organisms (catalogued in a database).",
                meaning=EDAM["data_2908"]))
        setattr(cls, "edam:data_2909",
            PermissibleValue(
                text="edam:data_2909",
                title="Organism name",
                description="The name of an organism (or group of organisms).",
                meaning=EDAM["data_2909"]))
        setattr(cls, "edam:data_2910",
            PermissibleValue(
                text="edam:data_2910",
                title="Protein family accession",
                description="Accession of a protein family (that is deposited in a database).",
                meaning=EDAM["data_2910"]))
        setattr(cls, "edam:data_2911",
            PermissibleValue(
                text="edam:data_2911",
                title="Transcription factor accession",
                description="Accession of an entry from a database of transcription factors or binding sites.",
                meaning=EDAM["data_2911"]))
        setattr(cls, "edam:data_2912",
            PermissibleValue(
                text="edam:data_2912",
                title="Strain accession",
                description="""Accession number of a strain of an organism variant, typically a plant, virus or bacterium.""",
                meaning=EDAM["data_2912"]))
        setattr(cls, "edam:data_2914",
            PermissibleValue(
                text="edam:data_2914",
                title="Sequence features metadata",
                description="Metadata on sequence features.",
                meaning=EDAM["data_2914"]))
        setattr(cls, "edam:data_2915",
            PermissibleValue(
                text="edam:data_2915",
                title="Gramene identifier",
                description="Identifier of a Gramene database entry.",
                meaning=EDAM["data_2915"]))
        setattr(cls, "edam:data_2916",
            PermissibleValue(
                text="edam:data_2916",
                title="DDBJ accession",
                description="An identifier of an entry from the DDBJ sequence database.",
                meaning=EDAM["data_2916"]))
        setattr(cls, "edam:data_2917",
            PermissibleValue(
                text="edam:data_2917",
                title="ConsensusPathDB identifier",
                description="An identifier of an entity from the ConsensusPathDB database.",
                meaning=EDAM["data_2917"]))
        setattr(cls, "edam:data_2955",
            PermissibleValue(
                text="edam:data_2955",
                title="Sequence report",
                description="""An informative report of information about molecular sequence(s), including basic information (metadata), and reports generated from molecular sequence analysis, including positional features and non-positional properties.""",
                meaning=EDAM["data_2955"]))
        setattr(cls, "edam:data_2956",
            PermissibleValue(
                text="edam:data_2956",
                title="Protein secondary structure",
                description="""Data concerning the properties or features of one or more protein secondary structures.""",
                meaning=EDAM["data_2956"]))
        setattr(cls, "edam:data_2957",
            PermissibleValue(
                text="edam:data_2957",
                title="Hopp and Woods plot",
                description="A Hopp and Woods plot of predicted antigenicity of a peptide or protein.",
                meaning=EDAM["data_2957"]))
        setattr(cls, "edam:data_2968",
            PermissibleValue(
                text="edam:data_2968",
                title="Image",
                description="""Data (typically biological or biomedical) that has been rendered into an image, typically for display on screen.""",
                meaning=EDAM["data_2968"]))
        setattr(cls, "edam:data_2969",
            PermissibleValue(
                text="edam:data_2969",
                title="Sequence image",
                description="Image of a molecular sequence, possibly with sequence features or properties shown.",
                meaning=EDAM["data_2969"]))
        setattr(cls, "edam:data_2970",
            PermissibleValue(
                text="edam:data_2970",
                title="Protein hydropathy data",
                description="A report on protein properties concerning hydropathy.",
                meaning=EDAM["data_2970"]))
        setattr(cls, "edam:data_2976",
            PermissibleValue(
                text="edam:data_2976",
                title="Protein sequence",
                description="One or more protein sequences, possibly with associated annotation.",
                meaning=EDAM["data_2976"]))
        setattr(cls, "edam:data_2977",
            PermissibleValue(
                text="edam:data_2977",
                title="Nucleic acid sequence",
                description="One or more nucleic acid sequences, possibly with associated annotation.",
                meaning=EDAM["data_2977"]))
        setattr(cls, "edam:data_2978",
            PermissibleValue(
                text="edam:data_2978",
                title="Reaction data",
                description="""Data concerning a biochemical reaction, typically data and more general annotation on the kinetics of enzyme-catalysed reaction.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_2978"]))
        setattr(cls, "edam:data_2979",
            PermissibleValue(
                text="edam:data_2979",
                title="Peptide property",
                description="Data concerning small peptides.",
                meaning=EDAM["data_2979"]))
        setattr(cls, "edam:data_2984",
            PermissibleValue(
                text="edam:data_2984",
                title="Pathway or network report",
                description="""An informative report concerning or derived from the analysis of a biological pathway or network, such as a map (diagram) or annotation.""",
                meaning=EDAM["data_2984"]))
        setattr(cls, "edam:data_2985",
            PermissibleValue(
                text="edam:data_2985",
                title="Nucleic acid thermodynamic data",
                description="A thermodynamic or kinetic property of a nucleic acid molecule.",
                meaning=EDAM["data_2985"]))
        setattr(cls, "edam:data_2991",
            PermissibleValue(
                text="edam:data_2991",
                title="Protein geometry data",
                description="""Geometry data for a protein structure, for example bond lengths, bond angles, torsion angles, chiralities, planaraties etc.""",
                meaning=EDAM["data_2991"]))
        setattr(cls, "edam:data_2992",
            PermissibleValue(
                text="edam:data_2992",
                title="Protein structure image",
                description="An image of protein structure.",
                meaning=EDAM["data_2992"]))
        setattr(cls, "edam:data_2994",
            PermissibleValue(
                text="edam:data_2994",
                title="Phylogenetic character weights",
                description="""Weights for sequence positions or characters in phylogenetic analysis where zero is defined as unweighted.""",
                meaning=EDAM["data_2994"]))
        setattr(cls, "edam:data_3002",
            PermissibleValue(
                text="edam:data_3002",
                title="Annotation track",
                description="""Annotation of one particular positional feature on a biomolecular (typically genome) sequence, suitable for import and display in a genome browser.""",
                meaning=EDAM["data_3002"]))
        setattr(cls, "edam:data_3021",
            PermissibleValue(
                text="edam:data_3021",
                title="UniProt accession",
                description="Accession number of a UniProt (protein sequence) database entry.",
                meaning=EDAM["data_3021"]))
        setattr(cls, "edam:data_3022",
            PermissibleValue(
                text="edam:data_3022",
                title="NCBI genetic code ID",
                description="Identifier of a genetic code in the NCBI list of genetic codes.",
                meaning=EDAM["data_3022"]))
        setattr(cls, "edam:data_3025",
            PermissibleValue(
                text="edam:data_3025",
                title="Ontology concept identifier",
                description="""Identifier of a concept in an ontology of biological or bioinformatics concepts and relations.""",
                meaning=EDAM["data_3025"]))
        setattr(cls, "edam:data_3028",
            PermissibleValue(
                text="edam:data_3028",
                title="Taxonomy",
                description="""Data concerning the classification, identification and naming of organisms.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_3028"]))
        setattr(cls, "edam:data_3029",
            PermissibleValue(
                text="edam:data_3029",
                title="Protein ID (EMBL/GenBank/DDBJ)",
                description="""EMBL/GENBANK/DDBJ coding feature protein identifier, issued by International collaborators.
This qualifier consists of a stable ID portion (3+5 format with 3 position letters and 5 numbers) plus a version number after the decimal point. When the protein sequence encoded by the CDS changes, only the version number of the /protein_id value is incremented; the stable part of the /protein_id remains unchanged and as a result will permanently be associated with a given protein; this qualifier is valid only on CDS features which translate into a valid protein.""",
                meaning=EDAM["data_3029"]))
        setattr(cls, "edam:data_3034",
            PermissibleValue(
                text="edam:data_3034",
                title="Sequence feature identifier",
                description="Name or other identifier of molecular sequence feature(s).",
                meaning=EDAM["data_3034"]))
        setattr(cls, "edam:data_3035",
            PermissibleValue(
                text="edam:data_3035",
                title="Structure identifier",
                description="""An identifier of a molecular tertiary structure, typically an entry from a structure database.""",
                meaning=EDAM["data_3035"]))
        setattr(cls, "edam:data_3036",
            PermissibleValue(
                text="edam:data_3036",
                title="Matrix identifier",
                description="An identifier of an array of numerical values, such as a comparison matrix.",
                meaning=EDAM["data_3036"]))
        setattr(cls, "edam:data_3103",
            PermissibleValue(
                text="edam:data_3103",
                title="ATC code",
                description="""Unique identifier of a drug conforming to the Anatomical Therapeutic Chemical (ATC) Classification System, a drug classification system controlled by the WHO Collaborating Centre for Drug Statistics Methodology (WHOCC).""",
                meaning=EDAM["data_3103"]))
        setattr(cls, "edam:data_3104",
            PermissibleValue(
                text="edam:data_3104",
                title="UNII",
                description="""A unique, unambiguous, alphanumeric identifier of a chemical substance as catalogued by the Substance Registration System of the Food and Drug Administration (FDA).""",
                meaning=EDAM["data_3104"]))
        setattr(cls, "edam:data_3106",
            PermissibleValue(
                text="edam:data_3106",
                title="System metadata",
                description="Metadata concerning the software, hardware or other aspects of a computer system.",
                meaning=EDAM["data_3106"]))
        setattr(cls, "edam:data_3108",
            PermissibleValue(
                text="edam:data_3108",
                title="Experimental measurement",
                description="""Raw data such as measurements or other results from laboratory experiments, as generated from laboratory hardware.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.""",
                meaning=EDAM["data_3108"]))
        setattr(cls, "edam:data_3110",
            PermissibleValue(
                text="edam:data_3110",
                title="Raw microarray data",
                description="""Raw data (typically MIAME-compliant) for hybridisations from a microarray experiment.
Such data as found in Affymetrix CEL or GPR files.""",
                meaning=EDAM["data_3110"]))
        setattr(cls, "edam:data_3111",
            PermissibleValue(
                text="edam:data_3111",
                title="Processed microarray data",
                description="""Data generated from processing and analysis of probe set data from a microarray experiment.
Such data as found in Affymetrix .CHP files or data from other software such as RMA or dChip.""",
                meaning=EDAM["data_3111"]))
        setattr(cls, "edam:data_3112",
            PermissibleValue(
                text="edam:data_3112",
                title="Gene expression matrix",
                description="""The final processed (normalised) data for a set of hybridisations in a microarray experiment.
This combines data from all hybridisations.""",
                meaning=EDAM["data_3112"]))
        setattr(cls, "edam:data_3113",
            PermissibleValue(
                text="edam:data_3113",
                title="Sample annotation",
                description="""Annotation on a biological sample, for example experimental factors and their values.
This might include compound and dose in a dose response experiment.""",
                meaning=EDAM["data_3113"]))
        setattr(cls, "edam:data_3115",
            PermissibleValue(
                text="edam:data_3115",
                title="Microarray metadata",
                description="""Annotation on the array itself used in a microarray experiment.
This might include gene identifiers, genomic coordinates, probe oligonucleotide sequences etc.""",
                meaning=EDAM["data_3115"]))
        setattr(cls, "edam:data_3117",
            PermissibleValue(
                text="edam:data_3117",
                title="Microarray hybridisation data",
                description="Data concerning the hybridisations measured during a microarray experiment.",
                meaning=EDAM["data_3117"]))
        setattr(cls, "edam:data_3128",
            PermissibleValue(
                text="edam:data_3128",
                title="Nucleic acid structure report",
                description="""A human-readable collection of information about regions within a nucleic acid sequence which form secondary or tertiary (3D) structures.
The report may be based on analysis of nucleic acid sequence or structural data, or any annotation or information about specific nucleic acid 3D structure(s) or such structures in general.""",
                meaning=EDAM["data_3128"]))
        setattr(cls, "edam:data_3134",
            PermissibleValue(
                text="edam:data_3134",
                title="Gene transcript report",
                description="""An informative report on features of a messenger RNA (mRNA) molecules including precursor RNA, primary (unprocessed) transcript and fully processed molecules. This includes reports on a specific gene transcript, clone or EST.
This includes 5'untranslated region (5'UTR), coding sequences (CDS), exons, intervening sequences (intron) and 3'untranslated regions (3'UTR).""",
                meaning=EDAM["data_3134"]))
        setattr(cls, "edam:data_3148",
            PermissibleValue(
                text="edam:data_3148",
                title="Gene family report",
                description="""A human-readable collection of information about a particular family of genes, typically a set of genes with similar sequence that originate from duplication of a common ancestor gene, or any other classification of nucleic acid sequences or structures that reflects gene structure.
This includes reports on on gene homologues between species.""",
                meaning=EDAM["data_3148"]))
        setattr(cls, "edam:data_3153",
            PermissibleValue(
                text="edam:data_3153",
                title="Protein image",
                description="An image of a protein.",
                meaning=EDAM["data_3153"]))
        setattr(cls, "edam:data_3181",
            PermissibleValue(
                text="edam:data_3181",
                title="Sequence assembly report",
                description="""An informative report about a DNA sequence assembly.
This might include an overall quality assessment of the assembly and summary statistics including counts, average length and number of bases for reads, matches and non-matches, contigs, reads in pairs etc.""",
                meaning=EDAM["data_3181"]))
        setattr(cls, "edam:data_3210",
            PermissibleValue(
                text="edam:data_3210",
                title="Genome index",
                description="""An index of a genome sequence.
Many sequence alignment tasks involving many or very large sequences rely on a precomputed index of the sequence to accelerate the alignment.""",
                meaning=EDAM["data_3210"]))
        setattr(cls, "edam:data_3236",
            PermissibleValue(
                text="edam:data_3236",
                title="Cytoband position",
                description="""Information might include start and end position in a chromosome sequence, chromosome identifier, name of band and so on.
The position of a cytogenetic band in a genome.""",
                meaning=EDAM["data_3236"]))
        setattr(cls, "edam:data_3238",
            PermissibleValue(
                text="edam:data_3238",
                title="Cell type ontology ID",
                description="Cell type ontology concept ID.",
                meaning=EDAM["data_3238"]))
        setattr(cls, "edam:data_3241",
            PermissibleValue(
                text="edam:data_3241",
                title="Kinetic model",
                description="Mathematical model of a network, that contains biochemical kinetics.",
                meaning=EDAM["data_3241"]))
        setattr(cls, "edam:data_3264",
            PermissibleValue(
                text="edam:data_3264",
                title="COSMIC ID",
                description="Identifier of a COSMIC database entry.",
                meaning=EDAM["data_3264"]))
        setattr(cls, "edam:data_3265",
            PermissibleValue(
                text="edam:data_3265",
                title="HGMD ID",
                description="Identifier of a HGMD database entry.",
                meaning=EDAM["data_3265"]))
        setattr(cls, "edam:data_3266",
            PermissibleValue(
                text="edam:data_3266",
                title="Sequence assembly ID",
                description="Unique identifier of sequence assembly.",
                meaning=EDAM["data_3266"]))
        setattr(cls, "edam:data_3270",
            PermissibleValue(
                text="edam:data_3270",
                title="Ensembl gene tree ID",
                description="Unique identifier for a gene tree from the Ensembl database.",
                meaning=EDAM["data_3270"]))
        setattr(cls, "edam:data_3271",
            PermissibleValue(
                text="edam:data_3271",
                title="Gene tree",
                description="A phylogenetic tree that is an estimate of the character's phylogeny.",
                meaning=EDAM["data_3271"]))
        setattr(cls, "edam:data_3272",
            PermissibleValue(
                text="edam:data_3272",
                title="Species tree",
                description="""A phylogenetic tree that reflects phylogeny of the taxa from which the characters (used in calculating the tree) were sampled.""",
                meaning=EDAM["data_3272"]))
        setattr(cls, "edam:data_3273",
            PermissibleValue(
                text="edam:data_3273",
                title="Sample ID",
                description="Name or other identifier of an entry from a biosample database.",
                meaning=EDAM["data_3273"]))
        setattr(cls, "edam:data_3274",
            PermissibleValue(
                text="edam:data_3274",
                title="MGI accession",
                description="Identifier of an object from the MGI database.",
                meaning=EDAM["data_3274"]))
        setattr(cls, "edam:data_3275",
            PermissibleValue(
                text="edam:data_3275",
                title="Phenotype name",
                description="Name of a phenotype.",
                meaning=EDAM["data_3275"]))
        setattr(cls, "edam:data_3354",
            PermissibleValue(
                text="edam:data_3354",
                title="Transition matrix",
                description="""A HMM transition matrix contains the probabilities of switching from one HMM state to another.
Consider for example an HMM with two states (AT-rich and GC-rich). The transition matrix will hold the probabilities of switching from the AT-rich to the GC-rich state, and vica versa.""",
                meaning=EDAM["data_3354"]))
        setattr(cls, "edam:data_3355",
            PermissibleValue(
                text="edam:data_3355",
                title="Emission matrix",
                description="""A HMM emission matrix holds the probabilities of choosing the four nucleotides (A, C, G and T) in each of the states of a HMM.
Consider for example an HMM with two states (AT-rich and GC-rich). The emission matrix holds the probabilities of choosing each of the four nucleotides (A, C, G and T) in the AT-rich state and in the GC-rich state.""",
                meaning=EDAM["data_3355"]))
        setattr(cls, "edam:data_3358",
            PermissibleValue(
                text="edam:data_3358",
                title="Format identifier",
                description="An identifier of a data format.",
                meaning=EDAM["data_3358"]))
        setattr(cls, "edam:data_3424",
            PermissibleValue(
                text="edam:data_3424",
                title="Raw image",
                description="Raw biological or biomedical image generated by some experimental technique.",
                meaning=EDAM["data_3424"]))
        setattr(cls, "edam:data_3425",
            PermissibleValue(
                text="edam:data_3425",
                title="Carbohydrate property",
                description="""Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all carbohydrates.""",
                meaning=EDAM["data_3425"]))
        setattr(cls, "edam:data_3442",
            PermissibleValue(
                text="edam:data_3442",
                title="MRI image",
                description="""An imaging technique that uses magnetic fields and radiowaves to form images, typically to investigate the anatomy and physiology of the human body.""",
                meaning=EDAM["data_3442"]))
        setattr(cls, "edam:data_3449",
            PermissibleValue(
                text="edam:data_3449",
                title="Cell migration track image",
                description="An image from a cell migration track assay.",
                meaning=EDAM["data_3449"]))
        setattr(cls, "edam:data_3451",
            PermissibleValue(
                text="edam:data_3451",
                title="Rate of association",
                description="Rate of association of a protein with another protein or some other molecule.",
                meaning=EDAM["data_3451"]))
        setattr(cls, "edam:data_3479",
            PermissibleValue(
                text="edam:data_3479",
                title="Gene order",
                description="""Multiple gene identifiers in a specific order.
Such data are often used for genome rearrangement tools and phylogenetic tree labeling.""",
                meaning=EDAM["data_3479"]))
        setattr(cls, "edam:data_3483",
            PermissibleValue(
                text="edam:data_3483",
                title="Spectrum",
                description="""The spectrum of frequencies of electromagnetic radiation emitted from a molecule as a result of some spectroscopy experiment.""",
                meaning=EDAM["data_3483"]))
        setattr(cls, "edam:data_3488",
            PermissibleValue(
                text="edam:data_3488",
                title="NMR spectrum",
                description="Spectral information for a molecule from a nuclear magnetic resonance experiment.",
                meaning=EDAM["data_3488"]))
        setattr(cls, "edam:data_3492",
            PermissibleValue(
                text="edam:data_3492",
                title="Nucleic acid signature",
                description="An informative report about a specific or conserved nucleic acid sequence pattern.",
                meaning=EDAM["data_3492"]))
        setattr(cls, "edam:data_3494",
            PermissibleValue(
                text="edam:data_3494",
                title="DNA sequence",
                description="A DNA sequence.",
                meaning=EDAM["data_3494"]))
        setattr(cls, "edam:data_3495",
            PermissibleValue(
                text="edam:data_3495",
                title="RNA sequence",
                description="An RNA sequence.",
                meaning=EDAM["data_3495"]))
        setattr(cls, "edam:data_3498",
            PermissibleValue(
                text="edam:data_3498",
                title="Sequence variations",
                description="""Data on gene sequence variations resulting large-scale genotyping and DNA sequencing projects.
Variations are stored along with a reference genome.""",
                meaning=EDAM["data_3498"]))
        setattr(cls, "edam:data_3505",
            PermissibleValue(
                text="edam:data_3505",
                title="Bibliography",
                description="A list of publications such as scientic papers or books.",
                meaning=EDAM["data_3505"]))
        setattr(cls, "edam:data_3509",
            PermissibleValue(
                text="edam:data_3509",
                title="Ontology mapping",
                description="A mapping of supplied textual terms or phrases to ontology concepts (URIs).",
                meaning=EDAM["data_3509"]))
        setattr(cls, "edam:data_3546",
            PermissibleValue(
                text="edam:data_3546",
                title="Image metadata",
                description="""Any data concerning a specific biological or biomedical image.
This can include basic provenance and technical information about the image, scientific annotation and so on.""",
                meaning=EDAM["data_3546"]))
        setattr(cls, "edam:data_3558",
            PermissibleValue(
                text="edam:data_3558",
                title="Clinical trial report",
                description="A human-readable collection of information concerning a clinical trial.",
                meaning=EDAM["data_3558"]))
        setattr(cls, "edam:data_3567",
            PermissibleValue(
                text="edam:data_3567",
                title="Reference sample report",
                description="A report about a biosample.",
                meaning=EDAM["data_3567"]))
        setattr(cls, "edam:data_3568",
            PermissibleValue(
                text="edam:data_3568",
                title="Gene Expression Atlas Experiment ID",
                description="Accession number of an entry from the Gene Expression Atlas.",
                meaning=EDAM["data_3568"]))
        setattr(cls, "edam:data_3667",
            PermissibleValue(
                text="edam:data_3667",
                title="Disease identifier",
                description="Identifier of an entry from a database of disease.",
                meaning=EDAM["data_3667"]))
        setattr(cls, "edam:data_3668",
            PermissibleValue(
                text="edam:data_3668",
                title="Disease name",
                description="The name of some disease.",
                meaning=EDAM["data_3668"]))
        setattr(cls, "edam:data_3669",
            PermissibleValue(
                text="edam:data_3669",
                title="Learning material",
                description="""Learning material is a document or another digital object that is designed for learning (educational, training) purposes.""",
                meaning=EDAM["data_3669"]))
        setattr(cls, "edam:data_3670",
            PermissibleValue(
                text="edam:data_3670",
                title="Online course",
                description="A training course available for use on the Web.",
                meaning=EDAM["data_3670"]))
        setattr(cls, "edam:data_3671",
            PermissibleValue(
                text="edam:data_3671",
                title="Text",
                description="""Any free or plain text, typically for human consumption and in English. Can instantiate also as a textual search query.""",
                meaning=EDAM["data_3671"]))
        setattr(cls, "edam:data_3707",
            PermissibleValue(
                text="edam:data_3707",
                title="Biodiversity data",
                description="Machine-readable biodiversity data.",
                meaning=EDAM["data_3707"]))
        setattr(cls, "edam:data_3716",
            PermissibleValue(
                text="edam:data_3716",
                title="Biosafety report",
                description="A human-readable collection of information concerning biosafety data.",
                meaning=EDAM["data_3716"]))
        setattr(cls, "edam:data_3717",
            PermissibleValue(
                text="edam:data_3717",
                title="Isolation report",
                description="A report about any kind of isolation of biological material.",
                meaning=EDAM["data_3717"]))
        setattr(cls, "edam:data_3718",
            PermissibleValue(
                text="edam:data_3718",
                title="Pathogenicity report",
                description="Information about the ability of an organism to cause disease in a corresponding host.",
                meaning=EDAM["data_3718"]))
        setattr(cls, "edam:data_3719",
            PermissibleValue(
                text="edam:data_3719",
                title="Biosafety classification",
                description="""Information about the biosafety classification of an organism according to corresponding law.""",
                meaning=EDAM["data_3719"]))
        setattr(cls, "edam:data_3720",
            PermissibleValue(
                text="edam:data_3720",
                title="Geographic location",
                description="""A report about localisation of the isolaton of biological material e.g. country or coordinates.""",
                meaning=EDAM["data_3720"]))
        setattr(cls, "edam:data_3721",
            PermissibleValue(
                text="edam:data_3721",
                title="Isolation source",
                description="""A report about any kind of isolation source of biological material e.g. blood, water, soil.""",
                meaning=EDAM["data_3721"]))
        setattr(cls, "edam:data_3722",
            PermissibleValue(
                text="edam:data_3722",
                title="Physiology parameter",
                description="""Experimentally determined parameter of the physiology of an organism, e.g. substrate spectrum.""",
                meaning=EDAM["data_3722"]))
        setattr(cls, "edam:data_3723",
            PermissibleValue(
                text="edam:data_3723",
                title="Morphology parameter",
                description="""Experimentally determined parameter of the morphology of an organism, e.g. size & shape.""",
                meaning=EDAM["data_3723"]))
        setattr(cls, "edam:data_3724",
            PermissibleValue(
                text="edam:data_3724",
                title="Cultivation parameter",
                description="Experimental determined parameter for the cultivation of an organism.",
                meaning=EDAM["data_3724"]))
        setattr(cls, "edam:data_3732",
            PermissibleValue(
                text="edam:data_3732",
                title="Sequencing metadata name",
                description="""Data concerning a sequencing experiment, that may be specified as an input to some tool.""",
                meaning=EDAM["data_3732"]))
        setattr(cls, "edam:data_3733",
            PermissibleValue(
                text="edam:data_3733",
                title="Flow cell identifier",
                description="""A flow cell is used to immobilise, amplify and sequence millions of molecules at once. In Illumina machines, a flowcell is composed of 8 \"lanes\" which allows 8 experiments in a single analysis.
An identifier of a flow cell of a sequencing machine.""",
                meaning=EDAM["data_3733"]))
        setattr(cls, "edam:data_3734",
            PermissibleValue(
                text="edam:data_3734",
                title="Lane identifier",
                description="""An identifier of a lane within a flow cell of a sequencing machine, within which millions of sequences are immobilised, amplified and sequenced.""",
                meaning=EDAM["data_3734"]))
        setattr(cls, "edam:data_3735",
            PermissibleValue(
                text="edam:data_3735",
                title="Run number",
                description="""A number corresponding to the number of an analysis performed by a sequencing machine. For example, if it's the 13th analysis, the run is 13.""",
                meaning=EDAM["data_3735"]))
        setattr(cls, "edam:data_3736",
            PermissibleValue(
                text="edam:data_3736",
                title="Ecological data",
                description="""Data concerning ecology; for example measurements and reports from the study of interactions among organisms and their environment.
This is a broad data type and is used a placeholder for other, more specific types.""",
                meaning=EDAM["data_3736"]))
        setattr(cls, "edam:data_3737",
            PermissibleValue(
                text="edam:data_3737",
                title="Alpha diversity data",
                description="The mean species diversity in sites or habitats at a local scale.",
                meaning=EDAM["data_3737"]))
        setattr(cls, "edam:data_3738",
            PermissibleValue(
                text="edam:data_3738",
                title="Beta diversity data",
                description="The ratio between regional and local species diversity.",
                meaning=EDAM["data_3738"]))
        setattr(cls, "edam:data_3739",
            PermissibleValue(
                text="edam:data_3739",
                title="Gamma diversity data",
                description="The total species diversity in a landscape.",
                meaning=EDAM["data_3739"]))
        setattr(cls, "edam:data_3743",
            PermissibleValue(
                text="edam:data_3743",
                title="Ordination plot",
                description="""A plot in which community data (e.g. species abundance data) is summarised. Similar species and samples are plotted close together, and dissimilar species and samples are plotted placed far apart.""",
                meaning=EDAM["data_3743"]))
        setattr(cls, "edam:data_3753",
            PermissibleValue(
                text="edam:data_3753",
                title="Over-representation data",
                description="""A ranked list of categories (usually ontology concepts), each associated with a statistical metric of over-/under-representation within the studied data.""",
                meaning=EDAM["data_3753"]))
        setattr(cls, "edam:data_3754",
            PermissibleValue(
                text="edam:data_3754",
                title="GO-term enrichment data",
                description="""A ranked list of Gene Ontology concepts, each associated with a p-value, concerning or derived from the analysis of e.g. a set of genes or proteins.""",
                meaning=EDAM["data_3754"]))
        setattr(cls, "edam:data_3756",
            PermissibleValue(
                text="edam:data_3756",
                title="Localisation score",
                description="""Score for localization of one or more post-translational modifications in peptide sequence measured by mass spectrometry.""",
                meaning=EDAM["data_3756"]))
        setattr(cls, "edam:data_3757",
            PermissibleValue(
                text="edam:data_3757",
                title="Unimod ID",
                description="Identifier of a protein modification catalogued in the Unimod database.",
                meaning=EDAM["data_3757"]))
        setattr(cls, "edam:data_3759",
            PermissibleValue(
                text="edam:data_3759",
                title="ProteomeXchange ID",
                description="""Identifier for mass spectrometry proteomics data in the proteomexchange.org repository.""",
                meaning=EDAM["data_3759"]))
        setattr(cls, "edam:data_3768",
            PermissibleValue(
                text="edam:data_3768",
                title="Clustered expression profiles",
                description="Groupings of expression profiles according to a clustering algorithm.",
                meaning=EDAM["data_3768"]))
        setattr(cls, "edam:data_3769",
            PermissibleValue(
                text="edam:data_3769",
                title="BRENDA ontology concept ID",
                description="An identifier of a concept from the BRENDA ontology.",
                meaning=EDAM["data_3769"]))
        setattr(cls, "edam:data_3779",
            PermissibleValue(
                text="edam:data_3779",
                title="Annotated text",
                description="""A text (such as a scientific article), annotated with notes, data and metadata, such as recognised entities, concepts, and their relations.""",
                meaning=EDAM["data_3779"]))
        setattr(cls, "edam:data_3786",
            PermissibleValue(
                text="edam:data_3786",
                title="Query script",
                description="A structured query, in form of a script, that defines a database search task.",
                meaning=EDAM["data_3786"]))
        setattr(cls, "edam:data_3805",
            PermissibleValue(
                text="edam:data_3805",
                title="3D EM Map",
                description="Structural 3D model (volume map) from electron microscopy.",
                meaning=EDAM["data_3805"]))
        setattr(cls, "edam:data_3806",
            PermissibleValue(
                text="edam:data_3806",
                title="3D EM Mask",
                description="""Annotation on a structural 3D EM Map from electron microscopy. This might include one or several locations in the map of the known features of a particular macromolecule.""",
                meaning=EDAM["data_3806"]))
        setattr(cls, "edam:data_3807",
            PermissibleValue(
                text="edam:data_3807",
                title="EM Movie",
                description="Raw DDD movie acquisition from electron microscopy.",
                meaning=EDAM["data_3807"]))
        setattr(cls, "edam:data_3808",
            PermissibleValue(
                text="edam:data_3808",
                title="EM Micrograph",
                description="Raw acquisition from electron microscopy or average of an aligned DDD movie.",
                meaning=EDAM["data_3808"]))
        setattr(cls, "edam:data_3842",
            PermissibleValue(
                text="edam:data_3842",
                title="Molecular simulation data",
                description="""Data coming from molecular simulations, computer \"experiments\" on model molecules.
Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic).""",
                meaning=EDAM["data_3842"]))
        setattr(cls, "edam:data_3856",
            PermissibleValue(
                text="edam:data_3856",
                title="RNA central ID",
                description="""Identifier of an entry from the RNA central database of annotated human miRNAs.
There are canonical and taxon-specific forms of RNAcentral ID. Canonical form e.g. urs_9or10digits identifies an RNA sequence (within the RNA central database) which may appear in multiple sequences. Taxon-specific form identifies a sequence in the specific taxon (e.g. urs_9or10digits_taxonID).""",
                meaning=EDAM["data_3856"]))
        setattr(cls, "edam:data_3861",
            PermissibleValue(
                text="edam:data_3861",
                title="Electronic health record",
                description="""A human-readable systematic collection of patient (or population) health information in a digital format.""",
                meaning=EDAM["data_3861"]))
        setattr(cls, "edam:data_3869",
            PermissibleValue(
                text="edam:data_3869",
                title="Simulation",
                description="""Data coming from molecular simulations, computer \"experiments\" on model molecules. Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic).""",
                meaning=EDAM["data_3869"]))
        setattr(cls, "edam:data_3870",
            PermissibleValue(
                text="edam:data_3870",
                title="Trajectory data",
                description="""Dynamic information of a structure molecular system coming from a molecular simulation: XYZ 3D coordinates (sometimes with their associated velocities) for every atom along time.""",
                meaning=EDAM["data_3870"]))
        setattr(cls, "edam:data_3871",
            PermissibleValue(
                text="edam:data_3871",
                title="Forcefield parameters",
                description="""Force field parameters: charges, masses, radii, bond lengths, bond dihedrals, etc. define the structural molecular system, and are essential for the proper description and simulation of a molecular system.""",
                meaning=EDAM["data_3871"]))
        setattr(cls, "edam:data_3872",
            PermissibleValue(
                text="edam:data_3872",
                title="Topology data",
                description="""Static information of a structure molecular system that is needed for a molecular simulation: the list of atoms, their non-bonded parameters for Van der Waals and electrostatic interactions, and the complete connectivity in terms of bonds, angles and dihedrals.""",
                meaning=EDAM["data_3872"]))
        setattr(cls, "edam:data_3905",
            PermissibleValue(
                text="edam:data_3905",
                title="Histogram",
                description="""Visualization of distribution of quantitative data, e.g. expression data, by histograms, violin plots and density plots.""",
                meaning=EDAM["data_3905"]))
        setattr(cls, "edam:data_3914",
            PermissibleValue(
                text="edam:data_3914",
                title="Quality control report",
                description="Report of the quality control review that was made of factors involved in a procedure.",
                meaning=EDAM["data_3914"]))
        setattr(cls, "edam:data_3917",
            PermissibleValue(
                text="edam:data_3917",
                title="Count matrix",
                description="""A table of unnormalized values representing summarised read counts per genomic region (e.g. gene, transcript, peak).""",
                meaning=EDAM["data_3917"]))
        setattr(cls, "edam:data_3924",
            PermissibleValue(
                text="edam:data_3924",
                title="DNA structure alignment",
                description="Alignment (superimposition) of DNA tertiary (3D) structures.",
                meaning=EDAM["data_3924"]))
        setattr(cls, "edam:data_3932",
            PermissibleValue(
                text="edam:data_3932",
                title="Q-value",
                description="""A score derived from the P-value to ensure correction for multiple tests. The Q-value provides an estimate of the positive False Discovery Rate (pFDR), i.e. the rate of false positives among all the cases reported positive: pFDR = FP / (FP + TP).
Q-values are widely used in high-throughput data analysis (e.g. detection of differentially expressed genes from transcriptome data).""",
                meaning=EDAM["data_3932"]))
        setattr(cls, "edam:data_3949",
            PermissibleValue(
                text="edam:data_3949",
                title="Profile HMM",
                description="""A profile HMM is a variant of a Hidden Markov model that is derived specifically from a set of (aligned) biological sequences. Profile HMMs provide the basis for a position-specific scoring system, which can be used to align sequences and search databases for related sequences.""",
                meaning=EDAM["data_3949"]))
        setattr(cls, "edam:data_3952",
            PermissibleValue(
                text="edam:data_3952",
                title="Pathway ID (WikiPathways)",
                description="Identifier of a pathway from the WikiPathways pathway database.",
                meaning=EDAM["data_3952"]))
        setattr(cls, "edam:data_3953",
            PermissibleValue(
                text="edam:data_3953",
                title="Pathway overrepresentation data",
                description="""A ranked list of pathways, each associated with z-score, p-value or similar, concerning or derived from the analysis of e.g. a set of genes or proteins.""",
                meaning=EDAM["data_3953"]))
        setattr(cls, "edam:data_4022",
            PermissibleValue(
                text="edam:data_4022",
                title="ORCID Identifier",
                description="""Identifier of a researcher registered with the ORCID database. Used to identify author IDs.""",
                meaning=EDAM["data_4022"]))
        setattr(cls, "edam:data_4040",
            PermissibleValue(
                text="edam:data_4040",
                title="Data management plan",
                description="""Data management plan is a document describing the data management of a project or an organisation, including acquisition, reuse, structure, processing, storage, documentation, sharing, and preservation of data. This may include budgeting for these operations.""",
                meaning=EDAM["data_4040"]))

class EnumFileHashType(EnumDefinitionImpl):
    """
    Types of file hashes supported.
    """
    md5 = PermissibleValue(
        text="md5",
        title="MD5")
    etag = PermissibleValue(
        text="etag",
        title="ETag")
    sha1 = PermissibleValue(
        text="sha1",
        title="SHA-1")

    _defn = EnumDefinition(
        name="EnumFileHashType",
        description="Types of file hashes supported.",
    )

# Slots
class slots:
    pass

slots.requiredClass__id = Slot(uri=CAM.id, name="requiredClass__id", curie=CAM.curie('id'),
                   model_uri=CAM.requiredClass__id, domain=None, range=Optional[str])

slots.requiredClass__full_name = Slot(uri=CAM.full_name, name="requiredClass__full_name", curie=CAM.curie('full_name'),
                   model_uri=CAM.requiredClass__full_name, domain=None, range=Optional[str])

slots.requiredClass__aliases = Slot(uri=CAM.aliases, name="requiredClass__aliases", curie=CAM.curie('aliases'),
                   model_uri=CAM.requiredClass__aliases, domain=None, range=Optional[str])

slots.requiredClass__phone = Slot(uri=CAM.phone, name="requiredClass__phone", curie=CAM.curie('phone'),
                   model_uri=CAM.requiredClass__phone, domain=None, range=Optional[str])

slots.requiredClass__age = Slot(uri=CAM.age, name="requiredClass__age", curie=CAM.curie('age'),
                   model_uri=CAM.requiredClass__age, domain=None, range=Optional[str])
