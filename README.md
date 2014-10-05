HotFuzz
=======

Super simple interpretation of the fuzzy logic search seen in sublime text.

Credit goes to this Quora question/answer [here](http://www.quora.com/Algorithms/How-is-the-fuzzy-search-algorithm-in-Sublime-Text-designed/answer/Bulat-Bochkariov)

Core logic is a simple RegEx searching for matching combinations in the strings
```Python
matched = [string for string in ministries if re.search(".*?".join(query),string,flags=re.IGNORECASE)]
```
