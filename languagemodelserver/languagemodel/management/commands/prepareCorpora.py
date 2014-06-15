from __future__ import print_function
from django.core.management.base import NoArgsCommand
import languagemodelserver.settings as settings
import os
import string

import nltk


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        b = nltk.corpus.brown
        corpusName = 'brown'
        corpusSentences = os.path.join(settings.BASE_DIR, 'corpus', corpusName+'_sentences')
        countsFile = os.path.join(settings.BASE_DIR, 'corpus', corpusName+'_counts')

        print("Dumping raw sentences from '%s' corpus... " % corpusName, end="")
        with open(corpusSentences, 'wb') as f:
            for tokens in b.sents():
                s = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in tokens]).strip()
                f.write(s+"\n")

        print("done.")

        
#        print("Generating ngram counts (%s)... " % countsFile)
#
#        ngram-count -text $testcorpus -sort -write $countsfile -order 5 -unk
#        echo " done."
#
#        echo "Building language model ($languagemodel)..."
#        make-big-lm -read $countsfile -lm $languagemodel -name $languagemodel -order 5 -unk
#        echo " done."
#
#
#