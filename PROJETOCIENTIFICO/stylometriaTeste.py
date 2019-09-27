import stylometry

novel_corpus = StyloCorpus.from_glob_pattern('‪cientifico2.txt')
novel_corpus.output_csv('‪cientifico2.csv')