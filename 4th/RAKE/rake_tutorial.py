from __future__ import absolute_import
from __future__ import print_function
import six

import rake
import operator
import io
from nltk.corpus import stopwords

# EXAMPLE ONE - SIMPLE
stoppath = "./data/stoplists/SmartStoplist.txt"
with open(stoppath, 'r', encoding='utf-8') as f:
    stop = f.read()
    stop = stop.split()
# 1. initialize RAKE by providing a path to a stopwords file
#rake_object = rake.Rake(stoppath, 5, 3, 4)
# 2. run on RAKE on a given text
sample_file = io.open("panther_text.txt", 'r',encoding="utf-8")
text = sample_file.read()
#text = text.split()
#text = [i.strip('?!)”“—(') for i in text]
#ext = ' '.join(text)

#keywords = rake_object.run(text)
#print(rake_object.run(text))
# 3. print results
#with open ('panther_keywords.txt', 'w', encoding='utf-8') as result:
#    result.write("Keywords:" + str(keywords))
#print("Keywords:", keywords)

#print("----------")
# EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

#text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \
 #      "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \
#       "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\
#       " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \
#       "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \
#       "systems and systems of mixed types."



# 1. Split text into sentences
sentenceList = rake.split_sentences(text)
#with open ('panther_keywords.txt', 'w', encoding='utf-8') as result:
#    for sentence in sentenceList:
#        result.write("\n Sentence:" + str(sentence))
 #   result.write("Keywords:" + str([i for i in keywords]))

# generate candidate keywords
stopwords = rake.load_stop_words(stoppath)
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern, stopwords)
#with open ('panther_keywords.txt', 'w', encoding='utf-8') as result:
#    result.write("\n Phrases:" + str(phraseList) + '\n')
#print("Phrases:", phraseList)

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
with open ('panther_keywords.txt', 'w', encoding='utf-8') as result:
    for candidate in keywordcandidates.keys():
        result.write("\n Candidate: " + str(candidate) + ", score: " + str(keywordcandidates.get(candidate)))
#for candidate in keywordcandidates.keys():
#    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
with open ('panther_keywords.txt', 'a', encoding='utf-8') as result:
    for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
        if keyword[0] not in stop:
            result.write("Keyword: "+ str(keyword[0]) + ", score: "+ str(keyword[1]) + '\n')

#print(rake_object.run(text))
keywords = rake_object.run('Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility " \ "of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. " \ "Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating"\ " sets of solutions for all types of systems are given. These criteria and the corresponding algorithms " \ "for constructing a minimal supporting set of solutions can be used in solving all the considered types of " \ "systems and systems of mixed types ')        
with open ('panther_keywords.txt', 'a', encoding='utf-8') as result:
    result.write("Keywords:" + str(keywords))
