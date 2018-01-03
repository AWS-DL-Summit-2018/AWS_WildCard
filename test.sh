echo "Test over an image"

python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=test/a.jpg

echo "Report the confidence values"
