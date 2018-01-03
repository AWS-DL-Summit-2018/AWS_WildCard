TRAINING_STEPS=1000
WGET1='--no-check-certificate -O yoda.zip https://onedrive.live.com/download?cid=CFC83C4C51275DF4&resid=CFC83C4C51275DF4%212710&authkey=AAsATpxh9fA0w-A'
WGET2='--no-check-certificate -O darth_vader.zip https://onedrive.live.com/download?cid=CFC83C4C51275DF4&resid=CFC83C4C51275DF4%212707&authkey=ACV_NhnmfoiW1ZY'
echo "Retraining script for Inception V3"

mkdir tf_files
cd tf_files
mkdir star_wars
cd ..

wget $WGET1
tar -xf yoda.zip -C tf_files/star_wars
rm yoda.zip
rm -rf tf_files/star_wars/__MACOSX

wget $WGET2
tar -xf darth_vader.zip -C tf_files/star_wars
rm darth_vader.zip
rm -rf tf_files/star_wars/__MACOSX

ls tf_files/star_wars/yoda
ls tf_files/star_wars/darth_vader

pkill -f "tensorboard"

tensorboard --logdir tf_files/training_summaries &


python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=$TRAINING_STEPS \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --image_dir=tf_files/star_wars

  echo "Report final accuracy"

