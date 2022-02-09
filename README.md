# kolist_from_text
This script parses a text file with a "copy paste" list of KO numbers from a specific KEGG BRITE database entry into a list of only the numbers separated by commas.

## DESCRIPTION

If run with -h|--help new_job.py produces the following:

```
$ ./text_to_kolist.py -h
usage: text_to_kolist.py [-h] [-o FILE] FILE

Extract the KO numbers from KEGG Brite entry

positional arguments:
  FILE                  The input text file

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output) (default: <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>)
```

The only required argument is the positional **input file**. This file should be a simplified .txt with a copy paste of the KEGG BRITE entry.

For example: 
```
crispr_raw.txt
 K15342  cas1; CRISP-associated protein Cas1
     K09951  cas2; CRISPR-associated protein Cas2
   Type I CRISPR-Cas system
     Type I signiture cas proteins
       K07012  cas3; CRISPR-associated endonuclease/helicase Cas3 [EC:3.1.-.- 5.6.2.4]
       K07475  cas3; CRISPR-associated endonuclease Cas3-HD [EC:3.1.-.-]
     Subtype I-A factors
       K19085  csa1; CRISPR-associated protein Csa1
       K19074  csa2; CRISPR-associated protein Csa2
       K07725  csa3; CRISPR-associated protein Csa3
       K19086  csa4, cas8a2; CRISPR-associated protein Csa4
       K19087  csa5; CRISPR-associated protein Csa5
       K19088  cst1, cas8a; CRISPR-associated protein Cst1
       K19075  cst2, cas7; CRISPR-associated protein Cst2
       K07464  cas4; CRISPR-associated exonuclease Cas4 [EC:3.1.12.1]
       K19089  cas5a_b_c; CRISPR-associated protein Cas5a/b/c
       K19090  cas5t; CRISPR-associated protein Cas5t
```

The script will find all instances of KO number (which takes the format: K#####) and output them as a table with one column. By default this script gives the output in the command line. By using the argument **-o --output** you can specify the name of the output file to save the output in. 



### Make sure you input a plain text. This is an example: 

1. Access the KEGG BRITE page for the "09182 Protein families: genetic information processing" system [here](https://www.genome.jp/kegg-bin/get_htext?htext=ko00001.keg&query=K15342). 
    (you can also download the htext)
2. Un collapse all the tabs and copy paste the entire list of KO numbers to a text file. Make sure that you are using plain text (you can do so in TextEdit for example by going to the Menu Bar > Format > Make Plain Text)

3. Save the text file.

