# Representation Analysis Project

You can use this repository to train:
- Vanilla VAE (Beta-VAE with Beta = 1)
- Beta-VAE
- Beta-TCVAE

This is to use an alternative representation for training the gym-duckietown-agent. To read about the utility of such representations, refer https://arxiv.org/abs/1707.08475


## Creating/Downloading the dataset

1) To train the VAE from images, download the training data from the following link:

``` https://drive.google.com/open?id=1QujAUmmbfv2NNiyojrpjDur8FfC4xhgN ```
(DEPRECATED: These images belongs to the old duckietown simulator)


Make sure the data is in the ``` representation_analysis/ ``` directory

Do not remove the directory structure of the `data/` folder! Get a coffee, because downloading and unzipping 
will take a while

Or,
2) You can manually create the dataset yourself using ``` representation_analysis/dataset_utils/get_data_mini.py ```



## Creating/Downloading the dataset

From `gym-duckietown-agent` run the following command:

``` python representation_analysis/train_vae.py ```
