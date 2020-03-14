# NER:
We are going to speed up NER by making use of the following:
#### We will have 2 kinds of data:
- One word answers for NER
- More than one word answers for NER.


##### Case: More than one word answers for NER:
- We will make 3 models:
    - Single word Models
    - Multi word models:
        - Bi-grma
        - Tri-gram
        - (Maybe allow for larger if the certain problem requires it)
        \


### TODO:
- Add number remover.
- A config for removal of extra information, **ADVANCED USAGE**
- Remove oov(out of vocab) words.
- Add  option to build upon older data, pre-trained
- Remove simlar suggestions