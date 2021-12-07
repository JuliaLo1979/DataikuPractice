# -*- coding: utf-8 -*-
#import dataiku
#import pandas as pd, numpy as np
#from dataiku import pandasutils as pdu

# Read recipe inputs
#mnist = dataiku.Folder("UVAoMwxi")
#mnist_info = mnist.get_info()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.
#mnist_imported_df = pd.DataFrame(columns=['path']) # Compute a Pandas dataframe to write into mnist_imported


# Write recipe outputs
#mnist_imported = dataiku.Dataset("mnist_imported")
#mnist_imported.write_with_schema(mnist_imported_df)
###

# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
folder = dataiku.Folder("UVAoMwxi")

# Initialize data frame
df = pd.DataFrame(columns=['path'])

# Populate dataframe with paths
df['path'] = folder.list_paths_in_partition()

# Write recipe outputs
mnist = dataiku.Dataset("mnist_imported")
mnist.write_with_schema(df)