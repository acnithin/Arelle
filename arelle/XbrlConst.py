from arelle.ModelValue import (qname)
import os

xsd = "http://www.w3.org/2001/XMLSchema"
xsi = "http://www.w3.org/2001/XMLSchema-instance"
qnXsiNil = qname(xsi,"xsi:nil") # need default prefix in qname
xml = "http://www.w3.org/XML/1998/namespace"
xbrli = "http://www.xbrl.org/2003/instance"
qnXbrliItem = qname("{http://www.xbrl.org/2003/instance}item")
qnXbrliTuple = qname("{http://www.xbrl.org/2003/instance}tuple")
qnXbrliStringItemType = qname("{http://www.xbrl.org/2003/instance}stringItemType")
qnXbrliMonetaryItemType = qname("{http://www.xbrl.org/2003/instance}monetaryItemType")
qnXbrliPure = qname("{http://www.xbrl.org/2003/instance}pure")
qnXbrliShares = qname("{http://www.xbrl.org/2003/instance}shares")
qnXbrliDateUnion = qname("{http://www.xbrl.org/2003/instance}dateUnion")
link = "http://www.xbrl.org/2003/linkbase"
qnLinkLabelLink = qname("{http://www.xbrl.org/2003/linkbase}labelLink")
qnLinkLabelArc = qname("{http://www.xbrl.org/2003/linkbase}labelArc")
qnLinkLabel = qname("{http://www.xbrl.org/2003/linkbase}label")
qnLinkReferenceLink = qname("{http://www.xbrl.org/2003/linkbase}referenceLink")
qnLinkReferenceArc = qname("{http://www.xbrl.org/2003/linkbase}referenceArc")
qnLinkReference = qname("{http://www.xbrl.org/2003/linkbase}reference")
qnLinkPart = qname("{http://www.xbrl.org/2003/linkbase}part")
qnLinkFootnote = qname("{http://www.xbrl.org/2003/linkbase}footnote")
qnLinkPresentationLink = qname("{http://www.xbrl.org/2003/linkbase}presentationLink")
qnLinkCalculationLink = qname("{http://www.xbrl.org/2003/linkbase}calculationLink")
qnLinkDefinitionLink = qname("{http://www.xbrl.org/2003/linkbase}definitionLink")
gen = "http://xbrl.org/2008/generic"
qnGenLink = qname("{http://xbrl.org/2008/generic}link")
qnGenArc = qname("{http://xbrl.org/2008/generic}arc")
elementReference = "http://xbrl.org/arcrole/2008/element-reference"
genReference = "http://xbrl.org/2008/reference"
qnGenReference = qname("{http://xbrl.org/2008/reference}reference")
elementLabel = "http://xbrl.org/arcrole/2008/element-label"
genLabel = "http://xbrl.org/2008/label"
qnGenLabel = qname("{http://xbrl.org/2008/label}label")
elementLabel = "http://xbrl.org/arcrole/2008/element-label"
xbrldt = "http://xbrl.org/2005/xbrldt"
qnXbrldtHypercubeItem = qname("{http://xbrl.org/2005/xbrldt}hypercubeItem")
qnXbrldtDimensionItem = qname("{http://xbrl.org/2005/xbrldt}dimensionItem")
xbrldi = "http://xbrl.org/2006/xbrldi"
qnXbrldiExplicitMember = qname("{http://xbrl.org/2006/xbrldi}explicitMember")
xlink = "http://www.w3.org/1999/xlink"
xl = "http://www.xbrl.org/2003/XLink"
xhtml = "http://www.w3.org/1999/xhtml"
ixbrl = "http://www.xbrl.org/2008/inlineXBRL"
conceptLabel = "http://www.xbrl.org/2003/arcrole/concept-label"
conceptReference = "http://www.xbrl.org/2003/arcrole/concept-reference"
footnote = "http://www.xbrl.org/2003/role/footnote"
factFootnote = "http://www.xbrl.org/2003/arcrole/fact-footnote"
factExplanatoryFact = "http://www.xbrl.org/2009/arcrole/fact-explanatoryFact"
parentChild = "http://www.xbrl.org/2003/arcrole/parent-child"
summationItem = "http://www.xbrl.org/2003/arcrole/summation-item"
essenceAlias = "http://www.xbrl.org/2003/arcrole/essence-alias"
similarTuples = "http://www.xbrl.org/2003/arcrole/similar-tuples"
requiresElement = "http://www.xbrl.org/2003/arcrole/requires-element"
generalSpecial = "http://www.xbrl.org/2003/arcrole/general-special"
dimStartsWith = "http://xbrl.org/int/dim"
all = "http://xbrl.org/int/dim/arcrole/all"
notAll = "http://xbrl.org/int/dim/arcrole/notAll"
hypercubeDimension = "http://xbrl.org/int/dim/arcrole/hypercube-dimension"
dimensionDomain = "http://xbrl.org/int/dim/arcrole/dimension-domain"
domainMember = "http://xbrl.org/int/dim/arcrole/domain-member"
dimensionDefault = "http://xbrl.org/int/dim/arcrole/dimension-default"
usTypesStartsWith = "http://xbrl.us/us-types/"
dtrTypesStartsWith = "http://www.xbrl.org/dtr/type/"
defaultLinkRole = "http://www.xbrl.org/2003/role/link"
iso4217 = "http://www.xbrl.org/2003/iso4217"
standardLabel = "http://www.xbrl.org/2003/role/label"
genStandardLabel = "http://www.xbrl.org/2008/role/label"
documentationLabel = "http://www.xbrl.org/2003/role/documentation"
standardReference = "http://www.xbrl.org/2003/role/reference"
periodStartLabel = "http://www.xbrl.org/2003/role/periodStartLabel"
periodEndLabel = "http://www.xbrl.org/2003/role/periodEndLabel"
conceptNameLabelRole = "XBRL-concept-name" # fake label role to show concept QName instead of label
xlinkLinkbase = "http://www.w3.org/1999/xlink/properties/linkbase"

ver = "http://xbrl.org/2010/versioning-base"
vercb = "http://xbrl.org/2010/versioning-concept-basic"
verce = "http://xbrl.org/2010/versioning-concept-extended"
verrels = "http://xbrl.org/2010/versioning-relationship-sets"
veria = "http://xbrl.org/2010/versioning-instance-aspects"

# formula specs
variable = "http://xbrl.org/2008/variable"
qnVariableSet = qname("{http://xbrl.org/2008/variable}variableSet")
qnVariableVariable = qname("{http://xbrl.org/2008/variable}variable")
qnVariableFilter = qname("{http://xbrl.org/2008/variable}filter")
qnParameter = qname("{http://xbrl.org/2008/variable}parameter")
qnFactVariable = qname("{http://xbrl.org/2008/variable}factVariable")
qnGeneralVariable = qname("{http://xbrl.org/2008/variable}generalVariable")
qnPrecondition = qname("{http://xbrl.org/2008/variable}precondition")
formula = "http://xbrl.org/2008/formula"
qnFormula = qname("{http://xbrl.org/2008/formula}formula")
qnFormulaUncovered = qname("{http://xbrl.org/2008/formula}uncovered")
qnFormulaDimensionSAV = qname("{http://xbrl.org/2008/formula}DimensionSAV") #signal that dimension aspect should use SAV of this dimension
qnFormulaOccEmpty = qname("{http://xbrl.org/2008/formula}occEmpty") #signal that OCC aspect should omit the SAV values
ca = "http://xbrl.org/2008/assertion/consistency"
qnConsistencyAssertion = qname("{http://xbrl.org/2008/assertion/consistency}consistencyAssertion")
ea = "http://xbrl.org/2008/assertion/existence"
qnExistenceAssertion = qname("{http://xbrl.org/2008/assertion/existence}existenceAssertion")
va = "http://xbrl.org/2008/assertion/value"
qnValueAssertion = qname("{http://xbrl.org/2008/assertion/value}valueAssertion")
variable = "http://xbrl.org/2008/variable"
formulaStartsWith = "http://xbrl.org/arcrole/20"
equalityDefinition = "http://xbrl.org/arcrole/2008/equality-definition"
qnEqualityDefinition = qname("{http://xbrl.org/2008/variable}equalityDefinition")
variableSet = "http://xbrl.org/arcrole/2008/variable-set"
variableSetFilter = "http://xbrl.org/arcrole/2008/variable-set-filter"
variableFilter = "http://xbrl.org/arcrole/2008/variable-filter"
variableSetPrecondition = "http://xbrl.org/arcrole/2008/variable-set-precondition"
consistencyAssertionFormula = "http://xbrl.org/arcrole/2008/consistency-assertion-formula"
consistencyAssertionParameter = "http://xbrl.org/arcrole/2008/consistency-assertion-parameter"
validation = "http://xbrl.org/2008/validation"
qnAssertion = qname("{http://xbrl.org/2008/validation}assertion")
qnAssertionSet = qname("{http://xbrl.org/2008/validation}assertionSet")
assertionSet = "http://xbrl.org/arcrole/2008/assertion-set"

acf = "http://xbrl.org/2010/filter/aspect-cover"
qnAspectCover = qname("{http://xbrl.org/2010/filter/aspect-cover}aspectCover")
bf = "http://xbrl.org/2008/filter/boolean"
qnAndFilter = qname("{http://xbrl.org/2008/filter/boolean}andFilter")
qnOrFilter = qname("{http://xbrl.org/2008/filter/boolean}orFilter")
booleanFilter = "http://xbrl.org/arcrole/2008/boolean-filter"
cfi = "http://xbrl.org/2010/custom-function"
functionImplementation = "http://xbrl.org/arcrole/2010/function-implementation"
qnCustomFunctionSignature = qname("{http://xbrl.org/2008/variable}function")
qnCustomFunctionImplementation = qname("{http://xbrl.org/2010/custom-function}implementation")
crf = "http://xbrl.org/2010/filter/concept-relation"
qnConceptRelation = qname("{http://xbrl.org/2010/filter/concept-relation}conceptRelation")
cf = "http://xbrl.org/2008/filter/concept"
qnConceptName = qname("{http://xbrl.org/2008/filter/concept}conceptName")
qnConceptPeriodType = qname("{http://xbrl.org/2008/filter/concept}conceptPeriodType")
qnConceptBalance = qname("{http://xbrl.org/2008/filter/concept}conceptBalance")
qnConceptCustomAttribute = qname("{http://xbrl.org/2008/filter/concept}conceptCustomAttribute")
qnConceptDataType = qname("{http://xbrl.org/2008/filter/concept}conceptDataType")
qnConceptSubstitutionGroup = qname("{http://xbrl.org/2008/filter/concept}conceptSubstitutionGroup")
cfcn = "http://xbrl.org/2008/conformance/function"
df = "http://xbrl.org/2008/filter/dimension"
qnExplicitDimension = qname("{http://xbrl.org/2008/filter/dimension}explicitDimension")
qnTypedDimension = qname("{http://xbrl.org/2008/filter/dimension}typedDimension")
ef = "http://xbrl.org/2008/filter/entity"
qnEntityIdentifier = qname("{http://xbrl.org/2008/filter/entity}identifier")
qnEntitySpecificIdentifier = qname("{http://xbrl.org/2008/filter/entity}specificIdentifier")
qnEntitySpecificScheme = qname("{http://xbrl.org/2008/filter/entity}specificScheme")
qnEntityRegexpIdentifier = qname("{http://xbrl.org/2008/filter/entity}regexpIdentifier")
qnEntityRegexpScheme = qname("{http://xbrl.org/2008/filter/entity}regexpScheme")
function = "http://xbrl.org/2008/function"
fn = "http://www.w3.org/2005/xpath-functions"
xfi = "http://www.xbrl.org/2008/function/instance"
qnXfiRoot = qname("{http://www.xbrl.org/2008/function/instance}root")
xff = "http://www.xbrl.org/2010/function/formula"
gf = "http://xbrl.org/2008/filter/general"
qnGeneral = qname("{http://xbrl.org/2008/filter/general}general")
instances = "http://xbrl.org/2010/variable/instance"
qnInstance = qname(instances,"instances:instance")
instanceVariable = "http://xbrl.org/arcrole/2010/instance-variable"
formulaInstance = "http://xbrl.org/arcrole/2010/formula-instance"
qnStandardInputInstance = qname(instances,"instances:standard-input-instance")
qnStandardOutputInstance = qname(instances,"instances:standard-output-instance")
mf = "http://xbrl.org/2008/filter/match"
qnMatchConcept = qname("{http://xbrl.org/2008/filter/match}matchConcept")
qnMatchDimension = qname("{http://xbrl.org/2008/filter/match}matchDimension")
qnMatchEntityIdentifier = qname("{http://xbrl.org/2008/filter/match}matchEntityIdentifier")
qnMatchLocation = qname("{http://xbrl.org/2008/filter/match}matchLocation")
qnMatchPeriod = qname("{http://xbrl.org/2008/filter/match}matchPeriod")
qnMatchSegment = qname("{http://xbrl.org/2008/filter/match}matchSegment")
qnMatchScenario = qname("{http://xbrl.org/2008/filter/match}matchScenario")
qnMatchNonXDTSegment = qname("{http://xbrl.org/2008/filter/match}matchNonXDTSegment")
qnMatchNonXDTScenario = qname("{http://xbrl.org/2008/filter/match}matchNonXDTScenario")
qnMatchUnit = qname("{http://xbrl.org/2008/filter/match}matchUnit")
msg = "http://xbrl.org/2010/message"
qnMessage = qname("{http://xbrl.org/2010/message}message")
assertionSatisfiedMessage = "http://xbrl.org/arcrole/2010/assertion-satisfied-message"
assertionUnsatisfiedMessage = "http://xbrl.org/arcrole/2010/assertion-unsatisfied-message"
standardMessage = "http://www.xbrl.org/2010/role/message"
terseMessage = "http://www.xbrl.org/2010/role/terseMessage"
verboseMessage = "http://www.xbrl.org/2010/role/verboseMessage"
pf = "http://xbrl.org/2008/filter/period"
qnPeriod = qname("{http://xbrl.org/2008/filter/period}period")
qnPeriodStart = qname("{http://xbrl.org/2008/filter/period}periodStart")
qnPeriodEnd = qname("{http://xbrl.org/2008/filter/period}periodEnd")
qnPeriodInstant = qname("{http://xbrl.org/2008/filter/period}periodInstant")
qnForever = qname("{http://xbrl.org/2008/filter/period}forever")
qnInstantDuration = qname("{http://xbrl.org/2008/filter/period}instantDuration")
registry = "http://xbrl.org/2008/registry"
rf = "http://xbrl.org/2008/filter/relative"
qnRelativeFilter = qname("{http://xbrl.org/2008/filter/relative}relativeFilter")
ssf = "http://xbrl.org/2008/filter/segment-scenario"
qnSegmentFilter = qname("{http://xbrl.org/2008/filter/segment-scenario}segment")
qnScenarioFilter = qname("{http://xbrl.org/2008/filter/segment-scenario}scenario")
tf = "http://xbrl.org/2008/filter/tuple"
qnAncestorFilter = qname("{http://xbrl.org/2008/filter/tuple}ancestorFilter")
qnLocationFilter = qname("{http://xbrl.org/2008/filter/tuple}locationFilter")
qnParentFilter = qname("{http://xbrl.org/2008/filter/tuple}parentFilter")
qnSiblingFilter = qname("{http://xbrl.org/2008/filter/tuple}siblingFilter")
uf = "http://xbrl.org/2008/filter/unit"
qnSingleMeasure = qname("{http://xbrl.org/2008/filter/unit}singleMeasure")
qnGeneralMeasures = qname("{http://xbrl.org/2008/filter/unit}generalMeasures")
vf = "http://xbrl.org/2008/filter/value"
qnNilFilter = qname("{http://xbrl.org/2008/filter/value}nil")
qnPrecisionFilter = qname("{http://xbrl.org/2008/filter/value}precision")
xpath2err = "http://www.w3.org/2005/xqt-errors"

euRend = "http://www.eurofiling.info/2010/rendering"
euTableAxis = "http://www.eurofiling.info/arcrole/2010/table-axis"
euAxisMember = "http://www.eurofiling.info/arcrole/2010/axis-member"
qnEuTable = qname("{http://www.eurofiling.info/2010/rendering}table")
qnEuAxisCoord = qname("{http://www.eurofiling.info/2010/rendering}axisCoord")

errMsgPrefixNS = {
    "err": xpath2err,
    "xbrldte": "http://xbrl.org/2005/xbrldt/errors",
    "xbrldie": "http://xbrl.org/2005/xbrldi/errors",
    "xbrlfe": "http://xbrl.org/2008/formula/error",
    "xbrlmsge": "http://xbrl.org/2010/message/error",
    "xbrlvarinste": "http://xbrl.org/2010/variable/instance/error",
    "xbrlve": "http://xbrl.org/2008/variable/error",
    "xbrlcae": "http://xbrl.org/2008/assertion/consistency/error",
    "xbrleae": "http://xbrl.org/2008/assertion/existence/error",
    "xbrldfe": "http://xbrl.org/2008/filter/dimension/error",  
    "xffe": "http://www.xbrl.org/2010/function/formula/error",
    "xfie": "http://www.xbrl.org/2008/function/instance/error",
    "verrelse": "http://xbrl.org/2010/versioning-relationship-sets/error",
    "xbrlacfe": "http://xbrl.org/2010/filter/aspect-cover/error",
    "xbrlcfie": "http://xbrl.org/2010/custom-function/error",
    }

def baseSetArcroleLabel(arcrole): # with sort char in first position
    if arcrole == "XBRL-dimensions": return _("1Dimension")
    if arcrole == "XBRL-formulae": return _("1Formula")
    if arcrole == "EU-rendering": return _("1Rendering")
    if arcrole == parentChild: return _("1Presentation")
    if arcrole == summationItem: return _("1Calculation")
    return "2" + os.path.basename(arcrole).title()

def labelroleLabel(role): # with sort char in first position
    if role == standardLabel: return _("1Standard Label")
    elif role == conceptNameLabelRole: return _("0Name")
    return "3" + os.path.basename(role).title()

def isStandardNamespace(namespaceURI):
    return namespaceURI in {xsd, xbrli, link, gen, xbrldt, xbrldi}

def isNumericXsdType(xsdType):
    return xsdType in {"integer", "positiveInteger", "negativeInteger", "nonNegativeInteger", "nonPositiveInteger",
                       "long", "unsignedLong", "int", "unsignedInt", "short", "unsignedShort",
                       "byte", "unsignedByte", "decimal", "float", "double"}
    
def isStandardRole(role):
    return role in {"http://www.xbrl.org/2003/role/label",
                    "http://www.xbrl.org/2003/role/terseLabel",
                    "http://www.xbrl.org/2003/role/verboseLabel",
                    "http://www.xbrl.org/2003/role/link",
                    "http://www.xbrl.org/2003/role/positiveLabel",
                    "http://www.xbrl.org/2003/role/positiveTerseLabel",
                    "http://www.xbrl.org/2003/role/positiveVerboseLabel",
                    "http://www.xbrl.org/2003/role/negativeLabel",
                    "http://www.xbrl.org/2003/role/negativeTerseLabel",
                    "http://www.xbrl.org/2003/role/negativeVerboseLabel",
                    "http://www.xbrl.org/2003/role/zeroLabel",
                    "http://www.xbrl.org/2003/role/zeroTerseLabel",
                    "http://www.xbrl.org/2003/role/zeroVerboseLabel",
                    "http://www.xbrl.org/2003/role/totalLabel",
                    "http://www.xbrl.org/2003/role/periodStartLabel",
                    "http://www.xbrl.org/2003/role/periodEndLabel",
                    "http://www.xbrl.org/2003/role/documentation",
                    "http://www.xbrl.org/2003/role/definitionGuidance",
                    "http://www.xbrl.org/2003/role/disclosureGuidance",
                    "http://www.xbrl.org/2003/role/presentationGuidance",
                    "http://www.xbrl.org/2003/role/measurementGuidance",
                    "http://www.xbrl.org/2003/role/commentaryGuidance",
                    "http://www.xbrl.org/2003/role/exampleGuidance",
                    "http://www.xbrl.org/2003/role/reference",
                    "http://www.xbrl.org/2003/role/definitionRef",
                    "http://www.xbrl.org/2003/role/disclosureRef",
                    "http://www.xbrl.org/2003/role/mandatoryDisclosureRef",
                    "http://www.xbrl.org/2003/role/recommendedDisclosureRef",
                    "http://www.xbrl.org/2003/role/unspecifiedDisclosureRef",
                    "http://www.xbrl.org/2003/role/presentationRef",
                    "http://www.xbrl.org/2003/role/measurementRef",
                    "http://www.xbrl.org/2003/role/commentaryRef",
                    "http://www.xbrl.org/2003/role/exampleRef",
                    "http://www.xbrl.org/2003/role/calculationLinkbaseRef",
                    "http://www.xbrl.org/2003/role/definitionLinkbaseRef",
                    "http://www.xbrl.org/2003/role/labelLinkbaseRef",
                    "http://www.xbrl.org/2003/role/presentationLinkbaseRef",
                    "http://www.xbrl.org/2003/role/referenceLinkbaseRef",
                    "http://www.xbrl.org/2003/role/footnote"}

def isStandardArcrole(role):
    return role in {"http://www.w3.org/1999/xlink/properties/linkbase",
                    "http://www.xbrl.org/2003/arcrole/concept-label",
                    "http://www.xbrl.org/2003/arcrole/concept-reference",
                    "http://www.xbrl.org/2003/arcrole/fact-footnote",
                    "http://www.xbrl.org/2003/arcrole/parent-child",
                    "http://www.xbrl.org/2003/arcrole/summation-item",
                    "http://www.xbrl.org/2003/arcrole/general-special",
                    "http://www.xbrl.org/2003/arcrole/essence-alias",
                    "http://www.xbrl.org/2003/arcrole/similar-tuples",
                    "http://www.xbrl.org/2003/arcrole/requires-element"}
    
standardArcroleCyclesAllowed = { 
                    "http://www.xbrl.org/2003/arcrole/concept-label":("any", None),
                    "http://www.xbrl.org/2003/arcrole/concept-reference":("any", None),
                    "http://www.xbrl.org/2003/arcrole/fact-footnote":("any",None),
                    "http://www.xbrl.org/2003/arcrole/parent-child":("undirected", "5.2.4.2"),
                    "http://www.xbrl.org/2003/arcrole/summation-item":("any", "5.2.5.2"),
                    "http://www.xbrl.org/2003/arcrole/general-special":("undirected", "5.2.6.2.1"),
                    "http://www.xbrl.org/2003/arcrole/essence-alias":("undirected", "5.2.6.2.1"),
                    "http://www.xbrl.org/2003/arcrole/similar-tuples":("any", "5.2.6.2.3"),
                    "http://www.xbrl.org/2003/arcrole/requires-element":("any", "5.2.6.2.4")}

def standardArcroleArcElement(arcrole):
    return {"http://www.xbrl.org/2003/arcrole/concept-label":"labelArc",
            "http://www.xbrl.org/2003/arcrole/concept-reference":"referenceArc",
            "http://www.xbrl.org/2003/arcrole/fact-footnote":"footnoteArc",
            "http://www.xbrl.org/2003/arcrole/parent-child":"presentationArc",
            "http://www.xbrl.org/2003/arcrole/summation-item":"calculationArc",
            "http://www.xbrl.org/2003/arcrole/general-special":"definitionArc",
            "http://www.xbrl.org/2003/arcrole/essence-alias":"definitionArc",
            "http://www.xbrl.org/2003/arcrole/similar-tuples":"definitionArc",
            "http://www.xbrl.org/2003/arcrole/requires-element":"definitionArc"}[arcrole]
            
def isStandardOrXdtArcrole(arcrole):
    return isDimensionArcrole(arcrole) or arcrole in {
            "http://www.xbrl.org/2003/arcrole/general-special",
            "http://www.xbrl.org/2003/arcrole/essence-alias",
            "http://www.xbrl.org/2003/arcrole/similar-tuples",
            "http://www.xbrl.org/2003/arcrole/requires-element"}

def isStandardResourceOrExtLinkElement(element):
    return element.namespaceURI == link and element.localName in (
          "definitionLink", "calculationLink", "presentationLink", "labelLink", "referenceLink", "footnoteLink", 
          "label", "footnote", "reference")
    
def isStandardArcElement(element):
    return element.namespaceURI == link and element.localName in (
          "definitionArc", "calculationArc", "presentationArc", "labelArc", "referenceArc", "footnoteArc")
        
def isStandardArcInExtLinkElement(element):
    return isStandardArcElement(element) and isStandardResourceOrExtLinkElement(element.parentNode)
        
def isStandardExtLinkQname(qName):
    return qName in (
          qname("{http://www.xbrl.org/2003/linkbase}definitionLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}calculationLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}presentationLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}labelLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}referenceLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}footnoteLink"), 
          qname("{http://www.xbrl.org/2003/linkbase}label"), 
          qname("{http://www.xbrl.org/2003/linkbase}footnote"), 
          qname("{http://www.xbrl.org/2003/linkbase}reference"))
    
standardExtLinkQnames = {qname("{http://www.xbrl.org/2003/linkbase}definitionLink"), 
                         qname("{http://www.xbrl.org/2003/linkbase}calculationLink"), 
                         qname("{http://www.xbrl.org/2003/linkbase}presentationLink"), 
                         qname("{http://www.xbrl.org/2003/linkbase}labelLink"),     
                         qname("{http://www.xbrl.org/2003/linkbase}referenceLink"), 
                         qname("{http://www.xbrl.org/2003/linkbase}footnoteLink")} 

def isStandardArcQname(qName):
    return qName in {
          qname("{http://www.xbrl.org/2003/linkbase}definitionArc"), 
          qname("{http://www.xbrl.org/2003/linkbase}calculationArc"), 
          qname("{http://www.xbrl.org/2003/linkbase}presentationArc"), 
          qname("{http://www.xbrl.org/2003/linkbase}labelArc"),
          qname("{http://www.xbrl.org/2003/linkbase}referenceArc"), 
          qname("{http://www.xbrl.org/2003/linkbase}footnoteArc")}
    
def isDimensionArcrole(arcrole):
    return arcrole.startswith("http://xbrl.org/int/dim/arcrole/")

def isEuRenderingArcrole(arcrole):
    return arcrole in (euTableAxis, euAxisMember)
   
def isFormulaArcrole(arcrole):
    return arcrole in {"http://xbrl.org/arcrole/2008/assertion-set",
                       "http://xbrl.org/arcrole/2008/variable-set",
                       "http://xbrl.org/arcrole/2008/variable-set-filter",
                       "http://xbrl.org/arcrole/2008/variable-filter",
                       "http://xbrl.org/arcrole/2008/boolean-filter",
                       "http://xbrl.org/arcrole/2008/variable-set-precondition",
                       "http://xbrl.org/arcrole/2008/consistency-assertion-formula",
                       "http://xbrl.org/arcrole/2010/function-implementation",
                       "http://xbrl.org/arcrole/2010/assertion-satisfied-message",
                       "http://xbrl.org/arcrole/2010/assertion-unsatisfied-message",
                       "http://xbrl.org/arcrole/2010/instance-variable",
                       "http://xbrl.org/arcrole/2010/formula-instance",
                       "http://xbrl.org/arcrole/2010/function-implementation"}
