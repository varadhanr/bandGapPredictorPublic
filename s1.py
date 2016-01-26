from pymatgen import MPRester, periodic_table
import itertools

API_KEY = 'qwD0Fv5BUfh6IAmp'

# There are 103 elements in pymatgen's list, giving C(103, 2) = 5253 binary systems
allBinaries = itertools.combinations(periodic_table.all_symbols(), 2) # Create list of all binary systems

with MPRester(API_KEY) as m:
    for system in allBinaries:
        results = m.get_data(system[0] + '-' + system[1], data_type='vasp') # Download DFT data for each binary system
        for material in results: # We will receive many compounds within each binary system
            if material['e_above_hull'] < 1e-6: # Check if this compound is thermodynamically stable
                print(material['pretty_formula'] + ',' + str(material['band_gap'])) # Output band gap csv to the screen   
