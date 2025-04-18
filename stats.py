def get_book_text(FilePath):
        charDict = {}
        with open(FilePath) as f: 
            FileContent = f.read().lower()
        WordList = FileContent.split()
        for char in FileContent:
            if char in charDict:
                charDict[char] = charDict.get(char) + 1
            else:
                charDict.update({char:1}) 
        NumWords = len(WordList)
        sortedCharDict = dict(sorted(charDict.items(), key=lambda item: item[1], reverse=True))
        return f"'Found {NumWords} total words'", sortedCharDict