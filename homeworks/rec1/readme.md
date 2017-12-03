_Работаю с операционной системой Ubuntu 16.04_

##1. Установка mrec

###1.1 Ставим setuptools

```
sudo apt install python3-setuptools
```

###1.2 Ставим mrec для python3

```
git clone https://github.com/inpefess/mrec
cd mrec
mkdir ~/scripts
python setup.py install --install-scripts ~/scripts
sudo mv ~/scripts/* /usr/local/sbin
```

##2. Обработка данных MovieLens 100K

###2.1 Скачиваем и разорхивируем архив с данными

```
wget http://files.grouplens.org/datasets/movielens/ml-100k.zip
unzip ml-100k.zip
```

###2.2 Подготавливаем данные

`mrec_prepare --dataset ml-100k/u.data --outdir splits --rating_thresh 4 --test_size 0.5 --binarize`

###2.3 Запускаем ipcluster

`ipcluster start -n4 --daemonize`

###2.4 Обучаем и предсказываем при помощи модели knn

```
mrec_train -n4 --model knn --input_format tsv --train "splits/u.data.train.*" --outdir models-knn
mrec_predict --input_format tsv --test_input_format tsv --train "splits/u.data.train.*" --modeldir models-knn --outdir recs-knn
```

**Результат**

```
CosineKNNRecommender(k=100)
mrr            0.6270 +/- 0.0053
prec@5         0.4010 +/- 0.0032
prec@10        0.3548 +/- 0.0018
prec@15        0.3237 +/- 0.0006
prec@20        0.2999 +/- 0.0005
```

###2.5 Обучаем и предсказываем при помощи модели popularity

```
mrec_train -n4 --model knn --input_format tsv --train "splits/u.data.train.*" --outdir models-popularity
mrec_predict --input_format tsv --test_input_format tsv --train "splits/u.data.train.*" --modeldir models-popularity --outdir recs-popularity
```

**Результат**

```
ItemPop
mrr            0.5216 +/- 0.0081
prec@5         0.2634 +/- 0.0012
prec@10        0.2467 +/- 0.0005
prec@15        0.2301 +/- 0.0011
prec@20        0.2123 +/- 0.0015
```

###2.6 Обучаем и предсказываем при помощи модели SLIM

```
mrec_train -n4 --model slim --input_format tsv --train "splits/u.data.train.*" --outdir models-slim
mrec_predict --input_format tsv --test_input_format tsv --train "splits/u.data.train.*" --modeldir models-slim --outdir recs-slim
```

**Результат**

```
SLIM(SGDRegressor(alpha=0.0011, average=False, epsilon=0.1, eta0=0.01,
       fit_intercept=False, l1_ratio=0.9090909090909091,
       learning_rate='invscaling', loss='squared_loss', max_iter=5,
       n_iter=None, penalty='elasticnet', power_t=0.25, random_state=None,
       shuffle=True, tol=None, verbose=0, warm_start=False))
mrr            0.6813 +/- 0.0032
prec@5         0.4342 +/- 0.0027
prec@10        0.3796 +/- 0.0019
prec@15        0.3408 +/- 0.0010
prec@20        0.3138 +/- 0.0005
```

Все файлы есть в текущей папке