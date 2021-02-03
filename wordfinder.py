from random import randrange, seed
seed(42)

"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """picks a random word from a list of words in file
    >>> wf = WordFinder('words.txt')
    235886 words read

    >>> wf.random()
    'researchful'

    >>> wf.random()
    'calyptriform'


    """
    def __init__(self, filepath):
        word_list = []
        with open (filepath) as f:
            for line in f:
                word_list.append(line.strip('\n'))
        self.word_list = word_list
        self.length = len(word_list)
        print(f'{self.length} words read')

    def random(self):
        return self.word_list[randrange(self.length)]
    
class SpecialWordFinder(WordFinder):
    """subclass of WordFinder
    picks random word from list of words in a file,
    ignoring blank lines and lines starting with '#'
    """
    def __init__(self, filepath):
        super().__init__(filepath)
        filtered_list = [word for word in self.word_list if len(word) > 0 and word[0] != '#']
        self.word_list = filtered_list
        self.length = len(self.word_list)
        print(f'{self.length} words in list')

