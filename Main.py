from FileHandler import *
from FeatureExtracting import *


def main():
    data = ReadFilesFromDir_CSV('test1')

    features = FeatureExtracting_ALL(data)
    WriteFeaturesToFiles_JSON(features)

    return 0


if __name__ == "__main__":
    main()

