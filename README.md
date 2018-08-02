# Categorisation of a Page Text

This project takes the URL of a specific page and gives percentages of how much this the included text is relative to the 20 categories already chosen.


### Prerequisites



* python 3 
* re #regular expression library
* urllib.request #library to handle urls
* bs4.tifulSoup #to extract and manage data of webpage
* datetime #to calculate the time spent for every process
* langdetect #to detect in which language the text of the page is written
* requests #to create requests for retrieving the text of pages
* nltk.tokenize, nltk.corpus, nltk.stem.porter #to achieve all the tasks of the Natural Language Processing part of the project


### Installing



To get the program working you will need to change the path of the keywords data (parameter name "direc") and put the base path of the folders.

The parameter (turl) will hold the url of the page that you want to categorize.

So for example if we want to run  a test for the BBC sport page:
```
turl="https://www.bbc.com/sport"
```
The output would be something like: 
```
['Animal', 0]     0.00 %
['Language', 1]     0.00 %
['Doctor', 9]     0.02 %
['Food', 11]     0.02 %
['Emotion', 14]     0.02 %
['Family', 15]     0.03 %
['Car', 19]     0.03 %
['Art', 20]     0.03 %
['Clothes', 22]     0.04 %
['Buildings', 27]     0.05 %
['Computer', 33]     0.06 %
['Vacation', 35]     0.06 %
['Body', 40]     0.07 %
['Weather', 54]     0.09 %
['School', 63]     0.11 %
['Sport', 214]     0.37 %
Fetching time is           :  0:00:01.826171
language detecting time is :  0:00:00.030992
text preprocessing time is :  0:00:00.062963
Matching process time is   :  0:00:00.203890
```


### Break down into end to end tests

This test is testing how accurate would the program categorize the page, it also measures detecting a big number of the keywords related to the major category presented by this page.


## Built With

* [SPYDER](https://anaconda.org/anaconda/spyder) - The Python IDE


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Ahmad Alkairat ** - *Data Scientest* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

