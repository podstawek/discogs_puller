#Discogs Puller

This script pulls data from your user-defined lists at [Discogs](https://www.discogs.com/), and builds a simple Webpage where the records on your lists are listed, with album art and some data, and also with links to Discogs itself if you need them.

To run the script, first create a few lists in your [Discogs lists section](https://www.discogs.com/user/podstawek/lists), then [request a Discogs token](https://www.discogs.com/developers#page:authentication). Rename the included `config_sample.py` file to `config.py` and update it with your real token and username.

Then run the script by typing in `python3 pull_lists.py`.

The script will take a while to run, and if everything went well it will produce a file `index.html` in the current directory which is your generated webpage. You can use it locally or put it on any server [as I did for myself](http://podstawczynski.com/favoritemusic/).

Enjoy!
