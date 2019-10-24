#  https://medium.com/gsi-technology/rdkit-for-newbies-3697e617521f

from rdkit import Chem

m = Chem.MolFromSmiles('Cc1ccccc1')

print(m)