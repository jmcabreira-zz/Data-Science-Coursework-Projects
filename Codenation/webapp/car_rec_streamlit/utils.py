# <=============================================       extra_features     ===================================================>

def extra_features(df):
    ''' Create individual features from extra column
    ARG:
    df(dataframe): the dataframe tha will be parsed

    RETURNS:
    df(dataframe): The dataframe containing features extracted from the extra column'''

    # check the greter extra variable length in order to identify all possible individual features

    string_length_list = [len(x) if type(x) == str else x for x in df.extra]

    greater_length = max(string_length_list)

    greater_length_index = max([(v, i) for i, v in enumerate(string_length_list)])[1]

    extra_features = df.iloc[greater_length_index].extra

    n_of_features = len(extra_features.rsplit(','))

    # Create column for each feature in extra column
    for feature in range(n_of_features):
        colname = extra_features.rsplit(',')[feature].strip()
        df[colname] = 0.0

    df = fill_in_the_features(df)

    return df

#<= == == == == == == == == == == == == == == == == == == == == == == fill_in_the_features == == == == == == == == == == == == == == == == == == == == == == == == = >

def fill_in_the_features(df):
    '''Fills in the feature cells stating whether the car contains the respective feature

    ARG:
    df(dataframe): The dataframe to be filled in

    RETURNS:
    df(dataframe): the dataframe with filled columns - 1 car has the feature and 0 car does not
    '''

    # find the index of the column extra
    columns = list(df.columns)
    index = columns.index('extra')

    for feature in df.columns[(index + 1):]:

        total_rows = df.shape[0]

        for row in range(total_rows):

            is_zero = (df.extra[row] == 0)

            if is_zero == True:

                df[feature].values[row] = 0.0

            else:

                contains_feature = feature in df.extra[row]

                if contains_feature == True:
                    df[feature].values[row] = 1
                else:
                    continue

    # delete extra column
    df.drop('extra', axis=1, inplace=True)

    return df




