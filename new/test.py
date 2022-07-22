import random
from models import *

ITEMS = {
        'TG': {'mid_code': 'TG', 'min_range': 0.55, 'max_range': 1.7},
        'EFT': {'mid_code': 'EFT', 'min_range': 0.0, 'max_range': 9999.0},
        'FRUC': {'mid_code': 'FRUC', 'min_range': 205.0, 'max_range': 285.0},
        'GA': {'mid_code': 'GA', 'min_range': 11.0, 'max_range': 16.0},
        'GAD': {'mid_code': 'GAD', 'min_range': 0.0, 'max_range': 9999.0},
        'GLU': {'mid_code': 'GLU', 'min_range': 3.33, 'max_range': 5.55},
        'HP': {'mid_code': 'HP', 'min_range': 0.0, 'max_range': 15.0},
        'K': {'mid_code': 'K', 'min_range': 3.5, 'max_range': 5.3},
        'MG': {'mid_code': 'MG', 'min_range': 0.7, 'max_range': 0.95},
        'PHOS': {'mid_code': 'PHOS', 'min_range': 1.15, 'max_range': 2.15},
        'SAA': {'mid_code': 'SAA', 'min_range': 0.0, 'max_range': 10.0},
        'CL': {'mid_code': 'CL', 'min_range': 99.0, 'max_range': 110.0},
        'TP': {'mid_code': 'TP', 'min_range': 44.0, 'max_range': 76.0},
        'UA': {'mid_code': 'UA', 'min_range': 155.0, 'max_range': 357.0},
        'UREA': {'mid_code': 'UREA', 'min_range': 1.43, 'max_range': 6.78},
        'ALBD': {'mid_code': 'ALBD', 'min_range': 0.0, 'max_range': 9999.0},
        'APO_A': {'mid_code': 'APO_A', 'min_range': 1.04, 'max_range': 2.02},
        'APO_B': {'mid_code': 'APO_B', 'min_range': 0.6, 'max_range': 1.33},
        'CREA': {'mid_code': 'CREA', 'min_range': 57.0, 'max_range': 97.0},
        'CYSC': {'mid_code': 'CYSC', 'min_range': 0.63, 'max_range': 1.25},
        'DBIL': {'mid_code': 'DBIL', 'min_range': 0.0, 'max_range': 5.0},
        'ADA': {'mid_code': 'ADA', 'min_range': 4.0, 'max_range': 22.0},
        'sdLDL-C': {'mid_code': 'sdLDL-C', 'min_range': 0.0, 'max_range': 94.0},
        'RF': {'mid_code': 'RF', 'min_range': 0.0, 'max_range': 14.0},
        'NA': {'mid_code': 'NA', 'min_range': 137.0, 'max_range': 147.0},
        'LPA': {'mid_code': 'LPA', 'min_range': 0.0, 'max_range': 300.0},
        'Lipaemic': {'mid_code': 'Lipaemic', 'min_range': 0.0, 'max_range': 100.0},
        'LDL_C': {'mid_code': 'LDL_C', 'min_range': 0.0, 'max_range': 3.37},
        'Icteric': {'mid_code': 'Icteric', 'min_range': 0.0, 'max_range': 50.0},
        'HSCRP': {'mid_code': 'HSCRP', 'min_range': 0.1, 'max_range': 2.8},
        'Hemoliti': {'mid_code': 'Hemoliti', 'min_range': 0.0, 'max_range': 80.0},
        'HDL_C': {'mid_code': 'HDL_C', 'min_range': 1.15, 'max_range': 9999},
        'ALB': {'mid_code': 'ALB', 'min_range': 38.0, 'max_range': 54.0},
        'ALP': {'mid_code': 'ALP', 'min_range': 0.0, 'max_range': 462.0},
        'ALT': {'mid_code': 'ALT', 'min_range': 9.0, 'max_range': 50.0},
        'ASLO': {'mid_code': 'ASLO', 'min_range': 0.0, 'max_range': 200.0},
        'AST': {'mid_code': 'AST', 'min_range': 13.0, 'max_range': 35.0},
        'CA': {'mid_code': 'CA', 'min_range': 2.25, 'max_range': 2.75},
        'CH50': {'mid_code': 'CH50', 'min_range': 23.0, 'max_range': 46.0},
        'CK': {'mid_code': 'CK', 'min_range': 39.0, 'max_range': 308.0},
        'CKMB': {'mid_code': 'CKMB', 'min_range': 0.0, 'max_range': 24.0},
        'HCY': {'mid_code': 'HCY', 'min_range': 0.0, 'max_range': 15.0},
        'CRP': {'mid_code': 'CRP', 'min_range': 0.0, 'max_range': 6.0},
        'AFU': {'mid_code': 'AFU', 'min_range': 0.0, 'max_range': 40.0},
        'HBDH': {'mid_code': 'HBDH', 'min_range': 72.0, 'max_range': 182.0},
        'GGT': {'mid_code': 'GGT', 'min_range': 10.0, 'max_range': 60.0},
        'LDH': {'mid_code': 'LDH', 'min_range': 120.0, 'max_range': 300.0},
        'LAP': {'mid_code': 'LAP', 'min_range': 20.0, 'max_range': 60.0},
        'PA': {'mid_code': 'PA', 'min_range': 180.0, 'max_range': 390.0},
        'CO2': {'mid_code': 'CO2', 'min_range': 22.0, 'max_range': 29.0},
        'CHOL': {'mid_code': 'CHOL', 'min_range': 3.38, 'max_range': 5.2},
        'TBA': {'mid_code': 'TBA', 'min_range': 0.0, 'max_range': 12.0},
        'TBIL': {'mid_code': 'TBIL', 'min_range': 0.0, 'max_range': 17.0},
        # 'AST/ALT': {'mid_code': 'AST/ALT', 'min_range': 0.0, 'max_range': 9999.0},
        # 'GLB': {'mid_code': 'GLB', 'min_range': 20.0, 'max_range': 40.0},
        # 'ALB/GLB': {'mid_code': 'ALB/GLB', 'min_range': 1.2, 'max_range': 2.4},
        # 'TBIL-DBIL': {'mid_code': 'TBIL-DBIL', 'min_range': 0.0, 'max_range': 9999.0},
        # 'CHOL-HLD_C': {'mid_code': 'CHOL-HLD_C', 'min_range': 0.0, 'max_range': 9999.0},
        # 'NA+K-CL-CO2': {'mid_code': 'NA+K-CL-CO2', 'min_range': 8.0, 'max_range': 16.0}
    }


def build_items(items):
    for item in items:
        pass

def built_results(items):
    for item, value in items:
        pass



if __name__ == '__main__':
    for k, b in ITEMS:
        print(k)
