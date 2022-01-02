
# -*-coding: utf-8 -*-

import fileinput
import re
import sys

filename = sys.argv[1]

outfile = open(filename+".dative", "w")

for line in fileinput.input():
    # URU
    # AG

    line = re.sub(' ag an bh', ' ag an mb', line.rstrip())
    line = re.sub(' ag an b', ' ag an mb', line.rstrip())

    line = re.sub(' ag an gh', ' ag an ng', line.rstrip())
    line = re.sub(' ag an g', ' ag an ng', line.rstrip())

    line = re.sub(' ag an ch', ' ag an gc', line.rstrip())
    line = re.sub(' ag an c', ' ag an gc', line.rstrip())

    line = re.sub(' ag an fh', ' ag an bhf', line.rstrip())
    line = re.sub(' ag an f', ' ag an bhf', line.rstrip())

    line = re.sub(' ag an ph', ' ag an bp', line.rstrip())
    line = re.sub(' ag an p', ' ag an bp', line.rstrip())

    line = re.sub(' ag an t-', ' ag an ', line.rstrip())
    

    # AR
    line = re.sub(' ar an bh', ' ar an mb', line.rstrip())
    line = re.sub(' ar an b', ' ar an mb', line.rstrip())

    line = re.sub(' ar an gh', ' ar an ng', line.rstrip())
    line = re.sub(' ar an g', ' ar an ng', line.rstrip())

    line = re.sub(' ar an ch', ' ar an gc', line.rstrip())
    line = re.sub(' ar an c', ' ar an gc', line.rstrip())

    line = re.sub(' ar an fh', ' ar an bhf', line.rstrip())
    line = re.sub(' ar an f', ' ar an bhf', line.rstrip())

    line = re.sub(' ar an ph', ' ar an bp', line.rstrip())
    line = re.sub(' ar an p', ' ar an bp', line.rstrip())

    line = re.sub(' ar an t-', ' ar an ', line.rstrip())

    # AS
    line = re.sub(' as an bh', ' as an mb', line.rstrip())
    line = re.sub(' as an b', ' as an mb', line.rstrip())

    line = re.sub(' as an gh', ' as an ng', line.rstrip())
    line = re.sub(' as an g', ' as an ng', line.rstrip())

    line = re.sub(' as an ch', ' as an gc', line.rstrip())
    line = re.sub(' as an c', ' as an gc', line.rstrip())

    line = re.sub(' as an fh', ' as an bhf', line.rstrip())
    line = re.sub(' as an f', ' as an bhf', line.rstrip())

    line = re.sub(' as an ph', ' as an bp', line.rstrip())
    line = re.sub(' as an p', ' as an bp', line.rstrip())

    line = re.sub(' as an t-', ' as an ', line.rstrip())
    
    # CHUIG
    line = re.sub(' chuig an bh', ' chuig an mb', line.rstrip())
    line = re.sub(' chuig an b', ' chuig an mb', line.rstrip())

    line = re.sub(' chuig an gh', ' chuig an ng', line.rstrip())
    line = re.sub(' chuig an g', ' chuig an ng', line.rstrip())

    line = re.sub(' chuig an ch', ' chuig an gc', line.rstrip())
    line = re.sub(' chuig an c', ' chuig an gc', line.rstrip())

    line = re.sub(' chuig an fh', ' chuig an bhf', line.rstrip())
    line = re.sub(' chuig an f', ' chuig an bhf', line.rstrip())

    line = re.sub(' chuig an ph', ' chuig an bp', line.rstrip())
    line = re.sub(' chuig an p', ' chuig an bp', line.rstrip())

    line = re.sub(' chuig an t-', ' chuig an ', line.rstrip())



    # FAOI
    line = re.sub(' faoin bh', ' faoin mb', line.rstrip())
    line = re.sub(' faoin b', ' faoin mb', line.rstrip())

    line = re.sub(' faoin gh', ' faoin ng', line.rstrip())
    line = re.sub(' faoin g', ' faoin ng', line.rstrip())

    line = re.sub(' faoin ch', ' faoin gc', line.rstrip())
    line = re.sub(' faoin c', ' faoin gc', line.rstrip())

    line = re.sub(' faoin fh', ' faoin bhf', line.rstrip())
    line = re.sub(' faoin f', ' faoin bhf', line.rstrip())

    line = re.sub(' faoin ph', ' faoin bp', line.rstrip())
    line = re.sub(' faoin p', ' faoin bp', line.rstrip())

    line = re.sub(' faoin t-', ' faoin ', line.rstrip())

    # I

    line = re.sub(' i fh', ' i bhf', line.rstrip())
    line = re.sub(' i f', ' i bhf', line.rstrip())
    
    line = re.sub(' i bh', ' i mb', line.rstrip())
    line = re.sub(' i b', ' i mb', line.rstrip())

    line = re.sub(' i gh', ' i ng', line.rstrip())
    line = re.sub(' i g', ' i ng', line.rstrip())

    line = re.sub(' i ch', ' i gc', line.rstrip())
    line = re.sub(' i c', ' i gc', line.rstrip())

    line = re.sub(' i ph', ' i bp', line.rstrip())
    line = re.sub(' i p', ' i bp', line.rstrip())
    


    # LE
    line = re.sub(' leis an bh', ' leis an mb', line.rstrip())
    line = re.sub(' leis an b', ' leis an mb', line.rstrip())

    line = re.sub(' leis an gh', ' leis an ng', line.rstrip())
    line = re.sub(' leis an g', ' leis an ng', line.rstrip())

    line = re.sub(' leis an ch', ' leis an gc', line.rstrip())
    line = re.sub(' leis an c', ' leis an gc', line.rstrip())

    line = re.sub(' leis an fh', ' leis an bhf', line.rstrip())
    line = re.sub(' leis an f', ' leis an bhf', line.rstrip())

    line = re.sub(' leis an ph', ' leis an bp', line.rstrip())
    line = re.sub(' leis an p', ' leis an bp', line.rstrip())

    line = re.sub(' leis an t-', ' leis an ', line.rstrip())


    # Ó
    line = re.sub(' ón bh', ' ón mb', line.rstrip())
    line = re.sub(' ón b', ' ón mb', line.rstrip())

    line = re.sub(' ón gh', ' ón ng', line.rstrip())
    line = re.sub(' ón g', ' ón ng', line.rstrip())

    line = re.sub(' ón ch', ' ón gc', line.rstrip())
    line = re.sub(' ón c', ' ón gc', line.rstrip())

    line = re.sub(' ón fh', ' ón bhf', line.rstrip())
    line = re.sub(' ón f', ' ón bhf', line.rstrip())

    line = re.sub(' ón ph', ' ón bp', line.rstrip())
    line = re.sub(' ón p', ' ón bp', line.rstrip())

    line = re.sub(' ón t-', ' ón ', line.rstrip())

    # ROIMH
    line = re.sub(' roimh an bh', ' roimh an mb', line.rstrip())
    line = re.sub(' roimh an b', ' roimh an mb', line.rstrip())

    line = re.sub(' roimh an gh', ' roimh an ng', line.rstrip())
    line = re.sub(' roimh an g', ' roimh an ng', line.rstrip())

    line = re.sub(' roimh an ch', ' roimh an gc', line.rstrip())
    line = re.sub(' roimh an c', ' roimh an gc', line.rstrip())

    line = re.sub(' roimh an fh', ' roimh an bhf', line.rstrip())
    line = re.sub(' roimh an f', ' roimh an bhf', line.rstrip())

    line = re.sub(' roimh an ph', ' roimh an bp', line.rstrip())
    line = re.sub(' roimh an p', ' roimh an bp', line.rstrip())

    line = re.sub(' roimh an t-', ' roimh an ', line.rstrip())

    # THAR
    line = re.sub(' thar an bh', ' thar an mb', line.rstrip())
    line = re.sub(' thar an b', ' thar an mb', line.rstrip())

    line = re.sub(' thar an gh', ' thar an ng', line.rstrip())
    line = re.sub(' thar an g', ' thar an ng', line.rstrip())

    line = re.sub(' thar an ch', ' thar an gc', line.rstrip())
    line = re.sub(' thar an c', ' thar an gc', line.rstrip())

    line = re.sub(' thar an fh', ' thar an bhf', line.rstrip())
    line = re.sub(' thar an f', ' thar an bhf', line.rstrip())

    line = re.sub(' thar an ph', ' thar an bp', line.rstrip())
    line = re.sub(' thar an p', ' thar an bp', line.rstrip())

    line = re.sub(' thar an t-', ' thar an ', line.rstrip())

    # TRÍ
    line = re.sub(' tríd an bh', ' tríd an mb', line.rstrip())
    line = re.sub(' tríd an b', ' tríd an mb', line.rstrip())

    line = re.sub(' tríd an gh', ' tríd an ng', line.rstrip())
    line = re.sub(' tríd an g', ' tríd an ng', line.rstrip())

    line = re.sub(' tríd an ch', ' tríd an gc', line.rstrip())
    line = re.sub(' tríd an c', ' tríd an gc', line.rstrip())

    line = re.sub(' tríd an fh', ' tríd an bhf', line.rstrip())
    line = re.sub(' tríd an f', ' tríd an bhf', line.rstrip())

    line = re.sub(' tríd an ph', ' tríd an bp', line.rstrip())
    line = re.sub(' tríd an p', ' tríd an bp', line.rstrip())

    line = re.sub(' tríd an t-', ' tríd an ', line.rstrip())

    # UM
    line = re.sub(' um an bh', ' um an mb', line.rstrip())
    line = re.sub(' um an b', ' um an mb', line.rstrip())

    line = re.sub(' um an gh', ' um an ng', line.rstrip())
    line = re.sub(' um an g', ' um an ng', line.rstrip())

    line = re.sub(' um an ch', ' um an gc', line.rstrip())
    line = re.sub(' um an c', ' um an gc', line.rstrip())

    line = re.sub(' um an fh', ' um an bhf', line.rstrip())
    line = re.sub(' um an f', ' um an bhf', line.rstrip())

    line = re.sub(' um an p', ' um an bp', line.rstrip())
    line = re.sub(' um an ph', ' um an bp', line.rstrip())

    line = re.sub(' um an t-', ' um an ', line.rstrip())

    #AG
    line= re.sub(' ag an Bh', ' ag an mB', line.rstrip())
    line= re.sub(' ag an B', ' ag an mB', line.rstrip())
    line= re.sub(' ag an Gh', ' ag an nG', line.rstrip())
    line= re.sub(' ag an G', ' ag an nG', line.rstrip())
    line= re.sub(' ag an Ch', ' ag an gC', line.rstrip())
    line= re.sub(' ag an C', ' ag an gC', line.rstrip())
    line= re.sub(' ag an Fh', ' ag an bhF', line.rstrip())
    line= re.sub(' ag an F', ' ag an bhF', line.rstrip())
    line= re.sub(' ag an Ph', ' ag an bP', line.rstrip())
    line= re.sub(' ag an P', ' ag an bP', line.rstrip())
    
    line= re.sub(' ag an tA', ' ag an A', line.rstrip())
    line= re.sub(' ag an tE', ' ag an E', line.rstrip())
    line= re.sub(' ag an tI', ' ag an I', line.rstrip())
    line= re.sub(' ag an tO', ' ag an O', line.rstrip())
    line= re.sub(' ag an tU', ' ag an U', line.rstrip())
    
    line= re.sub(' ag an tÁ', ' ag an Á', line.rstrip())
    line= re.sub(' ag an tÉ', ' ag an É', line.rstrip())
    line= re.sub(' ag an tÍ', ' ag an Í', line.rstrip())
    line= re.sub(' ag an tÓ', ' ag an Ó', line.rstrip())
    line= re.sub(' ag an tÚ', ' ag an Ú', line.rstrip())

    # AR
    line= re.sub(' ar an Bh', ' ar an mB', line.rstrip())
    line= re.sub(' ar an B', ' ar an mB', line.rstrip())
    line= re.sub(' ar an Gh', ' ar an nG', line.rstrip())
    line= re.sub(' ar an G', ' ar an nG', line.rstrip())
    line= re.sub(' ar an Ch', ' ar an gC', line.rstrip())
    line= re.sub(' ar an C', ' ar an gC', line.rstrip())
    line= re.sub(' ar an Fh', ' ar an bhF', line.rstrip())
    line= re.sub(' ar an F', ' ar an bhF', line.rstrip())
    line= re.sub(' ar an Ph', ' ar an bP', line.rstrip())
    line= re.sub(' ar an P', ' ar an bP', line.rstrip())
    
    line= re.sub(' ar an tA', ' ar an A', line.rstrip())
    line= re.sub(' ar an tE', ' ar an E', line.rstrip())
    line= re.sub(' ar an tI', ' ar an I', line.rstrip())
    line= re.sub(' ar an tO', ' ar an O', line.rstrip())
    line= re.sub(' ar an tU', ' ar an U', line.rstrip())
    
    line= re.sub(' ar an tÁ', ' ar an Á', line.rstrip())
    line= re.sub(' ar an tÉ', ' ar an É', line.rstrip())
    line= re.sub(' ar an tÍ', ' ar an Í', line.rstrip())
    line= re.sub(' ar an tÓ', ' ar an Ó', line.rstrip())
    line= re.sub(' ar an tÚ', ' ar an Ú', line.rstrip())

    # AS
    line= re.sub(' as an Bh', ' as an mB', line.rstrip())
    line= re.sub(' as an B', ' as an mB', line.rstrip())
    line= re.sub(' as an Gh', ' as an nG', line.rstrip())
    line= re.sub(' as an G', ' as an nG', line.rstrip())
    line= re.sub(' as an Ch', ' as an gC', line.rstrip())
    line= re.sub(' as an C', ' as an gC', line.rstrip())
    line= re.sub(' as an Fh', ' as an bhF', line.rstrip())
    line= re.sub(' as an F', ' as an bhF', line.rstrip())
    line= re.sub(' as an Ph', ' as an bP', line.rstrip())
    line= re.sub(' as an P', ' as an bP', line.rstrip())
    
    line= re.sub(' as an tA', ' as an A', line.rstrip())
    line= re.sub(' as an tE', ' as an E', line.rstrip())
    line= re.sub(' as an tI', ' as an I', line.rstrip())
    line= re.sub(' as an tO', ' as an O', line.rstrip())
    line= re.sub(' as an tU', ' as an U', line.rstrip())
    
    line= re.sub(' as an tÁ', ' as an Á', line.rstrip())
    line= re.sub(' as an tÉ', ' as an É', line.rstrip())
    line= re.sub(' as an tÍ', ' as an Í', line.rstrip())
    line= re.sub(' as an tÓ', ' as an Ó', line.rstrip())
    line= re.sub(' as an tÚ', ' as an Ú', line.rstrip())

    # FAOI
    line= re.sub(' faoin Bh', ' faoin mB', line.rstrip())
    line= re.sub(' faoin B', ' faoin mB', line.rstrip())
    line= re.sub(' faoin Gh', ' faoin nG', line.rstrip())
    line= re.sub(' faoin G', ' faoin nG', line.rstrip())
    line= re.sub(' faoin Ch', ' faoin gC', line.rstrip())
    line= re.sub(' faoin C', ' faoin gC', line.rstrip())
    line= re.sub(' faoin Fh', ' faoin bhF', line.rstrip())
    line= re.sub(' faoin F', ' faoin bhF', line.rstrip())
    line= re.sub(' faoin Ph', ' faoin bP', line.rstrip())
    line= re.sub(' faoin P', ' faoin bP', line.rstrip())
    
    line= re.sub(' faoin tA', ' faoin A', line.rstrip())
    line= re.sub(' faoin tE', ' faoin E', line.rstrip())
    line= re.sub(' faoin tI', ' faoin I', line.rstrip())
    line= re.sub(' faoin tO', ' faoin O', line.rstrip())
    line= re.sub(' faoin tU', ' faoin U', line.rstrip())
    
    line= re.sub(' faoin tÁ', ' faoin Á', line.rstrip())
    line= re.sub(' faoin tÉ', ' faoin É', line.rstrip())
    line= re.sub(' faoin tÍ', ' faoin Í', line.rstrip())
    line= re.sub(' faoin tÓ', ' faoin Ó', line.rstrip())
    line= re.sub(' faoin tÚ', ' faoin Ú', line.rstrip())

    # I
    line= re.sub(' i Bh', ' i mB', line.rstrip())
    line= re.sub(' i B', ' i mB', line.rstrip())
    line= re.sub(' i Gh', ' i nG', line.rstrip())
    line= re.sub(' i G', ' i nG', line.rstrip())
    line= re.sub(' i Ch', ' i gC', line.rstrip())
    line= re.sub(' i C', ' i gC', line.rstrip())
    line= re.sub(' i Fh', ' i bhF', line.rstrip())
    line= re.sub(' i F', ' i bhF', line.rstrip())
    line= re.sub(' i Ph', ' i bP', line.rstrip())
    line= re.sub(' i P', ' i bP', line.rstrip())
    
    line= re.sub(' i tA', ' in A', line.rstrip())
    line= re.sub(' i tE', ' in E', line.rstrip())
    line= re.sub(' i tI', ' in I', line.rstrip())
    line= re.sub(' i tO', ' in O', line.rstrip())
    line= re.sub(' i tU', ' in U', line.rstrip())
    
    line= re.sub(' i tÁ', ' in Á', line.rstrip())
    line= re.sub(' i tÉ', ' in É', line.rstrip())
    line= re.sub(' i tÍ', ' in Í', line.rstrip())
    line= re.sub(' i tÓ', ' in Ó', line.rstrip())
    line= re.sub(' i tÚ', ' in Ú', line.rstrip())
    
    line= re.sub(' in tA', ' in A', line.rstrip())
    line= re.sub(' in tE', ' in E', line.rstrip())
    line= re.sub(' in tI', ' in I', line.rstrip())
    line= re.sub(' in tO', ' in O', line.rstrip())
    line= re.sub(' in tU', ' in U', line.rstrip())
    
    line= re.sub(' in tÁ', ' in Á', line.rstrip())
    line= re.sub(' in tÉ', ' in É', line.rstrip())
    line= re.sub(' in tÍ', ' in Í', line.rstrip())
    line= re.sub(' in tÓ', ' in Ó', line.rstrip())
    line= re.sub(' in tÚ', ' in Ú', line.rstrip())
    
    line= re.sub(' sa tA', ' san A', line.rstrip())
    line= re.sub(' sa tE', ' san E', line.rstrip())
    line= re.sub(' sa tI', ' san I', line.rstrip())
    line= re.sub(' sa tO', ' san O', line.rstrip())
    line= re.sub(' sa tU', ' san U', line.rstrip())
    
    line= re.sub(' sa tÁ', ' san Á', line.rstrip())
    line= re.sub(' sa tÉ', ' san É', line.rstrip())
    line= re.sub(' sa tÍ', ' san Í', line.rstrip())
    line= re.sub(' sa tÓ', ' san Ó', line.rstrip())
    line= re.sub(' sa tÚ', ' san Ú', line.rstrip())
    
    line= re.sub(' san tA', ' san A', line.rstrip())
    line= re.sub(' san tE', ' san E', line.rstrip())
    line= re.sub(' san tI', ' san I', line.rstrip())
    line= re.sub(' san tO', ' san O', line.rstrip())
    line= re.sub(' san tU', ' san U', line.rstrip())
    
    line= re.sub(' san tÁ', ' san Á', line.rstrip())
    line= re.sub(' san tÉ', ' san É', line.rstrip())
    line= re.sub(' san tÍ', ' san Í', line.rstrip())
    line= re.sub(' san tÓ', ' san Ó', line.rstrip())
    line= re.sub(' san tÚ', ' san Ú', line.rstrip())

    # LE
    line= re.sub(' leis an Bh', ' leis an mB', line.rstrip())
    line= re.sub(' leis an B', ' leis an mB', line.rstrip())
    line= re.sub(' leis an Gh', ' leis an nG', line.rstrip())
    line= re.sub(' leis an G', ' leis an nG', line.rstrip())
    line= re.sub(' leis an Ch', ' leis an gC', line.rstrip())
    line= re.sub(' leis an C', ' leis an gC', line.rstrip())
    line= re.sub(' leis an Fh', ' leis an bhF', line.rstrip())
    line= re.sub(' leis an F', ' leis an bhF', line.rstrip())
    line= re.sub(' leis an Ph', ' leis an bP', line.rstrip())
    line= re.sub(' leis an P', ' leis an bP', line.rstrip())
    
    line= re.sub(' leis an tA', ' leis an A', line.rstrip())
    line= re.sub(' leis an tE', ' leis an E', line.rstrip())
    line= re.sub(' leis an tI', ' leis an I', line.rstrip())
    line= re.sub(' leis an tO', ' leis an O', line.rstrip())
    line= re.sub(' leis an tU', ' leis an U', line.rstrip())
    
    line= re.sub(' leis an tÁ', ' leis an Á', line.rstrip())
    line= re.sub(' leis an tÉ', ' leis an É', line.rstrip())
    line= re.sub(' leis an tÍ', ' leis an Í', line.rstrip())
    line= re.sub(' leis an tÓ', ' leis an Ó', line.rstrip())
    line= re.sub(' leis an tÚ', ' leis an Ú', line.rstrip())

    # Ó
    line= re.sub(' ón Bh', ' ón mB', line.rstrip())
    line= re.sub(' ón B', ' ón mB', line.rstrip())
    line= re.sub(' ón Gh', ' ón nG', line.rstrip())
    line= re.sub(' ón G', ' ón nG', line.rstrip())
    line= re.sub(' ón Ch', ' ón gC', line.rstrip())
    line= re.sub(' ón C', ' ón gC', line.rstrip())
    line= re.sub(' ón Fh', ' ón bhF', line.rstrip())
    line= re.sub(' ón F', ' ón bhF', line.rstrip())
    line= re.sub(' ón Ph', ' ón bP', line.rstrip())
    line= re.sub(' ón P', ' ón bP', line.rstrip())
    
    line= re.sub(' ón tA', ' ón A', line.rstrip())
    line= re.sub(' ón tE', ' ón E', line.rstrip())
    line= re.sub(' ón tI', ' ón I', line.rstrip())
    line= re.sub(' ón tO', ' ón O', line.rstrip())
    line= re.sub(' ón tU', ' ón U', line.rstrip())
    
    line= re.sub(' ón tÁ', ' ón Á', line.rstrip())
    line= re.sub(' ón tÉ', ' ón É', line.rstrip())
    line= re.sub(' ón tÍ', ' ón Í', line.rstrip())
    line= re.sub(' ón tÓ', ' ón Ó', line.rstrip())
    line= re.sub(' ón tÚ', ' ón Ú', line.rstrip())

    # ROIMH
    line= re.sub(' roimh an Bh', ' roimh an mB', line.rstrip())
    line= re.sub(' roimh an B', ' roimh an mB', line.rstrip())
    line= re.sub(' roimh an Gh', ' roimh an nG', line.rstrip())
    line= re.sub(' roimh an G', ' roimh an nG', line.rstrip())
    line= re.sub(' roimh an Ch', ' roimh an gC', line.rstrip())
    line= re.sub(' roimh an C', ' roimh an gC', line.rstrip())
    line= re.sub(' roimh an Fh', ' roimh an bhF', line.rstrip())
    line= re.sub(' roimh an F', ' roimh an bhF', line.rstrip())
    line= re.sub(' roimh an Ph', ' roimh an bP', line.rstrip())
    line= re.sub(' roimh an P', ' roimh an bP', line.rstrip())
    
    line= re.sub(' roimh an tA', ' roimh an A', line.rstrip())
    line= re.sub(' roimh an tE', ' roimh an E', line.rstrip())
    line= re.sub(' roimh an tI', ' roimh an I', line.rstrip())
    line= re.sub(' roimh an tO', ' roimh an O', line.rstrip())
    line= re.sub(' roimh an tU', ' roimh an U', line.rstrip())
    
    line= re.sub(' roimh an tÁ', ' roimh an Á', line.rstrip())
    line= re.sub(' roimh an tÉ', ' roimh an É', line.rstrip())
    line= re.sub(' roimh an tÍ', ' roimh an Í', line.rstrip())
    line= re.sub(' roimh an tÓ', ' roimh an Ó', line.rstrip())
    line= re.sub(' roimh an tÚ', ' roimh an Ú', line.rstrip())

    # THAR
    line= re.sub(' thar an Bh', ' thar an mB', line.rstrip())
    line= re.sub(' thar an B', ' thar an mB', line.rstrip())
    line= re.sub(' thar an Gh', ' thar an nG', line.rstrip())
    line= re.sub(' thar an G', ' thar an nG', line.rstrip())
    line= re.sub(' thar an Ch', ' thar an gC', line.rstrip())
    line= re.sub(' thar an C', ' thar an gC', line.rstrip())
    line= re.sub(' thar an Fh', ' thar an bhF', line.rstrip())
    line= re.sub(' thar an F', ' thar an bhF', line.rstrip())
    line= re.sub(' thar an Ph', ' thar an bP', line.rstrip())
    line= re.sub(' thar an P', ' thar an bP', line.rstrip())
    
    line= re.sub(' thar an tA', ' thar an A', line.rstrip())
    line= re.sub(' thar an tE', ' thar an E', line.rstrip())
    line= re.sub(' thar an tI', ' thar an I', line.rstrip())
    line= re.sub(' thar an tO', ' thar an O', line.rstrip())
    line= re.sub(' thar an tU', ' thar an U', line.rstrip())
    
    line= re.sub(' thar an tÁ', ' thar an Á', line.rstrip())
    line= re.sub(' thar an tÉ', ' thar an É', line.rstrip())
    line= re.sub(' thar an tÍ', ' thar an Í', line.rstrip())
    line= re.sub(' thar an tÓ', ' thar an Ó', line.rstrip())
    line= re.sub(' thar an tÚ', ' thar an Ú', line.rstrip())

    # TRÍD
    line= re.sub(' tríd an Bh', ' tríd an mB', line.rstrip())
    line= re.sub(' tríd an B', ' tríd an mB', line.rstrip())
    line= re.sub(' tríd an Gh', ' tríd an nG', line.rstrip())
    line= re.sub(' tríd an G', ' tríd an nG', line.rstrip())
    line= re.sub(' tríd an Ch', ' tríd an gC', line.rstrip())
    line= re.sub(' tríd an C', ' tríd an gC', line.rstrip())
    line= re.sub(' tríd an Fh', ' tríd an bhF', line.rstrip())
    line= re.sub(' tríd an F', ' tríd an bhF', line.rstrip())
    line= re.sub(' tríd an Ph', ' tríd an bP', line.rstrip())
    line= re.sub(' tríd an P', ' tríd an bP', line.rstrip())
    
    line= re.sub(' tríd an tA', ' tríd an A', line.rstrip())
    line= re.sub(' tríd an tE', ' tríd an E', line.rstrip())
    line= re.sub(' tríd an tI', ' tríd an I', line.rstrip())
    line= re.sub(' tríd an tO', ' tríd an O', line.rstrip())
    line= re.sub(' tríd an tU', ' tríd an U', line.rstrip())
    
    line= re.sub(' tríd an tÁ', ' tríd an Á', line.rstrip())
    line= re.sub(' tríd an tÉ', ' tríd an É', line.rstrip())
    line= re.sub(' tríd an tÍ', ' tríd an Í', line.rstrip())
    line= re.sub(' tríd an tÓ', ' tríd an Ó', line.rstrip())
    line= re.sub(' tríd an tÚ', ' tríd an Ú', line.rstrip())

    # UM
    line= re.sub(' um an Bh', ' um an mB', line.rstrip())
    line= re.sub(' um an B', ' um an mB', line.rstrip())
    line= re.sub(' um an Gh', ' um an nG', line.rstrip())
    line= re.sub(' um an G', ' um an nG', line.rstrip())
    line= re.sub(' um an Ch', ' um an gC', line.rstrip())
    line= re.sub(' um an C', ' um an gC', line.rstrip())
    line= re.sub(' um an Fh', ' um an bhF', line.rstrip())
    line= re.sub(' um an F', ' um an bhF', line.rstrip())
    line= re.sub(' um an P', ' um an bP', line.rstrip())
    line= re.sub(' um an Ph', ' um an bP', line.rstrip())
    
    line= re.sub(' um an tA', ' um an A', line.rstrip())
    line= re.sub(' um an tE', ' um an E', line.rstrip())
    line= re.sub(' um an tI', ' um an I', line.rstrip())
    line= re.sub(' um an tO', ' um an O', line.rstrip())
    line= re.sub(' um an tU', ' um an U', line.rstrip())
    
    line= re.sub(' um an tÁ', ' um an Á', line.rstrip())
    line= re.sub(' um an tÉ', ' um an É', line.rstrip())
    line= re.sub(' um an tÍ', ' um an Í', line.rstrip())
    line= re.sub(' um an tÓ', ' um an Ó', line.rstrip())
    line= re.sub(' um an tÚ', ' um an Ú', line.rstrip())
    

    #REMOVE WEIRD COMBOS

    line= re.sub(' ngc', ' gc', line.rstrip())
    line= re.sub(' ngC', ' gC', line.rstrip())
    line= re.sub(' mbp', ' bp', line.rstrip())
    line= re.sub(' mbP', ' bP', line.rstrip())
    line= re.sub(' mbhf', ' bhf', line.rstrip())
    line= re.sub(' mbhF', ' bhF', line.rstrip())
    line= re.sub(' mbf', ' bhf', line.rstrip())
    line= re.sub(' mbF', ' bhF', line.rstrip())

    #EXCEPTIONS
    line= re.sub(' ag an gCentre ', ' ag an Centre ', line.rstrip())
    line = re.sub(' an an nGaeilge ', ' ag an Ghaeilge ', line.rstrip())
    
    outfile.write(line + '\n')
