import pandas as pd

from base import Feature, get_arguments, generate_features

Feature.dir = 'features'


class FamilySize(Feature):
    def create_features(self):
        # 家族の人数 = SibSp(兄弟、配偶者の数) + Parch(両親、子供の数) + 自分
        self.train['family_size'] = train['SibSp'] + train['Parch'] + 1
        self.test['family_size'] = test['SibSp'] + test['Parch'] + 1


if __name__ == "__main__":
    args = get_arguments()
    # print(args)
    train = pd.read_csv('./input/train.csv')
    test = pd.read_csv('./input/test.csv')
    # print(globals())
    generate_features(globals(), args.force)
