import nltk
import nltk.data

# PATH_STOPWORDS = 'textteaser/stopWords.txt'
# PATH_PICKLE_EN = 'textteaser/english.pickle'
PATH_STOPWORDS = 'doc_summarizer/textteaser/stopWords.txt'
PATH_PICKLE_EN = 'doc_summarizer/textteaser/english.pickle'


class Parser(object):
    def __init__(self):
        self.ideal = 20.0
        self.stopWords = self.getStopWords()

    def getKeywords(self, text):
        text = self.removePunctations(text)
        words = self.splitWords(text)
        words = self.removeStopWords(words)
        uniqueWords = list(set(words))

        keywords = [{'word': word, 'count': words.count(word)} for word in uniqueWords]
        keywords = sorted(keywords, key=lambda x: -x['count'])
        return (keywords, len(words))

    def getSentenceLengthScore(self, sentence):
        return (self.ideal - abs(self.ideal - len(sentence))) / self.ideal

    # Jagadeesh, J., Pingali, P., & Varma, V. (2005). Sentence Extraction Based Single Document Summarization. International Institute of Information Technology, Hyderabad, India, 5.
    def getSentencePositionScore(self, i, sentenceCount):
        normalized = i / (sentenceCount * 1.0)

        if normalized > 0 and normalized <= 0.1:
            return 0.17
        elif normalized > 0.1 and normalized <= 0.2:
            return 0.23
        elif normalized > 0.2 and normalized <= 0.3:
            return 0.14
        elif normalized > 0.3 and normalized <= 0.4:
            return 0.08
        elif normalized > 0.4 and normalized <= 0.5:
            return 0.05
        elif normalized > 0.5 and normalized <= 0.6:
            return 0.04
        elif normalized > 0.6 and normalized <= 0.7:
            return 0.06
        elif normalized > 0.7 and normalized <= 0.8:
            return 0.04
        elif normalized > 0.8 and normalized <= 0.9:
            return 0.04
        elif normalized > 0.9 and normalized <= 1.0:
            return 0.15
        else:
            return 0

    def getTitleScore(self, title, sentence):
        titleWords = self.removeStopWords(title)
        sentenceWords = self.removeStopWords(sentence)
        matchedWords = [word for word in sentenceWords if word in titleWords]
        return len(matchedWords) / (len(title) * 1.0)

    def splitSentences(self, text):
        tokenizer = nltk.data.load(PATH_PICKLE_EN)
        return tokenizer.tokenize(text)

    def splitWords(self, sentence):
        return sentence.lower().split()

    def removePunctations(self, text):
        return ''.join(t for t in text if t.isalnum() or t == ' ')

    def removeStopWords(self, words):
        return [word for word in words if word not in self.stopWords]

    def getStopWords(self):
        with open(PATH_STOPWORDS) as file:
            words = file.readlines()
        return [word.replace('\n', '') for word in words]


class Summarizer(object):
    def __init__(self):
        self.parser = Parser()

    def summarize(self, text, title, source, category):
        sentences = self.parser.splitSentences(text)
        titleWords = self.parser.removePunctations(title)
        titleWords = self.parser.splitWords(title)
        (keywords, wordCount) = self.parser.getKeywords(text)
        topKeywords = self.getTopKeywords(keywords[:10], wordCount, source, category)
        result = self.computeScore(sentences, titleWords, topKeywords)
        result = self.sortScore(result)
        return result

    def getTopKeywords(self, keywords, wordCount, source, category):
        # Add getting top keywords in the database here
        for keyword in keywords:
            articleScore = 1.0 * keyword['count'] / wordCount
            keyword['totalScore'] = articleScore * 1.5
        return keywords

    def sortScore(self, dictList):
        return sorted(dictList, key=lambda x: -x['totalScore'])

    def sortSentences(self, dictList):
        return sorted(dictList, key=lambda x: x['order'])

    def computeScore(self, sentences, titleWords, topKeywords):
        keywordList = [keyword['word'] for keyword in topKeywords]
        summaries = []

        for i, sentence in enumerate(sentences):
            sent = self.parser.removePunctations(sentence)
            words = self.parser.splitWords(sent)

            sbsFeature = self.sbs(words, topKeywords, keywordList)
            dbsFeature = self.dbs(words, topKeywords, keywordList)

            titleFeature = self.parser.getTitleScore(titleWords, words)
            sentenceLength = self.parser.getSentenceLengthScore(words)
            sentencePosition = self.parser.getSentencePositionScore(i, len(sentences))
            keywordFrequency = (sbsFeature + dbsFeature) / 2.0 * 10.0
            totalScore = (
                                 titleFeature * 1.5 + keywordFrequency * 2.0 + sentenceLength * 0.5 + sentencePosition * 1.0) / 4.0

            summaries.append({
                # 'titleFeature': titleFeature,
                # 'sentenceLength': sentenceLength,
                # 'sentencePosition': sentencePosition,
                # 'keywordFrequency': keywordFrequency,
                'totalScore': totalScore,
                'sentence': sentence,
                'order': i
            })
        return summaries

    def sbs(self, words, topKeywords, keywordList):
        score = 0.0
        if len(words) == 0:
            return 0
        for word in words:
            word = word.lower()
            index = -1
            if word in keywordList:
                index = keywordList.index(word)
            if index > -1:
                score += topKeywords[index]['totalScore']
        return 1.0 / abs(len(words)) * score

    def dbs(self, words, topKeywords, keywordList):
        k = len(list(set(words) & set(keywordList))) + 1
        summ = 0.0
        firstWord = {}
        secondWord = {}

        for i, word in enumerate(words):
            if word in keywordList:
                index = keywordList.index(word)

                if firstWord == {}:
                    firstWord = {'i': i, 'score': topKeywords[index]['totalScore']}
                else:
                    secondWord = firstWord
                    firstWord = {'i': i, 'score': topKeywords[index]['totalScore']}
                    distance = firstWord['i'] - secondWord['i']

                    summ += (firstWord['score'] * secondWord['score']) / (distance ** 2)

        return (1.0 / k * (k + 1.0)) * summ


class TextTeaser(object):

    def __init__(self):
        self.sum = Summarizer()

    def summarize(self, title, text, category="Undefined", source="Undefined", count=5):
        result = self.sum.summarize(text, title, source, category)
        result = self.sum.sortSentences(result[:count])
        result = [res['sentence'] for res in result]

        return result
