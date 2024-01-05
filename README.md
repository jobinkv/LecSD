# LecSD
Official github repository of Semantic Labels-Aware Transformer Model for Searching over a Large Collection of Lecture-Slides WACV 2023.

In order to setup the dataset do the following steps:

Download all the slides by running

`
cd datasets
`

`
pytthon 1_download_slides.py
`

It will save all the slide images with a unique ID.

The slide summary of each slide are given in the `slide_summary.json` file.

The semantiic informations are given in `slide_summary.json` file.

The train, validation, test split of slide images are in `slide_summary.json` file.

All the manually drawn sketch queries are included in the `sketchQueries` folder