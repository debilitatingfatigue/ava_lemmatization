#collecting terminal output
file.txt: lemmatizator.py
	python3 $< > $@
