#!/usr/bin/python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from libraries.baselines import Corpus

from stanford_corenlp_python import jsonrpc
from simplejson import loads


def process_semeval_2015():
    # the train set is composed by train and trial data set
    corpora = dict()
    corpora['laptop'] = dict()
    train_filename = 'datasets/ABSA-SemEval2015/ABSA-15_Restaurants_Train_Final.xml'
    trial_filename = 'datasets/ABSA-SemEval2015/absa-2015_restaurants_trial.xml'

    reviews = ET.parse(train_filename).getroot().findall('Review') + \
              ET.parse(trial_filename).getroot().findall('Review')

    sentences = []
    for r in reviews:
        sentences += r.find('sentences').getchildren()

    # TODO: parser is not loading aspect words and opinioss
    corpus = Corpus(sentences)
    corpus.size()


def process_semeval_2014():
    # the train set is composed by train and trial dataset
    corpora = dict()
    corpora['restaurants'] = dict()
    train_filename = 'datasets/ABSA-SemEval2014/Restaurants_Train_v2.xml'
    trial_filename = 'datasets/ABSA-SemEval2014/restaurants-trial.xml'
    corpus = Corpus(ET.parse(train_filename).getroot().findall('sentence') +
                    ET.parse(trial_filename).getroot().findall('sentence'))
    corpora['restaurants']['trainset'] = dict()
    corpora['restaurants']['trainset']['corpus'] = corpus
    return corpora


def main():
    # TODO: start corenlp server "python corenlp.py"

    # interface for Stanford-Core-NLP server
    server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),
                                 jsonrpc.TransportTcpIp(addr=("127.0.0.1",
                                                              8080)))

    result = loads(server.parse("Hello world.  It is so beautiful"))
    print "Result", result

    corpora = process_semeval_2014()
    train_restaurants = corpora['restaurants']['trainset']['corpus']

    for s in train_restaurants.corpus:
        print s.text

    """
    print train_restaurants.size
    print train_restaurants.aspect_terms_fd
    """

if __name__ == '__main__':
    main()
