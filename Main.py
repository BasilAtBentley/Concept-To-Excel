from ram_concept.concept import Concept
import os

# ── PART 1: SETUP ──────────────────────────────────────────
# Connect to RAM Concept and open the model
concept = Concept.start_concept(headless=False)
model = concept.open_file(r'C:\ProgramData\Bentley\Engineering\RAM Concept\RAM Concept 2024\Reinforced Concrete Slab\rc tutorial - aci318.cpt')

# Save a working copy so we never touch the original
save_path = r'C:\Projects\floor_API_run.cpt'
concept.save_file_as(save_path)

print("Model opened and saved as:", save_path)