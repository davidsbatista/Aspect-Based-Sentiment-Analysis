#!/usr/bin/python
# -*- coding: utf-8 -*-

from libraries.baselines import Corpus
import xml.etree.ElementTree as ET, getopt, logging, sys, random, re, copy


def main():

    # the train set is composed by train and trial dataset
    corpora = dict()
    corpora['restaurants'] = dict()
    corpora['laptop'] = dict()
    train_filename = 'datasets/ABSA-SemEval2015/ABSA-15_Restaurants_Train_Final.xml'
    trial_filename = 'datasets/ABSA-SemEval2015/absa-2015_restaurants_trial.xml'

    reviews = ET.parse(train_filename).getroot().findall('Review') + \
              ET.parse(trial_filename).getroot().findall('Review')

    sentences = []
    for r in reviews:
        sentences += r.find('sentences').getchildren()

    corpus = Corpus(sentences)

    # TODO: testar com os dados de 2014, sacar daqui https://github.com/pedrobalage/SemevalAspectBasedSentimentAnalysis/tree/master/semeval_data
    # TODO: alterar o parser para funcionar com os dados de 2015
    print corpus.size
    print corpus.aspect_terms_fd
    print corpus.top_aspect_terms
    print corpus.corpus[0].text
    print corpus.corpus[0].id
    print corpus.corpus[0].aspect_terms
    print corpus.corpus[0].aspect_categories

if __name__ == '__main__':
    main()
