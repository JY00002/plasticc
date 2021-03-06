#!/usr/bin/env python
"""Script to train a set of classifiers using cross-validation on an augmented
test set
"""

import plasticc

from settings import settings

num_augments = settings['NUM_AUGMENTS']
d = plasticc.Dataset()
d.load_augment(num_augments)
d.load_features()

print("Training classifiers for %d augments." % num_augments)
classifiers = d.train_classifiers(do_fold=True)

plasticc.save_classifiers(classifiers, settings['MODEL_PATH_FORMAT'] %
                          num_augments)
