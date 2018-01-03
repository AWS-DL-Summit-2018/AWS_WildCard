TRAINING_STEPS=1000

echo "Retraining script with data augmentation for Inception V3"
ls data

pkill -f "tensorboard"

tensorboard --logdir tf_files/training_summaries &

echo "Installing Augmentor"
pip install Augmentor

python scripts/augment.py

python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=$TRAINING_STEPS \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --image_dir=tf_files/star_wars_2 \
  --learning_rate=0.0001 \
  --testing_percentage=20 \
  --validation_percentage=20 \
  --train_batch_size=32 \
  --validation_batch_size=-1 \
  --how_many_training_steps=TRAINING_STEPS

echo "Report final accuracy"
