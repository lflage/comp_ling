touch results.txt
echo $'\nBaseline Dice Performance:' >> ./results.txt
cd hw2
python score-alignments -n 0 < dice.a >> ../results.txt
echo $'\nIBM Model 1 Performance' >> ../results.txt
python score-alignments -n 0 < ../IBM_Model1/model1.a >> ../results.txt
echo $'\nFast align Performance' >> ../results.txt
python score-alignments -n 0 <  ../fast_align/forward.align >> ../results.txt
cd ..
echo $'\n### Alignments Comparison ###' >> ./results.txt
echo $'\n### Dice ###' >> ./results.txt
python align_viz.py -idx 0 -a_path ./hw2/dice.a >> ./results.txt
echo $'\n### IBM Model 1 ###' >> ./results.txt
python align_viz.py -idx 0 -a_path ./IBM_Model1/model1.a >> results.txt
echo $'\n### Fast aligner ###' >> ./results.txt
python align_viz.py -idx 0 -a_path ./fast_align/forward.align >> results.txt

