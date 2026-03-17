#IMPORT PYTHON LIBRARIES
import os
import openpyxl
import pathlib

#ACCESS MODULES FROM RAM API PACKAGE
from ram_concept.concept import Concept
from ram_concept.result_layers import ReactionContext


#SETUP
concept = Concept.start_concept(headless=False)
model = concept.open_file(pathlib(os.environ["PROGRAMDATA"]) / "Bentley"/ "Engineering" / "RAM Concept" / "RAM Concept 2024"/ "Reinforced Concrete Slab"/ "rc tutorial - aci318.cpt") #tutorial file
save_path = r'C:\Users\Basil.Chemais\Code\RC Slab.cpt' #saving to working directory
model.save_file(save_path)
print("Model saved as:", save_path)

#RUN ANALYSIS
model.calc_all()

#ACCESS THE CAD MANAGER
element_layer = model.cad_manager.element_layer
load_combos = model.cad_manager.load_combo_layers
all_columns = element_layer.column_elements_below

#SETUP WORKBOOK USING OPENPYXL
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.title = "Punching Shear Demands"
worksheet.append(["Column ID", "x (m)", "y (m)", "Load Combo", "Fz (kN)", "Mx (kNm)", "My (kNm)"])

#NESTED FOR LOOP 
#PRINT COLUMN RESULTS FOR EACH COLUMN FOR EACH LOAD COMBO 
for col in all_columns:
    pt = col.location
    for combo in load_combos:
        array = combo.column_reaction(col, ReactionContext.STANDARD)
        worksheet.append([col.uid, round(pt.x, 3) , round(pt.y, 3), combo.name, round(array.z, 3), round(array.rot_x, 3), round(array.rot_y , 3)])

#SAVE RESULTS TO EXCEL DOCUMENT        
excel_path = r'C:\Users\Basil.Chemais\Code\Punching Shear Demands.xlsx'
workbook.save(excel_path)
print("Excel saved as:", excel_path)

# SHUT DOWN RAM CONCEPT
concept.shut_down()
