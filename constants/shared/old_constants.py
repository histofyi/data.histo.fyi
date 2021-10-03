BUCKETS = {
    'default': 'histo2-filestore'
}

STOP_CHARACTERS = ['\n','\r','\t',' ','!','"','#','$','*','%','&','\'','(',')',',','-','/','<','=','>','?','@','[',']','^','_','`','\{','|','\}',',','.','+','_']

SEQUENTIAL_ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

AMINO_ACIDS = {
    "three_letter": ['ala', 'arg', 'asn', 'asp', 'cys', 'glu', 'gln', 'gly', 'his', 'ile', 'leu', 'lys', 'met', 'phe', 'pro', 'ser', 'thr', 'trp', 'tyr', 'val'],
    "one_letter": ['a', 'r', 'n', 'd', 'c', 'e', 'q', 'g', 'h', 'i', 'l', 'k', 'm', 'f', 'p', 's', 't', 'w', 'y', 'v']
}

PEPTIDE_LENGTH = 30

CHAIN_LABELS = {
    "A": {
        "letter": "A",
        "label": "Alpha Chain (Class I)",
        "definition": "class_i_a",
        "synonyms": ["class i alpha", "class i ", "class 1"]
    },
    "B": {
        "letter": "B",
        "label": "Beta-2 microglobulin",
        "definition": "b2m",
        "synonyms": ["beta 2 microglobulin", "microglobulin"]
    },
    "C": {
        "letter": "C",
        "label": "Alpha Chain (Class II)",
        "definition": "class_ii_a",
        "synonyms": ["class ii alpha"]
    },
    "D": {
        "letter": "D",
        "label": "Beta Chain (Class II)",
        "definition": "class_ii_b",
        "synonyms": ["class ii beta", " beta chain "]
    },
    "E": {
        "letter": "E",
        "label": "Peptide epitope",
        "definition": "peptide",
        "synonyms": ["peptide", " epitope "]
    },
    "F": {
        "letter": "F",
        "label": "T-cell receptor beta/delta",
        "definition": "tcr_b",
        "synonyms": ["tcr beta", "t cell receptor beta", "tcr delta", "t cell receptor delta"]
    },
    "G": {
        "letter": "G",
        "label": "T-cell receptor alpha/gamma chain",
        "definition": "tcr_a",
        "synonyms": ["tcr alpha", "t cell receptor alpha", "tcr gamma", "t cell receptor gamma"]
    },
    "I": {
        "letter": "I",
        "label": "CLIP/Invariant Chain",
        "definition": "clip",
        "synonyms": ["clip", "invariant chain"]
    },
    "M": {
        "letter": "M",
        "label": "HLA-DM, or similar alpha chain",
        "definition": "non_classical_class_ii_a",
        "synonyms": ["hla dm alpha", "h2 m alpha", "dm alpha"]
    },
    "N": {
        "letter": "N",
        "label": "HLA-DM, or similar beta chain",
        "definition": "non_classical_class_ii_b",
        "synonyms": ["hla dm beta", "h2 m beta", "dm beta"]
    },
    "O": {
        "letter": "O",
        "label": "HLA-DO, or similar alpha chain",
        "definition": "non_classical_class_ii_a",
        "synonyms": ["hla do alpha", "h2 o alpha", "do alpha"]
    },
    "P": {
        "letter": "P",
        "label": "HLA-DO, or similar, beta chain",
        "definition": "non_classical_class_ii_b",
        "synonyms": ["hla do beta", "h2 o beta", "do beta"]
    },
    "Q": {
        "letter": "Q",
        "label": "Non-classical class I alpha chain",
        "definition": "non_classical_class_i_a",
        "synonyms": []
    },
    "R": {
        "letter": "R",
        "label": "CD4 / CD8",
        "definition": "accessory_molecule",
        "synonyms": ["cd4", "cd8", "co receptor", "coreceptor"]
    },
    "S": {
        "letter": "S",
        "label": "Superantigen",
        "definition": "superantigen",
        "synonyms": ["superantigen", "super antigen", "enterotoxin"]
    },
    "T": {
        "letter": "T",
        "label": "Tapasin or similar",
        "definition": "antigen_processing_molecule",
        "synonyms": ["tapasin"]
    },
    "U": {
        "letter": "U",
        "label": "Unknown",
        "definition": None,
        "synonyms": []
    }
}

LENGTHS = ["octamer","nonamer","decamer","undecamer","dodecamer","tridecamer","tetradecamer","pentadecamer","hexadecamer","heptadecamer","octadecamer","nonadecamer","eicosamer"]

SIZES = {
    "octamer": {
        "length": 8
    },
    "nonamer": {
        "length": 9
    },
    "decamer": {
        "length": 10
    },
    "undecamer": {
        "length": 11
    },
    "dodecamer": {
        "length": 12
    },
    "tridecamer": {
        "length": 13
    },
    "tetradecamer": {
        "length": 14
    },
    "pentadecamer": {
        "length": 15
    },
    "hexadecamer": {
        "length": 16
    },
    "heptadecamer": {
        "length": 17
    },
    "octadecamer": {
        "length": 18
    },
    "nonadecamer": {
        "length": 19
    },
    "eicosamer": {
        "length": 20
    }
}


