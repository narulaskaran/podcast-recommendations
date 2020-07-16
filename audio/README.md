# Showcasing that we can make powerful podcast recommendations baed on transcript analysis
Transcripts acquired via [podgist](podgist.com). To add to the transcript collection, add a podcast entry to the `podcast_list.json` file (without a `transcript` attribute) and then run `scraper.py` from the root project directory.

## Bag of Words Categorization
We are using scikit-learn to place podcasts into categories based on the frequency of occurrence of certain words within the transcript. We will be categorizing on an episode-by-episode level rather than a show-by-show level for now. If the number of episodes we have transcriptions for becomes large enough, then we can make some sort of decision for the top `x` categories a certain show can fall into based on majority votes of its episodes. 


## Transcription
Started off trying to transcribe podcast files in chunks but once we found podgist, we decided it would be easier and more time-efficient to pull transcripts from there. 