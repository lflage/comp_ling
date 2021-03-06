# IBM Model 1 Implementation

## Initial instructions

This code was generated mainly using CLI. There are discriptive instructions bellow but you can also check the ```-h```.

To run these files correctly this folders must be on the same folder as the ```hw2``` folder of the original MTClass repository. The hw2 folder is in the zip file 

A report is provided, but to obtain it give the bash script ```get_report.sh``` the write and run permission.

The probabilities of french given english are stored as a dict. They are saved as file and amount to a size of 247M.

## Dependencies

python		3.9.7  
tqdm		4.62.3  

## Tree Structure
```
.
├── fast_align
│   └── fast_paralelize.py
├── hw2
│   ├── data
│   │   ├── hansards.a
│   │   ├── hansards.e
│   │   └── hansards.f
│   ├── align
│   ├── check-alignments
│   ├── README.md
│   └── score-alignments
├── IBM_Model1
│   ├── IBM_Model1_align.py
│   ├── IBM_Model1.py
├── align_viz.py
├── get_report.sh
├── README.md
└── results.txt
```
## How to Run

The probabilities table for French given English was created with 5 iterations of the Expectation Maximization Algorithm.
 
* Run the following command on the IBM_Model1 folder to create the probabilites dictionary 
```python IBM_Model1.py 5```

* Run the ```IBM_Model1_aligns.py``` file to obtain the alignments. The output file is ```model1.a```

* Change directories to the root directory of this repo and run the score-alignments file to check the scores.

* A small script was created to adapt the hansards files to be used as input for the fast_align model. To use it, simply change to the ```fast_align``` folder and run the file ```fast_paralelize.py```

* On the same folder run the fast aligner with the following arguments to generate the fast.a file containing its alignments:
```fast_align -i fast_paralelized -d -o -v -r > fast.a```

* Optional: Run the ```get_report.sh``` to create the ```Report.txt``` file containing the scores and the alignment comparisons. To do this give the file write and run permissions befor running it: ```chmod 777 get_report.sh```


## Runtimes

These runtimes were obtained using the ```tqdm``` library, on the most costly iterations.

* 'python IBM_Model1.py 5' - 09min03s
* 'python IBM_Model1_align.py' - 00min34s
