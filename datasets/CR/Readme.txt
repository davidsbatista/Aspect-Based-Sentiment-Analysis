*****************************************************************************
* Annotated by: Minqing Hu and Bing Liu, 2004.
*		Department of Computer Sicence
*               University of Illinois at Chicago
*
* Contact: Bing Liu, liub@cs.uic.edu
*          http://www.cs.uic.edu/~liub
*****************************************************************************

                            Readme file

This folder contains annotated customer reviews of 5 products.

	1. digital camera: Canon G3
	2. digital camera: Nikon coolpix 4300
	3. celluar phone:  Nokia 6610
	4. mp3 player:     Creative Labs Nomad Jukebox Zen Xtra 40GB
	5. dvd player:     Apex AD2600 Progressive-scan DVD player

All the reviews were from amazon.com. They were used in the following
two papers:

Minqing Hu and Bing Liu. "Mining and summarizing customer reviews".
   Proceedings of the ACM SIGKDD International Conference on
   Knowledge Discovery & Data Mining (KDD-04), 2004.

Minqing Hu and Bing Liu. "Mining Opinion Features in Customer
   Reviews." Proceedings of Nineteeth National Conference on
   Artificial Intellgience (AAAI-2004), 2004.

Our project homepage: http://www.cs.uic.edu/~liub/FBS/FBS.html



Symbols used in the annotated reviews:

  [t]: the title of the review: Each [t] tag starts a review.
       We did not use the title information in our papers.
  xxxx[+|-n]: xxxx is a product feature.
      [+n]: Positive opinion, n is the opinion strength: 3 strongest,
            and 1 weakest. Note that the strength is quite subjective.
            You may want ignore it, but only considering + and -
      [-n]: Negative opinion
  ##  : start of each sentence. Each line is a sentence.
  [u] : feature not appeared in the sentence.
  [p] : feature not appeared in the sentence. Pronoun resolution is needed.
  [s] : suggestion or recommendation.
  [cc]: comparison with a competing product from a different brand.
  [cs]: comparison with a competing product from the same brand.


Finally, tagging is a hard task. Errors and inconsistencies are inevitable.
If you see some problems, please let us know. We also welcome your comments.


