import argparse

def parse_feature_finder_args():
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--input_hdf5_sysfile', default = '', type = str,
                        help = 'HDF5 file containing the data '
                        'arrays of systematic values. It is assumed that each '
                        'systematic is stored as a HDF5 dataset of equal '
                        'length, and the indices of the arrays refer to the '
                        'same spatial position on the sky. No storage of '
                        'spatial information is required as long as the '
                        'user knows which array position corresponds to which '
                        'position on the sky. '
                        'These data arrays can be produced from HealPIX, '
                        'STOMP, smoothed fits images, or other pixelization '
                        'schemes.')
    parser.add_argument('--pre_load_data', action = 'store_true',
                        help = 'For smaller surveys such as CFHTLenS it may be '
                        'possible to load the full array data into memory. '
                        'This will save later disk reads and seed up the code. '
                        'This option may not be possible for larger surveys or '
                        'if the number of systematic columns is great.')
    parser.add_argument('--hdf5_group', default = None, type = str,
                        help = 'In case the datasets are stored '
                        'within a hdf5 group (i.e. a group specifying a field '
                        'in the survey) this argument allows for loading of '
                        'the data from the specified group.')
    parser.add_argument('--sys_name_list', default  = '', type = str,
                        help = 'A CSV list of the names of the survey '
                        'systematics to load and consider for the feature '
                        'finder. (i.e. for KiDS this could be '
                        '"r_depth,r_seeing,...").')
    parser.add_argument('--standardize_data', action = 'store_true',
                        help = 'For the feature finder to function properly, '
                        'the input systematics arrays must be standardized by, ' 
                        '(array - <array>) / sigma_array. If the arrays are '
                        'not already standardized, this argument will do so. '
                        'WARNING: This requires the loading of the full array '
                        'data and can be very slow or case memory errors for '
                        'large surveys.')
    parser.add_argument('--feature_classifier_type',
                        default = 'MiniBatchKMeans', type = str,
                        help = 'Specify the feature classifier to use. '
                        'Currently this defaults to the MiniBatchKMeans module '
                        'from scikit-learn.')
    ### TODO:
    ###     Collect other possible feature classifiers for use in the code.
    parser.add_argument('--n_features', default = 256, type = int,
                        help = 'Number of features to identify in the '
                        'systematics arrays.')
    ### TODO:
    ###     Add a method for passing more arguments into feature classifier.
    return parser.parse_args()