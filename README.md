# seoul-classifier
This is a project classifying different types of buses in Seoul

By this [website](https://english.visitkorea.or.kr/enu/TRP/TP_ENG_8_1_1.jsp), there are 5 different types of buses in Seoul.

- Green buses, which are branch buses, look like this
    - ![s_grn (1).jpeg](https://github.com/jKyuery/seoul-classifier/blob/main/data/s_grn/s_grn%20(1).jpeg)

- Blue buses, which are mainline buses
    - ![s_blue (1).jpeg](https://github.com/jKyuery/seoul-classifier/blob/main/data/s_blue/s_blue%20(1).jpeg)

- Red buses which are rapid buses
    - ![s_red (1).jpeg](https://github.com/jKyuery/seoul-classifier/blob/main/data/s_red/s_red%20(1).jpeg)

- Airport buses
    - ![s_air (1).jpeg](https://github.com/jKyuery/seoul-classifier/blob/main/data/s_air/s_air%20(1).jpeg)

- And Night buses which operate only at night
    - ![s_night (1).jpeg](https://github.com/jKyuery/seoul-classifier/blob/main/data/s_night/s_night%20(1).jpeg)

- There's other buses that roam around Seoul too.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
The data was scraped using the [Google Image Scraper](https://github.com/ohyicong/Google-Image-Scraper) and hand picked from NamuWiki pages.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
- Scraped, handpicked and labeled data
- Converted images into tensors and performed feature normalization / scaling 
- Used Convoluted Neural Network as base, Data Augmentation and Transfer Learning to determine which method provided the best performance
- Used Mobilenet V2 pretrained model for Transfer Learning
-------------------------------------------------------------------------------------------------------------------------------------------------------------
## Model Performance
- Base CNN 
    - Training Accuracy: 98%
    - Test Accuracy: 75%

    - ![Opera Snapshot_2023-05-26_205442_localhost.png](https://github.com/jKyuery/seoul-classifier/blob/main/data/Opera%20Snapshot_2023-05-26_205442_localhost.png)
- Data Augmentation + CNN
    - Training Accuracy: 55%
    - Test Accuracy: 55%

    - ![Opera Snapshot_2023-05-26_205512_localhost.png](https://github.com/jKyuery/seoul-classifier/blob/main/data/Opera%20Snapshot_2023-05-26_205512_localhost.png)   
- Transfer Learning
    - Training Accuracy: 97%
    - Test Accuracy: 84%
 
    - ![Opera Snapshot_2023-05-26_205548_localhost.png](https://github.com/jKyuery/seoul-classifier/blob/main/data/Opera%20Snapshot_2023-05-26_205548_localhost.png)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
## Model Deployment
The final model that correctly classified the buses with high accuracy was deployed on a web application on Streamlit.

-------------------------------------------------------------------------------------------------------------------------------------------------------------
## Afterthoughts
This was just a one-dimensional model. There are some inaccuracies with the labeling. To further accurately classify the buses, we would need to add a dimension or two to check for two colors and hues.
