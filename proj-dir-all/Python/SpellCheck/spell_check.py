########################################################################################
#
# Description: The following code reads data from an excel file and conducts spell check
#              and spacing checks on the job description column
# 
# Date: 5/5/2023
#
# Contact: Attulya Pratap Gupta
#          guptaatt@msu.edu
#
#########################################################################################

#Importing basic packages for use in the program
import re
import pandas as pd
from spellchecker import SpellChecker
import time

#Importing nltk packages for use in the program
'''
All the packages below have to be downloaaded for use. Use the command:
nltk.download('all') to avoid downloading each corpus individually
All packages here are already installed through jupyter notebook
'''
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import reuters
from nltk.corpus import treebank
from nltk.corpus import wordnet
from nltk.corpus import ConllCorpusReader

#Importing the python language tool
import language_tool_python

#Creating an object of the language tool
language_tool = language_tool_python.LanguageTool('en-US')

#Creating an object of the pyspellchecker package
spell = SpellChecker()

#Creating a list of unique words from the corpora
word_list = list(set(word.lower() for word in nltk.corpus.words.words()))
brown_list = list(set(word.lower() for word in nltk.corpus.brown.words()))
webtext_list = list(set(word.lower() for word in nltk.corpus.webtext.words()))
reuters_list = list(set(nltk.corpus.reuters.words()))
gutenberg_list = list(set(nltk.corpus.gutenberg.words()))
treebank_list = list(set(nltk.corpus.treebank.words()))

wordnet_set = set()

for synset in wordnet.all_synsets():
    for lemma in synset.lemmas():
        wordnet_set.add(lemma.name())
wordnet_list = list(wordnet_set)

conll_list = list(set(word.lower() for sent in nltk.corpus.conll2000.tagged_sents() for (word, pos) in sent))

#Adding all the custom made lists

#Extracted Certifications Data
masters_abv = ['MAcc', 'MAc', 'MAcy', 'M.A.S.', 'M.Econ', 'MASc', 'MAppSc', 'MApplSc', 'M.A.Sc.', 'MAS', 'M.Arch.', 'M.A.', 'MA', 'A.M.', 'AM', 'MAT', 'MA', 'ALM', 'MLA', 'MLS', 'MALS', 'MBA', 'M.B.A.', 'MBus', 'MBI', 'MChem', 'Master of City Planning', 'MCom', 'MComm', 'Master of Computational Finance', 'MCA', 'MCJ', 'Master in Creative Technologies', 'MDes', 'M.Des.', 'M.Design', 'M.Div.', 'M.Econ.', 'M.Ed.', 'MEd', 'Ed.M.', 'M.A.Ed.', 'M.S.Ed.', 'M.S.E.', 'M.Ed.L', 'M.Eng.', 'ME', 'MEng', 'MEM', 'M.Ent.', 'LL.M. Eur', 'M.Fin.', 'Master of Financial Economics', 'Master of Financial Engineering', 'Master of Financial Mathematics', 'MFA', 'M.F.A.', 'MHA', 'MHS', 'MH', 'MILR', 'Master of International Affairs', 'Master of International Business', 'Masters in International Economics', 'MIS', 'M.ISM', 'MS.IM', 'M.IS', 'MSIT', 'MScIT', 'M.Sc.IT', 'MSc.IT', 'M.Sc IT.', 'M.J.', 'M.Jur', 'LL.M.', 'LLM', 'M.S.L.', 'MLitt', 'MLIS', 'MM', 'Master of Mathematical Finance', 'MMath', 'Master of Medical Science', 'M.M.', 'M.Mus.', 'OT', 'MPharm', 'M.Phil.', 'Master of Physician Assistant Studies', 'MPhys', 'Master of Political Science', 'MPS', 'M.P.S.', 'MPA', 'M.P.Aff.', 'M.P.H.', 'M.P.P.', 'Master of Public Management', 'Master of Quantitative Finance', 'MRb', 'Master of Real Estate Development', 'Master of Religious Education', 'MSc(R)', 'MSM', 'S.T.M.', 'M.Sc.', 'MSc', 'M.Sci.', 'M.Si.', 'Sc.M.', 'M.S.', 'MS', 'Mag.', 'Mg.', 'Mgr', 'S.M.', 'SM', 'Master of Science in Education', 'MSE', 'HRD', 'MSHRD', 'MSIS', 'MSMIS', 'MSIT', 'MScIT', 'M.Sc.IT', 'MSc.IT', 'M.Sc IT.', 'MSL', 'MSc', 'Master of Science in Nursing', 'M.S.P.M.', 'SCM', 'MSSCM', 'MST', 'Master of Science in Taxation', 'MSSc', 'MSW', 'M.St.', 'MSt', 'Ch.M.', 'M.Th.', 'M.T.S.', 'Master of Urban Planning', 'MVSC', 'MVSc.']
ass_abv =['AA', 'AE','ACLS', 'ASN', 'AS', 'AF', 'AT', 'AAA', 'AAB', 'AAS', 'AAT', 'ABA', 'ABS', 'ADN', 'AES', 'AET', 'AFA', 'AGS', 'AIT', 'AOS', 'AOT', 'APE', 'APS', 'ASPT-APT']
bchlrs_abv = ['BArch', 'BDes','BRN', 'BA','BLS', 'AB', 'BS', 'BSc', 'SB', 'ScB', 'BAA', 'BAAS', 'BEng', 'BE', 'BSE', 'BESc', 'BSEng', 'BASc', 'BTech', 'BSc(Eng)', 'AMIE', 'GradIETE', 'B.Tech.', 'BSET', 'BBA', 'BIBE', 'BSBA', 'BMS', 'Bachelor of Administrative Studies', 'BC...achelor of Theology', 'Th.B.', 'BTheol', 'BRS', 'BRE', 'BFA', 'BF&TV', 'BIS', 'BJ', 'BAJ', 'BSJ', 'BJourn', 'BLArch', 'B.L.A.', 'A.L.B.', 'BGS', 'BSGS', 'BAS', 'Bachelor of Liberal Studies', 'BPS', 'B.L.S.', 'B.Lib.', 'B.L.I.S.', 'BM', 'BMus', 'BA in Music']

#Extracting abbreviations for job postings in each industry
exec_abv = ['Exec','Assoc Dir', 'CAO', 'CEO', 'CDO', 'CFO', 'Chair', 'CHRO', 'CIO', 'CLO', 'CMO', 'COO', 'CPO', 'CSO', 'CTO', 'Dir', 'ED', 'EVP', 'MD', 'MP', 'Pres', 'SGT', 'SUPR', 'Supe', 'VC', 'VP', 'VP of TA', 'VP of TM']
mng_abv = ['AM', 'AM', 'AMB', 'Acct Mgr', 'EAM', 'HRM', 'PM', 'Sr Mgr', 'Ter Mgr']
asst_abv = ['Admin Asst', 'Asst', 'Exec Asst', 'EA', 'PA', 'VA', 'AA', 'AASA', 'AD', 'AVP']
egr_abv = ['AE', 'Aero Eng', 'CE','C/E', 'Chem Engr', 'Cloud Ops Eng', 'CNE', 'Comp Engr', 'Electr Eng', 'Environ Engr', 'Eng', 'Engr', 'Jr Engr', 'Manuf Eng', 'Mech Engr', 'Prof Engr', 'Sr. AE', 'Struct Eng', 'SWE', 'UI Eng']
swe_abv = ['BE Developer', 'Dev', 'FE Developer', 'JS Developer', "Jr", "JR"]
sales_abv = ['AE', "BDM", "BDR", "Sales Rep", "SDR"]
design_abv = ['Art Dir', 'Creative Dir', 'UI Designer', 'UX Designer']
corp_abv = ['AAMS', 'Admin', 'ADV', 'Acct', 'Agt', 'Anlst', 'APR', 'Assoc', 'Assoc Prof', 'ATTD', 'CFP', 'CHANC', 'Coord', 'CPA', 'CSM', 'CSR', 'DA', 'DEVL', 'DSGN', 'ELEC', 'FAC', 'GC', 'HRBP', 'INSP', 'INSTR', 'INT', 'IT', 'JR', 'LEC', 'LIBR', 'MACH', 'MECH', 'Mkg', 'Mkt', 'Mktg', 'Off', 'OPER', 'PM', 'PRIN', 'PRO', 'Prof', 'Prog', 'Rep', 'ROR Dev', 'QA Analyst', 'Sales Assoc', 'SM Spec', 'Spec', 'Specl', 'Sr', 'Tech', 'TRNE', 'TRNR', 'UX Des']
judge_abv = ['ALJ', 'Arb', 'Assemb', 'AG', 'Atty Gen', 'B.', 'C.B.', 'C.J.', 'J', 'J.J.', 'Mag', 'Med', 'Sen']
nurse_abv = ['APRN', 'APRN-NP', 'APRN-FNP', 'APRN-ANP', 'ANP', 'CANP', 'ANP-BC','APRN-AGACNP', 'APRN-PNP', 'APRN-CNM', 'ACNP-BC', 'ACRN', 'ALNC', 'CLNC','AOCN', 'AOCN', 'AOCNP', 'AOCNS', 'APN', 'APNP', 'ARNP', 'CAPA', 'CAPA','CARN', 'CCCN', 'CCNS', 'CCNS', 'CCRN', 'CCTN','CCTRN']
nurse_abv_2 = ['CDDN', 'CDN', 'CDONA/LTC', 'CEN', 'CETN', 'CFCN', 'CFN', 'CFNP', 'CFRN', 'CGN', 'CGRN', 'CHN', 'CHPN', 'CHRN', 'CLPNI', 'CMCN', 'CMSRN', 'CNA', 'CNDLTC', 'CNI', 'CNLCP', 'CNN', 'CNNP', 'CNO', 'CNP', 'CNRN', 'CND', 'CNSN', 'COCN', 'COHN', 'COHN-S', 'COHN-S/CM', 'CORLN', 'CORN', 'CPAN', 'CPSN', 'CPN', 'CPNA', 'CPNL', 'CPNP', 'CPON', 'CPSN', 'CRN', 'CRNA', 'CRNH', 'CRNI', 'CRNI', 'CRNL', 'CRNO', 'CRNP', 'CRRN', 'CRRN-a', 'CSN', 'CTN', 'CTRN', 'CUCNS', 'CUNP', 'CURN', 'CVN', 'CWCN', 'CWOCN', 'DNC', 'DON', 'EN', 'ENP', 'FAAN', 'FAEN', 'IPN', 'LNC', 'LNCC', 'LSN', 'LVN', 'LVN', 'MHN', 'MICN', 'MN', 'MSN', 'NCSN', 'NE-BC', 'NEA-BC', 'NIC', 'NMT', 'NNP', 'NP', 'NPC', 'NPP', 'OCN', 'OGNP', 'OHNCS', 'ONC', 'PCCN', 'PCNS', 'PHN', 'PHRN', 'PMHCNS', 'PMHNP', 'PNP', 'RIPRN', 'RN', 'RN,C', 'RN-BC', 'RNA', 'RNC', 'RNCS', 'RNCS', 'RNFA', 'RNP', 'RPN', 'SANE-A', 'SANE-', 'SEN', 'SHN', 'SN', 'SPN', 'TNP', 'TNS', 'WHNP', 'WOCN']
doc_abv = ['C-SPI', 'ChD', 'DO', 'DPM', 'DCH', 'DM', 'DME', 'DMSc', 'Dmt', 'DN', 'DNE', 'DNP', 'DNS', 'DNSc', 'DO', 'DOs', 'DP', 'DPH', 'DPHN', 'DrNP', 'DRPH', 'DSW', 'LRCS', 'MBBS', 'MD', 'MD', 'ME', 'MRCP', 'MRCS', 'MS', 'MSc', 'MSurg', 'NCT', 'ND', 'OD']
med_abv = ["PA", "PA-C", "CLA", "CMA", "CMA-A", "CMA-C", "CNA", "CNA-A", "COMA", "COTA", "CRNFA", "MPAS", "MRL", "MTA", "OTA", "PTA", "RMA", "CDA", "DA", "DDS", "DDSC", "DMD", "FACD", "FAGD", "FDS", "MDS", "MSD", "RDA", "RDH", "PH", "RPh", "Phar", "Pharm", "Pharm. D.", "PharmD"]

#Extracted Computer terms data
comp_terms = []
comp_abv = []

with open('comp_soft_it_terms.txt', 'r') as f:
    # Read the entire contents of the file into a string
    terms = f.read()
    terms = terms.split('\n')
    #Split the text into abbreviations and terms
    for line in terms:
        sub_parts= line.split("  ")
        abv = sub_parts[0].strip()
        if(abv ==''):
            continue
        if ':' in abv:
            index = abv.find(':')
            abv = abv[:index]
        comp_abv.append(abv)
f.close()

with open('Computer_related_terms.txt', 'r') as file:
    # Read the entire contents of the file into a string
    text = file.read()
    text = text.split('\n')

    for line in text:
        index = line.find('â€”')
        line = line[:index]
        comp_terms.append(line)

file.close()

more_terms = []
with open('more_comp_terms.txt', 'r') as file:
    # Read the entire contents of the file into a string
    text = file.read()
    text = text.split('\n')
    for line in text:
        line  = line.split()
        more_terms += [element for element in line]

#Adding all the custom made lists to the pyspellchecker dictionary
all_lists = [exec_abv, masters_abv, ass_abv, bchlrs_abv, mng_abv, asst_abv, swe_abv, egr_abv, sales_abv, design_abv, corp_abv, judge_abv, nurse_abv, nurse_abv_2, doc_abv, med_abv, comp_terms, comp_abv, word_list, brown_list, webtext_list, gutenberg_list,more_terms, wordnet_list, reuters_list, treebank_list, conll_list]
for ind_list in all_lists:
    spell.word_frequency.load_words(ind_list)


# CREATING SMALLER FUNCTIONS FOR USAGE

def is_correct(ind):
    '''
    Input: string
    Output: boolean (true/false)

    Takes in a token and checks if it is in any of the custom made lists
    '''
    all_lists = [exec_abv, masters_abv, ass_abv, bchlrs_abv, mng_abv, asst_abv, swe_abv, egr_abv, sales_abv, design_abv, corp_abv, judge_abv, nurse_abv, nurse_abv_2, doc_abv, med_abv, comp_terms, comp_abv, word_list, brown_list, webtext_list, gutenberg_list, wordnet_list, reuters_list, treebank_list, conll_list]
    for lst in all_lists:
        if ind in lst:
            return True
    return False

def is_roman_numeral(token):
    '''
    Input: string
    Output: boolean (true/false)

    Checks if a particular string is a roman numeral
    '''
    #Defining a set for roman numerals
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Check if the input token is a valid Roman numeral
    if all(c in roman_numerals for c in token):
        # Convert the Roman numeral to an integer
        total = 0
        prev = None
        for c in token:
            if prev and roman_numerals[c] > roman_numerals[prev]:
                total += roman_numerals[c] - 2 * roman_numerals[prev]
            else:
                total += roman_numerals[c]
            prev = c

        # Check if the integer value of the Roman numeral is between 1 and 3999
        if 1 <= total <= 3999:
            return True

    return False

def special_string(string):
    '''
    Input: string
    Output: boolean (true/false)

    Checks if a particular string is a pattern
    '''
    pattern = r'^[\d\W]+$'
    return bool(re.match(pattern, string))

def pycheck(string):
    '''
    Input: string
    Output: boolean (true/false)

    Checks if a particular string can be corrected using pyspellchecker
    '''
    cw = spell.correction(string)
    if cw == None:
        return False
    if(cw.lower()==string.lower()):
        return True
    return False

def correct_grammar_and_spacing(text):
    '''
    Input: string
    Output: string

    The following function takes in a string and corrects all whitespace, grammatical and typographical errors in the text
    '''
    matches = language_tool.check(text)
    # Only correct grammar and spacing errors, not spelling errors
    matches = [match for match in matches if match.ruleIssueType in ['whitespace', 'grammar', 'typographical']]
    return language_tool_python.utils.correct(text, matches)

def spell_check(test_string):
    '''
    Input: string
    Output: string

    The following function is PRIMARY function of the program that calls all necessary functions and return the corrected job description
    '''
    #Creatig a lambda function to check for misspellings
    is_correctly_spelled = lambda rule: rule.ruleIssueType == 'misspelling' and pycheck(rule.matchedText)
    matches = language_tool.check(test_string)
    
    #Creating empty variables for storing values
    new_matches = []
    to_correct = []
    
    #Iterating through the errors in the text
    for rule in matches:
        #Checking for misspelling and if word is present in the LanguageTool vocabulary
        if not is_correctly_spelled(rule):
            #Checking for specific terms
            if rule.matchedText.isupper()==False:
                new_matches.append(rule)
        else:
            #List of words that are wrongly written
            to_correct.append(rule.matchedText)

    matches = new_matches
    #Conducting prelimnary corrections
    test_string = language_tool_python.utils.correct(test_string, matches)
    
    all_tokens = nltk.word_tokenize(test_string)
    new_tokens = []
    for token in all_tokens:
        if token in to_correct:
            #Conducting spell checks
            token = spell.correction(token)
        new_tokens.append(token)
        
    text = " ".join(new_tokens)
    #Conducting spacing and grammatical checks
    test_string = correct_grammar_and_spacing(text)
    return test_string

#Reading the csv file as a pandas dataframe
postings = pd.read_csv("jobdec_sd_cw.csv")

#Extracting the job descriptions
job_descriptions = postings['job_desc']

#Creating an empty list to store the corrected job descriptions
correct_desc = []

#Starting the time clock to measure time
start_time = time.time()

#Initializing a counter to track progress in terminal
counter = 1

#Iterating through the job descriptions
for desc in job_descriptions:
    #Checking if the job description is a string
    if isinstance(desc, str):
        #Conducting spell checks and grammar checks
        correct_desc.append(spell_check(desc))
    else:
        correct_desc.append(desc)
    #Keeping check of progress in the terminal
    if(counter%500==0):
        print(counter)
    counter+=1

#Appending the new column to the pandas dataframe
postings.insert(loc = 4, column = 'Corrected_Desc', value = correct_desc)

#Saving the newly created datafrmae as a .csv file
postings.to_csv('corrected.csv', index=False)

#Calculating the time taken
end_time = time.time()

#Printing the time taken
print(end_time-start_time)